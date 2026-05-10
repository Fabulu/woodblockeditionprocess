# OCR Startup Evidence Requirements

Date: `2026-05-10`  
Status: binding before the first OCR-first transcription slice

## Purpose

The ReadZen side can now expose:

- evidence-tier transparency
- character-level evidence notices when `char_boxes` are present
- synchronized Chinese/translation time travel tied to anchor events

So `song-of-enlightenment` must not begin OCR as if geometry were optional exhaust.

## Mandatory preflight rules

### 1. Tiered evidence capture

Every poem locus must be capable of landing in:

- Tier 1 `page`
- Tier 2 `line`

Any locus likely to appear in `apparatus.json` must be prepared for:

- Tier 3 `character`

Tier 4 `cross_witness_character` is optional and only applies if later multi-witness character alignment is actually performed.

### 2. Anchor fields

Before handoff or later comparison, package-local anchor rows must expose:

- `evidence_tier`
- `char_coverage`

If OCR starts before those fields are planned, later time-travel and evidence UI will drift.

### 3. PaddleOCR setting

For this edition, PaddleOCR must be run with:

```text
return_word_box: True
```

Reason:

- the app can now surface character-level evidence directly
- contested poem loci should not require a later geometry reconstruction if OCR already had access to word or character boxes

### 4. Minimum locus geometry promise

The next OCR-first tranche must guarantee:

- page-level anchorability for every poem line
- line-level `locus_bbox` for every poem line
- best-effort character boxes for contested loci

### 5. Translation sync rule

Once Chinese text work starts, translation must change in the same bounded slice.

No accepted Chinese correction may land without:

- `translation-diff-log.md`
- `translation-reasoning-log.md` when the English decision is non-trivial
- matching `anchor-event-log.jsonl` event data

## Immediate next slice

The next bounded slice is:

`ocr_startup_slice_first_tier_exact_core_with_tiered_evidence_capture`

That slice should:

1. declare the first OCR witness tranche from the held first-tier exact core
2. open OCR engine directories and status surfaces
3. ensure Paddle is configured for word boxes
4. create line-ready anchor planning for the poem loci before adjudication starts
