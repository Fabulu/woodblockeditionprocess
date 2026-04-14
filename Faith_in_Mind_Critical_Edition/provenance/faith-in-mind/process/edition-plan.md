# Edition Plan: Faith in Mind

Date: 2026-04-14
Status: planning
Slug: `faith-in-mind`
Work name: `Faith in Mind`
Work name zh: `信心銘`

## Goal

Produce a rigorous critical-edition package for `信心銘` from the free witness set already collected in this repo, using an OCR-first workflow and explicit decision logging.

## Current phase

Phase 0: package scaffold

This workspace exists to start cleanly after removing the premature `OpenZenTexts` scaffold.

No OCR, transcription, collation, or TEI text production has started here.

## Working scope

- Tier 1: primary text witnesses
- Tier 2: anthology / derivative witnesses
- Tier 3: translation / commentary / reception controls
- Tier 4: source-tradition controls

## Immediate tasks

1. Continue witness search until the credible free pool appears saturated.
2. Confirm rights basis, source page, and best download path for every accepted witness.
3. Acquire or re-acquire local files where needed.
4. Record hash, size, and local canonical filenames.
5. Lock the witness set.
6. Only then begin OCR and segmentation.

## Exclusions for this phase

- no OCR runs
- no manual transcription
- no copy-text lock
- no line-by-line collation
- no apparatus entries beyond placeholders
- no published reading text

## Governing docs

- `CRITICAL_EDITION_GUIDED_WORKFLOW.md`
- `CRITICAL_EDITION_ENTRYPOINT.md`
- `CRITICAL_EDITION_SYSTEM_SPEC_2026-04-14.md`
- `WORKFLOW.md`
- `TRANSCRIPTION_METHOD.md`
- `STANDARD_TRANSCRIPTION_WORKFLOW.md`

## Decision policy

Every decision must log:

- what changed
- why
- evidence
- confidence
- actor type: `agent`, `human`, or `hybrid`
- actor identifier when known
