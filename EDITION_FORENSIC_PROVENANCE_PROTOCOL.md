# Edition Forensic Provenance Protocol

**Version:** 1.0
**Status:** Required for all critical edition projects
**Applies to:** Any AI or human agent performing critical edition work under ReadZen/OpenZen

---

## Purpose

Six log files make every editorial decision fully reproducible. Given these logs and the source PDFs, a reviewer can reconstruct every character choice, verify OCR consensus, audit rejected readings, and challenge any translation decision.

## File locations

```
provenance/{slug}/process/
  correction-log.md              ← Chinese text corrections (existing)
  translation-diff-log.md        ← Bilingual retranslation diffs (existing)
  ocr-consensus-log.md           ← Per-locus OCR engine agreement (NEW)
  rejected-readings-log.md       ← Readings considered and discarded (NEW)
  translation-reasoning-log.md   ← Why each English rendering was chosen (NEW)
  character-provenance-log.md    ← Per-character source and confidence (NEW)
```

App discovery: `xml-open/{kind}/{slug}/ → ../../../provenance/{slug}/process/`

---

## 1. correction-log.md

| Date | Locus | Change type | Before | After | Basis | Status |
|------|-------|-------------|--------|-------|-------|--------|

All text fields backtick-delimited. Change type: `OCR certainty fix`, `visual certainty fix`, `comparison-supported certainty fix`, `visual de-certainty rollback`. Status: `fixed`, `superseded by visual fix`, `provisional`.

**Image evidence** (optional extended fields): `EvidencePdf` (filename), `EvidencePage` (0-based), `EvidenceRegionX`/`Y`/`Width`/`Height` (0.0-1.0 normalized). When present, the app shows "View Evidence" linking to the exact PDF region.

```
| 2026-04-14 | `T1-p007.l01` | OCR certainty fix | `至道無雅催焦择` | `至道無難唯嫌揀擇` | standard opening lemma recovered from clear OCR corruption | fixed |
```

**MUST:** Every correction generates a corresponding translation-diff-log entry.

---

## 2. translation-diff-log.md

Fully specified in `EDITION_TRANSLATION_DIFF_PROTOCOL.md`.

| Step | Locus | Chinese Before | Chinese After | English Before | English After | Basis |
|------|-------|---------------|---------------|----------------|---------------|-------|

**MUST:** Step 0 covers every text-bearing locus. Step numbers match correction-log entries.

---

## 3. ocr-consensus-log.md

| Locus | Tesseract | RapidOCR | PaddleOCR | EasyOCR | Agreement | Adopted | Basis |
|-------|-----------|----------|-----------|---------|-----------|---------|-------|

Engine columns backtick-delimited. Use `—` if engine unavailable. Agreement: `4/4`, `3/4`, etc. Adopted: backtick-delimited final reading.

```
| `T1-p007.l01` | `至道無雅催焦择` | `至道無難唯嫌揀擇` | `至道無難唯嫌揀择` | `至道無雅催焦择` | 2/4 agree on core | `至道無難唯嫌揀擇` | RapidOCR + PaddleOCR consensus |
```

**MUST:** One row per locus where OCR was consulted. **SHOULD:** Include full-agreement loci too.

---

## 4. rejected-readings-log.md

| Locus | Rejected | Source | Adopted | Reason | Date |
|-------|----------|--------|---------|--------|------|

Locus, Rejected, Adopted backtick-delimited. Source: engine name, witness siglum, or `sequence-based correction`. Date: `YYYY-MM-DD`.

```
| `T1-p075.l01` | `若不如此必不須守` | sequence-based correction | `祖大師超州廣携取封在日隐野花帝鸟` | image shows commentary material; earlier correction rolled back | 2026-04-15 |
```

**MUST:** Every rollback or superseded correction-log entry generates a rejected-readings entry.

---

## 5. translation-reasoning-log.md

| Step | Locus | Chinese | Chosen English | Alternatives Considered | Reasoning |
|------|-------|---------|----------------|------------------------|-----------|

Step matches correction-log. Locus, Chinese, Chosen English backtick-delimited. Alternatives and Reasoning are free text.

```
| 3 | `T1-p007.l01` | `至道無難唯嫌揀擇` | `The Supreme Way is not difficult — if only you refrain from picking and choosing` | "The Great Way has no difficulty"; "The highest path is easy" | "Supreme Way" for register consistency |
```

**SHOULD:** Cover every non-trivial English change. Script-form-only changes may be omitted.

---

## 6. character-provenance-log.md

| Locus | Position | Character | Source | Confidence | Witness |
|-------|----------|-----------|--------|------------|---------|

Locus and Character backtick-delimited. Position: 1-based index. Source: `OCR consensus`, `single-engine recovery`, `cross-witness`, `image inspection`, `editorial conjecture`. Confidence: `strong`, `moderate`, `weak`, `provisional`. Witness: siglum or `—`.

```
| `T1-p060.l01` | 3 | `窮` | single-engine recovery | moderate | T1 |
| `T1-p021.l01a` | 1 | `一` | cross-witness | strong | T4 |
```

**SHOULD:** Cover characters requiring non-trivial source decisions. Full coverage ideal for contested loci.

---

## Cross-file integrity constraints

1. Every correction-log entry at step N / locus L **MUST** have a translation-diff-log entry at the same step/locus.
2. Every rollback **MUST** have a rejected-readings-log entry.
3. Loci with < 4/4 OCR agreement **SHOULD** explain the adopted reading.
4. Locus IDs **MUST** match exactly across all 6 files (case-insensitive, spelling-exact).
5. Translation-reasoning step numbers **MUST** match translation-diff-log steps.

---

## Starting mid-project

For editions already in progress (e.g., Faith in Mind):

1. Create ocr-consensus entries for loci with existing engine outputs on disk.
2. Create rejected-readings entries for every `superseded` or rollback correction-log entry.
3. Create translation-reasoning entries from this point forward. Retroactive entries encouraged but not required.
4. Character-provenance: begin with contested loci, expand as time permits.

Mark retroactive entries: "reconstructed at step N".

---

## The reproducibility promise

Given these 6 logs and the source PDFs, a reviewer can: reconstruct the text at any step; verify OCR readings against engine outputs; audit every rejected alternative; challenge any translation; trace any character to its source; view the exact PDF region supporting a correction.

This is the standard from now on.
