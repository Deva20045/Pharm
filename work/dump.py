#!/usr/bin/env python3
"""Dump every OCR box of an image as "y% x% | text" (no row merging).

Useful when work/ocr.py's row grouping merges two lines that sit close together.

Usage: python3 work/dump.py <image.png>
"""
import sys
import cv2
from rapidocr_onnxruntime import RapidOCR

path = sys.argv[1]
img = cv2.imread(path)
H, W = img.shape[:2]
res, _ = RapidOCR()(path)
rows = []
for box, text, score in (res or []):
    ys = [p[1] for p in box]
    xs = [p[0] for p in box]
    rows.append((sum(ys) / 4, min(xs), text, score))
rows.sort()
print(f"# {path} {W}x{H} boxes={len(rows)}")
for y, x, t, s in rows:
    print(f"{int(y/H*100):3d}% {int(x/W*100):3d}% | {t}   [{s:.2f}]")
