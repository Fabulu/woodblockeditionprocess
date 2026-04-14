# Programmer Brief: Definitive Witness Text Delivery And Viewer Use

Date: 2026-04-15
Purpose: tell the architect and implementer exactly what the edition pipeline will produce for witness texts, and how the viewer should use those outputs for hover, popup, copy, and comparison workflows.

## Core rule

Every published critical edition must ship not only:

- the critical reading text
- apparatus
- process and timeline history

but also a definitive delivered text package for each witness the edition actually produced.

The viewer must be able to open those witness texts directly.

## What "definitive witness text" means

This does not mean:

- infallible
- final in an absolute scholarly sense
- silently normalized into agreement with the critical text

It means:

- the best explicit edition-stage text file for that witness
- with a declared status
- with stable witness id / siglum
- with stable locus or page-line addressing
- with enough metadata that the program can expose it without guessing

## New hard rule: witness texts must line up by machine-readable locus

At handoff, the viewer must be able to tell which witness passage belongs to which edition locus.

Do not assume this means every witness can be forced into the same visual line breaks as the critical text.

That is often false.

What is required is machine-readable alignment.

Preferred contract:

- shared edition `locus_id`
- each witness can answer "what is your reading at this locus?"

Acceptable fallback when exact line-for-line alignment is impossible:

- stable witness-local anchors such as page-line ids or segment ids
- a companion locus map that maps edition `locus_id` to witness-local `start_anchor` / `end_anchor`
- explicit statuses such as:
  - `present`
  - `omitted`
  - `lacuna`
  - `unreadable`
  - `uncertain_span`

Not acceptable:

- raw witness text with no locus contract
- viewer-side guessing from filenames
- asking the UI to infer alignment from OCR folders

## What the pipeline will produce

For every witness used in the edition package, the pipeline should produce:

1. a definitive witness text file
2. a machine-readable witness registry entry
3. machine-readable locus access for comparison

## Required per-witness outputs

At minimum, each witness should have:

- `witness_id`
- `siglum`
- witness label
- witness family
- source metadata link
- text status
- completeness status
- confidence status
- text file path
- locus map or page-line map

Recommended text-status values:

- `raw_ocr`
- `normalized`
- `corrected_working`
- `definitive_witness_text`

The published witness surface should expose which one is being shown.

The edition should not make the viewer infer this from filenames.

## Recommended publication artifacts

### 1. `witnesses.json`

This is the machine-readable witness delivery registry for the app.

It should answer:

- what witnesses exist in this edition
- which are primary vs secondary
- which text artifact is the definitive delivered text for each witness
- where that text lives
- what its status and completeness are

Each witness entry should include:

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
- `alignment_mode`
- `alignment_statuses_supported`

### 2. definitive witness text files

Recommended forms:

- plain text for easy copy and inspection
- JSON or line-addressed companion for programmatic locus lookup

For example:

- `witness-texts/T1.txt`
- `witness-texts/T1.loci.json`

Recommended companion structure:

- one record per shared `locus_id`, or
- one span map from `locus_id` to witness-local start / end anchor

The text file should stay easy for a human to read and copy.

The JSON companion should let the app jump to a locus without parsing ad hoc text formats.

It should also let the app distinguish:

- exact aligned reading
- multi-locus span
- omission
- lacuna
- unreadable or uncertain witness coverage

### 3. comparison-ready locus payload

The app needs a stable way to ask:

- what do the witnesses read at this locus?

This can come from:

- `apparatus.json`
- per-witness locus maps
- or a derived `witness-readings.json`

But the contract must be explicit.

The viewer should not scrape markdown or improvise from OCR folders.

If a witness cannot yet be aligned confidently, mark that witness or locus as unresolved rather than pretending there is no problem.

## Viewer behavior expected from these outputs

### Default reading surface

- show the critical text
- keep footnotes and apparatus anchors on that surface

### Locus interaction

At a locus, the viewer should be able to open:

- short footnote
- apparatus detail
- witness comparison popup or panel
- timeline state at that locus

These remain separate surfaces.

### Witness comparison popup or panel

The comparison UI should:

- show the critical reading at the top
- show witness readings beneath it
- identify each witness by siglum and label
- show only differing witnesses by default if the witness count is large
- allow expansion to all witnesses
- allow plain-text copy of each witness reading
- allow copy of the whole comparison block
- show text-status and confidence when relevant

With many witnesses, default behavior should be:

- show witnesses that differ from the adopted reading
- show witnesses marked uncertain or unresolved
- collapse identical witnesses unless the user expands them

## Timeline relation

The timeline is still useful.

It should show:

- when a witness entered
- when a reading changed
- when an apparatus decision was made

But it is not the main witness-comparison surface.

The popup or panel is for source comparison.
The timeline is for edition history.

## Footnote relation

Footnotes should stay short.

They may say:

- why the edited reading was chosen
- that witnesses differ
- that a place remains unresolved

They should not dump the full comparison payload.

The full comparison payload belongs in the witness-comparison surface.

## Architect / implementer instruction

Assume the edition pipeline will deliver:

- critical text
- apparatus
- timeline
- definitive text outputs for all produced witnesses
- machine-readable witness registry
- machine-readable locus access

Build the viewer so it can:

1. open a witness comparison from a locus
2. show only differing witnesses by default
3. expand to all witnesses
4. copy witness readings as plain text
5. open the full witness text for any siglum
6. keep timeline separate from witness browsing

## Anti-patterns

Do not:

- make witness browsing depend on the timeline slider
- require markdown scraping to discover witness texts
- expose only the final critical text and hide witness texts off-stage
- collapse footnotes, apparatus, and witness comparison into one unreadable block
- assume all witnesses should be shown expanded at once when there are many

## Acceptance criteria

The implementation is acceptable only if:

1. every produced witness has a definitive delivered text artifact
2. the app can locate witness texts programmatically
3. a locus can open witness comparison without leaving the critical text
4. differing witnesses can be shown first
5. witness readings can be copied as plain text
6. timeline and witness comparison remain separate UI surfaces
