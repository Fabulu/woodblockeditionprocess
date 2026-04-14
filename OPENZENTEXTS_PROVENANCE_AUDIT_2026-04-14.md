# OpenZenTexts Provenance And Critical-Edition Audit

Date: 2026-04-14
Scope: `OpenZenTexts` and `CBETA-Translator`
Focus: whether the current documentation and provenance model are strong enough for a rigorous scan-first critical edition program, using `信心銘` as the next target and `wumenguan-1632` as the exemplar under review.

## Main conclusions

No. The current documentation is a strong start, but it is not yet rigorous enough for a true OpenZen critical-edition program.

The target standard is:

- OCR should be used as far as possible before editorial intervention
- every editorial decision must be auditable
- every editorial intervention must be attributable to an agent, a human, or a hybrid pass
- provenance must be split cleanly into:
  - licensing / source facts for downstream reuse
  - process / method / apparatus for scholarly inspection
- the UI must expose both of those layers without collapsing them into one sidebar blob

The current system is already good enough for:

- basic source capture
- per-text manifesting
- machine-readable license flags
- lightweight witness display

The current system is not yet good enough for:

- consistency across duplicated provenance docs
- process-level reproducibility
- apparatus structure
- per-decision traceability
- OCR workflow instrumentation
- UI separation of source facts vs editorial method

Therefore the process must be tightened around five non-negotiable rules:

1. One edition, one authoritative process bundle.
2. One source of truth for witness rights and validation state.
3. OCR-first, editor-pass-second, with actor identity recorded.
4. Reader-facing source/licensing separate from scholarly process/apparatus.
5. No publication without structured evidence for coverage, decisions, unresolved loci, and validation.

## Concrete findings

### 1. The Wumenguan provenance is already fragmented and partially contradictory

Current contradictions:

- `OpenZenTexts/xml-open/pd/wumenguan-1632/manifest.json`
  says `NDL2537788` is high-vetting, exact Commons-pinned, fully anchored.
- `OpenZenTexts/provenance/wumenguan-1632/witnesses/wumenguan-1632-ndl-README.md`
  still says the base `NDL12865429` local PDF is "not yet re-downloaded after deletion."
- `OpenZenTexts/xml-open/pd/wumenguan-1632/README.md`
  still says the Huikai-record rights memo is incomplete, which is now stale.

Effect:

- a reader can no longer tell which document is authoritative
- the UI can surface a correct manifest while nearby markdown says the opposite
- a future editor can accidentally regress the source memo because there is no single source of truth

### 2. The current manifest is provenance-capable but not process-capable

`OpenZenTexts/MANIFEST_SCHEMA.md` is good for:

- text identity
- licensing
- witness list
- basic production summary

It is not enough for a critical-edition pipeline because it has no first-class fields for:

- witness families vs physical witnesses
- base witness selection rationale
- OCR engines and versions used
- segmentation method
- page/leaf coverage status
- unresolved loci
- decision log references
- apparatus linkage
- confidence metrics by stage
- editor-intervention accounting

Result:

- `manifest.json` can say a text is a `critical_edition`, but cannot explain how it earned that label in a structured way

### 3. The current process docs are strong narrative guidance but not a locked pipeline contract

Good documents already exist:

- `OpenZenTexts/docs/curation/WORKFLOW.md`
- `OpenZenTexts/docs/curation/REPO_INTAKE_PIPELINE.md`
- `OpenZenTexts/docs/curation/TRANSCRIPTION_METHOD.md`
- `OpenZenTexts/docs/curation/PROCESS_LOG_TEMPLATE.md`

But they still leave major things as conventions rather than enforceable structure:

- no canonical artifact tree for a critical edition
- no required machine-readable per-stage outputs
- no required "decision record" schema
- no required page-to-leaf coverage table
- no required unresolved-locus register
- no required OCR benchmark report
- no required publication checklist for apparatus completeness
- no required actor-attribution field for agent vs human decisions

### 4. The current provenance UI is too flat

Current implementation:

- `CBETA-Translator/Views/ProvenancePanel.axaml`
- `CBETA-Translator/Views/ProvenancePanel.axaml.cs`

What it does well:

- shows edition kind
- shows license flags
- shows witnesses
- shows production method
- shows markdown documents discovered from `provenance/{slug}/`

What it cannot yet do:

- distinguish "license/source facts" from "editorial process"
- show apparatus entries or unresolved loci systematically
- show stats
- show decision records
- show witness-family relationships
- show OCR pipeline evidence
- show coverage progress

The `Documents` section currently just expands arbitrary markdown files. That is flexible, but it is not a system.

### 5. The data model in ReadZen is underspecified for a critical-edition browser

`CBETA-Translator/Models/ManifestInfo.cs` currently loads only a narrow subset of manifest fields.

Missing from the typed model:

- alternate names
- edition notes in a structured way beyond one string
- production inputs dir
- stable revision IDs
- local captured paths / filenames
- rights basis text
- provenance checks
- witness notes

Even before adding new critical-edition fields, the app is not consuming the full current manifest schema.

### 5a. The renderer already supports footnotes, but the supported note model is narrower than the edition program needs

Current parser behavior in `CBETA-Translator/Text/TeiRenderer.cs`:

- supports inline notes: `<note place="inline">`
- supports end notes in `<back>` when they are anchored from the body via:
  - `<anchor xml:id="nkr_note_*">`
  - `<note ... target="#nkr_note_*">`
- infers note kind only from these ID families:
  - `nkr_note_mod_`
  - `nkr_note_orig_`
  - `nkr_note_add_`

CBETA examples confirm the pattern:

- `CbetaZenTexts/xml-p5/B/B06/B06n0007.xml`
- `CbetaZenTexts/xml-p5/B/B26/B26n0147.xml`

This is enough to prove that the app can surface footnote-style annotations today.

It is not yet enough for OpenZen critical editions because we need note kinds like:

- critical decision note
- provenance note
- translation/reception note
- unresolved locus note

So the renderer is footnote-capable, but not yet critical-edition-capable by type system.

### 6. The Wumenguan exemplar is rich, but still spread across too many ad hoc files

The project already has real material:

- diplomatic draft
- reading edition
- verification notes
- source READMEs
- run specs in the app repo

But it is split between:

- `C:\woodblocks`
- `OpenZenTexts/provenance/...`
- `OpenZenTexts/xml-open/...`
- `CBETA-Translator/runs/...`

That makes sense during experimentation, but it is not a stable critical-edition program layout.

### 7. Encoding and rendering are vulnerable to mojibake and stale duplication

Visible issue:

- multiple markdown files render mojibake in terminal and some committed docs still contain damaged display text

This is not just cosmetic. In a critical edition, character integrity and naming consistency are part of provenance.

## What must change now

1. One authoritative machine-readable provenance/process bundle per edition.
2. One canonical source of truth for witness rights and validation status.
3. A separate process/apparatus data layer, not stuffed into free-text notes.
4. A UI split:
   - sidebar = source + rights + short witness list
   - dedicated panel/dialog = process, decisions, apparatus, stats
5. Required structured logs for OCR, adjudication, unresolved loci, and publication checks.

These are not optional improvements. They are the minimum conditions for calling an OpenZen text a rigorous critical edition.

## Standards direction

External standards support this move:

- TEI critical-apparatus guidance already supports lemma / reading / witness modeling:
  https://www.tei-c.org/Vault/P5/2.0.1/doc/tei-p5-doc/es/html/TC.html
- OCR-D gives a strong vocabulary for repeatable OCR workflows and QA:
  https://ocr-d.de/en/spec/intro.html
  https://ocr-d.de/en/spec/ocrd_eval

Those standards should inform the new OpenZen critical-edition layer instead of relying on prose-only local habit.
