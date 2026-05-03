# Current State: Faith in Mind

Date: 2026-05-02
Status: active
Edition slug: `faith-in-mind`

## Resume summary

- Witness set: locked
- Scope: broader
- Copy-text: `T1` locked as starting spine, switch allowed only by logged evidence-based decision
- Current phase: `manual_correction_pass_1_started`
- Last completed phase: `manual_correction_slice_T1_second_pass_p032_right_edge_paired_category_line_recovery`

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
- `C1` page roles isolate `C1-p051` to `C1-p052` as the target `ä¿¡å¿ƒéŠ˜å’Œè­¯` span, with `C1-p001` to `C1-p005` as wrapper or contents matter, `C1-p006` to `C1-p050` as earlier anthology or translation material, `C1-p053` to `C1-p075` as later anthology or translation material, and `C1-p076` as rear cover matter
- a full `RapidOCR` pass now exists for `C1` under `ocr/C1/ocr/rapidocr/`
- a full `tesseract` pass now exists for `C1` under `ocr/C1/ocr/tesseract-full-pass/`
- a full `PaddleOCR PP-OCRv4` pass now exists for `C1` under `ocr/C1/ocr/paddleocr-ppocrv4/`
- derived Paddle text support now exists for `C1` under `ocr/C1/ocr/paddleocr-ppocrv4/extracted-text/`
- a full `EasyOCR` pass now exists for `C1` under `ocr/C1/ocr/easyocr-full-pass/`
- `C1` now has full recorded four-engine OCR compliance and is ready for bounded comparison use as a translation or reception control witness
- a bounded `C1` comparison slice now exists and confirms broad transmitted order plus the standard close as a translation or reception control witness, without exposing a new high-confidence repair locus
- `C2` is now opened as the next commentary or translation control witness with in-package metadata, rendered page images, and a classified page map
- `C2` page roles isolate `C2-p021` to `C2-p023` as the target `ä¸‰ç¥–å¤§å¸«ä¿¡å¿ƒéŠ˜` span, with `C2-p020`, `C2-p032`, `C2-p060`, and `C2-p094` as section-divider title pages and the remaining rendered part-volume as non-target anthology or liturgical material
- a first full `RapidOCR` pass now exists for `C2` under `ocr/C2/ocr/rapidocr/`
- a full `tesseract` pass now also exists for `C2` under `ocr/C2/ocr/tesseract-full-pass/`
- a full `PaddleOCR PP-OCRv4` pass now also exists for `C2` under `ocr/C2/ocr/paddleocr-ppocrv4/`
- derived Paddle text support now exists for `C2` under `ocr/C2/ocr/paddleocr-ppocrv4/extracted-text/`
- a full `EasyOCR` pass now also exists for `C2` under `ocr/C2/ocr/easyocr-full-pass/`
- `C2` now has full recorded four-engine OCR compliance and is ready for bounded comparison use as a translation or reception control witness
- `C3` is now opened as the next commentary control witness with in-package metadata, rendered page images, and a classified page map
- `C3` page roles isolate `C3-p004` to `C3-p056` as the main `ä¿¡å¿ƒéŠ˜è¬›è©±` commentary body span, with wrapper or title matter on `C3-p001` to `C3-p003`, publisher or colophon tail matter on `C3-p057` to `C3-p059`, and rear wrapper or library tail matter on `C3-p060` to `C3-p063`
- a first full `RapidOCR` pass now exists for `C3` under `ocr/C3/ocr/rapidocr/`
- a full `tesseract` pass now also exists for `C3` under `ocr/C3/ocr/tesseract-full-pass/`
- a full `PaddleOCR PP-OCRv4` pass now also exists for `C3` under `ocr/C3/ocr/paddleocr-ppocrv4/`
- derived Paddle text support now exists for `C3` under `ocr/C3/ocr/paddleocr-ppocrv4/extracted-text/`
- a full `EasyOCR` pass now also exists for `C3` under `ocr/C3/ocr/easyocr-full-pass/`
- `C3` now has full recorded four-engine OCR compliance and is ready for bounded comparison use as a commentary control witness
- a bounded `C3` commentary-control comparison slice now exists and confirms broad commentary-backed support for the recovered `T1` lemma spine plus the standard close, without exposing a new high-confidence repair locus
- `C4` is now opened as the next commentary control witness with in-package metadata, rendered page images, and a classified page map
- `C4` page roles isolate `C4-p005` to `C4-p022` as the main `ä¿¡å¿ƒéŠ˜æ‹ˆæ` commentary body span, with wrapper or title matter on `C4-p001` to `C4-p004`, a mixed terminal body-plus-colophon spread on `C4-p023`, and tail or wrapper matter on `C4-p024` to `C4-p026`
- a first full `RapidOCR` pass now exists for `C4` under `ocr/C4/ocr/rapidocr/`
- a full `tesseract` pass now also exists for `C4` under `ocr/C4/ocr/tesseract-full-pass/`
- a full `PaddleOCR PP-OCRv4` pass now also exists for `C4` under `ocr/C4/ocr/paddleocr-ppocrv4/`
- derived Paddle text support now exists for `C4` under `ocr/C4/ocr/paddleocr-ppocrv4/extracted-text/`
- a full `EasyOCR` pass now also exists for `C4` under `ocr/C4/ocr/easyocr-full-pass/`
- `C4` now has full recorded four-engine OCR compliance and is ready for bounded comparison use as a commentary control witness
- a bounded `C4` commentary-control comparison slice now exists and confirms broad commentary-backed support for the recovered `T1` lemma spine plus the standard close, without exposing a new high-confidence repair locus
- `C5` is now opened as the next commentary control witness with in-package metadata, rendered page images, and a classified page map
- `C5` page roles isolate `C5-p004` to `C5-p072` as the main `å† è¨»ä¿¡å¿ƒéŠ˜å¤œå¡˜æ°´` commentary body span, with front matter on `C5-p001` to `C5-p003`, an explicit terminal page on `C5-p073`, and rear wrapper or library-tail matter on `C5-p074`
- a first full `RapidOCR` pass now exists for `C5` under `ocr/C5/ocr/rapidocr/`
- a full `tesseract` pass now also exists for `C5` under `ocr/C5/ocr/tesseract-full-pass/`
- a full `PaddleOCR PP-OCRv4` pass now also exists for `C5` under `ocr/C5/ocr/paddleocr-ppocrv4/`
- derived Paddle text support now exists for `C5` under `ocr/C5/ocr/paddleocr-ppocrv4/extracted-text/`
- a full `EasyOCR` pass now also exists for `C5` under `ocr/C5/ocr/easyocr-full-pass/`
- `C5` now has full recorded four-engine OCR compliance and is ready for bounded comparison use as a commentary control witness
- a bounded `C5` commentary-control comparison slice now exists and confirms broad commentary-backed support for the recovered `T1` lemma spine across the `å·»ä¸Š` body, without exposing a new high-confidence repair locus
- `C6` is now opened as the next commentary control witness with in-package metadata, rendered page images, and a classified page map
- `C6` page roles treat `C6-p001` as a mixed title-plus-opening spread, `C6-p002` to `C6-p058` as the main `å† è¨»ä¿¡å¿ƒéŠ˜å¤œå¡˜æ°´` `å·»ä¸‹` commentary body, `C6-p059` as a mixed terminal body-plus-colophon spread, and `C6-p060` to `C6-p061` as rear wrapper or library-tail matter
- a full `RapidOCR` pass now exists for `C6` under `ocr/C6/ocr/rapidocr/`
- a full `tesseract` pass now exists for `C6` under `ocr/C6/ocr/tesseract-full-pass/`
- a full `PaddleOCR PP-OCRv4` pass now exists for `C6` under `ocr/C6/ocr/paddleocr-ppocrv4/`
- derived Paddle text support now exists for `C6` under `ocr/C6/ocr/paddleocr-ppocrv4/extracted-text/`
- a repaired full `EasyOCR` pass now exists for `C6` under `ocr/C6/ocr/easyocr-full-pass/`
- `C6` now has full recorded four-engine OCR compliance and is ready for bounded comparison use as a commentary control witness
- a bounded `C6` commentary-control comparison slice now exists and confirms broad commentary-backed support for the recovered `T1` lemma spine across the `å·»ä¸‹` continuation of the `å¤œå¡˜æ°´` tradition, without exposing a new high-confidence repair locus
- `C7` is now opened as the next Kyoto commentary-control witness with in-package metadata and a classified page map
- `C7` page roles treat `C7-p001` to `C7-p003` as wrapper or title matter, `C7-p004` to `C7-p005` as prefatory or front matter, `C7-p006` to `C7-p043` as the main `ä¿¡å¿ƒéŠ˜æ‹ˆæ` commentary body, `C7-p044` as publication or colophon matter, and `C7-p045` to `C7-p046` as rear wrapper or tail matter
- a full `RapidOCR` pass now exists for `C7` under `ocr/C7/ocr/rapidocr/`
- a full `tesseract` pass now exists for `C7` under `ocr/C7/ocr/tesseract-full-pass/`
- a full `PaddleOCR PP-OCRv4` pass now exists for `C7` under `ocr/C7/ocr/paddleocr-ppocrv4/`
- derived Paddle text support now exists for `C7` under `ocr/C7/ocr/paddleocr-ppocrv4/extracted-text/`
- a full `EasyOCR` pass now exists for `C7` under `ocr/C7/ocr/easyocr-full-pass/`
- `C7` now has full recorded four-engine OCR compliance and is ready for bounded comparison use as a Kyoto commentary control witness
- a bounded `C7` commentary-control comparison slice now exists and confirms broad Kyoto commentary-backed support for the recovered `T1` lemma spine and transmitted macro-sequence, without exposing a new high-confidence repair locus
- `C8` is now opened as the next commentary-control witness with in-package metadata, rendered page images, and a classified page map
- `C8` page roles treat `C8-p001` to `C8-p002` as title matter, `C8-p003` to `C8-p029` as the main `ä¿¡å¿ƒéŠ˜æ‹ˆæ - å¤ªç¥–å¼˜å¾³å††æ˜Žå›½å¸«` commentary body, `C8-p030` as a mixed closing page with explicit end marker plus publication matter, `C8-p031` as blank tail, and `C8-p032` to `C8-p033` as modern back matter or tail
- a full `RapidOCR` pass now exists for `C8` under `ocr/C8/ocr/rapidocr/`
- a full `tesseract` pass now exists for `C8` under `ocr/C8/ocr/tesseract-full-pass/`
- a full `PaddleOCR PP-OCRv4` pass now exists for `C8` under `ocr/C8/ocr/paddleocr-ppocrv4/`
- derived Paddle text support now exists for `C8` under `ocr/C8/ocr/paddleocr-ppocrv4/extracted-text/`
- a full `EasyOCR` pass now exists for `C8` under `ocr/C8/ocr/easyocr-full-pass/`
- `C8` now has full recorded four-engine OCR compliance and is ready for bounded comparison use as a commentary control witness
- a bounded `C8` commentary-control comparison slice now exists and confirms broad NDL commentary-backed support for the recovered `T1` lemma spine and transmitted macro-sequence, without exposing a new high-confidence repair locus
- `C9` is now opened as the next commentary-control witness with in-package metadata, rendered page images, and a classified page map
- `C9` page roles treat `C9-p001` to `C9-p002` as title matter, `C9-p003` to `C9-p074` as the main `ä¿¡å¿ƒéŠ˜å¤œå¡˜æ°´ - å¢—å† å‚è¨» å·»ä¸Š` commentary body, and `C9-p075` to `C9-p076` as tail or wrapper matter
- the package has now adopted the six-log forensic provenance protocol as binding workflow law and the missing forensic log surfaces now exist under `process/`
- the first bounded forensic-provenance reconstruction slice is now complete on the high-value contested `T1` loci
- the second bounded forensic-provenance reconstruction slice is now complete on the stabilized `T1` poem band around `p022-p030` and `p060-p063`
- the third bounded forensic-provenance reconstruction slice is now complete on the stabilized `T1` opening run around `p008-p019`
- the fourth bounded forensic-provenance reconstruction slice is now complete on the stabilized `T1` central band around `p024-p041`
- the fifth bounded forensic-provenance reconstruction slice is now complete on the stabilized `T1` middle-late band around `p042-p059`
- the sixth bounded forensic-provenance reconstruction slice is now complete on the stabilized `T1` late band around `p061-p074`
- the consolidation review now finds the reconstructed forensic coverage materially sufficient across the stabilized `T1` poem spine
- the package now has a validation entrypoint at `scripts/validate_package.py`
- a full `RapidOCR` pass now exists for `C9` under `ocr/C9/ocr/rapidocr/`
- a full `tesseract` pass now exists for `C9` under `ocr/C9/ocr/tesseract-full-pass/`
- a full `PaddleOCR PP-OCRv4` pass now exists for `C9` under `ocr/C9/ocr/paddleocr-ppocrv4/`
- derived Paddle text support now exists for `C9` under `ocr/C9/ocr/paddleocr-ppocrv4/extracted-text/`
- a full `EasyOCR` pass now exists for `C9` under `ocr/C9/ocr/easyocr-full-pass/`
- `C9` now has full recorded four-engine OCR compliance and is ready for bounded comparison use as a commentary control witness
- a bounded `C9` commentary-control comparison slice now exists and confirms broad NDL commentary-backed support for the recovered `T1` lemma spine and transmitted macro-sequence, without exposing a new high-confidence repair locus
- `C10` is now opened as the next commentary-control witness with in-package metadata, rendered page images, and a classified page map
- `C10` page roles treat `C10-p001` to `C10-p002` as title matter, `C10-p003` to `C10-p062` as the main `ä¿¡å¿ƒéŠ˜å¤œå¡˜æ°´ - å¢—å† å‚è¨» å·»ä¸‹` commentary body, `C10-p063` as terminal colophon or imprint matter, and `C10-p064` to `C10-p065` as blank or wrapper tail matter
- a full `RapidOCR` pass now exists for `C10` under `ocr/C10/ocr/rapidocr/`
- a full `tesseract` pass now exists for `C10` under `ocr/C10/ocr/tesseract-full-pass/`
- a full `PaddleOCR PP-OCRv4` pass now exists for `C10` under `ocr/C10/ocr/paddleocr-ppocrv4/`
- derived Paddle text support now exists for `C10` under `ocr/C10/ocr/paddleocr-ppocrv4/extracted-text/`
- a full `EasyOCR` pass now exists for `C10` under `ocr/C10/ocr/easyocr-full-pass/`
- `C10` now has full recorded four-engine OCR compliance and is ready for bounded comparison use as a commentary control witness
- a bounded `C10` commentary-control comparison slice now exists and confirms broad NDL commentary-backed support for the recovered `T1` lemma spine and transmitted macro-sequence, without exposing a new high-confidence repair locus
- `C11` is now opened as the next commentary-control witness with in-package metadata, rendered page images, and a classified page map
- `C11` page roles treat `C11-p001` to `C11-p003` as cover, title, or prefatory matter and `C11-p004` to `C11-p100` as the active `ä¿¡å¿ƒéŠ˜å¤œå¡˜æ°´è¬›ç¾©` lecture body within part 1
- a full `RapidOCR` pass now exists for `C11` under `ocr/C11/ocr/rapidocr/`
- a full `tesseract` pass now exists for `C11` under `ocr/C11/ocr/tesseract-full-pass/`; all `100` text sidecars are present, although the resumed summary undercounts at `99` pages with text because `C11-p060` was not re-entered into the summary array
- a full `PaddleOCR PP-OCRv4` pass now exists for `C11` under `ocr/C11/ocr/paddleocr-ppocrv4/`
- derived Paddle text support now exists for `C11` under `ocr/C11/ocr/paddleocr-ppocrv4/extracted-text/`
- a full `EasyOCR` pass now exists for `C11` under `ocr/C11/ocr/easyocr-full-pass/`
- `C11` now has full recorded four-engine OCR compliance and is ready for bounded comparison use as a lecture commentary control witness
- a bounded `C11` lecture-commentary-control comparison slice now exists and confirms broad opening and central-sequence support for the recovered `T1` lemma spine without exposing a new high-confidence repair locus
- `C11` is part 1 of a lecture pair and is not being used for a complete terminal-close judgment; the queue now moves to `C12`
- `C12` is now opened as the next lecture commentary control witness with in-package metadata, rendered page images, and a classified page map
- `C12` page roles treat `C12-p001` to `C12-p094` as active `ä¿¡å¿ƒéŠ˜å¤œå¡˜æ°´è¬›ç¾©` part 2 lecture body, `C12-p095` as publication or colophon matter, `C12-p096` to `C12-p099` as publisher catalogue or advertising matter, and `C12-p100` as rear wrapper or library-tail matter
- a full resumed `RapidOCR` pass now exists for `C12` under `ocr/C12/ocr/rapidocr/`
- a full `tesseract` pass now exists for `C12` under `ocr/C12/ocr/tesseract-full-pass/`
- a full resumed `PaddleOCR PP-OCRv4` pass now exists for `C12` under `ocr/C12/ocr/paddleocr-ppocrv4/`
- derived Paddle text support now exists for `C12` under `ocr/C12/ocr/paddleocr-ppocrv4/extracted-text/`
- a full resumed `EasyOCR` pass now exists for `C12` under `ocr/C12/ocr/easyocr-full-pass/`
- `C12` now has full recorded four-engine OCR compliance and is ready for bounded comparison use as the part 2 lecture commentary control witness
- a bounded `C12` lecture-commentary-control comparison slice now exists and confirms broad central, late, and terminal-close support for the recovered `T1` lemma spine without exposing a new high-confidence repair locus or accepted `T1` text change
- `C13` is now opened as the next commentary control witness with in-package metadata, rendered page images, and a classified page map
- `C13` page roles treat `C13-p001` as front wrapper or cover/title material, `C13-p002` as mixed title plus opening body, and `C13-p003` to `C13-p100` as active `é€šä¿—ä¿¡å¿ƒéŠ˜è¬›è©±` part 1 commentary body
- a full `RapidOCR` pass now exists for `C13` under `ocr/C13/ocr/rapidocr/`
- a full resumed `tesseract` pass now exists for `C13` under `ocr/C13/ocr/tesseract-full-pass/`
- a full resumed `PaddleOCR PP-OCRv4` pass now exists for `C13` under `ocr/C13/ocr/paddleocr-ppocrv4/`
- derived Paddle text support now exists for `C13` under `ocr/C13/ocr/paddleocr-ppocrv4/extracted-text/`
- a full resumed `EasyOCR` pass now exists for `C13` under `ocr/C13/ocr/easyocr-full-pass/`
- `C13` now has full recorded four-engine OCR compliance and is ready for bounded comparison use as the part 1 `é€šä¿—ä¿¡å¿ƒéŠ˜è¬›è©±` commentary control witness
- a bounded `C13` commentary-control comparison slice now exists and confirms broad opening, central one-mind/all-dharmas, and early quoted terminal-anchor support for the recovered `T1` lemma spine without exposing a new high-confidence repair locus or accepted `T1` text change
- `C14` is now opened as the next commentary control witness with in-package metadata, rendered page images, and a classified page map
- `C14` page roles treat `C14-p001` to `C14-p008` as active `é€šä¿—ä¿¡å¿ƒéŠ˜è¬›è©±` part 2 continuation body, `C14-p009` as mixed terminal body plus publication or colophon matter, `C14-p010` to `C14-p013` as publisher catalogue or advertising matter, and `C14-p014` to `C14-p015` as rear wrapper, rear cover, or library-tail matter
- a full `RapidOCR` pass now exists for `C14` under `ocr/C14/ocr/rapidocr/`
- a full `tesseract` pass now exists for `C14` under `ocr/C14/ocr/tesseract-full-pass/`; the accepted saved pass uses logged `ocr/C14/ocr-input-120dpi/` JPEG derivatives because the direct `150` DPI PNG run completed only `C14-p001` before a ten-minute timeout
- a full `PaddleOCR PP-OCRv4` pass now exists for `C14` under `ocr/C14/ocr/paddleocr-ppocrv4/`
- derived Paddle text support now exists for `C14` under `ocr/C14/ocr/paddleocr-ppocrv4/extracted-text/`
- a full `EasyOCR` pass now exists for `C14` under `ocr/C14/ocr/easyocr-full-pass/`
- `C14` now has full recorded four-engine OCR compliance and is ready for bounded comparison use as the part 2 commentary control witness
- a bounded `C14` commentary-control comparison slice now exists and confirms late scale/nondual, late branch, and terminal-close commentary support for the recovered `T1` lemma spine without exposing a new high-confidence repair locus or accepted `T1` text change
- `C15` is now opened as the next study control witness with in-package metadata, rendered page images, and a classified page map
- `C15` page roles treat `C15-p001` as front cover or library calibration, `C15-p002` as blank or front endpaper, `C15-p003` as title page, `C15-p004` as dedication or inscription matter, `C15-p005` as preface, `C15-p006` as mixed preface plus contents, and `C15-p007` to `C15-p100` as active study body
- a full resumed `RapidOCR` pass now exists for `C15` under `ocr/C15/ocr/rapidocr/`
- a full resumed `tesseract` pass now exists for `C15` under `ocr/C15/ocr/tesseract-full-pass/`
- a full resumed `PaddleOCR PP-OCRv4` pass now exists for `C15` under `ocr/C15/ocr/paddleocr-ppocrv4/`
- derived Paddle text support now exists for `C15` under `ocr/C15/ocr/paddleocr-ppocrv4/extracted-text/`
- a full resumed `EasyOCR` pass now exists for `C15` under `ocr/C15/ocr/easyocr-full-pass/`
- `C15` now has full recorded four-engine OCR compliance and is ready for bounded comparison use as a study control witness
- a bounded `C15` study-control comparison slice now exists and broadly confirms the recovered `T1` lemma spine and standard close without exposing a new high-confidence repair locus or accepted `T1` text change
- `C16` is now opened as the next commentary-related control witness with a continuous `256`-page image set rendered from the three locked Commons PDFs
- `C16` page roles treat `C16-p001` as front cover, `C16-p002` as blank front endpaper, `C16-p003` as title page, `C16-p004` to `C16-p005` as preface or author-note matter, `C16-p006` to `C16-p011` as contents or front matter, `C16-p012` to `C16-p249` as the active commentary-related body, `C16-p250` to `C16-p255` as publisher catalogue or advertising matter, and `C16-p256` as rear blank or wrapper-tail matter
- a full resumed `RapidOCR` pass now exists for `C16` under `ocr/C16/ocr/rapidocr/` on the logged `ocr-input-120dpi/` derivative basis
- a full resumed `tesseract` pass now exists for `C16` under `ocr/C16/ocr/tesseract-full-pass/` on the same logged `ocr-input-120dpi/` basis
- a full resumed `PaddleOCR PP-OCRv4` pass now exists for `C16` under `ocr/C16/ocr/paddleocr-ppocrv4/`
- derived Paddle text support now exists for `C16` under `ocr/C16/ocr/paddleocr-ppocrv4/extracted-text/`
- a full resumed `EasyOCR` pass now exists for `C16` under `ocr/C16/ocr/easyocr-full-pass/` on the logged `ocr-input-90dpi/` derivative basis
- `C16` now has full recorded four-engine OCR compliance
- a bounded `C16` control check now exists and closes `C16` as a non-overlap related-control witness rather than a usable `Faith in Mind` lemma witness
- `C17` is now opened as the next commentary-related control witness with a continuous `218`-page image set rendered from the three locked Commons PDFs
- `C17` page roles treat `C17-p001` as front cover, `C17-p002` as blank front endpaper or inside cover, `C17-p003` as title page, `C17-p004` to `C17-p009` as preface or table-of-contents matter, `C17-p010` to `C17-p200` as non-target series body, `C17-p201` to `C17-p214` as the active `ä¸­å³°å’Œå°šä¿¡å¿ƒéŠ˜ç¾©è§£` target segment, `C17-p215` as publication colophon, `C17-p216` as blank rear endpaper, `C17-p217` as rear pastedown or inside wrapper, and `C17-p218` as rear cover
- the `C17` opening notes explicitly record that the final `18`-page PDF segment contains the Faith in Mind target material but that its internal printed-page order is not monotonic by rendered image index
- logged `ocr-input-120dpi/` and `ocr-input-90dpi/` derivative JPEG sets now exist for `C17` to keep long-witness OCR computationally manageable on this workstation
- a full resumed `RapidOCR` pass now exists for `C17` under `ocr/C17/ocr/rapidocr/` on the logged `ocr-input-120dpi/` derivative basis
- a full resumed `tesseract` pass now exists for `C17` under `ocr/C17/ocr/tesseract-full-pass/` and closes at `218/218` pages with only familiar tiny-fragment warnings and no recorded engine errors
- a full `PaddleOCR PP-OCRv4` pass under Python `3.12` now exists for `C17` under `ocr/C17/ocr/paddleocr-ppocrv4/` and closes at `218` success pages with `0` recorded errors
- derived Paddle support text now exists for `C17` under `ocr/C17/ocr/paddleocr-ppocrv4/extracted-text/`
- a full `EasyOCR` pass now exists for `C17` under `ocr/C17/ocr/easyocr-full-pass/` and closes at `218` processed pages with text on `205`, leaving only `C17-p002`, `C17-p216`, `C17-p217`, and `C17-p218` empty, and no recorded engine errors
- `C17` now has full recorded four-engine OCR compliance and is ready for bounded comparison use as a commentary-related control witness
- the package now has a witness-page coverage audit for the active non-blank `T1` span at `scripts/audit_witness_page_coverage.py`

- `T1-p031.l01 = ç¸±æœ‰æ˜¯éžç´›ç„¶å¤±å¿ƒ` and `T1-p031.l05 = ä¸è¦‹å¤œä¾†ä¾èˆŠå®¿è˜†èŠ±` are now secured from direct image inspection plus local OCR support.
- `T1-p032.l02 = æ˜¯è½‰å¥ä¸è¦‹ä¸€è‰²å§‹æ˜¯åŠææ›´é ˆçŸ¥æœ‰å…¨æ`, `T1-p032.l04 = è¨€è¬è¨€ç§–æ˜¯ä¸€è¨€åƒæ³•è¬æ³•ç§–æ˜¯ä¸€æ³•å¾—åˆ°`, `T1-p032.l08 = æ­¤è™•äº¦é ˆè½‰å´è‹¥å®ˆä½å…¶ä¸€ä¾¿æ˜¯ç¹«é©¢æ©›æ‰€`, and `T1-p032.l09 = ç›¡åæ–¹ä¸€å¥è¶…è¬è±¡åƒå¥è¬å¥ç§–æ˜¯ä¸€å¥åƒ` are now secured from direct image inspection plus local OCR support and bounded `C9` phrase confirmation.
- `T1-p032.l06 = ç®‡ä¸»äººå…¬ç„¡äºŒç„¡åˆ¥å¤äººä¸å¾—å·²è€Œå–šä½œ` and `T1-p032.l07 = ä¼¼é›²é–€é“ç›´å¾—è“‹ä¹¾å¤å¤§åœ°ç„¡çµ²æ¯«éŽæ‚£` are now also secured from direct image inspection plus local OCR support.
- `T1-p032.l03 = å¤±ä¸€åˆ‡å–æ¨ä¸€åˆ‡æ†Žæ„›ä¸€åˆ‡æ˜¯éžéƒ½è™›ç§–æ˜¯` is now also secured from direct image inspection plus local OCR support and bounded `C9` phrase confirmation.

## Next action

Open `provenance/faith-in-mind/process/CONTINUATION_GATE.md` and `provenance/faith-in-mind/process/STATUS_REPORT_GATE.md` before deciding a correction or comparison run is done or before writing any status report.

The first end-to-end commentary continuation has already closed at the real terminal page `T1-p083`, and the second pass is now active from the earliest unresolved prose. The second-pass recoveries now include `T1-p007.l07 = é‚„æ§‹å¾—éº¼ç§–é€™è‡³é“ç„¡é›£è¨€ç«¯èªžç«¯éžä½†`, `T1-p008.l08 = æ˜¯ç®‡ç„¡äº‹åº•é“äººè‹¥æ„æ ¹ä¸æ–·è¦‹è§£ä¸å¿˜`, `T1-p011.l01 = é”é †ç›¸çˆ­æ˜¯ç‚ºå¿ƒç—…`, `T1-p011.l02 = ä½•å¾—ç›¸æ‡‰åŽ»å¤§åœ°é›ªæ¼«æ¼«æ˜¥ä¾†ä¾èˆŠå¯’`, `T1-p011.l03 = æ˜Žè‡ªå·±ä¸äº†ç›®å‰æ­¤äººç§–å…·ä¸€éš»çœ¼è‹¥äº†ç›®`, `T1-p011.l05 = è‹¥å¾—æéº¼åŽ»é€†ä¹Ÿä¸è¦‹é †ä¹Ÿä¸è¦‹é ­`, `T1-p011.l06 = ç¶ è‰ä¾†è±ˆä¸è¦‹é´»å±±äºŒåå¹´ä¸åƒç¦ªä¸å­¸é“`, `T1-p011.l08 = ä¸€æ™‚åæ–·å–šä½œå¸¸å…‰ç¾å‰å¿µå¿µä¸æ˜§è‹¥åª`, `T1-p012.l01 = ä½ é“æˆ–æ˜¯æˆ–éžäººä¸è­˜é€†è¡Œé †è¡Œå¤©èŽ«æ¸¬è¿Ž`, `T1-p012.l03 = å¸«äº‘è€Œä»Šæéº¼è€…å¤šä¸æéº¼è€…å°‘æˆç¾¤ä½œéšŠ`, `T1-p012.l04 = ä¾¿æ˜¯æ„›ä¸çŸ¥æ†Žæ„›æ˜¯å¿ƒé•é †æ˜¯å¢ƒå› å°é †å¢ƒ`, `T1-p012.l05 = æœ‰è¨±å¤šèˆ¬ç—…å¦‚ä½•æ•‘å¾—åˆ¥äºº`, `T1-p012.l06 = æ˜¯æˆ‘è‡ªå¿ƒè£å¦„å€’`, `T1-p012.l07 = æ˜¯æ³•åŸ·ç¸½æ˜¯å¿ƒç—…åƒç¦ªç§–è¦å®‰æ¨‚ä½ è‚šè£¹`, `T1-p012.l08 = å¦‚éº»ä¼¼ç²Ÿæ²’é‡å¤§äººä½œé€™è¦‹è§£ä¸æ˜¯`, `T1-p012.l09 = å‰‡èµ·æ„›å¿ƒé‡é•æƒ…å‰‡èµ·çž‹å¿ƒæ—¢ä¸äº†é•é †`, `T1-p012.l10 = è‡ªç”Ÿæ†Žæ„›è‡ªé”è‡ªé•`, `T1-p014.l07 = æŽ›è§’ä¸ç”¨é³¥é“è™›çŽ„äº”è‰²ä¸èƒ½ç›²äº”éŸ³ä¸èƒ½äº‚`, `T1-p015.l04 = æ»¿ç„¡éš›åœ¨å‡¡å¤«å–šä½œå‡¡å¤«æ³•åœ¨è–äººå–šä½œè–äºº`, `T1-p015.l06 = äººæ³•æœ¬ç„¡æ¬ å°‘äº¦ç„¡é¤˜å‰Œåœ¨ä»€éº¼è™•å‹˜`, `T1-p016.l04 = ç¥–å¸«éº¼äº‘è‰¯ä¹…æ‡‰é ˆæéº¼æœƒæ–¹å§‹å¥‘å¦‚`, `T1-p016.l05 = å¹³åœ°ä¸Šæ­»äººç„¡æ•¸å¦‚ä»Šæèµ·æ´»æ–å­å‘ç™¾è‰`, `T1-p016.l06 = ç¤ºè¡†äº‘æ–¬é‡˜æˆªéµé–€å‰è‰æ·±ä¸€ä¸ˆç ´äºŒä½œä¸‰`, `T1-p016.l08 = æ˜¯å–ä¸å¾—æ¨ä¸å¾—ä¸å¯å¾—ä¸­æéº¼å¾—é‚„è¦‹`, `T1-p017.l05 = é ­å‡ºé ­æ²’ä½ å¦‚ä»Šè¦ä¸é€æœ‰ç·£éº¼é ˆæ˜¯æˆªæ–·`, `T1-p017.l06 = é€ä»–æœƒæ„›å–æ¨é€ æ¥­å—å ±å‘è¼ªè¿´ç”Ÿæ­»æµ·è£`, `T1-p018.l01 = ä¸€ç¨®å¹³æ‡·æ³¯ç„¶è‡ªç›¡`, `T1-p018.l08 = è‰¯ä¹…æš—è£æŠ½æ©«éª¨æ˜Žä¸­åèˆŒé ­`, `T1-p018.l09 = æ–¹çŸ¥æœ‰å‘ä¸Šäº‹ä¿—ä¸”é“ä½œéº¼ç”Ÿæ˜¯å‘ä¸Šäº‹`, `T1-p019.l03 = å¸«äº‘çš®è†šè„«è½ç›¡å”¯æœ‰ä¸€çœŸå¯¦è€€å¤é¨°ä»Šæ˜Ž`, `T1-p020.l03 = ä½œä»€éº¼å‹•æ˜¯ä½•ç‰©éœæ˜¯ä»€éº¼ä¸å¯æœ‰å…©ç®‡ä¹Ÿ`, `T1-p021.l03 = å ªä½œä»€éº¼`, `T1-p021.l04 = å¸«æ‰“äº‘ç§–ç‚ºä½ å°‡èµ¤è‚‰åœ˜è¦æ‰›æˆ‘æ£’ä¸è­˜ç—›`, `T1-p021.l05 = ä½œéº¼ç”Ÿé“æ‹ç¦ªåºŠä¸€ä¸‹åŽ»ç™¾é›œç¢Ž`, `T1-p021.l09 = äº‚å‹•å…¨æ˜¯éœ`, `T1-p022.l02 = å…¨æ˜¯å‹•è£ä¸€ç„¡äºŒ`, `T1-p022.l03 = å¸«äº‘æœ‰ä»€éº¼æ•‘è™•å•ä½ æœ‰ä»€éº¼ç‰©æ•™ä½ é£`, `T1-p022.l04 = ç¨‹è¡Œ`, `T1-p022.l05 = é‡å`, `T1-p022.l06 = åæž¯æƒ…å¢ƒæ·»æ¼èŽ«é“å…©è™•å¤±åŠŸè‡´ä½¿`, `T1-p022.l07 = éŽæ°è‹¥ä¸€è™•é€åƒè™•è¬è™•ä¸€æ™‚é€`, `T1-p023.l01 = æ˜Žå¿ƒåœ°è¬æœ‰`, `T1-p023.l02 = ä½†æ­¢å…¶å‹•ä¾¿æ˜¯`, `T1-p023.l04 = æœ¬ä¾†ç„¡ç›¸`, `T1-p023.l05 = èƒŒå…¶çœŸç©ºè€Œä¸çŸ¥è¬æ³•ç•¶é«”æ˜¯çœŸç©ºè§¸ç‰©`, `T1-p023.l06 = è¬æœ‰å³è¿·å¦™æœ‰è½åœ¨æ–·è¦‹ç¦ªå’Œå­ä½†ä»”ç´°æ€`, `T1-p023.l10 = æœ‰å¾—æ–·ç©ºå³è¿·çœŸç©º`, `T1-p023.l11 = å…¶éœä¾¿æ˜¯ç©ºå…¸`, `T1-p024.l02 = å¸«äº‘ä½Žè²ä½ çº”é–‹å£ä¾¿æ²’äº¤æ¶‰äº†ä¹Ÿ`, `T1-p024.l03 = é£Ÿè§€å¤©ä¸Šæœˆå…‰å´å­¸ä¸­ç `, `T1-p024.l06 = æ˜¯ç©ºåç•°é«”åŒæ›´é»žä»–æ³•ä¸”é“é‡åœ¨ä»€éº¼è™•`, `T1-p024.l07 = æ•™ç„¡è¨€ä½•å¿…æ‹ˆèŠ±å¾®ç¬‘å‚³æ­£æ³•çœ¼è—ä½ è¦`, `T1-p024.l08 = æ™‚å¾—å‡ºåŽ»ç¦ªå’Œå­æ­¤äº‹è‹¥åœ¨è¨€å¥è£¹ä¸€å¤§è—`, `T1-p024.l09 = åœ¨è‘›è—¤çª è£å¦‚è·›é¼ˆç›²é¾œå…¥ç©ºè°·ç›¸ä¼¼`, `T1-p025.l02 = å¸«äº‘ä»€éº¼è™•å¾—æ¶ˆæ¯ä¾†å¯§å¯æˆªèˆŒ`, `T1-p025.l03 = ç«Ÿæˆå¾—ç®‡ä»€éº¼äº‹ä¸€å¤œè½èŠ±é›¨æ»¿åŸŽæµæ°´`, `T1-p025.l04 = ç›¸ä¼¼ä»¥ä½›ç¥–éž­å­å¾·å±±è‡¨æ¿Ÿæœ‰æ£’æœ‰å–`, `T1-p025.l05 = æ™ºéš”æƒ³é«”æ®Šè¦æ¼”èªžè·¯çµ•å¿ƒè¡Œè™•æ»…`, `T1-p026.l06 = å¯’å²©ç•°è‰é’åè‘—æ—¥é›²å®—ä¸å¦™`, `T1-p026.l09 = ç¦ªå’Œå­ä½ å¦‚ä»Šæ“¬`, `T1-p026.l10 = é–‹å£è¦è©±æœƒéš¨è¨€é€å¥ä¾¿`, `T1-p027.l07 = éº¼ç”Ÿé ˆå½Œé ‚ä¸Šç„¡æ ¹è‰ä¸å—æ˜¥é¢¨èŠ±è‡ªé–‹`, `T1-p027.l09 = å¸«äº‘ä½ å¾…ç¿»æ‚”é‚£å‰ä¾†é£æœ‰æ²’æœ‰å¾žç©ºèƒŒç©º`, `T1-p028.l04 = è¿´é¿ä¹‹è™•ç›´é¥’æéº¼å·²æ˜¯è‡ªçžž`, `T1-p028.l06 = å¸«äº‘è‡ªçŸ¥å³å¾—å‰ä¾†ç§ªç®¡è§€ç©ºåŽ»ç”Ÿæ»…å¿µ`, `T1-p028.l09 = é€™ç®‡ç”°åœ°é–‹ä¸€è½‰æ—¥ç”¨ä¹‹é–“åœ°æ›´ç„¡`, `T1-p029.l05 = è²ä¹ŸçœŸè‰²ä¹ŸçœŸå‹•éœä¹ŸçœŸèªžé»˜ä¹ŸçœŸå¦‚æ˜¯æ—¥`, `T1-p029.l07 = å¡«æºå¡žå£‘åƒè®Šè¬åŒ–å…¨é«”ä¸€çœŸä¸å‹•çµ²æ¯«`, `T1-p029.l08 = åˆ‡ç¾æˆæ›´ç„¡æ¬ å°‘ä½ ä½†æ‡‰ä¿‚æœ‰è¦‹ç©ºè¦‹ä½›è¦‹`, `T1-p029.l09 = ç”¨è¦‹èžè¦ºçŸ¥ç„¡ä¸ç´”çœŸç›´å¾—äº˜å¤§åœ°æ»¿å¤©ä¸‹`, and `T1-p029.l10 = å¸«äº‘ç¾æˆå…¬æ¡ˆä½ æ±‚ä»–ä½œéº¼è¦‹ä¹ŸçœŸèžä¹ŸçœŸ`. `T1-p081` and `T1-p082` remain visually confirmed non-blank tail matter, and `T1-p083` remains blank. The remaining unresolved loci on `T1-p007` are now `l03`, `l04`, `l08`, `l09`, and `l12`, while `T1-p011.l04`, `T1-p012.l02`, `T1-p014.l08`, `T1-p022.l08` to `T1-p022.l12`, and much of the remaining commentary prose from `T1-p007` to `T1-p080` remain materially open for continued second-pass work.

Use:

- `provenance/faith-in-mind/process/current-state.md`
- `provenance/faith-in-mind/process/human-log.md`
- `provenance/faith-in-mind/process/decision-log.md`
- `provenance/faith-in-mind/process/CONTINUATION_GATE.md`
- `provenance/faith-in-mind/process/translation-diff-log.md`
- `provenance/faith-in-mind/process/ocr-consensus-log.md`
- `provenance/faith-in-mind/process/rejected-readings-log.md`
- `provenance/faith-in-mind/process/translation-reasoning-log.md`
- `provenance/faith-in-mind/process/character-provenance-log.md`
- `provenance/faith-in-mind/witnesses/witness-register.md`
- `provenance/faith-in-mind/witnesses/acquisition-metadata.md`
- `provenance/faith-in-mind/transcription/corrected/T1-corrected-pass1-working.txt`
- `provenance/faith-in-mind/process/correction-log.md`
- `provenance/faith-in-mind/process/ocr-run-log.md`
- `provenance/faith-in-mind/ocr/T1/`
- `provenance/faith-in-mind/ocr/T4/`
- `provenance/faith-in-mind/ocr/T5/`
- `provenance/faith-in-mind/ocr/T2/`
- `provenance/faith-in-mind/ocr/T3/`
- `provenance/faith-in-mind/ocr/A1/`
- `provenance/faith-in-mind/ocr/A2/`
- `provenance/faith-in-mind/ocr/A3/`
- `provenance/faith-in-mind/ocr/C1/`
- `provenance/faith-in-mind/ocr/C2/`
- `provenance/faith-in-mind/ocr/C3/`
- `provenance/faith-in-mind/ocr/C4/`
- `provenance/faith-in-mind/ocr/C5/`
- `provenance/faith-in-mind/ocr/C13/`
- `provenance/faith-in-mind/ocr/C14/`
- `provenance/faith-in-mind/ocr/C15/`
- `provenance/faith-in-mind/ocr/C16/`
- `provenance/faith-in-mind/ocr/C17/`
- `provenance/faith-in-mind/process/ocr-run-log.md`
- `provenance/faith-in-mind/collation/first-pass-variant-table.md`

Produce next:

- continue bounded `T1` manual correction work with the locked witness set now fully opened, OCR-compliant, and comparison-checked through `C17`
- continue the unresolved `T1` commentary prose second pass from the remaining `T1-p029` and `T1-p030` residue, now especially `T1-p029.l02`, `T1-p029.l06`, and the rougher leftward `T1-p030` columns, while the earlier `T1-p007`, `T1-p011.l04`, `T1-p012.l02`, and `T1-p014.l08` holdouts remain open for later reinspection; the prefatory `T1-p005` to `T1-p006` block remains paused unless a new bounded evidence basis appears
- keep `C16` closed as a non-overlap related-control witness unless a later evidence-based reason requires reinspection
- keep `C17` closed as a corroborative commentary-related control witness unless a later locus-specific reason requires reinspection
- do not create a `T1` text change unless later witness work exposes a new high-confidence repair locus corroborated by the existing direct-witness record
- do not create translation diffs unless the accepted `T1` edition text changes
- keep `current-state.md`, `process-log.md`, `human-log.md`, `process.json`, `timeline.json`, `ocr-run-log.md`, and any collation notes aligned after the `C17` comparison closeout
- rerun `python scripts/validate_package.py` before any XML or publication handoff

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
`C5` has now also completed its first full `RapidOCR` pass.
`C5` has now also completed its full `tesseract` pass.
`C5` has now also completed its full `PaddleOCR PP-OCRv4` pass.
`C5` has now also completed its full `EasyOCR` pass.
`C5` has now also completed its first bounded commentary-control comparison slice.
`C6` through `C10` have each completed witness opening, four-engine OCR compliance, and first bounded commentary-control comparison.
`C11` has now completed its witness-opening slice, four-engine OCR-compliance slice, and first bounded lecture-commentary-control comparison slice.
`C12` has now completed its witness-opening slice, four-engine OCR-compliance slice, and first bounded lecture-commentary-control comparison slice.
`C13` has now completed its witness-opening slice, four-engine OCR-compliance slice, and first bounded commentary-control comparison slice.
`C14` has now completed its witness-opening slice, four-engine OCR-compliance slice, and first bounded commentary-control comparison slice.
`C15` has now completed its witness-opening slice, four-engine OCR-compliance slice, and first bounded study-control comparison slice.
`C16` has now completed its witness-opening slice, four-engine OCR-compliance slice, and first bounded comparison slice, but that slice closes it as a non-overlap related-control witness rather than as a usable `Faith in Mind` lemma witness.
`C17` has now completed its witness-opening slice, four-engine OCR-compliance slice, and first bounded commentary-related control comparison slice.
the bounded post-`C17` `T1` prefatory-prose continuation has now secured `T1-p005.l01`, `T1-p005.l02`, `T1-p005.l03`, `T1-p005.l09`, `T1-p006.l03`, `T1-p006.l06`, `T1-p006.l07`, and `T1-p006.l09`, and the remaining prefatory damage is now paused at an honest evidence wall rather than freely reconstructed.
the remaining uncovered `T1` `l01` surfaces in the audit are commentary-only or rollback exceptions (`T1-p012`, `T1-p016`, `T1-p020`, `T1-p023`, `T1-p075`) rather than unresolved poem-baseline failures

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
- `C1` is a Japanese translation or reception control rather than a base-text witness: only `p051-p052` belong to the target `ä¿¡å¿ƒéŠ˜å’Œè­¯` span in the current page-role pass
- `C1` now has full four-engine OCR compliance on the direct rendered `page-images/` basis; unlike `T2` and `A3`, no derivative OCR-input basis was required on this machine
- `C2` is also a Japanese translation or reception control rather than a base-text witness: only `p021-p023` belong to the target `ä¸‰ç¥–å¤§å¸«ä¿¡å¿ƒéŠ˜` span in the current page-role pass, and the opening and closing images are mixed-content boundary spreads
- `C16` is a long multi-part commentary-related control witness rather than a direct base-text witness; only `p012-p249` belong to the active body span in the current page-role pass
- the six-log forensic provenance protocol was adopted mid-project on `2026-04-18`, so retroactive reconstruction is now required before fresh witness work continues
- on this machine, prefer Python `3.12` for PaddleOCR and related tooling instead of the default Python `3.14`
- the local OCR tool stack is uneven; machine health must be logged honestly rather than assumed
- only the title lines and a broad recovered lemma-line spine through `T1-p079.l01` have been corrected so far; most prose remains uncorrected

## Open these first when resuming

1. `provenance/faith-in-mind/process/current-state.md`
2. `provenance/faith-in-mind/process/human-log.md`
3. `provenance/faith-in-mind/process/decision-log.md`
4. `provenance/faith-in-mind/process/CONTINUATION_GATE.md`
5. `provenance/faith-in-mind/process/STATUS_REPORT_GATE.md`
6. `provenance/faith-in-mind/process/ocr-environment.md`
7. `provenance/faith-in-mind/process/ocr-run-log.md`
8. `provenance/faith-in-mind/transcription/ocr-transcription-plan.md`
9. `xml-open/ce/faith-in-mind/timeline.json`
## Live manual-correction state
- `T1` second-pass commentary correction is active beyond `T1-p032`; `T1-p033.l08` is now secured from direct image review plus both Paddle support surfaces and the local `C9` control.
- `T1-p034.l04`, `T1-p034.l07`, and `T1-p034.l08` are now also secured from direct image review plus both Paddle support surfaces.
- `T1-p035.l02`, `T1-p035.l03`, `T1-p035.l04`, `T1-p035.l05`, `T1-p035.l07`, and `T1-p035.l08` are now also secured from direct image review plus local OCR support and both Paddle support surfaces where applicable.
- the main live holdouts immediately around this point are `T1-p032.l05`; the still-open `T1-p033.l03`, `l04`, `l05`, `l06`, `l07`, and `l09` columns; the remaining `T1-p034.l02`, `l03`, `l05`, and `l06` residue; and `T1-p035.l06`, `l09`, and `l10`.
- the next required bounded slice is to continue image-led manual correction from the remaining `T1-p033` residue, then the remaining `T1-p034` residue, and then the still-productive `T1-p035` speaking line and doctrinal tail without treating the page boundaries as stopping points.
