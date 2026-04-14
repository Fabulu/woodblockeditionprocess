# Critical Edition Recording Matrix

Date: 2026-04-14
Status: binding workflow law
Purpose: define exactly what gets recorded where, and when, during a critical-edition build.

## Core rule

Do not let one file try to do every job.

Use the right file for the right layer:

- prose step log
- machine-readable event stream
- human-readable narrative
- explicit editorial decision
- apparatus data
- witness metadata

If a fact matters to the reader-facing timeline, it must not live only in markdown.

If a fact matters to a human reviewer, it must not live only in JSON.

## File responsibilities

### `process-log.md`

Use for the operational chronology.

Record here:

- recon and search actions
- source pages checked
- downloads and redownloads
- hash and validation steps
- OCR runs
- OCR failures
- segmentation steps
- failed or abandoned paths
- which stage is next

Do not rely on this file alone for visible text changes.

### `decision-log.md`

Use for non-trivial judgments.

Record here:

- copy-text choice
- copy-text challenge or switch
- witness promotion or demotion
- editorial reading choices
- normalization policy choices
- structural ordering decisions
- reversibility and rationale

If a judgment changes visible text, it also requires a `text_changed` event in `timeline.json`.

### `human-log.md`

Use for readable narrative explanation.

Record here:

- what happened
- why it happened
- what changed
- what remained unresolved

This is the reader-facing prose log, not the machine contract.

### `timeline.json`

Use for ordered machine-readable events and state reconstruction.

Record here:

- every state-changing event
- all text changes
- copy-text lock / challenge / switch
- witness-set lock
- OCR start / finish / failure
- unresolved opening / closing

Preferred text-change model:

- top-level per-locus `readings` table
- `reading_before` / `reading_after` indices in each `text_changed` event

Fallback only if needed:

- `previous_reading`
- `new_reading`

### `apparatus.json`

Use for structured variant and decision data.

Record here:

- locus-level readings
- witness support
- chosen lemma
- decision basis
- apparatus status

Do not use this as the only place that a visible text change is recorded.

### `documents.json`

Use for curated document registration.

Register here:

- `process-log.md`
- `decision-log.md`
- `human-log.md`
- `edition-plan.md`
- `copy-text-ranking.md`
- `family-stemma.md`
- other approved supporting docs

Do not rely on markdown autodiscovery.

### Witness `README.md`

Use for source and rights facts.

Record here:

- source page
- best download link
- rights basis
- local file name
- size
- hash
- validation status

### `acquisition-metadata.md`

Use for normalized witness facts across the edition set.

Record here:

- siglum
- source page
- download path
- rights basis
- size
- hash
- page count
- validation status

## Recording triggers

### When a search or recon happens

Write to:

- `process-log.md`

If it changes state:

- also `timeline.json`

### When a witness is accepted, rejected, or re-tiered

Write to:

- `process-log.md`
- `decision-log.md` if judgment is involved
- `timeline.json`

### When a download happens

Write to:

- witness `README.md`
- `acquisition-metadata.md` when normalized
- `process-log.md`

If it changes witness status:

- also `timeline.json`

### When OCR runs

Write to:

- `process-log.md`
- OCR-specific run log
- `timeline.json`

### When a visible reading changes

Always write to:

- `timeline.json` as `text_changed`

Also write to:

- `decision-log.md` if the change is editorially non-trivial
- `human-log.md` if the change matters to reader-facing explanation
- `apparatus.json` if it affects the structured apparatus
- TEI note layer if a visible footnote is warranted

### When a locus remains unresolved

Write to:

- `unresolved-loci.md`
- `timeline.json`

### When a revision is published or extended

Write to:

- `timeline.json` revision metadata
- `human-log.md`
- `process.json`

## Text-change law

For every visible text change, record:

- exact `locus_id`
- `change_kind`
- `reason`
- `witness_support`
- `note_anchor_id` if present

Preferred state capture:

- `reading_before`
- `reading_after`
- backed by a per-locus readings table

Fallback only if needed:

- `previous_reading`
- `new_reading`

Capture the earlier state at the moment of change, before overwrite.

One changed locus at one moment equals one `text_changed` event.

If the same locus changes twice, record two events.

## Reverse-patching law

The visible timeline should reconstruct earlier text states by reverse-patching from the final reading text.

That means:

- later `text_changed` events are reversed when scrubbing backward
- non-text events do not mutate the visible text
- notes and apparatus should only appear once their originating events have happened

Full historical snapshots may exist as caches, but they are not the primary model.
