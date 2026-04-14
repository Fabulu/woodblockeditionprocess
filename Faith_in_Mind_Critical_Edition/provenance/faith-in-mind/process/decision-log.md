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
