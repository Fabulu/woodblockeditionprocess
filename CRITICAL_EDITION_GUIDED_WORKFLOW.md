# Guided Critical Edition Workflow

Date: 2026-04-14
Purpose: a single file to use when the user says "Make a critical edition of XXX" and wants guided help through the whole process.

## Use

Use this file when the user gives you:

- one starting folder in the repo
- one work title
- or one simple request like `Make a critical edition of Faith in Mind`

## Shared Path Rule

In shared markdown, do not use:

- local absolute paths like `C:\...`
- renderer-only absolute links

Use repo-relative paths or repo-name-relative paths instead.

## First Question

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
7. Confirm annotation depth.
8. Confirm intervention policy.
9. Confirm what counts as done.

## Default Rules

- free first
- scans before plain text
- OCR first
- exact source pages before secondary references
- every intervention logged
- agent decisions logged too, not just human decisions
- every meaningful step logged while it happens, not reconstructed later
- failed searches, rejected leads, failed downloads, OCR failures, and abandoned options logged too

## Required Actor Logging

Every intervention must record:

- what changed
- why
- evidence
- confidence
- actor type: `agent`, `human`, or `hybrid`
- actor id or person name when known

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

Each step log entry should record:

- date
- step type
- object worked on
- action taken
- outcome
- evidence or URLs
- next step if unresolved
- actor type: `agent`, `human`, or `hybrid`

## Required Output

The workflow does not stop at finding witnesses.

It ends in a full documented edition package:

- TEI XML
- `manifest.json`
- `process.json`
- `apparatus.json`
- `stats.json`
- edition `README.md`
- witness READMEs with source and download links
- process log
- decision log
- unresolved loci log

## Files To Read

1. `README.md`
2. `CRITICAL_EDITION_GUIDED_WORKFLOW.md`
3. `CRITICAL_EDITION_ENTRYPOINT.md`
4. `CRITICAL_EDITION_SYSTEM_SPEC_2026-04-14.md`
5. `WORKFLOW.md`
6. `REPO_INTAKE_PIPELINE.md`
7. `TRANSCRIPTION_METHOD.md`
8. `STANDARD_TRANSCRIPTION_WORKFLOW.md`

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

## Launch Sentence

`Make a critical edition of {FolderName}. Follow CRITICAL_EDITION_GUIDED_WORKFLOW.md and ask me how many witnesses to find before locking the witness set.`
