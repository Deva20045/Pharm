#!/usr/bin/env python3
"""Crop a book page by PIXEL coordinates given in 300-dpi space, render at any dpi
and (optionally) OCR it.

Usage: python3 work/crop3.py <book_page> <x0> <y0> <x1> <y1> [dpi=500] [--ocr] [--plain]

Coordinates are in the 300-dpi render frame (page ~2479 x 3506 px), so they can be
read straight off `python3 work/ocr.py <page> 300` output.
"""
import sys
import os
import pymupdf
os.makedirs("work/pages", exist_ok=True)

args = sys.argv[1:]
do_ocr = "--ocr" in args
args = [a for a in args if a != "--ocr"]
book, x0, y0, x1, y1 = int(args[0]), *[float(v) for v in args[1:5]]
dpi = int(args[5]) if len(args) > 5 else 500

doc = pymupdf.open("uploads/Pharmacology Marrow E8 (1).pdf")
pg = doc[book + 5 - 1]
r = pg.rect
W, H = r.width, r.height
sx, sy = 300 / 72, 300 / 72          # px per pt in the reference frame
ref_w, ref_h = W * sx, H * sy
clip = pymupdf.Rect(r.x0 + x0 / ref_w * W, r.y0 + y0 / ref_h * H,
                    r.x0 + x1 / ref_w * W, r.y0 + y1 / ref_h * H)
pix = pg.get_pixmap(dpi=dpi, clip=clip)
out = "work/pages/crop.png"
pix.save(out)
print(f"book p{book} crop ({x0},{y0})-({x1},{y1}) @ {dpi} -> {out} {pix.width}x{pix.height}")
if do_ocr:
    sys.argv = ["ocr.py", out] + (["--plain"] if "--plain" in sys.argv else [])
    import ocr
    ocr.ocr_file(out)
