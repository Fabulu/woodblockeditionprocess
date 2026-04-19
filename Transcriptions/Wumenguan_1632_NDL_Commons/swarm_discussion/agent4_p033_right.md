# Agent 4 Audit: PDF p.033 Right Leaf

Witnesses used: `batch_refined/frames/page_033_right_frame.png`, `batch_refined/ocr/page_033_right.txt`, `batch_refined/frames/page_033_right_frame.rapidocr.txt`, `batch_refined/frames/page_033_right_frame.paddleocr.txt`, and `architect/WUMENGUAN_1632.md:1697-1715`.

## Findings

- Strengthen `architect/WUMENGUAN_1632.md:1705`: the leaf appears to show `遂問婆子近處有甚麼宗師。` rather than `甚宗師`. The `麼` is faint, but the image supports it better than the draft does.
- Weaken `architect/WUMENGUAN_1632.md:1709`: the current draft is too clean at `可謂是前言不應後語。`. The image and OCR comparators both suggest a damaged or intervening phrase before `可謂` (OCR variants include `盡敗關` / `書败開`), so this should stay qualified rather than asserted as a smooth clause.
- Strengthen `architect/WUMENGUAN_1632.md:1707-1708`: `五里外有龍潭和尚。` and `及到龍潭，` are well supported by the image and by both OCR comparators.
- Leave unresolved `architect/WUMENGUAN_1632.md:1714-1715`: `雖然救得鼻孔，爭奈瞎却眼睛。` is readable, but the final character should remain orthography-cautious if the project is standardizing `却/卻`.

## Bottom Line

The draft is broadly aligned with the leaf, but the middle transition into `可謂是前言不應後語` should not be treated as fully settled yet. The verse tail is much safer than the prose bridge.
