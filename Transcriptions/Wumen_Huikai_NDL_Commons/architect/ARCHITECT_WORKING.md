# Wumen Huikai Witness Corroboration Working File

## Current Witness

- Folder: `C:\woodblocks\Wumen_Huikai_NDL_Commons`
- Canonical PDF: `NDL2537788_wumen_kai_record.redownload.pdf`
- Page count: `70`
- Commons filename: `NDL2537788_無門開和尚語録.pdf`

## Purpose

- This workspace is a secondary witness for corroboration.
- The primary base draft remains `C:\woodblocks\Transcriptions\Wumenguan_1632_NDL_Commons\architect\WUMENGUAN_1632.md`.
- This witness may clarify weak graphs, case boundaries, and end-matter readings.
- It must not silently overwrite the 1632 witness where the two differ.

## Working Rule

- Keep this workspace scan-derived.
- No CBETA or external text spine.
- Record corroboration as witness-to-witness comparison.
- When the two witnesses diverge, describe the divergence instead of flattening it.
- Read OCR outputs first for evidence inventory; use witness images second to adjudicate and extend.

## Pipeline

- `scripts\batch_render_ocr.py`: full page render, leaf split, coarse frame detection, first-pass Tesseract OCR
- `scripts\refine_leaf_ocr.py`: refined side crops and second-pass Tesseract OCR
- `scripts\run_rapidocr_leaf.py`: single-image RapidOCR comparator
- `scripts\run_paddleocr_leaf.py`: single-image PaddleOCR comparator

## Immediate Next Step

1. render the full 70-page PDF
2. refine all leaves
3. anchor a handful of known hard loci from the 1632 draft
4. build a verification loop for whole-book comparison
