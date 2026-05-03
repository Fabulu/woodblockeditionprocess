# OCR / Critical Edition Text-Production Plan: Faith in Mind

Date: 2026-04-14  
Status: approved planning stage, pre-OCR  
Scope: first production pass for the critical edition, starting from `T1`

## Purpose

This plan defines the first text-production stage for the Faith in Mind critical edition.

The goal of this stage is not to finish the edition, and it is not to produce a standalone transcription project.

The goal is to produce a clean, reviewable first working text spine for the critical edition from `T1`, document every intervention, and set clear rules for when comparison witnesses enter the workflow and when the starting spine may be revised.

## Continuation law

Outside long OCR loops, the same no-useless-stop rule still applies.

Before stopping a manual correction or comparison run, open `process/CONTINUATION_GATE.md`.

If the current run is still incomplete, the next bounded slice is already available, the package still validates, and no real blocker or judgment call has appeared, you must continue instead of stopping.

Page turns, neat sub-slice boundaries, and the urge to summarize are not valid stopping reasons.

## Locked starting assumptions

- `T1` is the locked starting copy-text spine.
- The first comparison controls are:
  - `T4`
  - `T5`
  - `T2`
- `T3`, `A3`, `A2`, and `A1` remain queued for the second comparison pass.
- Commentary, translation, study, and source-tradition witnesses do not control the first transcription pass.

## Copy-text law

`T1` is locked as the starting copy-text for the edition.

This lock is not absolute. It may be revised only if a later comparison stage produces evidence that `T1` is materially inferior as the edition spine.

A copy-text switch is allowed only if all of the following are true:

1. the triggering evidence is identified at specific loci
2. the competing witness has been directly compared at those loci
3. the reason for switching is written as a decision record
4. the timeline records the switch as a state-changing event
5. the previous state remains reconstructable

Allowed reasons include:

- systematic damage or omission in `T1`
- repeated evidence that a different witness preserves a superior base layer
- proven extraction or boundary problems that make `T1` unsuitable as the main spine

Not allowed:

- switching because another witness merely looks cleaner
- switching without a written evidence trail
- silent replacement of the working base

## Production principle

Use as much OCR reliance as possible before manual intervention.

Manual reading is allowed only after:

1. a direct OCR attempt exists
2. OCR failure or ambiguity is logged
3. the unresolved locus is narrowed to a specific page, line, or glyph problem

## Stage breakdown

### Stage 2A. Page preparation

For `T1`:

1. confirm canonical source file, hash, size, and page count
2. create stable page-image derivatives if needed for OCR
3. assign page identifiers that stay stable through the whole edition
4. log every generated derivative and tool used

Required outputs:

- page image set or equivalent OCR-ready derivative set
- page inventory table
- derivative-generation log entry

### Stage 2B. OCR pass 1

Run the first OCR pass against the full `T1` witness.

For this edition, the required comparator loop is:

- `tesseract`
- `RapidOCR`
- `PaddleOCR`
- `EasyOCR`

This four-engine loop is mandatory for East Asian scan witnesses in this edition workflow.

At minimum, before manual correction begins, all four engines must be handled in one of these two ways:

1. run on the same calibration slice and preserve the outputs for comparison
2. if an engine is blocked, record the exact runtime failure and keep the blocker open explicitly

Do not silently shrink the OCR basis.
Do not describe the OCR stage as complete if the four-engine comparison requirement has not been satisfied or formally blocked.

Requirements:

- record OCR engine, model, version, language data, and settings
- preserve raw OCR output
- preserve page-level OCR outputs if the tool supports them
- preserve a same-page comparison set across all four engines where possible
- log failed pages separately from successful pages
- log cross-engine disagreement and cross-engine recovery where one engine fills a gap another missed

### Long-run OCR resume law

For long resumable OCR witnesses on this machine, shell timeout is not an accepted stopping point by itself.

If a pass has already demonstrated all of the following:

1. page-level outputs are being saved cleanly
2. the witness-local summary is updating or is easily reconcilable from saved sidecars
3. no new engine-level failure has appeared beyond known timeout or warning behavior

then the required behavior is:

1. inspect the saved extent
2. reconcile logs and summaries honestly
3. validate package state if state files changed
4. relaunch the same witness-local OCR runner immediately

Before stopping, yielding, or writing a status message in this loop, open:

- `provenance/faith-in-mind/process/OCR_STOP_GATE.md`

Do not stop merely because one shell window ended.
Do not treat a timeout-safe checkpoint as a natural session boundary.
Do not yield control back to the human operator after a healthy checkpoint if the pass is still incomplete.
Do not treat successful validation as a stopping point; validation is part of the internal resume loop.
Do not interrupt the human operator with repetitive progress messages during this loop.
Do not stop the loop to explain, summarize, or reassure while the OCR pass is still healthy and incomplete.

Interrupt only if one of the following becomes true:

- the witness reaches genuine four-engine OCR completion
- a new engine error appears that is not the already known timeout or warning pattern
- package validation fails
- saved files and saved summaries diverge in a way that is not safely reconcilable
- a human operator explicitly redirects the work
- clarification is genuinely required to avoid a risky or irreversible mistake

Required outputs:

- raw OCR corpus
- page-level OCR status table
- OCR run log

### Stage 2C. Normalization pass

Normalize OCR output only for structural handling, not silent editorial cleanup.

Normalization may begin from the healthiest available full-pass engine, but this does not waive the mandatory four-engine comparison requirement.

Before Stage 2D manual correction is treated as valid, the edition must have either:

- four-engine calibration comparisons in hand
- or an explicit logged blocker for each missing engine result

Allowed normalization:

- line-break handling needed to reconstruct running text
- consistent whitespace cleanup
- page-break markers
- stable locus IDs

Not allowed in this pass:

- silent character replacement
- silent modernization
- silent punctuation repair
- unlogged guesswork

Required outputs:

- normalized working text
- normalization rule log

### Stage 2D. Manual correction pass 1

Do the first manual correction pass on `T1`.

Rules:

- every meaningful correction must be attributable
- every substantial correction batch must declare a bounded work slice before edits begin
- correction entries must distinguish:
  - OCR certainty fix
  - ambiguous reading
  - damaged graph
  - supplied punctuation
  - unresolved locus
- if a reading cannot be secured from `T1`, mark unresolved instead of smoothing it over
- if visible text changes in a later batch, create a fresh `text_changed` timeline event for that batch rather than expanding the details of an older correction-start event

Required outputs:

- corrected `T1` working text
- correction log
- unresolved locus register

### Stage 2E. Comparison pass 1

Bring in `T4`, `T5`, and `T2` only after the first corrected `T1` working text exists.

Use them to:

- confirm obvious OCR ambiguities
- identify omissions, duplicated lines, or broken boundaries
- detect clear branch-level differences

Do not yet:

- rewrite the text into a synthetic eclectic edition
- let commentary witnesses override the core witnesses

Required outputs:

- first comparison table
- loci requiring second-pass witness review
- apparatus seed entries

### Stage 2F. Review gate

At the end of the first pass, decide whether the edition can move to second-pass collation or whether the starting copy-text lock must be challenged.

The gate is passed only if:

- `T1` has a full OCR-derived working text
- all unresolved loci are explicitly listed
- first-pass comparison against `T4`, `T5`, and `T2` is logged
- no silent edits remain in the working file

## Logging law for this stage

Every step must generate chronological records in both human-readable and machine-readable form.

Minimum required records:

- process log entries
- decision log entries where a judgment call is made
- timeline events
- document registry entries for all new artifacts

For each bounded text-work slice, close out all of:

- active correction-log coverage
- `current-state.md`
- `timeline.json`

If the state changes, the change must be visible chronologically.

That includes:

- copy-text lock
- copy-text challenge
- copy-text switch
- new unresolved loci
- resolved unresolved loci
- comparison witness entry
- apparatus-seed creation

Nothing in this stage may happen silently.
Nothing in this stage may remain chronologically ambiguous.

## Artifact law for this stage

This stage must produce, at minimum:

- `transcription/raw-ocr/`
- `transcription/normalized/`
- `transcription/corrected/`
- `transcription/unresolved-loci.md`
- `edition/working-critical-text.md`
- `collation/first-pass-variant-table.md`
- `process/ocr-run-log.md`
- `process/correction-log.md`

If the implementation uses JSON companions, they must be registered in `documents.json`.

## Success criteria

This stage is successful when:

- the edition has a usable `T1` working text spine derived from OCR
- the four-engine OCR comparison requirement has been satisfied or formally blocked with explicit machine/runtime records
- the first-pass control witnesses have been consulted
- unresolved places are explicit
- every change is attributable to an actor and a stage
- the package is ready for second-pass collation rather than guesswork

## Failure conditions

This stage is not complete if:

- OCR output exists but is not preserved
- the four-engine OCR loop was silently reduced
- manual fixes were made without logging
- comparison witnesses were used before a `T1` spine existed
- unresolved readings were silently normalized away
- a copy-text switch occurred without a formal decision record and timeline event
- any output artifact exists outside the registered package structure
