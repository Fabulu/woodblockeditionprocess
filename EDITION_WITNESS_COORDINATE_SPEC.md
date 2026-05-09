# Witness Coordinate Specification for ReadZen Integration

**Version:** 1.0
**Date:** 2026-05-09
**Status:** Mandatory for all new critical editions

## Purpose

Defines the coordinate data that critical edition packages must produce so ReadZen can offer character-click → witness page viewing with zoom and highlight overlay.

## Required Files

### 1. anchor-base-register.jsonl

One JSON object per line. Each entry maps a textual locus to a physical location on a witness page.

**Required fields:**

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `anchor_id` | string | Unique ID: `{locus_id}@{witness_id}` | `T1-p031.l01@T1` |
| `witness_id` | string | Witness siglum | `T1` |
| `page_id` | string | Page identifier | `T1-p031` |
| `locus_id` | string | Textual locus | `T1-p031.l01` |
| `source_asset_path` | string | Relative path to page image | `provenance/.../T1-p031.png` |
| `source_kind` | string | Always `page_image` | `page_image` |
| `page_bbox` | array | Full page: `[0.0, 0.0, 1.0, 1.0]` | `[0.0, 0.0, 1.0, 1.0]` |
| `locus_bbox` | array | `[x, y, width, height]` normalized 0-1 | `[0.04, 0.04, 0.92, 0.20]` |

**Optional fields:**

| Field | Type | Description |
|-------|------|-------------|
| `source_download_url` | string | URL to download witness (Commons redirect or IIIF manifest) |
| `page_number` | int | Page number for PDF witnesses |
| `char_boxes` | array | Per-character bboxes: `[[x,y,w,h], ...]` |
| `polygon` | array | Polygon coordinates for non-rectangular regions |
| `crop_asset_path` | string | Path to pre-cropped region image |
| `ocr_region_ref` | string | Reference to OCR region data |
| `notes` | string | Editorial context |

### 2. Bounding Box Coordinate System

- All coordinates normalized to `[0.0, 1.0]` relative to page dimensions
- Format: `[x_min, y_min, width, height]`
- Origin: top-left corner of page
- Example: `[0.04, 0.04, 0.92, 0.20]` = starts 4% from left, 4% from top, spans 92% width, 20% height
- For full page: `[0.0, 0.0, 1.0, 1.0]`

### 3. TEI XML Requirements

Each poem line MUST have `n` and `corresp` attributes:

```xml
<l n="22" corresp="urn:locus:T1-p031.l01">縱有是非紛然失心</l>
```

- `n`: Sequential line number (used for TeiRenderer segment keys `l|22`)
- `corresp`: URN pointing to locus ID (used for apparatus + anchor lookup)
- `type` (optional): e.g., `type="omission_judgment"` for special loci

ReadZen maps: click → segment `l|22` → LociMappingService → `urn:locus:T1-p031.l01` → apparatus/anchor lookup.

### 4. apparatus.json Requirements

Each entry MUST have `locus_id` matching the TEI `corresp` value (without the `urn:locus:` prefix).

Required fields per entry: `locus_id`, `lemma`, `readings[]`, `decision`, `decision_basis`, `status`.

### 5. Witness Source URLs in manifest.json

Each witness in `witnesses_consulted[]` MUST have `upstream_url`:

- **Commons PDFs**: `https://commons.wikimedia.org/wiki/Special:Redirect/file/{filename}`
- **Kyoto IIIF**: `https://rmda.kulib.kyoto-u.ac.jp/item/{record_id}`
- **Other IIIF**: Standard IIIF Image API v3 endpoint

### 6. Page Number Derivation

ReadZen derives page numbers from locus IDs:

- `T1-p031.l01` → page 31 (parse digits after `-p`)
- `T4-p002.poem-band` → page 2
- For PDFs: page number is 0-indexed internally (subtract 1 from display number)
- For IIIF: image filename = `{record_id}_{page_number:05d}`

### 7. When to Capture Coordinates

**During edition production (not as backfill):**

- Every accepted text-changing correction → anchor-event row + anchor-base row
- Every apparatus entry locus → anchor-base row with locus bbox
- Every supplied or omitted locus → anchor-base rows for BOTH T1 and comparison witness

**Minimum coverage:**

- Every locus referenced in `apparatus.json` MUST have an anchor-base entry
- Every poem line SHOULD have at least a page-level anchor
- If line-level bbox is unavailable, use full page bbox and note it

### 8. Witness Type Handling

**PDF witnesses (e.g., Wikimedia Commons):**
- Single PDF file per witness
- `page_number` field required in anchor-base
- ReadZen renders specific page via Docnet.Core (Pdfium)

**IIIF witnesses (e.g., Kyoto University):**
- Individual JPEG pages per witness
- IIIF Image API URL pattern: `https://.../iiif/3/{ID}%2F{FILENAME}_0.ptif/full/max/0/default.jpg`
- ReadZen downloads full-resolution page on demand

### 9. Examples

**Minimal anchor-base (PDF witness):**
```json
{"anchor_id":"T1-p031.l01@T1","witness_id":"T1","page_id":"T1-p031","locus_id":"T1-p031.l01","source_asset_path":"provenance/faith-in-mind/ocr/T1/page-images/T1-p031.png","source_kind":"page_image","page_number":31,"page_bbox":[0.0,0.0,1.0,1.0],"locus_bbox":[0.04,0.04,0.92,0.20],"notes":"Corrected opening graph"}
```

**Comparison witness (IIIF):**
```json
{"anchor_id":"T4-p002.poem-band@T4","witness_id":"T4","page_id":"T4-p002","locus_id":"T4-p002.poem-band","source_asset_path":"provenance/faith-in-mind/ocr/T4/page-images/T4-p002.png","source_download_url":"https://rmda.kulib.kyoto-u.ac.jp/item/rb00009461","source_kind":"page_image","page_bbox":[0.0,0.0,1.0,1.0],"locus_bbox":[0.10,0.30,0.80,0.40],"notes":"Opening poem band with supplied line T1-p021.l01a"}
```

**With character boxes:**
```json
{"anchor_id":"T1-p031.l01@T1","witness_id":"T1","page_id":"T1-p031","locus_id":"T1-p031.l01","source_asset_path":"provenance/faith-in-mind/ocr/T1/page-images/T1-p031.png","source_kind":"page_image","page_bbox":[0.0,0.0,1.0,1.0],"locus_bbox":[0.04,0.04,0.92,0.20],"char_boxes":[[0.05,0.06,0.08,0.12],[0.14,0.06,0.08,0.12]]}
```

### 10. Validation Checklist

Before handoff to ReadZen:

- [ ] Every apparatus locus_id appears in anchor-base-register.jsonl
- [ ] Every anchor-base entry has valid locus_bbox (not all zeros)
- [ ] Every TEI `<l>` element has both `n` and `corresp` attributes
- [ ] manifest.json `witnesses_consulted[]` entries have `upstream_url`
- [ ] Page numbers derivable from locus IDs match actual witness page images
- [ ] JSONL files parse without errors (one valid JSON object per non-empty line)
