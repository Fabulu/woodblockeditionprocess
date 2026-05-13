# Poem Anchor Planning

Date: `2026-05-13`
Status: active planning basis after boundary-focused closing tranche completed through `我今解此如意珠 信受之者皆相應`

## Purpose

This document records the live page-tier and line-tier planning basis for the active exact image witnesses `YJG-W16`, `YJG-W17`, and `YJG-W22` after the OCR tranche-1 baseline, corrected-opening review, and the shared-interior continuation through `無量法門咸在目前 咫尺匪遙蹔時岐隔`.

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

- Poem-bearing page span: `page-0007` through `page-0056`
- Non-poem confirmation:
  - `page-0001` through `page-0006` are slip, title, or prefatory matter
  - `page-0057` is the terminal captured page but now confirmed as a dated note outside the poem span
- Planning posture:
  - `page-0007` is the mixed opening page and remains on the early character-tier watchlist
  - `page-0008` through `page-0055` are interior poem pages
  - `page-0056` is the Berkeley closing page

### `YJG-W22`

- Poem-bearing page span: `page-0007` through `page-0063`
- Non-poem confirmation:
  - `page-0001` through `page-0006` are cover, title, or prefatory matter
  - `page-0064` begins explicit afterword material
  - `page-0065` through `page-0068` are non-poem matter, with `page-0068` blank to OCR
- Planning posture:
  - `page-0007` is the mixed opening page and remains on the early character-tier watchlist
  - `page-0008` through `page-0062` are interior poem pages
  - `page-0063` is the final poem page at page tier, but its mixed closing geometry remains on the early character-tier watchlist

## Execution result

- `anchor-base-register.jsonl` is opened at page-plus-line tier for the confirmed poem loci in `YJG-W16`, `YJG-W17`, and `YJG-W22`.
- Opened row totals after the boundary-focused closing recheck:
  - `155` page-tier `.poem-band` rows
  - `717` line-tier `.l##` rows
  - `872` total anchor rows
- Still-provisional mixed or boundary pages remain:
  - `YJG-W16` `page-0007`
  - `YJG-W17` `page-0007`
  - `YJG-W22` `page-0007`
  - `YJG-W22` `page-0063`

## Current consequence

- Shared interior exact comparison has already advanced through the clean `YJG-W16` / `YJG-W17` `page-0017` tranche, ending at `無量法門咸在目前 咫尺匪遙蹔時岐隔`.
- The later shared-body continuation has now been carried through `我今解此如意珠 信受之者皆相應`.
- Direct review of the next poem-band-filtered left-frame surfaces in `YJG-W16 page-0019` and `YJG-W17 page-0021` showed commentary-style prose and back-references to already stabilized lines rather than one more adjacent stable shared poem continuation.
- The next bounded slice was therefore boundary-focused closing work, not another shared interior continuation or a return to witness hunt or OCR startup.
- That closing recheck has now resolved `YJG-W17 page-0057` out of the poem span and fixed `YJG-W22 page-0063` as the last poem page only at page tier.
- The active closing-boundary tranche is therefore exhausted for this witness set, and the next honest phase is copy-text selection.
- The active closing-boundary tranche is therefore exhausted for this witness set.
