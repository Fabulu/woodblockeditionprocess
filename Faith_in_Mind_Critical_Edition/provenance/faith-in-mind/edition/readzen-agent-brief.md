# ReadZen Agent Brief: Faith in Mind

Date: 2026-05-12  
Status: frontend handoff brief  
Audience: ReadZen / OpenZen frontend agent

## 1. What this package is

This is a poem-first critical edition of the `信心銘` (`Faith in Mind`).

The package contains:

- a publication-facing TEI poem text
- a selective poem-level apparatus
- a bounded evented-anchor layer for time travel and evidence jumps
- a substantial commentary and reception corpus preserved in provenance
- a large preserved provenance archive from the research and recovery process

The reader-facing product should foreground the poem and keep raw workflow archaeology mostly hidden by default.

## 2. What the reader should experience

Default reading experience:

- read the poem cleanly
- see line numbers or stable loci
- access only important editorial notes
- optionally move through editorial time travel
- optionally jump to source images or supporting witness pages

Do not surface in the reader-facing product:

- Japanese commentary / reception material
- OCR engine history
- `X1`, `X2`, `X173` style source-hunt chronology
- unresolved commentary residue
- raw process logs

Those belong in a research or provenance layer, not the reader-facing product.

## 3. Authoritative files to read first

Read these first. They define the edition and how it should be presented.

### Main edition files

- `C:\woodblocks\Faith_in_Mind_Critical_Edition\xml-open\ce\faith-in-mind\faith-in-mind.xml`
- `C:\woodblocks\Faith_in_Mind_Critical_Edition\xml-open\ce\faith-in-mind\apparatus.json`
- `C:\woodblocks\Faith_in_Mind_Critical_Edition\xml-open\ce\faith-in-mind\render-manifest.json`
- `C:\woodblocks\Faith_in_Mind_Critical_Edition\xml-open\ce\faith-in-mind\README.md`
- `C:\woodblocks\Faith_in_Mind_Critical_Edition\xml-open\ce\faith-in-mind\documents.json`
- `C:\woodblocks\Faith_in_Mind_Critical_Edition\xml-open\ce\faith-in-mind\process.json`

### Editorial-facing docs

- `C:\woodblocks\Faith_in_Mind_Critical_Edition\provenance\faith-in-mind\edition\editorial-introduction.md`
- `C:\woodblocks\Faith_in_Mind_Critical_Edition\provenance\faith-in-mind\edition\editorial-method.md`
- `C:\woodblocks\Faith_in_Mind_Critical_Edition\provenance\faith-in-mind\edition\working-critical-text.md`
- `C:\woodblocks\Faith_in_Mind_Critical_Edition\provenance\faith-in-mind\edition\commentary-secondary-track.md`
- `C:\woodblocks\Faith_in_Mind_Critical_Edition\provenance\faith-in-mind\edition\readzen-handoff.md`
- `C:\woodblocks\Faith_in_Mind_Critical_Edition\provenance\faith-in-mind\edition\readzen-commentary-integration-brief.md`

### Time-travel and evidence files

- `C:\woodblocks\Faith_in_Mind_Critical_Edition\provenance\faith-in-mind\process\anchor-base-register.jsonl`
- `C:\woodblocks\Faith_in_Mind_Critical_Edition\provenance\faith-in-mind\process\anchor-event-log.jsonl`
- `C:\woodblocks\Faith_in_Mind_Critical_Edition\xml-open\ce\faith-in-mind\timeline.json`

### Witness and source-link files

- `C:\woodblocks\Faith_in_Mind_Critical_Edition\provenance\faith-in-mind\witnesses\acquisition-metadata.md`
- `C:\woodblocks\Faith_in_Mind_Critical_Edition\provenance\faith-in-mind\witnesses\witness-register.md`

## 4. Procedural and protocol docs you should know

These are not for default reader display, but they tell you the workflow rules and provenance expectations behind the package.

- `C:\woodblocks\EDITION_EVENTED_ANCHOR_PROTOCOL.md`
- `C:\woodblocks\EDITION_AGENT_MASTER_INSTRUCTIONS.md`
- `C:\woodblocks\EDITION_FORENSIC_PROVENANCE_PROTOCOL.md`
- `C:\woodblocks\EDITION_TRANSLATION_DIFF_PROTOCOL.md`

Faith-specific state and closeout docs:

- `C:\woodblocks\Faith_in_Mind_Critical_Edition\provenance\faith-in-mind\process\current-state.md`
- `C:\woodblocks\Faith_in_Mind_Critical_Edition\provenance\faith-in-mind\process\publication-checklist.md`
- `C:\woodblocks\Faith_in_Mind_Critical_Edition\provenance\faith-in-mind\process\time-travel-anchor-backfill-plan.md`
- `C:\woodblocks\Faith_in_Mind_Critical_Edition\provenance\faith-in-mind\process\unresolved-loci.md`

Deep process logs if needed:

- `C:\woodblocks\Faith_in_Mind_Critical_Edition\provenance\faith-in-mind\process\process-log.md`
- `C:\woodblocks\Faith_in_Mind_Critical_Edition\provenance\faith-in-mind\process\human-log.md`
- `C:\woodblocks\Faith_in_Mind_Critical_Edition\provenance\faith-in-mind\process\correction-log.md`
- `C:\woodblocks\Faith_in_Mind_Critical_Edition\provenance\faith-in-mind\process\translation-diff-log.md`

## 5. How the files are organized

### Package root for the edition

- `xml-open/ce/faith-in-mind/`

This is the publication-facing package layer.

Use it for:

- TEI
- apparatus
- package metadata
- render manifest
- timeline

### Research / provenance root

- `provenance/faith-in-mind/`

This is the scholarly support layer.

Important subfolders:

- `edition/`
  - editorial introduction
  - editorial method
  - working critical text
  - ReadZen handoff notes
- `process/`
  - current state
  - logs
  - anchor files
  - unresolved loci
  - publication checklist
- `witnesses/`
  - witness register
  - acquisition metadata
- `ocr/`
  - page images
  - OCR outputs
  - page maps

## 6. What to render

### Main reading layer

Source:

- `faith-in-mind.xml`

Render:

- title
- careful attribution: traditionally attributed to Sengcan
- poem text
- stable line numbering

Do not mix commentary prose into the main poem body.

### Apparatus layer

Source:

- `apparatus.json`

Render as:

- selective note markers only
- expandable notes, side notes, or toggles

Apparatus should cover only material poem-level interventions:

- supplied lines
- corrected readings
- remapped loci
- omission judgment

### Editorial layer

Sources:

- `editorial-introduction.md`
- `editorial-method.md`

Render as:

- preface / introduction
- method section

### Commentary layer
Do not build one from the current package commentary corpus.

The currently assembled commentary corpus is largely Japanese-side reception/commentary material and should be ignored for the reader-facing product.

### Research layer

Optional or hidden by default:

- witness register
- process logs
- unresolved loci
- commentary-secondary-track

## 7. Time-travel behavior

Time travel should be event-driven, not full-text-snapshot driven.

Use:

- `anchor-event-log.jsonl` as the change stream
- `anchor-base-register.jsonl` as the stable anchor lookup

Per event, support:

- Chinese before / after
- English before / after
- event id
- change type
- evidence type
- confidence
- basis note

Chinese and English must move together.

Do not implement independent desynchronized sliders for Chinese and translation.

## 8. Evidence-jump behavior

Current honest support level:

- page image jumps: yes
- page-band or locus-band jumps: yes
- source page / download links: yes
- universal character-level click in every witness: no

Important constraint:

- supplied and omission loci may point both to a `T1` boundary page and to a supporting `T4` page band
- this is intentional and honest
- do not fake exact direct `T1` character geometry where the line was not separately preserved

## 9. Important edition semantics

### Omission judgment

`T1-p075` is important.

- the line `若不如此必不須守` exists in comparison witnesses
- it was **not** restored silently into the `T1` reading text
- it is represented as an omission judgment

That means the UI should distinguish:

- a supplied line
- a corrected line
- an omitted-in-base judgment

### Commentary is de-privileged here

The package contains a lot of commentary and recovery work.

That does **not** mean the frontend should present this as a commentary-driven base text edition.

The main product is the poem. The assembled commentary corpus should remain in the research layer unless a later curated Chinese commentary layer is added.

## 10. Remaining unresolved material

There are still four unresolved fragment-wall loci in the broader package:

- `T1-p007.l03`
- `T1-p007.l12`
- `T1-p012.l02`
- `T1-p029.l06`

These are preserved in provenance.

They are not part of the published poem text and should not be presented as if the reader is missing poem lines in the main reading view.
