# Standard Transcription Workflow

This is the default workflow for transcription and editorial work in this repo.

The goal is to produce the strongest historical-critical edition that can be justified from the open witness set. A project does not become "critical" by sounding polished. It becomes critical when every meaningful editorial decision is accountable to documented evidence.

This workflow applies unless a project explicitly states otherwise.

---

## 1. Start with witnesses, not text expectations

At project start, define the witness set explicitly.

- Assign sigla to every witness actually used.
- Record source URL, local path, and rights basis.
- Distinguish between:
  - active witnesses
  - rejected witnesses
  - deferred witnesses
- If a stronger witness exists but cannot be used because it is licensed or rights-unclear, record that fact explicitly.

Do not begin by silently harmonizing to a familiar received text.

---

## 2. Stay inside the open-witness policy

Edition work must be based only on witnesses that are open enough for the project policy.

- Do not use licensed, paywalled, or rights-unclear texts as hidden control witnesses.
- Do not silently import readings from non-open sources.
- If non-open material is known to exist, note that as a limit on the edition, not as covert support.

This means the edition should be described as:
- a historical-critical edition from the open witness set
not:
- a full witness-universal edition unless that is actually true

---

## 3. Keep a running process log during the work

Every project should maintain a process log from the beginning.

Use:
- `PROCESS_LOG_TEMPLATE.md`

The log must be written during the work, not reconstructed at the end.

It must include failures and abandoned attempts, not just successful progress.

At minimum, record:
- witness acquisition
- recon and source-search passes
- transcription sessions
- failed OCR runs
- rejected witness leads
- unresolved pages and abandoned readings
- corroboration sessions
- editorial decisions
- rough readings retained
- build steps
- quality checks
- project limits

If a future reviewer cannot tell what was done, in what order, and why, the edition is under-documented.

Chronological recording is now split across layers:

- `process-log.md` for operational steps
- `decision-log.md` for judgments
- `human-log.md` for readable narrative
- `timeline.json` for app-facing ordered state changes

---

## 4. Separate transcription from edition

Do not collapse the whole workflow into one file.

Maintain distinct layers:
- witness-facing transcription or draft
- corroboration / identification notes
- reading edition
- apparatus or editorial notes

The reading edition should read like a text.
The apparatus should explain why the text looks the way it does.

Do not leave workbench notes, excuses, or process commentary inside the reading text.

Do not assume every scanned page belongs to the main text body.

A short work may be transmitted inside a much longer physical witness with commentary, prefatory matter, or end matter.

Classify page roles before deep correction.

---

## 5. Record every substantive editorial decision

Any meaningful intervention must be documented.

That includes:
- character choice
- graph normalization
- punctuation shaping
- line breaking when not obvious
- section assignment
- case ordering
- contents ordering
- deduplication
- omission of unstable matter
- appendix treatment
- movement of material between body and back matter

For each such decision, the record should make clear:
- what the problem was
- which witnesses were consulted
- what options existed
- which choice was made
- why that choice was made

If the answer is only "it reads better," that is not enough.

If the decision changes visible text, it must also create a `text_changed` timeline event.

That event must record:

- exact `locus_id`
- `change_kind`
- `reason`
- `witness_support`
- preferred:
  - `reading_before`
  - `reading_after`
  - via a per-locus readings table
- fallback only:
  - `previous_reading`
  - `new_reading`

Capture the earlier reading state at the moment of change, before overwrite.

---

## 6. Preserve witness roughness unless there is evidence to improve it

A reading edition may smooth presentation, but it must not silently overwrite witness evidence.

If a line is rough:
- keep it if the witness support is strong
- smooth it only if witness support is weak enough to justify intervention
- record the intervention

Unfamiliar is not the same as wrong.
Polished is not the same as historical.

Maintain a rough-readings table for unusual but retained readings.

---

## 7. Treat structural problems as textual problems

Historical-critical work is not only about characters.
It also includes structure.

Always track:
- contents vs body order
- displaced blocks
- duplicated prose
- appendix status
- preface layering
- end-matter boundaries
- leaf loss and unstable joins

If witness order and reading-edition order diverge, do not silently harmonize them.
Either:
- keep the witness order
- keep the reader-facing order
- or leave the matter partial

But whichever choice is made must be documented.

---

## 8. Keep the reading edition clean

The reading edition should contain:
- the edited text
- only the headings needed for reading structure

It should not contain:
- English workbench labels
- witness excuses
- process reminders
- apparatus-style caveats in the text flow
- duplicate blocks included only for mapping convenience

If explanatory prose is necessary, move it to notes or apparatus.

---

## 9. Maintain an apparatus-capable record even if the output is not yet a full critical edition

Even when producing only a reading edition, preserve enough information to support later apparatus work.

For every important locus, make it possible to recover:
- base reading
- corroborant reading(s)
- omitted reading(s)
- uncertainty
- final editorial choice

This can live in logs, witness notes, or structured markup, but it must exist somewhere.

Without that trail, later XML or TEI work becomes guesswork.

The same applies to timeline replay:

- if the visible reading text changed
- but the before/after state was not recorded at the moment of change
- the slider history is no longer trustworthy

---

## 10. Define what kind of edition the project is

Each project should explicitly state one of the following:

- diplomatic transcription
- witness-based reading edition
- historical-critical edition from the open witness set
- full critical edition

Do not claim a stronger category than the documentation supports.

If the edition is not fully critical, say what prevents that:
- missing witnesses
- policy-barred witnesses
- incomplete collation
- unresolved structure
- unstable back matter

Being explicit about limits increases credibility.

---

## 11. Perform formal quality checks before handoff

Before handoff or publication, run and record quality checks.

At minimum verify:
- witness set frozen
- rights basis recorded
- structure counts correct
- major rough readings reviewed
- known ordering mismatches either resolved or documented
- reading edition free of workbench notes
- build scripts rerun successfully
- handoff file set complete

If a known issue is left in place, record that it is intentional.

---

## 12. Handoff must include evidence, not just output

When handing off to XML, TEI, or publication work, include:
- reading edition
- editorial notes
- witness-facing draft
- corroboration notes
- process log
- human-readable log
- timeline data
- rights / provenance files
- scan witness paths

The next stage should never have to infer the editorial history from the final text alone.

---

## 13. Standard of legitimacy

For this repository, a transcription project counts as a legitimate historical-critical edition workflow when:

- the witness set is explicit
- the rights basis is explicit
- the open-witness policy is respected
- the editorial method is stated
- substantive decisions are documented
- rough readings are tracked
- text and apparatus are separated
- structural problems are treated explicitly
- quality checks are recorded

Perfection is not required.
Accountability is required.

---

## 14. Default rule

If in doubt:
- prefer the witness over polish
- prefer documentation over silent correction
- prefer a clean partial result over a misleading complete one

That is the standard from now on.
