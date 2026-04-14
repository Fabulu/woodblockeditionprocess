# Normalization Rule Log: T1 Pass 1

Date: 2026-04-14
Scope: structural normalization of RapidOCR full-pass output for `T1`

## Inputs

- Source OCR directory: `provenance/faith-in-mind/ocr/T1/ocr/rapidocr/`
- Engine: `rapidocr_onnxruntime`
- Page basis: `T1-p001` to `T1-p083`

## Rules applied

- preserve UTF-8 text as extracted from the page-level RapidOCR `.txt` files
- insert explicit page markers as `[[page:T1-pNNN]]`
- assign stable line identifiers as `[T1-pNNN.lNN]`
- trim leading and trailing whitespace on each OCR line
- collapse repeated internal whitespace to a single space for structural readability
- drop empty lines created by OCR output formatting
- mark pages with no extracted text as `<NO_TEXT>`

## Rules not applied

- no character correction
- no modernization
- no punctuation repair
- no witness comparison
- no manual reading override
- no synthetic line reordering

## Output

- `T1-normalized-pass1.txt`
