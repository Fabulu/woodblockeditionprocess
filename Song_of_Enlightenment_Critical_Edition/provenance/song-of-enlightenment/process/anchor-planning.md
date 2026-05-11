# Poem Anchor Planning

Date: `2026-05-11`
Status: completed page-span and page-plus-line planning for OCR tranche 1 exact image witnesses

## Purpose

This document converts the completed four-engine OCR baseline for `YJG-W16`, `YJG-W17`, and `YJG-W22` into the bounded planning needed before comparison or transcription starts.

It does **not** pretend that final line segmentation or character boxing has already been captured in `anchor-base-register.jsonl`.

## Planning rules adopted here

- Page-tier planning is now fixed for the poem-bearing spans in the three active exact witnesses.
- Line-tier planning is now fixed at the page-class level:
  - opening mixed pages
  - interior poem pages
  - closing mixed pages
- Character-tier work remains deferred unless a locus is already clearly risky from the page evidence.
- OCR is support evidence only at this stage. Final line anchors must still be taken from the page images, with OCR used to help order and isolate poem lines.
- Until cross-witness line adjudication starts, the planning locus pattern should be:
  - page tier: `{witness_id}-p####.poem-band`
  - line tier: `{witness_id}-p####.l##`
- Future `anchor-base-register.jsonl` rows opened from this plan must carry:
  - `evidence_tier`
  - `char_coverage`

## Witness planning

### `YJG-W16`

- Poem-bearing page span: `page-0004` through `page-0054`
- Non-poem confirmation:
  - `page-0001` to `page-0003` are cover or pre-poem matter
  - `page-0055` is back matter and also the only RapidOCR zero-text page
- Page-tier plan:
  - `page-0004`: opening mixed page; anchor only the framed poem block on the right-hand text-bearing side and exclude the blank facing area plus library stamps outside the block
  - `page-0005` through `page-0053`: interior poem pages; use the full framed poem text area for page-tier planning
  - `page-0054`: closing poem page; still poem-bearing and no separate afterword begins on this page
- Line-tier plan:
  - On `page-0004`, line anchors must start only where the poem body begins inside the framed block; title and non-poem outer marks stay out of line loci
  - On `page-0005` through `page-0053`, derive one line locus per poem line from the framed text block in right-to-left reading order
  - On `page-0054`, derive line loci normally inside the framed poem block; do not create any post-poem line loci unless a later direct image review proves a separate prose tail inside the frame
- Early character-tier watchlist:
  - `page-0004` opening title/body transition if the first comparison pass turns on where the poem proper begins

### `YJG-W17`

- Poem-bearing page span: `page-0004` through `page-0057`
- Non-poem confirmation:
  - `page-0001` to `page-0003` are slip, catalog, or title surfaces rather than the poem body
  - no separate non-poem leaf appears after `page-0057` because `page-0057` is the terminal captured page and still carries poem text
- Page-tier plan:
  - `page-0004`: opening mixed page; anchor the framed poem block only, excluding outer library marks and non-poem edge matter
  - `page-0005` through `page-0056`: interior poem pages; use the full framed poem text area
  - `page-0057`: closing poem page; still poem-bearing to the end of the witness image tranche
- Line-tier plan:
  - On `page-0004`, line anchors begin only inside the framed poem block after the title opening
  - On `page-0005` through `page-0056`, derive one line locus per poem line from the main framed block in right-to-left reading order
  - On `page-0057`, derive line loci through the surviving poem block and do not invent a postscript break that the page image does not show
- Early character-tier watchlist:
  - `page-0004` opening title/body transition if opening-line delimitation becomes contested
  - `page-0057` closing lines if later comparison shows a possible damaged or compressed final locus

### `YJG-W22`

- Poem-bearing page span: `page-0004` through `page-0063`
- Non-poem confirmation:
  - `page-0001` to `page-0003` are cover or pre-poem matter
  - `page-0064` begins explicit `houxu` / afterword material
  - `page-0065` continues non-poem prose
  - `page-0066` is glossary / pronunciation matter
  - `page-0067` and `page-0068` are end matter / covers, with `page-0068` also blank to OCR
- Page-tier plan:
  - `page-0004`: opening mixed page; anchor only the framed poem block and exclude outer catalog marks or title-side matter outside the block
  - `page-0005` through `page-0062`: interior poem pages; use the full framed poem text area
  - `page-0063`: closing mixed page; anchor only the main framed poem block and exclude the upper marginal prose plus outer note bands
- Line-tier plan:
  - On `page-0004`, line anchors begin only within the poem block after the opening title matter
  - On `page-0005` through `page-0062`, derive one line locus per poem line from the main framed block in right-to-left reading order
  - On `page-0063`, derive line loci only from the main framed poem block; the upper prose and side notes belong to post-poem commentary, not to poem line anchors
- Early character-tier watchlist:
  - `page-0004` opening title/body transition if the first exact-witness comparison disputes the opening line break
  - `page-0063` final poem line against adjacent prose, because this is the clearest boundary page in the active tranche where a later apparatus decision may need graph-level confirmation

## Cross-witness consequences for the next slice

- The next comparison or transcription slice can now open line loci only inside the confirmed poem-bearing spans instead of wasting work on covers, afterwords, or glossary pages.
- The first anchor rows should be opened from this plan witness by witness, starting with page-band rows and then line rows for the actual poem lines encountered.
- No character boxes should be fabricated during that opening pass; only the watchlist loci above should be considered early candidates for Tier 3 capture.
