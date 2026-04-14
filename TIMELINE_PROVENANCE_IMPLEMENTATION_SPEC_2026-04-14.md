# Timeline Provenance And Visible-Edition Spec

Date: 2026-04-14  
Audience: programmer agent implementing `OpenZenTexts` and `CBETA-Translator` / ReadZen  
Status: binding spec for future critical-edition output

## Purpose

This spec makes the process history of a critical edition fully visible and navigable.

The reader must be able to:

1. read the edition text itself
2. see footnotes and use footnote navigation normally
3. inspect what changed, when, and why
4. move through the edition build chronologically with a timeline slider
5. see human-readable logs for every important step

This is no longer optional. Future critical-edition output must conform to this spec.

## Core rule

A critical edition is not only a final text plus provenance summary.

It is:

- a visible reading text
- a visible note system
- a visible apparatus
- a visible chronological build history
- a visible human-readable log of what happened

If the system cannot show how the text was built over time, it is incomplete.

## Mandatory product surfaces

The implementation must expose seven distinct surfaces:

1. `Edition text surface`
   - the reading text
   - visible notes and anchors
   - visible apparatus-linked loci where relevant

2. `Sidebar provenance surface`
   - short source / rights summary only
   - no giant process dump here

3. `Process surface`
   - current state of the build
   - stage summaries
   - unresolved counts

4. `Timeline surface`
   - slider or stepper over the chronological event stream
   - state at each point in time

5. `Log surface`
   - human-readable narrative log
   - what happened, why, by whom, with links to evidence

6. `Apparatus surface`
   - variants
   - decisions
   - witness support

7. `Stats surface`
   - quantitative summary of witnesses, OCR, unresolved loci, interventions, and coverage

Do not collapse these into one markdown blob or one overgrown manifest.

## Required output artifacts

Every critical-edition package must include:

### In `xml-open/{prefix}/{slug}/`

- `{slug}.xml`
- `manifest.json`
- `process.json`
- `timeline.json`
- `apparatus.json`
- `stats.json`
- `documents.json`
- `README.md`

### In `provenance/{slug}/process/`

- `edition-plan.md`
- `process-log.md`
- `decision-log.md`
- `unresolved-loci.md`
- `publication-checklist.md`
- `human-log.md`

### In `provenance/{slug}/collation/`

- `family-stemma.md`
- `copy-text-ranking.md`
- `witness-map.json`
- `locus-table.csv`

### In `provenance/{slug}/witnesses/`

- one `README.md` per witness or witness-family folder
- `witness-register.md`
- `acquisition-metadata.md`

## Required TEI behavior

The text itself must remain visible as text, not buried behind dialogs.

### Footnote rule

The reader must be able to:

- see footnote anchors in the text
- click or tap a footnote anchor
- jump to or open the relevant note
- return from note to anchor

Use anchored notes in TEI.

Preferred note-id families:

- `nkr_note_crit_*`
- `nkr_note_prov_*`
- `nkr_note_trans_*`
- `nkr_note_unres_*`
- `nkr_note_proc_*`

### Required footnote kinds

At minimum, the renderer must support:

- `critical`
  editorial or textual decisions
- `provenance`
  source or rights clarifications
- `translation`
  translation / reception notes
- `unresolved`
  unresolved reading warnings
- `process`
  build-stage notes when a visible edition location is directly affected

`process` notes are the exception, not the default.

Do not use `nkr_note_proc_*` for general chronology or workflow journaling.

Use them only when a process fact directly affects a visible text locus and the reader needs that note from the text itself.

### Visibility rule

When a visible reading in the text was changed, normalized, selected, or rejected:

- the change must be visible in the timeline system
- the reason must be visible in the log system
- if relevant to a locus, the note must be visible from the text itself

The note layer does not replace the log layer.
The timeline does not replace the apparatus layer.
These surfaces must remain distinct.

## Timeline model

The timeline is mandatory.

## Canonical reconstruction model

The canonical reconstruction model is reverse-patching from the final rendered text.

Do not treat full historical text snapshots as the primary truth source.

When the user scrubs to position `P`:

1. start from the current final reading text
2. collect all later `text_changed` events after `P`
3. reverse them in descending sequence order
4. restore each affected locus to its earlier state

This is now the required default design.

Non-text events do not mutate the visible text. They only change the visible metadata, process, apparatus, or state panels.

### Required user behavior

The user must be able to:

- drag a time slider across the build history
- step event by event
- jump by stage
- inspect what changed at each step
- see the state of the edition at that step

### Required artifact

Create `timeline.json`.

It is the canonical chronological event stream.

It must support reverse-patching and append-only revision growth.

### Timeline ordering rule

Every event must have:

- `event_id`
- `sequence`
- `timestamp`

`sequence` is authoritative for ordering if timestamps collide.

### Required event schema

Each event object must include:

```json
{
  "event_id": "evt_000123",
  "sequence": 123,
  "timestamp": "2026-04-14T18:20:00Z",
  "stage": "witness_validation",
  "event_type": "download_replaced",
  "object_type": "witness_file",
  "object_id": "A3",
  "summary": "Browser-downloaded replacement fixed A3.",
  "details": "The previous command-line downloads had inconsistent hashes and failed page-tree validation. The browser copy validated at 57 pages.",
  "actor_type": "hybrid",
  "actor_id": "user+agent",
  "inputs": [
    "Faith_in_Mind_NDL_Shiburokushou/NDL2537799_shiburokushou.pdf.bad_20260414_175854"
  ],
  "outputs": [
    "Faith_in_Mind_NDL_Shiburokushou/NDL2537799_shiburokushou.pdf"
  ],
  "evidence_links": [
    "https://commons.wikimedia.org/wiki/File:NDL2537799_%E5%9B%9B%E9%83%A8%E9%8C%B2%E6%8A%84.pdf"
  ],
  "state_effects": {
    "witness_status": "validated",
    "hash_changed": true,
    "page_count": 57
  },
  "decision_ref": "D-011",
  "supersedes": [
    "evt_000117",
    "evt_000118"
  ],
  "status": "applied"
}
```

### Required event types

At minimum:

- `project_started`
- `witness_found`
- `witness_rejected`
- `witness_tier_changed`
- `witness_set_locked`
- `sigla_frozen`
- `download_attempted`
- `download_failed`
- `download_replaced`
- `hash_recorded`
- `hash_changed`
- `validation_passed`
- `validation_failed`
- `ocr_started`
- `ocr_finished`
- `ocr_failed`
- `segmentation_started`
- `segmentation_finished`
- `copy_text_ranked`
- `copy_text_selected`
- `decision_made`
- `apparatus_entry_added`
- `apparatus_entry_changed`
- `unresolved_opened`
- `unresolved_closed`
- `text_changed`
- `publication_check_changed`

### Required stages

At minimum:

- `project_setup`
- `witness_search`
- `witness_validation`
- `witness_lock`
- `sigla_freeze`
- `copy_text_selection`
- `ocr`
- `segmentation`
- `collation`
- `apparatus`
- `reading_text`
- `review`
- `publication`

## Human-readable log model

The app must provide a log dialog or log tab that explains the process in normal prose.

### Required artifact

Create `human-log.md`.

This is not the same as `process-log.md`.

### Rule

`process-log.md` may be terse and tabular.

`human-log.md` must be readable as a chronological explanation of the edition build.

Each log entry should explain:

- what happened
- why it happened
- what changed
- who did it
- what evidence was used
- what remained unresolved afterward

### UI requirement

The log dialog must show:

- current event summary
- expanded human-readable explanation
- links to evidence
- links to related witnesses, decisions, apparatus entries, and notes

## State reconstruction requirement

The timeline slider must not be cosmetic.

The system must be able to reconstruct edition state at each event step.

### Minimum state fields at each step

- accepted witnesses
- rejected witnesses
- current witness tiers
- current copy-text candidate / selection
- current unresolved loci
- current OCR status
- current apparatus count
- current edition maturity

### Implementation options

Allowed:

- reconstruct state by replaying events from `timeline.json`
- derive earlier visible text states by reverse-patching from final text
- optionally maintain derived caches or snapshots as a secondary performance layer

Not allowed:

- fake the slider with a static list that does not affect visible state
- depend on full historical text snapshots as the primary archival model

## Visible text change tracking

When the edition text changes, the change must be visible in both the timeline and the text ecosystem.

### Required `text_changed` event fields

- `locus_id`
- `change_kind`
- `reason`
- `witness_support`
- `note_anchor_id` if a visible note exists

Preferred text-state payload:

- `reading_before`
- `reading_after`

with those indices referring to a top-level per-locus readings table.

Fallback only if needed:

- `previous_reading`
- `new_reading`

### Required `change_kind` values

- `selection`
- `emendation`
- `conjecture`
- `deletion`
- `addition`
- `normalization`
- `segmentation`
- `punctuation`
- `character_choice`
- `apparatus_only`

### Capture rule

The earlier reading state must be recorded at the moment of change, before overwrite.

Do not reconstruct it later from a later file state.

### One-event rule

One `text_changed` event corresponds to one locus changed one time.

If the same locus changes twice, create two events with different sequence numbers.

### Rule

If a reading decision is important enough to matter, it must be visible somewhere the reader can inspect:

- text note
- apparatus
- timeline
- human-readable log

## Provenance dialog / timeline dialog requirements

The current short provenance sidebar remains.

Add a dedicated dialog or browser for the richer system.

### Required tabs

1. `Sources`
2. `Timeline`
3. `Log`
4. `Apparatus`
5. `Stats`
6. `Documents`

### Timeline tab required controls

- slider
- next / previous event buttons
- jump by stage
- filter by actor type
- filter by witness
- filter by event type
- `show only text-changing events`

### Timeline tab required panels

- event summary
- event details
- state-at-this-step
- linked evidence
- related decisions
- related notes

### Log tab required behavior

- chronological prose log
- same event selected as timeline if possible
- human-readable explanation of the selected event

## JSON contract additions

### `process.json`

Must now include at least:

- `current_stage`
- `edition_maturity`
- `base_witness_id`
- `timeline_file`
- `human_log_file`
- `state_model`
- `reconstruction_model`
- `revisions`

### `timeline.json`

Preferred top-level structure:

```json
{
  "text_id": "ce.example",
  "reconstruction_model": "reverse_patch_from_final",
  "readings": {},
  "revisions": [],
  "events": []
}
```

### Revision model

The timeline must support append-only revision growth.

Rules:

- new events always get higher sequence numbers
- earlier event meanings do not change
- later revisions may supersede earlier outcomes through new events
- the UI should be able to jump to the end-state of a named revision

### `documents.json`

Must explicitly register:

- `process-log.md`
- `decision-log.md`
- `human-log.md`
- `family-stemma.md`
- `copy-text-ranking.md`
- other curated docs

Do not rely on autodiscovery.

## Programmer implementation requirements

The programmer agent must implement:

1. `timeline.json` schema
2. UI timeline slider
3. state reconstruction for each slider position
4. human-readable log dialog
5. TEI note-kind support for the required note families
6. visible linkage between text notes, apparatus entries, and timeline events
7. filtering and event inspection
8. document registry integration

## Output law for future editions

Future critical-edition packages must conform to this spec.

That means:

- no timeline = not complete
- no human-readable log = not complete
- no visible footnote support = not complete
- no ordered event system = not complete
- no state reconstruction for the slider = not complete

## Recommended first implementation target

Implement this first on:

- `wumenguan-1632` as migration exemplar

Then require it for:

- `faith-in-mind`

## Minimal acceptance checklist

The feature is not done unless all are true:

1. the text displays with note anchors
2. footnotes open and return correctly
3. the timeline slider steps through ordered events
4. the visible state changes when the slider moves
5. the human-readable log explains the selected event
6. a text-changing event can link back to apparatus and note anchors
7. the package validates against the new artifact requirements
