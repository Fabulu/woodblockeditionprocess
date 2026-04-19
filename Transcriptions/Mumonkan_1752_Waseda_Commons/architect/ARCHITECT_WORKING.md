# Mumonkan 1752 Waseda Witness Working File

## Current Witness

- Folder: `Mumonkan_1752_Waseda_Commons`
- Canonical PDF: `WUL-bunko31_e1102_mumonkan.pdf`
- Page count: `56`

## Purpose

- This workspace is a third witness for corroboration.
- Base draft remains `Transcriptions\Wumenguan_1632_NDL_Commons\architect\WUMENGUAN_1632.md`.
- Secondary corroborant remains `Transcriptions\Wumen_Huikai_NDL_Commons`.
- This witness should help test hard graphs, case boundaries, and larger witness divergences.

## Working Rule

- Keep this workspace scan-derived.
- No external text spine.
- Record differences as witness differences, not silent corrections.
- Read OCR outputs first for evidence inventory; use witness images second to adjudicate and extend.

## Pipeline

- `scripts\batch_render_ocr.py`
- `scripts\refine_leaf_ocr.py`
- `scripts\run_rapidocr_leaf.py`
- `scripts\run_paddleocr_leaf.py`

## Immediate Next Step

1. confirm first reliable anchors
2. run batch render / refined OCR if the witness quality justifies it
3. use it as a third corroborant for hard loci and broader verification

## First Anchor Assessment

- Verdict: usable as a corroborating witness, but selectively
- Front matter:
  - page `3` shows stable vocabulary including `世尊升座`, `法筵龍象界`, `白椎`, `維那`
- Later body anchors:
  - page `13`
  - page `47`
  - stable phrases reported from local inspection include:
    - `百尺竿頭進步`
    - `不落因果 / 不昧因果`
    - `南泉已前作生會`
    - `百尺竿頭坐底人`
    - `十方世界現全身`
- Current limitation:
  - this witness is useful for corroborating known cases and front matter
  - it does not yet solve the `扇子 / 帝釋` holdout
