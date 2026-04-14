# Process Log: Faith in Mind (`ce.faith-in-mind`)

**Curator:** pending  
**Started:** 2026-04-14  
**Status:** witness hunt locked; pre-OCR  
**Primary open witnesses:** locked  
**Closed / licensed witnesses used in edition:** none

---

## Purpose

This log starts with the fresh package reset.

The previous premature edition scaffold in `OpenZenTexts` was removed before production work began, so this log is the canonical restart point.

---

## Witness set

See `../witnesses/witness-register.md`.

The set is now locked for the free witness phase.

Lock rule used:

- lock after `2` consecutive recon waves with no new credible free witness of any tier

---

## Witness acquisition

| Date | Action | Notes |
|------|--------|-------|
| 2026-04-14 | Created fresh local-only package scaffold | No OCR or transcription started |
| 2026-04-14 | Reset premature OpenZen Faith in Mind scaffold | `OpenZenTexts` Faith in Mind package deleted before production |
| 2026-04-14 | Downloaded `五味禪` | Local file `NDL8929982_five_tastes_zen.pdf`, SHA-256 recorded, `43` pages validated locally |
| 2026-04-14 | Downloaded `諸經合部` | Local file `CNTS-00047993099_combined_sutras.pdf`, SHA-256 recorded, `188` pages validated locally |
| 2026-04-14 | Downloaded `信心獲得章百席談 前` | Three local parts downloaded, SHA-256 recorded, Commons page counts confirmed |
| 2026-04-14 | Downloaded `国訳禅学大成 第二卷` Faith-related parts | Three local parts downloaded, SHA-256 recorded, part 1 Commons page count confirmed |

---

## Recon and search steps

| Date | Query or source | Action | Outcome | Next step | Actor |
|------|------------------|--------|---------|-----------|-------|
| 2026-04-14 | Japanese, Korean, Chinese, Commons, NDL, Kyoto, Waseda, broader web | Parallel recon wave run against Faith in Mind witness space | No new standalone base witness confirmed; search remains open | Keep scanning for free direct witnesses and strong anthology/control leads | agent |
| 2026-04-14 | Commons / NDL / CNTS | Checked new exact file-page leads | New reusable control leads found: `五味禪`, `諸經合部`, `信心獲得章百席談 前`, and `国訳禅学大成 第二卷` | Create lead folders and keep them outside the locked core for now | agent |
| 2026-04-14 | Broader web outside library scan surfaces | Checked translation/commentary surfaces | Mostly free reading or study pages without clear commercial-reuse terms | Do not treat these as acquisition wins under current policy | agent |
| 2026-04-14 | Broad free recon wave A | Searched Commons, NDL, Kyoto, Waseda, Korean-facing surfaces, and broader web for additional free Faith in Mind witnesses | No net-new credible free witness found; `NDL823161` was only a re-confirmation of an already listed item | Count as `no-new-free` recon wave `1/2`; continue one more broad wave | agent |
| 2026-04-14 | Broad free recon wave B | Repeated broad search across Commons, NDL, Kyoto, Waseda, open web PDFs, and known witness-title combinations | No net-new credible free witness found; search surfaced only already-known items such as `CNTS-00047968260`, `NDL2537640`, and `NDL823161` | Lock witness hunt and move to sigla / acquisition-finalization stage | agent |

---

## Rejected or deferred witnesses

| Date | Witness | Reason not used |
|------|---------|-----------------|
| 2026-04-14 | Multiple broader-web text pages and PDFs without explicit reuse terms | Deferred pending rights clarity |
| 2026-04-14 | Kyoto `景徳伝燈録` leads as core witnesses | Deferred to source-tradition control tier, not primary `信心銘` witness tier |
| 2026-04-14 | Newly surfaced generic Sengcan / Xinxin Ming websites | Deferred because they did not yield rights-safe scan witnesses or stronger source metadata than the existing inventory |

---

## Transcription sessions

None yet.

---

## OCR and page-prep sessions

| Date | Stage | Action | Outcome |
|------|-------|--------|---------|
| 2026-04-14 | Page preparation | Re-verified `T1` canonical PDF, rendered stable page images at `200` DPI, and created `ocr/T1/page-map.csv` plus `ocr/T1/metadata.json` | Stage 2A completed for `T1`; `83` page-image derivatives now exist |
| 2026-04-14 | OCR environment | Checked local OCR tool availability | `tesseract` and `magick` were absent; Python OCR stack chosen instead |
| 2026-04-14 | OCR environment | Installed `rapidocr_onnxruntime`, `onnxruntime`, and `opencv-python-headless` | First local OCR engine became available without relying on system Tesseract |
| 2026-04-14 | OCR environment | Installed `easyocr` in Python `3.14` and `paddleocr` plus `paddlepaddle` in Python `3.12` | `EasyOCR` became probe-runnable; `PaddleOCR` installed but still fails at runtime on this machine |
| 2026-04-14 | OCR environment | Located existing system `tesseract` binary and supplied local East Asian traineddata | `tesseract` became probe-runnable against `T1` using local `chi_tra` / `chi_tra_vert` models |
| 2026-04-14 | OCR probe | Ran RapidOCR probe on `T1-p001` and `T1-p002` | Text extracted on both pages; OCR quality noisy but usable enough for full pass |
| 2026-04-14 | OCR probe | Ran comparator probes on `T1-p001` for `tesseract`, `EasyOCR`, and `PaddleOCR` | `tesseract` and `EasyOCR` ran; `PaddleOCR` still fails with a Paddle runtime `NotImplementedError` |
| 2026-04-14 | OCR pass 1 | Ran full RapidOCR pass across `T1` page images and preserved page-level `.json` and `.txt` outputs | `83` pages processed, `80` with extracted text, `3` no-text pages (`T1-p081`-`T1-p083`); normalization is next |
| 2026-04-14 | OCR environment | Researched Paddle runtime failure against official Paddle/PaddleOCR sources and tested local backend switches | Evidence pointed to a stack/backend issue rather than a simple OCR model setting; local MKL-DNN flag toggles did not fix the original failure |
| 2026-04-14 | OCR environment | Downgraded Python `3.12` Paddle stack to `paddleocr 3.2.0`, `paddlepaddle 3.1.1`, and `paddlex 3.2.1` | The documented compatibility pair installed successfully |
| 2026-04-14 | OCR probe | Re-tested `PaddleOCR(lang='ch')` after downgrade | Default `PP-OCRv5` no longer raised the old Python exception, but still crashed with a Windows access violation during prediction |
| 2026-04-14 | OCR probe | Ran Paddle calibration probe on `T1-p001` using `PP-OCRv4` with CPU / no-HPI / no-MKL-DNN settings and saved outputs | Paddle became calibration-usable on this machine; outputs saved under `ocr/T1/ocr/paddleocr-ppocrv4/` |
| 2026-04-14 | OCR probe | Saved `tesseract` and `EasyOCR` calibration outputs for `T1-p001` | The same-page four-engine comparison slice now exists for `RapidOCR`, `tesseract`, `EasyOCR`, and `PaddleOCR` |
| 2026-04-14 | OCR pass 1 | Completed resumable PaddleOCR `PP-OCRv4` full pass across `T1` and preserved page-level outputs | `83` pages saved successfully under `ocr/T1/ocr/paddleocr-ppocrv4/`; default `PP-OCRv5` remains unusable on this machine |
| 2026-04-14 | Normalization | Built the first normalized `T1` working spine from page-level RapidOCR outputs | `transcription/normalized/T1-normalized-pass1.txt` created with page markers and stable line IDs; `transcription/normalized/normalization-rule-log.md` records the applied structural rules |
| 2026-04-14 | Page-role classification | Classified `T1` pages in `ocr/T1/page-map.csv` by dominant role before manual correction | `p001-p004` title or imprint matter, `p005-p006` prefatory prose, `p007-p080` commentary-dominant with embedded poem lemmata, `p081-p083` blank tail pages |
| 2026-04-14 | Manual correction pass 1 | Opened Stage 2D artifacts and corrected the first title-and-lemma slice in the `T1` working spine | Created `transcription/corrected/T1-corrected-pass1-working.txt`, `process/correction-log.md`, updated `process/unresolved-loci.md`, and recovered high-confidence title and lemma lines through `T1-p079.l01` |
| 2026-04-14 | OCR support extension | Extracted Paddle text companions from saved JSON and ran a focused Tesseract support batch on `T1-p005` to `T1-p010` | Early prefatory and commentary pages now have extra OCR evidence under `ocr/T1/ocr/paddleocr-ppocrv4/extracted-text/` and `ocr/T1/ocr/tesseract-early-support/` |
| 2026-04-14 | OCR support extension | Ran a full Tesseract pass across all `83` `T1` pages after fixing the `chi_tra` traineddata path | A first attempt failed because the system install did not resolve `chi_tra.traineddata`; the successful rerun used witness-local `ocr/T1/tessdata/` and saved outputs under `ocr/T1/ocr/tesseract-full-pass/` |
| 2026-04-14 | OCR probe | Re-tested vertical Tesseract on commentary pages with `chi_tra_vert` and `--psm 5/6` | The vertical model was materially worse than witness-local `chi_tra`, so no full vertical Tesseract pass was saved |
| 2026-04-15 | OCR support extension | Derived Paddle column-ordered support text from saved JSON geometry and then extended it to the full witness | The geometry-sorted support view under `ocr/T1/ocr/paddleocr-ppocrv4/column-ordered-text/` now covers all `83` `T1` pages and can be used as a support layer on vertical pages |
| 2026-04-15 | Manual correction pass 1 | Recovered one more secure late-band lemma line from the broader OCR support stack | `T1-p060.l01` was corrected to `究竟窮極不存軌則` using the extracted Paddle near-match plus immediate poem-sequence context; surrounding commentary prose remains unresolved |
| 2026-04-15 | Manual correction pass 1 | Recovered one more secure poem line from the broader OCR support stack | `T1-p030.l01` was corrected to `二見不住慎勿追尋` using the extracted Paddle near-match plus rapid shape support and poem-sequence placement |
| 2026-04-15 | Manual correction pass 1 | Recovered three more secure poem lines from the broader OCR support stack | `T1-p022.l01`, `T1-p025.l01`, and `T1-p028.l01` were corrected to `遣有沒有從空背空`, `絕言絕慮無處不通`, and `前空轉變皆由妄見`; the commentary prose remains open |
| 2026-04-15 | Manual correction pass 1 | Recovered two more secure poem lines from the broader OCR support stack | `T1-p027.l01` was corrected to `須臾返照勝卻前空` from the shared OCR core `...照...卻前空` plus its placement between `T1-p026.l01` and `T1-p028.l01`; `T1-p063.l01` was corrected to `一切不留無可記憶` from the Paddle column-ordered support `切不留...可記憶` plus the secured sequence between `T1-p062.l01` and `T1-p064.l01` |
| 2026-04-15 | Manual correction pass 1 | Recovered one more secure closing-line lemma from the broader OCR support stack | `T1-p077.l01` was corrected to `但能如是何慮不畢` because RapidOCR and extracted Paddle both preserved `但能如是何...不...`, and the already secured closing sequence before `T1-p078.l01` fixed the remaining graphs |

---

## Witness corroboration sessions

None yet.

---

## Editorial decisions

None yet.

---

## Stage planning

| Date | Stage | Action | Outcome |
|------|-------|--------|---------|
| 2026-04-14 | OCR / transcription planning | Defined the first production-stage workflow in `../transcription/ocr-transcription-plan.md` | `T1` remains the OCR-first copy-text spine; `T4`, `T5`, and `T2` stay queued as first comparison controls after the initial corrected `T1` pass |

---

## Quality checks

| Date | Check | Result |
|------|-------|--------|
| 2026-04-14 | Premature OpenZen scaffold removed | ok |
| 2026-04-14 | Fresh local-only package created | ok |
| 2026-04-14 | OCR started | yes |
| 2026-04-14 | Witness set locked | yes |
| 2026-04-14 | Consecutive no-new-free recon waves | `2/2` |
| 2026-04-14 | Core witness metadata normalization | `T1-T5` and `A1-A3` normalized into `witnesses/acquisition-metadata.md` |
| 2026-04-14 | Supporting witness metadata normalization | `C1-C17` and `S1-S5` normalized into `witnesses/acquisition-metadata.md` |
| 2026-04-14 | Installed stronger PDF support | Added `cryptography` and `pikepdf` to improve local validation before OCR work |
| 2026-04-14 | Re-ran blocked PDF validation | Most previously blocked NDL commentary and study files now validate locally with `pypdf` |
| 2026-04-14 | Re-downloaded suspect commentary PDFs and compared hashes | `C11` and `C13` changed hash, size, and validation behavior after redownload, confirming earlier local copies were bad |
| 2026-04-14 | Browser-downloaded `A3` replacement validated | User-provided browser download for `NDL2537799 四部録抄` replaced the bad local copy; `pypdf`, `fitz`, and `pikepdf` now all validate `57` pages |
| 2026-04-14 | Copy-text ranking completed | Added `collation/copy-text-ranking.md`; current recommendation is `T1` as copy-text with `T4`, `T5`, and `T2` as first comparison controls |
| 2026-04-14 | `T1` page-role classification completed | `page-map.csv` no longer leaves all `83` pages unclassified; manual correction can now proceed with page-role awareness |
