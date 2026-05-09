# Edition Agent Master Instructions

**Version:** 1.1  
**Status:** Required reading at session start for every edition agent  
**Scope:** All critical edition work under ReadZen/OpenZen

---

## Part 1: What You Are Doing

You are producing a machine-auditable critical edition of an East Asian text. Your corrections, translations, OCR readings, rejected alternatives, reasoning, and anchor packets are consumed by the ReadZen desktop app to power:

- **Time-travel slider** -- reconstructs the Chinese text at any editorial step, with bilingual English reconstruction alongside it
- **OCR consensus overlay** -- character hover shows all 4 engine readings and agreement level, color-coded by confidence
- **Character provenance popup** -- character click shows the full forensic chain: which engine, which witness, what confidence
- **PDF evidence viewer** -- "View Evidence" button zooms to the exact woodblock region supporting a correction
- **Evented evidence time-travel** -- slider reconstructs not only the text state, but the exact source page/crop/locus used when that state changed
- **Apparatus panel** -- shows rejected readings and the reasons they were discarded
- **Translation reasoning hover** -- English hover shows why this particular rendering was chosen
- **Confidence heatmap** -- visual overlay showing editorial certainty across the text

Every field you record enables a specific UI feature. Missing fields produce blank panels, broken links, or silent gaps in the reconstruction. Your logs are not bureaucracy -- they are the data layer.

From now on, the data layer includes the mandatory evented anchor system defined in `EDITION_EVENTED_ANCHOR_PROTOCOL.md`.

---

## Part 2: The 6 Log Files Plus Mandatory Anchor Capture

All logs live at `provenance/{slug}/process/`. Schemas are defined in:

- `EDITION_FORENSIC_PROVENANCE_PROTOCOL.md`
- `EDITION_TRANSLATION_DIFF_PROTOCOL.md`
- `EDITION_EVENTED_ANCHOR_PROTOCOL.md`

### 1. correction-log.md
**When:** Every time you change a Chinese character in the working text.  
**Schema:** `| Date | Locus | Change type | Before | After | Basis | Status |`  
**Drives:** Time-travel slider (Chinese pane).  
**Mistakes to avoid:** Recording corrections without backtick-delimited text fields. Forgetting to create the paired translation-diff entry. Using `fixed` status for readings you later roll back (use `superseded by visual fix`).

### 2. translation-diff-log.md
**When:** Step 0 covers every text-bearing locus. Steps 1..N match every correction-log entry.  
**Schema:** `| Step | Locus | Chinese Before | Chinese After | English Before | English After | Basis |`  
**Drives:** Time-travel slider (English pane). Drift detection for unmatched steps.  
**Mistakes to avoid:** Skipping step 0 entries. Step number mismatch with correction-log. Omitting entries for script-form-only changes.

### 3. ocr-consensus-log.md
**When:** After running the 4-engine OCR loop on each text-bearing page. Write immediately after OCR, before any correction work.  
**Schema:** `| Locus | Tesseract | RapidOCR | PaddleOCR | EasyOCR | Agreement | Adopted | Basis |`  
**Drives:** Character hover consensus overlay.  
**Mistakes to avoid:** Recording only disagreement loci. You should include full-agreement loci too.

### 4. rejected-readings-log.md
**When:** Every time you discard a reading during comparison, and every rollback or superseded correction-log entry.  
**Schema:** `| Locus | Rejected | Source | Adopted | Reason | Date |`  
**Drives:** Apparatus panel (alternatives considered).  
**Mistakes to avoid:** Logging only the final choice without recording what was rejected. Every `superseded` status in correction-log must generate a rejected-readings entry.

### 5. translation-reasoning-log.md
**When:** Every non-trivial English translation choice. Script-form-only changes may be omitted.  
**Schema:** `| Step | Locus | Chinese | Chosen English | Alternatives Considered | Reasoning |`  
**Drives:** English hover reasoning tooltip.  
**Mistakes to avoid:** Recording only the chosen translation without listing alternatives. Step numbers must match translation-diff-log.

### 6. character-provenance-log.md
**When:** For every character requiring a non-trivial source decision. Full coverage ideal for contested loci.  
**Schema:** `| Locus | Position | Character | Source | Confidence | Witness |`  
**Source values:** `OCR consensus`, `single-engine recovery`, `cross-witness`, `image inspection`, `editorial conjecture`.  
**Confidence values:** `strong`, `moderate`, `weak`, `provisional`.  
**Drives:** Character click provenance popup.  
**Mistakes to avoid:** Omitting the 1-based position index. Using free-text confidence instead of the bounded vocabulary.

### 7. anchor-base-register.jsonl + anchor-event-log.jsonl
**When:** For every accepted or rejected text-changing event, in the same bounded session as the decision.  
**Schema:** See `EDITION_EVENTED_ANCHOR_PROTOCOL.md`.  
**Drives:** Time-travel evidence jumps, source-image zoom, locus drilldown, and future per-character witness navigation.  
**Mistakes to avoid:** Deferring anchor capture. Recording only the source filename without locus geometry. Capturing a page link but not the locus box used in the decision.

---

## Part 3: Workflow-to-Log Mapping

| Workflow Stage | Log Action |
|---|---|
| Witness hunt | Update `witness-register.md`. No provenance log entries yet. |
| Acquisition | Record downloads, failures, rights checks in `process-log.md`. |
| Page preparation | Generate page images. Record in `timeline.json`. Seed anchor-base rows where stable page/locus geometry already exists. |
| OCR baseline | Run 4 engines. Immediately write `ocr-consensus-log.md` entries for every text-bearing page. Do this before any correction. |
| Comparison slices | Write `rejected-readings-log.md` entries for every comparison decision. |
| Correction passes | Write `correction-log.md` and `translation-diff-log.md` entries together. Never one without the other. Also write the matching `anchor-event-log.jsonl` row in the same bounded session. |
| Translation | Write `translation-reasoning-log.md` for non-trivial choices. |
| Character provenance | Write `character-provenance-log.md` for corrected or contested characters. |
| Evidence anchoring | Update `anchor-base-register.jsonl` or reuse an existing anchor, then bind the decision in `anchor-event-log.jsonl`. |

---

## Part 4: Image Evidence Coordinates

When a correction is supported by visual inspection of a PDF or page image, record these extended fields on the correction-log entry:

- **EvidencePdf**: filename of the source PDF
- **EvidencePage**: 0-based page index in the PDF
- **EvidenceRegionX/Y/Width/Height**: normalized coordinates (`0.0` to `1.0`) defining the bounding box of the relevant region

To estimate line-level Y coordinates from page images: divide the text block height by the number of text lines, then use the line's fractional position. For a 10-line page, line 3 starts at roughly `Y=0.2` with `Height=0.1`.

When coordinates are unavailable (remote-only witnesses, unrendered pages), record `EvidencePdf` and `EvidencePage` with region fields set to `—`. The app will link to the full page instead of a zoomed region.

For new editions, these correction-log fields are not enough by themselves. The same decision must also be represented in the evented anchor system so the UI can bind the time-travel state to the exact page/crop/locus packet used to make the decision.

---

## Part 5: Starting Mid-Project

For editions already in progress:

1. Create `ocr-consensus-log.md` entries from existing engine outputs where available.
2. Create `rejected-readings-log.md` entries for every superseded or rollback correction.
3. Create `translation-diff-log.md` step 0 entries for the current working text, then backfill earlier steps where feasible.
4. Create `anchor-event-log.jsonl` entries first for changed or contested loci, not for every untouched line.
5. Expand `character-provenance-log.md` and optional `char_boxes` only where the editorial decision genuinely turned on individual graphs.

If you cannot reconstruct an older anchor packet fully, record the best available page/locus anchor and mark the limits in the event note. Do not invent geometry.

---

## Part 6: Quality Checks Before Handoff

Before declaring any phase complete:

- [ ] All 6 markdown log files exist and are non-empty for the processed portion
- [ ] `anchor-base-register.jsonl` and `anchor-event-log.jsonl` exist for the processed portion
- [ ] Step numbers match between `correction-log.md` and `translation-diff-log.md`
- [ ] Every accepted text-changing event has a matching anchor-event row
- [ ] Every `superseded` or rollback correction-log entry has a `rejected-readings-log.md` counterpart
- [ ] Locus IDs are spelled identically across all files
- [ ] `timeline.json` event count matches actual work done
- [ ] `python scripts/validate_package.py` passes
- [ ] No prose-only entries where structured data is expected
- [ ] All text fields in markdown tables use backtick delimiters

---

## Part 7: What the App Does With Your Data

| Your Data | App Feature | What Breaks If Missing |
|---|---|---|
| correction-log | Time-travel slider reconstructs Chinese text at step N | Slider shows no Chinese changes |
| translation-diff-log | English pane reconstructs alongside Chinese | English pane blank during time-travel |
| ocr-consensus-log | Character hover shows 4-engine readings plus consensus color | Hover shows no OCR data |
| rejected-readings-log | Apparatus panel shows alternatives considered | Apparatus panel empty |
| translation-reasoning-log | English hover shows why this translation was chosen | Hover shows no reasoning |
| character-provenance-log | Character click shows full forensic chain | Click shows no provenance data |
| Image evidence coords | View Evidence button zooms to woodblock line | Button disabled or shows full page |
| anchor-event-log / anchor-base-register | Time-travel evidence jumps and locus-level source navigation | Slider cannot jump to the evidence that produced the text state |

Every empty cell in your logs is a blank panel in the reader's UI. The reproducibility promise depends on your discipline in maintaining these files.

This is the standard. Follow it.
