# Decision Log: Faith in Mind

## D-001 2026-04-14 - Restart from a clean local-only package

- Decision: remove the premature `OpenZenTexts` Faith in Mind scaffold and restart in the local repo workspace
- Why: the workflow and package format were tightened after that scaffold was created
- Evidence: the removed scaffold had already jumped ahead to edition-package files before witness lock and OCR
- Confidence: high
- Actor type: `human`
- Actor id: user
- Execution actor: `agent`

## D-002 2026-04-14 - Search scope set to all credible free witnesses

- Decision: keep searching until the credible free witness space is saturated enough to lock
- Why: user requested a full research pass rather than a pilot or small edition
- Evidence: guided workflow scope decision
- Confidence: high
- Actor type: `human`
- Actor id: user

## D-003 2026-04-14 - Broader edition scope accepted

- Decision: keep a broader working set rather than limiting the edition to base witnesses only
- Why: user wanted to see what broader looks like
- Evidence: guided workflow scope decision
- Confidence: high
- Actor type: `human`
- Actor id: user

## D-004 2026-04-14 - Tier source-tradition materials as secondary controls

- Decision: use materials like `景徳伝燈録` only as secondary source-tradition controls, not core witnesses
- Why: they are contextual transmission witnesses, not automatically direct `信心銘` witnesses
- Evidence: scope clarification during guided workflow
- Confidence: high
- Actor type: `hybrid`
- Actor id: user + agent

## D-005 2026-04-14 - Keep new anthology and commentary finds outside the locked core for now

- Decision: record new reusable finds as leads and control witnesses, not as accepted in-hand core witnesses
- Why: the new hits are mostly anthology or commentary/control material and should not redefine the primary witness core by default
- Evidence: recon wave results for `五味禪`, `諸經合部`, `信心獲得章百席談 前`, and `国訳禅学大成 第二卷`
- Confidence: high
- Actor type: `agent`
- Actor id: assistant

## D-024 2026-05-05 - Open a human-authorized broad corroborative hunt for the remaining nine exhausted holdouts

- Decision: permit a broader corroborative hunt for `T1-p007.l03`, `T1-p007.l04`, `T1-p007.l08`, `T1-p007.l09`, `T1-p007.l12`, `T1-p012.l02`, `T1-p029.l02`, `T1-p029.l06`, and `T1-p030.l08`, continuing beyond `X1` and `X2` but still limiting work to materially overlapping source traditions for those exact loci
- Why: the in-package queue, the stronger direct-image-separation pass, the bounded `KR6q0359` exception, and the fresh bounded `X2` source-set pass were all already exhausted, and the human operator explicitly authorized a broader corroborative roam for the remaining nine loci only
- Evidence: `current-state.md`, `unresolved-loci.md`, the completed `X1/X2` logs, and the user instruction opening this broader nine-locus hunt
- Confidence: high
- Actor type: `hybrid`
- Actor id: user+assistant

## D-025 2026-05-05 - Keep the remaining nine loci unresolved after the broad corroborative hunt

- Decision: do not change `T1-p007.l03`, `T1-p007.l04`, `T1-p007.l08`, `T1-p007.l09`, `T1-p007.l12`, `T1-p012.l02`, `T1-p029.l02`, `T1-p029.l06`, or `T1-p030.l08` after opening `X3 = 圓悟佛果禪師語錄` and `X4 = 碧巖錄/卷第六`
- Why: `X3` gives a stronger external cadence for `T1-p030.l08` through `猛割猛斷十分棄捨轉捨轉明轉遠轉近...斷却命去`, and `X4` gives a direct `曾有人問我直得五年分疏不下` frame for the damaged `T1-p007` cluster, but the local `T1` image still does not isolate full safe line readings at any of the nine loci without forcing non-local reconstruction
- Evidence: the local `T1-p007` and `T1-p030` crops, saved OCR surfaces for `T1-p007`, `T1-p012`, `T1-p029`, and `T1-p030`, plus `X3` and `X4`
- Confidence: high
- Actor type: `agent`
- Actor id: assistant

## D-006 2026-04-14 - Witness-set lock rule

- Decision: stop the hunt only after `2` consecutive recon waves with no new credible free witness of any tier
- Why: user explicitly set that rule during guided workflow
- Evidence: guided workflow decision
- Confidence: high
- Actor type: `human`
- Actor id: user

## D-007 2026-04-14 - Count recon wave A as no-new-free

- Decision: count broad recon wave A as `no-new-free` rather than as witness growth
- Why: the only notable surfaced item in that pass was `NDL823161`, which was already present in the current Faith in Mind witness inventory
- Evidence: `FAITH_IN_MIND_WITNESSES.md` already listed `NDL823161`
- Confidence: high
- Actor type: `agent`
- Actor id: assistant

## D-008 2026-04-14 - Lock the free witness hunt after recon wave B

- Decision: lock the free Faith in Mind witness hunt now
- Why: recon wave B also produced no net-new credible free witness, satisfying the `2`-wave lock rule
- Evidence: wave B surfaced only already-known items such as `CNTS-00047968260`, `NDL2537640`, and `NDL823161`
- Confidence: high
- Actor type: `agent`
- Actor id: assistant

## D-009 2026-04-14 - Freeze witness sigla

- Decision: assign and freeze sigla `T1-T5`, `A1-A3`, `C1-C17`, and `S1-S5`
- Why: later OCR notes, apparatus entries, and editorial decisions need stable short witness labels
- Evidence: witness hunt is now locked, so sigla can be frozen without ongoing renumbering risk
- Confidence: high
- Actor type: `hybrid`
- Actor id: user + agent

## D-010 2026-04-14 - Initial copy-text ranking

- Decision: rank `T1` as the initial copy-text candidate, with `T4`, `T5`, and `T2` as the first comparison controls
- Why: `T1` is the only standalone direct witness in the locked core and therefore minimizes anthology-boundary ambiguity at the start
- Evidence: witness register, acquisition metadata, and the family split in the stemma notes
- Confidence: medium-high
- Actor type: `agent`
- Actor id: assistant

## D-011 2026-04-14 - OCR-first transcription workflow starts from T1

- Decision: the first production pass must begin with an OCR-first transcription of `T1`, and only then bring in `T4`, `T5`, and `T2` for first-pass comparison
- Why: this preserves a clear copy-text spine, maximizes OCR reliance before manual reading, and prevents premature synthetic editing
- Evidence: copy-text ranking and the locked witness hierarchy
- Confidence: high
- Actor type: `hybrid`
- Actor id: user + agent

## D-012 2026-04-14 - Lock T1 as the starting copy-text, but allow evidence-based revision

- Decision: lock `T1` as the starting copy-text for the critical edition, while allowing a later switch only through a logged, evidence-based critical decision
- Why: the edition needs a stable starting spine, but the goal is the best possible critically edited text rather than loyalty to a starting witness
- Evidence: user instruction to lock `T1` with leeway to switch if there is reason, plus the current copy-text ranking
- Confidence: high
- Actor type: `hybrid`
- Actor id: user + agent

## D-013 2026-04-14 - Use RapidOCR as the first OCR engine for T1 pass 1

- Decision: use `rapidocr_onnxruntime` as the first OCR engine for the initial `T1` pass
- Why: the machine did not have system `tesseract` or `magick`, while RapidOCR could be installed locally and produced usable probe output on `T1-p001` and `T1-p002`
- Evidence: local environment check, successful package install, and probe OCR results
- Confidence: medium-high
- Actor type: `agent`
- Actor id: assistant

## D-014 2026-04-14 - Treat the four-engine OCR loop as the target law, but log live engine health honestly

- Decision: keep `tesseract`, `RapidOCR`, `PaddleOCR`, and `EasyOCR` as the required OCR comparison loop, while explicitly logging engines that are installed but currently failing at runtime
- Why: the method depends on cross-engine comparison, but the process log must reflect actual machine behavior rather than an idealized tool list
- Evidence: `RapidOCR`, `tesseract`, and `EasyOCR` are probe-runnable; `PaddleOCR` is installed in Python `3.12` but currently fails with a Paddle runtime `NotImplementedError`
- Confidence: high
- Actor type: `hybrid`
- Actor id: user + agent

## D-015 2026-04-14 - Pin the Python 3.12 Paddle stack to the documented compatibility pair

- Decision: replace the newer failing Paddle stack with `paddleocr 3.2.0`, `paddlepaddle 3.1.1`, and `paddlex 3.2.1` in Python `3.12`
- Why: official release information documented PaddleOCR `3.2.0` as fully supporting PaddlePaddle `3.1.0` / `3.1.1`, while the newer local stack was failing during prediction
- Evidence: official release notes plus local reproduction of the `NotImplementedError` under the newer stack
- Confidence: medium-high
- Actor type: `hybrid`
- Actor id: user + agent

## D-016 2026-04-14 - Use PP-OCRv4 as the working Paddle calibration path on this machine

- Decision: use `PP-OCRv4` rather than the default `PP-OCRv5` path for the current Paddle calibration slice on this machine
- Why: after the stack downgrade, the default `PP-OCRv5` path still crashed with a Windows access violation, while `PP-OCRv4` successfully completed a saved calibration run on `T1-p001`
- Evidence: local calibration probes and saved outputs under `ocr/T1/ocr/paddleocr-ppocrv4/`
- Confidence: high
- Actor type: `agent`
- Actor id: assistant

## D-017 2026-04-15 - Enforce strict four-engine compliance before editorial use of new scan witnesses

- Decision: from this point forward, no new East Asian scan witness may influence correction, collation, or apparatus claims in any critical edition package until its four-engine status is recorded, and any sub-four-engine use must be marked provisional until the missing engine runs are logged
- Why: the user explicitly required strict protocol compliance across all critical editions, and `T4` had already begun provisional comparison from only a RapidOCR pass
- Evidence: `WORKFLOW.md`, `CRITICAL_EDITION_RECORDING_MATRIX.md`, and the recorded `T4` state in this package
- Confidence: high
- Actor type: `human`
- Actor id: user
- Execution actor: `agent`

## D-018 2026-04-15 - Tighten authority, evidence-strength, and stage-separation rules from the evaluation pass

- Decision: treat `current-state.md` as the authoritative resumability surface for this package, require explicit evidence basis plus evidence strength on non-trivial editorial actions, and forbid casual mixing of recon, transcription, collation, and edition stages
- Why: the evaluation pass correctly identified that documentation drift, hidden certainty, and blurred stage boundaries are the fastest way for a process-rich edition to collapse back into AI slop
- Evidence: `critical_edition_evaluation.md`, existing package drift at the live `T1-p032.l01` working-text locus, and the need to keep `T2` in OCR-compliance work rather than silently treating it as already comparison-ready
- Confidence: high
- Actor type: `hybrid`
- Actor id: user + agent

## D-019 2026-04-18 - Adopt the six-log forensic provenance protocol as binding package law

- Decision: adopt `EDITION_AGENT_MASTER_INSTRUCTIONS.md`, `EDITION_FORENSIC_PROVENANCE_PROTOCOL.md`, and `EDITION_TRANSLATION_DIFF_PROTOCOL.md` as binding workflow law for this package and for all later critical editions
- Why: the user explicitly required that the new protocol be baked permanently into the process rather than remaining advisory, and the active Faith in Mind package must not continue into `C6` while still lacking the required forensic log surfaces
- Evidence: top-level governance docs were updated on `2026-04-18`, the new protocol requires six synchronized process logs, and the master instructions define a mid-project Faith in Mind adoption path before further witness work
- Confidence: high
- Actor type: `hybrid`
- Actor id: user + agent

## D-020 2026-05-04 - Open a bounded external corroborative-evidence exception for the 12 exhausted holdouts

- Decision: permit a tightly bounded external corroborative-evidence exception for the 12 remaining exhausted holdouts, using the digital source `KR6q0359` only where it directly overlaps the exact unresolved local `T1` loci
- Why: the in-package queue and the stronger direct-image-separation continuation were both already exhausted, the human operator explicitly redirected the work to this narrower step, and the task is not a fresh witness hunt but a locus-specific corroborative check
- Evidence: `current-state.md`, `unresolved-loci.md`, the completed stronger local image workbench, and the user instruction opening this exception
- Confidence: high
- Actor type: `hybrid`
- Actor id: user + agent

## D-021 2026-05-04 - Accept only three KR6q0359-supported local T1 repairs and leave the remaining nine holdouts unresolved

- Decision: accept `T1-p033.l03 = 萬仞崖頭打箇筋斗直下命根斷去方得少分`, `T1-p033.l05 = 師良久云山是山水是水天是天地是地有什麼過`, and `T1-p034.l05 = 師云一穿却一提起八面玲瓏峭措無賽`; do not change the other nine holdouts
- Why: these three lines now have a defensible local `T1` frame plus exact external corroboration on the damaged opening or tail clusters, while the other nine loci still do not cross threshold without forcing non-local reconstruction
- Evidence: local `T1` page images and saved OCR surfaces for `T1-p033` and `T1-p034`, plus the bounded `KR6q0359` overlaps on the same lemma bands
- Confidence: medium-high
- Actor type: `agent`
- Actor id: assistant

## D-022 2026-05-04 - Open a fresh bounded corroborative source set for the remaining nine holdouts only

- Decision: permit one further tightly bounded corroborative-evidence exception for `T1-p007.l03`, `T1-p007.l04`, `T1-p007.l08`, `T1-p007.l09`, `T1-p007.l12`, `T1-p012.l02`, `T1-p029.l02`, `T1-p029.l06`, and `T1-p030.l08`, using the external source set `五燈會元/卷第四`, `楞嚴經`-related NTU/CBETA text for the `吾不見時何不見吾不見之處` band, and `真心直說` for the `一片月生海幾家人上樓` band only where they materially overlap those exact unresolved local loci
- Why: the in-package queue, the stronger direct-image-separation pass, and the first bounded corroborative exception on `KR6q0359` were already exhausted; the human operator explicitly redirected the work to one fresh step-2 corroborative pass for the remaining nine loci rather than to a general witness hunt
- Evidence: `current-state.md`, `unresolved-loci.md`, the saved holdout workbench, the completed `KR6q0359` exception, and the user instruction opening this fresh nine-locus bounded pass
- Confidence: high
- Actor type: `hybrid`
- Actor id: user+assistant

## D-023 2026-05-04 - Reject further T1 repairs after the fresh nine-locus corroborative source-set pass

- Decision: do not change `T1-p007.l03`, `T1-p007.l04`, `T1-p007.l08`, `T1-p007.l09`, `T1-p007.l12`, `T1-p012.l02`, `T1-p029.l02`, `T1-p029.l06`, or `T1-p030.l08` after the bounded `X2` corroborative pass
- Why: the new source set strengthens contextual or phrase-level overlap around the `趙州 / 五年分疏不下`, `吾不見時何不見吾不見之處`, and `一片月生海幾家人上樓` bands, but the local `T1` image basis still does not isolate full safe line readings at those nine loci without forcing non-local reconstruction
- Evidence: the local `T1` page images and saved OCR surfaces for `T1-p007`, `T1-p012`, `T1-p029`, and `T1-p030`, together with the bounded `X2` corroborative source set
- Confidence: high
- Actor type: `agent`
- Actor id: assistant
