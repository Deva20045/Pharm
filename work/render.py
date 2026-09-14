#!/usr/bin/env python3
"""Render book pages from the source PDF to PNGs for transcription.

Source mapping (from PROGRESS.md):
- uploads/Pharmacology Marrow E8 (1).pdf = 298 pdf pages = book pages 1-293
- PAGE-OFFSET FORMULA:
      book page = pdf page - 5      (pdf 1 cover; pdf 2-5 contents; pdf 6 = book p1)
      pdf page  = book page + 5

Usage: python3 work/render.py <book_page_a> <book_page_b> [dpi=100]
Output: work/pages/bNNN.png (NNN = zero-padded book page)
"""
import glob, os, sys

def find_pdf():
    for p in ("uploads/Pharmacology*Marrow*E8*.pdf", "uploads/*.pdf"):
        g = sorted(glob.glob(p))
        if g:
            return g[0]
    return None

def render(a, b, dpi=100):
    try:
        import fitz  # PyMuPDF
    except ImportError:
        os.system("pip3 install -q pymupdf || pip3 install -q --break-system-packages pymupdf")
        import fitz
    os.makedirs("work/pages", exist_ok=True)
    pdf = find_pdf()
    if not pdf or not os.path.exists(pdf):
        print("!! source PDF not found — expected uploads/Pharmacology Marrow E8 (1).pdf")
        return
    doc = fitz.open(pdf)
    for book in range(a, b + 1):
        page = book + 5                      # book = pdf - 5
        if page < 1 or page > doc.page_count:
            print(f"!! b{book:03d}: pdf page {page} out of range in {pdf}")
            continue
        pix = doc[page - 1].get_pixmap(dpi=dpi)
        out = f"work/pages/b{book:03d}.png"
        pix.save(out)
        print(f"b{book:03d} <- {os.path.basename(pdf)} pdf p{page} -> {out} ({pix.width}x{pix.height})")
    doc.close()

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(__doc__); sys.exit(1)
    render(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]) if len(sys.argv) > 3 else 100)
