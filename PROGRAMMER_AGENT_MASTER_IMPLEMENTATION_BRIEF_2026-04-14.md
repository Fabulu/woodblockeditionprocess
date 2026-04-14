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
- every editorial action records whether it was taken by an agent, a human, or a hybrid pass
- English critical notes are supported in TEI and the app
- provenance sidebar stays concise
- full process/apparatus/stats get their own structured browser
- visible text history uses reverse-patching from final text

## Shared path policy

Shared docs and examples produced under this brief must not use:

- local absolute filesystem paths like `C:\...`
- renderer-only absolute links

Use instead:

- repo-relative paths
- repo-name-relative paths such as `OpenZenTexts/xml-open/pd/wumenguan-1632/manifest.json`
- web URLs for online sources

## Required output modes

The implementation must preserve eight distinct output modes:

1. `Sidebar provenance mode`
   - source, rights, witness summary
   - powered by `manifest.json`
2. `Process mode`
   - workflow history, decision trail, unresolved state
   - powered by `process.json` plus process markdown docs
3. `Apparatus mode`
   - structured variants and editorial reasoning
   - powered by `apparatus.json` plus TEI note/app anchors
4. `Stats mode`
   - compact quantitative summary
   - powered by `stats.json`
5. `Document registry mode`
   - curated supporting docs
   - powered by `documents.json`
6. `Edition text mode`
   - the reading text with notes/anchors
   - powered by `{slug}.xml`
7. `Timeline mode`
   - chronological replay of what changed and why
   - powered by `timeline.json` plus `human-log.md`
8. `Witness comparison mode`
   - direct source-witness inspection at a selected locus
   - powered by witness-text data plus locus/page mapping

Do not collapse these modes into one sidebar, one markdown blob, or one oversized manifest.

Do not collapse reader-facing notes into process history either.

The implementation must preserve this boundary:

- TEI notes are short reader-facing locus notes
- `human-log.md` is chronological narrative
- `decision-log.md` is full reasoning
- `apparatus.json` is structured textual evidence
- `timeline.json` is state-change history
- witness comparison is source inspection, not timeline replay

## Core timeline contract

Implement timeline reconstruction with reverse-patching from the final text.

Expected behavior:

- the final reading text renders normally
- when the slider moves backward, later `text_changed` events are reversed
- each `text_changed` event identifies one TEI locus exactly
- the affected locus highlights and should auto-scroll when feasible
- non-text events update metadata without mutating the visible text

Preferred `timeline.json` storage model:

- top-level `readings` table keyed by `locus_id`
- `reading_before` / `reading_after` indices in events
- append-only `revisions` array

This is the contract future transcription and collation agents must target.

This brief authorizes changes in:

- `OpenZenTexts`
- `CBETA-Translator`

Reference planning docs:

- `OPENZENTEXTS_PROVENANCE_AUDIT_2026-04-14.md`
- `CRITICAL_EDITION_SYSTEM_SPEC_2026-04-14.md`

## Relevant file inventory

The programmer agent should treat these as the primary known file set.

### Planning and orchestration

- `OPENZENTEXTS_PROVENANCE_AUDIT_2026-04-14.md`
- `CRITICAL_EDITION_SYSTEM_SPEC_2026-04-14.md`
- `PROGRAMMER_AGENT_MASTER_IMPLEMENTATION_BRIEF_2026-04-14.md`

### OpenZenTexts repo root and schema

- `OpenZenTexts/README.md`
- `OpenZenTexts/MANIFEST_SCHEMA.md`

### OpenZenTexts curation docs

- `OpenZenTexts/docs/curation/README.md`
- `OpenZenTexts/docs/curation/WORKFLOW.md`
- `OpenZenTexts/docs/curation/REPO_INTAKE_PIPELINE.md`
- `OpenZenTexts/docs/curation/TRANSCRIPTION_METHOD.md`
- `OpenZenTexts/docs/curation/TRANSCRIPTION_CHECKLIST.md`
- `OpenZenTexts/docs/curation/PROCESS_LOG_TEMPLATE.md`

### OpenZenTexts Wumenguan exemplar

- `OpenZenTexts/xml-open/pd/wumenguan-1632/manifest.json`
- `OpenZenTexts/xml-open/pd/wumenguan-1632/README.md`
- `OpenZenTexts/xml-open/pd/wumenguan-1632/wumenguan-1632.xml`
- `OpenZenTexts/provenance/wumenguan-1632/WUMENGUAN_1632_DIPLOMATIC_DRAFT.md`
- `OpenZenTexts/provenance/wumenguan-1632/witnesses/wumenguan-1632-ndl-README.md`
- `OpenZenTexts/provenance/wumenguan-1632/witnesses/wumen-huikai-ndl-README.md`
- `OpenZenTexts/provenance/wumenguan-1632/witnesses/mumonkan-1752-waseda-README.md`

### OpenZenTexts existing converter

- `OpenZenTexts/tools/woodblock-to-tei/convert-wumenguan-1632.mjs`

### ReadZen parser, models, services, UI

- `CBETA-Translator/Text/TeiRenderer.cs`
- `CBETA-Translator/Models/RenderedDocument.cs`
- `CBETA-Translator/Models/ManifestInfo.cs`
- `CBETA-Translator/Services/ManifestService.cs`
- `CBETA-Translator/Views/ProvenancePanel.axaml`
- `CBETA-Translator/Views/ProvenancePanel.axaml.cs`

### ReadZen provenance-browser and Wumenguan run notes

- `CBETA-Translator/runs/CLAUDE-RUNS/RUN-20260412-0942-provenance-browser/SPEC_v1.md`
- `CBETA-Translator/runs/CLAUDE-RUNS/RUN-20260412-0110-wumenguan-1632-openzen-import/SPEC_v1.md`
- `CBETA-Translator/runs/CLAUDE-RUNS/RUN-20260412-0110-wumenguan-1632-openzen-import/DECISIONS.md`

### CBETA reference corpus for note patterns

- `CbetaZenTexts/xml-p5/README.md`
- `CbetaZenTexts/xml-p5/B/B06/B06n0007.xml`
- `CbetaZenTexts/xml-p5/B/B26/B26n0147.xml`

### Working woodblocks-side source docs that matter for current truth

- `Wumen_Huikai_NDL_Commons/README.md`
- `FAITH_IN_MIND_WITNESSES.md`
- `FAITH_IN_MIND_STEMMA.md`

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

- `OpenZenTexts/MANIFEST_SCHEMA.md`
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
   - JSON parse and schema integrity
   - cross-file reference integrity

2. Define "publication-candidate" checks.

3. Fail publication when required edition artifacts are missing.

Deliverables:

- validator scripts or docs-backed validation flow
- explicit final release-pass checklist for coherence and machine usability

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
8. editor-pass records require actor type and actor identifier.

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
