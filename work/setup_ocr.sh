#!/bin/sh
# Install the OCR stack used to transcribe the scanned Marrow book
# (the PDF has no text layer, so pages must be read as images).
#
#   sh work/setup_ocr.sh
#
# Packages: pymupdf (render pages), rapidocr-onnxruntime (PP-OCRv4, bundled models),
# opencv-python-headless (needs no libGL; the plain opencv-python wheel breaks import).
pip3 install --break-system-packages pymupdf rapidocr-onnxruntime
pip3 uninstall -y opencv-python opencv-contrib-python
pip3 install --break-system-packages --force-reinstall --no-deps opencv-python-headless
python3 -c "import pymupdf, rapidocr_onnxruntime, cv2; print('OCR stack OK')"
