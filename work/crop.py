#!/usr/bin/env python3
"""Render a magnified CROP of a book page -> work/pages/crop.png
Usage: python3 work/crop.py <book_page> <x0%> <y0%> <x1%> <y1%> [dpi=300]
"""
import sys, fitz
bp, x0, y0, x1, y1 = int(sys.argv[1]), *[float(v)/100 for v in sys.argv[2:6]]
dpi = int(sys.argv[6]) if len(sys.argv) > 6 else 300
doc = fitz.open("uploads/Pharmacology Marrow E8 (1).pdf")
pg = doc[bp + 5 - 1]
r = pg.rect
clip = fitz.Rect(r.x0 + x0*r.width, r.y0 + y0*r.height, r.x0 + x1*r.width, r.y0 + y1*r.height)
pix = pg.get_pixmap(dpi=dpi, clip=clip)
pix.save("work/pages/crop.png")
print(f"book p{bp} crop {x0}-{x1}% x {y0}-{y1}% -> work/pages/crop.png {pix.width}x{pix.height}")
