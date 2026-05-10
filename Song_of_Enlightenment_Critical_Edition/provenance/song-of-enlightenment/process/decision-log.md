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
