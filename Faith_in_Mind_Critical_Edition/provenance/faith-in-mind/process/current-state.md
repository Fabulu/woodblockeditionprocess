# Current State: Faith in Mind

Date: 2026-04-14
Status: active
Edition slug: `faith-in-mind`

## Resume summary

- Witness set: locked
- Scope: broader
- Copy-text: `T1` locked as starting spine, switch allowed only by logged evidence-based decision
- Current phase: `manual_correction_pending`
- Last completed phase: `normalization_pass_1`

## What is already done

- witness hunt completed and locked after the two-wave no-new-free rule
- sigla frozen as `T1-T5`, `A1-A3`, `C1-C17`, `S1-S5`
- acquisition metadata normalized across the locked set
- copy-text ranking completed
- `T1` locked as the starting copy-text
- `T1` page images and page map generated
- RapidOCR pass 1 completed across all `83` `T1` pages
- PaddleOCR `PP-OCRv4` full pass completed across all `83` `T1` pages

## Next action

Before Stage 2D manual correction, classify `T1` page roles in `page-map.csv`, then correct the normalized working spine.

Use:

- `provenance/faith-in-mind/transcription/ocr-transcription-plan.md`
- `provenance/faith-in-mind/ocr/T1/page-map.csv`
- `provenance/faith-in-mind/transcription/normalized/T1-normalized-pass1.txt`
- `provenance/faith-in-mind/transcription/normalized/normalization-rule-log.md`
- `provenance/faith-in-mind/process/ocr-run-log.md`
- `provenance/faith-in-mind/process/ocr-environment.md`

Produce next:

- page-role classification for `T1`
- corrected working text under `provenance/faith-in-mind/transcription/corrected/`
- correction log
- unresolved loci opened where `T1` cannot be secured

Do not start a fresh witness hunt.
Do not reopen copy-text selection unless new locus-specific evidence appears.
Do not bring in `T4`, `T5`, or `T2` until a first corrected `T1` working text exists.

## Known blockers and cautions

- `T1-p081`, `T1-p082`, and `T1-p083` returned no text in RapidOCR pass 1 and need classification during normalization or correction
- the four-engine same-page comparison requirement is now satisfied on `T1-p001`, but only RapidOCR has a full-pass run across all `83` pages
- `PaddleOCR` now also has a full pass with `PP-OCRv4` under Python `3.12`, but the default `PP-OCRv5` path still crashes on this machine
- `T1` page roles are still unclassified, so the current `83` pages must not yet be treated as if they were all poem body
- on this machine, prefer Python `3.12` for OCR and related tooling instead of the default Python `3.14`
- the local OCR tool stack is uneven; machine health must be logged honestly rather than assumed
- no manual correction pass has started yet; the normalized spine is still uncorrected OCR

## Open these first when resuming

1. `provenance/faith-in-mind/process/current-state.md`
2. `provenance/faith-in-mind/process/human-log.md`
3. `provenance/faith-in-mind/process/decision-log.md`
4. `provenance/faith-in-mind/process/ocr-environment.md`
5. `provenance/faith-in-mind/transcription/ocr-transcription-plan.md`
6. `xml-open/ce/faith-in-mind/timeline.json`
