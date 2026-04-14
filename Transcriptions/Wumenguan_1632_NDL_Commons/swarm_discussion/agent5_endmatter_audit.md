# End-Matter Audit: p.049-p.055

Scope: local leaf images plus the existing `batch_refined` OCR artifacts only. No outside witnesses used.

## Findings

- `p.049 left` is still undertranscribed. The current four-line verse in the main draft is too smooth and too compressed for what the image/OCR show. The local OCR is noisy, but it repeatedly supports a denser admonitory passage with recoverable phrases like `ç„¡ç¢å¤–é“`, `å¦‚ä½•å¦¨ä»Šç”Ÿ`, `æ¾„å¯‚é»žç…§é‚ªç¦ª`, and `å…€ç„¶ç¿’å®š`. This leaf should be re-read as a full text block rather than kept as a generic verse summary.

- `p.050 right` should be expanded. The current draft only preserves the short three-line core, but the OCR/image support the heading `é»ƒé¾ä¸‰é—œ` plus additional recoverable lines, including `æˆ‘æ‰‹ä½•ä¼¼ä½›æ‰‹`, `æˆ‘è„šä½•ä¼¼é©¢è„š`, `å¤§ç¬‘å‘µä¹‹`, and `å…ƒä¾†é€šèº«æ˜¯æ‰‹`. This is high-confidence local recovery.

- `p.050 left` is also too conservative. The OCR supports a fuller passage than the current `äººä»¥æœ‰ç®‡ç”Ÿç·£...` summary, with recoverable phrases such as `å‡¡è·¯é ­ä¿±æˆªæ–­`, `ç‘žæ—¥...åˆ¤å¤ä»Š`, `ä½›æœª...éžä½›éžé“éžèŽ«æ€ª`, `æŠ˜éª¨é‚„çˆ¶`, `ç„¡é–€...`, `äººä»¥æœ‰ç”Ÿå„äººé€å¾®æ©Ÿå…ˆ...`, and a trailing `è«‹`. The middle characters are still partly unstable, but the leaf clearly contains more text than is currently represented.

- `p.051 right` is not just the signature block currently kept in the draft. The frame OCR recovers multiple opening lines before the colophon, including `æˆä½›ç›´æŒ‡...`, `å¿ƒåˆ‡æƒ¡è²æµå¸ƒ`, `éƒŽç•¶ä¸å°‘`, and `ç›´æŒ‡äººå¿ƒè¦‹æ€§`. Keep the signature/colophon block, but do not collapse the leaf to that alone.

- `p.051 left` has a secure core phrase, but the draft omits the surrounding administrative/patronage matter. OCR supports `å››åä¹å‰‡å…¶é–“äº›å­èµ·çœ‰æ¯›` and also a surrounding block with date/patronage information. If the architecture wants a complete end-matter transcription, this leaf should include that extra metadata text instead of only the central phrase.

- `p.052 left` is recoverable beyond the current two-line summary. The strongest local phrase is `ç„¡é–€è€ç¦ªä½œå››åå…«èªž...åˆ¤æ–·å¤å¾·`, and the surrounding OCR also suggests additional explanatory lines about the composition process. The present transcription is safe, but it is still too short for the available witness.

- `p.053 right` has a secure heading, but the leaf is more than a one-line marker. The OCR supports `ç¬¬å››åä¹å‰‡èªž` and also a short explanatory block on the same leaf. Keep the heading, but do not treat the whole leaf as exhausted by that single line.

- `p.053 left` is mostly fine in the current draft. The local OCR supports the dialogue core `å‚äººå•äº‘...ç•¢ç«Ÿä½œå¦‚ä½•çµæ–·...æ­¢æ­¢ä¸é ˆèªªæˆ‘æ³•å¦™é›£æ€`, so only minor punctuation/segmentation cleanup looks warranted here.

- `p.055 left` still has no secure recovery from the local witnesses. `RapidOCR` returned no result, and I do not see a safe upgrade beyond the current blank/uncertain status.

## Conclusion

The highest-value reopen items are `p.050 right`, `p.050 left`, `p.051 right`, and `p.052 left`. `p.049 left` also merits another manual pass, but the text there is still less stable than the other leaves. `p.055 left` currently looks genuinely unrecoverable from the local OCR set.
