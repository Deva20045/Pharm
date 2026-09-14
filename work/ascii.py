#!/usr/bin/env python3
"""Render an image crop as ASCII art - a fallback "view" when no vision is available.

Usage: python3 work/ascii.py <image.png> [cols=160] [--gamma 1.0]
"""
import sys
import cv2

path = sys.argv[1]
cols = int(sys.argv[2]) if len(sys.argv) > 2 else 160
gamma = 1.0
if "--gamma" in sys.argv:
    gamma = float(sys.argv[sys.argv.index("--gamma") + 1])

img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
h, w = img.shape
rows = max(1, int(cols * h / w * 0.5))
small = cv2.resize(img, (cols, rows), interpolation=cv2.INTER_AREA)
small = cv2.normalize(small, None, 0, 255, cv2.NORM_MINMAX)
if gamma != 1.0:
    small = cv2.pow(small / 255.0, gamma) * 255
small = small.astype("uint8")
ramp = " .:-=+*#%@"
for r in small:
    print("".join(ramp[min(len(ramp) - 1, int((255 - v) / 256 * len(ramp)))] for v in r))
