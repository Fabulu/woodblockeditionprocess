# OpenZen Critical Edition System Spec

Date: 2026-04-14
Audience: programmer agent, curator, future editorial agents
Purpose: define a repeatable, scan-first, OCR-maximal workflow for rigorous OpenZen critical editions, starting with `信心銘`.

## Goals

Build a system where:

- source rights and witness provenance are locked down
- OCR is pushed as far as possible before editorial intervention
- every editorial intervention is logged, whether by agent or human
- every decision is traceable
- every meaningful workflow step is traceable, including failed and abandoned steps
- every meaningful workflow step is chronologically reconstructable as state changes over time
- every published edition has a coherent artifact tree
- the app can display:
  - quick licensing and source facts in the sidebar
  - full process, apparatus, and stats in a dedicated browser

These surfaces must remain distinct:

- critical reading text
- witness comparison
- timeline / editorial history

## Shared path policy

Shared markdown and JSON examples intended for repo use must not depend on:

- local absolute filesystem paths like `C:\...`
- renderer-only absolute links

Use instead:

- repo-relative paths
- repo-name-relative paths when referring to another repository
- normal web URLs for online sources

## Non-goals

- no OCR or edition production in this planning pass
- no TEI body editing in this planning pass
- no UI implementation in this planning pass

## High-level architecture

Separate the edition into four layers:

1. `acquisition`
   Raw witness capture, rights evidence, hashes, file validation

2. `transcription`
   OCR outputs, page segmentation, editorial adjudication work products

3. `edition`
   The editorial text, apparatus, decisions, and TEI output

4. `presentation`
   Manifest and derived JSON documents used by the app

## Required directory layout

For each work slug, use one canonical tree in `OpenZenTexts`:

```text
provenance/{slug}/
  witnesses/
    {witness-id}/
      README.md
      source_page.html
      rights_evidence/
      files/
  process/
    edition-plan.md
    process-log.md
    decision-log.md
    unresolved-loci.md
    publication-checklist.md
    stats.json
  ocr/
    {witness-id}/
      metadata.json
      page-map.csv
      page-images/
      leaf-images/
      ocr/
        tesseract/
        rapidocr/
        paddleocr/
      evaluation/
        sample-ground-truth.csv
        engine-comparison.json
  collation/
    witness-map.json
    locus-table.csv
    apparatus.json
    family-stemma.md
  edition/
    base-text.md
    reading-edition.md
    diplomatic-transcript.md
    commentary-notes.md
```

Published output stays here:

```text
xml-open/{prefix}/{slug}/
  {slug}.xml
  manifest.json
  process.json
  witnesses.json
  apparatus.json
  stats.json
  README.md
```

## Canonical roles of the files

## Output modes

Every critical edition must emit outputs in clearly separated modes.

The programmer should treat these as distinct product surfaces, not interchangeable blobs.

### Mode 1. Sidebar provenance mode

- purpose: concise source and license facts
- primary artifact: `manifest.json`
- must stay short and reader-facing

### Mode 2. Process mode

- purpose: reproducible editorial workflow history
- primary artifacts:
  - `process.json`
  - `process/edition-plan.md`
  - `process/process-log.md`
  - `process/decision-log.md`
  - `process/unresolved-loci.md`
  - `process/publication-checklist.md`

### Mode 2A. Timeline mode

- purpose: replayable chronological reconstruction of how the edition was built
- primary artifacts:
  - `timeline.json`
  - `human-log.md`
- must support visible state changes, not only static summaries

### Mode 3. Apparatus mode

- purpose: structured variant and editorial-decision display
- primary artifacts:
  - `apparatus.json`
  - TEI note and apparatus anchors where appropriate

### Mode 3A. Witness delivery mode

- purpose: definitive delivered witness texts plus programmatic witness lookup
- primary artifacts:
  - `witnesses.json`
  - definitive witness text files
  - per-witness locus or page-line maps where available

### Witness alignment handoff rule

Published witness delivery is not complete unless the program can tell which witness passage belongs to which editable locus.

At handoff, witness texts must line up against shared edition loci by machine-readable contract.

Preferred contract:

- one shared `locus_id` space across the critical text, apparatus, and delivered witnesses
- each delivered witness can answer "what is your text at locus X?"
- one witness reading may map to:
  - one locus
  - multiple contiguous loci
  - a lacuna / omission / unreadable state at that locus

Do not require exact one-line-equals-one-line visual formatting across all witnesses.

That will often fail in commentary witnesses, prose witnesses, damaged witnesses, or witnesses whose page layout cuts across the edition lineation.

What is mandatory is machine-readable alignment.

If exact line alignment is not possible, fallback is:

- stable witness text file
- stable witness-local anchors such as page-line or segment ids
- a locus map that maps edition `locus_id` to witness span start / end
- explicit statuses such as `present`, `omitted`, `lacuna`, `unreadable`, `uncertain_span`

Unmapped free text is not an acceptable final delivery format for witness comparison.

### Mode 4. Stats mode

- purpose: compact machine-readable quantitative summary
- primary artifact: `stats.json`

### Mode 5. Document registry mode

- purpose: curated list of human-readable supporting documents
- primary artifact: `documents.json`
- must not rely on arbitrary markdown autodiscovery

### Mode 6. Edition text mode

- purpose: the actual reading text with notes and anchors
- primary artifact: `{slug}.xml`

### Separation rule

The UI and pipeline must preserve mode separation:

- sidebar provenance mode stays concise
- process/apparatus/stats/documents open in a dedicated edition dialog or browser
- edition text mode remains the reading surface
- witness delivery mode must support direct witness browsing and locus comparison
- timeline mode must be able to replay how the reading surface and editorial state changed over time

### `manifest.json`

This is the source-rights and witness-summary document for the UI sidebar.

It should answer only:

- what is this text
- what license applies
- what witnesses were used
- where they came from
- whether commercial use is allowed
- whether the source chain is CBETA-clean

It should not try to hold the full edition process.

### `process.json`

This is the machine-readable editorial workflow record.

Required top-level sections:

- `project`
- `base_witness`
- `witness_families`
- `ocr_pipeline`
- `segmentation_pipeline`
- `editor_passes`
- `decision_records`
- `coverage`
- `unresolved_loci`
- `publication_checks`
- `derived_artifacts`
- `timeline`
- `state_model`

### `timeline.json`

This is the canonical ordered event stream for the edition.

It is not optional.

Every meaningful action that changes knowledge, text state, witness state, or editorial state must appear here.

The preferred reconstruction model is reverse-patching from the final reading text.

For visible text changes, the preferred storage contract is:

- top-level per-locus `readings` table
- `reading_before` and `reading_after` indices in each `text_changed` event

Fallback only if necessary:

- `previous_reading`
- `new_reading`

Minimum event fields:

- `event_id`
- `sequence`
- `timestamp`
- `stage`
- `event_type`
- `object_type`
- `object_id`
- `summary`
- `details`
- `actor_type`
- `actor_id`
- `inputs`
- `outputs`
- `evidence_links`
- `decision_ref`
- `status`
- `state_effect`

Required event classes include:

- witness found
- witness rejected
- download attempted
- download replaced
- hash changed
- validation passed
- validation failed
- copy-text locked
- copy-text challenged
- copy-text switched
- OCR run started
- OCR run completed
- OCR run failed
- correction applied
- unresolved locus opened
- unresolved locus resolved
- apparatus seed added
- decision recorded
- text changed

### `human-log.md`

This is the human-readable narrative counterpart to `timeline.json`.

It must explain, in readable prose:

- what happened
- why it happened
- what changed
- what remains unresolved

It is the text shown in the log dialog for readers who do not want raw JSON.

### `apparatus.json`

This is the machine-readable variant/apparatus layer for UI display and stats.

Each entry should include:

- `locus_id`
- `tei_target`
- `lemma`
- `readings[]`
- `witnesses_supporting`
- `decision`
- `decision_basis`
- `status`

### `witnesses.json`

This is the machine-readable witness delivery registry for the viewer.

It is not optional for a published critical edition that intends to expose witness comparison.

Each witness entry should include at minimum:

- `witness_id`
- `siglum`
- `label`
- `family_id`
- `role`
- `definitive_text_file`
- `text_format`
- `text_status`
- `completeness`
- `confidence`
- `has_locus_map`
- `locus_map_file`
- `source_readme`

The viewer must be able to answer from this file:

- what witnesses exist
- which text artifact is the definitive delivered text for each witness
- how to open that witness at a relevant locus

### `stats.json`

This is the compact derived summary for the app.

Required fields:

- witness counts
- page / leaf counts
- OCR engine counts
- percent of loci machine-resolved
- percent requiring editor intervention
- unresolved count
- apparatus count
- base-text confidence distribution

## Witness model

Distinguish:

- `witness_family`
  Example: `四部録`
- `physical_witness`
  Example: `NDL2537640`, `RB00012929`, `WUL-bunko31_e1087`

Each physical witness needs:

- exact source URL
- stable revision or file page
- local file path
- bytes
- SHA-256
- rights basis
- vetting status
- page count
- completeness status
- family membership
- role:
  - `base`
  - `primary-collation`
  - `secondary-collation`
  - `context-only`

## Required process stages

## Global logging rule

Do not rely on retrospective summaries.

The system must log work as it happens.

At minimum, the process layer must preserve:

- search and recon actions
- source pages checked
- download attempts
- validation attempts
- rights evaluations
- OCR runs
- OCR evaluation results
- manual adjudication passes
- witness acceptance and rejection
- deferred or abandoned options
- every editorial decision
- every state-changing event that affects what the edition currently is

Each loggable step should record:

- timestamp or date
- step category
- target object
- action
- outcome
- evidence path or URL
- actor type: `agent`, `human`, or `hybrid`
- actor identifier when known
- follow-up state if unresolved
- whether current edition state changed
- resulting state if it did

### Stage 0. Edition charter

Create:

- `provenance/{slug}/process/edition-plan.md`

It must declare:

- scope
- target edition kind
- target witnesses
- success conditions
- what counts as "published"
- what is out of scope

### Stage 1. Witness acquisition and rights lock

For every witness:

- capture source page
- capture license page if separate
- download file
- hash file
- verify file structure
- assign rights confidence
- assign completeness status

Also log:

- searches that failed to produce a usable witness
- witnesses rejected as duplicates
- witnesses rejected on rights grounds
- witnesses rejected on completeness grounds
- failed or corrupted downloads

No witness enters OCR before this stage is complete.

### Stage 2. Segmentation

Every scan witness gets:

- page inventory
- leaf split if needed
- reading-order map
- image crop metadata

Required file:

- `page-map.csv`

Columns:

- `page_id`
- `leaf_id`
- `page_number_display`
- `side`
- `image_path`
- `crop_path`
- `content_role`
- `notes`

### Stage 3. OCR-maximal pass

Run all available OCR engines first.

Default required OCR comparison loop for East Asian scan witnesses:

- `tesseract`
- `RapidOCR`
- `PaddleOCR`
- `EasyOCR`

This loop is mandatory, not optional.

An edition may proceed with the healthiest available engine for normalization, but it must not silently reduce the comparison basis.

Before manual correction is accepted as methodologically valid, each of the four engines must be:

1. run on the same calibration slice and logged with preserved output
2. or explicitly logged as blocked with exact runtime failure details

If an engine remains blocked, the blocker must remain visible in the package state and OCR logs.

If any engine in that loop is missing, unavailable, or fails on the witness, that absence or failure must be logged explicitly.

The loop exists to:

- compare OCR disagreement directly
- recover text one engine misses
- identify likely false positives
- surface damaged or unstable loci before manual intervention
- fill partial omissions from cross-engine evidence before image adjudication

Required recording:

- engine name
- version
- model name
- parameters
- run date
- input images
- output files

Also record:

- failed runs
- unusable outputs
- pages skipped
- reruns and why they were rerun

Do not allow silent OCR replacement. All engine outputs stay on disk.

### Stage 4. OCR evaluation

Before human editing, benchmark representative pages.

Required output:

- `engine-comparison.json`

At minimum compare:

- character accuracy on sample loci
- title detection
- reading-order stability
- punctuation behavior
- vertical text handling
- omission and no-text behavior
- whether one engine recovers text another misses

This stage decides:

- which engine becomes default
- which engine is comparator only
- which pages or loci require multi-engine rescue before manual review

### Physical-page classification law

Do not assume that every scanned page in a witness belongs to the edited text body.

A short poem may survive inside a much longer physical witness that also contains:

- title or cover matter
- prefatory material
- commentary or exposition
- appended notes
- colophon or publication matter
- blank or near-blank leaves

Before deep correction or collation, classify the page set.

Required output:

- `page-map.csv`

Minimum page-role categories:

- `body`
- `title`
- `preface`
- `commentary`
- `appendix`
- `colophon`
- `blank`
- `other`

Do not treat the physical page count as the poem or text-body length until this classification pass is done.

### Stage 5. Editorial adjudication

Editorial intervention begins only after OCR outputs exist.

Every editor pass must record:

- actor_type
  - `agent`
  - `human`
  - `hybrid`
- actor_id
- witness
- pages or loci touched
- reason for intervention
- whether the change was:
  - OCR-confirm
  - OCR-reject
  - image-only recovery
  - cross-witness decision

No silent interventions are allowed.

If the agent inspects a page, rejects an OCR reading, chooses one witness over another, or leaves a locus unresolved, that step must be logged even if no final text is emitted yet.

Required file:

- `process-log.md`

### Stage 6. Collation and apparatus

Build a locus table for all variant-bearing places.

Required file:

- `collation/locus-table.csv`

Minimum columns:

- `locus_id`
- `section`
- `base_text`
- `witness_id`
- `reading`
- `certainty`
- `is_ocr_only`
- `is_human_checked`
- `notes`

Then derive `apparatus.json`.

### Stage 7. Decision logging

Every non-trivial editorial choice gets a decision record.

Required file:

- `process/decision-log.md`

Every decision must include:

- issue
- options considered
- evidence
- chosen reading
- reversibility
- affected loci

If a decision changes the current edition state, it must also generate a timeline event.

If it changes visible text, it must generate a `text_changed` event with exact `locus_id`, cause, evidence, and before/after reading state captured at the moment of change.

Visible text work must be recorded by bounded slices.

For each substantial correction, collation adoption, or other text-editing batch:

1. define the slice boundary before edits begin
2. update the active pass log as the slice closes
3. update `current-state.md` so `last_completed_phase` names that slice
4. create a fresh `text_changed` timeline event for that slice

Do not merely revise the details of an older stage-start event after later text changes occur.

### Stage 8. Unresolved loci

Do not bury uncertainty in prose notes.

Required file:

- `process/unresolved-loci.md`

Each unresolved item must include:

- locus
- why unresolved
- what evidence is missing
- publication status:
  - `must-resolve-before-publication`
  - `publishable-with-note`

### Stage 9. Publication package

Only after stages 0-8:

- generate TEI
- generate manifest
- generate process/apparatus/stats JSON
- write per-text README
- run validation

## TEI policy

Use TEI for the edition text and, when appropriate, inline apparatus.

Preferred rule:

- keep the main reading text readable
- put heavy variant detail in `apparatus.json`
- optionally mirror decisive variants in TEI `<app>`, `<lem>`, `<rdg>`

## Footnote and apparatus policy

The app already supports note extraction through `CBETA-Translator/Text/TeiRenderer.cs`, and CBETA demonstrates the existing anchored-footnote pattern in `CbetaZenTexts/xml-p5`.

Current supported shapes:

- inline note in the body:
  - `<note place="inline">...</note>`
- anchored end note:
  - body anchor: `<anchor xml:id="nkr_note_mod_0001"/>`
  - note in `<back>`: `<note target="#nkr_note_mod_0001">...</note>`

### Recommendation

Use English editorial notes as footnotes, but do it with a clean OpenZen convention instead of overloading free-text markdown.

#### Phase 1: parser-compatible immediately

Support these note families in OpenZen output:

- `nkr_note_crit_...`
- `nkr_note_prov_...`
- `nkr_note_trans_...`
- `nkr_note_unres_...`

Parser change required:

- extend `InferNoteKindFromId(...)` in `CBETA-Translator/Text/TeiRenderer.cs`
  to recognize those OpenZen note kinds
- preserve backward compatibility with:
  - `nkr_note_mod_`
  - `nkr_note_orig_`
  - `nkr_note_add_`

#### Phase 2: UI grouping

In the edition-process dialog, group note kinds separately:

- `crit`
  editorial / textual decision notes
- `prov`
  provenance or witness-source notes
- `trans`
  translation or reception notes
- `unres`
  unresolved readings or pending questions

### Encoding rule

Use:

```xml
<anchor xml:id="nkr_note_crit_xxm001"/>
```

in the body at the relevant locus, and:

```xml
<back>
  <div type="notes">
    <note xml:lang="en" type="critical" target="#nkr_note_crit_xxm001">
      Base witness reads X; NDL2537799 and WUL-bunko31_e1089 support Y; editor adopts Y because...
    </note>
  </div>
</back>
```

for the note itself.

### When to use footnotes vs apparatus.json

Use footnotes for:

- short English editorial notes a reader can consume inline
- decisive provenance clarifications
- short unresolved warnings

Use `apparatus.json` for:

- full variant tables
- witness-by-witness evidence
- machine-readable statistics
- filtering and aggregation in the UI

The footnote is the reader surface.
The JSON apparatus is the data backbone.

### What footnotes are not for

Do not use TEI footnotes as a second process log.

Do not put into reader-facing notes:

- chronological work history
- download or OCR troubleshooting narrative
- full decision-log argument chains
- generalized methodology explanation not tied to a visible locus
- duplicate prose already carried adequately by `human-log.md`

Those belong instead in:

- `process-log.md` for chronology
- `decision-log.md` for the full reasoning trail
- `human-log.md` for readable narrative history
- `timeline.json` for machine-readable state change history

### Footnote scope rule

A TEI footnote should exist only when all of the following are true:

1. it is tied to a visible text locus or visible note anchor
2. a reader benefits from seeing it from the text itself
3. it is short enough to function as a note rather than a mini-essay

If the content is primarily for editors, auditors, or programmatic processing, keep it out of the footnote layer and in apparatus or logs instead.

### Duplication rule

If a note corresponds to a logged editorial decision:

- the footnote may summarize the reason briefly
- the full reasoning still belongs in `decision-log.md`
- the event still belongs in `timeline.json`
- the structured evidence still belongs in `apparatus.json` when variant-bearing

Do not copy the full argument verbatim across all four surfaces.

## Critical text vs witness comparison vs timeline

Do not collapse these into one feature.

### Critical text

This is the main edited reading text.

It is:

- the primary reader surface
- the place where footnote anchors live
- the place where apparatus-linked loci are highlighted

It is not:

- a raw witness browser
- a timeline replay view

### Witness comparison

This is the place where the reader or editor inspects source witnesses directly.

Preferred UI:

- popup
- side panel
- comparison dialog

It should show the same locus across selected witnesses.

When witness count is large, the default comparison view should:

- show differing witnesses first
- collapse identical witnesses unless expanded
- allow plain-text copy of witness readings
- allow opening the full delivered witness text for a selected siglum

It is not:

- the final critical text itself
- the process log
- the timeline slider

### Timeline

This is the chronological replay of edition construction.

It shows:

- editorial state changes
- `text_changed` events
- witness-set and copy-text state transitions
- unresolved opening/closing

It is not:

- a raw witness comparison surface
- a replacement for apparatus

### Required separation

The system must preserve all three:

1. critical text surface
2. witness comparison surface
3. timeline surface

Witness comparison is necessary, but witness comparison alone is not the critical-edition model.

It must also preserve definitive delivered witness texts as first-class artifacts rather than leaving witness access buried in OCR working directories.

### Converter requirement

The next-generation OpenZen converter should not only emit body TEI.
It should also be able to emit:

- anchors in the body
- `<back>` notes in English
- parallel `apparatus.json`

The current Wumenguan converter is therefore only a minimal precedent, not the target architecture.

Reference:

- TEI critical apparatus guidance:
  https://www.tei-c.org/Vault/P5/2.0.1/doc/tei-p5-doc/es/html/TC.html

## Manifest schema changes required

Add to `MANIFEST_SCHEMA.md`:

- `process_file`
- `apparatus_file`
- `stats_file`
- `base_witness_id`
- `witness_family_count`
- `physical_witness_count`
- `ocr_maximal` boolean
- `editor_intervention_required` boolean
- `editor_intervention_note`
- `edition_maturity`
  - `draft`
  - `review`
  - `publication-candidate`
  - `published`
- `witnesses_file`

For each witness add:

- `family_id`
- `page_count`
- `completeness`
- `validation_method`
- `source_page_snapshot`
- `license_snapshot`

## App UI split

### Sidebar: keep this short

Sidebar should show only:

- work title
- edition kind
- license badge
- commercial-use flag
- no-CBETA flag
- base witness
- witness count
- source links

This keeps the current provenance panel focused.

### New dedicated browser/dialog

Add a new "Edition Process" or "Critical Edition" dialog reachable from the sidebar.

Tabs:

1. `Sources`
   Full witness cards, rights evidence, hashes, completeness

2. `Process`
   Pipeline stages, OCR engines, editor passes, publication checks

3. `Timeline`
   Slider-based chronological replay of edition construction with visible state changes and human-readable explanations

4. `Apparatus`
   Locus-by-locus variants and decisions

5. `Witnesses`
   Open definitive witness texts, compare at locus, copy readings, and expand from differing-only to all witnesses

6. `Stats`
   coverage, unresolved counts, machine/human ratios

7. `Documents`
   markdown logs and notes

The timeline surface must let the reader:

- move event by event
- jump by stage
- filter by actor, witness, or event type
- see what changed at the selected step
- open linked evidence and documents

The witness surface must let the reader:

- open a locus-driven popup or panel from the critical text
- show differing witnesses by default when witness counts are high
- expand to all witnesses
- copy witness readings as plain text
- open the full definitive text for a selected witness

The visible reading text should be able to reflect the selected timeline state when feasible.

## ReadZen implementation requirements

### Data model

Extend:

- `CBETA-Translator/Models/ManifestInfo.cs`

Add models for:

- `ProcessInfo`
- `WitnessFamilyInfo`
- `ApparatusInfo`
- `EditionStatsInfo`
- `DecisionRecordInfo`
- `UnresolvedLocusInfo`

### Services

Add loaders parallel to `ManifestService`:

- `ProcessService`
- `ApparatusService`
- `EditionStatsService`

### UI

Keep:

- `CBETA-Translator/Views/ProvenancePanel.axaml`

But simplify its mission to source and license facts, and add:

- `EditionProcessDialog.axaml`
- `EditionProcessDialog.axaml.cs`

### Discovery rules

Current markdown autodiscovery in `CBETA-Translator/Views/ProvenancePanel.axaml.cs` is useful but too loose.

Replace "scan all `.md` files" with:

- structured known JSON files for data
- a curated markdown registry for human-readable documents

## Publication checklist

A critical edition is not publishable unless:

1. all witness rights are high-confidence or explicitly waived with reason
2. all witness files hash-validate
3. segmentation is complete
4. OCR runs are recorded
5. OCR benchmark exists
6. editor passes are logged with actor identity
7. apparatus exists
8. unresolved loci are classified
9. TEI validates
10. manifest/process/apparatus/stats files all validate

## Final coherence and integrity pass

Before calling any package complete, run one last coherence pass over the whole edition.

This pass must confirm:

- every required JSON file parses cleanly
- every required JSON file validates against its schema where a schema exists
- `documents.json` paths resolve to real files
- manifest-declared files actually exist
- witness ids, sigla, and file references are internally consistent
- TEI note anchors and note targets resolve
- TEI notes, apparatus entries, and timeline events do not contradict one another
- reader-facing footnotes are not being used as a duplicate process journal
- `human-log.md`, `decision-log.md`, and TEI notes each stay in their proper role

This is a mandatory release gate, not a nice-to-have cleanup pass.

## Faith in Mind rollout recommendation

Use `信心銘` as the first text to fully adopt this system because:

- it has multiple witness families
- it has anthology witnesses and commentary witnesses
- it needs stemmatic thinking
- it is smaller than many lamp records
- it will stress-test the difference between:
  - base text
  - translation/reception witnesses
  - commentary control witnesses

## Programmer-agent task list

1. Patch `MANIFEST_SCHEMA.md` to add process/apparatus/stat hooks.
2. Define JSON schemas for `process.json`, `apparatus.json`, `stats.json`.
3. Define the JSON schema for `timeline.json` and the state model it depends on.
4. Define the JSON schema for `witnesses.json` and the definitive witness text delivery contract.
5. Extend `ManifestInfo.cs` and add new typed models.
6. Add new services to load those JSON files.
7. Extend `TeiRenderer.cs` note-kind inference to support OpenZen critical-note families while keeping CBETA compatibility.
8. Keep the current provenance sidebar focused on license/source facts.
9. Build a dedicated edition-process dialog with tabs for sources, process, timeline, apparatus, witnesses, stats, documents, and notes.
10. Add curated document-discovery rules instead of free-for-all markdown scanning.
11. Add validators so a critical edition cannot be published with missing required process artifacts or missing definitive witness delivery artifacts.
12. Migrate `wumenguan-1632` into the new structure as the first exemplar.
13. Then start `信心銘` under the new pipeline instead of the old ad hoc one.

## Immediate cleanup required before migration

Fix stale Wumenguan provenance statements first:

- `OpenZenTexts/provenance/wumenguan-1632/witnesses/wumenguan-1632-ndl-README.md`
- `OpenZenTexts/xml-open/pd/wumenguan-1632/README.md`

Those contradictions should not survive into the new system.
