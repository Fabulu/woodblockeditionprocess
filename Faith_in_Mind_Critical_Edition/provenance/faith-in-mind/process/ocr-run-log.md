# OCR Run Log: Faith in Mind

Date: 2026-04-14  
Status: pass 1 started  
Scope: `T1` first OCR engine pass

## Environment check

- `python`: available
- `fitz` / PyMuPDF: available
- `pypdf`: available
- `pikepdf`: available
- `tesseract`: not installed at run start
- `magick`: not installed at run start

## Installed for this stage

- `rapidocr_onnxruntime`
- `onnxruntime`
- `opencv-python-headless`
- `easyocr`
- `paddleocr` in a Python `3.12` side environment

## Four-engine loop status

Intended comparator loop for this edition:

- `tesseract`
- `RapidOCR`
- `PaddleOCR`
- `EasyOCR`

Current machine status:

- `tesseract`: available at `C:/Program Files/Tesseract-OCR/tesseract.exe`
- `RapidOCR`: available and already used for the full first pass
- `EasyOCR`: available and probe-runnable in the main Python `3.14` environment
- `PaddleOCR`: installed and importable in a Python `3.12` side environment, but still failing at runtime on this machine

### Tesseract language status

System `tesseract` was present but only had `eng` and `osd` in system `tessdata`.

To make East Asian use possible without changing the system install, local workspace models were added under:

- `ocr/T1/tessdata/chi_tra.traineddata`
- `ocr/T1/tessdata/chi_tra_vert.traineddata`

This lets the edition run `tesseract` with local traineddata even if the system install remains minimal.

These were installed after Stage 2A page preparation and before the full OCR pass.

## Page preparation inputs

- Witness: `T1`
- Source file: `Faith_in_Mind_Korea_Commons/CNTS-00047968260_faith_in_mind.pdf`
- SHA-256: `B08ED6F3128C0154C9C164B72884ED5050BF68E70B9E2B6CAA2C50F14B0C5C31`
- Page count: `83`
- Render engine: `PyMuPDF`
- Render DPI: `200`
- Output page images: `ocr/T1/page-images/`
- Page map: `ocr/T1/page-map.csv`

## Probe run

- Engine: `rapidocr_onnxruntime`
- Probe pages:
  - `T1-p001`
  - `T1-p002`
- Outcome:
  - text extracted on both probe pages
  - OCR output is noisy but usable enough to justify a full first pass
- Important note:
  - an initial terminal print failed because PowerShell tried to emit Chinese text through a non-UTF-8 console path
  - the OCR itself did not fail

## Additional engine probes

### Tesseract

- Binary used: `C:/Program Files/Tesseract-OCR/tesseract.exe`
- Local language model: `chi_tra_vert`
- Probe page: `T1-p001`
- Result: runnable, but output is much noisier than RapidOCR on this page

### EasyOCR

- Environment: Python `3.14`
- Probe page: `T1-p001`
- Result: runnable, but probe output is sparse and low-quality on this page

### PaddleOCR

- Environment: Python `3.12`
- Probe page: `T1-p001`
- Result: not yet runnable on this machine
- Failure class: Paddle runtime `NotImplementedError` during prediction
- Current interpretation:
  - the engine is installed
  - model assets were cached
  - the runtime still fails before useful OCR is returned
- Next action:
  - keep PaddleOCR in the intended four-engine loop
  - log it as a currently failing comparator until the runtime issue is solved

## Full OCR pass 1

- Engine: `rapidocr_onnxruntime`
- Input directory: `ocr/T1/page-images/`
- Raw output directory: `ocr/T1/ocr/rapidocr/`
- Output types:
  - page-level `.json`
  - page-level `.txt`
  - `run-summary.json`

### Summary

- Total pages processed: `83`
- Pages with extracted text: `80`
- Pages with no extracted text: `3`
- No-text pages:
  - `T1-p081`
  - `T1-p082`
  - `T1-p083`
- Elapsed time: `356.61` seconds

## Interpretation

- The first OCR pass is good enough to continue into normalization.
- The intended four-engine loop is not yet fully healthy on this machine.
- Current practical loop status is:
  - `RapidOCR`: full-pass usable
  - `tesseract`: probe-usable
  - `EasyOCR`: probe-usable
  - `PaddleOCR`: installed but runtime-failing
- The no-text tail pages likely represent non-body or blank/end material, but that has not yet been classified.
- No editorial correction has happened yet.
- No copy-text challenge is triggered by this run alone.

## Next step

Move to Stage 2C normalization while preserving all raw page-level OCR outputs.
