# Edition Agent Master Instructions

**Version:** 1.0
**Status:** Required reading at session start for every edition agent
**Scope:** All critical edition work under ReadZen/OpenZen

---

## Part 1: What You Are Doing

You are producing a machine-auditable critical edition of an East Asian text. Your corrections, translations, OCR readings, rejected alternatives, and reasoning are consumed by the ReadZen desktop app to power:

- **Time-travel slider** -- reconstructs the Chinese text at any editorial step, with bilingual English reconstruction alongside it
- **OCR consensus overlay** -- character hover shows all 4 engine readings and agreement level, color-coded by confidence
- **Character provenance popup** -- character click shows the full forensic chain: which engine, which witness, what confidence
- **PDF evidence viewer** -- "View Evidence" button zooms to the exact woodblock region supporting a correction
- **Apparatus panel** -- shows rejected readings and the reasons they were discarded
- **Translation reasoning hover** -- English hover shows why this particular rendering was chosen
- **Confidence heatmap** -- visual overlay showing editorial certainty across the text

Every field you record enables a specific UI feature. Missing fields produce blank panels, broken links, or silent gaps in the reconstruction. Your logs are not bureaucracy -- they are the data layer.

---

## Part 2: The 6 Log Files

All logs live at `provenance/{slug}/process/`. Schemas are defined in `EDITION_FORENSIC_PROVENANCE_PROTOCOL.md` and `EDITION_TRANSLATION_DIFF_PROTOCOL.md`.

### 1. correction-log.md
**When:** Every time you change a Chinese character in the working text.
**Schema:** `| Date | Locus | Change type | Before | After | Basis | Status |`
**Drives:** Time-travel slider (Chinese pane).
**Mistakes to avoid:** Recording corrections without backtick-delimited text fields. Forgetting to create the paired translation-diff entry. Using `fixed` status for readings you later roll back (use `superseded by visual fix`).

### 2. translation-diff-log.md
**When:** Step 0 covers every text-bearing locus. Steps 1..N match every correction-log entry.
**Schema:** `| Step | Locus | Chinese Before | Chinese After | English Before | English After | Basis |`
**Drives:** Time-travel slider (English pane). Drift detection (orange gutter dots for unmatched steps).
**Mistakes to avoid:** Skipping step 0 entries -- causes blank English during time-travel. Step number mismatch with correction-log. Omitting entries for script-form-only changes (record them with identical English and note "meaning unchanged").

### 3. ocr-consensus-log.md
**When:** After running the 4-engine OCR loop on each text-bearing page. Write IMMEDIATELY after OCR, before any correction work.
**Schema:** `| Locus | Tesseract | RapidOCR | PaddleOCR | EasyOCR | Agreement | Adopted | Basis |`
**Drives:** Character hover consensus overlay.
**Mistakes to avoid:** Recording only disagreement loci. You SHOULD include full-agreement loci too. Using `--` instead of `---` for unavailable engines.

### 4. rejected-readings-log.md
**When:** Every time you discard a reading during comparison, and every rollback or superseded correction-log entry.
**Schema:** `| Locus | Rejected | Source | Adopted | Reason | Date |`
**Drives:** Apparatus panel (alternatives considered).
**Mistakes to avoid:** Logging only the final choice without recording what was rejected. Every `superseded` status in correction-log MUST generate a rejected-readings entry.

### 5. translation-reasoning-log.md
**When:** Every non-trivial English translation choice. Script-form-only changes MAY be omitted.
**Schema:** `| Step | Locus | Chinese | Chosen English | Alternatives Considered | Reasoning |`
**Drives:** English hover reasoning tooltip.
**Mistakes to avoid:** Recording only the chosen translation without listing alternatives. Step numbers MUST match translation-diff-log.

### 6. character-provenance-log.md
**When:** For every character requiring a non-trivial source decision. Full coverage ideal for contested loci.
**Schema:** `| Locus | Position | Character | Source | Confidence | Witness |`
**Source values:** `OCR consensus`, `single-engine recovery`, `cross-witness`, `image inspection`, `editorial conjecture`.
**Confidence values:** `strong`, `moderate`, `weak`, `provisional`.
**Drives:** Character click provenance popup.
**Mistakes to avoid:** Omitting the 1-based position index. Using free-text confidence instead of the bounded vocabulary.

---

## Part 3: Workflow-to-Log Mapping

| Workflow Stage | Log Action |
|---|---|
| Witness hunt | Update `witness-register.md`. No provenance log entries yet. |
| Acquisition | Record downloads, failures, rights checks in `process-log.md`. |
| Page preparation | Generate page images. Record in `timeline.json`. |
| OCR baseline | Run 4 engines. IMMEDIATELY write `ocr-consensus-log.md` entries for every text-bearing page. Do this before any correction. |
| Comparison slices | Write `rejected-readings-log.md` entries for every comparison decision. |
| Correction passes | Write `correction-log.md` AND `translation-diff-log.md` entries together. NEVER one without the other. |
| Translation | Write `translation-reasoning-log.md` for non-trivial choices. |
| Character provenance | Write `character-provenance-log.md` for corrected or contested characters. |

---

## Part 4: Image Evidence Coordinates

When a correction is supported by visual inspection of a PDF or page image, record these extended fields on the correction-log entry:

- **EvidencePdf**: filename of the source PDF (e.g., `T1.pdf`)
- **EvidencePage**: 0-based page index in the PDF
- **EvidenceRegionX/Y/Width/Height**: normalized coordinates (0.0-1.0) defining the bounding box of the relevant region

To estimate line-level Y coordinates from page images: divide the text block height by the number of text lines, then use the line's fractional position. For a 10-line page, line 3 starts at roughly Y=0.2 with Height=0.1.

When coordinates are unavailable (remote-only witnesses, unrendered pages), record `EvidencePdf` and `EvidencePage` with region fields set to `—`. The app will link to the full page instead of a zoomed region.

---

## Part 5: Starting Mid-Project (Faith in Mind)

The Faith in Mind edition already has a correction-log with entries through C5. To adopt the full protocol:

1. **ocr-consensus-log.md**: Generate from existing 4-engine outputs. Process T1 first (the copy-text), then T4, T5, T2, T3, A1-A3, C1-C5 in order. One row per text-bearing locus per witness.

2. **translation-diff-log.md**: Translate the current T1 working text as step 0 entries. Mark basis as `initial translation (added mid-project at correction step {current})`. For existing correction steps 1..N, use the retroactive approach where feasible: reconstruct before/after Chinese from the correction-log, translate both states.

3. **rejected-readings-log.md**: Extract from correction-log entries with status `superseded by visual fix` or `visual de-certainty rollback`. Example: step at T1-p075.l01 rolled back `若不如此必不須守` to the original OCR reading -- this MUST become a rejected-readings entry.

4. **From C6 onward**: Follow the full protocol for every action. No exceptions.

5. **Gaps**: If you cannot reconstruct a log entry retroactively, skip it and record the gap: `| {locus} | — | — | — | — | — | gap: pre-protocol, no data available |`

---

## Part 6: Quality Checks Before Handoff

Before declaring any phase complete:

- [ ] All 6 log files exist and are non-empty for the processed portion
- [ ] Step numbers match between `correction-log.md` and `translation-diff-log.md`
- [ ] Every `superseded`/rollback correction-log entry has a `rejected-readings-log.md` counterpart
- [ ] Locus IDs are spelled identically across all 6 files (case-insensitive, spelling-exact)
- [ ] `timeline.json` event count matches actual work done
- [ ] `python scripts/validate_package.py` passes
- [ ] No prose-only entries where structured table data is expected
- [ ] All text fields in markdown tables use backtick delimiters

---

## Part 7: What the App Does With Your Data

| Your Log | App Feature | What Breaks If Missing |
|---|---|---|
| correction-log | Time-travel slider reconstructs Chinese text at step N | Slider shows no Chinese changes |
| translation-diff-log | English pane reconstructs alongside Chinese | English pane blank during time-travel |
| ocr-consensus-log | Character hover shows 4-engine readings + consensus color | Hover shows "no OCR data" |
| rejected-readings-log | Apparatus panel shows alternatives considered | Apparatus panel empty |
| translation-reasoning-log | English hover shows why this translation was chosen | Hover shows no reasoning |
| character-provenance-log | Character click shows full forensic chain | Click shows "no provenance data" |
| Image evidence coords | "View Evidence" button zooms to woodblock line | Button disabled or shows full page |

Every empty cell in your logs is a blank panel in the reader's UI. The reproducibility promise -- that a reviewer can reconstruct every character choice, verify every OCR reading, audit every rejected alternative, and challenge every translation -- depends entirely on your discipline in maintaining these 6 files.

This is the standard. Follow it.
