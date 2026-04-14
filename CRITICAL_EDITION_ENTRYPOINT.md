# Critical Edition Entrypoint

Date: 2026-04-14
Purpose: one file a future agent can be pointed at when asked to turn a scan-rich work in `C:\woodblocks` into a rigorous OpenZen critical edition package for ReadZen.

If the user wants a guided, decision-by-decision run, start with [CRITICAL_EDITION_GUIDED_WORKFLOW.md](/abs/path/C:/woodblocks/CRITICAL_EDITION_GUIDED_WORKFLOW.md:1) first.

## Use case

If the user says something like:

- "Make a critical edition from `C:\woodblocks\Faith_in_Mind_*`"
- "Use `C:\woodblocks\Some_Text_Folder` to make a critical edition"
- "Start the OpenZen critical-edition workflow for this work"

then this file is the first thing to read.

This file is the top-level instruction sheet for the whole program. It points at the other workflow and guide files that govern acquisition, transcription, provenance, process logging, OpenZen packaging, and ReadZen display.

## Contract

The end state is not just a TEI file.

The end state is a full OpenZen critical-edition package that ReadZen can display systematically:

- source rights and witness provenance
- process history
- OCR and segmentation evidence
- apparatus / editorial decisions
- reader-facing notes / footnotes
- machine-readable stats

If any of those are missing, the work is not done.

## Starting assumptions

The user will usually point at one simply named folder in `C:\woodblocks`.

That folder is only the starting point, not the whole project.

From that folder, the agent must:

1. identify the work
2. identify the witness family and physical witness
3. find sibling folders for the same work if they already exist
4. collect the current source and witness documentation
5. follow the OpenZen critical-edition system documented below

## First files to read

Read these in this order:

1. [CRITICAL_EDITION_ENTRYPOINT.md](/abs/path/C:/woodblocks/CRITICAL_EDITION_ENTRYPOINT.md:1)
2. [OPENZENTEXTS_PROVENANCE_AUDIT_2026-04-14.md](/abs/path/C:/woodblocks/OPENZENTEXTS_PROVENANCE_AUDIT_2026-04-14.md:1)
3. [CRITICAL_EDITION_SYSTEM_SPEC_2026-04-14.md](/abs/path/C:/woodblocks/CRITICAL_EDITION_SYSTEM_SPEC_2026-04-14.md:1)
4. [PROGRAMMER_AGENT_MASTER_IMPLEMENTATION_BRIEF_2026-04-14.md](/abs/path/C:/woodblocks/PROGRAMMER_AGENT_MASTER_IMPLEMENTATION_BRIEF_2026-04-14.md:1)
5. [WORKFLOW.md](/abs/path/C:/woodblocks/WORKFLOW.md:1)
6. [REPO_INTAKE_PIPELINE.md](/abs/path/C:/woodblocks/REPO_INTAKE_PIPELINE.md:1)
7. [TRANSCRIPTION_METHOD.md](/abs/path/C:/woodblocks/TRANSCRIPTION_METHOD.md:1)
8. [STANDARD_TRANSCRIPTION_WORKFLOW.md](/abs/path/C:/woodblocks/STANDARD_TRANSCRIPTION_WORKFLOW.md:1)
9. [C:/Programmieren/OpenZenTexts/MANIFEST_SCHEMA.md](/abs/path/C:/Programmieren/OpenZenTexts/MANIFEST_SCHEMA.md:1)
10. [C:/programmieren/MergeWorkCbeta/CBETA-Translator/Text/TeiRenderer.cs](/abs/path/C:/programmieren/MergeWorkCbeta/CBETA-Translator/Text/TeiRenderer.cs:1)
11. [C:/programmieren/MergeWorkCbeta/CBETA-Translator/Views/ProvenancePanel.axaml.cs](/abs/path/C:/programmieren/MergeWorkCbeta/CBETA-Translator/Views/ProvenancePanel.axaml.cs:1)

## Main rule

Do not treat the current Wumenguan converter or current OpenZen file layout as the ceiling.

Treat them as:

- precedent
- migration material
- parser compatibility examples

The target architecture is the critical-edition system spec, not the minimal v1 Wumenguan implementation.

## What to do when given a single folder

Given a folder like:

- `C:\woodblocks\Faith_in_Mind_Korea_Commons`
- `C:\woodblocks\Faith_in_Mind_NDL_Shiburokushou`
- `C:\woodblocks\Some_Text_Source`

the agent must run this discovery loop:

### Step 1. Identify the work

Read the folder `README.md` and determine:

- work title
- witness title
- source type
- rights status

### Step 2. Find sibling witnesses

Search `C:\woodblocks` for sibling folders for the same work family.

For `信心銘`, examples include:

- [FAITH_IN_MIND_WITNESSES.md](/abs/path/C:/woodblocks/FAITH_IN_MIND_WITNESSES.md:1)
- [FAITH_IN_MIND_STEMMA.md](/abs/path/C:/woodblocks/FAITH_IN_MIND_STEMMA.md:1)
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

### Step 6. Record everything

Every pass must land in:

- process logs
- decision logs
- unresolved loci
- apparatus
- stats

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

### Step 7. Generate the OpenZen package

Produce:

- TEI
- `manifest.json`
- `process.json`
- `apparatus.json`
- `stats.json`
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

## TEI note policy

Use English notes when useful.

The current parser already supports note extraction. Preferred OpenZen note families:

- `nkr_note_crit_...`
- `nkr_note_prov_...`
- `nkr_note_trans_...`
- `nkr_note_unres_...`

If parser support is missing, the programmer agent must extend `TeiRenderer.cs` before relying on those note families.

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

## Faith in Mind instructions

For `信心銘`, begin with these anchors:

- [FAITH_IN_MIND_WITNESSES.md](/abs/path/C:/woodblocks/FAITH_IN_MIND_WITNESSES.md:1)
- [FAITH_IN_MIND_STEMMA.md](/abs/path/C:/woodblocks/FAITH_IN_MIND_STEMMA.md:1)

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

- [C:/Programmieren/OpenZenTexts/provenance/wumenguan-1632/witnesses/wumenguan-1632-ndl-README.md](/abs/path/C:/Programmieren/OpenZenTexts/provenance/wumenguan-1632/witnesses/wumenguan-1632-ndl-README.md:1)
- [C:/Programmieren/OpenZenTexts/xml-open/pd/wumenguan-1632/README.md](/abs/path/C:/Programmieren/OpenZenTexts/xml-open/pd/wumenguan-1632/README.md:1)

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

`Use C:\woodblocks\{FolderName} as the starting witness for an OpenZen critical edition. Follow C:\woodblocks\CRITICAL_EDITION_ENTRYPOINT.md and build the full documented package for ReadZen, including provenance, OCR/process logs, apparatus, stats, TEI, and display-compatible notes.`
