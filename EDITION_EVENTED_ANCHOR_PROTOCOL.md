# Edition Evented Anchor Protocol

**Version:** 1.0  
**Status:** Required for all new edition projects going forward  
**Applies to:** Any AI or human agent performing critical edition work under ReadZen/OpenZen

---

## Purpose

ReadZen can only offer trustworthy time-travel, evidence zoom, and witness drilldown if editorial changes are tied to stable image anchors.

This protocol defines the mandatory anchor layer for future editions:

- every accepted or rejected text-changing event must carry an anchor packet
- every anchor packet must point to the exact source asset used at the moment of judgment
- translation time-travel must stay synchronized with the same event ids

This is **evented**, not snapshot-based. You do **not** rebuild the whole text geometry at every step. You record stable anchors once, then record deltas for the loci that changed.

---

## Core model

There are two required layers.

### 1. Base anchor layer

Stable geometry and asset metadata for a witness locus.

### 2. Event delta layer

The editorial change tied to that locus, including before/after text and the anchor packet used to justify it.

---

## Required files

All files live under:

```
provenance/{slug}/process/
```

Required new files:

```
anchor-base-register.jsonl      <- stable page/locus anchors
anchor-event-log.jsonl          <- event-level before/after anchor packets
```

These are required in addition to the existing markdown logs.

---

## 1. anchor-base-register.jsonl

One JSON object per stable anchorable locus.

Minimum schema:

```json
{
  "anchor_id": "T1-p007.l09@T1",
  "witness_id": "T1",
  "page_id": "T1-p007",
  "locus_id": "T1-p007.l09",
  "source_asset_path": "provenance/faith-in-mind/ocr/T1/page-images/T1-p007.png",
  "source_download_url": "https://commons.wikimedia.org/wiki/Special:Redirect/file/CNTS-00047968260_三祖大師信心銘.pdf",
  "source_kind": "page_image",
  "page_number": 7,
  "page_bbox": [0.0, 0.0, 1.0, 1.0],
  "locus_bbox": [0.58, 0.22, 0.08, 0.51],
  "polygon": null,
  "crop_asset_path": "provenance/faith-in-mind/process/visual-workbench-holdouts/T1-p007/T1-p007-lower-cluster-rot90-mirror-hi.png",
  "ocr_region_ref": "paddleocr-ppocrv4:T1-p007:dt_polys[5]",
  "char_boxes": [],
  "notes": "Curated lower-cluster anchor for reopened manual segmentation review."
}
```

### Required fields

- `anchor_id`
- `witness_id`
- `page_id`
- `locus_id`
- `source_asset_path`
- `source_kind`
- `page_bbox`
- `locus_bbox`

### Optional but strongly preferred

- `source_download_url`
- `crop_asset_path`
- `ocr_region_ref`
- `polygon`
- `char_boxes`
- `notes`

### Rules

- `page_bbox` and `locus_bbox` use normalized `[x, y, width, height]` coordinates from `0.0` to `1.0`
- `char_boxes` are optional and should be used only when the locus was genuinely contested at character level
- `polygon` may be used instead of or alongside `locus_bbox` if OCR or manual geometry is polygonal

---

## 2. anchor-event-log.jsonl

One JSON object per editorial event affecting a locus.

Minimum schema:

```json
{
  "event_id": "FIM-456",
  "event_date": "2026-05-06",
  "edition_slug": "faith-in-mind",
  "locus_id": "T1-p007.l09",
  "witness_id": "T1",
  "before_text": "巍有语言是掉择是明日三想大",
  "after_text": "師云住總有語言是揀擇",
  "translation_before": "Lofty being-language is selection, tomorrow three thoughts great.",
  "translation_after": "The master said, \"Stop. To have language at all is picking and choosing.\"",
  "change_type": "human_directed_visual_promotion",
  "status": "accepted",
  "anchor_ids": ["T1-p007.l09@T1"],
  "source_asset_path": "provenance/faith-in-mind/ocr/T1/page-images/T1-p007.png",
  "source_download_url": "https://commons.wikimedia.org/wiki/Special:Redirect/file/CNTS-00047968260_三祖大師信心銘.pdf",
  "page_id": "T1-p007",
  "page_bbox": [0.0, 0.0, 1.0, 1.0],
  "locus_bbox": [0.58, 0.22, 0.08, 0.51],
  "char_boxes": [
    {"position": 1, "char": "師", "bbox": [0.60, 0.23, 0.02, 0.05]},
    {"position": 4, "char": "總", "bbox": [0.60, 0.35, 0.02, 0.05]}
  ],
  "evidence_type": "page_image_plus_local_ocr_support",
  "confidence": "moderate",
  "basis_note": "Accepted from direct page review plus convergent Paddle local frame; trailing OCR debris rejected."
}
```

### Required fields

- `event_id`
- `event_date`
- `edition_slug`
- `locus_id`
- `witness_id`
- `before_text`
- `after_text`
- `translation_before`
- `translation_after`
- `change_type`
- `status`
- `anchor_ids`
- `source_asset_path`
- `page_id`
- `page_bbox`
- `locus_bbox`
- `evidence_type`
- `confidence`

### Optional

- `source_download_url`
- `char_boxes`
- `basis_note`
- `polygon`
- `crop_asset_path`
- `ocr_region_ref`

---

## Character-box policy

Character boxes are **not required for every locus**.

They are required when:

- a change was accepted at character level
- a single graph was restored, rejected, supplied, or rolled back
- a character-click forensic UI is expected for that locus

They are optional when:

- the locus was unchanged
- the judgment was only page-level or line-level
- the witness is too degraded for responsible per-character geometry

This keeps the workflow realistic.

---

## Capture timing rules

### MUST capture immediately for:

- every accepted Chinese text change
- every rollback
- every rejected reading that remains editorially significant
- every new line insertion
- every omission judgment affecting publication text

### SHOULD capture immediately for:

- contested no-change outcomes
- major corroborative comparisons
- manual visual judgment calls

### MUST NOT defer indefinitely

If the agent used a page, crop, OCR box, or witness image to make a decision, the anchor packet must be recorded **in the same bounded session**.

---

## Acceptable evidence basis

Each event must declare one of:

- `page_image_only`
- `page_image_plus_ocr`
- `helper_crop_only`
- `ocr_region_only`
- `cross_witness_plus_image`
- `human_judgment_call`
- `rollback_after_image_review`

If more than one applies, use the most informative combined label and explain in `basis_note`.

---

## Cross-file integrity constraints

1. Every accepted correction-log row must have:
   - a translation-diff row
   - an anchor-event row

2. Every anchor-event row must point to at least one anchor-base row through `anchor_ids`.

3. `event_id` should match the corresponding timeline event when one exists.

4. If `status = accepted` and `before_text != after_text`, then:
   - `translation_before` and `translation_after` must both be present

5. If `char_boxes` are recorded, their `position` values must be 1-based and must refer to the `after_text` string unless explicitly noted otherwise.

---

## Retroactive backfill policy

For older editions, do **not** try to create full geometry for every line immediately.

Instead:

1. Backfill anchor packets for every **changed or contested** poem locus.
2. Use page-level and locus-level boxes first.
3. Add character boxes only where the editorial decision actually turned on individual graphs.
4. Treat untouched stable loci as page/locus-addressable only unless later UI needs force more detail.

This is the approved backfill strategy for legacy projects.

---

## Validation target

Future package validation should fail if:

- a new accepted correction lacks an anchor-event row
- an anchor-event row lacks a source asset or locus geometry
- a changed locus has no synchronized translation before/after

This requirement is now part of edition workflow law.
