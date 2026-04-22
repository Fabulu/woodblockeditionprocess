# Current State: Faith in Mind

Date: 2026-04-21
Status: active
Edition slug: `faith-in-mind`

## Resume summary

- Witness set: locked
- Scope: broader
- Copy-text: `T1` locked as starting spine, switch allowed only by logged evidence-based decision
- Current phase: `manual_correction_pass_1_started`
- Last completed phase: `ocr_compliance_slice_C13_four_engine_complete`

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
- a first full `RapidOCR` pass now exists for `C5` under `ocr/C5/ocr/rapidocr/`
- a full `tesseract` pass now also exists for `C5` under `ocr/C5/ocr/tesseract-full-pass/`
- a full `PaddleOCR PP-OCRv4` pass now also exists for `C5` under `ocr/C5/ocr/paddleocr-ppocrv4/`
- derived Paddle text support now exists for `C5` under `ocr/C5/ocr/paddleocr-ppocrv4/extracted-text/`
- a full `EasyOCR` pass now also exists for `C5` under `ocr/C5/ocr/easyocr-full-pass/`
- `C5` now has full recorded four-engine OCR compliance and is ready for bounded comparison use as a commentary control witness
- a bounded `C5` commentary-control comparison slice now exists and confirms broad commentary-backed support for the recovered `T1` lemma spine across the `巻上` body, without exposing a new high-confidence repair locus
- `C6` is now opened as the next commentary control witness with in-package metadata, rendered page images, and a classified page map
- `C6` page roles treat `C6-p001` as a mixed title-plus-opening spread, `C6-p002` to `C6-p058` as the main `冠註信心銘夜塘水` `巻下` commentary body, `C6-p059` as a mixed terminal body-plus-colophon spread, and `C6-p060` to `C6-p061` as rear wrapper or library-tail matter
- a full `RapidOCR` pass now exists for `C6` under `ocr/C6/ocr/rapidocr/`
- a full `tesseract` pass now exists for `C6` under `ocr/C6/ocr/tesseract-full-pass/`
- a full `PaddleOCR PP-OCRv4` pass now exists for `C6` under `ocr/C6/ocr/paddleocr-ppocrv4/`
- derived Paddle text support now exists for `C6` under `ocr/C6/ocr/paddleocr-ppocrv4/extracted-text/`
- a repaired full `EasyOCR` pass now exists for `C6` under `ocr/C6/ocr/easyocr-full-pass/`
- `C6` now has full recorded four-engine OCR compliance and is ready for bounded comparison use as a commentary control witness
- a bounded `C6` commentary-control comparison slice now exists and confirms broad commentary-backed support for the recovered `T1` lemma spine across the `巻下` continuation of the `夜塘水` tradition, without exposing a new high-confidence repair locus
- `C7` is now opened as the next Kyoto commentary-control witness with in-package metadata and a classified page map
- `C7` page roles treat `C7-p001` to `C7-p003` as wrapper or title matter, `C7-p004` to `C7-p005` as prefatory or front matter, `C7-p006` to `C7-p043` as the main `信心銘拈提` commentary body, `C7-p044` as publication or colophon matter, and `C7-p045` to `C7-p046` as rear wrapper or tail matter
- a full `RapidOCR` pass now exists for `C7` under `ocr/C7/ocr/rapidocr/`
- a full `tesseract` pass now exists for `C7` under `ocr/C7/ocr/tesseract-full-pass/`
- a full `PaddleOCR PP-OCRv4` pass now exists for `C7` under `ocr/C7/ocr/paddleocr-ppocrv4/`
- derived Paddle text support now exists for `C7` under `ocr/C7/ocr/paddleocr-ppocrv4/extracted-text/`
- a full `EasyOCR` pass now exists for `C7` under `ocr/C7/ocr/easyocr-full-pass/`
- `C7` now has full recorded four-engine OCR compliance and is ready for bounded comparison use as a Kyoto commentary control witness
- a bounded `C7` commentary-control comparison slice now exists and confirms broad Kyoto commentary-backed support for the recovered `T1` lemma spine and transmitted macro-sequence, without exposing a new high-confidence repair locus
- `C8` is now opened as the next commentary-control witness with in-package metadata, rendered page images, and a classified page map
- `C8` page roles treat `C8-p001` to `C8-p002` as title matter, `C8-p003` to `C8-p029` as the main `信心銘拈提 - 太祖弘徳円明国師` commentary body, `C8-p030` as a mixed closing page with explicit end marker plus publication matter, `C8-p031` as blank tail, and `C8-p032` to `C8-p033` as modern back matter or tail
- a full `RapidOCR` pass now exists for `C8` under `ocr/C8/ocr/rapidocr/`
- a full `tesseract` pass now exists for `C8` under `ocr/C8/ocr/tesseract-full-pass/`
- a full `PaddleOCR PP-OCRv4` pass now exists for `C8` under `ocr/C8/ocr/paddleocr-ppocrv4/`
- derived Paddle text support now exists for `C8` under `ocr/C8/ocr/paddleocr-ppocrv4/extracted-text/`
- a full `EasyOCR` pass now exists for `C8` under `ocr/C8/ocr/easyocr-full-pass/`
- `C8` now has full recorded four-engine OCR compliance and is ready for bounded comparison use as a commentary control witness
- a bounded `C8` commentary-control comparison slice now exists and confirms broad NDL commentary-backed support for the recovered `T1` lemma spine and transmitted macro-sequence, without exposing a new high-confidence repair locus
- `C9` is now opened as the next commentary-control witness with in-package metadata, rendered page images, and a classified page map
- `C9` page roles treat `C9-p001` to `C9-p002` as title matter, `C9-p003` to `C9-p074` as the main `信心銘夜塘水 - 増冠傍註 巻上` commentary body, and `C9-p075` to `C9-p076` as tail or wrapper matter
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
- `C10` page roles treat `C10-p001` to `C10-p002` as title matter, `C10-p003` to `C10-p062` as the main `信心銘夜塘水 - 増冠傍註 巻下` commentary body, `C10-p063` as terminal colophon or imprint matter, and `C10-p064` to `C10-p065` as blank or wrapper tail matter
- a full `RapidOCR` pass now exists for `C10` under `ocr/C10/ocr/rapidocr/`
- a full `tesseract` pass now exists for `C10` under `ocr/C10/ocr/tesseract-full-pass/`
- a full `PaddleOCR PP-OCRv4` pass now exists for `C10` under `ocr/C10/ocr/paddleocr-ppocrv4/`
- derived Paddle text support now exists for `C10` under `ocr/C10/ocr/paddleocr-ppocrv4/extracted-text/`
- a full `EasyOCR` pass now exists for `C10` under `ocr/C10/ocr/easyocr-full-pass/`
- `C10` now has full recorded four-engine OCR compliance and is ready for bounded comparison use as a commentary control witness
- a bounded `C10` commentary-control comparison slice now exists and confirms broad NDL commentary-backed support for the recovered `T1` lemma spine and transmitted macro-sequence, without exposing a new high-confidence repair locus
- `C11` is now opened as the next commentary-control witness with in-package metadata, rendered page images, and a classified page map
- `C11` page roles treat `C11-p001` to `C11-p003` as cover, title, or prefatory matter and `C11-p004` to `C11-p100` as the active `信心銘夜塘水講義` lecture body within part 1
- a full `RapidOCR` pass now exists for `C11` under `ocr/C11/ocr/rapidocr/`
- a full `tesseract` pass now exists for `C11` under `ocr/C11/ocr/tesseract-full-pass/`; all `100` text sidecars are present, although the resumed summary undercounts at `99` pages with text because `C11-p060` was not re-entered into the summary array
- a full `PaddleOCR PP-OCRv4` pass now exists for `C11` under `ocr/C11/ocr/paddleocr-ppocrv4/`
- derived Paddle text support now exists for `C11` under `ocr/C11/ocr/paddleocr-ppocrv4/extracted-text/`
- a full `EasyOCR` pass now exists for `C11` under `ocr/C11/ocr/easyocr-full-pass/`
- `C11` now has full recorded four-engine OCR compliance and is ready for bounded comparison use as a lecture commentary control witness
- a bounded `C11` lecture-commentary-control comparison slice now exists and confirms broad opening and central-sequence support for the recovered `T1` lemma spine without exposing a new high-confidence repair locus
- `C11` is part 1 of a lecture pair and is not being used for a complete terminal-close judgment; the queue now moves to `C12`
- `C12` is now opened as the next lecture commentary control witness with in-package metadata, rendered page images, and a classified page map
- `C12` page roles treat `C12-p001` to `C12-p094` as active `信心銘夜塘水講義` part 2 lecture body, `C12-p095` as publication or colophon matter, `C12-p096` to `C12-p099` as publisher catalogue or advertising matter, and `C12-p100` as rear wrapper or library-tail matter
- a full resumed `RapidOCR` pass now exists for `C12` under `ocr/C12/ocr/rapidocr/`
- a full `tesseract` pass now exists for `C12` under `ocr/C12/ocr/tesseract-full-pass/`
- a full resumed `PaddleOCR PP-OCRv4` pass now exists for `C12` under `ocr/C12/ocr/paddleocr-ppocrv4/`
- derived Paddle text support now exists for `C12` under `ocr/C12/ocr/paddleocr-ppocrv4/extracted-text/`
- a full resumed `EasyOCR` pass now exists for `C12` under `ocr/C12/ocr/easyocr-full-pass/`
- `C12` now has full recorded four-engine OCR compliance and is ready for bounded comparison use as the part 2 lecture commentary control witness
- a bounded `C12` lecture-commentary-control comparison slice now exists and confirms broad central, late, and terminal-close support for the recovered `T1` lemma spine without exposing a new high-confidence repair locus or accepted `T1` text change
- `C13` is now opened as the next commentary control witness with in-package metadata, rendered page images, and a classified page map
- `C13` page roles treat `C13-p001` as front wrapper or cover/title material, `C13-p002` as mixed title plus opening body, and `C13-p003` to `C13-p100` as active `通俗信心銘講話` part 1 commentary body
- a full `RapidOCR` pass now exists for `C13` under `ocr/C13/ocr/rapidocr/`
- a full resumed `tesseract` pass now exists for `C13` under `ocr/C13/ocr/tesseract-full-pass/`
- a full resumed `PaddleOCR PP-OCRv4` pass now exists for `C13` under `ocr/C13/ocr/paddleocr-ppocrv4/`
- derived Paddle text support now exists for `C13` under `ocr/C13/ocr/paddleocr-ppocrv4/extracted-text/`
- a full resumed `EasyOCR` pass now exists for `C13` under `ocr/C13/ocr/easyocr-full-pass/`
- `C13` now has full recorded four-engine OCR compliance and is ready for bounded comparison use as the part 1 `通俗信心銘講話` commentary control witness
- the package now has a witness-page coverage audit for the active non-blank `T1` span at `scripts/audit_witness_page_coverage.py`

## Next action

Complete the first bounded `C13` commentary-control comparison slice against the recovered `T1` lemma spine, using direct image review and the saved four-engine OCR stack as support.

Use:

- `provenance/faith-in-mind/process/current-state.md`
- `provenance/faith-in-mind/process/human-log.md`
- `provenance/faith-in-mind/process/decision-log.md`
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
- `provenance/faith-in-mind/process/ocr-run-log.md`
- `provenance/faith-in-mind/collation/first-pass-variant-table.md`

Produce next:

- inspect representative `C13` body leaves by direct image review before relying on OCR text
- use the saved `RapidOCR`, `tesseract`, `PaddleOCR PP-OCRv4`, and `EasyOCR` outputs only as support for the direct-image comparison
- complete a bounded `C13` commentary-control comparison slice against the recovered `T1` lemma spine
- do not create a `T1` text change unless C13 exposes a new high-confidence repair locus corroborated by the existing direct-witness record
- do not create translation diffs unless the accepted `T1` edition text changes
- keep `current-state.md`, `process-log.md`, `human-log.md`, `process.json`, `timeline.json`, `ocr-run-log.md`, and any collation notes aligned after the `C13` comparison slice
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
`C13` has now completed its witness-opening slice and four-engine OCR-compliance slice.
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
- `C1` is a Japanese translation or reception control rather than a base-text witness: only `p051-p052` belong to the target `信心銘和譯` span in the current page-role pass
- `C1` now has full four-engine OCR compliance on the direct rendered `page-images/` basis; unlike `T2` and `A3`, no derivative OCR-input basis was required on this machine
- `C2` is also a Japanese translation or reception control rather than a base-text witness: only `p021-p023` belong to the target `三祖大師信心銘` span in the current page-role pass, and the opening and closing images are mixed-content boundary spreads
- the six-log forensic provenance protocol was adopted mid-project on `2026-04-18`, so retroactive reconstruction is now required before fresh witness work continues
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
