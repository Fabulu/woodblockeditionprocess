# Guided Critical Edition Workflow

Date: 2026-04-14
Purpose: a single file to use when the user says "Make a critical edition of XXX" and wants guided help through the whole process.

## Use

Use this file when the user gives you:

- one starting folder in `C:\woodblocks`
- one work title
- or one simple request like `Make a critical edition of Faith in Mind`

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

## Required Actor Logging

Every intervention must record:

- what changed
- why
- evidence
- confidence
- actor type: `agent`, `human`, or `hybrid`
- actor id or person name when known

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

1. [README.md](/abs/path/C:/woodblocks/README.md:1)
2. [CRITICAL_EDITION_GUIDED_WORKFLOW.md](/abs/path/C:/woodblocks/CRITICAL_EDITION_GUIDED_WORKFLOW.md:1)
3. [CRITICAL_EDITION_ENTRYPOINT.md](/abs/path/C:/woodblocks/CRITICAL_EDITION_ENTRYPOINT.md:1)
4. [CRITICAL_EDITION_SYSTEM_SPEC_2026-04-14.md](/abs/path/C:/woodblocks/CRITICAL_EDITION_SYSTEM_SPEC_2026-04-14.md:1)
5. [WORKFLOW.md](/abs/path/C:/woodblocks/WORKFLOW.md:1)
6. [REPO_INTAKE_PIPELINE.md](/abs/path/C:/woodblocks/REPO_INTAKE_PIPELINE.md:1)
7. [TRANSCRIPTION_METHOD.md](/abs/path/C:/woodblocks/TRANSCRIPTION_METHOD.md:1)
8. [STANDARD_TRANSCRIPTION_WORKFLOW.md](/abs/path/C:/woodblocks/STANDARD_TRANSCRIPTION_WORKFLOW.md:1)

If the work has family notes, read them too.

Examples:

- [FAITH_IN_MIND_WITNESSES.md](/abs/path/C:/woodblocks/FAITH_IN_MIND_WITNESSES.md:1)
- [FAITH_IN_MIND_STEMMA.md](/abs/path/C:/woodblocks/FAITH_IN_MIND_STEMMA.md:1)
- [WUMENGUAN_NOTE.md](/abs/path/C:/woodblocks/WUMENGUAN_NOTE.md:1)

## Documentation Rule

Every witness README should include:

- source page
- best direct download path we know
- rights basis
- enough metadata to relocate the witness if the direct link dies

## Launch Sentence

`Make a critical edition of C:\woodblocks\{FolderName}. Follow C:\woodblocks\CRITICAL_EDITION_GUIDED_WORKFLOW.md and ask me how many witnesses to find before locking the witness set.`
