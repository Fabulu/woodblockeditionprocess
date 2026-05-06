# Transcription Checklist

## Setup

- Choose one scan witness as the base.
- Validate the PDF before doing text work.
- Create a dedicated workspace under `Transcriptions`.
- Add `architect/`, `agent_notes/`, `scripts/`, `batch/`, `batch_refined/`.

## Batch

- Render all pages to PNG.
- Split left/right leaves if needed.
- Create refined frame crops.
- Run OCR across all leaves.
- Keep OCR outputs on disk.

## Read

- Read OCR first for evidence inventory.
- Read the image second to adjudicate OCR.
- Keep only what the image supports.
- Do not silently repair from memory or outside text.

## Draft

- Build the Markdown draft leaf by leaf.
- Record:
  - page / side
  - role
  - confidence
  - consolidated readable text
  - notes
- Before assigning text to `公案`, `無門曰`, `頌曰`, or another marked unit, inspect the next sequential leaf or page and verify whether the section continues or a new header actually begins there.
- Assign the top carry-over columns on the next leaf before trusting a cleaner marker lower on the page.
- If the next leaf or page is unclear or unavailable, keep the boundary open and note it as unresolved or provisional.
- Record the continuation check in the notes or verification ledger.

## Corroborate

- Add other scan witnesses in separate workspaces.
- Batch them too.
- Find reliable anchors first.
- Use corroborants to:
  - confirm weak clusters
  - correct bad labels
  - log divergences

## Clean Up

- Inventory weak leaves.
- Revisit them image-first.
- Use OCR only as support.
- Patch only real improvements.

## Keep Honest

- Mark blank / seal-only leaves as such.
- Do not overclaim from noisy OCR.
- Do not flatten witness differences.
- Keep a verification ledger.
