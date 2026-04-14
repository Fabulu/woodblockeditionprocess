# Programmer Agent Master Implementation Brief

Date: 2026-04-14
Primary objective: turn OpenZenTexts and ReadZen into a real critical-edition platform, not just a text-and-provenance bundle
Primary pilot text: `信心銘`
Migration exemplar: `wumenguan-1632`

## Mission

Build the next OpenZen edition system so that:

- source attribution is authoritative
- OCR-first workflow is enforced
- editorial decisions are machine-readable and human-readable
- English critical notes are supported in TEI and the app
- provenance sidebar stays concise
- full process/apparatus/stats get their own structured browser

This brief authorizes changes in:

- `C:\Programmieren\OpenZenTexts`
- `C:\programmieren\MergeWorkCbeta\CBETA-Translator`

Reference planning docs:

- [OPENZENTEXTS_PROVENANCE_AUDIT_2026-04-14.md](/abs/path/C:/woodblocks/OPENZENTEXTS_PROVENANCE_AUDIT_2026-04-14.md:1)
- [CRITICAL_EDITION_SYSTEM_SPEC_2026-04-14.md](/abs/path/C:/woodblocks/CRITICAL_EDITION_SYSTEM_SPEC_2026-04-14.md:1)

## Relevant file inventory

The programmer agent should treat these as the primary known file set.

### Planning and orchestration

- [OPENZENTEXTS_PROVENANCE_AUDIT_2026-04-14.md](/abs/path/C:/woodblocks/OPENZENTEXTS_PROVENANCE_AUDIT_2026-04-14.md:1)
- [CRITICAL_EDITION_SYSTEM_SPEC_2026-04-14.md](/abs/path/C:/woodblocks/CRITICAL_EDITION_SYSTEM_SPEC_2026-04-14.md:1)
- [PROGRAMMER_AGENT_MASTER_IMPLEMENTATION_BRIEF_2026-04-14.md](/abs/path/C:/woodblocks/PROGRAMMER_AGENT_MASTER_IMPLEMENTATION_BRIEF_2026-04-14.md:1)

### OpenZenTexts repo root and schema

- [README.md](/abs/path/C:/Programmieren/OpenZenTexts/README.md:1)
- [MANIFEST_SCHEMA.md](/abs/path/C:/Programmieren/OpenZenTexts/MANIFEST_SCHEMA.md:1)

### OpenZenTexts curation docs

- [docs/curation/README.md](/abs/path/C:/Programmieren/OpenZenTexts/docs/curation/README.md:1)
- [docs/curation/WORKFLOW.md](/abs/path/C:/Programmieren/OpenZenTexts/docs/curation/WORKFLOW.md:1)
- [docs/curation/REPO_INTAKE_PIPELINE.md](/abs/path/C:/Programmieren/OpenZenTexts/docs/curation/REPO_INTAKE_PIPELINE.md:1)
- [docs/curation/TRANSCRIPTION_METHOD.md](/abs/path/C:/Programmieren/OpenZenTexts/docs/curation/TRANSCRIPTION_METHOD.md:1)
- [docs/curation/TRANSCRIPTION_CHECKLIST.md](/abs/path/C:/Programmieren/OpenZenTexts/docs/curation/TRANSCRIPTION_CHECKLIST.md:1)
- [docs/curation/PROCESS_LOG_TEMPLATE.md](/abs/path/C:/Programmieren/OpenZenTexts/docs/curation/PROCESS_LOG_TEMPLATE.md:1)

### OpenZenTexts Wumenguan exemplar

- [xml-open/pd/wumenguan-1632/manifest.json](/abs/path/C:/Programmieren/OpenZenTexts/xml-open/pd/wumenguan-1632/manifest.json:1)
- [xml-open/pd/wumenguan-1632/README.md](/abs/path/C:/Programmieren/OpenZenTexts/xml-open/pd/wumenguan-1632/README.md:1)
- [xml-open/pd/wumenguan-1632/wumenguan-1632.xml](/abs/path/C:/Programmieren/OpenZenTexts/xml-open/pd/wumenguan-1632/wumenguan-1632.xml:1)
- [provenance/wumenguan-1632/WUMENGUAN_1632_DIPLOMATIC_DRAFT.md](/abs/path/C:/Programmieren/OpenZenTexts/provenance/wumenguan-1632/WUMENGUAN_1632_DIPLOMATIC_DRAFT.md:1)
- [provenance/wumenguan-1632/witnesses/wumenguan-1632-ndl-README.md](/abs/path/C:/Programmieren/OpenZenTexts/provenance/wumenguan-1632/witnesses/wumenguan-1632-ndl-README.md:1)
- [provenance/wumenguan-1632/witnesses/wumen-huikai-ndl-README.md](/abs/path/C:/Programmieren/OpenZenTexts/provenance/wumenguan-1632/witnesses/wumen-huikai-ndl-README.md:1)
- [provenance/wumenguan-1632/witnesses/mumonkan-1752-waseda-README.md](/abs/path/C:/Programmieren/OpenZenTexts/provenance/wumenguan-1632/witnesses/mumonkan-1752-waseda-README.md:1)

### OpenZenTexts existing converter

- [tools/woodblock-to-tei/convert-wumenguan-1632.mjs](/abs/path/C:/Programmieren/OpenZenTexts/tools/woodblock-to-tei/convert-wumenguan-1632.mjs:1)

### ReadZen parser, models, services, UI

- [Text/TeiRenderer.cs](/abs/path/C:/programmieren/MergeWorkCbeta/CBETA-Translator/Text/TeiRenderer.cs:1)
- [Models/RenderedDocument.cs](/abs/path/C:/programmieren/MergeWorkCbeta/CBETA-Translator/Models/RenderedDocument.cs:1)
- [Models/ManifestInfo.cs](/abs/path/C:/programmieren/MergeWorkCbeta/CBETA-Translator/Models/ManifestInfo.cs:1)
- [Services/ManifestService.cs](/abs/path/C:/programmieren/MergeWorkCbeta/CBETA-Translator/Services/ManifestService.cs:1)
- [Views/ProvenancePanel.axaml](/abs/path/C:/programmieren/MergeWorkCbeta/CBETA-Translator/Views/ProvenancePanel.axaml:1)
- [Views/ProvenancePanel.axaml.cs](/abs/path/C:/programmieren/MergeWorkCbeta/CBETA-Translator/Views/ProvenancePanel.axaml.cs:1)

### ReadZen provenance-browser and Wumenguan run notes

- [runs/CLAUDE-RUNS/RUN-20260412-0942-provenance-browser/SPEC_v1.md](/abs/path/C:/programmieren/MergeWorkCbeta/CBETA-Translator/runs/CLAUDE-RUNS/RUN-20260412-0942-provenance-browser/SPEC_v1.md:1)
- [runs/CLAUDE-RUNS/RUN-20260412-0110-wumenguan-1632-openzen-import/SPEC_v1.md](/abs/path/C:/programmieren/MergeWorkCbeta/CBETA-Translator/runs/CLAUDE-RUNS/RUN-20260412-0110-wumenguan-1632-openzen-import/SPEC_v1.md:1)
- [runs/CLAUDE-RUNS/RUN-20260412-0110-wumenguan-1632-openzen-import/DECISIONS.md](/abs/path/C:/programmieren/MergeWorkCbeta/CBETA-Translator/runs/CLAUDE-RUNS/RUN-20260412-0110-wumenguan-1632-openzen-import/DECISIONS.md:1)

### CBETA reference corpus for note patterns

- [xml-p5/README.md](/abs/path/C:/Programmieren/CbetaZenTexts/xml-p5/README.md:1)
- [xml-p5/B/B06/B06n0007.xml](/abs/path/C:/Programmieren/CbetaZenTexts/xml-p5/B/B06/B06n0007.xml:3277)
- [xml-p5/B/B26/B26n0147.xml](/abs/path/C:/Programmieren/CbetaZenTexts/xml-p5/B/B26/B26n0147.xml:7711)

### Working woodblocks-side source docs that matter for current truth

- [Wumen_Huikai_NDL_Commons/README.md](/abs/path/C:/woodblocks/Wumen_Huikai_NDL_Commons/README.md:1)
- [FAITH_IN_MIND_WITNESSES.md](/abs/path/C:/woodblocks/FAITH_IN_MIND_WITNESSES.md:1)
- [FAITH_IN_MIND_STEMMA.md](/abs/path/C:/woodblocks/FAITH_IN_MIND_STEMMA.md:1)

## Program structure

Run this as a staged multi-agent program with explicit role separation.

Required roles:

1. `Opus Master Architect`
   Owns scope, task decomposition, standards decisions, merge policy

2. `Recon Agent(s)`
   Read code, schemas, TEI patterns, existing provenance structures, and standards

3. `Implementer Agent(s)`
   Make bounded code or schema changes in parallel where write scopes do not overlap

4. `Review Agent`
   Performs a code-review pass with findings-first mindset

5. `QA Agent`
   Runs manual and automated validation against real example texts

6. `Test Writer Agent`
   Adds or tightens automated tests for parser, manifests, JSON schemas, and UI data loading

## Operating rules

### Rule 1: master architect owns the plan

The master architect must:

- read both planning docs first
- produce the canonical task graph
- assign ownership of files or modules
- define wave boundaries
- maintain an implementation ledger

No implementer should independently redesign the architecture.

### Rule 2: recon before code

Before any implementation wave, recon agents must confirm:

- what OpenZen currently stores
- what ReadZen currently parses
- what CBETA note patterns already work
- where current Wumenguan docs are stale

### Rule 3: parallel only on disjoint write scopes

Parallel implementation is encouraged only when files do not overlap.

### Rule 4: exemplar-first rollout

Do not start by trying to solve all texts.

Use this order:

1. `wumenguan-1632` migration and cleanup
2. platform features
3. `信心銘` pipeline bootstrap

## Wave plan

## Wave 0. Recon and architecture lock

Owner: `Opus Master Architect`
Support: `Recon Agent(s)`

Tasks:

1. Read:
   - `OpenZenTexts/MANIFEST_SCHEMA.md`
   - `OpenZenTexts/docs/curation/*`
   - `OpenZenTexts/xml-open/pd/wumenguan-1632/*`
   - `OpenZenTexts/provenance/wumenguan-1632/*`
   - `CBETA-Translator/Text/TeiRenderer.cs`
   - `CBETA-Translator/Views/ProvenancePanel.*`
   - `CBETA-Translator/Models/ManifestInfo.cs`
   - `CBETA-Translator/Services/ManifestService.cs`
   - representative CBETA `xml-p5` files with note anchors

2. Confirm parser behavior for:
   - inline notes
   - `<back>` notes
   - anchored notes
   - unsupported note kinds

3. Produce a short architecture memo:
   - accepted JSON artifacts
   - note-kind strategy
   - UI split
   - migration order

Deliverable:

- `RUN-.../MASTER_ARCHITECT_SPEC.md`

## Wave 1. Schema and data-contract wave

Owner: `Implementer A`
Review by: `Review Agent`

Write scope:

- `C:\Programmieren\OpenZenTexts\MANIFEST_SCHEMA.md`
- new schema docs in `OpenZenTexts/docs/curation/`

Tasks:

1. Extend manifest spec with:
   - `process_file`
   - `apparatus_file`
   - `stats_file`
   - `base_witness_id`
   - witness family metadata
   - edition maturity fields

2. Define new document contracts:
   - `process.json`
   - `apparatus.json`
   - `stats.json`

3. Add a new curation doc:
   - `CRITICAL_EDITION_WORKFLOW.md`

4. Add a curated document registry spec for per-text docs.

Deliverables:

- updated `MANIFEST_SCHEMA.md`
- new schema docs
- new workflow doc

## Wave 2. Parser and model wave

Owner: `Implementer B`
Parallel-safe with Wave 1 after architecture lock

Write scope:

- `CBETA-Translator/Models/*`
- `CBETA-Translator/Services/*`
- `CBETA-Translator/Text/TeiRenderer.cs`

Tasks:

1. Extend `ManifestInfo` to consume more of the current schema.
2. Add models:
   - `ProcessInfo`
   - `ApparatusInfo`
   - `EditionStatsInfo`
   - `WitnessFamilyInfo`
   - `DecisionRecordInfo`
   - `UnresolvedLocusInfo`
3. Add services:
   - `ProcessService`
   - `ApparatusService`
   - `EditionStatsService`
4. Extend `TeiRenderer` note-kind inference to support:
   - `nkr_note_crit_`
   - `nkr_note_prov_`
   - `nkr_note_trans_`
   - `nkr_note_unres_`
5. Preserve compatibility with:
   - `nkr_note_mod_`
   - `nkr_note_orig_`
   - `nkr_note_add_`

Deliverables:

- typed models
- JSON-loading services
- note-kind parser changes

## Wave 3. Provenance UI split wave

Owner: `Implementer C`

Write scope:

- `CBETA-Translator/Views/ProvenancePanel.*`
- new dialog/view files
- related viewmodels if needed

Tasks:

1. Simplify `ProvenancePanel` to show only:
   - title
   - edition kind
   - license flags
   - no-CBETA badge
   - base witness
   - witness count
   - source links

2. Add a new dialog:
   - `EditionProcessDialog`

3. Tabs:
   - `Sources`
   - `Process`
   - `Apparatus`
   - `Stats`
   - `Documents`

4. Replace broad markdown autodiscovery with:
   - curated registry
   - explicit JSON-backed panels

Deliverables:

- slimmer sidebar
- process/apparatus dialog

## Wave 4. Validation and publishing wave

Owner: `Implementer D`

Write scope:

- OpenZen validation tooling
- app-side validation hooks if needed

Tasks:

1. Add validators for:
   - manifest completeness
   - process/apparatus/stats existence
   - witness hash fields
   - note-kind validity
   - document registry validity

2. Define "publication-candidate" checks.

3. Fail publication when required edition artifacts are missing.

Deliverables:

- validator scripts or docs-backed validation flow

## Wave 5. Wumenguan migration and cleanup wave

Owner: `Implementer E`

Write scope:

- `OpenZenTexts/provenance/wumenguan-1632/*`
- `OpenZenTexts/xml-open/pd/wumenguan-1632/*`

Tasks:

1. Fix stale docs:
   - `wumenguan-1632-ndl-README.md`
   - `xml-open/pd/wumenguan-1632/README.md`

2. Add new edition artifacts for Wumenguan:
   - `process.json`
   - `apparatus.json`
   - `stats.json`
   - curated doc registry

3. Reconcile manifest, README, provenance docs, and app expectations.

4. If possible, emit a small sample of English critical notes using the new note-kind path.

Deliverables:

- Wumenguan becomes the first migrated exemplar

## Wave 6. Faith in Mind bootstrap wave

Owner: `Opus Master Architect` plus dedicated implementer(s)

This wave is planning and scaffolding only unless explicitly authorized to produce the edition.

Tasks:

1. Create the canonical `信心銘` directory tree in OpenZen.
2. Register all current witnesses and families.
3. Define:
   - base witness candidates
   - commentary control witnesses
   - translation/reception witnesses
4. Prepare the OCR/process/artifact skeleton.

Deliverables:

- edition skeleton only
- no final edition publication unless separately authorized

## Recon requirements

Recons should be sent whenever an agent needs to answer one of these:

- how is a given TEI feature currently parsed
- where does current provenance contradict itself
- which JSON artifacts are already expected by the app
- which CBETA note patterns are worth mirroring
- which Wumenguan docs are stale

Recon outputs must be short and file-linked.

## Agent orchestration

## Master architect workflow

1. Read the planning docs.
2. Produce the task graph.
3. Identify parallel-safe write scopes.
4. Launch recon agents for unknowns.
5. Launch implementers in wave order.
6. Merge outputs into one coherent plan.
7. Hand completed wave to review.
8. Hand reviewed wave to QA.
9. Hand stable behavior to test writer.

## Implementer workflow

Each implementer must:

- own a disjoint write scope
- not revert other agents’ changes
- document files changed
- report blockers early

## Review workflow

The review agent must:

- inspect code changes findings-first
- focus on regressions, schema mismatch, stale docs, parser/UI mismatch
- confirm the implementation still respects the planning docs

## QA workflow

The QA agent must validate on real texts, not toy data.

Required QA targets:

1. `OpenZenTexts/xml-open/pd/wumenguan-1632/wumenguan-1632.xml`
2. at least one CBETA note-heavy text from `CbetaZenTexts/xml-p5`
3. one OpenZen text without process JSON, to confirm graceful fallback

QA checklist:

- provenance sidebar still works
- notes still render
- new note kinds render
- process dialog opens
- missing JSON fails gracefully
- stale Wumenguan contradictions are eliminated

## Test writer workflow

The test writer agent comes after QA has validated expected behavior.

Required tests:

1. `TeiRenderer` recognizes OpenZen note kinds.
2. anchored notes in `<back>` attach correctly.
3. inline notes still work.
4. unknown note kinds fail safely.
5. manifest/process/apparatus/stats loading works.
6. missing files produce graceful UI fallbacks.
7. validator rejects incomplete critical-edition packages.

## Deliverables checklist

The program is complete only when all of these exist:

- updated schema docs
- updated parser and models
- new edition-process dialog
- validation tooling or documented validation path
- migrated Wumenguan exemplar
- `信心銘` scaffolding under the new system
- tests covering note parsing and new data contracts

## Implementation order summary

1. Recon and architecture lock
2. Schema/data contracts
3. Parser/models/services
4. UI split
5. Validation
6. Wumenguan migration
7. Faith in Mind scaffold
8. Review
9. QA
10. Tests

## Hard constraints

- Do not treat the old Wumenguan converter as normative architecture.
- Do not keep contradictory provenance statements alive.
- Do not hide process facts only in markdown if the app needs them structurally.
- Do not ship a "critical edition" without apparatus/process/stats artifacts.
- Do not conflate source-rights display with editorial-process display.

## End state

When this program is done, OpenZen should support:

- simple free texts
- scan-based reading editions
- real critical editions with English footnotes
- structured provenance
- structured apparatus
- structured process history

That is the platform `信心銘` should be built on.
