# Current State: Faith in Mind

Date: 2026-04-14
Status: active
Edition slug: `faith-in-mind`

## Resume summary

- Witness set: locked
- Scope: broader
- Copy-text: `T1` locked as starting spine, switch allowed only by logged evidence-based decision
- Current phase: `manual_correction_pass_1_started`
- Last completed phase: `manual_correction_slice_opening_lemmas`

## What is already done

- witness hunt completed and locked after the two-wave no-new-free rule
- sigla frozen as `T1-T5`, `A1-A3`, `C1-C17`, `S1-S5`
- acquisition metadata normalized across the locked set
- copy-text ranking completed
- `T1` locked as the starting copy-text
- `T1` page images and page map generated
- RapidOCR pass 1 completed across all `83` `T1` pages
- PaddleOCR `PP-OCRv4` full pass completed across all `83` `T1` pages
- `T1` page roles classified at the dominant-page level in `page-map.csv`
- Stage 2D started with a corrected working file, correction log, and first lemma-line fixes through the early commentary run

## Next action

Continue Stage 2D manual correction against the corrected working spine, expanding from the opening title and lemma slice into prefatory and commentary prose.

Use:

- `provenance/faith-in-mind/transcription/ocr-transcription-plan.md`
- `provenance/faith-in-mind/ocr/T1/page-map.csv`
- `provenance/faith-in-mind/transcription/normalized/T1-normalized-pass1.txt`
- `provenance/faith-in-mind/transcription/normalized/normalization-rule-log.md`
- `provenance/faith-in-mind/process/ocr-run-log.md`
- `provenance/faith-in-mind/process/ocr-environment.md`

Produce next:

- continue correcting `T1-corrected-pass1-working.txt`
- expand `correction-log.md`
- resolve or refine entries in `unresolved-loci.md`

Do not start a fresh witness hunt.
Do not reopen copy-text selection unless new locus-specific evidence appears.
Do not bring in `T4`, `T5`, or `T2` until a first corrected `T1` working text exists.

## Known blockers and cautions

- `T1-p081`, `T1-p082`, and `T1-p083` returned no text in RapidOCR pass 1 and are now provisionally classified as `blank`
- the four-engine same-page comparison requirement is now satisfied on `T1-p001`, but only RapidOCR has a full-pass run across all `83` pages
- `PaddleOCR` now also has a full pass with `PP-OCRv4` under Python `3.12`, but the default `PP-OCRv5` path still crashes on this machine
- `T1` is not a pure poem-only object: `p001-p004` title or imprint matter, `p005-p006` prefatory prose, `p007-p080` commentary-dominant pages with embedded poem lemmata, `p081-p083` blank tail pages
- on this machine, prefer Python `3.12` for OCR and related tooling instead of the default Python `3.14`
- the local OCR tool stack is uneven; machine health must be logged honestly rather than assumed
- only the title lines and a first set of recovered lemma lines through `T1-p035.l01` have been corrected so far; most prose remains uncorrected

## Open these first when resuming

1. `provenance/faith-in-mind/process/current-state.md`
2. `provenance/faith-in-mind/process/human-log.md`
3. `provenance/faith-in-mind/process/decision-log.md`
4. `provenance/faith-in-mind/process/ocr-environment.md`
5. `provenance/faith-in-mind/transcription/ocr-transcription-plan.md`
6. `xml-open/ce/faith-in-mind/timeline.json`
