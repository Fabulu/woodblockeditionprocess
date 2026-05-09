# Edition Forensic Provenance Protocol

**Version:** 1.1  
**Status:** Required for all critical edition projects  
**Applies to:** Any AI or human agent performing critical edition work under ReadZen/OpenZen

---

## Purpose

The provenance system makes every editorial decision reproducible. Given the structured logs, anchor packets, and source assets, a reviewer can reconstruct every character choice, verify OCR consensus, audit rejected readings, challenge any translation decision, and jump to the exact evidence used when a text state changed.

---

## File locations

```
provenance/{slug}/process/
  correction-log.md              <- Chinese text corrections
  translation-diff-log.md        <- Bilingual retranslation diffs
  ocr-consensus-log.md           <- Per-locus OCR engine agreement
  rejected-readings-log.md       <- Readings considered and discarded
  translation-reasoning-log.md   <- Why each English rendering was chosen
  character-provenance-log.md    <- Per-character source and confidence
  anchor-base-register.jsonl     <- Stable page/locus anchors
  anchor-event-log.jsonl         <- Event-level anchor packets
```

App discovery: `xml-open/{kind}/{slug}/ -> ../../../provenance/{slug}/process/`

---

## 1. correction-log.md

| Date | Locus | Change type | Before | After | Basis | Status |
|------|-------|-------------|--------|-------|-------|--------|

All text fields backtick-delimited.  
Change type: `OCR certainty fix`, `visual certainty fix`, `comparison-supported certainty fix`, `visual de-certainty rollback`, `human judgment call`.  
Status: `fixed`, `superseded by visual fix`, `provisional`, `rolled back`.

**Image evidence** (legacy extended fields still allowed): `EvidencePdf`, `EvidencePage`, `EvidenceRegionX`, `EvidenceRegionY`, `EvidenceRegionWidth`, `EvidenceRegionHeight`.

**Must:** Every accepted correction also generates:

- a corresponding translation-diff row
- a corresponding anchor-event row

---

## 2. translation-diff-log.md

Fully specified in `EDITION_TRANSLATION_DIFF_PROTOCOL.md`.

| Step | Locus | Chinese Before | Chinese After | English Before | English After | Basis |
|------|-------|---------------|---------------|----------------|---------------|-------|

**Must:** Step 0 covers every text-bearing locus. Step numbers match correction-log entries.

---

## 3. ocr-consensus-log.md

| Locus | Tesseract | RapidOCR | PaddleOCR | EasyOCR | Agreement | Adopted | Basis |
|-------|-----------|----------|-----------|---------|-----------|---------|-------|

Engine columns backtick-delimited. Use `—` if an engine was unavailable. Agreement: `4/4`, `3/4`, etc. Adopted: backtick-delimited final reading.

**Must:** One row per locus where OCR was consulted.  
**Should:** Include full-agreement loci too.

---

## 4. rejected-readings-log.md

| Locus | Rejected | Source | Adopted | Reason | Date |
|-------|----------|--------|---------|--------|------|

Locus, Rejected, Adopted backtick-delimited.  
Source: engine name, witness siglum, corroborative title, or `sequence-based correction`.  
Date: `YYYY-MM-DD`.

**Must:** Every rollback or superseded correction-log entry generates a rejected-readings entry.

---

## 5. translation-reasoning-log.md

| Step | Locus | Chinese | Chosen English | Alternatives Considered | Reasoning |
|------|-------|---------|----------------|------------------------|-----------|

Step matches correction-log. Locus, Chinese, Chosen English backtick-delimited. Alternatives and Reasoning are free text.

**Should:** Cover every non-trivial English change. Script-form-only changes may be omitted.

---

## 6. character-provenance-log.md

| Locus | Position | Character | Source | Confidence | Witness |
|-------|----------|-----------|--------|------------|---------|

Locus and Character backtick-delimited.  
Position: 1-based index.  
Source: `OCR consensus`, `single-engine recovery`, `cross-witness`, `image inspection`, `editorial conjecture`, `human judgment call`.  
Confidence: `strong`, `moderate`, `weak`, `provisional`.  
Witness: siglum or `—`.

**Should:** Cover characters requiring non-trivial source decisions. Full coverage ideal for contested loci.

---

## 7. anchor-base-register.jsonl

Defined fully in `EDITION_EVENTED_ANCHOR_PROTOCOL.md`.

This is the stable geometry layer for:

- witness id
- page id
- locus id
- source asset
- page bbox
- locus bbox
- optional polygon
- optional crop asset
- optional OCR region reference
- optional character boxes

**Must:** Every new edition maintain this file from the moment stable page/locus geometry exists.

---

## 8. anchor-event-log.jsonl

Defined fully in `EDITION_EVENTED_ANCHOR_PROTOCOL.md`.

This is the event delta layer for:

- event id
- locus id
- witness id
- before/after Chinese
- before/after English
- evidence type
- confidence
- source asset
- page/locus geometry
- optional character boxes

**Must:** Every accepted or rejected text-changing event be recorded here in the same bounded session.

---

## Cross-file integrity constraints

1. Every correction-log entry at locus `L` must have a translation-diff-log entry at the same locus and step.
2. Every accepted correction-log entry must have an anchor-event-log row.
3. Every anchor-event-log row must point to at least one anchor-base row through `anchor_id` or equivalent reference.
4. Every rollback must have a rejected-readings entry.
5. Loci with less than `4/4` OCR agreement should explain the adopted reading.
6. Locus IDs must match exactly across all files.
7. Translation-reasoning step numbers must match translation-diff-log steps.

---

## Starting mid-project

For editions already in progress:

1. Create OCR-consensus entries for loci with existing engine outputs on disk.
2. Create rejected-readings entries for every superseded or rollback correction.
3. Create translation-reasoning entries from this point forward. Retroactive entries encouraged.
4. Backfill anchor-event rows first for changed or contested loci.
5. Backfill anchor-base rows at page/locus level before attempting per-character geometry.

Mark retroactive entries clearly as reconstructed.

---

## Reproducibility promise

Given these files and the source assets, a reviewer can:

- reconstruct the text at any step
- reconstruct the translation at any step
- verify OCR readings against engine outputs
- inspect rejected alternatives
- challenge any translation choice
- trace any contested character to its stated source
- jump from an event to the exact page or crop used to justify it

This is the standard from now on.
