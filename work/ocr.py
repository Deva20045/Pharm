#!/usr/bin/env python3
"""OCR helper for the scanned Marrow Pharmacology E8 book (no text layer).

Renders a book page from uploads/*.pdf and runs RapidOCR (PP-OCRv4, bundled
models) on it, then re-orders the detected boxes into reading order:

  * boxes are grouped into rows by y-centre (tolerance scales with box height)
  * if the page has a clear vertical gutter (an x-band with no box centres over
    most rows) the page is treated as two/three columns and each column is read
    top-to-bottom before moving to the next column
  * output: "  y | x  | text" lines, or plain text with --plain

Usage:
  python3 work/ocr.py <book_page> [dpi=200] [--plain] [--cols N]
"""
import sys


def get_ocr():
    from rapidocr_onnxruntime import RapidOCR
    return RapidOCR()


def render(book, dpi=200):
    import pymupdf
    doc = pymupdf.open("uploads/Pharmacology Marrow E8 (1).pdf")
    pg = doc[book + 5 - 1]
    pix = pg.get_pixmap(dpi=dpi)
    path = f"/tmp/ocr_{book}_{dpi}.png"
    pix.save(path)
    return path


def boxes(book, dpi=200):
    ocr = get_ocr()
    res, _ = ocr(render(book, dpi))
    out = []
    for box, text, score in (res or []):
        xs = [p[0] for p in box]
        ys = [p[1] for p in box]
        out.append({"x0": min(xs), "x1": max(xs), "y0": min(ys), "y1": max(ys),
                    "xc": sum(xs) / 4, "yc": sum(ys) / 4,
                    "h": max(ys) - min(ys), "t": text, "s": score})
    return out


def columns(bs, dpi, width):
    """Return list of (x0, x1) column bands, or [(0,width)] for single column."""
    if len(bs) < 8:
        return [(0, width)]
    best = None
    for gx in range(int(width * 0.28), int(width * 0.72), 12):
        band = (gx, gx + 22)
        hits = sum(1 for b in bs if band[0] <= b["xc"] <= band[1])
        if hits == 0:
            # strength = how many rows straddle / cross this gutter
            cross = sum(1 for b in bs if b["x0"] < band[0] and b["x1"] > band[1])
            rows_with_left = len({round(b["yc"] / 20) for b in bs if b["xc"] < band[0]})
            rows_with_right = len({round(b["yc"] / 20) for b in bs if b["xc"] > band[1]})
            score = min(rows_with_left, rows_with_right) - cross
            if best is None or score > best[0]:
                best = (score, gx)
    if best and best[0] >= 6:
        g = best[1]
        return [(0, g), (g, width)]
    return [(0, width)]


def order(bs, dpi, width, cols=None):
    if cols == 1:
        bands = [(0, width)]
    elif cols:
        step = width / cols
        bands = [(i * step, (i + 1) * step) for i in range(cols)]
    else:
        bands = columns(bs, dpi, width)
    lines = []
    for (a, b) in bands:
        sub = [x for x in bs if a <= x["xc"] < b]
        sub.sort(key=lambda x: x["yc"])
        rows, cur, ref = [], [], None
        for box in sub:
            tol = max(box["h"] * 0.65, 8)
            if ref is None or abs(box["yc"] - ref) <= tol:
                cur.append(box)
                ref = sum(x["yc"] for x in cur) / len(cur)
            else:
                rows.append(sorted(cur, key=lambda x: x["x0"]))
                cur, ref = [box], box["yc"]
        if cur:
            rows.append(sorted(cur, key=lambda x: x["x0"]))
        for r in rows:
            y = min(x["y0"] for x in r)
            x = min(x["x0"] for x in r)
            txt = "  |  ".join(x["t"] for x in r)
            lines.append((y, x, txt))
    lines.sort()
    return lines


def ocr_file(path, cols=None, plain=False):
    """OCR an existing image file (e.g. a crop) and print it in reading order."""
    import cv2
    img = cv2.imread(path)
    width = img.shape[1]
    ocr = get_ocr()
    res, _ = ocr(path)
    bs = []
    for box, text, score in (res or []):
        xs = [p[0] for p in box]
        ys = [p[1] for p in box]
        bs.append({"x0": min(xs), "x1": max(xs), "y0": min(ys), "y1": max(ys),
                   "xc": sum(xs) / 4, "yc": sum(ys) / 4,
                   "h": max(ys) - min(ys), "t": text, "s": score})
    lines = order(bs, 0, width, cols)
    print(f"# {path} {img.shape[1]}x{img.shape[0]} boxes={len(bs)}")
    for y, x, t in lines:
        print(t if plain else f"{int(y):5d} {int(x):5d} | {t}")
    return lines


def main():
    args = [a for a in sys.argv[1:]]
    plain = "--plain" in args
    args = [a for a in args if a != "--plain"]
    cols = None
    if "--cols" in args:
        i = args.index("--cols")
        cols = int(args[i + 1])
        del args[i:i + 2]
    if args and args[0].endswith((".png", ".jpg", ".jpeg")):
        ocr_file(args[0], cols, plain)
        return
    book = int(args[0])
    dpi = int(args[1]) if len(args) > 1 else 200
    import pymupdf
    doc = pymupdf.open("uploads/Pharmacology Marrow E8 (1).pdf")
    width = doc[book + 5 - 1].rect.width * dpi / 72
    bs = boxes(book, dpi)
    lines = order(bs, dpi, width, cols)
    print(f"# book p{book} dpi={dpi} boxes={len(bs)}")
    for y, x, t in lines:
        if plain:
            print(t)
        else:
            print(f"{int(y):5d} {int(x):5d} | {t}")


if __name__ == "__main__":
    main()
