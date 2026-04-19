# Edition Translation Diff Protocol

**Version:** 1.0
**Status:** Required for all critical edition projects going forward
**Applies to:** Any AI or human agent performing critical edition work under ReadZen/OpenZen

---

## Purpose

This protocol ensures that every correction to a critical edition's Chinese text is accompanied by a corresponding English translation update, and that both changes are recorded in a machine-parseable diff log. The ReadZen desktop app uses this log to reconstruct the full bilingual text at ANY point in the editorial process — enabling users to scrub through the entire edition timeline and see both Chinese and English evolve together.

**No other tool in any philological discipline does this.** It only works if you follow this protocol precisely.

---

## What you must produce

### 1. Initial full translation (Step 0)

When you begin work on a critical edition, after the initial OCR text is established (even if it's garbage), translate **every single line** of the working text into English. Mark these as step 0 entries.

Yes, this means translating OCR garbage. The translations will be rough ("至道無雅催焦择" might become "The supreme way without elegance..."). That's fine. The point is to have a baseline English for every locus so the time-travel view is never empty.

### 2. Correction + retranslation (Steps 1..N)

Every time you correct a Chinese reading (in the correction log), you MUST also:
1. Retranslate the affected English line
2. Record both the Chinese and English changes as a translation diff entry

If a correction doesn't change the meaning (e.g., script-form normalization 现→現), the English may stay the same. Still record the entry with identical before/after English.

### 3. New lines (insertions)

If a correction adds a new locus (e.g., `T1-p021.l01a`), the translation diff entry has empty `English Before` and the new translation as `English After`.

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

Each row is ONE translation change at ONE locus:

```
| {step} | `{locus}` | `{chinese_before}` | `{chinese_after}` | `{english_before}` | `{english_after}` | {basis} |
```

- **Step**: Integer matching the correction log step number. Step 0 = initial translation of the raw OCR text.
- **Locus**: Must exactly match the locus ID used in the correction log and working text (e.g., `T1-p007.l01`). Case-insensitive.
- **Chinese Before/After**: The Chinese text before and after the correction. For step 0 entries, Chinese Before is `—` (em-dash).
- **English Before/After**: The English translation before and after. For step 0, English Before is `—`.
- **Basis**: Why the retranslation was needed (e.g., "correction 3 retranslation", "initial OCR translation", "meaning unchanged — script form only").

### Example

```markdown
| 0 | `T1-p001.l01` | `—` | `三祖大部信心名` | `—` | `Third Patriarch's Great Section Faith in Name` | initial OCR translation |
| 0 | `T1-p007.l01` | `—` | `至道無雅催焦择` | `—` | `The supreme way without elegance urges burning choice` | initial OCR translation |
| 1 | `T1-p001.l01` | `三祖大部信心名` | `三祖大師信心銘` | `Third Patriarch's Great Section Faith in Name` | `Third Patriarch Master Sengcan's Inscription on Faith in Mind` | correction 1 retranslation |
| 3 | `T1-p007.l01` | `至道無雅催焦择` | `至道無難唯嫌揀擇` | `The supreme way without elegance urges burning choice` | `The Supreme Way is not difficult — if only you refrain from picking and choosing` | correction 3 retranslation |
```

---

## Rules

### MUST follow

1. **Every correction-log entry MUST have a corresponding translation-diff-log entry.** The app cross-references by step number and locus. Missing entries cause blank English during time-travel.

2. **Step numbers MUST match between correction-log.md and translation-diff-log.md.** If correction-log.md has a fix at step 47 for locus T1-p030.l01, the translation diff log must have a step 47 entry for T1-p030.l01.

3. **Locus IDs MUST match exactly.** `T1-p007.l01` in the correction log must be `T1-p007.l01` in the translation diff log (case-insensitive but spelling-exact).

4. **Step 0 entries MUST cover every text-bearing locus.** The app needs a baseline English for every line. If you skip loci at step 0, those lines will show blank English during time-travel.

5. **Use backtick delimiters** around all text fields in the markdown table (`` `text` ``). The parser uses these to extract content.

### SHOULD follow

6. **Translate OCR garbage literally** at step 0 rather than guessing what the text should say. "至道無雅催焦择" → "The supreme way without elegance urges burning choice" is better than pre-empting the correction. The point is to show the reader what the OCR produced and how bad it was.

7. **Note when meaning doesn't change.** If a correction only changes script form (现→現), record the entry with identical English and basis "meaning unchanged — script form only". This lets the app know the translation was reviewed, not just forgotten.

8. **Group step 0 entries at the top of the file**, then subsequent steps in chronological order. The parser doesn't require ordering but humans reading the file benefit from it.

---

## How the app uses this

The ReadZen desktop app's Reader tab has a **correction time-travel bar** — a slider that reconstructs the text at any point in the editorial process. When a `translation-diff-log.md` exists:

1. **Both panes update**: Chinese (left) shows the reconstructed text at step N, English (right) shows the reconstructed translation at step N.
2. **Playback works bilingually**: hit Play and watch both Chinese and English evolve from raw OCR to polished final text.
3. **Drift detection**: orange gutter dots in the English pane mark lines where the Chinese changed but the English hasn't caught up yet (only possible if you miss a retranslation entry — follow rule #1 to prevent this).

Without this file, the app shows Chinese-only during time-travel (English pane is blank).

---

## Starting mid-project (e.g., Faith in Mind)

If you're adding this protocol to an edition that already has a correction log with entries:

1. **Create step 0 entries** by translating the CURRENT working text (not the raw OCR — you don't have the original OCR state anymore). Mark these as step 0 with basis "initial translation (added mid-project at correction step {current})".

2. **For existing correction entries** (steps 1..N already in the correction log), you have two options:
   - **Retroactive**: go back through the correction log, reconstruct the before/after Chinese at each step, and translate both. This is thorough but time-consuming.
   - **Forward-only**: create step 0 entries for the current text, then only record new translation diffs from this point forward. Past steps will show the current English at step 0 and blank for steps 1..N until you reach the current step. This is faster but produces a gap in the time-travel view.

3. **Document which approach you chose** in the `Basis` column of the step 0 entries.

---

## File locations (summary)

```
provenance/{slug}/process/correction-log.md          ← Chinese corrections (already exists)
provenance/{slug}/process/translation-diff-log.md     ← English retranslations (NEW, this protocol)
provenance/{slug}/transcription/corrected/*working*   ← Current working text (already exists)
```

The app discovers all three from the edition's XML path via the convention:
`xml-open/{kind}/{slug}/ → ../../../provenance/{slug}/process/`

---

## Versioning

This is version 1.0 of the protocol. If the table format changes, bump the version number in the header and update the parser in `Services/TranslationDiffLogService.cs`.
