# OCR Workspace

This directory holds package-local OCR outputs for `song-of-enlightenment`.

Layout:

- `{witness_id}/ocr/{engine}/`
  - per-page `.json`
  - per-page `.txt`
  - `run-summary.json`

Current tranche-1 image witnesses:

- `YJG-W16`
- `YJG-W17`
- `YJG-W22`

The initial startup uses:

- `rapidocr`
- `paddleocr`
- `easyocr`
- `tesseract`

The OCR runner is:

- `scripts/run_witness_ocr.py`

The tranche launcher is:

- `scripts/run_tranche1_ocr.py`
