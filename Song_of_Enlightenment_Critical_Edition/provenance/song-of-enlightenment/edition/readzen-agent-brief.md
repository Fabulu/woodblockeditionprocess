# ReadZen Agent Brief: Song of Enlightenment

Date: 2026-05-15  
Status: frontend handoff brief  
Audience: ReadZen / OpenZen frontend programmer or agent

## 1. What this package is

This is a completed poem-first critical edition of the `永嘉證道歌` (`Song of Enlightenment`).

The package contains:

- a publication-facing TEI poem text
- a selective poem-level apparatus
- a synchronized English translation through the accepted current frontier
- a substantial witness / OCR / provenance archive
- a completed inter-critical-edition comparison gate against `Faith in Mind`

The reader-facing product should foreground the poem and its restrained editorial layer.

## 2. What the reader should experience

Default reading experience:

- read the poem cleanly
- see stable line numbering or stable loci
- access only important editorial notes
- access a short editorial introduction and method note
- optionally inspect selected witness or provenance material if the app has a research layer

Do not surface by default:

- raw OCR engine outputs
- wrapper logs
- witness-hunt chronology
- internal tranche names
- commentary-bearing witness clutter as if it were the main text

## 3. Authoritative files to read first

Read these first. They define the edition and how it should be presented.

### Main edition files

- `C:\woodblocks\Song_of_Enlightenment_Critical_Edition\xml-open\ce\song-of-enlightenment\song-of-enlightenment.xml`
- `C:\woodblocks\Song_of_Enlightenment_Critical_Edition\xml-open\ce\song-of-enlightenment\apparatus.json`
- `C:\woodblocks\Song_of_Enlightenment_Critical_Edition\xml-open\ce\song-of-enlightenment\README.md`
- `C:\woodblocks\Song_of_Enlightenment_Critical_Edition\xml-open\ce\song-of-enlightenment\documents.json`
- `C:\woodblocks\Song_of_Enlightenment_Critical_Edition\xml-open\ce\song-of-enlightenment\process.json`
- `C:\woodblocks\Song_of_Enlightenment_Critical_Edition\xml-open\ce\song-of-enlightenment\timeline.json`

### Editorial-facing docs

- `C:\woodblocks\Song_of_Enlightenment_Critical_Edition\provenance\song-of-enlightenment\edition\working-critical-text.md`
- `C:\woodblocks\Song_of_Enlightenment_Critical_Edition\provenance\song-of-enlightenment\edition\editorial-method.md`
- `C:\woodblocks\Song_of_Enlightenment_Critical_Edition\provenance\song-of-enlightenment\edition\editorial-introduction.md`
- `C:\woodblocks\Song_of_Enlightenment_Critical_Edition\provenance\song-of-enlightenment\edition\commentary-secondary-track.md`

### Inter-edition comparison files

- `C:\woodblocks\Song_of_Enlightenment_Critical_Edition\provenance\song-of-enlightenment\process\prior-editions-register.md`
- `C:\woodblocks\Song_of_Enlightenment_Critical_Edition\provenance\song-of-enlightenment\process\interedition-overlap-log.md`
- `C:\woodblocks\Song_of_Enlightenment_Critical_Edition\provenance\song-of-enlightenment\process\interedition-precedence-table.json`

## 4. Procedural and protocol docs you should know

These are not for default reader display, but they define the package law and provenance expectations.

- `C:\woodblocks\INTER_CRITICAL_EDITION_COMPARISON_PROTOCOL.md`
- `C:\woodblocks\EDITION_EVENTED_ANCHOR_PROTOCOL.md`
- `C:\woodblocks\EDITION_AGENT_MASTER_INSTRUCTIONS.md`
- `C:\woodblocks\EDITION_FORENSIC_PROVENANCE_PROTOCOL.md`
- `C:\woodblocks\EDITION_TRANSLATION_DIFF_PROTOCOL.md`

Song-specific state docs:

- `C:\woodblocks\Song_of_Enlightenment_Critical_Edition\provenance\song-of-enlightenment\process\current-state.md`
- `C:\woodblocks\Song_of_Enlightenment_Critical_Edition\provenance\song-of-enlightenment\process\publication-checklist.md`
- `C:\woodblocks\Song_of_Enlightenment_Critical_Edition\provenance\song-of-enlightenment\process\unresolved-loci.md`

## 5. How the files are organized

### Publication-facing package layer

- `xml-open/ce/song-of-enlightenment/`

Use it for:

- TEI
- apparatus
- package metadata
- timeline
- completion state

### Research / provenance layer

- `provenance/song-of-enlightenment/`

Important subfolders:

- `edition/`
  - working critical text
  - editorial method
  - editorial introduction
  - commentary-secondary note
- `process/`
  - current state
  - logs
  - unresolved loci
  - inter-edition comparison outputs
- `witnesses/`
  - witness register
  - acquisition metadata
- `ocr/`
  - OCR outputs
  - page images
  - runner logs and helper surfaces

## 6. What to render

### Main reading layer

Source:

- `song-of-enlightenment.xml`

Render:

- title
- careful attribution: traditionally attributed to Yongjia Xuanjue
- poem text
- stable line numbering or stable loci

Do not mix witness prose, commentary-bearing paratext, or OCR scaffolding into the main poem body.

### Apparatus layer

Source:

- `apparatus.json`

Render as:

- selective note markers only
- expandable notes, side notes, or toggles

Apparatus should stay poem-level and restrained.

### Editorial layer

Sources:

- `editorial-introduction.md`
- `editorial-method.md`

Render as:

- short introduction / preface
- method section

### Commentary layer

Do not build a visible commentary-reading layer from the current Song package.

Current rule:

- commentary, reception, and derivative anthology material remain secondary
- Japanese commentary is not part of the reader-facing edition logic for this work

## 7. Important edition semantics

### Copy-text rule

`YJG-W22` is the selected copy-text at witness level.

But:

- this does not mean every interior line should be presented as if it came from `YJG-W22` alone
- `YJG-W16` and `YJG-W17` control much of the stabilized interior because they preserve cleaner shared exact surfaces there

So the app should think in terms of:

- main edited reading text
- selective witness support

not:

- one raw witness dumped as the text

### Apparatus rule

The newly OCR-complete first-tier exact field did not produce another round of adopted text change.

The apparatus therefore records things like:

- opening boundary
- clean shared exact basis
- late receipt cluster
- copy-text closing watchpoint
- witness-class or blocked-source notes

not a full variorum.

### Inter-edition comparison rule

The Song package has already run the late mandatory comparison against `Faith in Mind`.

Current result:

- no Song poem-body text change
- real package-level intertextual relation in the secondary / commentary-facing layer

That means the app can later surface inter-edition contextual notes, but should not treat `Faith in Mind` as a hidden witness.

## 8. What to ignore

Ignore in the reader-facing product:

- wrapper logs
- suppressed Codex reports
- internal OCR tranche history
- scan-hunt archaeology
- Japanese commentary as if it were core Song editorial material

## 9. Suggested implementation order

1. Load and render `song-of-enlightenment.xml`.
2. Load `apparatus.json` and expose selective note markers.
3. Add editorial intro and method surfaces from the edition docs.
4. If desired, add a deeper research tab that points to witness/provenance docs from `documents.json`.
5. Reserve inter-edition comparison display for a later contextual layer; the data is already present.
