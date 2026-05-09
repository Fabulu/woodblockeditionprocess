# Publication Checklist: Faith in Mind

Status: publication candidate with frontend handoff in progress

## Pre-publication gates

- [x] witness search saturated enough to justify lock
- [x] accepted witness set locked
- [x] rejected/deferred witnesses recorded
- [x] every accepted witness has source page, download path, rights basis, local file info
- [x] OCR completed for active witnesses
- [x] OCR failure areas logged
- [x] copy-text chosen and justified
- [x] apparatus generated from logged decisions
- [x] unresolved loci reviewed
- [x] translation diff coverage kept in sync with accepted Chinese text changes
- [x] witness-page coverage audit passes for the active non-blank witness span
- [x] package validation entrypoint rerun successfully
- [x] local TEI structural QA passes
- [ ] TEI validated against an external schema
- [x] machine-readable package files aligned
- [x] required JSON files parse cleanly
- [x] schema validation passes where available
- [x] document-registry and manifest file paths resolve
- [x] TEI note anchors and note targets resolve
- [x] notes, apparatus, decision log, and human log stay in distinct roles
- [x] provenance and process docs registered in `documents.json`
- [x] poem-first reading text extracted from commentary-heavy working state
- [x] commentary and reception material demoted to a parallel secondary track
- [x] editorial introduction polished beyond first-draft state
- [x] poem-only evented-anchor backfill completed for material publication events
- [x] ReadZen handoff spec prepared
- [x] frontend render manifest prepared

## Current blocker

The project is no longer blocked on text recovery or package-internal publication prep. The remaining work is frontend integration:

- render the poem-first edition in ReadZen
- expose the selective apparatus cleanly
- wire synchronized Chinese and English time travel to the evented-anchor layer
- wire page or band-level evidence jumps and source links
