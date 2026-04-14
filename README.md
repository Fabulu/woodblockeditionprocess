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

- [CRITICAL_EDITION_GUIDED_WORKFLOW.md](/abs/path/C:/woodblocks/CRITICAL_EDITION_GUIDED_WORKFLOW.md:1)

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

1. [README.md](/abs/path/C:/woodblocks/README.md:1)
2. [CRITICAL_EDITION_GUIDED_WORKFLOW.md](/abs/path/C:/woodblocks/CRITICAL_EDITION_GUIDED_WORKFLOW.md:1)
3. [CRITICAL_EDITION_ENTRYPOINT.md](/abs/path/C:/woodblocks/CRITICAL_EDITION_ENTRYPOINT.md:1)
4. [CRITICAL_EDITION_SYSTEM_SPEC_2026-04-14.md](/abs/path/C:/woodblocks/CRITICAL_EDITION_SYSTEM_SPEC_2026-04-14.md:1)
5. [OPENZENTEXTS_PROVENANCE_AUDIT_2026-04-14.md](/abs/path/C:/woodblocks/OPENZENTEXTS_PROVENANCE_AUDIT_2026-04-14.md:1)
6. [PROGRAMMER_AGENT_MASTER_IMPLEMENTATION_BRIEF_2026-04-14.md](/abs/path/C:/woodblocks/PROGRAMMER_AGENT_MASTER_IMPLEMENTATION_BRIEF_2026-04-14.md:1)
7. [WORKFLOW.md](/abs/path/C:/woodblocks/WORKFLOW.md:1)
8. [REPO_INTAKE_PIPELINE.md](/abs/path/C:/woodblocks/REPO_INTAKE_PIPELINE.md:1)
9. [TRANSCRIPTION_METHOD.md](/abs/path/C:/woodblocks/TRANSCRIPTION_METHOD.md:1)
10. [STANDARD_TRANSCRIPTION_WORKFLOW.md](/abs/path/C:/woodblocks/STANDARD_TRANSCRIPTION_WORKFLOW.md:1)

## Repo Rule

This repo must be usable on its own.

Critical workflow files should live here, not only in another local checkout.

OpenZenTexts and the reader code are still relevant implementation targets, but this repo should contain the workflow and planning documents needed to run the edition process without depending on `C:\Programmieren\OpenZenTexts\...` paths in the basic instructions.

## Attribution Rule

Each witness README should record:

- the stable source page
- the best direct download path we know
- the rights basis
- enough metadata to relocate the witness if a direct link dies

## Edition Rule

Every intervention must be logged, including agent decisions, not just human ones.

Actor types:

- `agent`
- `human`
- `hybrid`

## Current Example Families

Useful work-family anchors already in this repo:

- [FAITH_IN_MIND_WITNESSES.md](/abs/path/C:/woodblocks/FAITH_IN_MIND_WITNESSES.md:1)
- [FAITH_IN_MIND_STEMMA.md](/abs/path/C:/woodblocks/FAITH_IN_MIND_STEMMA.md:1)
- [WUMENGUAN_NOTE.md](/abs/path/C:/woodblocks/WUMENGUAN_NOTE.md:1)

## Launch Sentence

`Make a critical edition of C:\woodblocks\{FolderName}. Follow C:\woodblocks\CRITICAL_EDITION_GUIDED_WORKFLOW.md and ask me how many witnesses to find before locking the witness set.`
