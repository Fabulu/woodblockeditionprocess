# Woodblock Edition Process

This repo is for producing rigorous critical editions of Zen texts from free witnesses, with scans first and plain text only as a fallback.

The goal is not just to collect source files. The goal is to produce a documented edition workflow that can feed ReadZen / OpenZen with:

- trusted witness attribution
- OCR-first transcription evidence
- logged editorial decisions
- apparatus and notes
- machine-readable process data

## Guided Mode

If you want the guided mode, start with:

- `CRITICAL_EDITION_GUIDED_WORKFLOW.md`

That is the file to point an agent at when you want to say:

`Make a critical edition of XXX`

In guided mode, the agent should:

1. ask how many witnesses to try to find before locking the witness set
2. help define the scope of the edition
3. find and classify witnesses
4. prompt for the decisions needed to continue
5. carry the work through provenance, OCR, collation, apparatus, and packaging

## Core Files

Read these first:

1. `README.md`
2. `CRITICAL_EDITION_GUIDED_WORKFLOW.md`
3. `CRITICAL_EDITION_RECORDING_MATRIX.md`
4. `CRITICAL_EDITION_ENTRYPOINT.md`
5. `CRITICAL_EDITION_SYSTEM_SPEC_2026-04-14.md`
6. `OPENZENTEXTS_PROVENANCE_AUDIT_2026-04-14.md`
7. `PROGRAMMER_AGENT_MASTER_IMPLEMENTATION_BRIEF_2026-04-14.md`
8. `WORKFLOW.md`
9. `REPO_INTAKE_PIPELINE.md`
10. `TRANSCRIPTION_METHOD.md`
11. `STANDARD_TRANSCRIPTION_WORKFLOW.md`

## Repo Rule

This repo must be usable on its own.

Critical workflow files should live here, not only in another local checkout.

OpenZenTexts and the reader code are still relevant implementation targets, but this repo should contain the workflow and planning documents needed to run the edition process without depending on local absolute paths in the basic instructions.

## Shared Path Rule

Shared markdown in this repo must not use:

- local absolute paths like `C:\...`
- renderer-only absolute links

Use instead:

- repo-relative paths like `FAITH_IN_MIND_WITNESSES.md`
- repo-name-relative paths when another repo is involved, such as `OpenZenTexts/xml-open/pd/wumenguan-1632/manifest.json`
- normal web URLs for online sources

## Attribution Rule

Each witness README should record:

- the stable source page
- the best direct download path we know
- the rights basis
- enough metadata to relocate the witness if a direct link dies

## Large-File Rule

When a large witness PDF fails validation:

- compare hashes across repeated downloads
- do not assume the witness itself is bad until you know whether the bytes are stable
- if command-line download keeps producing bad or inconsistent files, use the exact direct URL in a browser, then hash and validate the browser-downloaded copy

## Edition Rule

Every intervention must be logged, including agent decisions, not just human ones.

Actor types:

- `agent`
- `human`
- `hybrid`

## Current Example Families

Useful work-family anchors already in this repo:

- `FAITH_IN_MIND_WITNESSES.md`
- `FAITH_IN_MIND_STEMMA.md`
- `WUMENGUAN_NOTE.md`

## Launch Sentence

`Make a critical edition of {FolderName}. Follow CRITICAL_EDITION_GUIDED_WORKFLOW.md and ask me how many witnesses to find before locking the witness set.`
