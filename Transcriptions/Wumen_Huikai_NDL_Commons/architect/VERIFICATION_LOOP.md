# Cross-Witness Verification Loop

## Scope

- Base witness: `C:\woodblocks\Transcriptions\Wumenguan_1632_NDL_Commons\architect\WUMENGUAN_1632.md`
- Corroborating witness: `C:\woodblocks\Transcriptions\Wumen_Huikai_NDL_Commons`
- Goal: use the second witness to test weak readings, not to overwrite the 1632 witness by habit.

## Loop

1. Pick one target from the 1632 draft.
   - unresolved graph
   - weak leaf
   - suspicious case boundary
   - colophon/end-matter uncertainty
2. Anchor the target in the second witness.
   - case title
   - nearby lemma
   - verse incipit
   - named person or place
3. Pull evidence from the second witness.
   - cropped frame image
   - Tesseract refined OCR
   - RapidOCR
   - PaddleOCR
   - independent agent reading if still unclear
4. Classify the result.
   - `confirms 1632`
   - `clarifies weak 1632 graph`
   - `shows witness divergence`
   - `still inconclusive`
5. Patch the 1632 draft only if the change is actually supported.
6. Record the decision and evidence path in `SECOND_WITNESS_CORROBORATIONS.md`.

## Priority Order

1. remaining weak spots in the 1632 body
2. weak end-matter leaves
3. suspect case transitions
4. broad audit for large witness divergences

## Audit Pass After Spot Fixes

After the hard loci are done, run a broad witness audit:

1. map case anchors across the whole second witness
2. compare case openings and verse openings
3. flag major omissions, additions, reordered matter, and divergent end matter
4. log all non-trivial differences before any editorial normalization
