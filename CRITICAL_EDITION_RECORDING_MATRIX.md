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

Do not collapse:

- critical text surface
- witness comparison surface
- timeline surface

They are separate layers of use.

Every edition must also deliver definitive witness text outputs for the witnesses it actually produces, so the viewer can expose direct witness comparison without scraping working files.

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

### `current-state.md`

Use for the one-screen resumability summary.

Record here:

- current phase
- last completed phase
- exact next action
- locked witness-set status
- locked copy-text status
- first comparison witnesses if already chosen
- active blockers
- key files to open next

This file exists so a future agent does not restart the workflow from the top when the package already has state.

It must name the actual last bounded work slice that was completed, not only a broad stage label.

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

Do not absorb later text work into an older stage-start event.

If visible text changes again in a new bounded work slice, create a fresh `text_changed` event for that slice.

### `apparatus.json`

Use for structured variant and decision data.

Record here:

- locus-level readings
- witness support
- chosen lemma
- decision basis
- apparatus status

Do not use this as the only place that a visible text change is recorded.

### TEI note layer

Use for reader-facing locus-linked notes only.

Record here:

- short critical notes tied to a visible locus
- short provenance clarifications tied to a visible locus
- short unresolved warnings tied to a visible locus

Do not record here:

- step-by-step workflow chronology
- full editorial reasoning chains
- OCR troubleshooting history
- general methodology explanation

Those belong in logs, timeline, and apparatus instead.

### Witness comparison layer

Use for direct source-witness inspection at a locus.

This should expose:

- witness id / siglum
- witness text slice or mapped reading
- source witness support at the selected locus

This is not the same thing as:

- `timeline.json`
- TEI footnotes
- `human-log.md`

The comparison layer must be backed by definitive delivered witness texts and machine-readable witness lookup, not by ad hoc OCR-folder browsing.

### `witnesses.json`

Use for machine-readable witness delivery and viewer lookup.

Register here:

- witness id / siglum
- witness label
- witness family
- witness role
- definitive witness text file
- text status
- completeness
- confidence
- locus-map or page-line map path

This file exists so the app can open witness texts programmatically and present locus comparison without guessing from filenames.

### `documents.json`

Use for curated document registration.

Register here:

- `process-log.md`
- `decision-log.md`
- `human-log.md`
- `current-state.md`
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

### Before any substantial text-work slice begins

Declare the bounded work slice first.

At minimum record:

- slice label or short scope name
- starting locus
- ending locus if known
- target file or files expected to change

Record this in the active pass log and keep `current-state.md` aligned with it.

Do not begin a substantial correction or collation batch without a declared slice boundary.

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

For East Asian scan witnesses, also record the mandatory four-engine comparator status:

- `tesseract`
- `RapidOCR`
- `PaddleOCR`
- `EasyOCR`

For each engine, record:

- run status: full pass, calibration-only, blocked, or failed
- environment and model details
- output location if successful
- exact runtime failure if blocked or failed

Also update `page-map.csv` with page-role classification before treating the witness as if every page were body text.

### When a visible reading changes

Always write to:

- `timeline.json` as `text_changed`

Also write to:

- `decision-log.md` if the change is editorially non-trivial
- `human-log.md` if the change matters to reader-facing explanation
- `apparatus.json` if it affects the structured apparatus
- TEI note layer if a visible footnote is warranted

Also require:

- the active pass log to declare the bounded work slice that produced the change
- `current-state.md` updated so `last_completed_phase` names the completed slice
- a fresh `text_changed` event for the slice rather than silently expanding an older start event

If a TEI note is added:

- keep it short and locus-specific
- do not use it as a duplicate process journal entry
- keep the full reasoning in `decision-log.md` when needed

### When a locus remains unresolved

Write to:

- `unresolved-loci.md`
- `timeline.json`

### When a revision is published or extended

Write to:

- `timeline.json` revision metadata
- `human-log.md`

### When the package phase changes or work is paused

Write to:

- `current-state.md`
- `documents.json` if the file is newly introduced

If the phase change is machine-relevant:

- also `timeline.json`
- `process.json`

### When preparing to publish or hand off

Run a final coherence and integrity pass over:

- `manifest.json`
- `process.json`
- `timeline.json`
- `apparatus.json`
- `witnesses.json`
- `stats.json`
- `documents.json`
- TEI note anchors and note targets

Confirm:

- JSON parses
- schema validation passes where supported
- referenced files exist
- cross-file ids resolve
- every witness declared for viewer comparison has a definitive delivered text artifact
- note, apparatus, and journaling layers are not being misused or duplicated

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

A later correction batch in a new bounded slice is not the same moment.

Do not revise an older event instead of creating a new one.

## Slice close-out law

Before a bounded text-work slice is treated as complete, verify that these agree:

- the latest coverage named in the active pass log
- `last_completed_phase` in `current-state.md`
- the newest relevant `timeline.json` event

If those three do not point to the same completed slice, the slice is not closed out correctly.

## Reverse-patching law

The visible timeline should reconstruct earlier text states by reverse-patching from the final reading text.

That means:

- later `text_changed` events are reversed when scrubbing backward
- non-text events do not mutate the visible text
- notes and apparatus should only appear once their originating events have happened

Full historical snapshots may exist as caches, but they are not the primary model.
