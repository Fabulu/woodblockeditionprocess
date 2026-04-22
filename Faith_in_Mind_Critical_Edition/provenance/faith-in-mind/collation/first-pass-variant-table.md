# First-Pass Variant Table: `T4`, `T5`, `T2`, `T3`, `A1`, `A2`, `A3`, and `C1` vs `T1`

Date: 2026-04-15
Status: active first comparison pass
Scope: compare isolated comparison-control body spans against the current `T1` recovered lemma spine

## Method note

- `T1` remains the locked starting copy-text.
- `T4` is the first comparison-control witness.
- This table records only what the current comparison-witness images plus saved OCR stacks support clearly.
- Clear comparison support may:
  - confirm an existing `T1` recovered lemma
  - expose a likely missing or displaced `T1` lemma
  - expose a branch-level closing difference that should not be flattened silently
- This table does not itself authorize a copy-text switch or an unlogged overwrite of `T1`.

## High-confidence confirmations

| T4 evidence span | T1 locus or loci | Result | Notes |
|---|---|---|---|
| `至道無難 唯嫌揀擇` through `欲得現前 莫存順逆` on `T4-p002` | `T1-p007.l01` to `T1-p010.l01` | confirmed | the `T4` opening body supports the already corrected `T1` opening sequence |
| `違順相爭 是爲心病` on `T4-p002` | `T1-p011.l01` | confirmed | supports the existing `T1` correction |
| `圓同太虛 無欠無餘` and `良由取捨 所以不如` on `T4-p002` | `T1-p014.l01`, `T1-p015.l01` | confirmed | supports the existing `T1` corrections |
| `止動歸止 止更彌動` and `唯滯兩邊 寧知一種` on `T4-p002` | `T1-p019.l01`, `T1-p021.l01` | confirmed | supports the existing `T1` corrections |
| `多言多慮 轉不相應` through `一空同兩 齊含萬象` on `T4-p003` | `T1-p024.l01` to `T1-p036.l01` where already recovered | broadly confirmed | `T4` supports the already recovered mid-band sequence while also exposing one previously unresolved gap inside it |
| `不見精粗 寧有偏黨` through `智者無爲 愚人自縛` on `T4-p003` | `T1-p037.l01` to `T1-p046.l01` | confirmed | the recovered `T1` sequence matches the `T4` body cleanly here |
| `眼若不眠 諸夢自除` through `虛明自照 不勞心力` on `T4-p004` | `T1-p053.l01` to `T1-p064.l01` where already recovered | broadly confirmed | the late-band `T1` recoveries align well with `T4` |
| `真如法界 無他無自` through `言語道斷 非去來今` on `T4-p004` | `T1-p066.l01` to `T1-p079.l01` where already recovered | broadly confirmed | the final run confirms the broad `T1` spine, including the closing sequence from visible `T1-p076.l01` onward |

## Candidate repair or collation loci exposed by `T4`

| Comparison issue | Current T1 state | T4 support | Current judgment |
|---|---|---|---|
| missing line between `T1-p021.l01` and `T1-p022.l01` | `T1` formerly jumped from `唯滯兩邊寧知一種` to `遣有沒有從空背空` | `T4-p002` preserves `一種不通兩處失功` between those two lines | resolved through supplied stable insertion `T1-p021.l01a`; no silent renumbering was used |
| unresolved sequence around `T1-p032.l01` | `T1` had split or damaged the expected sequence across `T1-p031.l03` and `T1-p032.l01` | `T4-p003` preserves `二由一有 一亦莫守` followed by `一心不生 萬法無咎` before `無咎無法 不生不心` | resolved by restoring `T1-p031.l03` and `T1-p032.l01` to that sequence |
| likely repair for `T1-p047.l01` | `T1-p047.l01` had remained garbled | `T4-p003` preserves `法無異法 妄自愛著` between `智者無爲 愚人自縛` and `將心用心 豈非大錯` | resolved in the first post-compliance comparison-informed correction slice |
| likely repair for `T1-p065.l01` | `T1-p065.l01` had remained garbled | `T4-p004` preserves `非思量處 識情難測` between `虛明自照 不勞心力` and `真如法界 無他無自` | resolved in the first post-compliance comparison-informed correction slice |
| closing-sequence branch issue after `T1-p077.l01` | `T1` now carries supplied `T1-p077.l01a = 但能如是何慮不畢`, while `T1-p075.l01` remains commentary and `T1-p076.l01 = 若如是必不須守` is visually secure before `一即一切一切即一` | `T4-p004` clearly preserves `但能如是 何慮不畢`, and the broader transmitted sequence would also expect `若不如此必不須守` before `若如是必不須守` | resolved as omission judgment: the `T1` witness supports the visible `若如是必不須守` close onward but does not support reinstating the standard `若不如此必不須守` line on `T1-p075` |

## Immediate use

- `T4` has now done its first real comparison work.
- Do not treat every `T4` reading as automatically superior to `T1`.
- `T5` is now also completed as a bounded comparison-control witness and functions mainly as corroborative support for the recovered `T1` spine.
- `T2` is now also completed as a bounded comparison-control witness and functions mainly as corroborative support for the recovered `T1` spine.
- The next comparison-control target is `T3`, not more `T4`, `T5`, or `T2` closure work.

## `T5` confirmation slice

Date: 2026-04-15
Status: bounded confirmation pass completed
Scope: compare the isolated `T5-p004` to `T5-p006` body span against the current `T1` recovered lemma spine after `T5` reached full four-engine compliance

### Method note

- `T5` was not used before its full-pass `RapidOCR`, `tesseract`, `PaddleOCR PP-OCRv4`, and `EasyOCR` status block was recorded.
- The `T5` OCR text layers are noisier than the saved `T4` comparison witness, so exact line claims were checked against direct image review of `RB00012929_00004.jpg` to `RB00012929_00006.jpg`.
- This slice records only broad confirmation and any new high-confidence loci. It does not flatten `T1` to `T5`.

### High-confidence confirmations from `T5`

| T5 evidence span | T1 locus or loci | Result | Notes |
|---|---|---|---|
| visible opening run on `T5-p004` from `至道無難` through `遣有沒有 / 從空背空` | `T1-p007.l01` to `T1-p022.l01` plus supplied `T1-p021.l01a` | confirmed | direct image review shows that `T5` carries the same opening poem spine already recovered in `T1`, including the line supplied at the `T1-p021/T1-p022` gap |
| visible mid-band run on `T5-p005` from `多言多慮` through `無咎無法不生不心` | `T1-p024.l01` to `T1-p033.l01` where recovered | confirmed | `T5` independently supports the repaired sequence around `T1-p031.l03` and `T1-p032.l01`; no new alternative reading was exposed |
| visible later run on `T5-p005` and `T5-p006` from `不用求真` through `真如法界無他無自` | `T1-p037.l01` to `T1-p066.l01` where recovered | broadly confirmed | the witness supports the established late-band spine, including the already repaired `T1-p047.l01` and `T1-p065.l01`, but does not present a clearer new reading than the `T4` slice already used |
| visible close on `T5-p006` from `萬法一如` through `言語道斷 / 非去來今 / 信心不二 / 不二信心` and `信心銘之終` | `T1-p066.l01` to `T1-p079.l01` plus supplied `T1-p077.l01a` | broadly confirmed | `T5` supports the recovered closing spine from visible `T1-p076.l01` onward and the supplied corresponding line after `T1-p077.l01`, but it does not override the earlier omission judgment at `T1-p075` |

### New loci exposed by `T5`

- None at high confidence.
- `T5` serves as corroborative comparison support for the already recorded `T4`-driven repairs rather than as a source of fresh forced changes in this slice.

## `T2` confirmation slice

Date: 2026-04-15
Status: bounded confirmation pass completed
Scope: compare the isolated `T2-p003` to `T2-p005` body span against the current `T1` recovered lemma spine after `T2` reached full four-engine compliance

### Method note

- `T2` was not used before its full-pass `RapidOCR`, `tesseract`, `PaddleOCR PP-OCRv4`, and `EasyOCR` status block was recorded.
- Because the full-resolution rendered `T2` PNG pages were too large for stable PIL-based OCR loading on this workstation, all four engines used the explicitly logged `ocr/T2/ocr-input-120dpi/` derivative basis instead.
- Exact line claims were checked against direct image review of `T2-p003` to `T2-p005`; OCR was supporting evidence, not sole authority.
- Evidence basis: direct image review plus four-engine OCR support on the logged derivative basis.
- Evidence strength: strong for broad sequence confirmation, moderate for any exact OCR-led character rescue not already secured from earlier witnesses.

### High-confidence confirmations from `T2`

| T2 evidence span | T1 locus or loci | Result | Notes |
|---|---|---|---|
| visible opening run on `T2-p003` from `至道無難` through `遣有沒有 / 從空背空` | `T1-p007.l01` to `T1-p022.l01` plus supplied `T1-p021.l01a` | confirmed | direct image review shows that `T2` carries the same opening poem spine already recovered in `T1`, including the line supplied at the `T1-p021/T1-p022` gap |
| visible mid-band run on `T2-p004` from `多言多慮` through `無咎無法不生不心` | `T1-p024.l01` to `T1-p033.l01` where recovered | confirmed | `T2` independently supports the repaired sequence around `T1-p031.l03` and `T1-p032.l01`; no stronger alternative than the already logged `T4` repair emerged |
| visible later run on `T2-p004` and `T2-p005` from `不用求真` through `真如法界無他無自` | `T1-p037.l01` to `T1-p066.l01` where recovered | broadly confirmed | the witness supports the established late-band spine, including the already repaired `T1-p047.l01` and `T1-p065.l01`, but does not expose a cleaner new forced reading |
| visible close on `T2-p005` from `萬法一如` through `言語道斷 / 非去來今 / 信心不二 / 不二信心` and `信心銘之終` | `T1-p066.l01` to `T1-p079.l01` plus supplied `T1-p077.l01a` | broadly confirmed | `T2` supports the recovered closing spine from visible `T1-p076.l01` onward and the supplied corresponding line after `T1-p077.l01`, but it does not overturn the earlier omission judgment at `T1-p075` |

### New loci exposed by `T2`

- None at high confidence.
- `T2` serves as corroborative comparison support for the already recorded `T4`-driven repairs rather than as a source of fresh forced changes in this slice.

## `T3` confirmation slice

Date: 2026-04-15
Status: bounded confirmation pass completed
Scope: compare the isolated `T3-p034` to `T3-p036` body span against the current `T1` recovered lemma spine after `T3` reached full four-engine compliance

### Method note

- `T3` was not used before its full-pass `RapidOCR`, `tesseract`, `PaddleOCR PP-OCRv4`, and `EasyOCR` status block was recorded.
- `T3` is a late-body anthology witness rather than an opening-body one, so the actual comparison span was first isolated visually to `T3-p034` through `T3-p036`.
- Exact line claims were checked against direct image review of `RB00016909_00034.jpg` to `RB00016909_00036.jpg`; OCR was supporting evidence, not sole authority.
- Evidence basis: direct image review plus four-engine OCR support on the source-image basis.
- Evidence strength: strong for broad sequence confirmation and for the standard closing-line presence in `T3`; moderate for any claim that would insert a line back into `T1` against the visible `T1` page evidence.

### High-confidence confirmations from `T3`

| T3 evidence span | T1 locus or loci | Result | Notes |
|---|---|---|---|
| visible opening run on `T3-p034` from `至道無難` through `遣有沒有 / 從空背空` | `T1-p007.l01` to `T1-p022.l01` plus supplied `T1-p021.l01a` | confirmed | direct image review shows that `T3` carries the same opening poem spine already recovered in `T1`, including the supplied line at the `T1-p021/T1-p022` gap |
| visible mid-band run on `T3-p035` from `多言多慮` through `極大同小 / 不見邊表` | `T1-p024.l01` to `T1-p073.l01` where recovered | broadly confirmed | `T3` independently supports the repaired mid-band sequence and the already recovered later line-1 poem spine through the large/small polarity section |
| visible closing run on `T3-p036` from `有即是無 / 無即是有` through `言語道斷 / 非去來今` | `T1-p074.l01`, omission judgment at `T1-p075`, `T1-p076.l01`, `T1-p077.l01`, `T1-p077.l01a`, `T1-p078.l01`, and `T1-p079.l01` | confirmed with one branch-level note | `T3` directly preserves the standard close including `若不如此必不須守`, `若如是必不須守`, `一即一切一切即一`, `但能如是何慮不畢`, `信心不二不二信心`, and `言語道斷非去來今`; this strengthens the already logged judgment that `T1` omits the earlier standard line rather than preserving it visibly |

### New loci exposed by `T3`

- None at high confidence for fresh `T1` insertion or correction beyond the already logged omission judgment.
- `T3` functions as a strong direct poem corroborator and especially strengthens the already recorded `T1-p075` omission judgment without overturning the rule that `T1` itself must not be silently back-filled against its visible page evidence.

## Immediate use

- `T4` remains the decisive repair witness used so far.
- `T5`, `T2`, and `T3` now stand as corroborative comparison witnesses with full recorded four-engine OCR bases.
- The next full-pass witness target is `A1`, not more closure work on `T3`.

## `A1` confirmation slice

Date: 2026-04-16
Status: bounded confirmation pass completed
Scope: compare the poem-bearing `A1-p003` to `A1-p006` leaves, plus immediate post-close `A1-p007` to `A1-p008` end matter, against the current `T1` recovered lemma spine after `A1` reached full four-engine compliance

### Method note

- `A1` was not used before its full-pass `RapidOCR`, `tesseract`, `PaddleOCR PP-OCRv4`, and `EasyOCR` status block was recorded.
- `A1` is a Waseda PDF-derived anthology witness, so exact line claims were checked against direct image review of rendered `A1-p003` to `A1-p008`; OCR was supporting evidence, not sole authority.
- In practice, the poem-bearing comparison value is concentrated on `A1-p003` to `A1-p006`; `A1-p007` to `A1-p008` are immediate post-close or appended explanatory matter on the same target leaves rather than fresh poem-body support.
- Evidence basis: direct image review plus four-engine OCR support on the rendered page-image basis.
- Evidence strength: strong for broad sequence confirmation and for the standard closing-line presence in `A1`; moderate for any claim that would insert a line back into `T1` against the visible `T1` page evidence.

### High-confidence confirmations from `A1`

| A1 evidence span | T1 locus or loci | Result | Notes |
|---|---|---|---|
| visible opening run on `A1-p003` from `至道無難` through `止動歸止 / 止更彌動` | `T1-p007.l01` to `T1-p019.l01` where recovered | confirmed | direct image review shows that `A1` carries the same opening poem spine already recovered in `T1`, including the stable opening through the stop-return sequence |
| visible mid-band run on `A1-p004` from `唯滯兩邊` through `須臾返照 / 勝卻前空 / 前空轉變 / 皆由妄見` | `T1-p020.l01` to `T1-p029.l01` plus supplied `T1-p021.l01a` and repaired `T1-p027.l01` | confirmed | `A1` independently supports the supplied missing line `一種不通兩處失功`, the restored `須臾返照勝卻前空`, and the already recovered line sequence through the front half of the mid-band |
| visible later run on `A1-p004` and `A1-p005` from `二由一有 / 一亦莫守` through `法無異法 / 妄自愛著 / 將心用心 / 豈非大錯` and onward to `真如法界 / 無他無自` | `T1-p031.l03`, `T1-p032.l01`, `T1-p047.l01`, `T1-p065.l01`, and surrounding recovered loci through `T1-p066.l01` | broadly confirmed | `A1` independently supports the repaired `T1-p031/T1-p032` sequence and the already corrected late-band loci without exposing a cleaner new forced reading than the earlier `T4` slice |
| visible close on `A1-p006` from `真如法界 / 無他無自` through `若不如是必不須守 / 若如是必不須守 / 一即一切一切即一 / 但能如是何慮不畢 / 信心不二不二信心` | `T1-p066.l01` to `T1-p078.l01` plus supplied `T1-p077.l01a` and omission judgment at `T1-p075` | confirmed with one branch-level note | `A1` directly preserves the standard close including the omitted `若不如是必不須守` line before visible `若如是必不須守`, which further strengthens the already logged judgment that `T1` omits the earlier standard line rather than preserving it visibly |

### New loci exposed by `A1`

- None at high confidence for fresh `T1` insertion or correction beyond the already logged omission judgment.
- `A1` functions as a strong corroborative anthology witness and especially strengthens the already recorded `T1-p075` omission judgment without overturning the rule that `T1` itself must not be silently back-filled against its visible page evidence.

## Immediate use

- `T4` remains the decisive repair witness used so far.
- `T5`, `T2`, `T3`, and `A1` now stand as corroborative comparison witnesses with full recorded four-engine OCR bases.
- The next full-pass witness target is `A2`, not more closure work on `A1`.

## `A2` representative confirmation slice

Date: 2026-04-16
Status: bounded representative confirmation pass completed
Scope: compare representative poem-bearing and commentary-bearing `A2` leaves against the current `T1` recovered lemma spine after `A2` reached full four-engine compliance

### Method note

- `A2` was not used before its full-pass `RapidOCR`, `tesseract`, `PaddleOCR PP-OCRv4`, and `EasyOCR` status block was recorded.
- `A2` is a long derivative `四部録抄` witness rather than a short poem-only excerpt, so this first slice is representative rather than an exhaustive page-by-page closure of `A2-p002` to `A2-p044`.
- Exact claims were checked against direct image review of representative rendered leaves including `A2-p002`, `A2-p003`, `A2-p010`, `A2-p020`, `A2-p030`, and `A2-p038`; OCR was supporting evidence, not sole authority.
- Evidence basis: direct image review plus four-engine OCR support on the rendered page-image basis.
- Evidence strength: moderate for broad derivative corroboration of the recovered `T1` lemma spine; low for any attempt to force new exact character repairs from `A2` alone because the witness is commentary-heavy and its OCR is materially noisier than `T4`.

### Representative confirmations from `A2`

| A2 evidence span | T1 locus or loci | Result | Notes |
|---|---|---|---|
| visible opening run on `A2-p002` from `至道無難` through `但莫憎愛 / 洞然明白` | `T1-p007.l01` to `T1-p008.l01` where recovered | confirmed | the derivative witness clearly embeds the standard opening lemmata in commentary form and agrees with the recovered `T1` opening |
| visible early-band run on `A2-p003` from `毫釐有差 / 天地懸隔` through `一種不通 / 兩處失功` | `T1-p009.l01` to `T1-p021.l01a` where recovered | broadly confirmed | `A2` supports the early recovered sequence, including the already supplied `T1-p021.l01a`, but does not improve on the cleaner direct support already obtained from `T4` |
| visible mid-band and later-band representative lemmata on `A2-p010`, `A2-p020`, and `A2-p030` | representative recovered loci from the repaired mid-band through later commentary-supported sections of `T1` | broadly confirmed | the witness continues to preserve embedded poem lemmata inside derivative commentary across the body, showing that `A2` is aligned with the established recovered spine rather than exposing a rival branch at these checked points |
| visible later representative lemmata on `A2-p038` and nearby later leaves | later recovered `T1` lemma spine in the non-closing band | broadly confirmed | the inspected later leaves continue the same pattern: derivative commentary carrying recognizable poem lemmata without producing a new forced repair locus |

### New loci exposed by `A2`

- None at high confidence in this first representative slice.
- `A2` currently behaves like a corroborative derivative witness rather than a decisive repair witness.
- Because `A2` is long and commentary-heavy, this first slice should not be treated as exhaustive closure of the whole witness body; it is enough to show that the witness aligns broadly with the recovered `T1` spine and adds no fresh forced correction pressure at the inspected loci.

## Immediate use

- `T4` remains the decisive repair witness used so far.
- `T5`, `T2`, `T3`, `A1`, and now `A2` stand as corroborative comparison witnesses with full recorded four-engine OCR bases.
- The next full-pass witness target is `A3`, not more closure work on `A2` before the next witness is opened.

## `A3` representative confirmation slice

Date: 2026-04-16
Status: bounded representative confirmation pass completed
Scope: compare representative opening, body, and closing `A3` leaves against the current `T1` recovered lemma spine after `A3` reached full four-engine compliance

### Method note

- `A3` was not used before its full-pass `RapidOCR`, `tesseract`, `PaddleOCR PP-OCRv4`, and `EasyOCR` status block was recorded.
- `A3` is a derivative anthology witness rather than a short poem-only excerpt, so this first slice is representative rather than an exhaustive leaf-by-leaf closure of `A3-p003` to `A3-p011`.
- Direct page review had already established that the visible `Faith in Mind` close appears on `A3-p011`, while `A3-p012` has already moved into later anthology material.
- Exact OCR text on `A3` is materially noisier than on `T4`, `T5`, `T2`, `T3`, or `A1`, so evidence weight here is driven mainly by direct image review of representative leaves together with the saved four-engine OCR stack on the explicitly logged `ocr-input-120dpi/` derivative basis.
- Evidence basis: direct image review plus four-engine OCR support on the logged derivative basis.
- Evidence strength: moderate for broad derivative corroboration of the recovered `T1` lemma spine; low for any attempt to force new exact character repairs from `A3` alone.

### Representative confirmations from `A3`

| A3 evidence span | T1 locus or loci | Result | Notes |
|---|---|---|---|
| visible opening run beginning on `A3-p003` | opening recovered `T1` lemma spine | broadly confirmed | `A3` opens as a derivative witness carrying the standard opening rather than a rival branch, but the page is too noisy to treat as a cleaner repair surface than earlier witnesses |
| representative derivative body leaves within `A3-p004` to `A3-p010` | recovered `T1` body spine at inspected loci | broadly confirmed | inspected body leaves continue the same pattern seen in `A2`: recognizable poem lemmata embedded in derivative exposition without exposing a new forced correction beyond the already logged `T4`-supported set |
| visible close on `A3-p011`, where the target text ends before `A3-p012` turns to later anthology material | `T1-p076.l01` to `T1-p079.l01`, supplied `T1-p077.l01a`, and omission judgment at `T1-p075` | confirmed with one branch-level note | the visible close again supports the standard transmitted ending and strengthens the already logged judgment that `T1` omits the earlier standard closing line rather than preserving it visibly |

### New loci exposed by `A3`

- None at high confidence in this first representative slice.
- `A3` currently behaves like a corroborative derivative witness rather than a decisive repair witness.
- Its strongest immediate value is additional support for the already logged closing omission judgment at `T1-p075`, not a new exact repair to the `T1` working text.

## Immediate use

- `T4` remains the decisive repair witness used so far.
- `T5`, `T2`, `T3`, `A1`, `A2`, and now `A3` stand as corroborative comparison witnesses with full recorded four-engine OCR bases.
- The next full-pass witness target is `C1`, the first commentary or translation control, not more closure work on `A3` before the next witness is opened.

## `C1` translation-control confirmation slice

Date: 2026-04-16
Status: bounded translation-control comparison completed
Scope: compare the isolated `C1-p051` to `C1-p052` `信心銘和譯` span against the current `T1` recovered lemma spine after `C1` reached full four-engine compliance

### Method note

- `C1` was not used before its full-pass `RapidOCR`, `tesseract`, `PaddleOCR PP-OCRv4`, and `EasyOCR` status block was recorded.
- `C1` is a Japanese translation or reception control rather than a direct Chinese base-text witness, so evidence weight here comes primarily from direct image review of rendered `C1-p051` and `C1-p052`, with OCR used only as rough support.
- The witness presents `信心銘和譯` with embedded original-text anchors and explanatory Japanese reception framing, not as a clean standalone Chinese text for exact character rescue.
- Evidence basis: direct image review plus four-engine OCR support on the rendered page-image basis.
- Evidence strength: moderate for broad sequence confirmation and closing-order support; low for any attempt to force new exact Chinese character repairs from `C1`.

### High-confidence confirmations from `C1`

| C1 evidence span | T1 locus or loci | Result | Notes |
|---|---|---|---|
| visible opening and early-body run on `C1-p051` under the heading `信心銘和譯` | opening recovered `T1` lemma spine through the early and mid bands | broadly confirmed | the translation-control witness clearly tracks the standard opening sequence and major early poem turns in order, but it presents them in Japanese rendering rather than as a clean direct Chinese repair surface |
| visible continuation on `C1-p052` through the later body and close | later recovered `T1` lemma spine through `T1-p079.l01` | broadly confirmed | the witness continues the standard macro-sequence through the close, including the familiar ending movement rather than a rival branch |
| visible close on `C1-p052` including `信心不二 / 不二信心 / 言語道斷 / 非去來今` | `T1-p078.l01` and `T1-p079.l01` | confirmed | the close is clearly present in standard order inside the translation or reception framing, which supports the already recovered closing sequence in `T1` |

### New loci exposed by `C1`

- None at high confidence for fresh `T1` insertion or correction.
- `C1` currently behaves as a translation or reception control witness, not as a decisive repair witness.
- Its value in this first slice is confirming broad transmitted order and recognizable close structure, not supplying a cleaner Chinese reading than the earlier `T4`-driven repairs.

## Immediate use

- `T4` remains the decisive repair witness used so far.
- `T5`, `T2`, `T3`, `A1`, `A2`, `A3`, and now `C1` stand as corroborative comparison witnesses with full recorded OCR bases, but `C1` must be weighted as a translation or reception control rather than as a direct text witness.
- The next full-pass witness target is `C2`, the next translation or reception control, not more closure work on `C1` before the next witness is opened.

## `C2` translation-control confirmation slice

Date: 2026-04-17
Status: bounded translation-control comparison completed
Scope: compare the isolated `C2-p021` to `C2-p023` `三祖大師信心銘` span against the current `T1` recovered lemma spine after `C2` reached full four-engine compliance

### Method note

- `C2` was not used before its full-pass `RapidOCR`, `tesseract`, `PaddleOCR PP-OCRv4`, and `EasyOCR` status block was recorded.
- `C2` is a Japanese translation or reception control rather than a direct Chinese base-text witness, so evidence weight here comes primarily from direct image review of rendered `C2-p021` to `C2-p023`, with OCR used only as rough support.
- `C2-p021` and `C2-p023` are mixed-content boundary spreads: `C2-p021` opens `三祖大師信心銘` on the left page while the facing right page still carries section explanation, and `C2-p023` carries `三祖信心銘終` on the right page while the facing left page has already moved into `洞山悟本大師寶鏡三昧`.
- Evidence basis: direct image review plus four-engine OCR support on the rendered page-image basis.
- Evidence strength: moderate for broad sequence confirmation and closing-order support; low for any attempt to force new exact Chinese character repairs from `C2`.

### High-confidence confirmations from `C2`

| C2 evidence span | T1 locus or loci | Result | Notes |
|---|---|---|---|
| visible opening on the left page of `C2-p021` under the heading `三祖大師信心銘` | opening recovered `T1` lemma spine | broadly confirmed | the witness clearly opens with the standard `信心銘` frame rather than a rival branch, but does so inside Japanese reception formatting rather than as a clean standalone Chinese repair surface |
| visible continuation across `C2-p022` | recovered `T1` body spine through the main transmitted sequence | broadly confirmed | the control witness continues the standard macro-sequence through the body without exposing a new locus that pressures the already resolved `T4`-supported repairs |
| visible close on the right page of `C2-p023` with `三祖信心銘終` before the volume turns to the next item | recovered `T1` late band and close through `T1-p079.l01` | broadly confirmed | `C2` preserves the standard close and end marker structure inside reception framing, which supports broad transmitted order and close placement rather than exact character rescue |

### New loci exposed by `C2`

- None at high confidence for fresh `T1` insertion or correction.
- `C2` currently behaves as a translation or reception control witness, not as a decisive repair witness.
- Its value in this first slice is confirming broad transmitted sequence and standard close structure in a Japanese reception frame, not supplying a cleaner Chinese reading than the earlier `T4`-driven repairs.

## Immediate use

- `T4` remains the decisive repair witness used so far.
- `T5`, `T2`, `T3`, `A1`, `A2`, `A3`, `C1`, and now `C2` stand as corroborative comparison witnesses with full recorded OCR bases, but `C1` and `C2` must be weighted as translation or reception controls rather than as direct text witnesses.
- The next full-pass witness target is `C3`, unless the package queue is explicitly redirected.

## `C3` commentary-control confirmation slice

Date: 2026-04-17
Status: bounded commentary-control comparison completed
Scope: compare representative `C3` commentary-body surfaces against the current `T1` recovered lemma spine after `C3` reached full four-engine compliance

### Method note

- `C3` was not used before its full-pass `RapidOCR`, `tesseract`, `PaddleOCR PP-OCRv4`, and `EasyOCR` status block was recorded.
- `C3` is a dedicated commentary-control witness rather than a short direct poem witness, so this first slice is representative rather than a leaf-by-leaf closure of `C3-p004` to `C3-p056`.
- Direct page review shows that `C3-p004` is the title-opening page of `信心銘講話`, `C3-p005` visibly embeds the opening and early-body lemmata, representative mid-body leaves such as `C3-p020` and `C3-p040` carry commentary keyed to recognizable poem turns, and `C3-p056` closes the witness with `信心銘講了` before tail matter begins.
- Evidence basis: direct image review plus four-engine OCR support on the rendered page-image basis.
- Evidence strength: moderate for broad commentary-backed confirmation of the recovered `T1` lemma spine and the standard close; low for any attempt to force new exact character repairs from `C3` alone.

### Representative confirmations from `C3`

| C3 evidence span | T1 locus or loci | Result | Notes |
|---|---|---|---|
| title-opening and first body spread on `C3-p004` to `C3-p005` | opening recovered `T1` lemma spine from `T1-p007.l01` forward | broadly confirmed | `C3` presents `信心銘講話` as an explicit commentary witness and visibly carries the standard opening and early-body lemmata inside exposition rather than a rival opening branch |
| representative commentary body leaves such as `C3-p020` and `C3-p040` | recovered mid-band and later-band `T1` lemma spine at inspected loci | broadly confirmed | the witness remains commentary-heavy but continues to track recognizable poem lemmata in order, which supports the already recovered `T1` spine without exposing a cleaner repair surface than `T4` |
| visible close on `C3-p056` with `信心銘講了` before non-body tail matter | recovered late band and standard close through `T1-p079.l01` | broadly confirmed | the commentary witness closes against the standard transmitted ending and does not suggest a rival closing branch beyond the already logged omission judgment at `T1-p075` |

### New loci exposed by `C3`

- None at high confidence for fresh `T1` insertion or correction.
- `C3` currently behaves as a commentary control witness, not as a decisive repair witness.
- Its value in this first slice is broad commentary-backed confirmation of the recovered spine and standard close, not supplying a cleaner exact Chinese reading than the earlier `T4`-driven repairs.

## Immediate use

- `T4` remains the decisive repair witness used so far.
- `T5`, `T2`, `T3`, `A1`, `A2`, `A3`, `C1`, `C2`, and now `C3` stand as corroborative comparison witnesses with full recorded OCR bases, but `C1` and `C2` remain translation or reception controls and `C3` remains a commentary control rather than a direct repair witness.
- The next full-pass witness target is `C4`.

## `C4` commentary-control confirmation slice

Date: 2026-04-17
Status: bounded commentary-control comparison completed
Scope: compare representative `C4` commentary-body surfaces against the current `T1` recovered lemma spine after `C4` reached full four-engine compliance

### Method note

- `C4` was not used before its full-pass `RapidOCR`, `tesseract`, `PaddleOCR PP-OCRv4`, and `EasyOCR` status block was recorded.
- `C4` is a dedicated commentary-control witness rather than a short direct poem witness, so this first slice is representative rather than a leaf-by-leaf closure of `C4-p005` to `C4-p022`.
- Direct page review shows that `C4-p005` opens the main `信心銘拈提` body with embedded opening and early-body lemmata, representative mid-body leaves such as `C4-p015` continue commentary keyed to recognizable poem turns, `C4-p022` carries an explicit `信心銘拈提終` frame with the standard close still visible, and `C4-p023` is a mixed terminal spread with residual body on the right page and imprint or colophon matter on the left.
- Evidence basis: direct image review plus four-engine OCR support on the rendered page-image basis.
- Evidence strength: moderate for broad commentary-backed confirmation of the recovered `T1` lemma spine and standard close; low for any attempt to force new exact character repairs from `C4` alone.

### Representative confirmations from `C4`

| C4 evidence span | T1 locus or loci | Result | Notes |
|---|---|---|---|
| opening commentary spread on `C4-p005` | opening recovered `T1` lemma spine from `T1-p007.l01` forward | broadly confirmed | `C4` begins as explicit `信心銘拈提` commentary and visibly carries the standard opening and early-body lemmata inside exposition rather than a rival opening branch |
| representative commentary body such as `C4-p015` | recovered mid-band `T1` lemma spine at inspected loci | broadly confirmed | the witness remains commentary-heavy but continues to track recognizable poem lemmata in order, which supports the recovered `T1` spine without exposing a cleaner repair surface than `T4` |
| explicit closing frame on `C4-p022` and mixed terminal spread on `C4-p023` | recovered late band and standard close through `T1-p079.l01` | broadly confirmed | `C4-p022` shows `信心銘拈提終` together with the standard closing movement, and the mixed terminal `C4-p023` does not suggest a rival closing branch beyond the already logged omission judgment at `T1-p075` |

### New loci exposed by `C4`

- None at high confidence for fresh `T1` insertion or correction.
- `C4` currently behaves as a commentary control witness, not as a decisive repair witness.
- Its value in this first slice is broad commentary-backed confirmation of the recovered spine and standard close, not supplying a cleaner exact Chinese reading than the earlier `T4`-driven repairs.

## Immediate use

- `T4` remains the decisive repair witness used so far.
- `T5`, `T2`, `T3`, `A1`, `A2`, `A3`, `C1`, `C2`, `C3`, and now `C4` stand as corroborative comparison witnesses with full recorded OCR bases, but `C1` and `C2` remain translation or reception controls and `C3` plus `C4` remain commentary controls rather than direct repair witnesses.
- The next full-pass witness target is `C5`.

## `C5` commentary-control confirmation slice

Date: 2026-04-18
Status: bounded commentary-control comparison completed
Scope: compare representative `C5` commentary-body surfaces against the current `T1` recovered lemma spine after `C5` reached full four-engine compliance

### Method note

- `C5` was not used before its full-pass `RapidOCR`, `tesseract`, `PaddleOCR PP-OCRv4`, and `EasyOCR` status block was recorded.
- `C5` is a long commentary-control witness rather than a short direct poem witness, so this first slice is representative rather than a leaf-by-leaf closure of `C5-p004` to `C5-p072`.
- Direct page review shows that `C5-p004` opens the main `冠註信心銘夜塘水` body with embedded opening and early-body lemmata, representative mid-body leaves such as `C5-p040` continue commentary keyed to recognizable poem turns, `C5-p072` carries the late-body edge immediately before the terminal page, and `C5-p073` marks the end of `巻上`.
- Evidence basis: direct image review plus four-engine OCR support on the rendered page-image basis.
- Evidence strength: moderate for broad commentary-backed confirmation of the recovered `T1` lemma spine and macro-sequence; low for any attempt to force new exact character repairs from `C5` alone.

### Representative confirmations from `C5`

| C5 evidence span | T1 locus or loci | Result | Notes |
|---|---|---|---|
| opening commentary spread on `C5-p004` | opening recovered `T1` lemma spine from `T1-p007.l01` forward | broadly confirmed | `C5` begins as explicit `冠註信心銘夜塘水` commentary and visibly carries the standard opening and early-body lemmata inside exposition rather than a rival opening branch |
| representative commentary body such as `C5-p040` | recovered mid-band `T1` lemma spine at inspected loci | broadly confirmed | the witness remains commentary-heavy but continues to track recognizable poem lemmata in order, which supports the recovered `T1` spine without exposing a cleaner repair surface than `T4` |
| late-body edge on `C5-p072` and terminal page `C5-p073` marked as the end of `巻上` | recovered later body through the late-band approach to the close | broadly confirmed at the volume level | `C5` preserves the later transmitted sequence up to the end of this `巻上` volume and does not suggest a rival branch, but the surviving terminal page functions mainly as volume-end evidence rather than a cleaner direct close witness than the shorter controls |

### New loci exposed by `C5`

- None at high confidence for fresh `T1` insertion or correction.
- `C5` currently behaves as a commentary control witness, not as a decisive repair witness.
- Its value in this first slice is broad commentary-backed confirmation of the recovered spine across a long commentary body, not supplying a cleaner exact Chinese reading than the earlier `T4`-driven repairs.

## Immediate use

- `T4` remains the decisive repair witness used so far.
- `T5`, `T2`, `T3`, `A1`, `A2`, `A3`, `C1`, `C2`, `C3`, `C4`, and now `C5` stand as corroborative comparison witnesses with full recorded OCR bases, but `C1` and `C2` remain translation or reception controls and `C3` to `C5` remain commentary controls rather than direct repair witnesses.
- The next full-pass witness target is `C6`.

## `C6` commentary-control confirmation slice

Date: 2026-04-19
Status: bounded commentary-control comparison completed
Scope: compare representative `C6` commentary-body surfaces against the current `T1` recovered lemma spine after `C6` reached full four-engine compliance

### Method note

- `C6` was not used before its full-pass `RapidOCR`, `tesseract`, `PaddleOCR PP-OCRv4`, and repaired `EasyOCR` status block was recorded.
- `C6` is a long commentary-control witness and the natural `巻下` continuation of the same `冠註信心銘夜塘水` tradition represented by `C5`, so this first slice is representative rather than a leaf-by-leaf closure of `C6-p002` to `C6-p058`.
- Direct page review shows that `C6-p001` is a mixed title-plus-opening spread, `C6-p002` carries the active opening commentary body keyed to recognizable poem lemmata, representative mid-body leaves such as `C6-p030` continue commentary keyed to the transmitted poem sequence, `C6-p058` remains active late commentary body, and `C6-p059` is a mixed terminal body-plus-colophon spread.
- Evidence basis: direct image review plus four-engine OCR support on the rendered page-image basis.
- Evidence strength: moderate for broad commentary-backed confirmation of the recovered `T1` lemma spine and transmitted macro-sequence; low for any attempt to force new exact character repairs from `C6` alone.

### Representative confirmations from `C6`

| C6 evidence span | T1 locus or loci | Result | Notes |
|---|---|---|---|
| mixed opening on `C6-p001` and first stable commentary body on `C6-p002` | opening recovered `T1` lemma spine from `T1-p007.l01` forward | broadly confirmed | `C6` opens as explicit `冠註信心銘夜塘水` `巻下` commentary and continues to carry recognizable opening and early-body lemmata inside exposition rather than a rival opening branch |
| representative commentary body such as `C6-p030` | recovered mid-band `T1` lemma spine at inspected loci | broadly confirmed | the witness remains commentary-heavy but continues to track recognizable poem lemmata in order, which supports the recovered `T1` spine without exposing a cleaner repair surface than `T4` |
| late commentary body on `C6-p058` and mixed terminal spread on `C6-p059` | recovered later body and terminal macro-sequence | broadly confirmed at the volume level | `C6` preserves the later transmitted sequence through the end of this commentary volume and does not suggest a rival branch; the terminal spread functions mainly as volume-end evidence rather than as a cleaner direct close witness than the shorter controls |

### New loci exposed by `C6`

- None at high confidence for fresh `T1` insertion or correction.
- `C6` currently behaves as a commentary control witness, not as a decisive repair witness.
- Its value in this first slice is broad commentary-backed confirmation across the `巻下` continuation of the `夜塘水` tradition, not supplying a cleaner exact Chinese reading than the earlier `T4`-driven repairs.

## Immediate use

- `T4` remains the decisive repair witness used so far.
- `T5`, `T2`, `T3`, `A1`, `A2`, `A3`, `C1`, `C2`, and `C3` to `C6` stand as corroborative comparison witnesses with full recorded OCR bases, but `C1` and `C2` remain translation or reception controls and `C3` to `C6` remain commentary controls rather than direct repair witnesses.
- The next full-pass witness target is `C7`.

## `C7` commentary-control confirmation slice

Date: 2026-04-19
Status: bounded commentary-control comparison completed
Scope: compare representative `C7` commentary-body surfaces against the current `T1` recovered lemma spine after `C7` reached full four-engine compliance

### Method note

- `C7` was not used before its full-pass `RapidOCR`, `tesseract`, `PaddleOCR PP-OCRv4`, and `EasyOCR` status block was recorded.
- `C7` is a Kyoto commentary-control witness rather than a short direct poem witness, so this first slice is representative rather than a leaf-by-leaf closure of `C7-p006` to `C7-p043`.
- Direct page review already shows wrapper or title matter on `C7-p001` to `C7-p003`, front matter on `C7-p004` to `C7-p005`, the main commentary body beginning on `C7-p006`, representative body confirmation on leaves such as `C7-p010`, continued later-body support on `C7-p042` to `C7-p043`, and publication tail beginning on `C7-p044`.
- Evidence basis: direct image review plus four-engine OCR support on the direct Kyoto image basis.
- Evidence strength: moderate for broad commentary-backed confirmation of the recovered `T1` lemma spine and transmitted macro-sequence; low for any attempt to force new exact character repairs from `C7` alone.

### Representative confirmations from `C7`

| C7 evidence span | T1 locus or loci | Result | Notes |
|---|---|---|---|
| opening commentary body on `C7-p006` | opening recovered `T1` lemma spine from `T1-p007.l01` forward | broadly confirmed | `C7` opens as a commentary witness keyed to recognizable opening lemmata rather than a rival opening branch |
| representative commentary body such as `C7-p010` | recovered early and mid-band `T1` lemma spine at inspected loci | broadly confirmed | the witness remains commentary-heavy but continues to track recognizable poem lemmata in order, supporting the recovered `T1` spine without offering a cleaner repair surface than `T4` |
| late commentary body on `C7-p042` to `C7-p043` before publication matter begins on `C7-p044` | recovered later body and terminal macro-sequence | broadly confirmed at the volume level | `C7` preserves the later transmitted sequence through the end of its commentary body and does not suggest a rival branch or fresh repair pressure beyond the already resolved `T4`-supported set |

### New loci exposed by `C7`

- None at high confidence for fresh `T1` insertion or correction.
- `C7` currently behaves as a commentary control witness, not as a decisive repair witness.
- Its value in this first slice is broad Kyoto commentary-backed confirmation of the recovered spine and transmitted macro-sequence, not supplying a cleaner exact Chinese reading than the earlier `T4`-driven repairs.

## Immediate use

- `T4` remains the decisive repair witness used so far.
- `T5`, `T2`, `T3`, `A1`, `A2`, `A3`, `C1`, `C2`, and `C3` to `C7` stand as corroborative comparison witnesses with full recorded OCR bases, but `C1` and `C2` remain translation or reception controls and `C3` to `C7` remain commentary controls rather than direct repair witnesses.
- The next full-pass witness target is `C8`.

## `C8` commentary-control confirmation slice

Date: 2026-04-19
Status: bounded commentary-control comparison completed
Scope: compare representative `C8` commentary-body surfaces against the current `T1` recovered lemma spine after `C8` reached full four-engine compliance

### Method note

- `C8` was not used before its full-pass `RapidOCR`, `tesseract`, `PaddleOCR PP-OCRv4`, and `EasyOCR` status block was recorded.
- `C8` is an NDL commentary-control witness rather than a short direct poem witness, so this first slice is representative rather than a leaf-by-leaf closure of `C8-p003` to `C8-p029`.
- Direct page review already shows title matter on `C8-p001` to `C8-p002`, the main commentary body beginning on `C8-p003`, stable representative body support on leaves such as `C8-p004`, later-body support on `C8-p029`, and a mixed explicit closing page on `C8-p030` with `信心銘拈提終` plus publication matter.
- Evidence basis: direct image review plus four-engine OCR support on the rendered page-image basis.
- Evidence strength: moderate for broad commentary-backed confirmation of the recovered `T1` lemma spine and transmitted macro-sequence; low for any attempt to force new exact character repairs from `C8` alone.

### Representative confirmations from `C8`

| C8 evidence span | T1 locus or loci | Result | Notes |
|---|---|---|---|
| opening commentary body on `C8-p003` | opening recovered `T1` lemma spine from `T1-p007.l01` forward | broadly confirmed | `C8` opens as a commentary witness keyed to recognizable opening lemmata rather than a rival opening branch |
| representative commentary body such as `C8-p004` and the continuing body run through the middle leaves | recovered early and mid-band `T1` lemma spine at inspected loci | broadly confirmed | the witness remains commentary-heavy but continues to track recognizable poem lemmata in order, supporting the recovered `T1` spine without offering a cleaner repair surface than `T4` |
| later-body support on `C8-p029` and mixed explicit close on `C8-p030` | recovered later body and terminal macro-sequence | broadly confirmed | `C8-p030` explicitly marks `信心銘拈提終` while still carrying the closing commentary frame, which supports the transmitted end structure without introducing a rival branch or fresh repair pressure |

### New loci exposed by `C8`

- None at high confidence for fresh `T1` insertion or correction.
- `C8` currently behaves as a commentary control witness, not as a decisive repair witness.
- Its value in this first slice is broad NDL commentary-backed confirmation of the recovered spine and transmitted macro-sequence, not supplying a cleaner exact Chinese reading than the earlier `T4`-driven repairs.

## Immediate use

- `T4` remains the decisive repair witness used so far.
- `T5`, `T2`, `T3`, `A1`, `A2`, `A3`, `C1`, `C2`, and `C3` to `C8` stand as corroborative comparison witnesses with full recorded OCR bases, but `C1` and `C2` remain translation or reception controls and `C3` to `C8` remain commentary controls rather than direct repair witnesses.
- The next full-pass witness target is `C9`.

## `C9` commentary-control confirmation slice

Date: 2026-04-19
Status: bounded commentary-control comparison completed
Scope: compare representative `C9` commentary-body surfaces against the current `T1` recovered lemma spine after `C9` reached full four-engine compliance

### Method note

- `C9` was not used before its full-pass `RapidOCR`, `tesseract`, `PaddleOCR PP-OCRv4`, and `EasyOCR` status block was recorded.
- `C9` is a long NDL commentary-control witness rather than a short direct poem witness, so this first slice is representative rather than a leaf-by-leaf closure of `C9-p003` to `C9-p074`.
- Direct page review already shows title matter on `C9-p001` to `C9-p002`, the main commentary body beginning on `C9-p003`, representative mid-body support on leaves such as `C9-p020` and `C9-p040`, later-body support on `C9-p074`, and tail or wrapper matter on `C9-p075` to `C9-p076`.
- Evidence basis: direct image review plus four-engine OCR support on the rendered page-image basis.
- Evidence strength: moderate for broad commentary-backed confirmation of the recovered `T1` lemma spine and transmitted macro-sequence; low for any attempt to force new exact character repairs from `C9` alone.

### Representative confirmations from `C9`

| C9 evidence span | T1 locus or loci | Result | Notes |
|---|---|---|---|
| opening commentary body on `C9-p003` | opening recovered `T1` lemma spine from `T1-p007.l01` forward | broadly confirmed | `C9` opens as a commentary witness keyed to recognizable opening lemmata rather than a rival opening branch |
| representative commentary body such as `C9-p020` and `C9-p040` | recovered early and mid-band `T1` lemma spine at inspected loci | broadly confirmed | the witness remains commentary-heavy but continues to track recognizable poem lemmata in order, supporting the recovered `T1` spine without offering a cleaner repair surface than `T4` |
| later-body support on `C9-p074` before tail or wrapper matter on `C9-p075` to `C9-p076` | recovered later body and terminal macro-sequence | broadly confirmed at the volume level | `C9` preserves the transmitted later sequence through the end of its commentary body and does not suggest a rival branch or fresh repair pressure beyond the already resolved `T4`-supported set |

### New loci exposed by `C9`

- None at high confidence for fresh `T1` insertion or correction.
- `C9` currently behaves as a commentary control witness, not as a decisive repair witness.
- Its value in this first slice is broad NDL commentary-backed confirmation of the recovered spine and transmitted macro-sequence, not supplying a cleaner exact Chinese reading than the earlier `T4`-driven repairs.

## Immediate use

- `T4` remains the decisive repair witness used so far.
- `T5`, `T2`, `T3`, `A1`, `A2`, `A3`, `C1`, `C2`, and `C3` to `C9` stand as corroborative comparison witnesses with full recorded OCR bases, but `C1` and `C2` remain translation or reception controls and `C3` to `C9` remain commentary controls rather than direct repair witnesses.
- The next full-pass witness target is `C10`.

## `C10` commentary-control confirmation slice

Date: 2026-04-20
Status: bounded commentary-control comparison completed
Scope: compare representative `C10` commentary-body surfaces against the current `T1` recovered lemma spine after `C10` reached full four-engine compliance

### Method note

- `C10` was not used before its full-pass `RapidOCR`, `tesseract`, `PaddleOCR PP-OCRv4`, and `EasyOCR` status block was recorded.
- `C10` is a long NDL commentary-control witness rather than a short direct poem witness, so this first slice is representative rather than a leaf-by-leaf closure of `C10-p003` to `C10-p062`.
- Direct page review already shows title matter on `C10-p001` to `C10-p002`, the main `巻下` commentary body beginning on `C10-p003`, representative mid-body support on leaves such as `C10-p020` and `C10-p040`, later-body support on `C10-p062`, and terminal colophon or imprint matter on `C10-p063` before blank or wrapper tail matter on `C10-p064` to `C10-p065`.
- Evidence basis: direct image review plus four-engine OCR support on the rendered page-image basis.
- Evidence strength: moderate for broad commentary-backed confirmation of the recovered `T1` lemma spine and transmitted macro-sequence; low for any attempt to force new exact character repairs from `C10` alone.

### Representative confirmations from `C10`

| C10 evidence span | T1 locus or loci | Result | Notes |
|---|---|---|---|
| opening commentary body on `C10-p003` | opening recovered `T1` lemma spine from `T1-p007.l01` forward | broadly confirmed | `C10` opens as a `巻下` commentary witness keyed to recognizable opening lemmata rather than a rival opening branch |
| representative commentary body such as `C10-p020` and `C10-p040` | recovered early and mid-band `T1` lemma spine at inspected loci | broadly confirmed | the witness remains commentary-heavy but continues to track recognizable poem lemmata in order, supporting the recovered `T1` spine without offering a cleaner repair surface than `T4` |
| later-body support on `C10-p062` before terminal colophon or imprint matter on `C10-p063` | recovered later body and terminal macro-sequence | broadly confirmed at the volume level | `C10` preserves the transmitted later sequence through the end of its commentary body and does not suggest a rival branch or fresh repair pressure beyond the already resolved `T4`-supported set |

### New loci exposed by `C10`

- None at high confidence for fresh `T1` insertion or correction.
- `C10` currently behaves as a commentary control witness, not as a decisive repair witness.
- Its value in this first slice is broad NDL commentary-backed confirmation of the recovered spine and transmitted macro-sequence, not supplying a cleaner exact Chinese reading than the earlier `T4`-driven repairs.

## Immediate use

- `T4` remains the decisive repair witness used so far.
- `T5`, `T2`, `T3`, `A1`, `A2`, `A3`, `C1`, `C2`, and `C3` to `C10` stand as corroborative comparison witnesses with full recorded OCR bases, but `C1` and `C2` remain translation or reception controls and `C3` to `C10` remain commentary controls rather than direct repair witnesses.
- The next full-pass witness target is `C11`.

## `C11` lecture-commentary-control confirmation slice

Date: 2026-04-21
Status: bounded lecture-commentary-control comparison completed
Scope: compare representative `C11` lecture-body surfaces against the current `T1` recovered lemma spine after `C11` reached full four-engine compliance

### Method note

- `C11` was not used before its full-pass `RapidOCR`, `tesseract`, `PaddleOCR PP-OCRv4`, and `EasyOCR` status block was recorded.
- `C11` is part 1 of a long lecture witness (`信心銘夜塘水講義`), not a short direct poem witness, so this first slice is representative and part-volume bounded rather than a full terminal-text collation.
- Direct page review shows prefatory/title matter on `C11-p001` to `C11-p003`, active lecture commentary beginning on `C11-p004`, opening-lemma discussion surfacing around `C11-p018` to `C11-p021`, and the central `一心不生 / 萬法` discussion around `C11-p072` to `C11-p074`.
- Evidence basis: direct image review plus four-engine OCR support, with the usable anchor layer coming mainly from `PaddleOCR PP-OCRv4` derived text because the other engines are substantially noisier on this lecture witness.
- Evidence strength: moderate for broad lecture-backed confirmation of opening and central recovered `T1` lemma sequence; low for forcing exact new character repairs or terminal-branch judgments from `C11` part 1 alone.

### Representative confirmations from `C11`

| C11 evidence span | T1 locus or loci | Result | Notes |
|---|---|---|---|
| opening lecture body and lemma discussion around `C11-p018` to `C11-p021` | opening recovered `T1` lemma spine from `T1-p007.l01` through the early `但莫憎愛 / 洞然明白` band | broadly confirmed | OCR anchors include recognizably corrupted but usable `至道...`, `但莫增爱`, and `洞然明白`; direct image review confirms these pages are part of the lecture discussion rather than unrelated tail matter |
| continuing lecture body through representative mid-volume pages | recovered early-to-middle `T1` lemma spine at inspected loci | broadly confirmed at witness-role level | `C11` is commentary/lecture-heavy and does not provide a clean substitute transcription surface, but it remains keyed to the same transmitted poem sequence |
| central lecture discussion around `C11-p072` to `C11-p074` | `T1-p032` sequence and the `一心不生萬法無咎` band | broadly confirmed | Paddle-derived text gives repeated anchors for `一心不生`, `萬法`, and near forms of `萬法無咎`; this supports the already repaired `T1-p032` region but does not independently improve the reading |

### New loci exposed by `C11`

- None at high confidence for fresh `T1` insertion or correction.
- `C11` currently behaves as a lecture commentary control witness, not as a decisive repair witness.
- Because `C11` is part 1 of a lecture pair, it is not used here for a complete terminal-close judgment; that role should wait for `C12` if the continuation reaches the relevant closing band.

## Immediate use

- `T4` remains the decisive repair witness used so far.
- `T5`, `T2`, `T3`, `A1`, `A2`, `A3`, `C1`, `C2`, and `C3` to `C11` stand as corroborative comparison witnesses with full recorded OCR bases, but `C1` and `C2` remain translation or reception controls and `C3` to `C11` remain commentary or lecture controls rather than direct repair witnesses.
- The next full-pass witness target is `C12`.

## `C12` lecture-commentary-control confirmation slice

Date: 2026-04-21
Status: bounded lecture-commentary-control comparison completed
Scope: compare representative `C12` lecture-body surfaces against the current `T1` recovered lemma spine after `C12` reached full four-engine compliance

### Method note

- `C12` was not used before its full-pass `RapidOCR`, `tesseract`, `PaddleOCR PP-OCRv4`, and `EasyOCR` status block was recorded.
- `C12` is part 2 of the long lecture witness (`信心銘夜塘水講義`), not a short direct poem witness, so this slice is a lecture-commentary control comparison rather than a clean alternate transcription.
- Direct page review confirms a central one-mind/all-dharmas discussion around `C12-p024`, the late/close branch around `C12-p073`, continued terminal-close discussion around `C12-p077`, and repeated terminal `信心不二 / 不二信心` surfaces around `C12-p079` to `C12-p081`.
- Evidence basis: direct image review plus four-engine OCR support, with the usable anchor layer coming mainly from `PaddleOCR PP-OCRv4` derived text because the other engines are substantially noisier on this lecture witness.
- Evidence strength: moderate for broad lecture-backed confirmation of the terminal macro-sequence and the already supplied close locus; low for forcing exact new character repairs or overriding direct `T1` page judgments from `C12` alone.

### Representative confirmations from `C12`

| C12 evidence span | T1 locus or loci | Result | Notes |
|---|---|---|---|
| central lecture discussion around `C12-p024` | `T1-p032` sequence and the `一心不生萬法無咎` band | broadly confirmed | OCR anchors and direct image review show repeated one-mind/all-dharmas discussion; this supports the already repaired central band but does not independently improve the reading |
| late branch around `C12-p073` | standard omitted-line problem around `T1-p075` to `T1-p076` | branch support only | direct image review supports the lecture tradition's `若不如是` and `必不須守` branch, but `C12` remains a lecture-control witness and does not overturn the direct `T1` rollback judgment at `T1-p075` |
| terminal close discussion around `C12-p077` to `C12-p078` | supplied `T1-p077.l01a` close line `但能如是何慮不畢` | broadly confirmed | OCR anchors include the `但能如是` area and direct image review confirms the terminal discussion context; this strengthens the already supplied `T4`-backed close rather than creating a new independent correction |
| repeated terminal surfaces around `C12-p079` to `C12-p081` | `T1-p078.l01` and `T1-p079.l01` close sequence | broadly confirmed | direct image review and OCR search locate `信心不二` / `不二信心` surfaces and the terminal discussion sequence; no rival close branch or fresh repair pressure appears |

### New loci exposed by `C12`

- None at high confidence for fresh `T1` insertion or correction.
- `C12` strengthens external lecture-tradition support for the standard omitted close branch and for the already supplied terminal locus, but it does not create an accepted `T1` text change.
- `C12` currently behaves as a lecture commentary control witness, not as a decisive repair witness.

## Immediate use

- `T4` remains the decisive repair witness used so far.
- `T5`, `T2`, `T3`, `A1`, `A2`, `A3`, `C1`, `C2`, and `C3` to `C12` stand as corroborative comparison witnesses with full recorded OCR bases, but `C1` and `C2` remain translation or reception controls and `C3` to `C12` remain commentary or lecture controls rather than direct repair witnesses.
- The next witness-opening target is `C13`.

## `C13` commentary-control confirmation slice

Date: 2026-04-22
Status: bounded commentary-control comparison completed
Scope: compare representative `C13` body and quoted-lemma surfaces against the current `T1` recovered lemma spine after `C13` reached full four-engine compliance

### Method note

- `C13` was not used before its full-pass `RapidOCR`, `tesseract`, `PaddleOCR PP-OCRv4`, and `EasyOCR` status block was recorded.
- `C13` is part 1 of `通俗信心銘講話`, not a short direct poem witness, so this slice is commentary-control evidence rather than a substitute transcription.
- Direct page review confirms a mixed title/opening-lemma surface on `C13-p002`, an early quoted terminal-anchor surface on `C13-p004`, and central one-mind/all-dharmas discussion around `C13-p074`, with `C13-p054` and `C13-p097` as additional supportive body surfaces.
- OCR evidence was used only as support after image review; `RapidOCR` gives a useful opening anchor on `C13-p002`, while `PaddleOCR PP-OCRv4` supplies the clearest machine anchors on `C13-p004` and `C13-p074`.
- Evidence strength: moderate for broad commentary-backed confirmation of opening, central, and quoted terminal macro-sequence; low for forcing exact new character repairs or treating the early quoted terminal phrases as a physical terminal-close collation.

### Representative confirmations from `C13`

| C13 evidence span | T1 locus or loci | Result | Notes |
|---|---|---|---|
| mixed title/opening body on `C13-p002` | opening recovered `T1` lemma spine from `T1-p007.l01` through the early `但莫憎愛 / 洞然明白` band | broadly confirmed | direct image review shows embedded opening lines including `至道無難`, `唯嫌揀擇`, `但莫憎愛`, and `洞然明白`; RapidOCR independently anchors the opening with a corrupted but recognizable `至道無` line on this page |
| central body discussion around `C13-p074`, with support from `C13-p054` and `C13-p097` | `T1-p032.l01` and the central one-mind/all-dharmas band | broadly confirmed | direct image review and Paddle-derived text locate the one-mind/all-dharmas relation, including near forms of `一心即萬法` and `萬法即一心`; this supports the already repaired central band without improving it |
| early quoted terminal-anchor surface on `C13-p004` | terminal `T1-p077.l01a` to `T1-p079.l01` close sequence | quoted-anchor support only | direct image review shows terminal phrases quoted in an early commentary frame, including `言語道斷`, `非去來今`, `信心不二`, and `不二信心`; because the page is an early expository or overview surface, it is not treated as a physical terminal-close witness |

### New loci exposed by `C13`

- None at high confidence for fresh `T1` insertion or correction.
- `C13` currently behaves as a commentary control witness, not as a decisive repair witness.
- The early terminal phrase cluster on `C13-p004` strengthens reception/commentary support for the standard close, but it does not create a new accepted `T1` text change.

## Immediate use

- `T4` remains the decisive repair witness used so far.
- `T5`, `T2`, `T3`, `A1`, `A2`, `A3`, `C1`, `C2`, and `C3` to `C13` stand as corroborative comparison witnesses with full recorded OCR bases, but `C1` and `C2` remain translation or reception controls and `C3` to `C13` remain commentary or lecture controls rather than direct repair witnesses.
- The next witness-opening target is `C14`.
