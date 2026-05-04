# Visual Workbench Holdouts: 2026-05-04

This file consolidates the exhausted stronger direct-image-separation pass into a reusable evidence surface for the 12 remaining unresolved holdouts. It does not authorize a new `T1` text change.

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
| `T1-p007.l03` | `visual-workbench-holdouts/T1-p007/T1-p007-upper-cluster-a*`, `...upper-cluster-b*` | `T1-p007` RapidOCR plus both Paddle surfaces | upper-page spillover remains suggestive but not line-isolated enough for closure |
| `T1-p007.l04` | `visual-workbench-holdouts/T1-p007/T1-p007-upper-cluster-a*`, `...upper-cluster-b*` | `T1-p007` RapidOCR plus both Paddle surfaces | same upper spillover wall as `l03`; no safe internal separation |
| `T1-p007.l08` | `visual-workbench-holdouts/T1-p007/T1-p007-lower-cluster*` | `T1-p007` RapidOCR plus both Paddle surfaces | lower-page cluster remains mixed with neighboring prose |
| `T1-p007.l09` | `visual-workbench-holdouts/T1-p007/T1-p007-lower-cluster*` | `T1-p007` RapidOCR plus both Paddle surfaces | lower-page cluster remains mixed with neighboring prose |
| `T1-p007.l12` | `visual-workbench-holdouts/T1-p007/T1-p007-lower-cluster*` plus full-page review | `T1-p007` RapidOCR plus both Paddle surfaces | bottom spillover still below safe line threshold |
| `T1-p012.l02` | `visual-workbench-holdouts/T1-p012/T1-p012-cluster-a*`, `...cluster-b*`, `...cluster-c*` | `T1-p012` RapidOCR plus both Paddle surfaces; bounded `C11` support already opened for the page | denser middle-column debris; no defensible single-line isolate |
| `T1-p029.l02` | `visual-workbench-holdouts/T1-p029/T1-p029-l02-exact*`, `...l02-wide*` | `T1-p029` RapidOCR plus both Paddle surfaces | page-edge short-fragment problem; stronger crop helps visibility but not full recovery |
| `T1-p029.l06` | `visual-workbench-holdouts/T1-p029/T1-p029-l06-exact*`, `...l06-wide*` | `T1-p029` RapidOCR plus both Paddle surfaces | page-mapped and OCR-visible, but still not safely line-isolated |
| `T1-p030.l08` | `visual-workbench-holdouts/T1-p030/T1-p030-l08-exact*`, `...l08-wide*` | `T1-p030` RapidOCR plus both Paddle surfaces; bounded `C5/C9` phrase control already used earlier on the page | only unstable cadence `...轉親轉遠轉近...後來直得...` survives |
| `T1-p033.l03` | `visual-workbench-holdouts/T1-p033/T1-p033-open-cluster-a*`, `...open-cluster-b*` | `T1-p033` RapidOCR plus both Paddle surfaces; bounded `C5/C9` already opened for adjacent lines | tail `...方得少分` is clearer, but opening and middle still do not separate honestly |
| `T1-p033.l05` | `visual-workbench-holdouts/T1-p033/T1-p033-open-cluster-a*`, `...open-cluster-b*` | `T1-p033` RapidOCR plus both Paddle surfaces; bounded `C5/C9` already opened for adjacent lines | tail `...有什` is clearer, but no full defensible line emerges |
| `T1-p034.l05` | `visual-workbench-holdouts/T1-p034/T1-p034-l05-open-cluster*` | `T1-p034` RapidOCR plus both Paddle surfaces; bounded `C5/C9` already opened for adjacent lines | opening frame `師云一穿却一提起八面玲瓏...` is clearer, but the tail still collapses |

## Notes

- The `T1-p007` and `T1-p012` aliases are page-cluster evidence surfaces, not claims that each crop cleanly isolates one single line.
- The `T1-p029`, `T1-p030`, `T1-p033`, and `T1-p034` aliases are the cleaned reusable names for the stronger-pass exact or widened derivatives already generated in-package.
- No locus in this 12-item queue crossed threshold for a safe `T1` repair on the present in-package basis.
- The visual-workbench phase is therefore improved and easier to resume, but still exhausted unless genuinely cleaner image evidence or genuinely new corroborative evidence appears.
