# Edition Translation Diff Protocol

**Version:** 1.1  
**Status:** Required for all critical edition projects going forward  
**Applies to:** Any AI or human agent performing critical edition work under ReadZen/OpenZen

---

## Purpose

This protocol ensures that every correction to a critical edition's Chinese text is accompanied by a corresponding English translation update, and that both changes are recorded in a machine-parseable diff log.

The ReadZen desktop app uses this log to reconstruct the full bilingual text at any point in the editorial process, enabling users to scrub through the entire edition timeline and see both Chinese and English evolve together.

This protocol now also assumes the matching evented anchor packet required by `EDITION_EVENTED_ANCHOR_PROTOCOL.md`.

---

## What you must produce

### 1. Initial full translation (Step 0)

When you begin work on a critical edition, after the initial OCR text is established, translate every single text-bearing line of the working text into English. Mark these as step 0 entries.

Yes, this may mean translating OCR garbage. That is acceptable. The point is to have a baseline English for every locus so the time-travel view is never empty.

### 2. Correction + retranslation (Steps 1..N)

Every time you correct a Chinese reading in the correction log, you must also:

1. Retranslate the affected English line
2. Record both the Chinese and English changes as a translation diff entry
3. Ensure the same event is represented in the anchor-event log

If a correction does not change the meaning, the English may stay the same. Still record the entry with identical before/after English and note that the meaning is unchanged.

### 3. New lines (insertions)

If a correction adds a new locus, the translation diff entry has empty `English Before` and the new translation as `English After`.

---

## File format

### translation-diff-log.md

Place this file at:

```
provenance/{edition-slug}/process/translation-diff-log.md
```

Next to the existing `correction-log.md`.

### Header

```markdown
# Translation Diff Log: {Edition Name}

Date: {date}
Status: {in progress / complete}

## Entries

| Step | Locus | Chinese Before | Chinese After | English Before | English After | Basis |
|------|-------|---------------|---------------|----------------|---------------|-------|
```

### Entry format

Each row is one translation change at one locus:

```markdown
| {step} | `{locus}` | `{chinese_before}` | `{chinese_after}` | `{english_before}` | `{english_after}` | {basis} |
```

- **Step**: Integer matching the correction log step number. Step 0 is the initial translation baseline.
- **Locus**: Must exactly match the locus ID used in the correction log and working text.
- **Chinese Before/After**: The Chinese text before and after the correction. For step 0 entries, Chinese Before is `—`.
- **English Before/After**: The English translation before and after. For step 0 entries, English Before is `—`.
- **Basis**: Why the retranslation was needed.

---

## Rules

### Must follow

1. Every correction-log entry must have a corresponding translation-diff-log entry.
2. Step numbers must match between `correction-log.md` and `translation-diff-log.md`.
3. Locus IDs must match exactly.
4. Step 0 entries must cover every text-bearing locus.
5. Use backtick delimiters around all text fields in the markdown table.
6. Every text-changing step must also have a corresponding anchor-event entry carrying the same before/after Chinese and English state.

### Should follow

7. Translate OCR garbage literally at step 0 rather than silently normalizing it.
8. Note when meaning does not change.
9. Group step 0 entries at the top of the file.

---

## How the app uses this

The ReadZen reader can:

1. Reconstruct Chinese and English together at step `N`
2. Play back the editorial process bilingually
3. Detect drift when Chinese changes but English was not updated
4. Bind the bilingual state to the evented anchor packet for evidence jumps

Without this file, the app shows Chinese-only during time-travel.

---

## Starting mid-project

If you are adding this protocol to an edition that already has a correction log:

1. Create step 0 entries by translating the current working text.
2. For existing correction entries, choose:
   - **Retroactive**: reconstruct earlier before/after states and translate both
   - **Forward-only**: create step 0 for the current text and begin strict coverage from now on
3. Document which approach you chose in the `Basis` column.
4. For any retroactively reconstructed line that will support time-travel evidence jumps, backfill the matching anchor-event packet as well.

---

## File locations (summary)

```
provenance/{slug}/process/correction-log.md
provenance/{slug}/process/translation-diff-log.md
provenance/{slug}/process/anchor-event-log.jsonl
provenance/{slug}/transcription/corrected/*working*
```

The app discovers these from the edition XML path via:

`xml-open/{kind}/{slug}/ -> ../../../provenance/{slug}/process/`

---

## Versioning

This is version 1.1 of the protocol. If the table format changes, bump the version number and update the parser accordingly.
