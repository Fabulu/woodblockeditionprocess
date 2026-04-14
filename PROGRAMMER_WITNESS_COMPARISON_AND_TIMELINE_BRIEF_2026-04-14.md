# Programmer Brief: Witness Comparison vs Critical Text vs Timeline

Date: 2026-04-14
Purpose: codify the UI and data-model separation between the critical text, witness comparison, and editorial timeline so the implementation does not collapse distinct functions into one feature.

## Core rule

Do not treat these as the same thing:

1. the critical edition reading text
2. witness-text comparison
3. editorial history / timeline replay

They solve different user problems and must remain separate in both UI and data model.

## The three surfaces

### 1. Critical text surface

This is the main reading text.

It is:

- the edited critical text
- the reader-default surface
- the place where footnote anchors and note links live
- the place where apparatus-linked loci can be highlighted

It is not:

- a dump of one witness
- a side-by-side witness browser
- the editorial timeline itself

### 2. Witness comparison surface

This is the place where the user inspects source witnesses directly.

Preferred UI:

- a popup, drawer, side panel, or dedicated comparison dialog

It should show:

- the same locus across selected witnesses
- witness sigla and witness labels
- which witness supports which reading
- OCR/transcribed witness text for that locus
- confidence or check status where available

It is not:

- the final critical text
- the process journal
- the timeline slider

This surface answers:

- what do the witnesses actually read here?
- how do they differ?
- what raw basis supports the edited locus?

### 3. Timeline surface

This is the chronological replay of edition construction.

It should show:

- state-changing editorial events
- `text_changed` events
- witness-set locks
- copy-text locks or challenges
- unresolved opening/closing
- apparatus-affecting events

It is not:

- a witness browser
- a raw witness comparison tool
- a replacement for apparatus

This surface answers:

- how did the edition get to its current state?
- what changed, when, and why?

## Why this matters

A critical edition is not the same thing as displaying multiple source versions.

A critical edition is:

- a constructed editorial text
- grounded in multiple witnesses
- justified by apparatus, notes, and decision records

Therefore:

- witness access is necessary
- but witness access alone is not the critical-edition model

The app must support both:

- a coherent critical text
- and direct witness inspection

without confusing one for the other.

## Footnotes and apparatus interaction

Footnotes remain reader-facing locus notes.

They may:

- summarize why a reading was chosen
- warn about unresolved places
- point the reader toward witness disagreement

They should not:

- carry the whole decision log
- replace witness comparison
- replace timeline history

At a footnote or apparatus-linked locus, the UI may offer:

- `View witness readings`
- `Open apparatus`
- `Open timeline at this locus`

Those are three separate actions.

## Recommended user flow

### Reader default

1. reader sees the critical text
2. reader clicks a note anchor or apparatus-linked locus
3. reader chooses whether to inspect:
   - the note
   - witness readings
   - timeline history

### Editor / scholar flow

1. open a locus in the critical text
2. inspect witness comparison popup/panel
3. inspect apparatus detail
4. inspect timeline if needed to see how the edition state changed

Do not force witness comparison through the timeline UI.

## Data implications

To support witness comparison cleanly, the package should eventually expose witness-text data in a program-readable way.

At minimum, each witness should have:

- stable witness id / siglum
- source metadata
- OCR or transcribed text
- locus mapping or page/line mapping where possible
- registration in package metadata so the app can find it

The critical edition package should be able to answer:

- what witnesses exist?
- where is each witness text stored?
- how do I open witness text for a given locus?

## Suggested implementation direction

### Critical text mode

- keep the current reading surface centered on the edited text

### Witness comparison mode

- add a popup/panel/dialog for locus-based witness comparison
- start simple:
  - selected locus
  - selected witness set
  - text snippets or page/line slices
  - witness labels and sigla

### Timeline mode

- keep timeline tied to edition-state history only
- do not overload it with raw witness browsing

## Minimal acceptance criteria

The implementation is acceptable only if:

1. the critical text remains the primary surface
2. witness comparison can be opened without leaving the reading context
3. timeline remains about editorial history, not raw witness browsing
4. footnotes, apparatus, witness comparison, and timeline each have distinct jobs
5. the package data model can locate witness texts programmatically

## Anti-patterns

Do not implement any of these:

- using the timeline slider as the witness-comparison UI
- replacing apparatus with a loose witness popup and no structured evidence
- stuffing full editorial reasoning into footnotes
- making the critical text merely one tab among undifferentiated source versions

## Instruction to programmer

When implementing this in ReadZen / OpenZen:

1. preserve the critical text as the default reader experience
2. add witness comparison as a separate, locus-driven UI surface
3. keep timeline focused on edition history
4. ensure manifest/process/apparatus/document wiring can eventually locate witness texts programmatically
5. do not merge these three surfaces into one overloaded component
