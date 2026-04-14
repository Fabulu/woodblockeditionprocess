# PDF p.006 Right Leaf

## OCR

Command family used:

- `tesseract ... -l chi_tra_vert`
- `tesseract ... -l chi_tra`

Result quality:

- very noisy
- enough to confirm this is the opening prose leaf
- not reliable enough for direct transcription without image-based correction

## Agent Read A

Summary:

- identified the page as opening prose for the collection
- extracted the core claims about the text becoming a set of 48 cases called `無門關`

Best-effort transcription returned:

```text
ä½œæ•²é–€ã€”ç“¦/è‰²ã€•å­ï¼Œéš¨æ©Ÿå¼•å°Žèˆ‡è€…ï¼Œç«Ÿçˆ¾æŠ„éŒ„ã€‚
ä¸è¦ºæˆé›†ï¼Œåˆä¸ä»¥ã€”å…ˆ/å‰ã€•å¾Œï¼Œã€”å”/å­£/åˆŠã€•å…±æˆã€‚
å››åå…«å‰‡ï¼Œé€šæ›°ç„¡é–€é—œã€‚
è‹¥æ˜¯ç®‡æ¼¢ï¼Œç›´å…¥å…«è‡‚é‚£å’ï¼Œæ””ä»–ä¸ä½ã€‚
ç¸±ä½¿è¥¿å¤©å››ä¸ƒï¼Œæ±åœŸäºŒä¸‰ï¼Œåªå¾—æœ›é¢¨ã€”è€Œé€€/è€Œèµ°ã€•ã€‚
ã€”è¦“/å¾—ã€•çœ¼ä¾†æ—©å·²è¸éŽä¹Ÿã€‚
```

## Agent Read B

Summary:

- mistakenly described the page as the title / contents leaf
- still converged on the same core opening lines about the compilation of 48 cases

Best-effort transcription returned:

```text
ä½œæ•²é–€ã€”?ã€•å­ï¼Œéš¨æ©Ÿå¼•å°Žèˆ‡è€…ï¼Œç«Ÿçˆ¾æŠ„ä¸è¦ºæˆé›†ã€‚
åˆä¸ä»¥å‰å¾Œã€”?ã€•åˆ—ï¼Œç«Ÿæˆå››åå…«å‰‡ï¼Œé€šæ›°ç„¡é–€é—œã€‚
```

## Architect Takeaway

- the independent readers agree on the identity of the prose and the core sentence:
  `...å…±æˆå››åå…«å‰‡ï¼Œé€šæ›°ç„¡é–€é—œ`
- line-level reading remains uncertain in several places
- the next pass should use tighter crops per column or per text frame
