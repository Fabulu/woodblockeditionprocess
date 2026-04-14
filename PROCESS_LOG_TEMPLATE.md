# Process Log: [Text Name] ([Publisher Prefix].[Slug])

**Curator:** [name]  
**Started:** [date]  
**Status:** [in-progress | review | published]  
**Primary open witnesses:** [list with URLs]  
**Closed / licensed witnesses used in edition:** [none | not permitted under current policy]

---

## Purpose

This is the running journal for a transcription, reconstruction, and editorial project intended to support the strongest historical-critical edition that can be made under the current open-source policy.

Use this log during the work, not after the fact.

A future reviewer should be able to answer:
- What was acquired, from where, and on what rights basis
- What was transcribed directly from the witness
- What was corroborated and by which open witnesses
- Where editorial judgment was used
- Which rough readings were retained and why
- Which limits came from policy rather than evidence

Every meaningful step belongs here or in a linked per-stage log.

That includes failed attempts, rejected leads, and abandoned approaches, not just successes.

This log is not enough by itself for visible text changes.

If visible edition text changes, also create:

- a `text_changed` event in `timeline.json`
- a decision record in `decision-log.md` if the change is non-trivial
- a readable explanation in `human-log.md` if the change matters to the reader

---

## Policy constraints

- Only open / reusable witnesses may be used for corroboration in the edition workflow.
- Do not use licensed, paywalled, or rights-unclear texts as hidden control witnesses.
- If a stronger but non-open witness is known to exist, record that fact here, but do not rely on it for readings.
- The goal is the best historical-critical edition possible from the open witness set.

---

## Witness set

| Siglum | Witness | Type | Source URL | Rights basis | Status |
|------|--------|------|------------|--------------|--------|
| A | [base witness] | [scan / text / OCR-derived draft] | [url] | [PD / Commons / CC / etc.] | [active] |
| B | [open corroborant witness] | [scan / text] | [url] | [rights basis] | [active] |
| C | [open corroborant witness] | [scan / text] | [url] | [rights basis] | [active] |

Notes:
- Record only witnesses actually used in the edition here.
- If a witness is reviewed and rejected, record it under `Rejected or deferred witnesses`.

---

## Rejected or deferred witnesses

| Date | Witness | Reason not used |
|------|---------|-----------------|
| YYYY-MM-DD | [witness] | [licensed / rights unclear / too weak / duplicate / incomplete] |

---

## Witness acquisition

| Date | Action | Notes |
|------|--------|-------|
| YYYY-MM-DD | Identified [witness] at [source URL] | [rights basis, confidence] |
| YYYY-MM-DD | Downloaded PDF/scan to local | [filename, bytes, sha256 if available] |
| YYYY-MM-DD | Verified rights basis | [PD-old because..., Commons because..., local notes updated] |
| YYYY-MM-DD | Rejected [witness] | [duplicate / rights unclear / incomplete / bad download / other] |
| YYYY-MM-DD | Download failed for [witness] | [timeout / HTML / checksum mismatch / truncated / other] |

---

## Recon and search steps

| Date | Query or source | Action | Outcome | Next step | Actor |
|------|------------------|--------|---------|-----------|-------|
| YYYY-MM-DD | [search query / site / catalog] | [searched / checked / compared] | [new lead / duplicate / no result / unresolved] | [follow-up] | [agent / human / hybrid] |

---

## Transcription sessions

### Session [N]: [date] [time range]

**Scope:** [which leaves/pages/cases]  
**Method:** [OCR model(s), human reading, image adjudication, etc.]

**Results:**
- [N] leaves processed
- [M] high-confidence
- [K] need review
- Notable difficulties: [damage, missing graphs, page disorder, OCR failure]

**Decisions made:**
- [leaf / case / line] [decision]
- [leaf / case / line] [decision]

**Timeline obligations for text changes:**
- `locus_id`
- `change_kind`
- `reason`
- `witness_support`
- `note_anchor_id` if any
- preferred:
  - `reading_before`
  - `reading_after`
  - backed by a per-locus readings table
- fallback only:
  - `previous_reading`
  - `new_reading`

**Rejected or failed paths:**
- [location] [OCR failure / unusable crop / false positive / abandoned approach]

**Open questions:**
- [location] [issue]
- [location] [needs corroboration?]

---

## Witness corroboration sessions

### Corroboration [N]: [date] - [witness siglum]

**Scope:** [cases / leaves / prefatory matter / end matter]  
**Method:** [side-by-side comparison, OCR cross-check, image review]

**Confirmations:**
- [location]: [confirmed what]
- [location]: [confirmed what]

**Corrections applied:**
- [location]: [what changed]
- [location]: [why]

**Unresolved:**
- [location]: [disagreement or ambiguity]

**Rejected leads or witnesses in this pass:**
- [witness / source] [why rejected]

**Policy note:**
- [confirm that only open witnesses were used]

---

## Editorial decisions

### Decision [N]: [date] - [one-line summary]

**Context:** [what was the issue]

**Options considered:**
1. [option A] - [pros / cons]
2. [option B] - [pros / cons]

**Chose:** [which option and why]  
**Evidence:** [witness locus, leaf, corroboration note, image comparison]  
**Policy impact:** [allowed under open policy? yes / no]  
**Reversibility:** [easy / medium / hard]

**Timeline event required:** [yes / no]

If yes:
- event id: [evt_...]
- locus id(s): [...]

---

## Rough readings retained

| Location | Reading | Witness support | Why kept |
|----------|---------|-----------------|----------|
| [case / line] | [reading] | [A only / A+B / A+B+C] | [why not normalized] |

---

## Structure and ordering decisions

| Date | Location | Issue | Decision | Basis |
|------|----------|-------|----------|-------|
| YYYY-MM-DD | [contents / case order / appendix] | [mismatch] | [kept witness / followed body / left partial] | [witness evidence] |

---

## Assembly / reading edition build

### Build step [N]: [date]

**Source:** [draft files / chunk files / witness notes]  
**Output:** [reading edition / audit / notes / xml draft]

**Changes introduced:**
- [lineation / punctuation / section ordering / deduplication]
- [witness-backed correction]
- [formatting-only change]

If any visible reading changed here, confirm:
- corresponding `text_changed` events created
- `timeline.json` updated
- `human-log.md` updated if reader-facing significance exists

**Status:** [draft | corroborated | review-ready | final]

---

## Quality checks

| Date | Check | Result |
|------|-------|--------|
| YYYY-MM-DD | Witness count frozen | [ok / not ok] |
| YYYY-MM-DD | Core structure audit | [N complete, M partial] |
| YYYY-MM-DD | Body order checked against edition | [ok / mismatch logged] |
| YYYY-MM-DD | Contents checked against witness leaves | [ok / partial / separated] |
| YYYY-MM-DD | Rough readings table updated | [yes / no] |
| YYYY-MM-DD | Open-policy compliance check | [no licensed witness used] |
| YYYY-MM-DD | Build script rerun | [ok / failed / output path] |

---

## Historical-critical limits

- [What keeps this from being a full critical edition?]
- [Which missing witnesses are policy-barred rather than physically unavailable?]
- [Which unresolved readings remain because the open witness set is insufficient?]

---

## Publication / handoff

| Date | Action | Notes |
|------|--------|-------|
| YYYY-MM-DD | Reading edition finalized | [path] |
| YYYY-MM-DD | Notes finalized | [path] |
| YYYY-MM-DD | XML handoff prepared | [recipient / file set] |
| YYYY-MM-DD | Manifest / metadata updated | [path] |

---

## Lessons learned

- [What worked]
- [What failed]
- [What should be standardized next time]
- [What should be automated next time]
