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

## Interpreter and package lock

- Preferred OCR interpreter on this machine: `py -3.12`
- Do not default to Python `3.14` for PaddleOCR work in this package
- Python `3.12` version: `3.12.10`
- `paddleocr`: `3.2.0`
- `paddlepaddle`: `3.1.1`
- `paddlex`: `3.2.1`

See also:

- `process/ocr-environment.md`

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
- `PaddleOCR`: calibration-usable in Python `3.12` with `PP-OCRv4`; default `PP-OCRv5` still crashes on this machine

### Tesseract language status

System `tesseract` was present but only had `eng` and `osd` in system `tessdata`.

To make East Asian use possible without changing the system install, local workspace models were added under:

- `ocr/T1/tessdata/chi_tra.traineddata`
- `ocr/T1/tessdata/chi_tra_vert.traineddata`

This lets the edition run `tesseract` with local traineddata even if the system install remains minimal.

These were installed after Stage 2A page preparation and before the full OCR pass.

Additional probe note:

- `chi_tra_vert` was re-tested on commentary pages `T1-p007` and `T1-p008` with `--psm 5` and `--psm 6`
- the vertical model performed materially worse than the witness-local `chi_tra` path on this witness
- no full vertical Tesseract pass was saved

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
- Saved output:
  - `ocr/T1/ocr/tesseract/T1-p001.txt`

### EasyOCR

- Environment: Python `3.14`
- Probe page: `T1-p001`
- Result: runnable, but probe output is sparse and low-quality on this page
- Saved outputs:
  - `ocr/T1/ocr/easyocr/T1-p001.json`
  - `ocr/T1/ocr/easyocr/T1-p001.txt`
  - `ocr/T1/ocr/easyocr/run-summary.json`

### PaddleOCR

- Environment: Python `3.12`
- Probe page: `T1-p001`
- Initial failing stack:
  - `paddleocr 3.4.1`
  - `paddlepaddle 3.3.1`
  - `paddlex 3.4.3`
  - default `PaddleOCR(lang='ch')`
  - failure class: Paddle runtime `NotImplementedError`
  - failure signature:
    - `(Unimplemented) ConvertPirAttribute2RuntimeAttribute not support [pir::ArrayAttribute<pir::DoubleAttribute>]`
- Attempted mitigations that did not fix the initial failure:
  - `FLAGS_use_mkldnn=0`
  - `FLAGS_use_mkldnn=False`
- Working stack after downgrade:
  - `paddleocr 3.2.0`
  - `paddlepaddle 3.1.1`
  - `paddlex 3.2.1`
- Default `PP-OCRv5` status after downgrade:
  - constructor succeeds
  - prediction still fails with Windows fatal exception `access violation`
- Working calibration configuration:
  - `PaddleOCR(lang='ch', ocr_version='PP-OCRv4', device='cpu', enable_hpi=False, enable_mkldnn=False, cpu_threads=1)`
  - result: successful on `T1-p001`
  - saved outputs:
    - `ocr/T1/ocr/paddleocr-ppocrv4/T1-p001.json`
    - `ocr/T1/ocr/paddleocr-ppocrv4/T1-p001.txt`
    - `ocr/T1/ocr/paddleocr-ppocrv4/run-summary.json`
- Full-pass status:
  - the same `PP-OCRv4` configuration has now completed a saved full pass across all `83` `T1` pages
  - resumable output summary:
    - `ocr/T1/ocr/paddleocr-ppocrv4/run-summary-full.json`
  - extraction note:
    - the saved Paddle `.txt` companions were empty on this machine even when the JSON contained OCR text
    - extracted text companions have now been derived from `res.rec_texts` into:
      - `ocr/T1/ocr/paddleocr-ppocrv4/extracted-text/`

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
  - `tesseract`: full-pass usable once pointed at witness-local `chi_tra` traineddata
  - `EasyOCR`: calibration output saved on `T1-p001`
  - `PaddleOCR`: full-pass usable with `PP-OCRv4`; default `PP-OCRv5` still crashes on this machine
- The same-page calibration set now exists across all four engines on `T1-p001`.
- A focused Tesseract support batch now also exists for `T1-p005` to `T1-p010` under:
  - `ocr/T1/ocr/tesseract-early-support/`
- A full Tesseract pass now also exists for all `83` `T1` pages under:
  - `ocr/T1/ocr/tesseract-full-pass/`
- Tesseract environment note:
  - a first full-pass attempt failed because the system install did not resolve `chi_tra.traineddata`
  - the successful rerun used `TESSDATA_PREFIX=ocr/T1/tessdata/`
- A Paddle reading-order support derivative now also exists for `T1-p005` to `T1-p010` under:
  - `ocr/T1/ocr/paddleocr-ppocrv4/column-ordered-text/`
- Column-order heuristic:
  - sort detection boxes by x-center descending, then y-center ascending
  - use as support only on vertical pages where raw extraction order appears unstable
- The no-text tail pages likely represent non-body or blank/end material, but that has not yet been classified.
- No editorial correction has happened yet.
- No copy-text challenge is triggered by this run alone.

## Next step

Move into manual correction using the normalized `T1` spine while preserving:

- RapidOCR full-pass outputs
- PaddleOCR `PP-OCRv4` full-pass outputs
- the four-engine `T1-p001` comparison slice
