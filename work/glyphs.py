#!/usr/bin/env python3
"""Render each glyph of an image crop as its own ASCII block.

Useful for reading a single stubborn word/character in the handwritten book when
line-level OCR is wrong: the crop is thresholded, ink columns are grouped into
glyphs, and every glyph is printed as its own small ASCII picture.

Usage: python3 work/glyphs.py <image.png> [cols_per_glyph=26] [--gap N]
"""
import sys
import cv2
import numpy as np

path = sys.argv[1]
CW = int(sys.argv[2]) if len(sys.argv) > 2 else 26
gap = 6
if "--gap" in sys.argv:
    gap = int(sys.argv[sys.argv.index("--gap") + 1])

img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
# upscale so thin strokes survive
img = cv2.resize(img, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC)
blur = cv2.GaussianBlur(img, (0, 0), 3)
thr = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                            cv2.THRESH_BINARY_INV, 61, 15)
# keep only the strongest ink
thr = cv2.morphologyEx(thr, cv2.MORPH_CLOSE, np.ones((5, 5), np.uint8))
cols = (thr > 0).sum(axis=0)
rows = (thr > 0).sum(axis=1)
ink_rows = np.where(rows > max(2, rows.max() * 0.05))[0]
if len(ink_rows) == 0:
    print("no ink found")
    sys.exit()
y0, y1 = ink_rows[0], ink_rows[-1] + 1
thr = thr[y0:y1]

cols = (thr > 0).sum(axis=0)
on = cols > max(1, cols.max() * 0.03)
groups, start = [], None
for i, v in enumerate(on):
    if v and start is None:
        start = i
    elif not v and start is not None:
        if i - start >= gap:
            groups.append((start, i))
        start = None
if start is not None:
    groups.append((start, len(on)))
# merge groups that are very close (part of one glyph)
merged = []
for g in groups:
    if merged and g[0] - merged[-1][1] < gap:
        merged[-1] = (merged[-1][0], g[1])
    else:
        merged.append(g)
print(f"# {path}: {len(merged)} glyph groups")
ramp = " .:-=+*#%@"
for gi, (a, b) in enumerate(merged):
    g = thr[:, a:b]
    h, w = g.shape
    rh = max(1, int(CW * h / w * 0.55))
    sm = cv2.resize(g, (CW, rh), interpolation=cv2.INTER_AREA)
    print(f"--- glyph {gi} (w={w}) ---")
    for r in sm:
        print("".join(ramp[min(9, int(v / 256 * 10))] for v in r))
