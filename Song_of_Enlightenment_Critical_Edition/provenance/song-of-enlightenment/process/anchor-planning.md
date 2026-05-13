# Poem Anchor Planning

Date: `2026-05-13`
Status: active planning basis after corrected-opening review and shared interior batches through `page-0015`

## Purpose

This document records the live page-tier and line-tier planning basis for the active exact image witnesses `YJG-W16`, `YJG-W17`, and `YJG-W22` after the OCR tranche-1 baseline, corrected-opening review, and the shared-interior continuation through `??????? ???????`.

It no longer uses the superseded startup assumption that the poem opened on `page-0004`. The authoritative corrected openings are now `page-0007` for `YJG-W16`, `YJG-W17`, and `YJG-W22`.

## Planning rules

- Page-tier planning is fixed for the poem-bearing spans in the three active exact witnesses.
- Line-tier planning is fixed at the page-class level:
  - opening mixed pages
  - interior poem pages
  - closing mixed pages
- Character-tier work remains deferred unless a locus is already risky from direct page evidence.
- OCR remains support evidence only; final line anchors still depend on the page images.
- The active planning locus pattern remains:
  - page tier: `{witness_id}-p####.poem-band`
  - line tier: `{witness_id}-p####.l##`
- Future rows must carry:
  - `evidence_tier`
  - `char_coverage`

## Witness planning

### `YJG-W16`

- Poem-bearing page span: `page-0007` through `page-0054`
- Non-poem confirmation:
  - `page-0001` through `page-0006` are cover, title, or prefatory matter
  - `page-0055` is back matter and also the only RapidOCR zero-text page
- Planning posture:
  - `page-0007` is the mixed opening page and remains on the early character-tier watchlist
  - `page-0008` through `page-0053` are interior poem pages
  - `page-0054` is a poem-bearing closing page with no separate afterword opened inside the current frame

### `YJG-W17`

- Poem-bearing page span: `page-0007` through `page-0057`
- Non-poem confirmation:
  - `page-0001` through `page-0006` are slip, title, or prefatory matter
  - `page-0057` is the terminal captured page and still poem-bearing
- Planning posture:
  - `page-0007` is the mixed opening page and remains on the early character-tier watchlist
  - `page-0008` through `page-0056` are interior poem pages
  - `page-0057` is the live closing-boundary page and remains on the early character-tier watchlist

### `YJG-W22`

- Poem-bearing page span: `page-0007` through `page-0063`
- Non-poem confirmation:
  - `page-0001` through `page-0006` are cover, title, or prefatory matter
  - `page-0064` begins explicit afterword material
  - `page-0065` through `page-0068` are non-poem matter, with `page-0068` blank to OCR
- Planning posture:
  - `page-0007` is the mixed opening page and remains on the early character-tier watchlist
  - `page-0008` through `page-0062` are interior poem pages
  - `page-0063` is the live closing-boundary page and remains on the early character-tier watchlist

## Execution result

- `anchor-base-register.jsonl` is opened at page-plus-line tier for the confirmed poem loci in `YJG-W16`, `YJG-W17`, and `YJG-W22`.
- Opened row totals after corrected-opening review:
  - `156` page-tier `.poem-band` rows
  - `721` line-tier `.l##` rows
  - `877` total anchor rows
- Still-provisional mixed or boundary pages remain:
  - `YJG-W16` `page-0007`
  - `YJG-W17` `page-0007`
  - `YJG-W17` `page-0057`
  - `YJG-W22` `page-0007`
  - `YJG-W22` `page-0063`

## Current consequence

- Shared interior exact comparison has already advanced through the clean `YJG-W16` / `YJG-W17` `page-0015` tranche, ending at `??????? ???????`.
- The next bounded slice is the next shared interior continuation after that stabilized frontier, not a return to witness hunt or OCR startup.
