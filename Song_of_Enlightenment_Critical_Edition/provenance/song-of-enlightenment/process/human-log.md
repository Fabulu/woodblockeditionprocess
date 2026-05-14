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


- The first exact-witness comparison slice did not merely tighten a few line edges. It exposed that the startup opening span had been opened three pages too early in all three active exact witnesses.

- The important correction is now in place: YJG-W16, YJG-W17, and YJG-W22 all begin the poem on mixed opening page page-0007, while their earlier page-0004 to page-0006 leaves are title or prefatory prose rather than poem body.

- The slice also did the bounded closing work it was supposed to do. YJG-W17 page-0057 still stands as the terminal poem-bearing leaf in the held capture, and YJG-W22 page-0063 still stands as the final mixed poem boundary before the explicit afterword on page-0064.

- That means the package now honestly reflects a real first comparison/transcription batch rather than only a startup opening: the base register, line map, anchor-planning document, machine-readable state, and evidence logs all agree on the corrected opening and closing loci.

## 2026-05-12

- The next honest move after correcting the spans was not another span note. It was to begin transcribing the opening text itself from the corrected true openings.

- That opening work has now actually started. The package has stabilized the shared opening passage through `六度萬行體中圓` from direct image comparison on `YJG-W16` and `YJG-W17`, while keeping `YJG-W22` in play at the corrected opening page instead of forcing confidence from a visually interfered early-interior leaf.

- The closing watchpoints were not dropped while doing that work. `YJG-W17 page-0057` and `YJG-W22 page-0063` were re-checked directly and remain live boundary loci for the next tranche rather than silently assumed solved.


- The package has now carried the next early-interior tranche forward conservatively rather than trying to clear the whole adjacent page at once. The clean shared `YJG-W16` / `YJG-W17` `page-0009` surface supports the continuation through `比來塵鏡未曾磨 今日分明須剖析`.

- `YJG-W22` remains useful at the corrected opening and closing boundary, but it still does not provide a clean local early-interior comparison page because the inserted manuscript leaf continues to interfere with that surface.


- The package has now carried the next adjacent shared interior page forward as a separate bounded batch. The clean shared `YJG-W16` / `YJG-W17` `page-0010` surface supports the continuation through `決定說 表真僧 有人不肯任情徵`.

- `YJG-W22` remains useful at the corrected opening and closing boundary, but it still was not forced into the shared `page-0010` transcription because the package only needed the clean Toyo and Berkeley witness agreement for this batch.
- The package has now repaired the committed shared `page-0011` tranche into real transcribed text rather than placeholders. The clean shared `YJG-W16` / `YJG-W17` `page-0011` surface supports the continuation through `常獨行 常獨步 達者同遊涅槃路`.

- The package has also carried the next shared interior page forward as another separate bounded batch. The clean shared `YJG-W16` / `YJG-W17` `page-0012` surface supports the continuation through `三身四智體中圓 八解六通心地印`.

- `YJG-W22` remains useful at the corrected opening and closing boundary, but it still was not forced into the shared `page-0011` or `page-0012` transcription because the package only needed the clean Toyo and Berkeley witness agreement for these batches.

- The package has now carried three more consecutive shared interior pages forward without leaving the stable shared body. The clean shared `YJG-W16` / `YJG-W17` `page-0013` to `page-0015` surfaces support the continuation through `爭似無為實相門 一超直入如來地`.

- `YJG-W22` remains useful at the corrected opening and closing boundary, but it still was not forced into the shared `page-0013` to `page-0015` transcription because the package only needed the clean Toyo and Berkeley witness agreement for these batches.

- The package has now carried the next two consecutive shared interior pages forward in one uninterrupted run. The clean shared `YJG-W16` / `YJG-W17` `page-0016` to `page-0017` surfaces support the continuation through `無量法門咸在目前 咫尺匪遙蹔時岐隔`.

- `YJG-W22` remains useful at the corrected opening and closing boundary, but it still was not forced into the shared `page-0016` to `page-0017` transcription because the package only needed the clean Toyo and Berkeley witness agreement for this shared-body run.

- The package has now carried five more consecutive shared-interior loci forward without leaving the shared body, but the evidence basis had to tighten. The active exact witnesses no longer exposed the next continuation cleanly at full-page OCR level, so the tranche was stabilized only after restricting the OCR to the registered `poem-band` surfaces.

- That filtered shared-body continuation now reaches through `我今解此如意珠 信受之者皆相應`, with the post-`無量法門咸在目前 咫尺匪遙蹔時岐隔` run held to the repeated `師子吼`, `無畏`, `一句了然超百億`, and `河沙` recoveries that remained stable across the active exact witnesses.

- `YJG-W22` remains useful at the corrected opening and closing boundary, but it still was not forced into this post-`page-0017` shared-body continuation because the NIJL shared-interior surface did not become comparably clean after poem-band filtering.

- Direct review of the next registered left-frame surfaces in `YJG-W16 page-0019` and `YJG-W17 page-0021` has now shown that the package really did hit the honest stopping point at `我今解此如意珠 信受之者皆相應`.

- Those post-frontier surfaces break into commentary-style prose and back-references to already stabilized lines such as `行亦禪`, `坐亦禪`, `體安然`, and `忍辱`, so the next correct slice is boundary-focused closing work rather than one more fabricated shared-interior continuation.

- That boundary-focused closing work has now been completed for the active exact witness set. The Berkeley terminal page `YJG-W17 page-0057` turned out not to be poem text at all but a dated terminal note, so the real Berkeley closing page is `page-0056`.

- The NIJL closing page also tightened honestly rather than being forced shut. `YJG-W22 page-0063` remains the final poem page before the explicit afterword on `page-0064`, but only at page tier; its internal closing geometry still needs later non-boundary editorial work if line or character disputes matter.

- The practical consequence is that the package should now stop pretending boundary-focused closing is still open. The next honest bounded phase is copy-text selection, while the PDF-backed first-tier witnesses remain queued for a separate render-preparation slice and `YJG-W12` stays blocked honestly.

## 2026-05-14

- The next honest move after the boundary closeout was not more closing. It was finally to lock the copy-text.

- The package has now done that. `YJG-W22` is selected as copy-text because it is the earliest complete independent exact witness already in active local image comparison with a verified poem span, not because every one of its surfaces is cleaner than every later witness.

- The package is staying honest about what that does and does not mean. The early shared-interior surface in `YJG-W22` was still not forced where `YJG-W16` and `YJG-W17` were cleaner, and the closing page `page-0063` is still only fixed at page tier.

- So the next real queue item is straightforward: prepare the already held PDF-backed first-tier exact witnesses for direct use, while keeping `YJG-W12` blocked and leaving the derivative anthology controls out of that first-tier render tranche.

- That preparation step has now been done for the renderable files rather than postponed again. `YJG-W2`, `YJG-W4C`, `YJG-W4F`, `YJG-W4G`, `YJG-W8`, and `YJG-W9` now have local page-image tranches and can re-enter direct witness work as actual image surfaces.

- One witness did not cooperate, and the package is recording that bluntly instead of smoothing it over. The held `YJG-W21` PDF opens as a PDF but yields no renderable pages under the local renderer, so it stays blocked inside this slice until a better local source can be produced.

- That means the package has reached the next honest handoff: renewed exact-witness work on the six newly render-prepared first-tier witnesses, not more render-preparation theater.

- The first honest re-entry batch on that newly opened subset was opening-boundary work, not fake full-span certainty. Direct page review now fixes `YJG-W4C` at mixed opening `page-0001`, `YJG-W2` / `YJG-W4F` / `YJG-W4G` at mixed opening `page-0005`, and `YJG-W8` / `YJG-W9` at mixed opening `page-0002`.

- That opening pass also changed the practical posture of the subset. `YJG-W2` and `YJG-W4F` do not look like clean poem-only codices once reopened as local image tranches; both preserve prefatory prose before the poem and continue later into commentary or prose matter, so they should not be handled as if their poem necessarily runs to the physical end of the codex.

- `YJG-W4C` is the opposite kind of complication. The held render tranche begins directly on the poem with no prefatory leaves preserved locally, and the short `23`-page image set now looks more like a short or differently packaged witness than a normal full poem-plus-paratext codex.

- The next honest bounded step is therefore no longer "re-enter exact witnesses" in the abstract. It is closing/span tightening and witness-class differentiation on this render-prepared subset while keeping `YJG-W21` and `YJG-W12` blocked for different reasons.

- One part of that closing work has now actually completed rather than staying hypothetical. The cleaner Korean pair `YJG-W8` and `YJG-W9` both carry the late final-poem cluster through mixed `page-0055`, and `page-0056` breaks into post-poem prose or colophon matter instead of continuing the poem.

- That means the render-prepared subset is no longer one undifferentiated queue. `YJG-W8` and `YJG-W9` now have honest opening-and-closing page spans, while `YJG-W2`, `YJG-W4C`, `YJG-W4F`, and `YJG-W4G` still need their remaining closing or full-span tightening.

- The same closing-boundary tranche has now been carried forward onto two more render-prepared witnesses. `YJG-W4C` closes on mixed `page-0021`, with `page-0022` and later leaves shifting into commentary-style or editorial prose; `YJG-W4G` closes on mixed `page-0058`, with `page-0059` and later leaves shifting into post-poem quotation, prose, or colophon matter.

- That leaves only the genuinely harder commentary-bearing pair inside this local phase. `YJG-W2` and `YJG-W4F` still need full-span tightening, while `YJG-A10` and `YJG-A11` remain second-tier controls and `YJG-W21` / `YJG-W12` stay blocked honestly.
