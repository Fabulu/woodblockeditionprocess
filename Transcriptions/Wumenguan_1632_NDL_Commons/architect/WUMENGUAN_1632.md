# 無門關

## Source

- Witness: `Wumenguan_1632_NDL_Commons`
- PDF: `NDL12865429_wumenguan_1juan.pdf`
- Page count: 57
- Current state: scan-derived witness draft and leaf-level evidence log

## Method

- PDF pages rendered locally with PyMuPDF
- Tesseract 5.5.0 installed locally
- Chinese OCR models added locally in workspace:
  - `chi_tra`
  - `chi_sim`
  - `chi_tra_vert`
  - `chi_sim_vert`
- Independent image-reading agents used as cross-checkers
- Full witness leaf OCR pass completed under `batch_refined/`

## Witness Leaves

### PDF p.006 left leaf

- Role: 目錄 leaf
- Confidence: medium

#### Consolidated Readable Text

```text
目錄

å¤§é“ç„¡é–€
åƒå·®æœ‰è·¯
é€å¾—æ­¤é—œ
ä¹¾å¤ç¨æ­¥

佛祖機緣
å››åå…«å‰‡

è¶™å·žç‹—å­
å€¶èƒè±ŽæŒ‡
香嚴上樹
ç™¾ä¸ˆé‡Žç‹
èƒ¡å­ç„¡é¬š
世尊拈花
```

#### Notes

- This is only a partial recovery of the visible contents entries.
- `å€¶èƒè±ŽæŒ‡` is now the working reading.
- More contents entries are visible on the leaf and should be recovered in a dedicated pass.

### PDF p.007 left leaf

- Role: contents continuation
- Confidence: medium

#### Consolidated Readable Text

```text
ä¸æ€å–„æƒ¡
三座說法
ä¸æ˜¯å¿ƒä½›
éžé¢¨éžå¹¡
趙州勘婆
éžå¿ƒéžä½›
倩女離魂
åº­å‰æŸæ¨¹

é›¢å´èªžè¨€
äºŒåƒ§å·ç°¾
ä¹…éŸ¿é¾æ½­
å³å¿ƒå³ä½›
å¤–é“å•ä½›
æ™ºä¸æ˜¯é“
è·¯é€¢é”é“
ç‰›éŽçª“æ«º
```

#### Notes

- This leaf is a clean enough witness continuation of the contents list.
- `倩女離魂` is now adopted as the working reading.
- `ä¹…éŸ¿é¾æ½­` and `ç‰›éŽçª“æ«º` are supported by both the image and the stronger OCR comparators.

### PDF p.008 right leaf

- Role: contents ending
- Confidence: medium

#### Consolidated Readable Text

```text
目錄終

雲門話墮
é”ç£¨å®‰å¿ƒ
首山竹篦
他是阿誰
兜率三關

趯倒淨瓶
å¥³å­å‡ºå®š
èŠ­è•‰æ‹„æ–
竿頭進步
乾峰一路
```

#### Notes

- The leaf heading `目錄終` is clear in the witness.
- `趯倒淨瓶` and `乾峰一路` are supported by the image, though the first graph of `趯倒` is not especially dark.
- `PaddleOCR` helped on this leaf by segmenting the vertical lines more cleanly than `tesseract`.

### PDF p.006 right leaf

- Role: opening prose / prefatory explanation
- Confidence: medium

#### Consolidated Readable Text

```text
ä½œæ•²é–€ç“¦å­ï¼Œéš¨æ©Ÿå¼•å°Žå­¸è€…ï¼Œç«Ÿçˆ¾æŠ„éŒ„ï¼Œä¸è¦ºæˆé›†ã€‚
åˆä¸ä»¥å‰å¾Œæ•˜åˆ—ï¼Œå…±æˆå››åå…«å‰‡ï¼Œé€šæ›°ç„¡é–€é—œã€‚
è‹¥æ˜¯ç®‡æ¼¢ï¼Œå–®åˆ€ç›´å…¥ï¼Œå…«è‡‚é‚£å’ï¼Œæ“±ä»–ä¸ä½ã€‚
ç¸±ä½¿è¥¿å¤©å››ä¸ƒï¼Œæ±åœŸäºŒä¸‰ï¼Œåªå¾—æœ›é¢¨ä¹žå‘½ã€‚
è¨­æˆ–èºŠèº‡ï¼Œä¹Ÿä¼¼éš”çª—çœ‹é¦¬é¨Žï¼Œè²¶å¾—çœ¼ä¾†ï¼Œæ—©å·²è¹‰éŽã€‚
```

#### Notes

- `學者` is a consolidation choice from image-based comparison only.
- The opening phrase `ä½œæ•²é–€ç“¦å­` is supported by direct image reading.
- `單刀直入` is now resolved from the witness.
- OCR output was substantially weaker than the image-reading agents, so OCR is comparator-only here.

### PDF p.011 left leaf

- Role: commentary and verse on `ç™¾ä¸ˆé‡Žç‹`
- Confidence: high

#### Consolidated Readable Text

```text
無門曰：
ä¸è½å› æžœï¼Œç‚ºç”šå¢®é‡Žç‹ï¼Ÿ
ä¸æ˜§å› æžœï¼Œç‚ºç”šè„«é‡Žç‹ï¼Ÿ
è‹¥å‘è€…è£è‘—å¾—ä¸€éš»çœ¼ï¼Œ
ä¾¿çŸ¥å¾—å‰ç™¾ä¸ˆè´å¾—é¢¨æµäº”ç™¾ç”Ÿã€‚

頌曰
ä¸è½ä¸æ˜§ï¼Œ
兩采一賽。
ä¸æ˜§ä¸è½ï¼Œ
åƒéŒ¯è¬éŒ¯ã€‚
```

#### Notes

- The key doctrinal pair `ä¸è½å› æžœ / ä¸æ˜§å› æžœ` is very clear in the witness.
- The verse is stable and visually well supported.

### PDF p.009 left leaf

- Role: continuation of `è¶™å·žç‹—å­`
- Confidence: medium

#### Consolidated Readable Text

```text
å¦‚åžäº†ç®‡ç†±éµä¸¸ï¼Œç›¸ä¼¼ååˆåä¸å‡ºã€‚
è•©ç›¡å¾žå‰æƒ¡çŸ¥æƒ¡è¦ºï¼Œä¹…ä¹…ç´”ç†Ÿã€‚
è‡ªç„¶å…§å¤–æ‰“æˆä¸€ç‰‡ï¼Œå¦‚å•žå­å¾—å¤¢ï¼Œåªè¨±è‡ªçŸ¥ã€‚
驀然打發，驚天動地。
å¦‚å¥ªå¾—é—œå°‡è»å¤§åˆ€å…¥æ‰‹ï¼Œ
逢佛殺佛，逢祖殺祖。
於生死岸頭得大自在，
å‘å…­é“å››ç”Ÿä¸­éŠæˆ²ä¸‰æ˜§ã€‚
ä¸”ä½œéº¼ç”Ÿææ’•ã€‚
盡平生氣力，舉箇無字。
è‹¥ä¸é–“æ–·ï¼Œ
好似法燭一點便著。
```

#### Notes

- This leaf is readable enough to continue the opening `è¶™å·žç‹—å­` instructions in a coherent block.
- `PaddleOCR` was especially helpful on the lines beginning `è•©ç›¡å¾žå‰` and `è‡ªç„¶å…§å¤–`.
- A few punctuation choices remain editorial, but the underlying witness text is stable enough for this draft.

### PDF p.009 right leaf

- Role: opening prose on `è¶™å·žç‹—å­`
- Confidence: medium

#### Consolidated Readable Text

```text
å¸«é—œåªè€…ä¸€ç®‡ç„¡å­—ï¼Œä¹ƒå®—é–€ä¸€é—œä¹Ÿã€‚
é‚ç›®ä¹‹æ›°ç¦ªå®—ç„¡é–€é—œã€‚
é€å¾—éŽè€…ï¼Œéžä½†è¦ªè¦‹è¶™å·žï¼Œ
ä¾¿å¯èˆ‡æ­·ä»£ç¥–å¸«æŠŠæ‰‹å…±è¡Œï¼Œ
çœ‰æ¯›å»çµï¼ŒåŒä¸€çœ¼è¦‹ï¼ŒåŒä¸€è€³èžã€‚
è±ˆä¸æ…¶å¿«ã€‚
èŽ«æœ‰è¦é€é—œåº•éº¼ã€‚
å°‡ä¸‰ç™¾å…­åéª¨ç¯€ã€å…«è¬å››åƒæ¯«ç«…ï¼Œ
é€šèº«èµ·ç®‡ç–‘åœ˜ï¼Œåƒç®‡ç„¡å­—ã€‚
æ™å¤œææ’•ï¼ŒèŽ«ä½œè™›ç„¡æœƒï¼Œ
莫作有無會。
```

#### Notes

- This leaf is substantially clearer with `RapidOCR` and `PaddleOCR` as comparators than with `tesseract` alone.
- A few particles remain too faint to claim more than medium confidence, but the core prose block is secure from the witness.

### PDF p.010 right leaf

- Role: end of `è¶™å·žç‹—å­` verse and opening of `ç™¾ä¸ˆé‡Žç‹`
- Confidence: medium-high

#### Consolidated Readable Text

```text
ç‹—å­ä½›æ€§
å…¨ææ­£ä»¤
纔涉有無
喪身失命

ã€”ç™¾ä¸ˆé‡Žç‹ã€•

ç™¾ä¸ˆå’Œå°šï¼Œå‡¡åƒæ¬¡ï¼Œ
æœ‰ä¸€è€äººå¸¸éš¨çœ¾è½æ³•ã€‚
çœ¾äººé€€ï¼Œè€äººäº¦é€€ã€‚
å¿½ä¸€æ—¥ä¸é€€ã€‚
å¸«é‚å•ï¼š
é¢å‰ç«‹è€…å¾©æ˜¯ä½•äººã€‚
è€äººäº‘ï¼šè«¾ï¼ŒæŸç”²éžäººä¹Ÿã€‚
```

#### Notes

- The case boundary is clear: the verse ending `è¶™å·žç‹—å­` is followed by the opening of `ç™¾ä¸ˆé‡Žç‹`.
- The prose opening of `ç™¾ä¸ˆé‡Žç‹` is strong through `é¢å‰ç«‹è€…å¾©æ˜¯ä½•äºº`; the old manâ€™s reply begins on the leaf but is not fully secure from this page alone.
- `PaddleOCR` gave the cleanest support on the verse and opening prose lines here.
- Third-witness corroboration:
  - `Transcriptions\Mumonkan_1752_Waseda_Commons\batch_refined\frames\page_013_left_frame.png`
  - `Transcriptions\Mumonkan_1752_Waseda_Commons\batch_refined\frames\page_013_right_frame.png`
  - independently support the same `ä¸è½å› æžœ / ä¸æ˜§å› æžœ / äº”ç™¾ç”Ÿ / é‡Žç‹` cluster in the surrounding `ç™¾ä¸ˆé‡Žç‹` material

### PDF p.010 left leaf

- Role: continuation of `ç™¾ä¸ˆé‡Žç‹`
- Confidence: medium

#### Consolidated Readable Text

```text
è€äººäº‘ï¼š
è«¾ï¼ŒæŸç”²éžäººä¹Ÿã€‚
æ–¼éŽåŽ»è¿¦è‘‰ä½›æ™‚ï¼Œæ›¾ä½æ­¤å±±ã€‚
å› å­¸äººå•ï¼š
å¤§ä¿®è¡Œåº•äººï¼Œé‚„è½å› æžœä¹Ÿç„¡ã€‚
æŸç”²å°äº‘ï¼šä¸è½å› æžœã€‚
äº”ç™¾ç”Ÿå¢®é‡Žç‹èº«ã€‚
ä»Šè«‹å’Œå°šä»£ä¸€è½‰èªžï¼Œè²´è„«é‡Žç‹ã€‚
é‚å•ï¼š
å¤§ä¿®è¡Œåº•äººï¼Œé‚„è½å› æžœä¹Ÿç„¡ã€‚
å¸«äº‘ï¼šä¸æ˜§å› æžœã€‚
è€äººæ–¼è¨€ä¸‹å¤§æ‚Ÿã€‚
作禮云：
æŸç”²å·²è„«é‡Žç‹èº«ï¼Œä½åœ¨å±±å¾Œã€‚
æ•¢å‘Šå’Œå°šï¼Œä¹žä¾äº¡åƒ§äº‹ä¾‹ã€‚
師令維那白槌告眾。
```

#### Notes

- The witness strongly supports the doctrinal pair `ä¸è½å› æžœ / ä¸æ˜§å› æžœ`.
- The final action phrase beginning `師令維那...` continues onto the next leaf and remains incomplete here.
- `RapidOCR` and `PaddleOCR` both materially outperformed `tesseract` on this leaf.

### PDF p.012 right leaf

- Role: prose on `ä¿±èƒè±ŽæŒ‡`
- Confidence: high

#### Consolidated Readable Text

```text
ã€”ä¿±èƒè±ŽæŒ‡ã€•

ä¿±èƒå’Œå°šï¼Œå‡¡æœ‰è©°å•ï¼Œå”¯è±Žä¸€æŒ‡ã€‚
å¾Œæœ‰ç«¥å­ï¼Œå› å¤–äººå•å’Œå°šèªªä½•æ³•è¦ï¼Œ
ç«¥å­äº¦è±ŽæŒ‡é ­ã€‚
èƒèžï¼Œé‚ä»¥åˆ€æ–·å…¶æŒ‡ã€‚
ç«¥å­è² ç—›è™Ÿå“­è€ŒåŽ»ã€‚
èƒå¾©å¬ä¹‹ã€‚
ç«¥å­å›žé¦–ã€‚
èƒå»è±Žèµ·æŒ‡ã€‚
ç«¥å­å¿½ç„¶é ˜æ‚Ÿã€‚

èƒå°‡é †ä¸–ï¼Œè¬‚çœ¾æ›°ï¼š
å¾å¾—å¤©é¾ä¸€æŒ‡é ­ç¦ªï¼Œ
ä¸€ç”Ÿå—ç”¨ä¸ç›¡ã€‚
言訖示滅。
```

#### Notes

- The witness graph on the contents leaf may look like `å …æŒ‡`, but this body leaf supports `ä¿±èƒè±ŽæŒ‡`.
- This page is one of the clearest prose leaves in the current sample set.

### PDF p.011 right leaf

- Role: later prose on `ç™¾ä¸ˆé‡Žç‹`
- Confidence: medium

#### Consolidated Readable Text

```text
〔師令維那白槌告眾：〕
é£Ÿå¾Œé€äº¡åƒ§ã€‚
大眾言議：
ä¸€çœ¾çš†å®‰æ¶…æ§ƒå ‚ï¼Œåˆç„¡äººç—…ï¼Œä½•æ•…å¦‚æ˜¯ã€‚
é£Ÿå¾Œåªè¦‹å¸«é ˜çœ¾è‡³å±±å¾Œå·–ä¸‹ï¼Œ
ä»¥æ–æŒ‘å‡ºä¸€æ­»é‡Žç‹ï¼Œä¹ƒä¾ç«è‘¬ã€‚
å¸«è‡³æ™šä¸Šå ‚ï¼Œèˆ‰å‰å› ç·£ã€‚
é»ƒè˜—ä¾¿å•ï¼š
å¤äººéŒ¯ç¥‡å°ä¸€è½‰èªžï¼Œ
å¢®äº”ç™¾ç”Ÿé‡Žç‹èº«ã€‚
è½‰è½‰ä¸éŒ¯ï¼Œåˆä½œç®‡ç”šéº¼ã€‚
å¸«äº‘ï¼šè¿‘å‰ä¾†èˆ‡ä¼Šé“ã€‚
é»ƒè˜—é‚è¿‘å‰èˆ‡å¸«ä¸€æŽŒã€‚
å¸«æ‹æ‰‹ç¬‘äº‘ï¼šå°‡è¬‚èƒ¡é¬šèµ¤ï¼Œæ›´æœ‰èµ¤é¬šèƒ¡ã€‚
```

#### Notes

- `PaddleOCR` failed on this leaf with a runtime exception, but `RapidOCR`, `tesseract`, and the image itself were enough to recover the main prose block.
- The final line after `å¸«æ‹æ‰‹ç¬‘äº‘` is present but not yet secure enough from this leaf alone for a clean witness-only reading.

### PDF p.012 left leaf

- Role: commentary on `ä¿±èƒè±ŽæŒ‡`, verse, and opening of `èƒ¡å­ç„¡é¬š`
- Confidence: medium-high

#### Consolidated Readable Text

```text
無門曰：
ä¿±èƒå¹¶ç«¥å­æ‚Ÿè™•ï¼Œä¸åœ¨æŒ‡é ­ä¸Šã€‚
è‹¥å‘è€…è£è¦‹å¾—ï¼Œ
å¤©é¾åŒä¿±èƒå¹¶ç«¥å­ï¼Œ
èˆ‡è‡ªå·±ä¸€ä¸²ç©¿å´ã€‚

頌曰
ä¿±èƒéˆç½®è€å¤©é¾ï¼Œ
åˆ©åˆƒå–®æå‹˜å°ç«¥ã€‚
å·¨éˆæ“¡æ‰‹ç„¡å¤šå­ï¼Œ
åˆ†ç ´è¯å±±åƒè¬é‡ã€‚

ã€”èƒ¡å­ç„¡é¬šã€•
```

#### Notes

- The verse is strongly supported by both the image and the stronger OCR comparators.
- The title `èƒ¡å­ç„¡é¬š` is clear enough to mark the next case boundary confidently.
- `PaddleOCR` was the cleanest OCR comparator on this leaf.

### PDF p.013 right leaf

- Role: commentary and verse on `èƒ¡å­ç„¡é¬š`, with opening of `é¦™åš´ä¸Šæ¨¹`
- Confidence: medium

#### Consolidated Readable Text

```text
ã€”èƒ¡å­ç„¡é¬šã€•

或庵曰：
è¥¿å¤©èƒ¡å­ï¼Œå› ç”šç„¡é¬šã€‚

無門曰：
åƒé ˆå¯¦åƒï¼Œæ‚Ÿé ˆå¯¦æ‚Ÿã€‚
è€…ç®‡èƒ¡å­ï¼Œç›´é ˆè¦ªè¦‹ä¸€å›žï¼Œå§‹å¾—ã€‚
èªªè¦ªè¦‹ï¼Œæ—©æˆå…©ç®‡ã€‚

頌曰
ç™¡äººé¢å‰ï¼Œ
ä¸å¯èªªå¤¢ã€‚
èƒ¡å­ç„¡é¬šï¼Œ
惺惺添懵。

〔香嚴上樹〕
```

#### Notes

- The page is faint but the case identity and the main prose/verse structure are recoverable from the image.
- `RapidOCR` was more useful here than `tesseract`.
- The verse reading is scan-supported but still not as secure as the clearer early leaves.

### PDF p.013 left leaf

- Role: prose on `香嚴上樹`
- Confidence: medium

#### Consolidated Readable Text

```text
香嚴和尚云：
å¦‚äººä¸Šæ¨¹ï¼Œå£éŠœæ¨¹æžï¼Œæ‰‹ä¸æ”€æžï¼Œè„šä¸è¸æ¨¹ã€‚
æ¨¹ä¸‹æœ‰äººå•è¥¿ä¾†æ„ï¼Œ
ä¸å°ï¼Œå³é•ä»–æ‰€å•ï¼›
è‹¥å°ï¼Œåˆå–ªèº«å¤±å‘½ã€‚
æ­£ç•¶æéº¼æ™‚ï¼Œä½œéº¼ç”Ÿå°ã€‚

無門曰：
ç¸±æœ‰æ‡¸æ²³ä¹‹è¾¨ï¼Œç¸½ç”¨ä¸è‘—ã€‚
èªªå¾—ä¸€å¤§è—æ•™ï¼Œäº¦ç”¨ä¸è‘—ã€‚
è‹¥å‘è€…è£å°å¾—è‘—ï¼Œ
æ´»å´å¾žå‰æ­»è·¯é ­ï¼Œ
æ­»å´å¾žå‰æ´»è·¯é ­ã€‚
å…¶æˆ–æœªç„¶ï¼Œç›´å¾…ç•¶ä¾†å•å½Œå‹’ã€‚
```

#### Notes

- This leaf is structurally clear and the core prose block is well supported by the witness.
- A few punctuation choices are editorial, but the wording is stable enough for the scan-derived draft.

### PDF p.014 right leaf

- Role: verse on `香嚴上樹`, with opening of `世尊拈花`
- Confidence: medium

#### Consolidated Readable Text

```text
頌曰
é¦™åš´çœŸæœæ’°ï¼Œ
æƒ¡æ¯’ç„¡ç›¡é™ã€‚
å•žå´ç´åƒ§å£ï¼Œ
通身迸鬼眼。

〔世尊拈花〕

ä¸–å°Šæ˜”åœ¨éˆå±±æœƒä¸Šï¼Œæ‹ˆèŠ±ç¤ºçœ¾ã€‚
是時眾皆默然，
æƒŸè¿¦è‘‰å°Šè€…ç ´é¡å¾®ç¬‘ã€‚
```

#### Notes

- The `香嚴上樹` verse is supported by the page image, though the second half of the leaf is less dark than ideal.
- The opening of `世尊拈花` is clear enough to mark the next case boundary with confidence.

### PDF p.014 left leaf

- Role: commentary on `世尊拈花`
- Confidence: medium

#### Consolidated Readable Text

```text
無門曰：
é»ƒé¢çž¿æ›‡ï¼Œå‚è‹¥ç„¡äººï¼Œ
壓良為賤，懸羊頭賣狗肉。
將謂多少奇特。

åªå¦‚ç•¶æ™‚å¤§çœ¾éƒ½ç¬‘ï¼Œ
æ­£æ³•çœ¼è—ï¼Œä½œéº¼ç”Ÿå‚³ã€‚
è¨­ä½¿è¿¦è‘‰ä¸ç¬‘ï¼Œ
æ­£æ³•çœ¼è—åˆä½œéº¼ç”Ÿå‚³ã€‚
è‹¥é“æ­£æ³•çœ¼è—æœ‰å‚³ï¼Œ
é»ƒé¢è€å­ï¼Œèª‘è¬¼é–­é–»ã€‚
è‹¥é“ç„¡å‚³ï¼Œ
ç‚ºç”šéº¼ç¨è¨±è¿¦è‘‰ã€‚
```

#### Notes

- This page is readable at the line level, but the last third is not dark enough to claim every graph cleanly.
- `誑謼閭閻` is now favored from the witness image plus OCR comparison, but still not high-confidence enough to remove all caution.
- `RapidOCR` was more stable than `tesseract` here; `PaddleOCR` timed out on this leaf batch.

### PDF p.015 right leaf

- Role: end of one case and beginning of the next
- Confidence: medium-high

#### Consolidated Readable Text

```text
〔世尊拈花〕

å‚³æŽˆç‚ºç”šéº¼ï¼Œç¨è¨±è¿¦è‘‰ã€‚

頌曰
拈起花來，
è¿¦è‘‰ç ´é¡ã€‚
尾巴已露，
人天罔措。

〔趙州洗鉢〕

è¶™å·žå› åƒ§å•ï¼š
å…¶ç”²ä¹å…¥å¢æž—ï¼Œä¹žå¸«æŒ‡ç¤ºã€‚
州云：喫粥了也未？
僧云：喫粥了也。
州云：洗鉢盂去。
å…¶åƒ§æœ‰çœã€‚
```

#### Notes

- This leaf clearly spans a case boundary: the verse of `世尊拈花` and the prose opening of `趙州洗鉢`.
- `傳授為甚麼` is better supported than the earlier weaker reading.
- The phrase `å…¶ç”²ä¹å…¥å¢æž—` remains somewhat odd at the graph level, but the witness image supports it closely enough to retain for now.

### PDF p.015 left leaf

- Role: commentary and verse on `趙州洗鉢`
- Confidence: high

#### Consolidated Readable Text

```text
無門曰：
è¶™å·žé–‹å£ï¼Œè¦‹è†½éœ²å¿ƒè‚ã€‚
é€™åƒ§è½äº‹ä¸çœŸï¼Œå–šé˜ä½œç”•ã€‚

頌曰
åªçˆ²åˆ†æ˜Žæ¥µï¼Œ
ç¿»ä»¤æ‰€å¾—é²ã€‚
æ—©çŸ¥ç‡ˆæ˜¯ç«ï¼Œ
飯熟已多時。

〔奚仲造車〕

æœˆåºµå’Œå°šå•åƒ§ï¼š
奚仲造車，一百輻，
æ‹ˆå´å…©é ­ï¼ŒåŽ»å´è»¸ï¼Œ
明甚麼邊事。
```

#### Notes

- The page image supports this reading strongly.
- One or two graphs are faint in the witness, but the line-level reading is stable.
- `è¦‹è†½éœ²å¿ƒè‚` is better supported than the earlier shorter reading.
- This leaf also clearly opens the next case `奚仲造車`.

### PDF p.016 right leaf

- Role: case-boundary leaf; end of one case and opening of `å¤§é€šæ™ºå‹`
- Confidence: medium-high

#### Consolidated Readable Text

```text
無門曰：
若出直下明得，
çœ¼ä¼¼æµæ˜Ÿï¼Œ
機如掣電。

頌曰
機輪轉處，
é”è€…çŒ¶è¿·ã€‚
四維上下，
å—åŒ—æ±è¥¿ã€‚

ã€”å¤§é€šæ™ºå‹ã€•

èˆˆé™½è®“å’Œå°šå› åƒ§å•ï¼š
å¤§é€šæ™ºå‹ä½›ï¼ŒååŠ«åé“å ´ï¼Œ
ä½›æ³•ä¸ç¾å‰ï¼Œä¸å¾—æˆä½›é“ã€‚
```

#### Notes

- This leaf clearly spans a boundary between a preceding commentary / verse and the opening prose of `å¤§é€šæ™ºå‹`.
- The opening `å¤§é€šæ™ºå‹ä½›ï¼ŒååŠ«åé“å ´` line is secure from the witness.

### PDF p.016 left leaf

- Role: continuation of `å¤§é€šæ™ºå‹`
- Confidence: medium

#### Consolidated Readable Text

```text
時如何。
讓曰：
å…¶å•ç”šè«¦ã€‚
當僧云：
æ—¢æ˜¯åé“å ´ï¼Œ
çˆ²ç”šéº¼ä¸å¾—æˆä½›é“ã€‚

無門曰：
åªè¨±è€èƒ¡çŸ¥ï¼Œ
ä¸è¨±è€èƒ¡æœƒã€‚
å‡¡å¤«è‹¥çŸ¥ï¼Œå³æ˜¯è–äººã€‚
è–äººè‹¥æœƒï¼Œå³æ˜¯å‡¡å¤«ã€‚

頌曰
了身何似了心休，
äº†å¾—å¿ƒå…®èº«ä¸æ„ã€‚
若也身心俱了了，
ç¥žä»™ä½•å¿…æ›´å°ä¾¯ã€‚
```

#### Notes

- This leaf is less dark than the surrounding pages, but the prose/verse structure is still recoverable.
- The final verse is supported by the image and `RapidOCR`, though not at the same confidence level as the clearest early leaves.

### PDF p.017 right leaf

- Role: end of `å¤§é€šæ™ºå‹`, with opening of `æ¸…ç¨…å­¤è²§`
- Confidence: medium

#### Consolidated Readable Text

```text
〔頌曰〕
了身何似了心休，
äº†å¾—å¿ƒå…®èº«ä¸æ„ã€‚
若也身心俱了了，
ç¥žä»™ä½•å¿…æ›´å°ä¾¯ã€‚

〔清稅孤貧〕

æ›¹å±±å’Œå°šå› åƒ§å•äº‘ï¼š
清稅孤貧，乞師賑濟。
山云：
ç¨…é—æ¢¨ï¼Œé’åŽŸç™½å®¶é…’ï¼Œ
ä¸‰ç›žå–«äº†ï¼ŒçŒ¶é“æœªæ²¾å”‡ã€‚
```

#### Notes

- The verse ending of `å¤§é€šæ™ºå‹` is clear enough to carry forward from the previous leaf.
- The opening of `清稅孤貧` is readable, though a few graphs in the case prose remain slightly soft.
- `RapidOCR` materially helped on the `清稅孤貧` lines.

### PDF p.017 left leaf

- Role: opening prose on `州勘庵主`
- Confidence: medium

#### Consolidated Readable Text

```text
〔州勘庵主〕

è¶™å·žåˆ°ä¸€åºµä¸»è™•å•ï¼š
有麼有麼。
主竪起拳頭。
州云：
æ°´æ·ºä¸æ˜¯æ³Šèˆ¹è™•ã€‚
便行。

åˆåˆ°ä¸€åºµä¸»è™•äº‘ï¼š
有麼有麼。
主亦竪起拳頭。
州云：
能縱能奪，能殺能活。
便作禮。

頌曰
çœ¼æµæ˜Ÿï¼Œ
機掣電。
殺人刀，
æ´»äººåŠã€‚
```

#### Notes

- This leaf mixes the end of `清稅孤貧` material with the opening of `州勘庵主`, but the `州勘庵主` prose block is structurally clear.
- The exact phrasing of the first short exchange remains only medium-confidence from the witness.

### PDF p.018 right leaf

- Role: commentary on `州勘庵主`, with opening of `巖喚主人`
- Confidence: medium

#### Consolidated Readable Text

```text
無門曰：
一般竪起拳頭，
çˆ²ç”šéº¼è‚¯ä¸€ç®‡ï¼Œä¸è‚¯ä¸€ç®‡ã€‚
ä¸”é“ï¼Œç—…åœ¨ç”šè™•ã€‚
è‹¥å‘è€…è£ä¸‹å¾—ä¸€è½‰èªžï¼Œ
便見趙州舌頭無骨，
扶起放倒，得大自在。
然雖如是，
è¶™å·žå´è¢«äºŒåºµä¸»å‹˜ç ´ã€‚

〔巖喚主人〕
起拳頭，
別云：
能縱能奪，能殺能活，便作禮。
```

#### Notes

- The `州勘庵主` commentary is recoverable in substance, but still not graph-perfect.
- The opening of the next case is visible, though the first graph cluster after `起` is not yet secure.

### PDF p.018 left leaf

- Role: verse block around `州勘庵主` / `巖喚主人`
- Confidence: low-medium

#### Consolidated Readable Text

```text
çœ¼è‹¥é“ç„¡å„ªåŠ£ï¼Œäº¦æœªå…·åƒå­¸çœ¼ã€‚

頌曰
çœ¼æµæ˜Ÿï¼Œ
機掣電。
殺人刀，
æ´»äººåŠã€‚

ç‘žå·–å’Œå°šæ¯è‡ªå–šä¸»äººå…¬ï¼Œ
復自應諾。
乃云：
惺惺著。
他時異日，
èŽ«å—äººçžžã€‚
```

#### Notes

- This leaf is the weakest of the block.
- The carry-over line `çœ¼è‹¥é“ç„¡å„ªåŠ£ï¼Œäº¦æœªå…·åƒå­¸çœ¼ã€‚` is visible at the top margin and belongs to the preceding commentary.
- The `çœ¼æµæ˜Ÿ / æ©ŸæŽ£é›» / æ®ºäººåˆ€ / æ´»äººåŠ` lines are clear.
- The opening `ç‘žå·–å’Œå°šæ¯è‡ªå–šä¸»äººå…¬` lines are readable in substance, but the transition from the preceding verse is still too weak to normalize fully.

### PDF p.019 right leaf

- Role: commentary on `巖喚主人`
- Confidence: medium

#### Consolidated Readable Text

```text
無門曰：
ç‘žå·–è€å­ï¼Œè‡ªè²·è‡ªè³£ï¼Œå¼„å‡ºè¨±å¤šç¥žé ­é¬¼é¢ã€‚
何故。
一箇喚底，一箇應底；
ä¸€ç®‡æƒºæƒºåº•ï¼Œä¸€ç®‡ä¸å—äººçžžåº•ã€‚
èªè‘—ä¾å‰é‚„ä¸æ˜¯ã€‚
若也你擬他，
ç¸½æ˜¯é‡Žç‹è¦‹è§£ã€‚

頌曰
å­¸é“ä¹‹äººä¸è­˜çœŸï¼Œ
åªç‚ºå¾žå‰èªè­˜ç¥žã€‚
ç„¡é‡åŠ«ä¾†ç”Ÿæ­»æœ¬ï¼Œ
癡人喚作本來人。
```

#### Notes

- The prose/verse structure is clear from the witness.
- Several short phrases were tightened from the image with `RapidOCR`, but this leaf still sits at medium confidence overall.

### PDF p.019 left leaf

- Role: opening of `德山托鉢`
- Confidence: medium

#### Consolidated Readable Text

```text
〔德山托鉢〕

德山一日托鉢下堂。
è¦‹é›ªå³°å•è€…ï¼Œè€æ¼¢é˜æœªé³´ã€é¼“æœªéŸ¿ï¼Œ
æ‰˜é‰¢å‘ç”šè™•åŽ»ã€‚
山便回方丈。

峰舉似巖頭。
頭云：
å¤§å°å¾·å±±ï¼Œæœªæœƒæœ«å¾Œå¥ã€‚

å±±èžï¼Œä»¤ä¾è€…å–šå·–é ­ä¾†å•æ›°ï¼š
æ±ä¸è‚¯è€åƒ§é‚£ã€‚
```

#### Notes

- The opening exchange is structurally clear and matches the visual page layout.
- The closing rebuke line begins clearly but continues onto the next leaf.

### PDF p.020 right leaf

- Role: continuation and commentary on `德山托鉢`
- Confidence: medium

#### Consolidated Readable Text

```text
å·–é ­å¯†å•“å…¶æ„ã€‚
山乃休去。
æ˜Žæ—¥é™žåº§ï¼Œæžœèˆ‡å°‹å¸¸ä¸åŒã€‚
å·–é ­è‡³åƒ§å ‚å‰ï¼Œæ‹ŠæŽŒå¤§ç¬‘äº‘ï¼š
ä¸”å–œè€æ¼¢æœƒæœ«å¾Œå¥ã€‚

ä»–å¾Œå¤©ä¸‹äººä¸å¥ˆä¼Šä½•ã€‚

無門曰：
è‹¥æ˜¯æœªå¾Œå¥ï¼Œ
å·–é ­ã€å¾·å±±ä¿±æœªå¤¢è¦‹åœ¨ã€‚
檢點將來，好似一棚傀儡。
```

#### Notes

- The `德山托鉢` continuation is readable in substance, though the middle of the commentary remains slightly soft.
- `æœƒæœ«å¾Œå¥` is secure from the witness and is the key phrase on this leaf.

### PDF p.020 left leaf

- Role: verse on `å¾·å±±æ‰˜é‰¢`, with opening of `å—æ³‰æ–¬çŒ«`
- Confidence: medium

#### Consolidated Readable Text

```text
頌曰
è­˜å¾—æœ€åˆå¥ï¼Œ
ä¾¿æœƒæœ«å¾Œå¥ã€‚
æœ«å¾Œèˆ‡æœ€åˆï¼Œ
ä¸æ˜¯è€…ä¸€å¥ã€‚

ã€”å—æ³‰æ–¬çŒ«ã€•

å—æ³‰å’Œå°šå› æ±è¥¿å…©å ‚çˆ­çŒ«å…’ã€‚
æ³‰ä¹ƒæèµ·äº‘ï¼š
å¤§çœ¾é“å¾—å³æ•‘ï¼Œ
é“ä¸å¾—å³æ–¬å´ä¹Ÿã€‚
çœ¾ç„¡å°ã€‚
æ³‰é‚æ–¬ä¹‹ã€‚

趙州外歸，
泉舉似州。
州乃脱鞋，
安頭上而出。
```

#### Notes

- The verse and the opening of `å—æ³‰æ–¬çŒ«` are both secure enough for the witness draft.
- The phrase `æ±è¥¿å…©å ‚çˆ­çŒ«å…’` is visually strong and anchors the case identity.

### PDF p.017 right leaf

- Role: end of `å¤§é€šæ™ºå‹` verse and opening of `æ¸…ç¨…å­¤è²§`
- Confidence: medium

#### Consolidated Readable Text

```text
縱若也身心俱了了，
ç¥žä»™ä½•å¿…æ›´å°ä¾¯ã€‚

〔清稅孤貧〕

æ›¹å±±å’Œå°šå› åƒ§å•äº‘ï¼š
清稅孤貧，乞師賑濟。
山云：
ç¨…é—æ¢¨ï¼Œé’åŽŸç™½å®¶é…’ï¼Œ
ä¸‰ç›žå–«äº†ï¼ŒçŒ¶é“æœªæ²¾å”‡ã€‚
```

#### Notes

- The case boundary is clear in the witness.
- The `清稅孤貧` prose block is readable enough to carry into the draft without importing outside text.
- `RapidOCR` helped confirm `é’åŽŸç™½å®¶é…’ / ä¸‰ç›žå–«äº† / çŒ¶é“æœªæ²¾å”‡`.

### PDF p.017 left leaf

- Role: verse on `清稅孤貧`, with opening of `州勘庵主`
- Confidence: medium

#### Consolidated Readable Text

```text
頌曰
貧似范丹，
氣如項羽。
活計雖無，
敢與鬪富。

〔州勘庵主〕

è¶™å·žåˆ°ä¸€åºµä¸»è™•å•ï¼š
有麼有麼。
主豎起拳頭。
州云：
æ°´æ·ºä¸æ˜¯æ³ŠèˆŸè™•ã€‚
便行。
åˆåˆ°ä¸€åºµä¸»è™•äº‘ï¼š
有麼有麼。
主亦豎起拳頭。
```

#### Notes

- The verse is faint but readable from the image.
- `范丹 / 項羽 / 鬪富` are visually supported.
- This leaf clearly begins the `州勘庵主` case, though the prose continues on the next page.

### PDF p.018 right leaf

- Role: continuation and commentary on `州勘庵主`
- Confidence: medium

#### Consolidated Readable Text

```text
州云：
能縱能奪，
能殺能活，
便作禮。

無門曰：
一般豎起拳頭，
çˆ²ç”šéº¼è‚¯ä¸€ç®‡ï¼Œä¸è‚¯ä¸€ç®‡ã€‚
ä¸”é“ï¼Œè¨›åœ¨ç”šè™•ã€‚
è‹¥å‘è€…è£ä¸‹å¾—ä¸€è½‰èªžï¼Œ
便見趙州舌頭無骨，
扶起放倒，
得大自在。
然雖如是，
çˆ­å¥ˆè¶™å·žå´è¢«äºŒåºµä¸»å‹˜ç ´ã€‚
```

#### Notes

- The opening prose line `能縱能奪，能殺能活` is clear enough from the witness.
- `無門曰` and the main commentary block are well supported, though not at high confidence.

### PDF p.018 left leaf

- Role: verse on `州勘庵主`, with opening of `巖喚主人`
- Confidence: medium

#### Consolidated Readable Text

```text
頌曰
çœ¼æµæ˜Ÿï¼Œ
機掣電。
殺人刀，
æ´»äººåŠã€‚

〔巖喚主人〕

ç‘žå·–å’Œå°šï¼Œæ¯æ—¥è‡ªå–šä¸»äººå…¬ï¼Œ
復自應諾。
惺惺著。
他時異日，
èŽ«å—äººçžžã€‚
```

#### Notes

- The four short verse lines are visually distinct and strongly supported.
- The title `巖喚主人` and the opening prose are both clear enough to mark the next case boundary with confidence.

### PDF p.035 right leaf

- Role: body-text leaf, likely `趙州勘婆`
- Confidence: medium

#### Consolidated Readable Text

```text
〔趙州勘婆〕

è¶™å·žå› åƒ§å•å©†å­ï¼š
å°å±±è·¯å‘ç”šè™•åŽ»ï¼Ÿ
婆云：驀直去。
僧纔行三五步，
å©†äº‘ï¼šå¥½ç®‡å¸«åƒ§ï¼Œåˆæéº½åŽ»ã€‚

後有僧舉似州。
å·žäº‘ï¼šå¾…æˆ‘åŽ»èˆ‡ä½ å‹˜éŽé€™å©†å­ã€‚
æ˜Žæ—¥ä¾¿åŽ»ï¼Œäº¦å¦‚æ˜¯å•ã€‚
婆亦如是答。
州歸謂眾曰：
å°å±±å©†å­ï¼Œæˆ‘èˆ‡ä½ å‹˜ç ´äº†ä¹Ÿã€‚
```

#### Notes

- Short fragments near the top margin appear to belong to adjacent title or verse material, including readable pieces such as `æ›´å•å¦‚ä½•` and `æŠ±è³Šå«å±ˆ`.
- The body prose itself is clearer than those top fragments.
- Second-witness corroboration:
  - `Transcriptions\Wumen_Huikai_NDL_Commons\batch_refined\frames\page_046_left_frame.png`
  - independently supports the same prose cluster, including `å©†äº‘ï¼šé©€ç›´åŽ»`, `åƒ§çº”è¡Œä¸‰äº”æ­¥`, `å©†äº‘ï¼šå¥½ç®‡å¸«åƒ§`, and the later `èµ´è©¦ / é»žå¿ƒ / ç…Žæ²¹ç³` phrase family
- This section should be checked later against its facing leaf to recover the full case unit and verse.

### PDF p.021 right leaf

- Role: commentary and verse on `å—æ³‰æ–¬çŒ«`, with opening of `æ´žå±±ä¸‰é “`
- Confidence: medium

#### Consolidated Readable Text

```text
無門曰：
è‹¥å‘è€…è£ä¸‹å¾—ä¸€è½‰èªžï¼Œ
ä¾¿è¦‹å—æ³‰ä»¤ä¸è™›è¡Œã€‚
其或未然，
趙州若在，
å¥ªå´åˆ€å­ï¼Œ
倒行此令，
å—æ³‰ä¹žå‘½ã€‚

〔洞山三頓〕

é›²é–€å•æ´žå±±ï¼š
近日離甚處。
山云：
查渡。
門曰：
å¤åœ¨ç”šè™•ã€‚
山云：
æ¹–å—ã€‚
```

#### Notes

- The `å—æ³‰æ–¬çŒ«` commentary block is visually strong enough to recover without outside support.
- The start of `æ´žå±±ä¸‰é “` is clear through `æ¹–å—`.
- `RapidOCR` matched the visible case transition well enough to support this reading.

### PDF p.021 left leaf

- Role: continuation of `洞山三頓`, with opening commentary
- Confidence: medium

#### Consolidated Readable Text

```text
門曰：
幾時離彼。
山云：
å…«æœˆäºŒåäº”ã€‚
門曰：
æ”¾æ±ä¸‰é “æ£’ã€‚

至明日，
å±±å´ä¸Šå•è¨Šï¼š
昨日蒙和尚放三頓棒，
ä¸çŸ¥éŽåœ¨ç”šéº¼è™•ã€‚
門曰：
é£¯è¢‹å­ï¼Œ
æ±Ÿè¥¿æ¹–å—ä¾¿æéº¼åŽ»ã€‚
洞山於此大悟。

無門曰：
é›²é–€ç•¶æ™‚ä¾¿èˆ‡æœ¬åˆ†è‰æ–™ï¼Œ
使洞山別有生機一路，
å®¶é–€ä¸è‡´å¯‚å¯¥ã€‚
ä¸€å¤œåœ¨æ˜¯éžæµ·è£è‘—åˆ°ç›´å¾…å¤©æ˜Žå†ä¾†
```

#### Notes

- `PaddleOCR` was useful here for confirming `æ˜¨æ—¥è’™å’Œå°šæ”¾ä¸‰é “æ£’` and `æ±Ÿè¥¿æ¹–å—ä¾¿æéº¼åŽ»`.
- The last commentary line continues onto the next leaf, so this section stops before forcing the broken sentence.

### PDF p.022 right leaf

- Role: continuation of commentary on `洞山三頓`, with opening verse
- Confidence: medium

#### Consolidated Readable Text

```text
å¤©æ˜Žå†ä¾†ï¼Œ
別與他注破。
洞山直下悟去，
未是性燥。
ä¸”å•è«¸äººï¼Œ
洞山三頓棒，
åˆå–«ä¸åˆå–«ã€‚
è‹¥é“åˆå–«ï¼Œ
è‰æœ¨å¢æž—çš†åˆå–«æ£’ã€‚
è‹¥é“ä¸åˆå–«ï¼Œ
é›²é–€åˆæˆèª‘èªžã€‚
å‘è€…è£æ˜Žå¾—ï¼Œ
æ–¹èˆ‡æ´žå±±å‡ºä¸€å£æ°£ã€‚

頌曰
ç…å­æ•™å…’è¿·å­è¨£ï¼Œ
æ“¬å‰è·³èº‘æ—©ç¿»èº«ã€‚
```

#### Notes

- The commentary block on this leaf is stronger than the verse opening.
- `PaddleOCR` helped confirm the sequence `åˆå–«ä¸åˆå–« / è‰æœ¨å¢æž— / é›²é–€åˆæˆèª‘èªž`.
- The second half of the verse clearly continues onto the facing leaf.

### PDF p.022 left leaf

- Role: end of verse on `æ´žå±±ä¸‰é “`, with opening of `é˜è²ä¸ƒæ¢`
- Confidence: medium

#### Consolidated Readable Text

```text
ç„¡ç«¯å†æ•˜ç•¶é ­è‘—ï¼Œ
å‰ç®­çŒ¶è¼•å¾Œç®­æ·±ã€‚

ã€”é˜è²ä¸ƒæ¢ã€•

雲門曰：
ä¸–ç•Œæéº¼å»£é—Šï¼Œ
å› ç”šå‘é˜è²è£æŠ«ä¸ƒæ¢ã€‚
```

#### Notes

- The verse ending is readable from the image even though the leaf is stained.
- The next case title is legible as `é˜è²ä¸ƒæ¢`.
- `RapidOCR` and the page image agree on the opening `ä¸–ç•Œæéº¼å»£é—Š / å› ç”šå‘é˜è²è£æŠ«ä¸ƒæ¢`.

### PDF p.023 right leaf

- Role: continuation of `é˜è²ä¸ƒæ¢`
- Confidence: medium

#### Consolidated Readable Text

```text
é“å¾—è¦ªåˆ‡ï¼Œ
è±ˆå¯å‘è²ä¸Šè¦“ã€‚
è‹¥å°‡è€³è½æ‡‰é›£æœƒï¼Œ
çœ¼è™•èžè²æ–¹å§‹è¦ªã€‚

頌曰
æœƒå‰‡äº‹åŒä¸€å®¶ï¼Œ
ä¸æœƒè¬åˆ¥åƒå·®ã€‚
ä¸æœƒäº‹åŒä¸€å®¶ï¼Œ
æœƒå‰‡è¬åˆ¥åƒå·®ã€‚
```

#### Notes

- This leaf is stained, but the verse block is visually readable.
- The opening prose lines are weaker; I kept only the part that remains legible in the image.
- `æœƒå‰‡äº‹åŒä¸€å®¶ / è¬åˆ¥åƒå·®` is strongly supported by both image and OCR.

### PDF p.023 left leaf

- Role: `國師三喚` prose and commentary
- Confidence: medium

#### Consolidated Readable Text

```text
〔國師三喚〕

åœ‹å¸«ä¸‰å–šä¾è€…ï¼Œ
ä¾è€…ä¸‰æ‡‰ã€‚
國師云：
å°‡è¬‚å¾è¾œè² æ±ï¼Œ
å…ƒä¾†å´æ˜¯æ±è¾œè² å¾ã€‚

無門曰：
國師三喚，
ä¾è€…ä¸‰æ‡‰ã€‚
å’Œå…‰å‡ºåœ‹å¸«å¹³ç”Ÿè€å©†å¿ƒåˆ‡ã€‚
牛頭未見四祖時如何。
中飽人飢，
ä¸”é“é‚£è£æ˜¯ä»–è¾œè² è™•ã€‚

頌曰
åœ‹æ¸…æ‰å­è²´ï¼Œ
å®¶å¯Œå°å…’å¬Œã€‚
```

#### Notes

- The opening exchange is clear in the witness.
- The commentary is readable enough through `ä¸”é“é‚£è£æ˜¯ä»–è¾œè² è™•`.
- The verse continues onto the next leaf, so only the secure opening couplet is included here.
- Cross-witness support:
  - the second witness anchors `國師三喚` in its corresponding body sequence
  - the third witness supports the same cluster order at contents/title level

### PDF p.024 right leaf

- Role: end of `國師三喚`, with opening of `洞山三斤`
- Confidence: medium

#### Consolidated Readable Text

```text
頭角生也，
未肯承當。
ç¾©é£Ÿä¸é£½äººï¼Œ
飢腸先開。

〔洞山三斤〕

æ´žå±±å’Œå°šå› åƒ§å•ï¼š
如何是佛。
山云：
麻三斤。

無門曰：
æ´žå±±è€äººåƒå¾—äº›èšŒè›¤ç¦ªï¼Œ
纔開兩片，
éœ²å‡ºè‚è…¸ã€‚
然雖如是，
ä¸”é“å‘ç”šè™•è¦‹æ´žå±±ã€‚
```

#### Notes

- The `國師三喚` verse ending is weak; only the broad readable shape is kept and one graph remains uncertain.
- `洞山三斤` is clear and stable from the witness.
- `RapidOCR` strongly supported `如何是佛 / 麻三斤`.

### PDF p.024 left leaf

- Role: verse on `æ´žå±±ä¸‰æ–¤`, with opening of `å¹³å¸¸æ˜¯é“`
- Confidence: medium

#### Consolidated Readable Text

```text
頌曰
çªå‡ºéº»ä¸‰æ–¤ï¼Œ
è¨€è¦ªæ„æ›´è¦ªã€‚
ä¾†èªªæ˜¯éžè€…ï¼Œ
ä¾¿æ˜¯æ˜¯éžäººã€‚

ã€”å¹³å¸¸æ˜¯é“ã€•

å—æ³‰å› è¶™å·žå•ï¼š
å¦‚ä½•æ˜¯é“ã€‚
泉云：
å¹³å¸¸å¿ƒæ˜¯é“ã€‚
州云：
é‚„å¯è¶£å‘å¦ã€‚
泉云：
æ“¬å‘å³ä¹–ã€‚
州云：
ä¸æ“¬çˆ­çŸ¥æ˜¯é“ã€‚
泉云：
é“ä¸å±¬çŸ¥ï¼Œ
ä¸å±¬ä¸çŸ¥ã€‚
```

#### Notes

- The `洞山三斤` verse is clear enough to recover as a full quatrain.
- The opening dialogue of `å¹³å¸¸æ˜¯é“` is strong in the image and consistent with OCR.
- The rest of `å¹³å¸¸æ˜¯é“` continues beyond this leaf.
- Cross-witness support:
  - both corroborating witnesses preserve the same `å¹³å¸¸æ˜¯é“` phrase family in the corresponding mid-book cluster

### PDF p.025 right leaf

- Role: end of `å¹³å¸¸æ˜¯é“`, with verse
- Confidence: medium

#### Consolidated Readable Text

```text
泉云：
é“ä¸å±¬çŸ¥ï¼Œ
ä¸å±¬ä¸çŸ¥ã€‚
知是妄覺，
ä¸çŸ¥æ˜¯ç„¡è¨˜ã€‚
è‹¥çœŸé”ä¸ç–‘ä¹‹é“ï¼Œ
çŒ¶å¦‚å¤ªè™›å»“ç„¶æ´žè±ï¼Œ
è±ˆå¯å¼·æ˜¯éžä¹Ÿã€‚
州於言下頓悟。

無門曰：
å—æ³‰è¢«è¶™å·žç™¼å•ï¼Œ
直得瓦解氷消，
åˆ†è¸ˆä¸ä¸‹ã€‚
趙州縱饒悟去，
æ›´åƒä¸‰åå¹´å§‹å¾—ã€‚

頌曰
春有百花秋有月，
å¤æœ‰æ¶¼é¢¨å†¬æœ‰é›ªã€‚
```

#### Notes

- The prose close of `å¹³å¸¸æ˜¯é“` is strong in the image, including `çŸ¥æ˜¯å¦„è¦º / ä¸çŸ¥æ˜¯ç„¡è¨˜`.
- The verse begins clearly here and continues on the facing leaf.

### PDF p.025 left leaf

- Role: end of `å¹³å¸¸æ˜¯é“` verse, with opening of `å¤§åŠ›é‡äºº`
- Confidence: medium

#### Consolidated Readable Text

```text
若無閑事挂心頭，
便是人間好時節。

ã€”å¤§åŠ›é‡äººã€•

æ¾æºå’Œå°šäº‘ï¼š
å¤§åŠ›é‡äººï¼Œ
å› ç”šæ“¡è…³ä¸èµ·ã€‚
åˆäº‘ï¼š
é–‹å£ä¸åœ¨èˆŒé ­ä¸Šã€‚

無門曰：
æ¾æºå¯è¬‚å‚¾è…¸å€’è…¹ã€‚
åªæ˜¯æ¬ äººæ‰¿ç•¶ã€‚
直下承當，
正好來無門處喫痛棒。
何故。
```

#### Notes

- The `å¹³å¸¸æ˜¯é“` verse close is very clear.
- The `å¤§åŠ›é‡äºº` title and opening exchange are stable from the witness.
- The last commentary sentence continues onto the next leaf.

### PDF p.026 right leaf

- Role: end of `å¤§åŠ›é‡äºº`, with opening of `é›²é–€å±Žæ©›`
- Confidence: medium

#### Consolidated Readable Text

```text
è¦è­˜çœŸé‡‘ï¼Œ
ç«è£çœ‹ã€‚

〔雲門屎橛〕

åƒ§å•é›²é–€ï¼š
如何是佛。
門云：
乾屎橛。

無門曰：
é›²é–€å¯è¬‚å®¶è²§é›£è¾¨ç´ é£Ÿï¼Œ
äº‹å¿™ä¸åŠè‰æ›¸ã€‚
å‹•ä¾¿å°‡å±Žä¾†æ’é–€æ‹„æˆ¶ã€‚

頌曰
閃電光，
æ“ŠçŸ³ç«ã€‚
```

#### Notes

- The `å¤§åŠ›é‡äºº` close is readable and the `è¦è­˜çœŸé‡‘ï¼Œç«è£çœ‹ã€‚` couplet is clear.
- `如何是佛 / 乾屎橛` is strongly supported by the image and OCR.
- The verse on `雲門屎橛` continues onto the facing leaf.

### PDF p.026 left leaf

- Role: end of `雲門屎橛`, with opening of `迦葉刹竿`
- Confidence: medium

#### Consolidated Readable Text

```text
眨得眼，
å·²è¹‰éŽã€‚

〔迦葉刹竿〕

é˜¿é›£å•è¿¦è‘‰äº‘ï¼š
世尊傳金襴外，
別傳何物。
葉云：
å€’å´é–€å‰åˆ¹ç«¿è‘—ã€‚
```

#### Notes

- The closing verse lines on `雲門屎橛` are legible despite staining.
- The next case opening is clear enough to identify as `迦葉刹竿`.
- I kept this leaf conservative and stopped before forcing the weaker continuation lines.

### PDF p.027 right leaf

- Role: continuation of `è¿¦è‘‰åˆ¹ç«¿`, with opening of `ä¸æ€å–„æƒ¡`
- Confidence: medium

#### Consolidated Readable Text

```text
無門曰：
è‹¥å‘è€…è£ä¸‹å¾—ä¸€è½‰èªžè¦ªåˆ‡ï¼Œ
ä¾¿è¦‹éˆå±±ä¸€æœƒå„¼ç„¶æœªæ•£ã€‚
其或未然，
佛早留心，
ç›´è‡³è€Œä»Šä¸å¾—å¦™ã€‚

頌曰
å•è™•ä½•å¦‚ç­”è™•è¦ªï¼Œ
幾人於此眼生筋。
å…„å‘¼å¼Ÿæ‡‰æšå®¶é†œï¼Œ
ä¸å±¬é™°é™½åˆ¥æ˜¯æ˜¥ã€‚
```

#### Notes

- This leaf still belongs to the end of `迦葉刹竿`.
- The verse is readable enough from the image, though a few graphs remain faint.

### PDF p.027 left leaf

- Role: opening prose on `ä¸æ€å–„æƒ¡`
- Confidence: medium

#### Consolidated Readable Text

```text
ã€”ä¸æ€å–„æƒ¡ã€•

å…­ç¥–å› æ˜Žä¸Šåº§è¶è‡³å¤§åº¾å¶ºã€‚
祖見明至，
å³æ“²è¡£é‰¢æ–¼çŸ³ä¸Šäº‘ï¼š
此衣表信，
å¯åŠ›çˆ­è€¶ã€‚
æ˜Žé‚æ“§ä¹‹ï¼Œ
å¦‚å±±ä¸å‹•ã€‚
明白：
我來求法，
éžç‚ºè¡£ä¹Ÿã€‚
願行者開示。
祖云：
ä¸æ€å–„ï¼Œ
ä¸æ€æƒ¡ï¼Œ
正與麼時，
é‚£ç®‡æ˜¯æ˜Žä¸Šåº§æœ¬ä¾†é¢ç›®ã€‚
明當下大悟，
éé«”æ±—æµï¼Œ
æ³£æ·šä½œç¦®å•ã€‚
```

#### Notes

- The leaf is clear enough to recover the main `ä¸æ€å–„æƒ¡` exchange as continuous prose.
- The closing words continue onto the next leaf.

### PDF p.028 right leaf

- Role: continuation and commentary on `ä¸æ€å–„æƒ¡`
- Confidence: medium

#### Consolidated Readable Text

```text
明曰：
ä¸Šä¾†å¯†èªžå¯†æ„å¤–ï¼Œ
é‚„æ›´æœ‰æ„æ—¨å¦ã€‚
祖曰：
æˆ‘ä»Šç‚ºæ±èªªè€…ï¼Œ
å³éžå¯†ä¹Ÿã€‚
æ±è‹¥è¿”ç…§è‡ªå·±é¢ç›®ï¼Œ
å¯†å´åœ¨æ±é‚Šã€‚
明曰：
æŸç”²é›–åœ¨é»ƒæ¢…éš¨çœ¾ï¼Œ
å¯¦æœªçœè‡ªå·±é¢ç›®ã€‚
今蒙指授入處，
如人飲水，
冷暖自知。
```

#### Notes

- This leaf carries the clearer continuation after the main `æœ¬ä¾†é¢ç›®` exchange.
- The commentary transition is visible but weaker than the prose block.

### PDF p.028 left leaf

- Role: opening of `é›¢å»èªžè¨€`
- Confidence: medium

#### Consolidated Readable Text

```text
ã€”é›¢å»èªžè¨€ã€•

é¢¨ç©´å’Œå°šå› åƒ§å•ï¼š
語默涉離微，
å¦‚ä½•é€šä¸çŠ¯ã€‚
```

#### Notes

- The opening koan line is secure, but the rest of the leaf is too compressed for fuller recovery on this pass.
- The following leaf carries stronger support for the verse and commentary shape.

### PDF p.029 right leaf

- Role: verse/commentary on `é›¢å»èªžè¨€`
- Confidence: medium

#### Consolidated Readable Text

```text
無門曰：
風穴機如掣電，
得路便行。
çˆ­å¥ˆåå‰äººèˆŒé ­ä¸æ–·ã€‚
è‹¥å‘è€…è£è¦‹å¾—è¦ªåˆ‡ï¼Œ
自有出身之路。

頌曰
ä¸éœ²é¢¨éª¨å¥ï¼Œ
未語先分付。
é€²æ­¥å£å–ƒå–ƒï¼Œ
çŸ¥å›å¤§ç½¨ç¼¶ã€‚
é•·æ†¶æ±Ÿå—ä¸‰æœˆè£ï¼Œ
鷓鴣啼處百花香。
```

#### Notes

- The verse opening `ä¸éœ²é¢¨éª¨å¥ï¼Œæœªèªžå…ˆåˆ†ä»˜` is strong in both image and OCR.
- The last two lines are readable in the witness, though not as dark as the opening couplet.

### PDF p.029 left leaf

- Role: opening of `三座說法`
- Confidence: medium

#### Consolidated Readable Text

```text
〔三座說法〕

仰山和尚夢見往彌勒所，
安第三座。
有一尊者白槌云：
今日當第三座說法。
```

#### Notes

- The title and opening prose are secure.
- The rest of the leaf is present but remains compressed and should be revisited with the facing leaf when refining this case.

### PDF p.030 right leaf

- Role: opening of `äºŒåƒ§å·ç°¾`
- Confidence: medium

#### Consolidated Readable Text

```text
ã€”äºŒåƒ§å·ç°¾ã€•

æ¸…æ¶¼å¤§æ³•çœ¼å› åƒ§é½‹å‰ä¸Šåƒã€‚
眼以手指簾。
æ™‚æœ‰äºŒåƒ§åŒåŽ»å·ç°¾ã€‚
眼曰：
一得，
一失。
```

#### Notes

- The case identity and the key exchange are stable.
- This is the clearest leaf for the case opening.

### PDF p.030 left leaf

- Role: commentary on `äºŒåƒ§å·ç°¾`
- Confidence: low-medium

#### Consolidated Readable Text

```text
無門曰：
ä¸”é“æ˜¯å¾—æ˜¯å¤±ã€‚
è‹¥å‘è€…è£è‘—å¾—ä¸€éš»çœ¼ï¼Œ
便知清涼國師敗缺處。
然雖如是，
åˆ‡å¿Œå‘å¾—å¤±è£å•†é‡ã€‚
```

#### Notes

- This reading is more provisional than the prose leaf.
- The commentary shape is visible, but several graphs are faint and should be checked again later.

### PDF p.031 right leaf

- Role: opening of `ä¸æ˜¯å¿ƒä½›`
- Confidence: medium

#### Consolidated Readable Text

```text
ã€”ä¸æ˜¯å¿ƒä½›ã€•

å—æ³‰å’Œå°šå› åƒ§å•äº‘ï¼š
é‚„æœ‰ä¸æ˜¯å¿ƒï¼Œ
ä¸æ˜¯ä½›ï¼Œ
ä¸æ˜¯ç‰©ã€‚
泉云：
ä¸æ˜¯å¿ƒï¼Œ
ä¸æ˜¯ä½›ï¼Œ
ä¸æ˜¯ç‰©ã€‚
```

#### Notes

- The opening exchange is clear and stable.
- Commentary below is present but weaker than the koan block.

### PDF p.031 left leaf

- Role: opening of `ä¹…éŸ¿é¾æ½­`
- Confidence: medium

#### Consolidated Readable Text

```text
ã€”ä¹…éŸ¿é¾æ½­ã€•

é¾æ½­å› å¾·å±±è«‹ç›Šã€‚
夜云：
夜深。
å­ä½•ä¸ä¸‹åŽ»ã€‚
å±±é‚çé‡æ­ç°¾è€Œå‡ºã€‚
è¦‹å¤–é¢é»‘å´å›žäº‘ï¼š
å¤–é¢é»‘ã€‚
潭乃點紙燭度與山。
```

#### Notes

- This is the strongest opening leaf for `ä¹…éŸ¿é¾æ½­`.
- The continuation carries onto the next pages.
- Cross-witness support:
  - both corroborating witnesses preserve `é¾æ½­å’Œå°š` material in the same later-middle case cluster

### PDF p.032 right leaf

- Role: continuation of `ä¹…éŸ¿é¾æ½­`
- Confidence: medium

#### Consolidated Readable Text

```text
山擬接，
æ½­å¾©å¹æ»…ã€‚
å±±æ–¼æ­¤å¿½ç„¶æœ‰çœã€‚
便作禮。
潭云：
å­è¦‹ç®‡ç”šéº¼é“ç†ã€‚
山云：
æŸç”²å¾žä»Šæ—¥åŽ»ï¼Œ
ä¸ç–‘å¤©ä¸‹è€å’Œå°šèˆŒé ­ä¹Ÿã€‚
```

#### Notes

- The core enlightenment turn is readable enough from the image.
- Commentary begins lower on the leaf but is less stable.

### PDF p.032 left leaf

- Role: later continuation on `ä¹…éŸ¿é¾æ½­`
- Confidence: low-medium

#### Consolidated Readable Text

```text
至明日，
é¾æ½­é™žå ‚äº‘ï¼š
å¯ä¸­æœ‰ç®‡æ¼¢ï¼Œ
ç‰™å¦‚åŠæ¨¹ï¼Œ
å£ä¼¼è¡€ç›†ã€‚
ä¸€æ£’æ‰“ä¸å›žé ­ã€‚
ä»–æ™‚å‘å­¤å³°é ‚ä¸Šï¼Œ
ç«‹å¾é“åŽ»åœ¨ã€‚
```

#### Notes

- This leaf is weaker than the opening pair, but the main prose block is still recoverable.
- The lower commentary area remains provisional.

### PDF p.033 right leaf

- Role: `è¶™å·žå‹˜å©†` / `å©†å­`-side material
- Confidence: low-medium

#### Consolidated Readable Text

```text
é‚å•å©†å­è¿‘è™•æœ‰ç”šéº¼å®—å¸«ã€‚
婆云：
äº”é‡Œå¤–æœ‰é¾æ½­å’Œå°šã€‚
åŠåˆ°é¾æ½­ï¼Œ
å¯è¬‚æ˜¯å‰è¨€ä¸æ‡‰å¾Œèªžã€‚

ç«ç¨®éƒ½å¿™ï¼Œ
將惡水驀頭一澆。
冷地看來，
一場好笑。

頌曰
èžåä¸å¦‚è¦‹é¢ï¼Œ
è¦‹é¢ä¸å¦‚èžåã€‚
雖然救得鼻孔，
çˆ­å¥ˆçžŽå´çœ¼ç›ã€‚
```

#### Notes

- The visible text is `å©†å­` material, not `ä¹…éŸ¿é¾æ½­`.
- Secondary witness corroboration:
  - `Transcriptions\Wumen_Huikai_NDL_Commons\batch_refined\frames\page_047_right_frame.png`
  - supports the broader `è¶™å·žå‹˜å©†` zone with phrases such as `ä½•æ•…å©†äº‘`, `æˆ‘ç…Žå¾—é€åº•`, and `ç…Žæœªé€è€…åªç®¡ä½œ`
- The recovery is still partial, but the case-side identification is now materially stronger.

### PDF p.033 left leaf

- Role: opening of `éžé¢¨éžå¹¡`
- Confidence: medium

#### Consolidated Readable Text

```text
ã€”éžé¢¨éžå¹¡ã€•

六祖因風颺刹，
æœ‰äºŒåƒ§å°è«–ã€‚
一云風動，
一云幡動。
å¾€å¾©æ›¾æœªå¥‘ç†ã€‚
祖云：
ä¸æ˜¯é¢¨å‹•ï¼Œ
ä¸æ˜¯å¹¡å‹•ï¼Œ
ä»è€…å¿ƒå‹•ã€‚
```

#### Notes

- This is a clean witness opening and is one of the better leaves in this back-half stretch.
- The commentary below is present but not yet fully recovered.

### PDF p.034 right leaf

- Role: opening of `å³å¿ƒå³ä½›`
- Confidence: medium

#### Consolidated Readable Text

```text
ã€”å³å¿ƒå³ä½›ã€•

é¦¬ç¥–å› å¤§æ¢…å•ï¼š
如何是佛。
祖云：
å³å¿ƒæ˜¯ä½›ã€‚
```

#### Notes

- The title and opening dialogue are clear.
- The leaf also begins commentary/verse material, but the opening is the secure part.

### PDF p.034 left leaf

- Role: commentary on `å³å¿ƒå³ä½›`
- Confidence: low-medium

#### Consolidated Readable Text

```text
無門曰：
若能直下領得去，
著佛衣，
喫佛飯，
說佛話，
行佛行，
å³æ˜¯ä½›ä¹Ÿã€‚

頌曰
é’å¤©ç™½æ—¥ï¼Œ
切忌尋覓。
```

#### Notes

- The wording is supported by both the page image and OCR comparators, but the leaf is still lighter than the earlier body-text pages.
- The left-side verse opening `é’å¤©ç™½æ—¥ / åˆ‡å¿Œå°‹è¦“` is also visible enough to include.
- Remaining lines below that verse opening should be revisited later.

### PDF p.035 left leaf

- Role: commentary/verse on `趙州勘婆`
- Confidence: low-medium

#### Consolidated Readable Text

```text
無門曰：
å©†å­åªè§£åç±Œå¸·ï¼Œ
è¦ä¸”ä¸è­˜è¶™å·žã€‚
è¶™å·žè€äººï¼Œ
å–„ç”¨å¸ç‡ŸåŠ«å¯¨ã€‚
雖然如是，
ä¸”é“é‚£è£æ˜¯è¶™å·žå‹˜ç ´å©†å­è™•ã€‚

頌曰
å•æ—¢ä¸€èˆ¬ï¼Œ
答亦相似。
é£¯è£æœ‰ç ‚ï¼Œ
泥中有刺。
```

#### Notes

- This is the facing leaf to the earlier [PDF p.035 right leaf](Transcriptions/Wumenguan_1632_NDL_Commons/architect/WUMENGUAN_1632.md#L977).
- The commentary is recoverable, but still weaker than the prose leaf.

### PDF p.036 right leaf

- Role: opening of `å¤–é“å•ä½›`
- Confidence: medium

#### Consolidated Readable Text

```text
ã€”å¤–é“å•ä½›ã€•

ä¸–å°Šå› å¤–é“å•ï¼š
ä¸å•æœ‰è¨€ï¼Œ
ä¸å•ç„¡è¨€ã€‚
世尊良久。
å¤–é“è®šæ­Žäº‘ï¼š
世尊大慈大悲，
開我迷雲，
令我得入。
乃具禮而去。
é˜¿é›£å•ä½›ï¼š
å¤–é“æœ‰ä½•æ‰€è­‰ï¼Œ
而言讚歎而去。
```

#### Notes

- The opening exchange is one of the clearer recoveries in this compressed section.
- The leaf continues the case into the Buddhaâ€™s reply.

### PDF p.036 left leaf

- Role: opening of `éžå¿ƒéžä½›`
- Confidence: medium

#### Consolidated Readable Text

```text
ã€”éžå¿ƒéžä½›ã€•

é¦¬ç¥–å› åƒ§å•ï¼š
å¦‚ä½•æ˜¯ç¥–å¸«è¥¿ä¾†æ„ã€‚
祖云：
éžå¿ƒéžä½›ã€‚
```

#### Notes

- The title and core answer are secure.
- The lower commentary area is too faint for a stronger claim on this pass.
- Cross-witness support:
  - both corroborating witnesses preserve the same `ä¸æ˜¯å¿ƒä¸æ˜¯ä½›ä¸æ˜¯ç‰©` phrase family in this cluster

### PDF p.037 right leaf

- Role: `æ™ºä¸æ˜¯é“`
- Confidence: medium

#### Consolidated Readable Text

```text
ã€”æ™ºä¸æ˜¯é“ã€•

å—æ³‰äº‘ï¼š
å¿ƒä¸æ˜¯ä½›ï¼Œ
æ™ºä¸æ˜¯é“ã€‚
```

#### Notes

- This leaf is short and clear at the case-opening level.
- Additional commentary is visible but remains too compressed to normalize safely here.

### PDF p.037 left leaf

- Role: opening of `倩女離魂`
- Confidence: medium

#### Consolidated Readable Text

```text
〔倩女離魂〕

äº”ç¥–å•åƒ§äº‘ï¼š
倩女離魂，
那箇是正底。
```

#### Notes

- The title and opening question are secure from both image and OCR.
- The rest of the leaf remains faint and should be revisited later.

### PDF p.038 right leaf

- Role: opening of `è·¯é€¢é”é“`
- Confidence: medium

#### Consolidated Readable Text

```text
ã€”è·¯é€¢é”é“ã€•

五祖曰：
è·¯é€¢é”é“äººï¼Œ
ä¸å°‡èªžé»˜å°ï¼Œ
ä¸”é“å°‡ç”šéº¼å°ã€‚
```

#### Notes

- The opening prompt is stable in the witness.
- Commentary/verse below is present but not yet strong enough for fuller transcription.

### PDF p.038 left leaf

- Role: opening of `åº­å‰æŸæ¨¹`
- Confidence: medium

#### Consolidated Readable Text

```text
ã€”åº­å‰æŸæ¨¹ã€•

è¶™å·žå› åƒ§å•ï¼š
å¦‚ä½•æ˜¯ç¥–å¸«è¥¿ä¾†æ„ã€‚
州云：
åº­å‰æŸæ¨¹å­ã€‚
```

#### Notes

- This is a clean leaf for the case opening.
- The lower material likely belongs to commentary or transition and remains less secure.

### PDF p.039 right leaf

- Role: opening of `ç‰›éŽçª—æ«º`
- Confidence: medium

#### Consolidated Readable Text

```text
ã€”ç‰›éŽçª—æ«ºã€•

五祖曰：
è­¬å¦‚æ°´ç‰›éŽçª—æ«ºï¼Œ
é ­è§’å››è¹„éƒ½éŽäº†ï¼Œ
å› ç”šå°¾å·´éŽä¸å¾—ã€‚
```

#### Notes

- The core simile is stable enough to recover.
- The leaf below this block is weaker and should be revisited in a later pass.

### PDF p.039 left leaf

- Role: opening of `雲門話墮`
- Confidence: medium

#### Consolidated Readable Text

```text
〔雲門話墮〕

é›²é–€å› åƒ§å•ï¼š
å…‰æ˜Žå¯‚ç…§éæ²³æ²™ã€‚
```

#### Notes

- The opening question is secure.
- The continuation and response are more legible on the next leaf.

### PDF p.040 right leaf

- Role: continuation on `雲門話墮`
- Confidence: low-medium

#### Consolidated Readable Text

```text
門云：
è±ˆä¸æ˜¯å¼µæ‹™ç§€æ‰èªžã€‚
僧云：
是。
門云：
話墮也。
```

#### Notes

- This reading is supported by OCR and the page image, but the leaf is lighter than ideal.
- I kept only the main exchange that remains stable.

### PDF p.040 left leaf

- Role: opening of `趯倒淨瓶`
- Confidence: medium

#### Consolidated Readable Text

```text
〔趯倒淨瓶〕

溈山和尚始在百丈會中充典座。
ç™¾ä¸ˆå°‡é¸å¤§æºˆä¸»äººã€‚
ç™¾ä¸ˆé‚æ‹ˆæ·¨ç“¶ç½®åœ°ï¼Œ
è¨­å•äº‘ï¼š
ä¸å¾—å–šä½œæ·¨ç“¶ï¼Œ
æ±å–šä½œç”šéº¼ã€‚
```

#### Notes

- The case opening is stable from the witness and aligns with the OCR comparators.
- The decisive answer and follow-through continue onto the next leaf.

### PDF p.041 right leaf

- Role: continuation of `趯倒淨瓶`
- Confidence: low-medium

#### Consolidated Readable Text

```text
å±±é‚è¶¯å€’æ·¨ç“¶è€ŒåŽ»ã€‚
百丈云：
ç¬¬ä¸€åº§è¼¸å´å±±å­ä¹Ÿã€‚
因命之為開山。
```

#### Notes

- The action line is the secure core of this leaf.
- OCR and image also support the immediate follow-through `ç™¾ä¸ˆäº‘ / ç¬¬ä¸€åº§è¼¸å´å±±å­ä¹Ÿ / å› å‘½ä¹‹ç‚ºé–‹å±±`.
- The later commentary/verse material on the leaf remains too weak on this pass for a cleaner diplomatic recovery.

### PDF p.041 left leaf

- Role: opening of `é”ç£¨å®‰å¿ƒ`
- Confidence: medium

#### Consolidated Readable Text

```text
ã€”é”ç£¨å®‰å¿ƒã€•

é”ç£¨é¢å£ã€‚
二祖立雪斷臂云：
å¼Ÿå­å¿ƒæœªå®‰ï¼Œ
乞師安心。
祖云：
å°‡å¿ƒä¾†èˆ‡æ±å®‰ã€‚
```

#### Notes

- This leaf cleanly opens `é”ç£¨å®‰å¿ƒ`.
- The continuation is present below, but the opening exchange is the strongest recoverable block.

### PDF p.042 right leaf

- Role: opening of `å¥³å­å‡ºå®š`
- Confidence: medium

#### Consolidated Readable Text

```text
ã€”å¥³å­å‡ºå®šã€•

世尊昔因文殊至諸佛集處，
å€¼è«¸ä½›å„é‚„æœ¬è™•ï¼Œ
æƒŸæœ‰ä¸€å¥³äººè¿‘å½¼ä½›åå…¥å®šã€‚
文殊乃白佛：
äº‘ä½•å¥³äººå¾—è¿‘ä½›åï¼Œ
æˆ‘ä¸å¾—ã€‚
```

#### Notes

- The title and opening setup are secure.
- The doctrinal question continues on the facing leaf.

### PDF p.042 left leaf

- Role: continuation of `å¥³å­å‡ºå®š`
- Confidence: low-medium

#### Consolidated Readable Text

```text
佛告文殊：
但此女人令從三昧起，
æ±è‡ªè¿‘å‰å•ä¹‹ã€‚
若出得定，
便知所以。
```

#### Notes

- This leaf is weaker than the opening leaf.
- The continuation is legible in outline, but at least one graph remains uncertain.

### PDF p.043 right leaf

- Role: later continuation on `å¥³å­å‡ºå®š`
- Confidence: low-medium

#### Consolidated Readable Text

```text
無門曰：
ç¨½é¦–è€é‡‹è¿¦ï¼Œ
åªä½œä¸€å ´é›œåŠ‡ã€‚
ä¸”é“æ–‡æ®Šæ˜¯ä¸ƒä½›ä¹‹å¸«ï¼Œ
å› ç”šå‡ºå¥³å­å®šä¸å¾—ã€‚
ç½”æ˜Žåˆåœ°è©è–©ï¼Œ
ç‚ºç”šå´å‡ºå¾—ã€‚
```

#### Notes

- The commentary shape is visible and partly recoverable.
- This remains more provisional than the clearer prose leaves in the front half.

### PDF p.043 left leaf

- Role: opening of `首山竹篦`
- Confidence: medium

#### Consolidated Readable Text

```text
〔首山竹篦〕

首山和尚拈竹篦示眾云：
æ±ç­‰è«¸äººï¼Œ
若喚作竹篦則觸，
ä¸å–šä½œç«¹ç¯¦å‰‡èƒŒã€‚
ä¸å¾—æœ‰èªžï¼Œ
ä¸å¾—ç„¡èªžã€‚
é€Ÿé“ã€‚
```

#### Notes

- This is the strongest leaf for the case opening.
- Commentary below is visible but remains too light for a stronger transcription.

### PDF p.044 right leaf

- Role: opening of `èŠ­è•‰æ‹„æ–`
- Confidence: medium

#### Consolidated Readable Text

```text
ã€”èŠ­è•‰æ‹„æ–ã€•

芭蕉和尚示眾云：
æœ‰æ‹„æ–å­ï¼Œ
æˆ‘èˆ‡ä½ æ‹„æ–å­ã€‚
ç„¡æ‹„æ–å­ï¼Œ
æˆ‘å¥ªä½ æ‹„æ–å­ã€‚
```

#### Notes

- The title and core exchange are secure from the witness.
- The lower verse/commentary remains weaker.

### PDF p.044 left leaf

- Role: opening of `他是阿誰`
- Confidence: medium

#### Consolidated Readable Text

```text
〔他是阿誰〕

æ±å±±æ¼”å¸«ç¥–æ›°ï¼š
釋迦彌勒猶是他奴。
ä¸”é“ä»–æ˜¯é˜¿èª°ã€‚
```

#### Notes

- This leaf is short and clear at the case-opening level.
- Further material on the page remains compressed.

### PDF p.045 right leaf

- Role: opening of `竿頭進步`
- Confidence: medium

#### Consolidated Readable Text

```text
〔竿頭進步〕

石霜和尚云：
百尺竿頭，
如何進步。
```

#### Notes

- The case title and opening question are stable.
- The fuller old-adept quotation is clearer on the facing leaf.

### PDF p.045 left leaf

- Role: continuation of `竿頭進步`
- Confidence: medium

#### Consolidated Readable Text

```text
åˆå¤å¾·äº‘ï¼š
ç™¾å°ºç«¿é ­ååº•äººï¼Œ
雖然得入未為真。
百尺竿頭須進步，
åæ–¹ä¸–ç•Œç¾å…¨èº«ã€‚
```

#### Notes

- This is the stronger leaf for the caseâ€™s famous verse-like extension.
- Third-witness corroboration:
  - `Transcriptions\Mumonkan_1752_Waseda_Commons\batch_refined\frames\page_047_right_frame.png`
  - independently supports `ç™¾å°ºç«¿é ­ååº•äºº`, `ç™¾å°ºç«¿é ­é ˆé€²æ­¥`, and `åæ–¹ä¸–ç•Œç¾å…¨èº«`
- Lower commentary remains present but not yet normalized here.

### PDF p.046 right leaf

- Role: opening of `兜率三關`
- Confidence: medium

#### Consolidated Readable Text

```text
〔兜率三關〕

å…œçŽ‡æ‚…å’Œå°šè¨­ä¸‰é—œå•å­¸è€…ï¼š
æ’¥è‰åƒçŽ„åªåœ–è¦‹æ€§ã€‚
å³ä»Šä¸Šäººæ€§åœ¨ç”šè™•ã€‚
```

#### Notes

- The case title and first question are secure.
- The later questions and commentary are present but more compressed.

### PDF p.046 left leaf

- Role: opening of `乾峰一路`
- Confidence: medium

#### Consolidated Readable Text

```text
〔乾峰一路〕

ä¹¾å³°å’Œå°šå› åƒ§å•ï¼š
åæ–¹è–„ä¼½æ¢µï¼Œ
一路涅槃門。
未審路頭在甚麼處。
```

#### Notes

- This leaf gives a clean body-text opening for the final case of the 48.
- Further continuation below remains lighter and should be checked later if a fuller diplomatic pass is needed.

### PDF p.047 right leaf

- Role: closing/post-case material
- Confidence: low-medium

#### Consolidated Readable Text

```text
é–€äº‘æ‹ˆèµ·æ‰‡å­äº‘ã€‚
æ‰‡å­è¸è·³ä¸Šä¸‰åä¸‰å¤©ã€‚
ç¯‰è‘—å¸é‡‹é¼»å­”ã€‚
æ±æµ·é¯‰é­šæ‰“ä¸€æ£’ï¼Œ
雨似盆傾。
```

#### Notes

- This leaf appears to belong to the closing instructional material after the 48 cases.
- The line above is the clearest stable recovery.

### PDF p.047 left leaf

- Role: closing/post-case material
- Confidence: low

#### Consolidated Readable Text

```text
未舉步時先已到，
未動舌時先說了。
直饒著著在機先，
æ›´é ˆçŸ¥æœ‰å‘ä¸Šç«…ã€‚
```

#### Notes

- The quatrain is secure.
- OCR and image both suggest additional surrounding prose, including a clearer evaluative cluster around `éžå¤§ä¼¼å…©ç®‡çžŽæ¼¢å­ç›¸æ’žè‘—` and `ç„¡ç›´åº•äººæ­£çœ¼è§€ä¾†äºŒå¤§è€`.
- The adjacent phrase family `識路頭在 / 在機先` is also visible, but the prose remains too tight to normalize line by line with confidence on this pass.
- The safest reading remains the quatrain, with the surrounding prose logged only at the phrase-family level.

### PDF p.048 right leaf

- Role: postscript / closing statement
- Confidence: low-medium

#### Consolidated Readable Text

```text
從上佛祖垂示機緣，
æ’®çµæ¡ˆåˆã€‚
請人直下承當，
ä¸è½è™•äº†ç„¡ã€‚
æ–¹ä¸Šå£«çµ•èžèˆˆå­¸è€…ï¼Œ
ä¾¿çŸ¥è½è™•äº†ç„¡ã€‚
é“æ˜ŽçŸ¥é“åªæ˜¯é€™ç®‡ï¼Œ
çˆ²ç”šé€ä¸å¾—ç„¡é–€é—œã€‚
```

#### Notes

- This leaf is stronger than the earlier two-line stub.
- The main reflective block is readable in substance from the witness image, though the lower and side fragments remain unstable.

### PDF p.048 left leaf

- Role: postscript / reflective note
- Confidence: low

#### Consolidated Readable Text

```text
ä¸éŽæ·¨åŽ èªªè©±ï¼Œ
ä¹Ÿæ˜¯èµ¤åœŸæ½ç‰›å¥¶ã€‚
è‹¥é€å¾—ç„¡é–€é—œï¼Œ
æ—©æ˜¯éˆç½®ç„¡é–€é—œã€‚
é€ä¸å¾—ç„¡é–€é—œï¼Œ
亦乃辜負自己。
所謂涅槃心易曉，
差別智難明。
明得差別智，
家國自安寧。
ç´¹å®šæ”¹å…ƒè§£åˆ¶å‰äº”æ—¥ï¼Œ
æ¥Šå²å…«ä¸–å­«ç„¡é–€æ¯”ä¸˜æ…§é–‹è¬¹è­˜ã€‚
```

#### Notes

- This leaf is text-bearing and stronger than the earlier placeholder state.
- The central reflective block is readable in substance, and the lower signature/date block is also now visible enough to include.
- OCR and image both support the reflective cadence around `çŸ¥é“åªæ˜¯é€™ç®‡ / çˆ²ç”šé€ä¸å¾—ç„¡é–€é—œ` on the facing leaf, and this leaf continues with the clearer `æ¶…æ§ƒå¿ƒ / å·®åˆ¥æ™º / å®¶åœ‹è‡ªå®‰å¯§` cluster plus the dated `æ…§é–‹è¬¹è­˜` sign-off.

### PDF p.049 right leaf

- Role: end-matter title leaf
- Confidence: medium

#### Consolidated Readable Text

```text
ç„¡é–€å·
```

#### Notes

- This is the clearest title-like marker in the end matter sequence.

### PDF p.049 left leaf

- Role: end-matter prose / admonitory material
- Confidence: low

#### Consolidated Readable Text

```text
å„±ä¾—å®ˆç¦ªå¨å„€ï¼Œ
無繩自縛，
ç¸±æ©«ç„¡ç¢ã€‚
å¤–é“é­”è»å­˜å¿ƒï¼Œ
澄寂黑照邪禪。
èžè½æ·±å‘ï¼Œ
æ‡žç„¶ä¸æ˜§ã€‚
帶鎖擔枷，
æ€å–„æ€æƒ¡ã€‚
åœ°ç„å¤©å ‚ï¼Œ
佛見法見，
äºŒéµåœå±±ã€‚
å¿µèµ·å³è¦ºï¼Œ
é€²å‰‡è¿·ç†ï¼Œ
退則乖宗，
ä¸é€²ä¸é€€ã€‚
有氣死人，
ä¸”é“å¦‚ä½•å±¥è¸ã€‚
努力今生。
```

#### Notes

- The leaf is reflective/admonitory prose, not case text.
- The block above is now readable in substance from the witness image.
- OCR and image together support the added closing cadence `å¿µèµ·å³è¦º / é€²å‰‡è¿·ç† / é€€å‰‡ä¹–å®— / ä¸é€²ä¸é€€`.
- OCR and image also support the additional warning cluster `åœ°ç„å¤©å ‚ / ä½›è¦‹æ³•è¦‹ / äºŒéµåœå±±` and the closing push `æœ‰æ°£æ­»äºº / ä¸”é“å¦‚ä½•å±¥è¸ / åŠªåŠ›ä»Šç”Ÿ`.
- The remaining edge material is now mostly degraded continuation rather than a clearly separable new block.

### PDF p.050 right leaf

- Role: end-matter prose / verse-like material
- Confidence: low

#### Consolidated Readable Text

```text
é Œäº†å´èŽ«æ•™æ°¸åŠ«å—é¤˜æ®ƒã€‚

ã€”é»ƒé¾ä¸‰é—œã€•

我手何似佛手。
我脚何似驢脚。
人人有箇生緣處。
元來通身是手。
å››æµ·æ©«è¡Œå€’è·¨æ¥Šå²ä¸‰è„šã€‚
```

#### Notes

- `RapidOCR` also supports `元來通身是手`, which is now strong enough to include.
- OCR and image also support the framing line `é Œäº†å´èŽ«æ•™æ°¸åŠ«å—é¤˜æ®ƒ` and the closing motion line `å››æµ·æ©«è¡Œå€’è·¨æ¥Šå²ä¸‰è„š`.
- The inner explanatory prose between those lines remains compressed and is not yet stable enough to normalize further.

### PDF p.050 left leaf

- Role: end-matter prose
- Confidence: low

#### Consolidated Readable Text

```text
人以有箇生緣，
å„å„é€å¾®æ©Ÿã€‚
å…ˆé‚£å’æŠ˜éª¨é‚„çˆ¶ã€‚
五祖豈鑒爺娘。
å‡¡è–è·¯é ­ä¿±æˆªæ–·ï¼Œ
幾多蜂蟻起雷音。
```

#### Notes

- OCR and image support the phrase family `äººä»¥æœ‰ç”Ÿç·£ / å„äººé€å¾®æ©Ÿ / æŠ˜éª¨é‚„çˆ¶ / äº”ç¥–è±ˆé‘’çˆºå¨˜`.
- The lower verse tail `å‡¡è–è·¯é ­ä¿±æˆªæ–· / å¹¾å¤šèœ‚èŸ»èµ·é›·éŸ³` is also now visible enough to include.
- The middle compressed prose remains weaker than the opening and closing lines.

### PDF p.051 right leaf

- Role: end-matter prose
- Confidence: low

#### Consolidated Readable Text

```text
ç„¡é–€é¦–åº§ç«‹åƒ§å±±å€Ÿå¥‰è¬ç´¹å®šåºšå¯…å­£æ˜¥ç„¡é‡å®—å£½æ›¸è´Š
```

#### Notes

- `RapidOCR` also preserves the surrounding phrase family:
  - `é”ç£¨è¥¿ä¾†ä¸åŸ·æ–‡å­—ç›´æŒ‡äººå¿ƒè¦‹æ€§æˆä½›`
  - `ç„¡é–€é¦–åº§ç«‹åƒ§å±±å€Ÿå¥‰è¬ç´¹å®šåºšå¯…å­£æ˜¥ç„¡é‡å®—å£½æ›¸è´Š`
- The leaf also visibly preserves the surrounding admonitory cadence:
  - `æˆä½›èªªç®‡ç›´æŒ‡å·²æ˜¯è¿‚æ›²æ›´è¨€æˆä½›`
  - `無門因甚有關`
  - `è€å©†å¿ƒåˆ‡`
  - `æƒ¡è²æµå¸ƒ`
- The line is best treated as compressed but coherent colophon/dedicatory prose.
- `å€Ÿ` is retained as the working reading in `ç«‹åƒ§å±±å€Ÿå¥‰è¬`, with the phrase understood as a humility/compression marker rather than a literal borrowing verb.

### PDF p.051 left leaf

- Role: end-matter / patron or printing information
- Confidence: low-medium

#### Consolidated Readable Text

```text
å››åä¹å‰‡å…¶é–“äº›å­ï¼Œ
è«‹èªåˆ¥èµ·çœ‰æ¯›ã€‚
æª¢æ ¡ä¿å¯§è»ç¯€åº¦ä½¿äº¬æ¹–å®‰æ’«åˆ¶ç½®å¤§ä½¿å…¼çŸ¥æ±Ÿé™µåºœæ¼¢æ±éƒ¡é–‹åœ‹å…¬é£Ÿé‚‘
äºŒåƒä¸€ç™¾æˆ¶é£Ÿå¯¦å°é™¸ä½°æˆ¶
å­Ÿç™
```

#### Notes

- This leaf appears to include administrative or patronage matter rather than case text.
- The administrative block is now readable in substance from the witness image.
- Coarse OCR, refined OCR, and the crop pass do not reveal a clean omitted line beyond the block already transcribed here.
- Office-title and personal-name graphs may still admit later tightening, but this is no longer just a one-phrase stub.

### PDF p.052 right leaf

- Role: weak end-matter leaf
- Confidence: low

#### Consolidated Readable Text

```text
〔seals / no legible running text recovered〕
```

#### Notes

- `RapidOCR` returned no result for this leaf.

### PDF p.052 left leaf

- Role: end-matter prose
- Confidence: low

#### Consolidated Readable Text

```text
ç„¡é–€è€ç¦ªä½œå››åå…«å‰‡èªžï¼Œ
åˆ¤æ–·å¤å¾·å…¬æ¡ˆã€‚
大似黃油餅人，
ä»¤è²·å®¶é–‹å£æŽ¥ã€‚
å®‰æ™šæ¬²å°±æ¸ ç†±çˆä¸Šå†æ‰“ä¸€æ’¥ï¼Œ
è¶³æˆå¤§è¡ä¹‹æ•¸ã€‚
```

#### Notes

- The leaf is stronger than a single-phrase stub.
- OCR and image also support a further continuation around `å®‰æ™šæ¬²å°± / æ¸ ç†±çˆä¸Šå†æ‰“ä¸€æ’¥ / è¶³æˆå¤§è¡ä¹‹æ•¸`.
- The remaining lower lines are still too unstable for a fuller diplomatic recovery.

### PDF p.053 right leaf

- Role: later end-matter note
- Confidence: low

#### Consolidated Readable Text

```text
ç¬¬å››åä¹å‰‡èªž
頌云：
æ­¢æ­¢ä¸é ˆèªªæˆ‘æ³•å¦™é›£æ€ã€‚
æ³•å¾žä½•ä¾†ï¼Œå¦™å¾žä½•èªªæ™‚ï¼Œåˆä½œéº¼ç”Ÿã€‚
ç”Ÿè±ˆä½†è±å¹²é¥’èˆŒï¼Œ
å…ƒæ˜¯é‡‹è¿¦å¤šå£ã€‚
è€å­é€ ä½œå¥½æ€ªï¼Œ
ä»¤åƒç™¾ä»£å…’å­«è¢«è‘—ã€‚
è—¤çºå€’ï¼Œæœªå¾—é ­å‡ºï¼Œ
æ°ä¼¼é€™èˆ¬å¥‡ç‰¹è©±é ­ã€‚
èµ·è·³ä¸æ­¢ï¼Œé£¯è’¸ä¸ç†Ÿï¼Œ
æœ‰å¤šå°‘éŒ¯èªè™•ã€‚
```

#### Notes

- `ç¬¬å››åä¹å‰‡èªž` appears clearly enough in OCR to log.
- The upper block is stronger than the earlier one-line stub.
- OCR and image both support the added lower warning lines around `è±å¹²é¥’èˆŒ / é‡‹è¿¦å¤šå£ / è—¤çºå€’ / æœªå¾—é ­å‡º / å¥‡ç‰¹è©±é ­ / èµ·è·³ä¸æ­¢ / é£¯è’¸ä¸ç†Ÿ / éŒ¯èªè™•`.

### PDF p.053 left leaf

- Role: later end-matter prose
- Confidence: low

#### Consolidated Readable Text

```text
å‚äººå•äº‘ï¼š
ç•¢ç«Ÿä½œå¦‚ä½•çµæ–·ã€‚
å®‰æ™šåˆåæŒ‡çˆªæ›°ï¼š
æ­¢æ­¢ä¸é ˆèªªæˆ‘æ³•å¦™é›£æ€ã€‚
å´æ€¥åŽ»é›£æ‚£å…©å­—ä¸Šæ‰“ç®‡å°åœ“ç›¸å­ï¼Œ
指示衆人云：
ç¸½åœ¨è£è¨±ã€‚
```

#### Notes

- This leaf is materially stronger than the earlier placeholder state.
- The prose block above is now readable in substance from the witness image.
- A separate left-side verse/comment area remains present but not yet fully normalized.

### PDF p.054 right leaf

- Role: colophon / place and date note
- Confidence: low-medium

#### Consolidated Readable Text

```text
æ›¸äºŽè¥¿æ¹–æ¼èŽŠã€‚
æ·³ç¥ä¸™åˆå­£å¤åˆå‰ï¼Œ
安晚居士
```

#### Notes

- This is one of the clearer colophon leaves.
- The full right-side date/place/signature column is stable from the witness image.

### PDF p.054 left leaf

- Role: printing / block history note
- Confidence: medium

#### Consolidated Readable Text

```text
èˆŠæ¿ç£¨æ»…æ•…é‡å‘½å·¥ã€‚
æ¢“é€™æ¿ç½®æ–¼æ­¦è—å·žï¼Œ
駒牟山廣圓禪寺也。
æ‡‰æ°¸ä¹™é…‰åæœˆåä¸‰æ—¥ï¼Œ
幹緣比丘常牧。
```

#### Notes

- This is the clearest printing-history leaf in the end matter.
- Column order is now normalized to the witness sequence.
- The place-name and sponsor line are visible enough to retain, though one or two graphs in the recutting line may still admit later tightening.

### PDF p.055 right leaf

- Role: later colophon note
- Confidence: low-medium

#### Consolidated Readable Text

```text
å¯¬æ°¸ä¹å¹´å£¬ç”³ä¹æœˆ
中野宗左衛門刊行
```

#### Notes

- The date line is the strongest part of the leaf.
- The boxed `å¯¬æ°¸ä¹å¹´å£¬ç”³ä¹æœˆ / ä¸­é‡Žå®—å·¦è¡›é–€åˆŠè¡Œ` block is stable.
- The lighter side columns remain too weak for a cleaner reading on this pass.

### PDF p.055 left leaf

- Role: weak end-matter leaf
- Confidence: low

#### Consolidated Readable Text

```text
〔blank / no legible text recovered〕
```

#### Notes

- `RapidOCR` returned no result for this leaf.

## Next Targets

- verify the compressed middle run leaf by leaf where multiple short cases share one page sequence
- expand provisional witness runs into fuller diplomatic transcriptions where the image supports it
- separate end matter and printing notes more precisely from the 48-case body text
- leave damaged or low-confidence leaves explicitly marked rather than silently normalized
