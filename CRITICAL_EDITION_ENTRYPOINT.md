# Critical Edition Entrypoint

Date: 2026-04-14
Purpose: one file a future agent can be pointed at when asked to turn a scan-rich work in this repo into a rigorous OpenZen critical edition package for ReadZen.

If the user wants a guided, decision-by-decision run, start with `CRITICAL_EDITION_GUIDED_WORKFLOW.md` first.

## Use case

If the user says something like:

- "Make a critical edition from `Faith_in_Mind_*`"
- "Use `Some_Text_Folder` to make a critical edition"
- "Start the OpenZen critical-edition workflow for this work"

then this file is the first thing to read.

This file is the top-level instruction sheet for the whole program. It points at the other workflow and guide files that govern acquisition, transcription, provenance, process logging, OpenZen packaging, and ReadZen display.

The governing editorial posture is:

> AI proposes, human audits, system records.

AI may drive OCR, collation, triage, and draft editorial argument, but it must not silently finalize uncertain readings or hide ambiguity behind polished output.

## Contract

The end state is not just a TEI file.

The end state is a full OpenZen critical-edition package that ReadZen can display systematically:

- source rights and witness provenance
- process history
- OCR and segmentation evidence
- apparatus / editorial decisions
- definitive delivered witness texts
- reader-facing notes / footnotes
- machine-readable stats
- reverse-patching-compatible timeline history

ReadZen should also be able to expose witness comparison without collapsing that into the timeline or replacing the critical text surface.

If any of those are missing, the work is not done.

## Starting assumptions

The user will usually point at one simply named folder in the repo.

That folder is only the starting point, not the whole project.

From that folder, the agent must:

1. identify the work
2. identify the witness family and physical witness
3. find sibling folders for the same work if they already exist
4. collect the current source and witness documentation
5. follow the OpenZen critical-edition system documented below

## Resume rule

If the repo already contains a package or process tree for the same work, do not start from the generic witness-hunt opening.

Before doing anything else, inspect:

- `provenance/{slug}/process/current-state.md` if present
- `xml-open/*/{slug}/process.json`
- `xml-open/*/{slug}/timeline.json`
- `provenance/{slug}/process/process-log.md`
- `provenance/{slug}/process/decision-log.md`
- `provenance/{slug}/process/human-log.md`
- `provenance/{slug}/witnesses/witness-register.md`
- `provenance/{slug}/transcription/ocr-transcription-plan.md`

Then summarize:

1. what is already decided
2. what phase is already complete
3. what the recorded next step is
4. whether the user is asking to resume or to deliberately reopen an earlier stage

If those records exist, resume from the recorded next step unless the user explicitly says to reopen the witness hunt, scope, or copy-text decision.

Operational authority rule when resuming:

- `current-state.md` is the authoritative resumability surface for:
  - current phase
  - last completed bounded slice
  - exact next action
- `timeline.json` is the authoritative machine-readable event history
- if another log disagrees with `current-state.md` about what happens next, stop and reconcile the drift before more substantive work

## First files to read

Read these in this order:

1. `CRITICAL_EDITION_ENTRYPOINT.md`
2. `CRITICAL_EDITION_RECORDING_MATRIX.md`
3. `EDITION_AGENT_MASTER_INSTRUCTIONS.md`
4. `EDITION_FORENSIC_PROVENANCE_PROTOCOL.md`
5. `EDITION_TRANSLATION_DIFF_PROTOCOL.md`
6. `critical_edition_evaluation.md`
7. `OPENZENTEXTS_PROVENANCE_AUDIT_2026-04-14.md`
8. `CRITICAL_EDITION_SYSTEM_SPEC_2026-04-14.md`
9. `PROGRAMMER_AGENT_MASTER_IMPLEMENTATION_BRIEF_2026-04-14.md`
10. `WORKFLOW.md`
11. `REPO_INTAKE_PIPELINE.md`
12. `TRANSCRIPTION_METHOD.md`
13. `STANDARD_TRANSCRIPTION_WORKFLOW.md`
14. `OpenZenTexts/MANIFEST_SCHEMA.md`
15. `CBETA-Translator/Text/TeiRenderer.cs`
16. `CBETA-Translator/Views/ProvenancePanel.axaml.cs`

These three edition-protocol files are now mandatory for every critical edition session:

- `EDITION_AGENT_MASTER_INSTRUCTIONS.md`
- `EDITION_FORENSIC_PROVENANCE_PROTOCOL.md`
- `EDITION_TRANSLATION_DIFF_PROTOCOL.md`

Do not treat them as optional implementation notes. They are workflow law.

## Main rule

Do not treat the current Wumenguan converter or current OpenZen file layout as the ceiling.

Treat them as:

- precedent
- migration material
- parser compatibility examples

The target architecture is the critical-edition system spec, not the minimal v1 Wumenguan implementation.

## What to do when given a single folder

Given a folder like:

- `Faith_in_Mind_Korea_Commons`
- `Faith_in_Mind_NDL_Shiburokushou`
- `Some_Text_Source`

the agent must run this discovery loop:

### Step 1. Identify the work

Read the folder `README.md` and determine:

- work title
- witness title
- source type
- rights status

Before moving on, check whether this work already has an edition package in progress and switch to resume mode if it does.

### Step 2. Find sibling witnesses

Search this repo for sibling folders for the same work family.

For `信心銘`, examples include:

- `FAITH_IN_MIND_WITNESSES.md`
- `FAITH_IN_MIND_STEMMA.md`
- `Faith_in_Mind_*`
- `Sengcan_Faith_in_Mind_*`

### Step 3. Build the witness set

Classify every located witness as one of:

- base or near-base
- translation / reception
- commentary
- context-only

### Step 4. Build the edition plan

Before transcription or editing, create the edition charter and process tree under `OpenZenTexts/provenance/{slug}/`.

### Step 5. Push OCR as far as possible

Do OCR-first, not editor-first.

Only after OCR outputs exist should editorial adjudication begin.

Before full correction, classify the scanned pages by role.

Do not assume all pages in a witness belong to the target text body.

At minimum distinguish:

- title / cover matter
- prefatory matter
- text body
- commentary / exposition
- colophon / end matter
- blank or non-body pages

### Step 6. Record everything

Every pass must land in:

- process logs
- decision logs
- unresolved loci
- apparatus
- stats

Every critical edition package must also maintain the six forensic provenance logs under `provenance/{slug}/process/`:

- `correction-log.md`
- `translation-diff-log.md`
- `ocr-consensus-log.md`
- `rejected-readings-log.md`
- `translation-reasoning-log.md`
- `character-provenance-log.md`

Do not wait and summarize later.

Record every meaningful step while it happens:

- searches and recons
- source checks
- download attempts
- validation attempts
- OCR runs
- OCR evaluation passes
- editorial passes
- rejected paths
- stalled or failed attempts

Every editorial action must also record who made it:

- agent
- human
- hybrid

Visible text changes must also record:

- exact TEI `locus_id`
- change kind
- reason
- witness support
- evidence basis
- evidence strength
- before/after reading state captured at the moment of change

Mandatory paired-record rules:

- `correction-log.md` and `translation-diff-log.md` are never written separately
- every Chinese correction gets an English retranslation entry in the same bounded session
- OCR consensus is recorded immediately after each engine run, not reconstructed later if avoidable
- rejected readings are recorded at the moment a competing reading is refused or rolled back
- image evidence coordinates must be recorded when available

Preferred storage model:

- top-level readings table
- `reading_before` / `reading_after` indices in `timeline.json`

Use explicit evidence-strength labels:

- strong
- moderate
- weak
- provisional

Do not allow a clean-looking reading to stand without an explicit strength label in the supporting record.

### Step 6a. Keep stages hard-separated

Do not mix these stages casually:

- recon
- transcription
- collation
- edition

Rules:

- recon may discover and classify witnesses, but it does not silently enter correction
- transcription may correct a witness-facing working text, but it does not silently produce edition claims
- collation may compare witnesses and surface variant structure, but it does not silently publish a reading edition
- edition may present stabilized results, but it must still preserve uncertainty and traceability back to transcription and collation

If a slice crosses a stage boundary, declare that explicitly before starting it and update `current-state.md` and `process.json` at the same time.

### Step 7. Generate the OpenZen package

Produce:

- TEI
- `manifest.json`
- `process.json`
- `timeline.json`
- `witnesses.json`
- `apparatus.json`
- `stats.json`
- `documents.json`
- `human-log.md`
- per-text `README.md`

### Step 8. Confirm ReadZen compatibility

Check against the actual parser and provenance UI code in `CBETA-Translator`, not just against assumptions.

## Required output tree

Use the canonical target layout from the system spec:

```text
OpenZenTexts/provenance/{slug}/
  witnesses/
  process/
  ocr/
  collation/
  edition/

OpenZenTexts/xml-open/{prefix}/{slug}/
  {slug}.xml
  manifest.json
  process.json
  apparatus.json
  stats.json
  README.md
```

## Required file set

Minimum edition files:

- `manifest.json`
- `process.json`
- `witnesses.json`
- `apparatus.json`
- `stats.json`
- `{slug}.xml`
- `README.md`

Minimum process docs:

- `edition-plan.md`
- `process-log.md`
- `decision-log.md`
- `unresolved-loci.md`
- `publication-checklist.md`

Minimum witness docs:

- one `README.md` per physical witness
- source-page evidence
- rights evidence
- file hash and size data

## Download integrity rule

For large PDFs and other fragile witness files:

- do not trust one command-line download
- compare hashes across repeated downloads when a file fails structural validation
- treat differing hashes as evidence of unstable delivery or local download corruption

Escalation path:

1. validate current download
2. if structurally bad, re-download and compare hashes
3. if command-line delivery remains unstable, switch to exact browser download using the pinned direct file URL
4. swap the browser-downloaded file into the canonical witness folder
5. hash and validate again before clearing the witness

## TEI note policy

Use English notes when useful.

The current parser already supports note extraction. Preferred OpenZen note families:

- `nkr_note_crit_...`
- `nkr_note_prov_...`
- `nkr_note_trans_...`
- `nkr_note_unres_...`

If parser support is missing, the programmer agent must extend `TeiRenderer.cs` before relying on those note families.

Use notes only for short reader-facing locus-linked content.

Do not use TEI notes as a duplicate:

- `process-log.md`
- `decision-log.md`
- `human-log.md`

If the content is primarily chronology, workflow explanation, or full editorial reasoning, keep it out of the note layer.

## Surface separation policy

The implementation must preserve separate surfaces for:

- the critical reading text
- witness comparison
- editorial timeline replay

Witness comparison should be locus-driven and should open individual witness readings directly.

The final package must therefore include definitive delivered witness texts and machine-readable witness lookup, not only the critical text and apparatus.

Those delivered witness texts must also be machine-alignable to shared edition loci at handoff.

Preferred:

- the app can ask any delivered witness for its reading at `locus_id X`

Fallback when exact line-for-line matching is impossible:

- witness-local anchors such as page-line or segment ids
- a locus map from edition `locus_id` to witness-local span start / end
- explicit gap statuses for omitted, lacunose, unreadable, or uncertain text

Do not leave witness alignment to viewer heuristics.

Timeline replay should remain about edition-state history, not raw witness browsing.

## Publication standard

Do not call the work a critical edition unless:

1. witness rights are locked
2. witness hashes are locked
3. OCR runs are recorded
4. editor interventions are recorded with actor identity
5. apparatus exists
6. unresolved loci are classified
7. TEI validates
8. ReadZen can display the result coherently
9. required JSON files parse and validate where supported
10. cross-file references resolve cleanly

## Final release pass

Before release or handoff, perform one explicit final pass for coherence and machine usability.

Check:

- `manifest.json`
- `process.json`
- `timeline.json`
- `witnesses.json`
- `apparatus.json`
- `stats.json`
- `documents.json`
- TEI note anchors and targets

Confirm:

- JSON integrity
- schema validation where available
- existing file paths for all registered documents and manifest targets
- definitive delivered witness texts exist for all witnesses declared in viewer comparison data
- coherent separation between notes, apparatus, decision log, and human-log surfaces

## Faith in Mind instructions

For `信心銘`, begin with these anchors:

- `FAITH_IN_MIND_WITNESSES.md`
- `FAITH_IN_MIND_STEMMA.md`

The agent must not assume one witness equals the whole work.

It must distinguish:

- standalone `信心銘`
- `四部録`
- `四部録抄`
- `入衆日用`
- commentary branch
- translation/reception branch

## Wumenguan instructions

Use Wumenguan as the migration exemplar, not as the final model.

Before using it as precedent, reconcile these stale files:

- `OpenZenTexts/provenance/wumenguan-1632/witnesses/wumenguan-1632-ndl-README.md`
- `OpenZenTexts/xml-open/pd/wumenguan-1632/README.md`

## If the agent is asked to "just do it"

That means:

1. discover the full witness set from the one pointed folder
2. create the edition plan
3. create the OpenZen process tree
4. create or extend any missing parser/UI/schema support
5. only then produce the edition artifacts

Do not stop at "I found the files".
Do not stop at "I wrote the TEI".
Do not stop at "the provenance exists".

The goal is the full documented edition system.

## Short operational prompt

If a future user wants to launch this workflow with one sentence, this is the model:

`Use {FolderName} in this repo as the starting witness for an OpenZen critical edition. Follow CRITICAL_EDITION_ENTRYPOINT.md and build the full documented package for ReadZen, including provenance, OCR/process logs, apparatus, stats, TEI, and display-compatible notes.`
