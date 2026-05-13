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
- corrected true poem openings for those active exact witnesses now begin on `page-0007`
- the package is no longer at pure OCR startup; it is in exact-witness comparison/transcription

For the live phase, read:

- `provenance/song-of-enlightenment/process/current-state.md`
- `provenance/song-of-enlightenment/process/ocr-tranche-1-manifest.md`
- `provenance/song-of-enlightenment/process/ocr-consensus-log.md`
