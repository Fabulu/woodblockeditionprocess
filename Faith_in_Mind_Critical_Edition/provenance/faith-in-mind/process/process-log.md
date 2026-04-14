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
| 2026-04-14 | OCR started | no |
| 2026-04-14 | Witness set locked | yes |
| 2026-04-14 | Consecutive no-new-free recon waves | `2/2` |
| 2026-04-14 | Core witness metadata normalization | `T1-T5` and `A1-A3` normalized into `witnesses/acquisition-metadata.md` |
| 2026-04-14 | Supporting witness metadata normalization | `C1-C17` and `S1-S5` normalized into `witnesses/acquisition-metadata.md` |
| 2026-04-14 | Installed stronger PDF support | Added `cryptography` and `pikepdf` to improve local validation before OCR work |
| 2026-04-14 | Re-ran blocked PDF validation | Most previously blocked NDL commentary and study files now validate locally with `pypdf` |
| 2026-04-14 | Re-downloaded suspect commentary PDFs and compared hashes | `C11` and `C13` changed hash, size, and validation behavior after redownload, confirming earlier local copies were bad |
| 2026-04-14 | Browser-downloaded `A3` replacement validated | User-provided browser download for `NDL2537799 四部録抄` replaced the bad local copy; `pypdf`, `fitz`, and `pikepdf` now all validate `57` pages |
| 2026-04-14 | Copy-text ranking completed | Added `collation/copy-text-ranking.md`; current recommendation is `T1` as copy-text with `T4`, `T5`, and `T2` as first comparison controls |
