# Human Log: Faith in Mind Critical Edition

This is the readable chronological log for the Faith in Mind edition package.

## 2026-04-14

The edition was restarted as a local-only package after an earlier premature scaffold in `OpenZenTexts` was removed. The witness hunt was then expanded to all credible free witnesses, kept broad, and finally locked after two consecutive recon waves produced no new credible free witness.

The witness register was frozen with stable sigla:

- `T1-T5` primary or near-primary witnesses
- `A1-A3` anthology or derivative witnesses
- `C1-C17` commentary, translation, or study controls
- `S1-S5` secondary source-tradition or anthology controls

Acquisition metadata was then normalized across the locked set. During that phase, several structurally bad PDFs turned out to be bad local downloads rather than bad witnesses, and browser-download plus hash comparison became part of the formal workflow.

`T1` was ranked as the starting copy-text because it is the strongest direct standalone witness in hand. It is now locked as the starting spine, but not as an untouchable permanent base. A later switch is allowed only through explicit evidence, a decision record, a timeline event, and reconstructable prior state.

Stage 2 began with page preparation for `T1`. The canonical PDF was re-verified, then rendered into `83` stable page images at `200` DPI. A `page-map.csv` and OCR metadata record were created so the OCR step could proceed reproducibly.

The local environment did not have `tesseract` or ImageMagick, so a Python OCR stack was installed instead. A RapidOCR probe on the first two pages extracted usable text, even though the console briefly failed to print Chinese safely. That console failure was logging noise, not OCR failure.

RapidOCR pass 1 then ran across all `83` pages of `T1`. It produced text on `80` pages and no text on the final `3` pages: `T1-p081`, `T1-p082`, and `T1-p083`. The run was strong enough to move forward into normalization without pretending the OCR was already clean.

The page-role pass is now also complete. `T1` is not a bare poem witness spread across `83` body pages; it currently reads as title or imprint matter on `p001-p004`, prefatory prose on `p005-p006`, commentary-dominant pages with embedded poem lemmata on `p007-p080`, and blank tail pages on `p081-p083`.

Stage 2D has now started. A corrected working file and correction log exist, and the first bounded correction slice repaired the opening title lines plus a broad recoverable `信心銘` lemma spine through `T1-p079.l01`. That is enough to move the package out of planning and into real correction work without pretending the commentary prose is already secure.

Most of `T1` is still uncorrected. The prefatory prose remains unstable, the commentary-heavy body still needs line-by-line work, and the three blank tail pages should be re-confirmed visually during later review.

To keep the next correction step OCR-first rather than speculative, the package now also carries extracted Paddle text companions plus a focused Tesseract support batch for `T1-p005` to `T1-p010`. That does not yet make the prose secure, but it gives the early noisy pages more than one OCR witness on disk.

The OCR support layer is now stronger again. A first full Tesseract attempt failed because the Windows install could not find `chi_tra.traineddata`, so the pass was rerun against the witness-local `ocr/T1/tessdata/` directory instead of treating the environment as healthy by assumption. The corrected rerun completed across all `83` `T1` pages and now gives the package three full OCR witnesses on disk: RapidOCR, PaddleOCR `PP-OCRv4`, and Tesseract.

The active early-prose slice also gained a more targeted support derivative. Because the Paddle plain-text extraction on vertical pages may scramble reading order, a geometry-sorted Paddle support view was generated for `T1-p005` to `T1-p010`. This does not replace the raw extraction, but it gives the correction pass another OCR-only way to judge whether a bad line is an ordering problem rather than a recognition problem.
