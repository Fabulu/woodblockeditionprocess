# Current State



- Work: `永嘉證道歌` / `song-of-enlightenment`

- Date: `2026-05-11`

- Phase: `ocr-startup-baseline-complete`

- Current slice: `ocr_startup_slice_identify_poem_page_spans_from_completed_image_tranche_baselines`

- Last completed slice: `ocr_startup_slice_continue_and_complete_image_tranche_baselines_before_pdf_render_slice`

- Next required action: identify the poem-bearing page spans inside `YJG-W16`, `YJG-W17`, and `YJG-W22` from the completed four-engine OCR baseline; convert that baseline into page-plus-line anchor planning for the poem loci; keep the PDF-backed first-tier exact witnesses queued for a separate render-preparation slice; keep `YJG-A10` and `YJG-A11` as second-tier controls outside OCR tranche 1; keep `YJG-W12` blocked rather than pretending it is a latent OCR quick win

- Next required slice: `ocr_startup_slice_identify_poem_page_spans_from_completed_image_tranche_baselines`

- Copy-text status: not yet selected

- Translation status: not yet started



## Active facts



- A new critical-edition package has been opened specifically for `永嘉證道歌`.

- The work is being treated as a poem-first Chan critical edition with later commentary and translation witnesses as secondary controls.

- The inherited local `四部録` witness is already on disk and is the first recorded exact witness.

- Web and scout research now identify:

  - one strong standalone NDL exact witness

  - a Wenzhou exact family with multiple genuinely independent prints rather than only duplicates

  - an additional exact Wenzhou file outside the first category slice

  - a second anthology-like exact lead

  - a `永嘉集附證道歌` near-exact anthology lead

  - a `1935` bibliographic exact lead outside the immediate Commons image cluster

  - a Korean exact family with `1474`, `1647`, heritage, metal-type, and later backup-title lines

  - a Waseda `五味禅` anthology witness containing `永嘉真覺大師證道歌`

  - Kyoto and Waseda `四部録` anthology witnesses beyond the inherited local branch

  - a `四部録抄` derivative anthology branch with `證道歌抄`

  - an undated manuscript exact witness in Japanese holdings

  - two further exact image-backed Japanese standalone holdings in the NIJL image network

  - one further exact digital-content holding in the Okura network

  - one further scan-backed exact `1531` witness in the OSDL / ToyoJack network

  - one scan-backed non-Japanese manuscript container in the BnF IIIF network that explicitly includes `永嘉證道歌`

  - one newly captured Korean exact `1576` witness that now fills the family gap between `1474` and `1647`

  - one newly opened `1672` Berkeley `四部録` control with a direct public IIIF manifest

  - one second-tier exact witness `YJG-W19` is now fully harvested as a local image tranche

  - one second-tier manuscript container `YJG-W20` is now fully harvested as a local image tranche after a slower resumable pull

  - one newly surfaced `1641` NIJL exact standalone witness now fully harvested as a local image tranche

  - three newly surfaced NIJL exact fragmentary witnesses with direct public manifests

  - one new Korean `1574` metadata-only exact lead

  - one new image-backed Korean exact lead strengthening the Zhao-Mengfu / calligraphic-recut branch

  - one stronger public institutional holding for the older Korean `을해자` line

  - one `1631` Kyushu `四部録抄` derivative branch now fully held as a local image tranche

  - one `1648` Kyushu `校正四部録` corrected branch now fully held as a local image tranche

  - one `1647` Nagoya / NIJL-linked `四部録抄` derivative branch

  - one Kyoto manuscript `入衆日用` container with appended `證道歌`

  - a dated NLC commentary witness

  - an older Japanese commentary-print lead `証道歌註` (`1641`)

  - an image-backed `四部録` holding in the NMOE network

  - an image-backed `首書四部録` annotated branch in the Yutoku network

  - a `1689` kana-marked `四部録` branch

  - stronger surfaced Korean near-exact `南明` family lines with digital access

  - CiNii and reception controls

  - one Commons upload-log duplicate relation tying a suppressed Wenzhou `證道歌` upload to the Waseda `五味禅` mirror



## Ranked exact-family posture



- The package is no longer in undifferentiated witness expansion mode.

- The package has now adopted the ReadZen-facing tiered evidence rule for the next edition phase:

  - Tier 1 `page` anchor for every poem locus

  - Tier 2 `line` anchor for every poem locus

  - Tier 3 `character` anchor for any apparatus or character-contested locus

  - Tier 4 `cross_witness_character` only where true cross-witness alignment is later performed

- The next OCR/transcription phase must record `evidence_tier` and `char_coverage` in `anchor-base-register.jsonl` and `anchor-event-log.jsonl` from the start rather than backfilling them later.

- The next OCR/transcription phase must treat PaddleOCR word-box return as mandatory support for future character-level evidence display in ReadZen.

- The package-local OCR workspace now exists at:

  - `provenance/song-of-enlightenment/ocr/`

- The package-local OCR runner now exists at:

  - `scripts/run_witness_ocr.py`

- The tranche-1 launcher now exists at:

  - `scripts/run_tranche1_ocr.py`

- OCR tranche 1 is now opened on the held exact image subset:

  - `YJG-W16`

  - `YJG-W17`

  - `YJG-W22`

- Live baseline output has already begun on `YJG-W22` across all four engines.

- The first live startup pass exposed two environment truths that are now fixed in the local workflow:

  - Paddle must run under Python `3.12`

  - Tesseract must use an existing external `chi_tra.traineddata` path rather than the empty program-default lookup

- RapidOCR baseline has now completed cleanly across the active tranche-1 image witnesses:

  - `YJG-W16`

  - `YJG-W17`

  - `YJG-W22`

- OCR tranche 1 image baseline is now complete across the intended four-engine set:

  - `YJG-W16`: RapidOCR, PaddleOCR, EasyOCR, and Tesseract completed across `55/55` images

  - `YJG-W17`: RapidOCR, PaddleOCR, EasyOCR, and Tesseract completed across `57/57` images

  - `YJG-W22`: RapidOCR, PaddleOCR, EasyOCR, and Tesseract completed across `68/68` images

- The completed tranche has a small number of honest zero-text page results rather than engine blockers:

  - `YJG-W16` `RapidOCR` page `page-0055` completed with `0` extracted text rows

  - `YJG-W22` `RapidOCR` page `page-0068` completed with `0` extracted text rows

  - `YJG-W22` `EasyOCR` page `page-0068` completed with `0` extracted text rows

- The package had to recover from interactive launcher time limits honestly:

  - a direct shell-bound tranche run would advance real OCR work but could time out before the full slice finished

  - the active recovery path is a package-local background scheduler under `provenance/song-of-enlightenment/ocr/_logs/` that resumes only incomplete witness-engine jobs and keeps per-job logs

- The current first-tier scan-backed exact acquisition queue is:

  - `YJG-W2` standalone `1694` witness

  - `YJG-W8` Korean `1474` witness

  - `YJG-W9` Korean `1647` witness

  - `YJG-W4C` early exact Wenzhou/Korean line

  - `YJG-W4F` `1341` Yuan exact line

  - `YJG-W4G` `1474` Korean exact line in the Wenzhou backup family

  - `YJG-W22` NIJL `1641` standalone exact witness

  - `YJG-W12` manuscript witness

  - `YJG-W16` Toyo exact standalone image witness

  - `YJG-W17` Berkeley exact standalone image witness

- The direct Commons tranche is now already held in-package:

  - `YJG-W2`

  - `YJG-W4C`

  - `YJG-W4F`

  - `YJG-W4G`

- Additional first-tier capture from the latest sweep is now already held in-package:

  - `YJG-W8` full PDF

  - `YJG-W9` full PDF

  - `YJG-W21` full PDF

  - `YJG-W22` IIIF manifest plus `68` harvested local page images

  - `YJG-W16` IIIF manifest plus `55` harvested local page images

  - `YJG-W17` IIIF manifest plus `57` harvested local page images

- The remaining first-tier witnesses still require non-Commons capture or catalog/image-network extraction:

  - `YJG-W12`

- The following are now second-tier exact or family controls:

  - `YJG-W18` viewer-only and not independent from `YJG-W2`

  - `YJG-W19` held as a direct public IIIF v3 manifest plus full local image tranche

  - `YJG-W20` held as a direct public Gallica IIIF v2 manifest plus full local image tranche

  - `YJG-W4D`

  - `YJG-W4E`

  - `YJG-W10`

  - `YJG-W11`

  - `YJG-W23`

  - `YJG-W24`

  - `YJG-W25`

  - `YJG-W27`

  - `YJG-W28`

  - `YJG-W5`

  - `YJG-W6`

  - `YJG-A1`

  - `YJG-A2`

  - `YJG-A6`

  - `YJG-A7`

  - `YJG-A9`

  - `YJG-A10`

  - `YJG-A11`

  - `YJG-A12`

  - `YJG-A13`

- The following are currently treated as duplicate-risk, derivative, bibliographic-only, or backup-only branches:

  - `YJG-W4A`

  - `YJG-W4B`

  - `YJG-W7` dead-end bibliographic only

  - `YJG-W13`

  - `YJG-W14`

  - `YJG-W15`

  - `YJG-A3`

  - `YJG-A4`

  - `YJG-A5`

  - `YJG-A8`



## Immediate priorities



1. Identify the poem-bearing page spans inside `YJG-W16`, `YJG-W17`, and `YJG-W22` from the completed OCR baseline outputs.

2. Convert the image-tranche OCR baseline into page-plus-line anchor planning for the actual poem loci.

3. Keep separating likely duplicate or recut Wenzhou manifestations from genuinely independent exact witnesses.

4. Preserve Korean exact backup leads without letting them crowd out the already ranked first-tier queue, but keep `YJG-W28` active as a real image-backed branch gain.

5. Treat anthology and derivative branches as controls unless they prove needed for a family gap, while admitting the new Kyushu and Kyoto control branches into the live map.

6. Continue exact-witness hunting only where a scan gap still threatens family coverage.

7. Distinguish exact text witnesses from commentary, anthology, translation, and reception-only controls.

8. Treat the witness family map as secure enough for OCR startup, while leaving copy-text lock and deeper editorial adjudication for after the first OCR tranche.

9. Exclude prohibited canonical web mirrors from this package entirely.





