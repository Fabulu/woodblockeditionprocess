# Guided Critical Edition Workflow

Date: 2026-04-14
Purpose: a single file to use when the user says "Make a critical edition of XXX" and wants guided help through the whole process.

## Use

Use this file when the user gives you:

- one starting folder in the repo
- one work title
- or one simple request like `Make a critical edition of Faith in Mind`

## Resume Before Restart

Before asking the generic opening question, first check whether this work already has an edition package or process tree.

Look for:

- `*/provenance/{slug}/process/current-state.md`
- `*/xml-open/*/{slug}/process.json`
- `*/xml-open/*/{slug}/timeline.json`
- existing `process-log.md`
- existing `decision-log.md`
- existing `human-log.md`
- existing `witness-register.md`
- existing `ocr-transcription-plan.md`

If those exist, do not restart at witness discovery by default.

Read them first and answer these questions:

1. Is the witness set already locked?
2. Is the copy-text already chosen or locked?
3. What phase is complete?
4. What phase is next?
5. What exact artifact should be produced next?
6. What blockers are already known?

If the answers are already in the package, surface that state to the user and resume from the recorded next step.

Only ask `How many witnesses should I try to find before I lock the witness set?` if no credible edition state already exists, or if the user explicitly wants to reopen that earlier decision.

## Shared Path Rule

In shared markdown, do not use:

- local absolute paths like `C:\...`
- renderer-only absolute links

Use repo-relative paths or repo-name-relative paths instead.

## First Question For A Fresh Start

Ask this first:

`How many witnesses should I try to find before I lock the witness set?`

If the user does not specify, recommend:

- `5` for a pilot
- `10` for a strong small edition
- `all credible free witnesses` for a full research pass

## Then Guide the User Through These Decisions

Ask one decision at a time, not all at once.

1. Confirm the target text and starting witness.
2. Confirm whether the scope is base-text only, base plus anthology witnesses, or broader.
3. Confirm whether commentary and translation/reception witnesses should be included.
4. Build and show the candidate witness set.
5. Ask whether to lock the witness set or keep searching.
6. Recommend and confirm a copy-text.
   Lock it as the starting spine, but only as a reversible critical-edition decision rather than an untouchable permanent base.
7. Confirm annotation depth.
8. Confirm intervention policy.
9. Confirm what counts as done.

## Default Rules

- free first
- scans before plain text
- OCR first
- for East Asian scan witnesses, the four-engine OCR loop is mandatory: `tesseract`, `RapidOCR`, `PaddleOCR`, `EasyOCR`
- keep critical text, witness comparison, and timeline as separate surfaces
- exact source pages before secondary references
- every intervention logged
- agent decisions logged too, not just human decisions
- every meaningful step logged while it happens, not reconstructed later
- failed searches, rejected leads, failed downloads, OCR failures, and abandoned options logged too
- the current edition state must be replayable chronologically, not just described after the fact
- the canonical text-history model is reverse-patching from the final text, not full historical snapshots as primary truth

## Canonical Recording Model

Use these files for these jobs.

### `process-log.md`

Use for:

- chronological work steps
- recon passes
- downloads
- validation
- OCR runs
- failed attempts
- abandoned approaches

This is the running operational journal.

### `decision-log.md`

Use for:

- non-trivial editorial judgments
- copy-text decisions
- witness-tier changes
- any reversible or contestable judgment call

This is where the reasoning lives.

### `human-log.md`

Use for:

- readable narrative explanation of what happened and why
- the prose log a reader can understand without parsing tables or JSON

This is chronological narrative, not TEI footnote content.

### `timeline.json`

Use for:

- ordered machine-readable event history
- state reconstruction
- slider replay
- visible text changes

This is the app-facing chronological backbone.

### `documents.json`

Use for:

- curated registration of the human-readable docs

Do not rely on markdown autodiscovery.

## Text-Change Rule

If visible edition text changes, that change must not live only in prose.

It must generate a `text_changed` timeline event.

Record at minimum:

- exact `locus_id`
- `change_kind`
- `reason`
- `witness_support`
- `note_anchor_id` if a visible note was created

Preferred storage model:

- a top-level per-locus readings table
- `reading_before` / `reading_after` indices in the event

Fallback only if needed:

- `previous_reading`
- `new_reading`

Capture the earlier state at the moment of change, before overwrite.

## Required Actor Logging

Every intervention must record:

- what changed
- why
- evidence
- confidence
- actor type: `agent`, `human`, or `hybrid`
- actor id or person name when known
- previous state when changed
- new state when changed

If the action changes visible text, also record:

- exact `locus_id`
- before/after reading state
- whether a visible note anchor was added

## Required Step Logging

Do not log only final decisions.

Log every meaningful step during the run, including:

- recon searches
- source pages checked
- witness acceptance
- witness rejection
- failed or partial downloads
- rights checks
- OCR runs
- OCR failures
- manual adjudication passes
- apparatus-affecting choices
- page-role classification decisions

Each step log entry should record:

- date
- step type
- object worked on
- action taken
- outcome
- evidence or URLs
- next step if unresolved
- actor type: `agent`, `human`, or `hybrid`
- whether current edition state changed
- state delta if it did

If the step changed text, also create the matching `text_changed` event in `timeline.json`.

## Page-Role Rule

Do not assume the whole scanned witness is the target text body.

Before deep correction, classify witness pages into roles such as:

- title
- preface
- body
- commentary
- colophon
- blank
- other

The physical page count of a witness is not the same thing as the length of the edited text.

## Required Output

The workflow does not stop at finding witnesses.

It ends in a full documented edition package:

- TEI XML
- `manifest.json`
- `process.json`
- `timeline.json`
- `apparatus.json`
- `stats.json`
- `documents.json`
- edition `README.md`
- witness READMEs with source and download links
- process log
- decision log
- human-readable log
- unresolved loci log

## Footnote boundary rule

Reader-facing TEI notes are allowed, but they must not absorb the jobs of the process logs.

Use a TEI footnote only when it is:

- tied to a visible locus
- useful to a reader from the text itself
- short enough to function as a note

Do not use TEI footnotes for:

- run chronology
- OCR troubleshooting stories
- full editorial decision essays
- duplicate prose already present in `human-log.md`

Keep the surfaces distinct:

- `human-log.md` = readable chronological narrative
- `decision-log.md` = full reasoning trail
- `timeline.json` = machine state history
- `apparatus.json` = structured textual evidence
- TEI notes = short reader-facing locus notes

## Surface separation rule

Do not treat these as the same thing:

- critical reading text
- witness comparison
- timeline replay

The critical text is the reader-default surface.

Witness comparison is where a user inspects what individual witnesses read at a locus.

Timeline replay is where a user inspects how the edition changed over time.

Do not substitute one for another.

## Final Validation Pass

Before calling the package done, run one last integrity pass.

At minimum confirm:

- all required JSON files parse
- schema validation passes where available
- `documents.json` points only to existing files
- manifest-declared files exist
- TEI note anchors and note targets resolve
- timeline references and apparatus references resolve
- footnotes are not carrying process-log or human-log content by mistake

## Files To Read

1. `README.md`
2. `CRITICAL_EDITION_GUIDED_WORKFLOW.md`
3. `CRITICAL_EDITION_RECORDING_MATRIX.md`
4. `CRITICAL_EDITION_ENTRYPOINT.md`
5. `CRITICAL_EDITION_SYSTEM_SPEC_2026-04-14.md`
6. `WORKFLOW.md`
7. `REPO_INTAKE_PIPELINE.md`
8. `TRANSCRIPTION_METHOD.md`
9. `STANDARD_TRANSCRIPTION_WORKFLOW.md`

If the work has family notes, read them too.

Examples:

- `FAITH_IN_MIND_WITNESSES.md`
- `FAITH_IN_MIND_STEMMA.md`
- `WUMENGUAN_NOTE.md`

## Documentation Rule

Every witness README should include:

- source page
- best direct download path we know
- rights basis
- enough metadata to relocate the witness if the direct link dies

## Bad Download Rule

If a downloaded file looks structurally bad, do not assume the source witness is bad.

Before treating the witness as broken:

1. hash the current local file
2. re-download it
3. hash the replacement
4. compare the hashes
5. re-run validation

Interpretation:

- same hash + same failure:
  likely upstream-bad or consistently malformed
- different hash + fixed validation:
  earlier local download was bad
- different hash + same structural failure:
  source delivery may be unstable, or multiple bad variants may exist upstream

If command-line download keeps producing unstable or malformed results for a large file:

- give the user the exact direct file URL
- ask for a browser download
- once the browser-downloaded file is placed in the repo, swap it into the canonical witness folder
- hash and validate it immediately

This should be suggested automatically once:

- repeated command-line downloads yield different hashes
- or a large file keeps failing structure checks

## Launch Sentence

`Make a critical edition of {FolderName}. Follow CRITICAL_EDITION_GUIDED_WORKFLOW.md and ask me how many witnesses to find before locking the witness set.`
