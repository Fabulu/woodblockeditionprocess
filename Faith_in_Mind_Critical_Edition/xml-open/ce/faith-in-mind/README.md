# ce.faith-in-mind

Status: poem-first critical edition package

This package is no longer a scaffold. It now contains a publication-facing poem-first critical edition of the `信心銘` together with the supporting machine-readable apparatus, TEI, and bounded evented-anchor layer used for time travel and evidence navigation.

## Primary edition outputs

- `faith-in-mind.xml`
  - authoritative TEI reading-text package for the poem-first edition
- `apparatus.json`
  - selective poem-level apparatus
- `documents.json`
  - registered supporting documentation

## Time-travel and evidence outputs

- `../../../provenance/faith-in-mind/process/anchor-base-register.jsonl`
  - stable page or boundary anchors for the material poem loci
- `../../../provenance/faith-in-mind/process/anchor-event-log.jsonl`
  - event deltas for synchronized Chinese and English time travel
- `render-manifest.json`
  - frontend-facing summary of what to render and how to treat the package layers

## Scope

- Primary display object: the poem
- Apparatus scope: selective poem-level interventions and judgments only
- Commentary scope: preserved as a parallel secondary scholarly track, not part of the main reading body

## Current frontend expectation

ReadZen should treat this package as:

- a poem-first reading edition
- with restrained apparatus controls
- with synchronized Chinese and English time travel
- with page or band level evidence jumps for material poem events

The canonical research and provenance record still lives under:

- `Faith_in_Mind_Critical_Edition/provenance/faith-in-mind/`
