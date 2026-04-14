# OCR Environment Record: Faith in Mind

Date: 2026-04-14
Status: active
Scope: `T1` OCR checkpoint configuration and runtime state

## Interpreter rule

- Preferred interpreter for OCR and related tooling on this machine: `py -3.12`
- Do not default to Python `3.14` for PaddleOCR work in this package

## Core witness inputs

- Witness siglum: `T1`
- Source PDF: `Faith_in_Mind_Korea_Commons/CNTS-00047968260_faith_in_mind.pdf`
- Page image directory: `provenance/faith-in-mind/ocr/T1/page-images/`
- Calibration page used for cross-engine probes: `T1-p001`
- Additional RapidOCR probe page: `T1-p002`
- Local Tesseract language data:
  - `provenance/faith-in-mind/ocr/T1/tessdata/chi_tra.traineddata`
  - `provenance/faith-in-mind/ocr/T1/tessdata/chi_tra_vert.traineddata`

## Python environments

### Python `3.12`

- Version: `3.12.10`
- Intended role: primary OCR environment for PaddleOCR and related tooling
- Installed OCR packages:
  - `paddleocr 3.2.0`
  - `paddlepaddle 3.1.1`
  - `paddlex 3.2.1`

### Python `3.14`

- Status: present on machine
- Role in this package: not preferred for OCR
- Existing use before environment lock:
  - `EasyOCR` probe was run from Python `3.14`

## Engine status snapshot

### RapidOCR

- Environment: Python `3.14` in the earlier run
- Package family:
  - `rapidocr_onnxruntime`
  - `onnxruntime`
  - `opencv-python-headless`
- Status: full-pass usable
- Full output directory: `provenance/faith-in-mind/ocr/T1/ocr/rapidocr/`

### Tesseract

- Binary: `C:/Program Files/Tesseract-OCR/tesseract.exe`
- Mode used: local workspace `tessdata` rather than relying on system language packs
- Probe model: `chi_tra_vert`
- Status: probe-usable

### EasyOCR

- Environment used so far: Python `3.14`
- Status: probe-usable but low quality on `T1-p001`
- Next preference: re-run under Python `3.12` if package state is needed in the preferred OCR interpreter

### PaddleOCR

- Environment: Python `3.12`
- Status: calibration-usable with explicit `PP-OCRv4`; default `PP-OCRv5` still crashes on this machine

## PaddleOCR runtime failure record

### Reproduced failing call

- Constructor: `PaddleOCR(lang='ch')`
- Prediction call: `.predict(T1-p001.png)`

### Observed backend state

- `paddle 3.3.1`
- CPU-only runtime
- `paddle.is_compiled_with_cuda() == False`
- device: `cpu`
- oneDNN runtime path appears active during prediction

### Failure signature

- Exception type: `NotImplementedError`
- Message:
  - `(Unimplemented) ConvertPirAttribute2RuntimeAttribute not support [pir::ArrayAttribute<pir::DoubleAttribute>]`
- Stack focus:
  - `paddlex.inference.models.common.static_infer.py`
  - `predictor.run()`
  - `onednn_instruction.cc`

### Attempted mitigations already tried

These did not clear the failure:

- `FLAGS_use_mkldnn=0`
- `FLAGS_use_mkldnn=False`
- keeping the default `PaddleOCR(lang='ch')` path with cached models

### Reproduced failing stack after version rollback

After downgrading to:

- `paddleocr 3.2.0`
- `paddlepaddle 3.1.1`
- `paddlex 3.2.1`

the default `PP-OCRv5` route no longer raises the earlier Python `NotImplementedError`, but it still dies during prediction with:

- Windows fatal exception: `access violation`
- Stack focus:
  - `paddlex.inference.models.common.static_infer.py`
  - `paddlex.inference.models.text_detection.predictor.py`
  - `paddleocr._pipelines.ocr.py`

### Working configuration

This configuration produced a successful calibration run on `T1-p001`:

- interpreter: `py -3.12`
- constructor:
  - `PaddleOCR(lang='ch', ocr_version='PP-OCRv4', device='cpu', enable_hpi=False, enable_mkldnn=False, cpu_threads=1)`
- output directory:
  - `provenance/faith-in-mind/ocr/T1/ocr/paddleocr-ppocrv4/`

Saved calibration outputs:

- `T1-p001.json`
- `T1-p001.txt`
- `run-summary.json`

### Next diagnostic directions

- keep the downgraded Python `3.12` stack
- use `PP-OCRv4` as the working Paddle calibration path for this machine unless a later `PP-OCRv5` fix is confirmed
- capture the rest of the same-page comparison set under the now-pinned OCR environment

## Comparison checkpoint rule

Before manual correction begins, the package must retain:

- same-page comparison outputs for `tesseract`, `RapidOCR`, `EasyOCR`, and `PaddleOCR` where runnable
- exact blocker records for any engine that remains non-runnable

## Resume note

Open this file together with:

1. `process/current-state.md`
2. `process/ocr-run-log.md`
3. `transcription/ocr-transcription-plan.md`
