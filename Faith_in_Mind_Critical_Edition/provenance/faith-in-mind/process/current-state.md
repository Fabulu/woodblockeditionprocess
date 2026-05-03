# Current State: Faith in Mind

Date: 2026-05-02
Status: active
Edition slug: `faith-in-mind`

## Resume summary

- Witness set: locked
- Scope: broader
- Copy-text: `T1` locked as starting spine, switch allowed only by logged evidence-based decision
- Current phase: `manual_correction_pass_1_started`
- Last completed phase: `manual_correction_slice_T1_second_pass_p036_inner_and_right_column_recovery`

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
- a bounded `C13` commentary-control comparison slice now exists and confirms broad opening, central one-mind/all-dharmas, and early quoted terminal-anchor support for the recovered `T1` lemma spine without exposing a new high-confidence repair locus or accepted `T1` text change
- `C14` is now opened as the next commentary control witness with in-package metadata, rendered page images, and a classified page map
- `C14` page roles treat `C14-p001` to `C14-p008` as active `通俗信心銘講話` part 2 continuation body, `C14-p009` as mixed terminal body plus publication or colophon matter, `C14-p010` to `C14-p013` as publisher catalogue or advertising matter, and `C14-p014` to `C14-p015` as rear wrapper, rear cover, or library-tail matter
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
- `C17` page roles treat `C17-p001` as front cover, `C17-p002` as blank front endpaper or inside cover, `C17-p003` as title page, `C17-p004` to `C17-p009` as preface or table-of-contents matter, `C17-p010` to `C17-p200` as non-target series body, `C17-p201` to `C17-p214` as the active `中峰和尚信心銘義解` target segment, `C17-p215` as publication colophon, `C17-p216` as blank rear endpaper, `C17-p217` as rear pastedown or inside wrapper, and `C17-p218` as rear cover
- the `C17` opening notes explicitly record that the final `18`-page PDF segment contains the Faith in Mind target material but that its internal printed-page order is not monotonic by rendered image index
- logged `ocr-input-120dpi/` and `ocr-input-90dpi/` derivative JPEG sets now exist for `C17` to keep long-witness OCR computationally manageable on this workstation
- a full resumed `RapidOCR` pass now exists for `C17` under `ocr/C17/ocr/rapidocr/` on the logged `ocr-input-120dpi/` derivative basis
- a full resumed `tesseract` pass now exists for `C17` under `ocr/C17/ocr/tesseract-full-pass/` and closes at `218/218` pages with only familiar tiny-fragment warnings and no recorded engine errors
- a full `PaddleOCR PP-OCRv4` pass under Python `3.12` now exists for `C17` under `ocr/C17/ocr/paddleocr-ppocrv4/` and closes at `218` success pages with `0` recorded errors
- derived Paddle support text now exists for `C17` under `ocr/C17/ocr/paddleocr-ppocrv4/extracted-text/`
- a full `EasyOCR` pass now exists for `C17` under `ocr/C17/ocr/easyocr-full-pass/` and closes at `218` processed pages with text on `205`, leaving only `C17-p002`, `C17-p216`, `C17-p217`, and `C17-p218` empty, and no recorded engine errors
- `C17` now has full recorded four-engine OCR compliance and is ready for bounded comparison use as a commentary-related control witness
- the package now has a witness-page coverage audit for the active non-blank `T1` span at `scripts/audit_witness_page_coverage.py`

- `T1-p031.l01 = 縱有是非紛然失心` and `T1-p031.l05 = 不見夜來依舊宿蘆花` are now secured from direct image inspection plus local OCR support.
- `T1-p032.l02 = 是轉句不見一色始是半提更須知有全提`, `T1-p032.l04 = 言萬言秖是一言千法萬法秖是一法得到`, `T1-p032.l08 = 此處亦須轉却若守住其一便是繫驢橛所`, and `T1-p032.l09 = 盡十方一句超萬象千句萬句秖是一句千` are now secured from direct image inspection plus local OCR support and bounded `C9` phrase confirmation.
- `T1-p032.l06 = 箇主人公無二無別古人不得已而喚作` and `T1-p032.l07 = 似雲門道直得蓋乾坤大地無絲毫過患` are now also secured from direct image inspection plus local OCR support.
- `T1-p032.l03 = 失一切取捨一切憎愛一切是非都虛秖是` is now also secured from direct image inspection plus local OCR support and bounded `C9` phrase confirmation.

## Next action

Open `provenance/faith-in-mind/process/CONTINUATION_GATE.md` and `provenance/faith-in-mind/process/STATUS_REPORT_GATE.md` before deciding a correction or comparison run is done or before writing any status report.

The first end-to-end commentary continuation has already closed at the real terminal page `T1-p083`, and the second pass is now active from the earliest unresolved prose. The second-pass recoveries now include `T1-p007.l07 = 還構得麼秖這至道無難言端語端非但`, `T1-p008.l08 = 是箇無事底道人若意根不斷見解不忘`, `T1-p011.l01 = 達順相爭是為心病`, `T1-p011.l02 = 何得相應去大地雪漫漫春來依舊寒`, `T1-p011.l03 = 明自己不了目前此人秖具一隻眼若了目`, `T1-p011.l05 = 若得恁麼去逆也不見順也不見頭`, `T1-p011.l06 = 綠草來豈不見鴻山二十年不參禪不學道`, `T1-p011.l08 = 一時坐斷喚作常光現前念念不昧若只`, `T1-p012.l01 = 你道或是或非人不識逆行順行天莫測迎`, `T1-p012.l03 = 師云而今恁麼者多不恁麼者少成群作隊`, `T1-p012.l04 = 便是愛不知憎愛是心違順是境因對順境`, `T1-p012.l05 = 有許多般病如何救得別人`, `T1-p012.l06 = 是我自心裏妄倒`, `T1-p012.l07 = 是法執總是心病參禪秖要安樂你肚裹`, `T1-p012.l08 = 如麻似粟沒量大人作這見解不是`, `T1-p012.l09 = 則起愛心遇違情則起瞋心既不了違順`, `T1-p012.l10 = 自生憎愛自達自違`, `T1-p014.l07 = 掛角不用鳥道虛玄五色不能盲五音不能亂`, `T1-p015.l04 = 滿無際在凡夫喚作凡夫法在聖人喚作聖人`, `T1-p015.l06 = 人法本無欠少亦無餘剌在什麼處勘`, `T1-p016.l04 = 祖師麼云良久應須恁麼會方始契如`, `T1-p016.l05 = 平地上死人無數如今提起活杖子向百草`, `T1-p016.l06 = 示衆云斬釘截鐵門前草深一丈破二作三`, `T1-p016.l08 = 是取不得捨不得不可得中恁麼得還見`, `T1-p017.l05 = 頭出頭沒你如今要不逐有緣麼須是截斷`, `T1-p017.l06 = 逐他會愛取捨造業受報向輪迴生死海裏`, `T1-p018.l01 = 一種平懷泯然自盡`, `T1-p018.l08 = 良久暗裏抽橫骨明中坐舌頭`, `T1-p018.l09 = 方知有向上事俗且道作麼生是向上事`, `T1-p019.l03 = 師云皮膚脫落盡唯有一真實耀古騰今明`, `T1-p020.l03 = 作什麼動是何物靜是什麼不可有兩箇也`, `T1-p021.l03 = 堪作什麼`, `T1-p021.l04 = 師打云秖為你將赤肉團要扛我棒不識痛`, `T1-p021.l05 = 作麼生道拍禪床一下去百雜碎`, `T1-p021.l09 = 亂動全是靜`, `T1-p022.l02 = 全是動裏一無二`, `T1-p022.l03 = 師云有什麼救處問你有什麼物教你遣`, `T1-p022.l04 = 程行`, `T1-p022.l05 = 遇偏`, `T1-p022.l06 = 偏枯情境添漏莫道兩處失功致使`, `T1-p022.l07 = 過恰若一處透千處萬處一時透`, `T1-p023.l01 = 明心地萬有`, `T1-p023.l02 = 但止其動便是`, `T1-p023.l04 = 本來無相`, `T1-p023.l05 = 背其真空而不知萬法當體是真空觸物`, `T1-p023.l06 = 萬有即迷妙有落在斷見禪和子但仔細思`, `T1-p023.l10 = 有得斷空即迷真空`, `T1-p023.l11 = 其靜便是空典`, `T1-p024.l02 = 師云低聲你纔開口便沒交涉了也`, `T1-p024.l03 = 食觀天上月光却學中珠`, `T1-p024.l06 = 是空名異體同更點他法且道遇在什麼處`, `T1-p024.l07 = 教無言何必拈花微笑傳正法眼藏你要`, `T1-p024.l08 = 時得出去禪和子此事若在言句裹一大藏`, `T1-p024.l09 = 在葛藤窠裏如跛鼈盲龜入空谷相似`, `T1-p025.l02 = 師云什麼處得消息來寧可截舌`, `T1-p025.l03 = 竟成得箇什麼事一夜落花雨滿城流水`, `T1-p025.l04 = 相似以佛祖鞭子德山臨濟有棒有喝`, `T1-p025.l05 = 智隔想體殊要演語路絕心行處滅`, `T1-p026.l06 = 寒岩異草青坐著日雲宗不妙`, `T1-p026.l09 = 禪和子你如今擬`, `T1-p026.l10 = 開口要話會隨言逐句便`, `T1-p027.l07 = 麼生須彌頂上無根草不受春風花自開`, `T1-p027.l09 = 師云你待翻悔那前來遣有沒有從空背空`, `T1-p028.l04 = 迴避之處直饒恁麼已是自瞞`, `T1-p028.l06 = 師云自知即得前來秪管觀空去生滅念`, `T1-p028.l09 = 這箇田地開一轉日用之間地更無`, `T1-p029.l05 = 聲也真色也真動靜也真語默也真如是日`, `T1-p029.l07 = 填溝塞壑千變萬化全體一真不動絲毫`, `T1-p029.l08 = 切現成更無欠少你但應係有見空見佛見`, `T1-p029.l09 = 用見聞覺知無不純真直得亘大地滿天下`, and `T1-p029.l10 = 師云現成公案你求他作麼見也真聞也真`. `T1-p081` and `T1-p082` remain visually confirmed non-blank tail matter, and `T1-p083` remains blank. The remaining unresolved loci on `T1-p007` are now `l03`, `l04`, `l08`, `l09`, and `l12`, while `T1-p011.l04`, `T1-p012.l02`, `T1-p014.l08`, `T1-p022.l08` to `T1-p022.l12`, and much of the remaining commentary prose from `T1-p007` to `T1-p080` remain materially open for continued second-pass work.

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
- `C1` is a Japanese translation or reception control rather than a base-text witness: only `p051-p052` belong to the target `信心銘和譯` span in the current page-role pass
- `C1` now has full four-engine OCR compliance on the direct rendered `page-images/` basis; unlike `T2` and `A3`, no derivative OCR-input basis was required on this machine
- `C2` is also a Japanese translation or reception control rather than a base-text witness: only `p021-p023` belong to the target `三祖大師信心銘` span in the current page-role pass, and the opening and closing images are mixed-content boundary spreads
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
- `T1-p035.l02`, `T1-p035.l03`, `T1-p035.l04`, `T1-p035.l05`, `T1-p035.l06`, `T1-p035.l07`, `T1-p035.l08`, and `T1-p035.l10` are now also secured from direct image review plus local OCR support and both Paddle support surfaces where applicable, with `l07` re-tightened after enlarged image review corrected its middle doctrinal contrast.
- `T1-p036.l08 = 依舊白雲中` is now also secured from direct image review plus convergent local OCR support.
- `T1-p036.l01`, `T1-p036.l02`, `T1-p036.l03`, `T1-p036.l04`, `T1-p036.l05`, `T1-p036.l06`, `T1-p036.l07`, `T1-p036.l08`, and `T1-p036.l09` are now all secured from direct image review plus convergent local OCR support and bounded comparison corroboration where needed, with `l01/l05` specifically corrected after an earlier local misassignment was reopened and reversed.
- `T1-p032.l05` is now also secured from direct image review plus convergent local OCR support.
- the main live holdouts immediately around this point are the still-open `T1-p033.l03`, `l04`, `l05`, `l06`, `l07`, and `l09` columns; the remaining `T1-p034.l02`, `l03`, `l05`, and `l06` residue; and the surviving short-fragment problem at `T1-p035.l09`.
- the next required bounded slice is to continue the earliest unresolved second-pass residue on `T1-p033`, starting with the cleaner middle and right-side columns before reassessing the page as a whole.
