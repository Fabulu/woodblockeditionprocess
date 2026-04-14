# OpenZen Critical Edition System Spec

Date: 2026-04-14
Audience: programmer agent, curator, future editorial agents
Purpose: define a repeatable, scan-first, OCR-maximal workflow for rigorous OpenZen critical editions, starting with `信心銘`.

## Goals

Build a system where:

- source rights and witness provenance are locked down
- OCR is pushed as far as possible before human reading
- every human intervention is logged
- every decision is traceable
- every published edition has a coherent artifact tree
- the app can display:
  - quick licensing and source facts in the sidebar
  - full process, apparatus, and stats in a dedicated browser

## Non-goals

- no OCR or edition production in this planning pass
- no TEI body editing in this planning pass
- no UI implementation in this planning pass

## High-level architecture

Separate the edition into four layers:

1. `acquisition`
   Raw witness capture, rights evidence, hashes, file validation

2. `transcription`
   OCR outputs, page segmentation, human adjudication work products

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
  apparatus.json
  stats.json
  README.md
```

## Canonical roles of the files

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
- `human_passes`
- `decision_records`
- `coverage`
- `unresolved_loci`
- `publication_checks`
- `derived_artifacts`

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

### `stats.json`

This is the compact derived summary for the app.

Required fields:

- witness counts
- page / leaf counts
- OCR engine counts
- percent of loci machine-resolved
- percent requiring human intervention
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

Required recording:

- engine name
- version
- model name
- parameters
- run date
- input images
- output files

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

This stage decides:

- which engine becomes default
- which engine is comparator only

### Stage 5. Human adjudication

Humans only step in after OCR outputs exist.

Every human pass must record:

- witness
- pages or loci touched
- reason for intervention
- whether the change was:
  - OCR-confirm
  - OCR-reject
  - image-only recovery
  - cross-witness decision

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

The app already supports note extraction through [Text/TeiRenderer.cs](/abs/path/C:/programmieren/MergeWorkCbeta/CBETA-Translator/Text/TeiRenderer.cs:1), and CBETA demonstrates the existing anchored-footnote pattern in `xml-p5`.

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

- extend `InferNoteKindFromId(...)` in [Text/TeiRenderer.cs](/abs/path/C:/programmieren/MergeWorkCbeta/CBETA-Translator/Text/TeiRenderer.cs:1)
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
- `human_intervention_required` boolean
- `human_intervention_note`
- `edition_maturity`
  - `draft`
  - `review`
  - `publication-candidate`
  - `published`

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
   Pipeline stages, OCR engines, human passes, publication checks

3. `Apparatus`
   Locus-by-locus variants and decisions

4. `Stats`
   coverage, unresolved counts, machine/human ratios

5. `Documents`
   markdown logs and notes

## ReadZen implementation requirements

### Data model

Extend:

- [Models/ManifestInfo.cs](/abs/path/C:/programmieren/MergeWorkCbeta/CBETA-Translator/Models/ManifestInfo.cs:1)

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

- [Views/ProvenancePanel.axaml](/abs/path/C:/programmieren/MergeWorkCbeta/CBETA-Translator/Views/ProvenancePanel.axaml:1)

But simplify its mission to source and license facts, and add:

- `EditionProcessDialog.axaml`
- `EditionProcessDialog.axaml.cs`

### Discovery rules

Current markdown autodiscovery in [Views/ProvenancePanel.axaml.cs](/abs/path/C:/programmieren/MergeWorkCbeta/CBETA-Translator/Views/ProvenancePanel.axaml.cs:1) is useful but too loose.

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
6. human passes are logged
7. apparatus exists
8. unresolved loci are classified
9. TEI validates
10. manifest/process/apparatus/stats files all validate

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
3. Extend `ManifestInfo.cs` and add new typed models.
4. Add new services to load those JSON files.
5. Extend `TeiRenderer.cs` note-kind inference to support OpenZen critical-note families while keeping CBETA compatibility.
6. Keep the current provenance sidebar focused on license/source facts.
7. Build a dedicated edition-process dialog with tabs for sources, process, apparatus, stats, documents, and notes.
8. Add curated document-discovery rules instead of free-for-all markdown scanning.
9. Add validators so a critical edition cannot be published with missing required process artifacts.
10. Migrate `wumenguan-1632` into the new structure as the first exemplar.
11. Then start `信心銘` under the new pipeline instead of the old ad hoc one.

## Immediate cleanup required before migration

Fix stale Wumenguan provenance statements first:

- [provenance/wumenguan-1632/witnesses/wumenguan-1632-ndl-README.md](/abs/path/C:/Programmieren/OpenZenTexts/provenance/wumenguan-1632/witnesses/wumenguan-1632-ndl-README.md:1)
- [xml-open/pd/wumenguan-1632/README.md](/abs/path/C:/Programmieren/OpenZenTexts/xml-open/pd/wumenguan-1632/README.md:1)

Those contradictions should not survive into the new system.
