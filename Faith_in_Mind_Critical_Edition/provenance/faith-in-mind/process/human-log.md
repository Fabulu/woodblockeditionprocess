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

RapidOCR pass 1 then ran across all `83` pages of `T1`. It produced text on `80` pages and no text on the final `3` pages: `T1-p081`, `T1-p082`, and `T1-p083`. Those tail pages are not yet classified, but the run is strong enough to move forward into normalization without pretending the OCR is already clean.

At this point, the edition has not yet entered manual correction. The current state is: witness set locked, copy-text locked as starting spine, page preparation complete, first OCR pass complete, normalization next.
