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
- A Paddle reading-order support derivative now also exists for all `83` `T1` pages under:
  - `ocr/T1/ocr/paddleocr-ppocrv4/column-ordered-text/`
- A focused closing-band Tesseract probe now also exists under:
  - `ocr/T1/ocr/tesseract-closing-probes/`
- `T4` has now been opened as the first comparison-control OCR package with:
  - `ocr/T4/metadata.json`
  - `ocr/T4/page-map.csv`
- Column-order heuristic:
  - sort detection boxes by x-center descending, then y-center ascending
  - use as support only on vertical pages where raw extraction order appears unstable
- Closing-band probe note:
  - alternate `chi_tra` Tesseract probes were run on `T1-p076` and `T1-p077`
  - the saved outputs were too noisy to resolve the `T1-p076.l01` ordering problem honestly
  - no visible text change was made from that probe
- The no-text tail pages likely represent non-body or blank/end material, but that has not yet been classified.
- No editorial correction has happened yet.
- No copy-text challenge is triggered by this run alone.

## Next step

Move into manual correction using the normalized `T1` spine while preserving:

- RapidOCR full-pass outputs
- PaddleOCR `PP-OCRv4` full-pass outputs
- the four-engine `T1-p001` comparison slice

## T4 comparison-control extension

Date: 2026-04-15
Scope: first OCR pass for the first comparison-control witness

### Witness inputs

- Witness: `T4`
- Source image set: `Faith_in_Mind_Kyoto_RB00009461_Shiburoku/images/`
- Page count: `28`
- Page map: `ocr/T4/page-map.csv`

### Page-role classification

- `T4-p001`: `title`
- `T4-p002` to `T4-p004`: `body`
- `T4-p005` to `T4-p026`: `other`
- `T4-p027`: `colophon`
- `T4-p028`: `title`

Classification note:

- the target `Faith in Mind` span appears confined to `T4-p002` through `T4-p004`
- the rest of the witness is wrapper, tail, or non-target anthology material and should not be treated as if it were part of the poem body

### Full OCR pass 1

- Engine: `rapidocr_onnxruntime`
- Input directory: `Faith_in_Mind_Kyoto_RB00009461_Shiburoku/images/`
- Raw output directory: `ocr/T4/ocr/rapidocr/`
- Output types:
  - page-level `.json`
  - page-level `.txt`
  - `run-summary.json`

Summary:

- total pages processed: `28`
- pages with extracted text: `25`
- pages with no extracted text: `3`
- no-text pages:
  - `T4-p008`
  - `T4-p027`
  - `T4-p028`
- error count: `0`
- elapsed time: `337.043` seconds

Interpretation:

- `T4` is now a real OCR-backed comparison witness rather than only a scaffold
- the RapidOCR pass is good enough to start first-pass witness comparison on the target `T4-p002` to `T4-p004` body span
- the no-text result on `T4-p027` is consistent with low-density tail matter rather than with a workflow failure
- `T4-p028` also appears to be wrapper/back-cover matter and can remain out of comparison focus unless a later structural question requires it

## T4 strict four-engine compliance extension

Date: 2026-04-15
Scope: record all four engine statuses before any stronger `T4` editorial use

### Comparator status block

- `RapidOCR`: full pass completed
  - output: `ocr/T4/ocr/rapidocr/`
  - summary: `ocr/T4/ocr/rapidocr/run-summary.json`
- `tesseract`: full pass completed with runtime warnings
  - binary: `C:/Program Files/Tesseract-OCR/tesseract.exe`
  - language model: `chi_tra`
  - `TESSDATA_PREFIX`: `ocr/T1/tessdata/`
  - output: `ocr/T4/ocr/tesseract-full-pass/`
  - summary: `ocr/T4/ocr/tesseract-full-pass/run-summary.json`
  - warning note:
    - six pages emitted scale warnings like `Image too small to scale!! (2x36 vs min width of 3)` while still producing `.txt` outputs
- `EasyOCR`: full pass completed
  - environment: Python `3.14`
  - languages: `ch_tra`, `en`
  - calibration output:
    - `ocr/T4/ocr/easyocr-calibration/`
  - full-pass output:
    - `ocr/T4/ocr/easyocr-full-pass/`
  - full-pass summary:
    - `ocr/T4/ocr/easyocr-full-pass/run-summary.json`
  - save-path note:
    - the engine itself ran during the first calibration attempt, but the initial serializer failed on NumPy `int32` values before output write
    - the normalized serializer was then used for the saved calibration and full-pass outputs
- `PaddleOCR`: full pass completed with the established `PP-OCRv4` machine-local path
  - environment: Python `3.12`
  - configuration:
    - `PaddleOCR(lang='ch', ocr_version='PP-OCRv4', device='cpu', enable_hpi=False, enable_mkldnn=False, cpu_threads=1)`
  - output: `ocr/T4/ocr/paddleocr-ppocrv4/`
  - summary: `ocr/T4/ocr/paddleocr-ppocrv4/run-summary-full.json`
  - derivative text support:
    - `ocr/T4/ocr/paddleocr-ppocrv4/extracted-text/`
  - machine note:
    - as on `T1`, the raw saved Paddle `.txt` companions are not the usable text layer on this machine
    - the recoverable text is in saved JSON under `res.rec_texts` and has been derived into `extracted-text/`

### Compliance interpretation

- `T4` now has a recorded status block for all four mandated engines
- `T4` is no longer undocumented at the OCR-comparator layer
- `T4` now has full-pass coverage from `RapidOCR`, `tesseract`, `PaddleOCR PP-OCRv4`, and `EasyOCR`
- the existing `T4` comparison table is no longer provisional merely for missing engine-status reasons
- machine quirks still matter:
  - `tesseract` produced scale warnings on tiny fragments
  - Paddle usable text still comes from `res.rec_texts` rather than the raw saved `.txt` companions

## T5 comparison-control extension

Date: 2026-04-15
Scope: full protocol opening for the second comparison-control witness

### Witness inputs

- Witness: `T5`
- Source image set: `Faith_in_Mind_Kyoto_RB00012929_Shiburoku/images/`
- Page count: `29`
- Page map: `ocr/T5/page-map.csv`

### Page-role classification

- `T5-p001` to `T5-p003`: `title`
- `T5-p004` to `T5-p006`: `body`
- `T5-p007` to `T5-p028`: `other`
- `T5-p029`: `title`

Classification note:

- the target `Faith in Mind` span appears confined to `T5-p004` through `T5-p006`
- the rest of the witness is wrapper or non-target anthology material and should not be treated as if it were part of the poem body

### Comparator status block

- `RapidOCR`: full pass completed
  - output: `ocr/T5/ocr/rapidocr/`
  - summary: `ocr/T5/ocr/rapidocr/run-summary.json`
  - no-text pages:
    - `T5-p014`
    - `T5-p015`
    - `T5-p027`
    - `T5-p029`
- `tesseract`: full pass completed with runtime warnings
  - binary: `C:/Program Files/Tesseract-OCR/tesseract.exe`
  - language model: `chi_tra`
  - `TESSDATA_PREFIX`: `ocr/T1/tessdata/`
  - output: `ocr/T5/ocr/tesseract-full-pass/`
  - summary: `ocr/T5/ocr/tesseract-full-pass/run-summary.json`
  - warning note:
    - `28` pages emitted scale warnings on very small fragments while still producing `.txt` outputs
- `EasyOCR`: full pass completed
  - environment: Python `3.14`
  - languages: `ch_tra`, `en`
  - output:
    - `ocr/T5/ocr/easyocr-full-pass/`
  - summary:
    - `ocr/T5/ocr/easyocr-full-pass/run-summary.json`
  - save-path note:
    - the first serialization attempt failed on NumPy `int32` values before any page outputs landed
    - the normalized serializer was then used for the saved full-pass outputs
- `PaddleOCR`: full pass completed with the established `PP-OCRv4` machine-local path
  - environment: Python `3.12`
  - configuration:
    - `PaddleOCR(lang='ch', ocr_version='PP-OCRv4', device='cpu', enable_hpi=False, enable_mkldnn=False, cpu_threads=1)`
  - output: `ocr/T5/ocr/paddleocr-ppocrv4/`
  - summary: `ocr/T5/ocr/paddleocr-ppocrv4/run-summary-full.json`
  - derivative text support:
    - `ocr/T5/ocr/paddleocr-ppocrv4/extracted-text/`
  - machine note:
    - as on `T1` and `T4`, the raw saved Paddle `.txt` companions are not the usable text layer on this machine
    - the recoverable text is in saved JSON under `res.rec_texts` and has been derived into `extracted-text/`

### Compliance interpretation

- `T5` now has a recorded status block for all four mandated engines
- `T5` is now a real OCR-backed comparison witness rather than only a queued metadata record
- `T5` now has full-pass coverage from `RapidOCR`, `tesseract`, `PaddleOCR PP-OCRv4`, and `EasyOCR`
- `T5` is no longer provisional merely for missing engine-status reasons
- machine quirks still matter:
  - `tesseract` produced widespread scale warnings on tiny fragments
  - Paddle usable text still comes from `res.rec_texts` rather than the raw saved `.txt` companions

## T2 comparison-control opening

Date: 2026-04-15
Witness: `T2`
Source package: `Sengcan_Faith_in_Mind_NDL_Shibulu/NDL2537640_shiburoku.pdf`

### Render and page-role basis

- render engine: `PyMuPDF`
- render output:
  - `ocr/T2/page-images/`
- render note:
  - the locked `T2` witness exists locally as a PDF rather than a downloaded image directory, so page images were rendered in-package before OCR work began
- page count:
  - `28`
- classified target span:
  - `T2-p003` to `T2-p005` = `body`
  - `T2-p001` to `T2-p002` = `title`
  - `T2-p006` = `colophon`
  - `T2-p007` to `T2-p027` = `other`
  - `T2-p028` = `title`

### RapidOCR

- status: full pass completed
- engine: `RapidOCR`
- output:
  - `ocr/T2/ocr/rapidocr/`
- summary:
  - `ocr/T2/ocr/rapidocr/run-summary.json`
- input basis:
  - `ocr/T2/ocr-input-120dpi/`
- machine note:
  - the full-resolution rendered PNG pages in `ocr/T2/page-images/` exceeded PIL's decompression-bomb guard on this workstation before `RapidOCR` could begin
  - a separate `120` DPI JPEG derivative set was therefore created and is explicitly logged as the OCR input basis for `T2`
- result:
  - `28` pages processed
  - `28` pages with text
  - `0` pages without text
  - `0` errors

### Tesseract

- status: full pass completed
- binary: `C:/Program Files/Tesseract-OCR/tesseract.exe`
- language model: `chi_tra`
- `TESSDATA_PREFIX`:
  - `ocr/T1/tessdata/`
- output:
  - `ocr/C3/ocr/tesseract-full-pass/`
- summary:
  - `ocr/C3/ocr/tesseract-full-pass/run-summary.json`
- input basis:
  - `ocr/C3/page-images/`
- result:
  - `63` pages processed
  - `63` pages with text
  - `0` pages without text
  - `0` errors
- warning note:
  - `C3` again produced the familiar Tesseract scale warnings on tiny fragments while still returning saved text output across the witness
- machine note:
  - the first long run exceeded the one-hour shell timeout before process exit
  - the saved file set and summary had already closed the witness at full `63/63` coverage, so no restart was needed

### Tesseract

- status: full pass completed
- binary: `C:/Program Files/Tesseract-OCR/tesseract.exe`
- language model: `chi_tra`
- `TESSDATA_PREFIX`:
  - `ocr/T1/tessdata/`
- output:
  - `ocr/T2/ocr/tesseract-full-pass/`
- summary:
  - `ocr/T2/ocr/tesseract-full-pass/run-summary.json`
- input basis:
  - `ocr/T2/ocr-input-120dpi/`
- result:
  - `28` pages processed
  - `28` pages with text
  - `0` pages without text
  - `0` errors
- warning note:
  - `T2-p027` emitted Tesseract scale warnings on very small fragments during the resumed closeout pass while still producing text output

### PaddleOCR

- status: full pass completed
- environment: Python `3.12`
- configuration:
  - `PaddleOCR(lang='ch', ocr_version='PP-OCRv4', device='cpu', enable_hpi=False, enable_mkldnn=False, cpu_threads=1)`
- output:
  - `ocr/T2/ocr/paddleocr-ppocrv4/`
- summary:
  - `ocr/T2/ocr/paddleocr-ppocrv4/run-summary-full.json`
- derivative text support:
  - `ocr/T2/ocr/paddleocr-ppocrv4/extracted-text/`
- input basis:
  - `ocr/T2/ocr-input-120dpi/`
- machine note:
  - as on `T1`, `T4`, and `T5`, the raw saved Paddle `.txt` companions are not the usable text layer on this machine
  - the recoverable text is in saved JSON and has been derived into `extracted-text/`
- result:
  - `28` pages processed
  - `28` success pages
  - `0` error pages

### EasyOCR

- status: full pass completed
- environment: Python `3.14`
- languages:
  - `ch_tra`
  - `en`
- output:
  - `ocr/T2/ocr/easyocr-full-pass/`
- summary:
  - `ocr/T2/ocr/easyocr-full-pass/run-summary.json`
- input basis:
  - `ocr/T2/ocr-input-120dpi/`
- result:
  - `28` pages processed
  - `28` pages with text
  - `0` no-text pages
  - `0` errors

## T3 comparison-control opening

Date: 2026-04-15
Witness: `T3`
Source package: `Faith_in_Mind_Sengcan_Kyoto_RB00016909/manifest.json`

### Page-role basis

- render engine: `source-images`
- page count:
  - `41`
- classified target span:
  - `T3-p034` to `T3-p036` = `body`
  - `T3-p001` to `T3-p003` = `title`
  - `T3-p004` to `T3-p033` = `other`
  - `T3-p037` to `T3-p039` = `other`
  - `T3-p040` to `T3-p041` = `title`
- machine note:
  - unlike `T4`, `T5`, and `T2`, the target `Faith in Mind` span in `T3` sits late in the anthology rather than near the opening leaves

### RapidOCR

- status: full pass completed
- engine: `RapidOCR`
- output:
  - `ocr/T3/ocr/rapidocr/`
- summary:
  - `ocr/T3/ocr/rapidocr/run-summary.json`
- input basis:
  - `Faith_in_Mind_Sengcan_Kyoto_RB00016909/images/`
- result:
  - `41` pages processed
  - `39` pages with text
  - `2` pages without text: `T3-p040`, `T3-p041`
  - `0` errors

### Tesseract

- status: full pass completed
- binary: `C:/Program Files/Tesseract-OCR/tesseract.exe`
- language model: `chi_tra`
- `TESSDATA_PREFIX`:
  - `ocr/T1/tessdata/`
- output:
  - `ocr/T3/ocr/tesseract-full-pass/`
- summary:
  - `ocr/T3/ocr/tesseract-full-pass/run-summary.json`
- input basis:
  - `Faith_in_Mind_Sengcan_Kyoto_RB00016909/images/`
- result:
  - `41` pages processed
  - `41` pages with text
  - `0` pages without text
  - `0` errors
- warning note:
  - wrapper, tail, and small-fragment regions emitted the familiar Tesseract scale warnings on many pages while still producing text output

### PaddleOCR

- status: full pass completed
- environment: Python `3.12`
- configuration:
  - `PaddleOCR(lang='ch', ocr_version='PP-OCRv4', device='cpu', enable_hpi=False, enable_mkldnn=False, cpu_threads=1)`
- output:
  - `ocr/T3/ocr/paddleocr-ppocrv4/`
- summary:
  - `ocr/T3/ocr/paddleocr-ppocrv4/run-summary-full.json`
- derivative text support:
  - `ocr/T3/ocr/paddleocr-ppocrv4/extracted-text/`
- input basis:
  - `Faith_in_Mind_Sengcan_Kyoto_RB00016909/images/`
- machine note:
  - this witness run saved the recoverable text under nested `res.rec_texts`, so the usable Paddle layer had to be derived from saved JSON into `extracted-text/`
  - as on `T1`, `T4`, `T5`, and `T2`, the raw saved Paddle `.txt` companions are not the stable text surface on this machine
- result:
  - `41` pages processed
  - `41` success pages
  - `0` error pages

### EasyOCR

- status: full pass completed
- environment: Python `3.14`
- languages:
  - `ch_tra`
  - `en`
- output:
  - `ocr/T3/ocr/easyocr-full-pass/`
- summary:
  - `ocr/T3/ocr/easyocr-full-pass/run-summary.json`
- input basis:
  - `Faith_in_Mind_Sengcan_Kyoto_RB00016909/images/`
- result:
  - `41` pages processed
  - `40` pages with text
  - `1` no-text page: `T3-p041`
  - `0` errors

### Compliance interpretation

- `T3` now has a recorded status block for all four mandated engines
- `T3` is now a real OCR-backed comparison witness rather than only a queued metadata record
- `T3` now has full-pass coverage from `RapidOCR`, `tesseract`, `PaddleOCR PP-OCRv4`, and `EasyOCR`
- `T3` is ready for bounded comparison use on `T3-p034` to `T3-p036`

## A1 comparison-control opening

Date: 2026-04-16
Witness: `A1`
Source package: `Faith_in_Mind_Waseda_Commons/WUL-bunko31_e1087_shiburoku.pdf`

### Render and page-role basis

- render engine: `PyMuPDF`
- render output:
  - `ocr/A1/page-images/`
- page count:
  - `42`
- source hash:
  - `53B7FB84D80767AE4008D3E883E76166C903C05FB9275383C6DE5FD3FC38036F`
- classified target span:
  - `A1-p001` to `A1-p002` = `title`
  - `A1-p003` to `A1-p008` = `body`
  - `A1-p009` to `A1-p041` = `other`
  - `A1-p042` = `title`
- machine note:
  - unlike `T2` and unlike the Kyoto image-root witnesses, `A1` enters the package from a locked Waseda PDF and required in-package rendering before OCR work could begin

### RapidOCR

- status: full pass completed
- engine: `RapidOCR`
- output:
  - `ocr/A1/ocr/rapidocr/`
- summary:
  - `ocr/A1/ocr/rapidocr/run-summary.json`
- input basis:
  - `ocr/A1/page-images/`
- result:
  - `42` pages processed
  - `37` pages with text
  - `5` pages without text:
    - `A1-p022`
    - `A1-p025`
    - `A1-p028`
    - `A1-p036`
    - `A1-p042`
  - `0` errors

### Tesseract

- status: full pass completed
- binary: `C:/Program Files/Tesseract-OCR/tesseract.exe`
- language model: `chi_tra`
- `TESSDATA_PREFIX`:
  - `ocr/T1/tessdata/`
- output:
  - `ocr/A1/ocr/tesseract-full-pass/`
- summary:
  - `ocr/A1/ocr/tesseract-full-pass/run-summary.json`
- input basis:
  - `ocr/A1/page-images/`
- result:
  - `42` pages processed
  - `42` pages with text
  - `0` pages without text
  - `0` errors
- warning note:
  - `A1` again produced the familiar Tesseract scale warnings on tiny fragments while still returning saved text output on every page

### PaddleOCR

- status: full pass completed
- environment: Python `3.12`
- configuration:
  - `PaddleOCR(lang='ch', ocr_version='PP-OCRv4', device='cpu', enable_hpi=False, enable_mkldnn=False, cpu_threads=1)`
- output:
  - `ocr/A1/ocr/paddleocr-ppocrv4/`
- summary:
  - `ocr/A1/ocr/paddleocr-ppocrv4/run-summary-full.json`
- derivative text support:
  - `ocr/A1/ocr/paddleocr-ppocrv4/extracted-text/`
- input basis:
  - `ocr/A1/page-images/`
- machine note:
  - as on `T1`, `T4`, `T5`, `T2`, and `T3`, the raw saved Paddle `.txt` companions are not the stable text surface on this machine
  - the recoverable text is in saved JSON and has been derived into `extracted-text/`
- result:
  - `42` pages processed
  - `42` success pages
  - `0` error pages

### EasyOCR

- status: full pass completed
- environment: Python `3.14`
- languages:
  - `ch_tra`
  - `en`
- output:
  - `ocr/A1/ocr/easyocr-full-pass/`
- summary:
  - `ocr/A1/ocr/easyocr-full-pass/run-summary.json`
- input basis:
  - `ocr/A1/page-images/`
- result:
  - `42` pages processed
  - `41` pages with text
  - `1` no-text page: `A1-p042`
  - `0` errors

### Compliance interpretation

- `A1` now has a recorded status block for all four mandated engines
- `A1` is now a real OCR-backed comparison witness rather than only a queued metadata record
- `A1` now has full-pass coverage from `RapidOCR`, `tesseract`, `PaddleOCR PP-OCRv4`, and `EasyOCR`
- `A1` is ready for bounded comparison use on `A1-p003` to `A1-p008`

## A2 comparison-control opening

Date: 2026-04-16
Witness: `A2`
Source package: `Faith_in_Mind_Waseda_Commons/WUL-bunko31_e1089_shiburokushou.pdf`

### Render and page-role basis

- render engine: `PyMuPDF`
- render output:
  - `ocr/A2/page-images/`
- page count:
  - `46`
- source hash:
  - `8C05FBD4CB87F1C45A2A46455C51A4DFD5A597C450DCF37068BEEA3B178F1BA9`
- classified target span:
  - `A2-p001` = `title`
  - `A2-p002` to `A2-p044` = `body`
  - `A2-p045` = `colophon`
  - `A2-p046` = `title`
- machine note:
  - `A2` is a longer Waseda derivative witness rather than a short poem-only excerpt, so its page-role pass treats most of the object as in-scope derivative body rather than trying to isolate only a tiny poem band

### RapidOCR

- status: full pass completed
- engine: `RapidOCR`
- output:
  - `ocr/A2/ocr/rapidocr/`
- summary:
  - `ocr/A2/ocr/rapidocr/run-summary.json`
- input basis:
  - `ocr/A2/page-images/`
- result:
  - `46` pages processed
  - `44` pages with text
  - `2` pages without text:
    - `A2-p045`
    - `A2-p046`
  - `0` errors
- machine note:
  - the first long run timed out before the non-resumable summary finished writing, so `RapidOCR` was rerun cleanly to preserve a complete final witness state

### Tesseract

- status: full pass completed
- binary: `C:/Program Files/Tesseract-OCR/tesseract.exe`
- language model: `chi_tra`
- `TESSDATA_PREFIX`:
  - `ocr/T1/tessdata/`
- output:
  - `ocr/A2/ocr/tesseract-full-pass/`
- summary:
  - `ocr/A2/ocr/tesseract-full-pass/run-summary.json`
- input basis:
  - `ocr/A2/page-images/`
- result:
  - `46` pages processed
  - `46` pages with text
  - `0` pages without text
  - `0` errors
- warning note:
  - `A2` again produced the familiar Tesseract scale warnings on tiny fragments while still returning saved text output on every page

### PaddleOCR

- status: full pass completed
- environment: Python `3.12`
- configuration:
  - `PaddleOCR(lang='ch', ocr_version='PP-OCRv4', device='cpu', enable_hpi=False, enable_mkldnn=False, cpu_threads=1)`
- output:
  - `ocr/A2/ocr/paddleocr-ppocrv4/`
- summary:
  - `ocr/A2/ocr/paddleocr-ppocrv4/run-summary-full.json`
- derivative text support:
  - `ocr/A2/ocr/paddleocr-ppocrv4/extracted-text/`
- input basis:
  - `ocr/A2/page-images/`
- machine note:
  - as on the earlier witnesses, the raw saved Paddle `.txt` companions are not the stable text surface on this machine
  - the recoverable text is in saved JSON and has been derived into `extracted-text/`
- result:
  - `46` pages processed
  - `46` success pages
  - `0` error pages

### EasyOCR

- status: full pass completed
- environment: Python `3.14`
- languages:
  - `ch_tra`
  - `en`
- output:
  - `ocr/A2/ocr/easyocr-full-pass/`
- summary:
  - `ocr/A2/ocr/easyocr-full-pass/run-summary.json`
- input basis:
  - `ocr/A2/page-images/`
- result:
  - `46` pages processed
  - `45` pages with text
  - `1` no-text page: `A2-p046`
  - `0` errors
- machine note:
  - `EasyOCR` required a resumable second pass because the first one-hour run closed at `A2-p032`, but the saved final state is now complete

### Compliance interpretation

- `A2` now has a recorded status block for all four mandated engines
- `A2` is now a real OCR-backed comparison witness rather than only a queued metadata record
- `A2` now has full-pass coverage from `RapidOCR`, `tesseract`, `PaddleOCR PP-OCRv4`, and `EasyOCR`
- `A2` is ready for bounded comparison use on the derivative body span under the current page-role pass

## A3 comparison-control opening

Date: 2026-04-16
Witness: `A3`
Source package: `Faith_in_Mind_NDL_Shiburokushou/NDL2537799_shiburokushou.pdf`

### Render and page-role basis

- render engine: `PyMuPDF`
- render output:
  - `ocr/A3/page-images/`
- page count:
  - `57`
- source hash:
  - `36CB2E2629DA410B9DF7DB4DA151DE2374029B262702EE300C7A4A9B08774F6D`
- classified target span:
  - `A3-p001` to `A3-p002` = `title`
  - `A3-p003` to `A3-p011` = `body`
  - `A3-p012` to `A3-p054` = `other`
  - `A3-p055` = `colophon`
  - `A3-p056` to `A3-p057` = `title`
- machine note:
  - `A3` is a larger NDL derivative anthology witness rather than a short poem-only excerpt
  - direct page review shows the visible Faith in Mind close on `A3-p011`, with later anthology material already underway by `A3-p012`

### RapidOCR

- status: full pass completed
- engine: `RapidOCR`
- output:
  - `ocr/A3/ocr/rapidocr/`
- summary:
  - `ocr/A3/ocr/rapidocr/run-summary.json`
- input basis:
  - `ocr/A3/ocr-input-120dpi/`
- result:
  - `57` pages processed
  - `57` pages with text
  - `0` pages without text
  - `0` errors
- machine note:
  - the rendered `200` DPI `A3` PNG pages are too large for practical full-res OCR on this workstation, so the saved run uses explicitly logged `120` DPI JPEG derivatives

### Tesseract

- status: full pass completed
- binary: `C:/Program Files/Tesseract-OCR/tesseract.exe`
- language model: `chi_tra`
- `TESSDATA_PREFIX`:
  - `ocr/T1/tessdata/`
- output:
  - `ocr/A3/ocr/tesseract-full-pass/`
- summary:
  - `ocr/A3/ocr/tesseract-full-pass/run-summary.json`
- input basis:
  - `ocr/A3/ocr-input-120dpi/`
- result:
  - `57` pages processed
  - `57` pages with text
  - `0` pages without text
  - `0` errors
- warning note:
  - `A3` again produced the familiar Tesseract scale warnings on tiny fragments while still returning saved text output on every page

### PaddleOCR

- status: full pass completed
- environment: Python `3.12`
- configuration:
  - `PaddleOCR(lang='ch', ocr_version='PP-OCRv4', device='cpu', enable_hpi=False, enable_mkldnn=False, cpu_threads=1)`
- output:
  - `ocr/A3/ocr/paddleocr-ppocrv4/`
- summary:
  - `ocr/A3/ocr/paddleocr-ppocrv4/run-summary-full.json`
- derivative text support:
  - `ocr/A3/ocr/paddleocr-ppocrv4/extracted-text/`
- input basis:
  - `ocr/A3/ocr-input-120dpi/`
- machine note:
  - as on the earlier witnesses, the raw saved Paddle `.txt` companions are not the stable text surface on this machine
  - the recoverable text is in saved JSON and has been derived into `extracted-text/`
- result:
  - `57` pages processed
  - `57` success pages
  - `0` error pages

### EasyOCR

- status: full pass completed
- environment: Python `3.14`
- languages:
  - `ch_tra`
  - `en`
- output:
  - `ocr/A3/ocr/easyocr-full-pass/`
- summary:
  - `ocr/A3/ocr/easyocr-full-pass/run-summary.json`
- input basis:
  - `ocr/A3/ocr-input-120dpi/`
- result:
  - `57` pages processed
  - `57` pages with text
  - `0` no-text pages
  - `0` errors
- machine note:
  - `EasyOCR` required a resumable second pass because the first one-hour run closed at `A3-p036`, but the saved final state is now complete

### Compliance interpretation

- `A3` now has a recorded status block for all four mandated engines
- `A3` is now a real OCR-backed comparison witness rather than only a queued metadata record
- `A3` now has full-pass coverage from `RapidOCR`, `tesseract`, `PaddleOCR PP-OCRv4`, and `EasyOCR`
- `A3` is ready for bounded comparison use on `A3-p003` to `A3-p011`

## C1 comparison-control opening

Date: 2026-04-16
Witness: `C1`
Source type: translation or reception control PDF

### Source verification

- source file:
  - `Faith_in_Mind_Translations_NDL/NDL906534_zaike_sotoshu_seiten.pdf`
- bytes:
  - `80,083,222`
- SHA-256:
  - `1F62970F85985D2488572B1D6FF80EF168F38562EEB3BB79F75B3B38BD6C2FA6`
- local validation:
  - readable on this machine with `pypdf`
  - `76` pages confirmed locally

### Render package

- output:
  - `ocr/C1/page-images/`
  - `ocr/C1/metadata.json`
  - `ocr/C1/page-map.csv`
- render engine:
  - `PyMuPDF`
- render DPI:
  - `150`
- render format:
  - `png`

### Page-role judgment

- classification:
  - `C1-p001` to `C1-p005` = `title`
  - `C1-p006` to `C1-p050` = `other`
  - `C1-p051` to `C1-p052` = `body`
  - `C1-p053` to `C1-p075` = `other`
  - `C1-p076` = `title`
- evidence note:
  - the contents page on `C1-p005` lists `信心銘和譯` at internal page `90`
  - internal pagination begins at PDF page `6`, where the image carries internal pages `1-2`
  - that mapping places the target opening on PDF page `51`
  - direct page review confirms `C1-p051` opens `信心銘和譯`, `C1-p052` continues it, and `C1-p053` has already moved into `證道歌和譯`

### Opening interpretation

- `C1` is now an opened in-package translation or reception control witness rather than a source-pinned metadata placeholder
- the isolated target span for future OCR and comparison work is `C1-p051` to `C1-p052`

## C1 strict four-engine compliance extension

Date: 2026-04-16
Scope: record all four engine statuses for the first translation or reception control witness before bounded comparison use

### RapidOCR

- status: full pass completed
- engine: `RapidOCR`
- output:
  - `ocr/C1/ocr/rapidocr/`
- summary:
  - `ocr/C1/ocr/rapidocr/run-summary.json`
- input basis:
  - `ocr/C1/page-images/`
- result:
  - `76` pages processed
  - `71` pages with text
  - `4` pages without text:
    - `C1-p002`
    - `C1-p074`
    - `C1-p075`
    - `C1-p076`
  - `0` errors

### Tesseract

- status: full pass completed
- binary: `C:/Program Files/Tesseract-OCR/tesseract.exe`
- language model: `chi_tra`
- `TESSDATA_PREFIX`:
  - `ocr/T1/tessdata/`
- output:
  - `ocr/C1/ocr/tesseract-full-pass/`
- summary:
  - `ocr/C1/ocr/tesseract-full-pass/run-summary.json`
- input basis:
  - `ocr/C1/page-images/`
- result:
  - `76` pages processed
  - `75` pages with text
  - `0` errors
- warning note:
  - `C1` again produced the familiar Tesseract scale warnings on tiny fragments while still returning saved text output across the witness

### PaddleOCR

- status: full pass completed
- environment: Python `3.12`
- configuration:
  - `PaddleOCR(lang='ch', ocr_version='PP-OCRv4', device='cpu', enable_hpi=False, enable_mkldnn=False, cpu_threads=1)`
- output:
  - `ocr/C1/ocr/paddleocr-ppocrv4/`
- summary:
  - `ocr/C1/ocr/paddleocr-ppocrv4/run-summary-full.json`
- derivative text support:
  - `ocr/C1/ocr/paddleocr-ppocrv4/extracted-text/`
- input basis:
  - `ocr/C1/page-images/`
- machine note:
  - as on the earlier witnesses, the raw saved Paddle `.txt` companions are not the stable text surface on this machine
  - the recoverable text is in saved JSON and has been derived into `extracted-text/`
- result:
  - `76` pages processed
  - `76` success pages
  - `0` error pages

### EasyOCR

- status: full pass completed
- environment: Python `3.14`
- languages:
  - `ch_tra`
  - `en`
- output:
  - `ocr/C1/ocr/easyocr-full-pass/`
- summary:
  - `ocr/C1/ocr/easyocr-full-pass/run-summary.json`
- input basis:
  - `ocr/C1/page-images/`
- result:
  - `76` pages processed
  - `73` pages with text
  - `3` no-text pages:
    - `C1-p002`
    - `C1-p074`
    - `C1-p075`
  - `0` errors
- machine note:
  - `EasyOCR` required a resumable targeted closeout to finish the final six pages after the initial long run timed out

### Compliance interpretation

- `C1` now has a recorded status block for all four mandated engines
- `C1` is now a real OCR-backed translation or reception control witness rather than only a queued metadata record
- `C1` now has full-pass coverage from `RapidOCR`, `tesseract`, `PaddleOCR PP-OCRv4`, and `EasyOCR`
- unlike `T2` and `A3`, `C1` did not require a derivative OCR-input basis on this machine; the direct rendered `page-images/` set remained the OCR input surface
- `C1` is ready for bounded comparison use on `C1-p051` to `C1-p052`, but its editorial force remains that of a translation or reception control rather than a direct character-repair witness

## C2 comparison-control opening

Date: 2026-04-17
Witness: `C2`
Source type: translation or reception control PDF

### Source verification

- source file:
  - `Faith_in_Mind_Translations_NDL/NDL961952_zenmon_sotoshuten_part3.pdf`
- bytes:
  - `71,377,423`
- SHA-256:
  - `1752E7775D80C9446DD66B21D7114032A586412B6CCE924CFEB31569E72D4684`
- local validation:
  - readable on this machine with `pypdf`
  - `100` pages confirmed locally

### Render package

- output:
  - `ocr/C2/page-images/`
  - `ocr/C2/metadata.json`
  - `ocr/C2/page-map.csv`
- render engine:
  - `PyMuPDF`
- render DPI:
  - `150`
- render format:
  - `png`
- machine note:
  - an initial full render timed out before finishing and a resumed PyMuPDF save hit a file-replace permission fault on `C2-p040.png`
  - the final witness render was closed by resuming with a safer write path that skipped complete existing images and wrote new PNG bytes directly for missing pages

### Page-role judgment

- classification:
  - `C2-p001` to `C2-p019` = `other`
  - `C2-p020` = `title`
  - `C2-p021` to `C2-p023` = `body`
  - `C2-p024` to `C2-p031` = `other`
  - `C2-p032` = `title`
  - `C2-p033` to `C2-p059` = `other`
  - `C2-p060` = `title`
  - `C2-p061` to `C2-p093` = `other`
  - `C2-p094` = `title`
  - `C2-p095` to `C2-p100` = `other`
- evidence note:
  - the local PDF exposes no searchable text layer, so the target span was isolated by direct page review of the rendered images rather than by PDF text extraction
  - `C2-p020` is the divider for `第七 支那諷詠部`
  - `C2-p021` opens `三祖大師信心銘` on the left page while the facing right page still carries section explanation
  - `C2-p022` is a full continuation spread of the target text
  - `C2-p023` carries `三祖信心銘終` on the right page while the facing left page has already moved into `洞山大師玄中銘`

### Opening interpretation

- `C2` is now an opened in-package translation or reception control witness rather than a source-pinned metadata placeholder
- the isolated image-level target span for future OCR and comparison work is `C2-p021` to `C2-p023`
- `C2-p021` and `C2-p023` are mixed-content boundary spreads and should remain documented that way in later comparison notes
- no OCR-compliance claim is made yet for `C2`

### RapidOCR

- status: full pass completed
- engine: `RapidOCR`
- output:
  - `ocr/C2/ocr/rapidocr/`
- summary:
  - `ocr/C2/ocr/rapidocr/run-summary.json`
- input basis:
  - `ocr/C2/page-images/`
- result:
  - `100` pages processed
  - `100` pages with text outputs on disk
  - `0` pages without text
  - `0` errors
- machine note:
  - the first long run hit shell timeout before witness closeout
  - a resumed witness-local runner completed the full set
  - the saved summary then needed repair because `C2-p018` was missing from `run-summary.json` even though its page outputs already existed on disk

### Tesseract

- status: full pass completed
- binary: `C:/Program Files/Tesseract-OCR/tesseract.exe`
- language model: `chi_tra`
- `TESSDATA_PREFIX`:
  - `ocr/T1/tessdata/`
- output:
  - `ocr/C2/ocr/tesseract-full-pass/`
- summary:
  - `ocr/C2/ocr/tesseract-full-pass/run-summary.json`
- input basis:
  - `ocr/C2/page-images/`
- result:
  - `100` pages processed
  - `100` pages with text
  - `0` pages without text
  - `0` errors
- warning note:
  - `C2` again produced the familiar Tesseract scale warnings on tiny fragments while still returning saved text output across the witness
- machine note:
  - the first long run exceeded the one-hour shell timeout at `97/100` saved page outputs
  - the resumed closeout completed the remaining pages without needing a restart

### PaddleOCR

- status: full pass completed
- environment: Python `3.12`
- configuration:
  - `PaddleOCR(lang='ch', ocr_version='PP-OCRv4', device='cpu', enable_hpi=False, enable_mkldnn=False, cpu_threads=1)`
- output:
  - `ocr/C2/ocr/paddleocr-ppocrv4/`
- summary:
  - `ocr/C2/ocr/paddleocr-ppocrv4/run-summary-full.json`
- derivative text support:
  - `ocr/C2/ocr/paddleocr-ppocrv4/extracted-text/`
- input basis:
  - `ocr/C2/page-images/`
- machine note:
  - the first long run exceeded the one-hour shell timeout at `27/100` saved page outputs
  - the resumed closeout completed the remaining pages
  - as on the earlier witnesses, the usable Paddle support is carried in the derived `extracted-text/` layer rather than being left implicit in raw JSON alone
- result:
  - `100` pages processed
  - `100` success pages
  - `0` error pages

### EasyOCR

- status: full pass completed
- environment: Python `3.14`
- languages:
  - `ch_tra`
  - `en`
- output:
  - `ocr/C2/ocr/easyocr-full-pass/`
- summary:
  - `ocr/C2/ocr/easyocr-full-pass/run-summary.json`
- input basis:
  - `ocr/C2/page-images/`
- result:
  - `100` pages processed
  - `100` pages with text
  - `0` no-text pages
  - `0` errors
- machine note:
  - the first long run exceeded the two-hour shell timeout at `30/100` saved page outputs
  - the resumed closeout completed the remaining pages
  - the saved summary then needed repair to recompute `pages_with_text` from the full resumed file set

### Compliance interpretation

- `C2` now has a recorded status block for all four mandated engines
- `C2` is now a real OCR-backed translation or reception control witness rather than only an opened metadata record
- `C2` now has full-pass coverage from `RapidOCR`, `tesseract`, `PaddleOCR PP-OCRv4`, and `EasyOCR`
- `C2` is ready for bounded comparison use on `C2-p021` to `C2-p023`, with `C2-p021` and `C2-p023` kept explicit as mixed-content boundary spreads

## C3 commentary-control opening

Date: 2026-04-17
Witness: `C3`
Source type: commentary control PDF

### Source verification

- source file:
  - `Faith_in_Mind_NDL_Commentaries/NDL823155_xinxinming_kowa.pdf`
- bytes:
  - `81,074,643`
- SHA-256:
  - `E87729A0233C58ECE07697C675AC371FBE695F7F6738905396F0955648454BA9`
- local validation:
  - readable on this machine with `pypdf`
  - `63` pages confirmed locally

### Render package

- output:
  - `ocr/C3/page-images/`
  - `ocr/C3/metadata.json`
  - `ocr/C3/page-map.csv`
- render engine:
  - `PyMuPDF`
- render DPI:
  - `150`
- render format:
  - `png`

### Page-role judgment

- classification:
  - `C3-p001` to `C3-p003` = `title`
  - `C3-p004` to `C3-p056` = `body`
  - `C3-p057` = `other`
  - `C3-p058` to `C3-p059` = `colophon`
  - `C3-p060` to `C3-p063` = `title`
- evidence note:
  - the local PDF does not expose a usable searchable text layer for clean span isolation, so the target span was isolated by direct page review of the rendered images
  - `C3-p001` to `C3-p003` are wrapper, title, or epigraph matter before the main commentary run
  - `C3-p004` begins the main `信心銘講話` commentary body
  - `C3-p056` is the last clear commentary body spread before publisher tail matter begins
  - `C3-p057` is publisher catalogue matter and `C3-p058` to `C3-p059` carry terminal publication matter
  - `C3-p060` to `C3-p063` are rear wrapper or library-tail images rather than commentary body

### Opening interpretation

- `C3` is now an opened in-package commentary control witness rather than a source-pinned metadata placeholder
- the isolated image-level commentary body span for future OCR and comparison work is `C3-p004` to `C3-p056`
- no OCR-compliance claim is made yet for `C3`

### RapidOCR

- status: full pass completed
- engine: `RapidOCR`
- output:
  - `ocr/C3/ocr/rapidocr/`
- summary:
  - `ocr/C3/ocr/rapidocr/run-summary.json`
- input basis:
  - `ocr/C3/page-images/`
- result:
  - `63` pages processed
  - `60` pages with text outputs on disk
  - `3` pages without text:
    - `C3-p060`
    - `C3-p061`
    - `C3-p062`
  - `0` errors

### Tesseract

- status: full pass completed
- environment:
  - witness-local `chi_tra` model under `ocr/T1/tessdata/`
- output:
  - `ocr/C3/ocr/tesseract-full-pass/`
- summary:
  - `ocr/C3/ocr/tesseract-full-pass/run-summary.json`
- input basis:
  - `ocr/C3/page-images/`
- result:
  - `63` pages processed
  - `63` pages with text outputs on disk
  - `0` errors
- machine note:
  - the first long run exceeded the one-hour shell timeout before process exit
  - the saved file set and saved summary had already closed the witness at `63/63` pages
  - the run carries only the familiar tiny-fragment scale warnings

### PaddleOCR

- status: full pass completed
- environment: Python `3.12`
- configuration:
  - `PaddleOCR(lang='ch', ocr_version='PP-OCRv4', device='cpu', enable_hpi=False, enable_mkldnn=False, cpu_threads=1)`
- output:
  - `ocr/C3/ocr/paddleocr-ppocrv4/`
- summary:
  - `ocr/C3/ocr/paddleocr-ppocrv4/run-summary-full.json`
- derivative text support:
  - `ocr/C3/ocr/paddleocr-ppocrv4/extracted-text/`
- input basis:
  - `ocr/C3/page-images/`
- result:
  - `63` pages processed
  - `63` success pages
  - `0` error pages
- machine note:
  - the run completed in a single pass
  - resized-image warnings were emitted by the local Paddle stack but did not prevent successful saved outputs

### EasyOCR

- status: full pass completed
- environment: Python `3.14`
- languages:
  - `ch_tra`
  - `en`
- output:
  - `ocr/C3/ocr/easyocr-full-pass/`
- summary:
  - `ocr/C3/ocr/easyocr-full-pass/run-summary.json`
- input basis:
  - `ocr/C3/page-images/`
- result:
  - `63` pages processed
  - `61` pages with text
  - `2` no-text pages:
    - `C3-p061`
    - `C3-p062`
  - `0` errors
- machine note:
  - the run completed in a single pass
  - the local EasyOCR stack emitted the familiar CPU and `pin_memory` warnings without preventing saved outputs

### Compliance interpretation

- `C3` now has a recorded status block for all four mandated engines
- `C3` is now a real OCR-backed commentary control witness rather than only an opened metadata record
- `C3` now has full-pass coverage from `RapidOCR`, `tesseract`, `PaddleOCR PP-OCRv4`, and `EasyOCR`
- `C3` is ready for bounded comparison use on representative commentary-body leaves rather than as a direct short poem witness

## C4 commentary-control opening

Date: 2026-04-17
Witness: `C4`
Source type: commentary control PDF

### Source verification

- source file:
  - `Faith_in_Mind_NDL_Commentaries/NDL823156_xinxinming_nentei.pdf`
- bytes:
  - `53,116,077`
- SHA-256:
  - `FA1C9CA05B09D327FFF02A4FE5F37DFC4440117E1916E445B4F7E40D619BA2B1`
- local validation:
  - readable on this machine with `pypdf`
  - `26` pages confirmed locally

### Render package

- output:
  - `ocr/C4/page-images/`
  - `ocr/C4/metadata.json`
  - `ocr/C4/page-map.csv`
- render engine:
  - `PyMuPDF`
- render DPI:
  - `150`
- render format:
  - `png`
- machine note:
  - the first long render run exceeded the shell timeout after `20` saved pages
  - the render was resumed from the saved page set and closed cleanly at `26/26` pages without restarting from scratch

### Page-role judgment

- classification:
  - `C4-p001` to `C4-p004` = `title`
  - `C4-p005` to `C4-p022` = `body`
  - `C4-p023` = `colophon`
  - `C4-p024` to `C4-p026` = `title`
- evidence note:
  - direct page review shows wrapper, cover, and title or presentation matter on `C4-p001` to `C4-p004`
  - `C4-p005` begins the main `信心銘拈提` commentary body and the commentary run remains stable through `C4-p022`
  - `C4-p023` is a mixed terminal spread with commentary body still on the right page while imprint or colophon matter occupies the left page
  - `C4-p024` to `C4-p026` are tail, wrapper, or library matter rather than commentary body

### Opening interpretation

- `C4` is now an opened in-package commentary control witness rather than a source-pinned metadata placeholder
- the isolated image-level commentary body span for future OCR and comparison work is `C4-p005` to `C4-p022`, with `C4-p023` kept explicit as a mixed terminal boundary spread
- no OCR-compliance claim is made yet for `C4`

### RapidOCR

- status: full pass completed
- engine: `RapidOCR`
- output:
  - `ocr/C4/ocr/rapidocr/`
- summary:
  - `ocr/C4/ocr/rapidocr/run-summary.json`
- input basis:
  - `ocr/C4/page-images/`
- result:
  - `26` pages processed
  - `24` pages with text outputs on disk
  - `2` pages without text:
    - `C4-p003`
    - `C4-p025`
  - `0` errors

### Tesseract

- status: full pass completed
- environment:
  - witness-local `chi_tra` model under `ocr/T1/tessdata/`
- output:
  - `ocr/C4/ocr/tesseract-full-pass/`
- summary:
  - `ocr/C4/ocr/tesseract-full-pass/run-summary.json`
- input basis:
  - `ocr/C4/page-images/`
- result:
  - `26` pages processed
  - `26` pages with text outputs on disk
  - `0` errors
- machine note:
  - the run completed in a single pass
  - the run carries only the familiar tiny-fragment scale warnings

### PaddleOCR

- status: full pass completed
- environment: Python `3.12`
- configuration:
  - `PaddleOCR(lang='ch', ocr_version='PP-OCRv4', device='cpu', enable_hpi=False, enable_mkldnn=False, cpu_threads=1)`
- output:
  - `ocr/C4/ocr/paddleocr-ppocrv4/`
- summary:
  - `ocr/C4/ocr/paddleocr-ppocrv4/run-summary-full.json`
- derivative text support:
  - `ocr/C4/ocr/paddleocr-ppocrv4/extracted-text/`
- input basis:
  - `ocr/C4/page-images/`
- result:
  - `26` pages processed
  - `26` success pages
  - `0` error pages
- machine note:
  - the run completed in a single pass
  - resized-image warnings were emitted by the local Paddle stack but did not prevent successful saved outputs

### EasyOCR

- status: full pass completed
- environment: Python `3.14`
- languages:
  - `ch_tra`
  - `en`
- output:
  - `ocr/C4/ocr/easyocr-full-pass/`
- summary:
  - `ocr/C4/ocr/easyocr-full-pass/run-summary.json`
- input basis:
  - `ocr/C4/page-images/`
- result:
  - `26` pages processed
  - `26` pages with text
  - `0` no-text pages
  - `0` errors
- machine note:
  - the run completed in a single pass
  - the local EasyOCR stack emitted the familiar CPU and `pin_memory` warnings without preventing saved outputs

### Compliance interpretation

- `C4` now has a recorded status block for all four mandated engines
- `C4` is now a real OCR-backed commentary control witness rather than only an opened metadata record
- `C4` now has full-pass coverage from `RapidOCR`, `tesseract`, `PaddleOCR PP-OCRv4`, and `EasyOCR`
- `C4` is ready for bounded comparison use on representative commentary-body leaves rather than as a direct short poem witness

## C5 commentary-control opening

Date: 2026-04-18
Witness: `C5`
Source type: commentary control PDF

### Source verification

- source file:
  - `Faith_in_Mind_NDL_Commentaries/NDL823160_yetangshui_guanzhu_part1.pdf`
- bytes:
  - `135,624,253`
- SHA-256:
  - `9E9E74ED7A2100DB21241B748BCE1A6A7A28B5FA2A2AD94D47F34898DD13FB16`
- local validation:
  - readable on this machine with `pypdf`
  - `74` pages confirmed locally

### Render package

- output:
  - `ocr/C5/page-images/`
  - `ocr/C5/metadata.json`
  - `ocr/C5/page-map.csv`
- render engine:
  - `PyMuPDF`
- render DPI:
  - `150`
- render format:
  - `png`
- machine note:
  - the first long render run exceeded the shell timeout after a partial saved page set
  - the original render process was allowed to continue and the witness later closed cleanly at `74/74` rendered pages

### Page-role judgment

- classification:
  - `C5-p001` to `C5-p003` = `title`
  - `C5-p004` to `C5-p072` = `body`
  - `C5-p073` = `colophon`
  - `C5-p074` = `title`
- evidence note:
  - direct page review shows seal, title, publication, or prefatory matter on `C5-p001` to `C5-p003`
  - `C5-p004` begins the main `冠註信心銘夜塘水` commentary body and the commentary run remains stable through `C5-p072`
  - `C5-p073` is an explicit terminal page marked as the end of `巻上`
  - `C5-p074` is rear wrapper or library-tail matter rather than commentary body

### Opening interpretation

- `C5` is now an opened in-package commentary control witness rather than a source-pinned metadata placeholder
- the isolated image-level commentary body span for future OCR and comparison work is `C5-p004` to `C5-p072`, with `C5-p073` kept explicit as the terminal page
- no OCR-compliance claim is made yet for `C5`

### RapidOCR

- status: full pass completed
- engine: `RapidOCR`
- output:
  - `ocr/C5/ocr/rapidocr/`
- summary:
  - `ocr/C5/ocr/rapidocr/run-summary.json`
- input basis:
  - `ocr/C5/page-images/`
- result:
  - `74` pages processed
  - `73` pages with text outputs on disk
  - `1` page without text:
    - `C5-p073`
  - `0` errors

### Tesseract

- status: full pass completed
- environment:
  - witness-local `chi_tra` model under `ocr/T1/tessdata/`
- output:
  - `ocr/C5/ocr/tesseract-full-pass/`
- summary:
  - `ocr/C5/ocr/tesseract-full-pass/run-summary.json`
- input basis:
  - `ocr/C5/page-images/`
- result:
  - `74` pages processed
  - `74` pages with text outputs on disk
  - `0` errors
- machine note:
  - the run completed in a single pass
  - the run carries only the familiar tiny-fragment scale warnings

### PaddleOCR

- status: full pass completed
- environment: Python `3.12`
- configuration:
  - `PaddleOCR(lang='ch', ocr_version='PP-OCRv4', device='cpu', enable_hpi=False, enable_mkldnn=False, cpu_threads=1)`
- output:
  - `ocr/C5/ocr/paddleocr-ppocrv4/`
- summary:
  - `ocr/C5/ocr/paddleocr-ppocrv4/run-summary-full.json`
- derivative text support:
  - `ocr/C5/ocr/paddleocr-ppocrv4/extracted-text/`
- input basis:
  - `ocr/C5/page-images/`
- result:
  - `74` pages processed
  - `74` success pages
  - `0` error pages
- machine note:
  - the first long run exceeded the shell timeout at a saved state through `C5-p052`
  - the resumed closeout completed the remaining back half of the witness
  - resized-image warnings were emitted by the local Paddle stack but did not prevent successful saved outputs

### EasyOCR

- status: full pass completed
- environment: Python `3.14`
- languages:
  - `ch_tra`
  - `en`
- output:
  - `ocr/C5/ocr/easyocr-full-pass/`
- summary:
  - `ocr/C5/ocr/easyocr-full-pass/run-summary.json`
- input basis:
  - `ocr/C5/page-images/`
- result:
  - `74` pages processed
  - `73` pages with text
  - `1` no-text page:
    - `C5-p073`
  - `0` errors
- machine note:
  - the first two long runs exceeded the shell timeout at saved states through `C5-p031` and then `C5-p066`
  - the final closeout completed the remaining tail pages
  - the local EasyOCR stack emitted the familiar CPU and `pin_memory` warnings without preventing saved outputs

### Compliance interpretation

- `C5` now has a recorded status block for all four mandated engines
- `C5` is now a real OCR-backed commentary control witness rather than only an opened metadata record
- `C5` now has full-pass coverage from `RapidOCR`, `tesseract`, `PaddleOCR PP-OCRv4`, and `EasyOCR`
- `C5` is ready for bounded comparison use on representative commentary-body leaves rather than as a direct short poem witness
