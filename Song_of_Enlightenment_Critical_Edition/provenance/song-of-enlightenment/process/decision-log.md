# Decision Log



## D-001 `2026-05-09`



- Decision: start a dedicated critical-edition package for `永嘉證道歌`.

- Reason: it is the strongest poem-shaped follow-up to `信心銘`, with direct local witness overlap through `四部録`, high Chan relevance, and a bounded scope suitable for the now-established poem-first workflow.



## D-002 `2026-05-09`



- Decision: begin in witness-hunt mode and do not lock a copy-text yet.

- Reason: the local inherited anthology witness is strong enough to start from, but the edition should first secure standalone and family-diverse exact witnesses before selecting the base witness.



## D-003 `2026-05-09`



- Decision: keep commentary and translation witnesses secondary during startup.

- Reason: the first requirement is an exact witness family map for the poem itself. Commentary and reception witnesses are useful controls but should not drive the initial copy-text decision.



## D-004 `2026-05-09`



- Decision: continue widening the exact witness family before copy-text lock instead of treating the first standalone NDL witness as sufficient.

- Reason: `永嘉證道歌` appears to have a healthier exact witness ecology than the first local survey suggested, including multiple Commons-hosted exact witnesses. This justifies a wider acquisition pass before OCR begins.



## D-005 `2026-05-09`



- Decision: treat the Wenzhou Commons category as a structured exact-witness family with file-level child witnesses rather than one vague lead.

- Reason: the category already exposes enough file-level differentiation to support early manifestation analysis before download and OCR.



## D-006 `2026-05-09`



- Decision: remove prohibited canonical web controls from the `證道歌` package and rely only on rights-safe image/PDF witnesses plus neutral bibliographic leads.

- Reason: the package should not depend on or point to the excluded source family; exact image/PDF witnesses and library metadata are sufficient for the present hunt phase.



## D-007 `2026-05-09`



- Decision: promote the Korean exact family and the newly surfaced Japanese anthology/manuscript leads into first-class witness objects.

- Reason: the five-agent witness wave shows that the text's exact transmission is broader than the original NDL + Wenzhou picture and should be modeled before copy-text lock.



## D-008 `2026-05-09`



- Decision: track `四部録抄` and the newly surfaced Korean exact-title leads as separate branches rather than collapsing them prematurely into the earlier anthology and Korean clusters.

- Reason: the second five-agent wave surfaced enough branch-specific evidence that premature collapsing would erase potentially important witness-family distinctions.



## D-009 `2026-05-09`



- Decision: rank the witness field now and treat only a small first-tier exact set as the immediate acquisition/OCR queue.

- Reason: the package has moved past the stage where more undifferentiated witness names are helpful. A ranked queue preserves breadth while keeping OCR and later editorial work tied to the strongest independent scan-backed exact families.



## D-010 `2026-05-09`



- Decision: revise the first-tier queue after the targeted scan-gap hunt instead of keeping the earlier placeholder ranking fixed.

- Reason: the targeted five-agent pass showed that some previously demoted Wenzhou witnesses are genuinely independent while one previously promoted Wenzhou file collapses into the NDL `1694` line. It also surfaced two additional image-backed exact Japanese standalones that deserve witness-object status.



## D-011 `2026-05-09`



- Decision: keep widening online witness coverage even after the first-tier queue is set, but treat most new additions as second-tier controls unless they materially threaten copy-text-family coverage.

- Reason: the latest five-agent sweep found real additional witnesses, but mostly in anthology, annotated, or parallel-control branches. They are worth logging now without letting the edition drift away from the ranked exact core.



## D-012 `2026-05-10`



- Decision: treat harvested IIIF page-image tranches as meaningful acquisition milestones even when the institutional source does not expose a single downloadable local PDF.

- Reason: once the full currently exposed page-image tranche is held locally, the witness is materially in hand for OCR, comparison, and later coordinate work, so the package should record it as a held image witness rather than a manifest-only placeholder.



## D-013 `2026-05-10`



- Decision: promote the newly captured `1576` Korean exact witness into the active first-tier held exact family rather than parking it as a second-tier backup.

- Reason: it is an exact standalone witness with a real scan-backed asset in hand and it fills the chronological Korean family gap between `1474` and `1647`, so its stemmatic value is stronger than that of the looser calligraphic backup-title branch.



## D-014 `2026-05-10`



- Decision: treat `YJG-W19` and `YJG-W20` as materially advanced held second-tier witnesses now that their direct public manifests are captured locally, even before full page-image harvest.

- Reason: a held manifest is enough to make later selective image harvesting deterministic and reproducible, which is a clear gain over mere catalog citation.



## D-015 `2026-05-10`



- Decision: mark `YJG-W19` as a held image witness, but keep `YJG-W20` below that level until the Gallica harvest actually completes.

- Reason: `YJG-W19` harvested cleanly, while `YJG-W20` currently only yields a partial local image tranche before host throttling interrupts the run.



## D-016 `2026-05-10`



- Decision: promote `YJG-W20` to a held second-tier image witness and prune the overlapping anthology-control set after the latest hunt.

- Reason: the slower resumable Gallica pull eventually completed, and the newest five-agent search did not uncover a materially new exact branch. The next honest move is to keep the strongest exact core and a smaller, non-overlapping control layer.



## D-017 `2026-05-10`



- Decision: treat the next `song-of-enlightenment` slice as OCR-first preflight with mandatory tiered evidence capture, not as generic OCR startup.

- Reason: the ReadZen side can now consume evidence tiers and character-level boxes directly. That means the edition process must capture page/line anchors for every poem locus and require PaddleOCR word-box output for loci that may later need character-level apparatus evidence.



## D-018 `2026-05-10`



- Decision: promote `YJG-W22` into the active first-tier exact queue, admit `YJG-W23`/`W24`/`W25` and `YJG-W28` as real new branch evidence, and collapse `YJG-W18` as non-independent from `YJG-W2`.

- Reason: the five-agent post-preflight witness wave surfaced one genuinely strong early Japanese exact print line and several real fragmentary or branch-significant witnesses, while also resolving that the Okura lead does not widen the exact family independently.



## D-019 `2026-05-10`



- Decision: after actual capture, expand OCR tranche 1 to include `YJG-W22`, but keep `YJG-A10` and `YJG-A11` as held second-tier controls and keep `YJG-W23`/`W24`/`W25` out of the first OCR tranche.

- Reason: `YJG-W22` is now a fully held exact image witness with strong independence and full page coverage. `YJG-A10` and `YJG-A11` are valuable control branches, but they are derivative or corrected anthology witnesses rather than first-pass exact base surfaces. `YJG-W23`/`W24`/`W25` are real but fragmentary and should not drive tranche-1 OCR.



## D-020 `2026-05-10`



- Decision: begin OCR tranche 1 on the held exact image subset `YJG-W16` / `YJG-W17` / `YJG-W22` before opening a PDF-render slice for the remaining first-tier exact witnesses.

- Reason: these three witnesses are already locally image-runnable and therefore let the package enter real OCR baseline work immediately without faking readiness for the PDF-backed tranche.



## D-021 `2026-05-10`



- Decision: split the OCR runtime by engine and interpreter instead of forcing all four engines through the default Python.

- Reason: the first live startup pass proved that PaddleOCR needs Python `3.12` with the actual `paddle` runtime, while the other engines are currently available under Python `3.14`.



## D-022 `2026-05-10`



- Decision: when the sequential tranche launcher advances real OCR but exceeds interactive shell time limits, recover by resuming only the incomplete witness-engine jobs under a bounded package-local background scheduler rather than pretending the slice is blocked or restarting the tranche from scratch.

- Reason: the package already has resumable per-engine outputs and per-page summaries. Preserving that state keeps the OCR evidence honest, avoids duplicate work, and lets the tranche continue to completion without degrading the established runtime split or logging surfaces.





## D-023 2026-05-10



- Decision: when the first bounded recovery scheduler leaves additional incomplete tranche-1 jobs waiting behind a four-worker queue, open the remaining incomplete witness-engine jobs manually under the same package-local runner and logs instead of letting the tranche idle in artificial serialization.

- Reason: the package has enough local CPU headroom to keep more of the incomplete resumable jobs moving at once, and widening the active batch preserves the same evidence-capture rules while reducing queue-bound delay.





## D-024 `2026-05-11`



- Decision: treat OCR tranche 1 as complete once all four engine summaries reach completed state across `YJG-W16` / `YJG-W17` / `YJG-W22`, even if one final page records zero extracted text.

- Reason: the startup goal for this slice is engine-complete baseline coverage with honest evidence capture, not forced non-empty text on every page. The recorded zero-text results on `YJG-W16` `RapidOCR` page `page-0055` and `YJG-W22` page `page-0068` under `RapidOCR` and `EasyOCR` are completed blank-page results, not runtime blockers.


## D-025 `2026-05-11`



- Decision: complete the current OCR-derived planning slice by fixing poem-bearing page spans and page-plus-line planning in a dedicated package-local planning document, but do not yet open speculative line rows in `anchor-base-register.jsonl`.

- Reason: the completed four-engine baseline and direct image checks are strong enough to identify the true poem spans and the mixed opening or closing boundary pages. They are not, by themselves, a license to pretend that every final line locus has already been adjudicated. The honest next move is to lock the spans and page classes now, then open actual anchor rows during the first comparison or transcription slice.


## D-026 `2026-05-11`

- Decision: convert the completed poem-span plan into a first stable page-plus-line base-anchor opening now, but keep the mixed opening and closing pages explicitly provisional rather than forcing character-tier precision.

- Reason: the package already has enough direct page evidence to open honest poem-band and line-tier loci for the tranche-1 exact witnesses. Leaving the register empty would stall the comparison workflow, while pretending the mixed boundary pages were already graph-resolved would overclaim what this slice actually established.



## D-027 2026-05-11

- Decision: override the startup opening-span assumption for YJG-W16, YJG-W17, and YJG-W22 and reset the true mixed opening page in all three witnesses from page-0004 to page-0007, while keeping YJG-W17 page-0057 and YJG-W22 page-0063 as the live closing-boundary loci.

- Reason: the first exact-witness comparison pass against the actual page images showed that page-0004 to page-0006 in all three active witnesses are title or prefatory prose surfaces rather than poem body. Leaving those rows open as poem loci would overstate the evidence and contaminate the first transcription tranche.

## D-028 `2026-05-12`

- Decision: open the first corrected-opening transcription batch from the shared opening passage visible on `YJG-W16` and `YJG-W17`, while retaining `YJG-W22 page-0007` as a corrected-opening control and keeping `YJG-W17 page-0057` plus `YJG-W22 page-0063` active as unresolved boundary watchpoints.

- Reason: the corrected true openings now support real line-content comparison. `YJG-W16` and `YJG-W17` provide the cleanest immediately legible early interior surfaces, while the locally held `YJG-W22` early-interior image surface is visually interfered by an inserted manuscript leaf and is therefore better used in this batch as an opening-control witness rather than a forced primary interior transcription surface.


## D-029 `2026-05-12`

- Decision: continue the next bounded early-interior transcription batch from the shared `YJG-W16` / `YJG-W17` `page-0009` surface, but only for the first clearly recoverable continuation after `六度萬行體中圓`.

- Reason: the package can extend the stabilized poem text honestly on the clean Toyo and Berkeley interior page without pretending that the whole adjacent tranche is already solved. `YJG-W22` still does not supply a comparably clean local early-interior control, so the honest move is a conservative shared-page continuation rather than a larger forced synthesis.


## D-030 `2026-05-12`

- Decision: continue the next bounded adjacent-interior transcription batch from the shared `YJG-W16` / `YJG-W17` `page-0010` surface through `誰無念 誰無生 若實無生無不生`, while keeping `YJG-W17 page-0057` and `YJG-W22 page-0063` active as boundary watchpoints.

- Reason: the clean Toyo and Berkeley `page-0010` images support one more honest shared-page continuation after `比來塵鏡未曾磨 今日分明須剖析` without reopening witness hunt or forcing the locally interfered `YJG-W22` adjacent-interior surface into false certainty.
## D-031 `2026-05-12`

- Decision: continue the next bounded shared-interior transcription batch from the shared `YJG-W16` / `YJG-W17` `page-0011` surface through `常獨行 常獨步 達者同遊涅槃路`, while keeping `YJG-W17 page-0057` and `YJG-W22 page-0063` active as boundary watchpoints.

- Reason: the clean Toyo and Berkeley `page-0011` images support one more honest shared-page continuation after `有人不肯任情徵` without reopening witness hunt or forcing the locally interfered `YJG-W22` shared-interior surface into false certainty.

## D-032 `2026-05-12`

- Decision: continue the next bounded shared-interior transcription batch from the shared `YJG-W16` / `YJG-W17` `page-0012` surface through `三身四智體中圓 八解六通心地印`, while keeping `YJG-W17 page-0057` and `YJG-W22 page-0063` active as boundary watchpoints.

- Reason: the clean Toyo and Berkeley `page-0012` images support another honest shared-page continuation after `常獨行 常獨步 達者同遊涅槃路` without reopening witness hunt or forcing the locally interfered `YJG-W22` shared-interior surface into false certainty.

## D-033 `2026-05-13`

- Decision: continue the next bounded shared-interior transcription batch from the shared `YJG-W16` / `YJG-W17` `page-0013` surface through `鏡裏看形見不難 水中捉月爭拈得`, while keeping `YJG-W17 page-0057` and `YJG-W22 page-0063` active as boundary watchpoints.

- Reason: the clean Toyo and Berkeley `page-0013` images support another honest shared-page continuation after `三身四智體中圓 八解六通心地印` without reopening witness hunt or forcing the locally interfered `YJG-W22` shared-interior surface into false certainty.

## D-034 `2026-05-13`

- Decision: continue the next bounded shared-interior transcription batch from the shared `YJG-W16` / `YJG-W17` `page-0014` surface through `自從頓悟了無生 於諸榮辱何憂喜`, while keeping `YJG-W17 page-0057` and `YJG-W22 page-0063` active as boundary watchpoints.

- Reason: the clean Toyo and Berkeley `page-0014` images support another honest shared-page continuation after `鏡裏看形見不難 水中捉月爭拈得` without reopening witness hunt or forcing the locally interfered `YJG-W22` shared-interior surface into false certainty.

## D-035 `2026-05-13`

- Decision: continue the next bounded shared-interior transcription batch from the shared `YJG-W16` / `YJG-W17` `page-0015` surface through `爭似無為實相門 一超直入如來地`, while keeping `YJG-W17 page-0057` and `YJG-W22 page-0063` active as boundary watchpoints.

- Reason: the clean Toyo and Berkeley `page-0015` images support another honest shared-page continuation after `自從頓悟了無生 於諸榮辱何憂喜` without reopening witness hunt or forcing the locally interfered `YJG-W22` shared-interior surface into false certainty.

## D-036 `2026-05-13`

- Decision: continue the next bounded shared-interior transcription batch as one uninterrupted run across the shared `YJG-W16` / `YJG-W17` `page-0016` to `page-0017` surfaces through `無量法門咸在目前 咫尺匪遙蹔時岐隔`, while keeping `YJG-W17 page-0057` and `YJG-W22 page-0063` active as boundary watchpoints.

- Reason: the clean Toyo and Berkeley `page-0016` to `page-0017` images support a longer honest shared-body continuation after `爭似無為實相門 一超直入如來地`; the package does not need to fragment that same slice class into tiny stops, and it still does not need to force the locally interfered `YJG-W22` shared-interior surface into false certainty.

## D-037 `2026-05-13`

- Decision: close the active boundary-focused tranche by removing `YJG-W17 page-0057` from the poem span and fixing `YJG-W22 page-0063` as the final poem page at page tier, then hand the package forward to copy-text selection rather than reopening boundary work.

- Reason: direct witness-image recheck shows that Berkeley `page-0057` is a dated terminal note beginning `庚辰秋仲住蔣山...` rather than a surviving poem leaf, while NIJL `page-0063` remains the last poem-bearing page before the explicit afterword on `page-0064`. No further honest progress remains in this exact boundary slice without changing phase.


## D-038 `2026-05-14`

- Decision: allow one more selective apparatus continuation tranche, but only as grouped poem-level entries built from already stabilized evidence classes rather than as fresh locus-by-locus variant adjudication.

- Reason: the existing stabilized surfaces still support one ordinary continuation pass across the clean early interior, the main shared interior run, and the later poem-band-filtered receipt cluster. Beyond those grouped classes, the next apparatus work would no longer be simple continuation; it would require fresh editorial selection or a different phase such as translation opening.

## D-039 `2026-05-14`

- Decision: open translation sync now, beginning with a bounded tranche from the stabilized opening through the first clean interior continuation.

- Reason: ordinary apparatus continuation is exhausted, and the package already has an accepted Chinese text basis for these loci. Translation is the next honest local phase because it can now proceed from the stabilized poem text without forcing new witness adjudication or reopening blocked witnesses.

## D-040 `2026-05-14`

- Decision: continue the same translation-sync phase immediately through the main clean shared interior run, ending at `無量法門咸在目前 咫尺匪遙蹔時岐隔`.

- Reason: after the first translation tranche, the next required slice remained a normal local continuation on already stabilized loci. The clean shared interior run is the largest adjacent same-class batch still supported by the current evidence without requiring new apparatus selection or blocked-witness reopening.

## D-041 `2026-05-14`

- Decision: complete one final translation-sync tranche through the late poem-band-filtered receipt cluster at `我今解此如意珠 信受之者皆相應`, then stop the local continuation queue there for now.

- Reason: this was the last already stabilized Chinese frontier that still lacked synchronized English rendering. Beyond it, no further honest local continuation remains inside the present package evidence without reopening finer closing adjudication, blocked witnesses, or fresh apparatus-level judgment.

## D-042 `2026-05-14`

- Decision: open the selective apparatus as a machine-readable layer now, but keep it grouped and poem-level rather than pretending full variant collation is complete.

- Reason: the newly completed first-tier OCR field materially strengthens witness-class and closure judgments, so the apparatus should no longer live only in markdown. But the package still does not have a warrant for full line-by-line or character-tier extraction from commentary-bearing, short-tranche, or blocked witnesses.

