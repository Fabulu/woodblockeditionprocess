# Current State: Faith in Mind

Date: 2026-04-18
Status: active
Edition slug: `faith-in-mind`

## Resume summary

- Witness set: locked
- Scope: broader
- Copy-text: `T1` locked as starting spine, switch allowed only by logged evidence-based decision
- Current phase: `manual_correction_pass_1_started`
- Last completed phase: `comparison_control_slice_C5_opening`

## What is already done

- witness hunt completed and locked after the two-wave no-new-free rule
- sigla frozen as `T1-T5`, `A1-A3`, `C1-C17`, `S1-S5`
- acquisition metadata normalized across the locked set
- copy-text ranking completed
- `T1` locked as the starting copy-text
- `T1` page images and page map generated
- RapidOCR pass 1 completed across all `83` `T1` pages
- PaddleOCR `PP-OCRv4` full pass completed across all `83` `T1` pages
- Tesseract full pass completed across all `83` `T1` pages using witness-local `chi_tra` traineddata
- `T1` page roles classified at the dominant-page level in `page-map.csv`
- Stage 2D started with a corrected working file, correction log, and a broad recovered lemma-line spine through `T1-p079.l01`
- `T4` is now opened as the first comparison control with in-package metadata, page map, and a full recorded four-engine OCR basis
- `T4` page roles isolate `T4-p002` to `T4-p004` as the target body span
- a first `T4` vs `T1` comparison table now exists under `collation/first-pass-variant-table.md` on a full four-engine-recorded witness basis
- comparison-informed `T1` repairs from `T4` now include `T1-p021.l01a`, `T1-p031.l03`, `T1-p032.l01`, `T1-p047.l01`, `T1-p065.l01`, and `T1-p077.l01a`
- the `T1-p075` to `T1-p079` closing-band issue is now closed as omission rather than substitution in `T1`
- `T1-p081` and `T1-p082` are already aligned in `page-map.csv` as non-blank tail material, while `T1-p083` remains the only visually blank tail page
- `T5` is now opened as the next comparison-control witness with in-package `ocr/T5/metadata.json` and `ocr/T5/page-map.csv`
- `T5` page roles isolate `T5-p004` to `T5-p006` as the target `Faith in Mind` body span
- `T5` now has recorded full-pass OCR status across all four engines: `RapidOCR`, `tesseract`, `PaddleOCR PP-OCRv4`, and `EasyOCR`
- derived Paddle text support now exists for `T5` under `ocr/T5/ocr/paddleocr-ppocrv4/extracted-text/`
- a bounded `T5` comparison slice now exists and broadly confirms the recovered `T1` lemma spine without exposing a new forced repair locus
- the live `T1` working file integrity issue at `T1-p032.l01` has been restored to the already logged comparison-supported reading
- `T2` is now opened as the third comparison-control witness with in-package metadata, rendered page images, and a classified page map
- `T2` page roles isolate `T2-p003` to `T2-p005` as the target `Faith in Mind` body span, with `T2-p006` as immediate post-text colophon or imprint matter
- a first full `RapidOCR` pass now exists for `T2` under `ocr/T2/ocr/rapidocr/`
- because the full-resolution rendered `T2` PNG pages tripped PIL decompression-bomb guards on this workstation, the saved `T2` RapidOCR pass uses explicitly logged `ocr-input-120dpi/` JPEG derivatives as OCR input
- a full `tesseract` pass now also exists for `T2` under `ocr/T2/ocr/tesseract-full-pass/`
- a full `PaddleOCR PP-OCRv4` pass now exists for `T2` under `ocr/T2/ocr/paddleocr-ppocrv4/`
- derived Paddle text support now exists for `T2` under `ocr/T2/ocr/paddleocr-ppocrv4/extracted-text/`
- a full `EasyOCR` pass now exists for `T2` under `ocr/T2/ocr/easyocr-full-pass/`
- `T2` now has full recorded four-engine OCR compliance and is ready for bounded comparison use
- a bounded `T2` comparison slice now exists and broadly confirms the recovered `T1` lemma spine without exposing a new forced repair locus
- `T3` is now opened as the fourth comparison-control witness with in-package metadata, page map, and a classified late-body span
- `T3` page roles isolate `T3-p034` to `T3-p036` as the target `Faith in Mind` body span, with `T3-p001` to `T3-p003` and `T3-p040` to `T3-p041` as wrapper or title matter
- a full `RapidOCR` pass now exists for `T3` under `ocr/T3/ocr/rapidocr/`
- a full `tesseract` pass now exists for `T3` under `ocr/T3/ocr/tesseract-full-pass/`
- a full `PaddleOCR PP-OCRv4` pass now exists for `T3` under `ocr/T3/ocr/paddleocr-ppocrv4/`
- derived Paddle text support now exists for `T3` under `ocr/T3/ocr/paddleocr-ppocrv4/extracted-text/`
- a full `EasyOCR` pass now exists for `T3` under `ocr/T3/ocr/easyocr-full-pass/`
- `T3` now has full recorded four-engine OCR compliance and is ready for bounded comparison use
- a bounded `T3` comparison slice now exists and broadly confirms the recovered `T1` lemma spine without exposing a new forced repair locus
- `A1` is now opened as the first non-`T` anthology witness with in-package metadata, rendered page images, and a classified page map
- `A1` page roles isolate `A1-p003` to `A1-p008` as the target `Faith in Mind` body span, with `A1-p001` to `A1-p002` as wrapper or title matter, `A1-p009` to `A1-p041` as later anthology material, and `A1-p042` as rear wrapper or closing tail matter
- a full `RapidOCR` pass now exists for `A1` under `ocr/A1/ocr/rapidocr/`
- a full `tesseract` pass now exists for `A1` under `ocr/A1/ocr/tesseract-full-pass/`
- a full `PaddleOCR PP-OCRv4` pass now exists for `A1` under `ocr/A1/ocr/paddleocr-ppocrv4/`
- derived Paddle text support now exists for `A1` under `ocr/A1/ocr/paddleocr-ppocrv4/extracted-text/`
- a full `EasyOCR` pass now exists for `A1` under `ocr/A1/ocr/easyocr-full-pass/`
- `A1` now has full recorded four-engine OCR compliance and is ready for bounded comparison use
- a bounded `A1` comparison slice now exists and broadly confirms the recovered `T1` lemma spine without exposing a new forced repair locus, while further strengthening the omission judgment at `T1-p075`
- `A2` is now opened as the next derivative Waseda witness with in-package metadata, rendered page images, and a classified page map
- `A2` page roles currently treat `A2-p002` to `A2-p044` as the derivative body span, with `A2-p001` as front wrapper, `A2-p045` as colophon-like tail matter, and `A2-p046` as rear wrapper
- a full `RapidOCR` pass now exists for `A2` under `ocr/A2/ocr/rapidocr/`
- a full `tesseract` pass now exists for `A2` under `ocr/A2/ocr/tesseract-full-pass/`
- a full `PaddleOCR PP-OCRv4` pass now exists for `A2` under `ocr/A2/ocr/paddleocr-ppocrv4/`
- derived Paddle text support now exists for `A2` under `ocr/A2/ocr/paddleocr-ppocrv4/extracted-text/`
- a full `EasyOCR` pass now exists for `A2` under `ocr/A2/ocr/easyocr-full-pass/`
- `A2` now has full recorded four-engine OCR compliance and is ready for bounded comparison use
- a bounded representative `A2` comparison slice now exists and broadly confirms the recovered `T1` lemma spine without exposing a new forced repair locus
- `A3` is now opened as the next derivative NDL witness with in-package metadata, rendered page images, and a classified page map
- `A3` page roles isolate `A3-p003` to `A3-p011` as the target Faith in Mind body span, with `A3-p001` to `A3-p002` as wrapper or title matter, `A3-p012` to `A3-p054` as later anthology material, `A3-p055` as colophon-like tail matter, and `A3-p056` to `A3-p057` as rear wrapper matter
- a full `RapidOCR` pass now exists for `A3` under `ocr/A3/ocr/rapidocr/`
- a full `tesseract` pass now exists for `A3` under `ocr/A3/ocr/tesseract-full-pass/`
- a full `PaddleOCR PP-OCRv4` pass now exists for `A3` under `ocr/A3/ocr/paddleocr-ppocrv4/`
- derived Paddle text support now exists for `A3` under `ocr/A3/ocr/paddleocr-ppocrv4/extracted-text/`
- a full `EasyOCR` pass now exists for `A3` under `ocr/A3/ocr/easyocr-full-pass/`
- `A3` now has full recorded four-engine OCR compliance and is ready for bounded comparison use
- a bounded representative `A3` comparison slice now exists and broadly confirms the recovered `T1` lemma spine without exposing a new high-confidence repair locus
- `C1` is now opened as the first commentary or translation control witness with in-package metadata, rendered page images, and a classified page map
- `C1` page roles isolate `C1-p051` to `C1-p052` as the target `信心銘和譯` span, with `C1-p001` to `C1-p005` as wrapper or contents matter, `C1-p006` to `C1-p050` as earlier anthology or translation material, `C1-p053` to `C1-p075` as later anthology or translation material, and `C1-p076` as rear cover matter
- a full `RapidOCR` pass now exists for `C1` under `ocr/C1/ocr/rapidocr/`
- a full `tesseract` pass now exists for `C1` under `ocr/C1/ocr/tesseract-full-pass/`
- a full `PaddleOCR PP-OCRv4` pass now exists for `C1` under `ocr/C1/ocr/paddleocr-ppocrv4/`
- derived Paddle text support now exists for `C1` under `ocr/C1/ocr/paddleocr-ppocrv4/extracted-text/`
- a full `EasyOCR` pass now exists for `C1` under `ocr/C1/ocr/easyocr-full-pass/`
- `C1` now has full recorded four-engine OCR compliance and is ready for bounded comparison use as a translation or reception control witness
- a bounded `C1` comparison slice now exists and confirms broad transmitted order plus the standard close as a translation or reception control witness, without exposing a new high-confidence repair locus
- `C2` is now opened as the next commentary or translation control witness with in-package metadata, rendered page images, and a classified page map
- `C2` page roles isolate `C2-p021` to `C2-p023` as the target `三祖大師信心銘` span, with `C2-p020`, `C2-p032`, `C2-p060`, and `C2-p094` as section-divider title pages and the remaining rendered part-volume as non-target anthology or liturgical material
- a first full `RapidOCR` pass now exists for `C2` under `ocr/C2/ocr/rapidocr/`
- a full `tesseract` pass now also exists for `C2` under `ocr/C2/ocr/tesseract-full-pass/`
- a full `PaddleOCR PP-OCRv4` pass now also exists for `C2` under `ocr/C2/ocr/paddleocr-ppocrv4/`
- derived Paddle text support now exists for `C2` under `ocr/C2/ocr/paddleocr-ppocrv4/extracted-text/`
- a full `EasyOCR` pass now also exists for `C2` under `ocr/C2/ocr/easyocr-full-pass/`
- `C2` now has full recorded four-engine OCR compliance and is ready for bounded comparison use as a translation or reception control witness
- `C3` is now opened as the next commentary control witness with in-package metadata, rendered page images, and a classified page map
- `C3` page roles isolate `C3-p004` to `C3-p056` as the main `信心銘講話` commentary body span, with wrapper or title matter on `C3-p001` to `C3-p003`, publisher or colophon tail matter on `C3-p057` to `C3-p059`, and rear wrapper or library tail matter on `C3-p060` to `C3-p063`
- a first full `RapidOCR` pass now exists for `C3` under `ocr/C3/ocr/rapidocr/`
- a full `tesseract` pass now also exists for `C3` under `ocr/C3/ocr/tesseract-full-pass/`
- a full `PaddleOCR PP-OCRv4` pass now also exists for `C3` under `ocr/C3/ocr/paddleocr-ppocrv4/`
- derived Paddle text support now exists for `C3` under `ocr/C3/ocr/paddleocr-ppocrv4/extracted-text/`
- a full `EasyOCR` pass now also exists for `C3` under `ocr/C3/ocr/easyocr-full-pass/`
- `C3` now has full recorded four-engine OCR compliance and is ready for bounded comparison use as a commentary control witness
- a bounded `C3` commentary-control comparison slice now exists and confirms broad commentary-backed support for the recovered `T1` lemma spine plus the standard close, without exposing a new high-confidence repair locus
- `C4` is now opened as the next commentary control witness with in-package metadata, rendered page images, and a classified page map
- `C4` page roles isolate `C4-p005` to `C4-p022` as the main `信心銘拈提` commentary body span, with wrapper or title matter on `C4-p001` to `C4-p004`, a mixed terminal body-plus-colophon spread on `C4-p023`, and tail or wrapper matter on `C4-p024` to `C4-p026`
- a first full `RapidOCR` pass now exists for `C4` under `ocr/C4/ocr/rapidocr/`
- a full `tesseract` pass now also exists for `C4` under `ocr/C4/ocr/tesseract-full-pass/`
- a full `PaddleOCR PP-OCRv4` pass now also exists for `C4` under `ocr/C4/ocr/paddleocr-ppocrv4/`
- derived Paddle text support now exists for `C4` under `ocr/C4/ocr/paddleocr-ppocrv4/extracted-text/`
- a full `EasyOCR` pass now also exists for `C4` under `ocr/C4/ocr/easyocr-full-pass/`
- `C4` now has full recorded four-engine OCR compliance and is ready for bounded comparison use as a commentary control witness
- a bounded `C4` commentary-control comparison slice now exists and confirms broad commentary-backed support for the recovered `T1` lemma spine plus the standard close, without exposing a new high-confidence repair locus
- `C5` is now opened as the next commentary control witness with in-package metadata, rendered page images, and a classified page map
- `C5` page roles isolate `C5-p004` to `C5-p072` as the main `冠註信心銘夜塘水` commentary body span, with front matter on `C5-p001` to `C5-p003`, an explicit terminal page on `C5-p073`, and rear wrapper or library-tail matter on `C5-p074`

## Next action

Continue the `C5` four-engine OCR-compliance slice on the newly isolated `冠註信心銘夜塘水` commentary control witness.

Use:

- `provenance/faith-in-mind/process/current-state.md`
- `provenance/faith-in-mind/process/human-log.md`
- `provenance/faith-in-mind/process/decision-log.md`
- `provenance/faith-in-mind/witnesses/witness-register.md`
- `provenance/faith-in-mind/witnesses/acquisition-metadata.md`
- `Faith_in_Mind_NDL_Commentaries/`
- `provenance/faith-in-mind/ocr/C4/`
- `provenance/faith-in-mind/ocr/C5/`
- `provenance/faith-in-mind/process/ocr-run-log.md`
- `provenance/faith-in-mind/collation/first-pass-variant-table.md`
- `Faith_in_Mind_NDL_Commentaries/`
- `provenance/faith-in-mind/ocr/C4/`

Produce next:

- declare the bounded OCR-compliance slice for `C5`
- complete and record the full `RapidOCR`, `tesseract`, `PaddleOCR PP-OCRv4`, and `EasyOCR` passes for `C5`
- keep the commentary-control role of `C5` explicit rather than treating it as a direct base-text witness
- keep `current-state.md`, `process-log.md`, `human-log.md`, `ocr-run-log.md`, `process.json`, and `timeline.json` aligned before any `C5` comparison use

Do not start a fresh witness hunt.
Do not reopen copy-text selection unless new locus-specific evidence appears.
`T4` remains the first completed comparison-control witness.
`T5` has now completed its first bounded comparison slice.
`T2` has now completed its first bounded comparison slice.
`T3` has now completed its first bounded comparison slice.
`A1` has now completed its witness-opening and four-engine OCR-compliance slice.
`A1` has now also completed its first bounded comparison slice.
`A2` has now completed its witness-opening slice.
`A2` has now also completed its four-engine OCR-compliance slice.
`A2` has now also completed its first bounded representative comparison slice.
`A3` has now completed its witness-opening slice.
`A3` has now also completed its four-engine OCR-compliance slice.
`A3` has now also completed its first bounded representative comparison slice.
`C1` has now completed its witness-opening slice.
`C1` has now also completed its four-engine OCR-compliance slice.
`C1` has now also completed its first bounded translation-control comparison slice.
`C2` has now completed its witness-opening slice.
`C2` has now also completed its first full `RapidOCR` pass.
`C2` has now also completed its full `tesseract` pass.
`C2` has now also completed its full `PaddleOCR PP-OCRv4` pass.
`C2` has now also completed its full `EasyOCR` pass.
`C2` has now also completed its first bounded translation-control comparison slice.
`C3` has now completed its witness-opening slice.
`C3` has now also completed its first full `RapidOCR` pass.
`C3` has now also completed its full `tesseract` pass.
`C3` has now also completed its full `PaddleOCR PP-OCRv4` pass.
`C3` has now also completed its full `EasyOCR` pass.
`C3` has now also completed its first bounded commentary-control comparison slice.
`C4` has now completed its witness-opening slice.
`C4` has now also completed its first full `RapidOCR` pass.
`C4` has now also completed its full `tesseract` pass.
`C4` has now also completed its full `PaddleOCR PP-OCRv4` pass.
`C4` has now also completed its full `EasyOCR` pass.
`C4` has now also completed its first bounded commentary-control comparison slice.
`C5` has now completed its witness-opening slice.

## Known blockers and cautions

- `T1-p081`, `T1-p082`, and `T1-p083` returned no text in RapidOCR pass 1, but visual review now shows only `T1-p083` is blank; `T1-p081` and `T1-p082` are already recorded in `page-map.csv` as tail material rather than blank pages
- the four-engine same-page comparison requirement is satisfied on `T1-p001`, and full-pass runs now exist for `RapidOCR`, `PaddleOCR PP-OCRv4`, and `Tesseract`
- `PaddleOCR` now also has a full pass with `PP-OCRv4` under Python `3.12`, but the default `PP-OCRv5` path still crashes on this machine
- `Tesseract` required the witness-local `ocr/T1/tessdata/chi_tra.traineddata`; a first full-pass attempt failed until `TESSDATA_PREFIX` was pointed at that directory
- the original saved Paddle `.txt` companions are empty on this machine even where the JSON has OCR text; use `extracted-text/` derivatives instead
- the raw extracted Paddle text can also have unstable ordering on vertical pages; use it as support rather than as an unchallenged final reading
- `T1` is not a pure poem-only object: `p001-p004` title or imprint matter, `p005-p006` prefatory prose, `p007-p080` commentary-dominant pages with embedded poem lemmata, `p081-p082` tail material, and `p083` blank
- `T4` is not a pure poem-only physical object: only `p002-p004` belong to the target text body in the current page-role pass
- `T5` is not a pure poem-only physical object: only `p004-p006` belong to the target text body in the current page-role pass
- `T3` is not a pure poem-only physical object: only `p034-p036` belong to the target text body in the current page-role pass
- `A1` is not a pure poem-only physical object: only `p003-p008` belong to the target text body in the current page-role pass
- `A2` is a derivative witness rather than a short poem-only object: the current page-role pass treats `p002-p044` as the main derivative body span
- `A3` is also a derivative anthology witness rather than a short poem-only object: the current page-role pass treats only `p003-p011` as the Faith in Mind target body span inside a much larger anthology volume
- the rendered `A3` page images are too large for practical full-res OCR on this workstation (`13471x12300` at `200` DPI), so the saved `A3` OCR passes use explicitly logged `ocr-input-120dpi/` JPEG derivatives as OCR input
- `C1` is a Japanese translation or reception control rather than a base-text witness: only `p051-p052` belong to the target `信心銘和譯` span in the current page-role pass
- `C1` now has full four-engine OCR compliance on the direct rendered `page-images/` basis; unlike `T2` and `A3`, no derivative OCR-input basis was required on this machine
- `C2` is also a Japanese translation or reception control rather than a base-text witness: only `p021-p023` belong to the target `三祖大師信心銘` span in the current page-role pass, and the opening and closing images are mixed-content boundary spreads
- on this machine, prefer Python `3.12` for PaddleOCR and related tooling instead of the default Python `3.14`
- the local OCR tool stack is uneven; machine health must be logged honestly rather than assumed
- only the title lines and a broad recovered lemma-line spine through `T1-p079.l01` have been corrected so far; most prose remains uncorrected

## Open these first when resuming

1. `provenance/faith-in-mind/process/current-state.md`
2. `provenance/faith-in-mind/process/human-log.md`
3. `provenance/faith-in-mind/process/decision-log.md`
4. `provenance/faith-in-mind/process/ocr-environment.md`
5. `provenance/faith-in-mind/process/ocr-run-log.md`
6. `provenance/faith-in-mind/transcription/ocr-transcription-plan.md`
7. `xml-open/ce/faith-in-mind/timeline.json`
