# Time-Travel Anchor Backfill Plan: Faith in Mind Poem Edition

**Date:** 2026-05-09  
**Status:** completed for poem-first v1  
**Scope:** poem-first publication layer only

---

## Goal

Retrofit the existing `Faith in Mind` poem-first package with a diff-based evented anchor system that can support:

- synchronized Chinese + English time travel
- event-to-evidence jumps
- locus-level source navigation
- selective future character-level drilldown for contested poem loci

This backfill is intentionally limited to the poem-first edition layer. The commentary-secondary archive is out of scope unless a specific poem event depends on it.

---

## What will be backfilled

### 1. Event coverage

Backfill anchor-event rows only for poem-level events that materially affect the published reading or apparatus.

Priority classes:

1. accepted poem text changes
2. poem omission judgments
3. poem rollbacks or de-certainty events still relevant to apparatus
4. highly contested poem loci with explicit character provenance

### 2. Geometry coverage

Backfill page/locus geometry for:

- every poem locus that changed
- every poem locus cited in the selective apparatus
- every poem locus that received a human judgment call

Do **not** attempt universal full-text character geometry in v1.

### 3. Character-box coverage

Backfill per-character boxes only for loci where the accepted reading actually turned on individual graphs, such as:

- `T1-p007.l08`
- `T1-p007.l09`
- `T1-p007.l04`
- `T1-p030.l08`
- any comparison-supported restored poem loci already present in the selective apparatus

---

## Source files to use

### Text / state

- `xml-open/ce/faith-in-mind/timeline.json`
- `xml-open/ce/faith-in-mind/process.json`
- `xml-open/ce/faith-in-mind/apparatus.json`
- `provenance/faith-in-mind/transcription/corrected/T1-corrected-pass1-working.txt`

### Diff / reasoning

- `provenance/faith-in-mind/process/correction-log.md`
- `provenance/faith-in-mind/process/translation-diff-log.md`
- `provenance/faith-in-mind/process/translation-reasoning-log.md`
- `provenance/faith-in-mind/process/rejected-readings-log.md`
- `provenance/faith-in-mind/process/character-provenance-log.md`

### Evidence assets

- `provenance/faith-in-mind/ocr/T1/page-images/`
- `provenance/faith-in-mind/ocr/T1/page-map.csv`
- `provenance/faith-in-mind/ocr/T1/ocr/paddleocr-ppocrv4/*.json`
- `provenance/faith-in-mind/process/visual-workbench-holdouts/`
- `provenance/faith-in-mind/witnesses/acquisition-metadata.md`

---

## Output files

Created:

- `provenance/faith-in-mind/process/anchor-base-register.jsonl`
- `provenance/faith-in-mind/process/anchor-event-log.jsonl`

Optional later helpers:

- `provenance/faith-in-mind/process/anchor-backfill-notes.md`
- `provenance/faith-in-mind/process/character-box-exceptions.md`

---

## Backfill method

### Phase 1: Poem event inventory

Build the canonical poem event list from:

- `apparatus.json`
- final poem reading text
- poem-only `timeline.json` events
- poem-relevant correction-log rows

Each event should be normalized to:

- `event_id`
- `locus_id`
- `before_text`
- `after_text`
- `translation_before`
- `translation_after`
- `change_type`

### Phase 2: Page and locus anchors

For each poem event:

1. resolve the `T1` page id
2. bind the page image path
3. bind source download URL from acquisition metadata
4. record a locus bbox using:
   - curated crop geometry where available
   - OCR region geometry where reliable
   - manual normalized locus box where neither exists

### Phase 3: Selective character boxes

Only for contested or judgment-call loci:

1. derive character boxes from:
   - OCR polygons if usable
   - crop-local manual boxing if OCR is too coarse
2. attach them to the event row

### Phase 4: Validation

Check:

- every poem apparatus locus has either a page anchor or a locus anchor
- every poem-changing event has synchronized Chinese and English before/after states
- every event row points to a real asset path
- source download URLs resolve from acquisition metadata, even if they are not fetched at runtime

---

## Explicit non-goals for v1

- full commentary-anchor backfill
- full every-character geometry for the entire text
- all-witness universal character click support
- automatic PDF deep-linking beyond page/crop/locus where exact character boxes do not exist

---

## Definition of done

This backfill is complete when:

1. the published poem layer can time-travel bilingually through every material poem event
2. each poem event can open a supporting page or crop
3. major judgment-call loci can show selective character-level anchors
4. the remaining non-anchored loci are explicitly documented as page-level only

---

## Completion note

On `2026-05-09`, the poem-first v1 backfill was completed in the bounded form defined above:

- `anchor-base-register.jsonl` now records the stable page or boundary anchors for the poem-level apparatus loci
- `anchor-event-log.jsonl` now records the material poem-event deltas needed for bilingual time travel
- the backfill stays selective and poem-first
- coarse page or band geometry is used wherever finer boxing would have been fake in retroactive reconstruction
- supplied and omission-judgment loci now carry support-witness anchors instead of pretending to have direct T1 line geometry

Character-box capture remains deferred for any future UI work that truly needs per-graph drilldown on selected poem loci.

---

## Follow-up after backfill

Once this poem-only anchor system is working, the same protocol can be applied prospectively to future editions so this data is captured at edit time instead of reconstructed later.
