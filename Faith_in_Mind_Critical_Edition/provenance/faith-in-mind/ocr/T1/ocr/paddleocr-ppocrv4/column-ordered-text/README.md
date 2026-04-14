# Paddle Column-Ordered Support Text

Date: 2026-04-15
Status: support derivative

These files are derived from saved PaddleOCR `PP-OCRv4` JSON outputs for the active early-prose slice.

They do not claim to be correct running text.

They are a support view built from OCR geometry:

- detections are sorted by x-center descending
- ties are sorted by y-center ascending

Purpose:

- give the editor another non-image support witness on vertical pages
- reduce obvious reading-order noise in the raw extracted Paddle text
- help judge whether a noisy line is an OCR-recognition problem or an ordering problem

Current coverage:

- `T1-p001` to `T1-p083`

Use these as support only, not as silent replacement text.
