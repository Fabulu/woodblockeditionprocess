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

Current OCR status:

- tranche 1 four-engine baseline is complete for `YJG-W16`, `YJG-W17`, and `YJG-W22`
- the remaining render-prepared held first-tier tranche is now also complete for `YJG-W2`, `YJG-W4C`, `YJG-W4F`, `YJG-W4G`, `YJG-W8`, and `YJG-W9`
- `YJG-W21` remains blocked honestly because the held PDF still opens locally as PDF `1.4` with `0` renderable pages
- `YJG-W4G` PaddleOCR required a page-specific local fallback without word boxes on `page-0008` and `page-0067` after `return_word_box=True` hit a reproducible engine `KeyError`
- corrected true poem openings for those active exact witnesses now begin on `page-0007`
- the package is no longer at pure OCR startup; the remaining first-tier OCR queue is exhausted and the next necessary work is post-OCR editorial comparison / consolidation

For the live phase, read:

- `provenance/song-of-enlightenment/process/current-state.md`
- `provenance/song-of-enlightenment/process/ocr-tranche-1-manifest.md`
- `provenance/song-of-enlightenment/process/ocr-consensus-log.md`
