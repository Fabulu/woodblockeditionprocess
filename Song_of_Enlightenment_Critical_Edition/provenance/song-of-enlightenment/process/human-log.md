# Human Log



## 2026-05-09



- User selected `永嘉證道歌` as the next critical edition target after reviewing broader Zen candidates.

- User explicitly asked for strong due diligence, including five-agent review of the edition process and substantial online witness research before edition production.



## 2026-05-10



- The witness hunt is no longer the only active concern. The package has now been reframed for OCR-first preflight with explicit ReadZen-facing evidence capture requirements.

- The practical meaning is simple: the next OCR pass must not just produce text. It must also preserve enough geometry to support future line-level and character-level evidence display where editorial decisions depend on individual graphs.

- A further five-agent witness wave was still worth doing before OCR. It surfaced one genuinely strong new Japanese exact print lead, several fragmentary exact NIJL witnesses, a stronger Korean branch picture, and several new control containers, while also proving that some lingering leads were dead ends or non-independent duplicates rather than hidden wins.

- That wave has now been cashed out into real holdings: `YJG-W22` is fully in hand, and `YJG-A10` / `YJG-A11` are no longer abstract control leads but real held image tranches. The editorial consequence is that the first OCR tranche should widen to include `YJG-W22`, while the new anthology controls and fragmentary witnesses stay out of tranche 1.

- OCR has now actually started, not just been planned.

- The sane first move was to start with the exact witnesses that are already locally image-backed rather than stalling on the PDF-backed tranche.

- The first live startup pass did exactly what a startup pass should do: it exposed the runtime split that the package really needs. Paddle had to move to Python `3.12`; Tesseract had to be given a real `chi_tra` data path; RapidOCR and EasyOCR were already viable in the default environment.

- The resumed tranche did not turn out to be a one-command matter. A shell-bound sequential launcher could make real progress, but it would also hit execution time limits before the whole image tranche was done.

- The honest fix was not to fake completion or restart blindly. It was to preserve the resumable package-local outputs, confirm that RapidOCR had already completed cleanly across the three active witnesses, and then reopen only the incomplete witness-engine jobs under a bounded background scheduler with logs.



- A later OCR checkpoint showed that the first recovery scheduler had kept real work alive but had also left some incomplete tranche-1 jobs waiting behind a four-slot queue. The package therefore widened the live resumable batch intentionally instead of pretending that partial directories meant real progress everywhere.

- At the current checkpoint, RapidOCR is complete on all three active witnesses, PaddleOCR is complete on YJG-W16, and the remaining PaddleOCR, EasyOCR, and Tesseract jobs are still advancing honestly under the same package-local output and log surfaces.





## 2026-05-11



- The tranche-1 image baseline is now actually complete, not just mostly complete. All four engines finished across `YJG-W16`, `YJG-W17`, and `YJG-W22` under the package-local resumable outputs and logs.

- The notable edge cases at completion are benign and recorded rather than hidden: `YJG-W16` `RapidOCR` page `page-0055`, plus `YJG-W22` `RapidOCR` and `EasyOCR` page `page-0068`, each completed with no extracted text.

- With the engine baseline complete, the next honest move is no longer more startup OCR. It is page-span identification and anchor planning on top of the completed OCR surfaces.

- That anchor-planning move has now been completed for the active exact image tranche. The package has confirmed where the poem actually lives in `YJG-W16`, `YJG-W17`, and `YJG-W22`, and it has converted those spans into a witness-by-witness page-tier and line-tier plan without faking final geometry.


- That planning result has now been cashed out into the first actual poem-locus opening rather than left as a paper plan. The package has derived a stable tranche-bounded line map from the confirmed spans and opened the base register at page-plus-line tier across `YJG-W16`, `YJG-W17`, and `YJG-W22`.

- The opening stays honest about mixed boundaries. `page-0004` in all three active witnesses, `page-0057` in `YJG-W17`, and `page-0063` in `YJG-W22` are recorded as provisional line-tier loci inside the confirmed poem frame rather than being promoted to fake final segmentation or unnecessary character boxes.

- The next bounded slice is now narrower and better defined: real exact-witness comparison/transcription should start against the opened loci, with the mixed opening pages and `YJG-W22` `page-0063` as the first tightening targets.

