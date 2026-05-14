# Inter-Critical-Edition Comparison Protocol

**Version:** 1.0  
**Status:** Binding final-stage process law for completed critical editions  
**Applies to:** Any critical edition declared complete under ReadZen/OpenZen

## Purpose

Each new critical edition must be compared against every prior **completed** critical edition in the repo.

This is a mandatory late philological step. It exists to surface:

- direct citation
- probable quotation or reuse
- close parallel without secure dependence
- shared source-family inheritance
- meaningful non-overlap

The result can feed:

- apparatus notes
- commentary notes
- chronology-aware precedence warnings
- decision support
- visible text change if warranted

## Ordering rule

Run this protocol:

1. after the current edition has completed its own witness, OCR, collation, major boundary, and unresolved-loci work
2. before final completion declaration
3. before adding the current edition to `xml-open/ce/completed-editions.json`

## Scope rule

Compare only against prior **completed** critical editions unless the user explicitly broadens scope.

Do not use prior critical editions as hidden witness authority.

## Required inputs

For the current edition:

- locked witness set or explicit witness-set freeze
- copy-text selection or formal deferral
- current reading text / TEI candidate
- apparatus layer
- `current-state.md`
- `decision-log.md`
- `unresolved-loci.md`
- `process.json`
- `timeline.json`

For each prior completed comparandum:

- `xml-open/ce/completed-editions.json`
- comparandum `process.json`
- comparandum `timeline.json`
- comparandum edition text / TEI
- comparandum apparatus layer
- comparandum core editorial-method or introduction docs when present

## Mandatory steps

1. Build the comparandum set from `xml-open/ce/completed-editions.json`.
2. Normalize comparison units by locus, line span, passage span, or quoted band.
3. Detect overlap, citation, reuse, or meaningful non-overlap.
4. Classify each meaningful overlap as:
   - direct citation
   - probable quotation or reuse
   - close parallel without secure dependence
   - shared source-family inheritance
   - no meaningful overlap
5. Apply chronology-aware precedence control.
6. Determine editorial consequence:
   - no effect
   - corroborative only
   - apparatus note
   - commentary note
   - unresolved warning
   - decision support
   - text change
7. Feed any real consequence back into the edition.
8. Declare completion only after the gate closes.

## Required outputs

Every edition that runs this gate must produce:

- `provenance/{slug}/process/prior-editions-register.md`
- `provenance/{slug}/process/interedition-overlap-log.md`
- `provenance/{slug}/process/interedition-precedence-table.json`

## Footnote and commentary rule

This phase may generate reader-facing notes only when they are locus-linked and useful.

Valid products:

- short note that a line is quoted or paralleled in a prior completed critical edition
- short note that chronology supports probable reuse
- short warning that overlap exists but precedence remains unresolved
- short note that a prior edition preserves the same phrase family more clearly

Do not dump overlap tables or workflow history into footnotes.

## Completed-editions registry rule

The canonical repo-wide registry is:

- `xml-open/ce/completed-editions.json`

An edition may be added only after:

- package-local completion is explicitly declared
- the inter-critical-edition comparison gate is closed
- completion is reflected in package-local `process.json` and `timeline.json`

## Non-negotiable rule

A critical edition is not philologically complete until it can answer:

- which prior completed critical editions were checked
- where overlaps exist
- whether those overlaps are citation, reuse, parallel, or shared inheritance
- what chronology permits
- what editorial consequences followed
