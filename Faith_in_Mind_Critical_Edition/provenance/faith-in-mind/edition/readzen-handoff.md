# ReadZen Handoff: Faith in Mind

Date: 2026-05-09  
Status: prepared for frontend integration

## 1. Primary reader experience

Render this edition as a poem-first critical reading text.

The reader should see:

- the title
- careful attribution: traditionally attributed to Sengcan
- a short editorial preface or introduction
- the edited poem text as the main visual object
- restrained note controls for material poem-level interventions

Do not foreground:

- commentary-body recovery
- OCR archaeology
- witness-hunt history
- `X*` source-opening chains
- unresolved commentary residue

Those belong in a research or provenance layer, not in the default reading surface.

## 2. Authoritative files

### Main reading layer

- `xml-open/ce/faith-in-mind/faith-in-mind.xml`
  - authoritative TEI reading text
- `provenance/faith-in-mind/edition/editorial-introduction.md`
  - publication preface
- `provenance/faith-in-mind/edition/editorial-method.md`
  - method summary

### Apparatus layer

- `xml-open/ce/faith-in-mind/apparatus.json`
  - selective poem-level apparatus only

### Time-travel and evidence layer

- `provenance/faith-in-mind/process/anchor-base-register.jsonl`
  - stable anchor layer
- `provenance/faith-in-mind/process/anchor-event-log.jsonl`
  - event delta layer
- `xml-open/ce/faith-in-mind/timeline.json`
  - package event chronology

### Research / secondary layer

- `provenance/faith-in-mind/edition/commentary-secondary-track.md`
- `provenance/faith-in-mind/process/process-log.md`
- `provenance/faith-in-mind/process/human-log.md`
- `provenance/faith-in-mind/witnesses/witness-register.md`

## 3. Reading-layer rules

Default visible text should be the poem only.

Use:

- `faith-in-mind.xml` as the rendered main text
- line numbering from the TEI `l/@n`
- `corresp` loci as stable drilldown ids

The main reading layer should not include commentary prose.

## 4. Apparatus-layer rules

The apparatus is selective and poem-level.

Only expose notes for:

- supplied loci
- corrected loci
- remapped loci
- omission judgments

Do not auto-expand all notes.

Preferred behavior:

- subtle inline marker or line-adjacent indicator
- click or expand to show the note
- show supporting witnesses and the kind of intervention

## 5. Time-travel rules

Time travel should be event-driven, not full-snapshot driven.

Use:

- `anchor-event-log.jsonl` as the main event delta source
- `anchor-base-register.jsonl` to resolve the supporting page or band anchor

For each event step, the UI should be able to show:

- Chinese before and after
- English before and after
- change type
- evidence type
- confidence
- basis note

The Chinese and English must move together by event id.

## 6. Evidence-jump rules

Support three levels of evidence jump:

1. page image
2. curated or band-level locus anchor
3. source download or source page link

Current package honesty boundary:

- many poem events have page or page-band anchors
- supplied or omitted loci may anchor through the T1 boundary page plus a comparison witness page band
- universal exact character boxing is not yet present and should not be implied

## 7. Character-click expectations

Do not promise universal character-level witness drilldown yet.

What is safe now:

- event or line click
- apparatus note
- page or page-band source jump

Character-level UX should be exposed only where future selective character boxes actually exist.

## 8. Display model

Use three conceptual layers:

### A. Reading

- poem text only
- clean typography
- stable line numbers

### B. Editorial

- introduction
- method
- selective apparatus
- omission and supplied-line notes

### C. Research

- witness register
- process logs
- commentary secondary track
- deep provenance

## 9. Package-specific cautions

- `T1-p075` is an omission judgment, not a silently restored line
- commentary-secondary material remains valuable but should stay out of the main reading body
- event anchors are intentionally selective and poem-first, not commentary-universal
- coarse page or band geometry is deliberate where finer retroactive boxing would have been fake

## 10. Ready-now frontend goals

The package is ready for:

- poem-first rendering
- selective apparatus display
- synchronized Chinese and English time travel
- page or band level evidence jumps

The package is not yet claiming:

- universal per-character witness coordinates
- full commentary-layer time travel
- all-witness character-variant matrices
