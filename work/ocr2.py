#!/usr/bin/env python3
"""OCR a crop with preprocessing (upscale + adaptive threshold), which reads the
handwritten Marrow notes better than the raw scan.

Usage: python3 work/ocr2.py <image.png> [scale=2] [--inv]
"""
import sys
import cv2
import numpy as np
from rapidocr_onnxruntime import RapidOCR

path = sys.argv[1]
scale = float(sys.argv[2]) if len(sys.argv) > 2 else 2.0
img = cv2.imread(path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
big = cv2.resize(gray, None, fx=scale, fy=scale, interpolation=cv2.INTER_CUBIC)
thr = cv2.adaptiveThreshold(big, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                            cv2.THRESH_BINARY, 31, 12)
out = "/tmp/pre.png"
cv2.imwrite(out, thr)
ocr = RapidOCR()
res, _ = ocr(out)
print("# preprocessed", thr.shape, "boxes", len(res or []))
rows = []
for box, text, score in (res or []):
    ys = [p[1] for p in box]
    xs = [p[0] for p in box]
    rows.append((min(ys), min(xs), text, round(score, 2)))
rows.sort()
for y, x, t, s in rows:
    print(f"{int(y/scale):5d} {int(x/scale):5d} | {t}   [{s}]")
