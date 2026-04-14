# Agent 1: page_047_right unresolved graph

## Scope

- Witness only
- Focused on `page_047_right_frame.png`
- Target phrase currently drafted around: `門云拈起扇…`

## Materials used

- `batch_refined/frames/page_047_right_frame.png`
- cropped enlargements made locally during this pass
- `batch_refined/frames/page_047_right_frame.rapidocr.txt`
- Tesseract with local `chi_tra_vert` model
- parent draft entry in `architect/WUMENGUAN_1632.md`

## Best reading of visible lines

What I consider stable from the witness:

```text
é–€äº‘æ‹ˆèµ·æ‰‡å­äº‘ã€‚
æ‰‡å­ã€”?ã€•è·³ä¸Šä¸‰åä¸‰å¤©ã€‚
ç¯‰è‘—å¸é‡‹é¼»å­”ã€‚
æ±æµ·é¯‰é­šæ‰“ä¸€æ£’ï¼Œ
雨似盆傾。
```

I am confident about:

- `門`
- `云`
- `拈`
- `起`
- `扇`
- `å­`
- second `扇`
- second `å­`
- `ä¸‰åä¸‰å¤©`
- `ç¯‰è‘—å¸é‡‹é¼»å­”`
- `æ±æµ·é¯‰é­šæ‰“ä¸€æ£’`
- `雨似盆傾`

## Confidence per graph in the disputed area

For the narrow disputed band after the second `æ‰‡å­`:

- `扇`: high
- `å­`: high
- next graph: low
- following motion graph: medium-low, likely `跳`
- `上`: inferred from column continuation, medium
- `ä¸‰åä¸‰å¤©`: high

## Alternatives considered

### Option A

```text
æ‰‡å­è·³ä¸Šä¸‰åä¸‰å¤©
```

Reason considered:

- this is the simplest fit if the apparent extra mark between `å­` and `è·³` is only overlap/carry from an adjacent column or an artifact of the crop

Why I rejected it:

- in the enlarged crop, I still see evidence of an additional graph-like form after the second `å­` and before the clearer jump-like graph lower down
- I cannot prove that the extra form is just noise

### Option B

```text
æ‰‡å­ã€”?ã€•è·³ä¸Šä¸‰åä¸‰å¤©
```

Reason considered:

- this matches the visible sequence best if there really are two graph positions after the second `å­`
- the lower of the two looks compatible with `跳`

Current judgment:

- this remains the most defensible conservative reading

### Option C

- some two-character motion phrase after `æ‰‡å­`, e.g. an extra verb before `è·³`

Why rejected:

- none of the OCR engines gave a trustworthy candidate
- the image itself does not support a decisive graph identification for the first slot

## OCR corroboration summary

- RapidOCR strongly supported the surrounding structure but not the disputed graph
- Tesseract was noisy and not decisive
- PaddleOCR did not materially improve the target graph
- EasyOCR was not used by me in this agent note; my conclusion is based on image plus the three in-workspace OCR comparators above

## Recommendation

The unknown graph should remain unknown.

I recommend keeping:

```text
æ‰‡å­ã€”?ã€•è·³ä¸Šä¸‰åä¸‰å¤©ã€‚
```

and not normalizing it to `æ‰‡å­è·³ä¸Šä¸‰åä¸‰å¤©` unless another human reader can justify removing the extra slot from the witness image itself.
