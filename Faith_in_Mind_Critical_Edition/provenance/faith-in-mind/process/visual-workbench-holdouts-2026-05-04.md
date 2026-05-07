# Visual Workbench Holdouts: 2026-05-04

This file consolidates the exhausted stronger direct-image-separation pass into a reusable evidence surface for the original 12 unresolved holdouts. It does not authorize a new `T1` text change by itself.

As of `2026-05-07`, the live unresolved queue has been reduced to four loci:

- `T1-p007.l03`
- `T1-p007.l12`
- `T1-p012.l02`
- `T1-p029.l06`

The helper-crop aliases for those loci were regenerated on `2026-05-07` because the problem had shifted from image quality to stale or mis-targeted local isolation surfaces.

## Workspace

- Alias directory: `provenance/faith-in-mind/process/visual-workbench-holdouts/`
- Source page images remain under `provenance/faith-in-mind/ocr/T1/page-images/`
- OCR support surfaces remain under:
  - `provenance/faith-in-mind/ocr/T1/ocr/rapidocr/`
  - `provenance/faith-in-mind/ocr/T1/ocr/paddleocr-ppocrv4/extracted-text/`
  - `provenance/faith-in-mind/ocr/T1/ocr/paddleocr-ppocrv4/column-ordered-text/`

## Holdout Index

| Locus | Alias evidence surface | Support surfaces | Current limit |
|------|------|------|------|
| `T1-p007.l03` | `visual-workbench-holdouts/T1-p007/T1-p007-l03-context*` plus legacy `...upper-cluster-b*` | `T1-p007` RapidOCR plus both Paddle surfaces | regenerated locus-specific alias now targets the tiny upper stub directly; surviving ink still remains only a contaminated `微`-like remnant |
| `T1-p007.l04` | `visual-workbench-holdouts/T1-p007/T1-p007-upper-cluster-a*`, `...upper-cluster-b*` | `T1-p007` RapidOCR plus both Paddle surfaces | same upper spillover wall as `l03`; no safe internal separation |
| `T1-p007.l08` | `visual-workbench-holdouts/T1-p007/T1-p007-lower-cluster*` | `T1-p007` RapidOCR plus both Paddle surfaces | lower-page cluster remains mixed with neighboring prose |
| `T1-p007.l09` | `visual-workbench-holdouts/T1-p007/T1-p007-lower-cluster*` | `T1-p007` RapidOCR plus both Paddle surfaces | lower-page cluster remains mixed with neighboring prose |
| `T1-p007.l12` | `visual-workbench-holdouts/T1-p007/T1-p007-l12-context*` plus legacy `...lower-cluster*` and full-page review | `T1-p007` RapidOCR plus both Paddle surfaces | regenerated locus-specific alias now isolates the lower tail better, but the page still yields only weak spillover around `前` |
| `T1-p012.l02` | `visual-workbench-holdouts/T1-p012/T1-p012-l02-exact*`, `...l02-wide*`, `...l02-context*`, `...l02-fullcol-context*` | `T1-p012` RapidOCR plus both Paddle surfaces; bounded `C11` support already opened for the page | regenerated upper-right opening-band helpers are materially better than the old generic clusters, but the local line still does not separate cleanly enough for repair |
| `T1-p029.l02` | `visual-workbench-holdouts/T1-p029/T1-p029-l02-exact*`, `...l02-wide*` | `T1-p029` RapidOCR plus both Paddle surfaces | page-edge short-fragment problem; stronger crop helps visibility but not full recovery |
| `T1-p029.l06` | `visual-workbench-holdouts/T1-p029/T1-p029-l06-exact*`, `...l06-wide*`, `...l06-context*`, `...l06-reference-fa-jian-column*` | `T1-p029` RapidOCR plus both Paddle surfaces | regenerated helpers now distinguish the exact `l06` column from neighboring context and the separate `法見...` reference lane; the remaining wall is local interpretation, not scan weakness |
| `T1-p030.l08` | `visual-workbench-holdouts/T1-p030/T1-p030-l08-exact*`, `...l08-wide*` | `T1-p030` RapidOCR plus both Paddle surfaces; bounded `C5/C9` phrase control already used earlier on the page | only unstable cadence `...轉親轉遠轉近...後來直得...` survives |
| `T1-p033.l03` | `visual-workbench-holdouts/T1-p033/T1-p033-open-cluster-a*`, `...open-cluster-b*` | `T1-p033` RapidOCR plus both Paddle surfaces; bounded `C5/C9` already opened for adjacent lines | tail `...方得少分` is clearer, but opening and middle still do not separate honestly |
| `T1-p033.l05` | `visual-workbench-holdouts/T1-p033/T1-p033-open-cluster-a*`, `...open-cluster-b*` | `T1-p033` RapidOCR plus both Paddle surfaces; bounded `C5/C9` already opened for adjacent lines | tail `...有什` is clearer, but no full defensible line emerges |
| `T1-p034.l05` | `visual-workbench-holdouts/T1-p034/T1-p034-l05-open-cluster*` | `T1-p034` RapidOCR plus both Paddle surfaces; bounded `C5/C9` already opened for adjacent lines | opening frame `師云一穿却一提起八面玲瓏...` is clearer, but the tail still collapses |

## Notes

- On `2026-05-07`, stale helper aliases were regenerated for the still-open `T1-p007`, `T1-p012`, and `T1-p029` loci after five independent crop-mapping checks showed that local isolation, not scan quality, was the live problem.
- A second `2026-05-07` remap then replaced the first guessed `T1-p012.l02` and `T1-p029.l06` helper boxes with RapidOCR-geometry-based short-fragment crops, because those two loci turned out to be tiny local strips rather than full-column remnants.
- A same-day fragment OCR rerun was then executed directly on the regenerated `T1-p012.l02` and `T1-p029.l06` exact/wide helper variants through both locally available fast engines. `RapidOCR` returned no text on any variant, and `PaddleOCR` returned only junk-level hallucinations such as `限果时易` and `天医`; these outputs are useful as negative evidence only and do not justify any `T1` text change.
- `T1-p007-upper-cluster-a*` and `T1-p012-cluster-a*` are now best treated as legacy exploratory assets rather than preferred live review surfaces.
- The newer `T1-p007-l03-context*`, `T1-p007-l12-context*`, `T1-p012-l02-*`, and `T1-p029-l06-*` aliases are the preferred entry points for any further manual visual pass on the remaining unresolved loci.
- The `T1-p007` and `T1-p012` aliases remain evidence surfaces, not claims that each crop cleanly isolates one single line.
- The `T1-p029`, `T1-p030`, `T1-p033`, and `T1-p034` aliases are the cleaned reusable names for the stronger-pass exact or widened derivatives already generated in-package.
- No locus in this 12-item queue crossed threshold for a safe `T1` repair on the present in-package basis.
- The visual-workbench phase is therefore improved and easier to resume, but still exhausted unless genuinely cleaner image evidence or genuinely new corroborative evidence appears.
