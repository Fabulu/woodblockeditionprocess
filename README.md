# Woodblock Edition Process

This repo contains **125 witness folders** covering major Chinese Chan/Zen texts, with source scans, OCR outputs, collation data, and documented editorial workflows. It feeds the [OpenZen](https://github.com/Fabulu/OpenZenTexts) freely-licensed corpus and the [Read Zen](https://github.com/Fabulu/ReadZen) desktop + web reading environment.

The goal is not just to collect source files. The goal is to produce documented critical editions with:

- trusted witness attribution and provenance chains
- OCR-first transcription evidence (scans before plain text)
- logged editorial decisions (human, agent, and hybrid)
- apparatus and variant readings
- machine-readable process data for downstream tooling

## Current Scale

- **125 witness folders** — woodblock scans, library digitizations, and vetted free-text witnesses
- **25 workflow documents** — protocols, specs, briefs, and process logs
- Sources from NDL, NLC, CADAL, Kyoto University, Korea National Library, Harvard-Yenching, Waseda, Wikisource, and others
- Multi-witness coverage tracking for major works (Wumenguan: 5 witnesses, Biyanlu: 2, Congrong Lu: 1)

## Quick Start: Make a Critical Edition

Point an agent at the guided workflow:

```
Make a critical edition of {FolderName}.
Follow CRITICAL_EDITION_GUIDED_WORKFLOW.md and ask me how many witnesses
to find before locking the witness set.
```

In guided mode, the agent will:
1. Ask how many witnesses to find before locking the witness set
2. Help define the scope of the edition
3. Find and classify witnesses
4. Prompt for editorial decisions
5. Carry the work through provenance, OCR, collation, apparatus, and packaging

## Core Documents

| Document | Purpose |
|----------|---------|
| `CRITICAL_EDITION_GUIDED_WORKFLOW.md` | Agent-facing guided workflow (start here) |
| `CRITICAL_EDITION_ENTRYPOINT.md` | Human-facing overview and entry point |
| `CRITICAL_EDITION_RECORDING_MATRIX.md` | What to record at each stage |
| `CRITICAL_EDITION_SYSTEM_SPEC_2026-04-14.md` | Full system specification |
| `WORKFLOW.md` | Step-by-step edition process |
| `REPO_INTAKE_PIPELINE.md` | How finished editions flow into OpenZenTexts |
| `TRANSCRIPTION_METHOD.md` | OCR and transcription standards |
| `STANDARD_TRANSCRIPTION_WORKFLOW.md` | Standard operating procedure for transcription |
| `EDITION_AGENT_MASTER_INSTRUCTIONS.md` | Master instructions for edition agents |
| `EDITION_FORENSIC_PROVENANCE_PROTOCOL.md` | Provenance verification protocol |
| `EDITION_TRANSLATION_DIFF_PROTOCOL.md` | Translation comparison protocol |
| `ZEN_TEXT_WORKLIST.md` | Acquisition tracking for all target texts |
| `SOURCES.md` | Library and digital collection source list |

## Work Families

Active edition projects with multiple witnesses and collation in progress:

| Text | Witnesses | Status | Key Files |
|------|-----------|--------|-----------|
| Wumenguan (無門關) | 5 | Strong coverage | `WUMENGUAN_NOTE.md` |
| Faith in Mind (信心銘) | Multiple | Collation in progress | `FAITH_IN_MIND_WITNESSES.md`, `FAITH_IN_MIND_STEMMA.md` |
| Blue Cliff Record (碧巖錄) | 2 | Seeking 3rd witness | Multiple witness folders |
| Book of Serenity (從容錄) | 1 | Seeking 2nd witness | Multiple witness folders |

## Downstream Integration

Finished editions flow into:
- **[OpenZenTexts](https://github.com/Fabulu/OpenZenTexts)** — freely-licensed TEI XML with apparatus, provenance manifests, and witness delivery registry
- **[Read Zen](https://github.com/Fabulu/ReadZen)** — desktop app with witness comparison viewer, critical edition time-travel, and provenance browser
- **[readzen.pages.dev](https://readzen.pages.dev)** — web reader for the published texts

## Repo Rules

**Self-contained**: This repo must be usable on its own. All workflow documents live here, not in external checkouts.

**No absolute paths**: Use repo-relative paths (`FAITH_IN_MIND_WITNESSES.md`) or repo-name-relative paths (`OpenZenTexts/xml-open/pd/wumenguan-1632/manifest.json`).

**Attribution**: Each witness README records the stable source page, direct download path, rights basis, and enough metadata to relocate the witness if links die.

**Large files**: When a witness PDF fails validation, compare hashes across repeated downloads before assuming the witness is bad. Browser downloads may succeed where CLI tools fail.

**Logging**: Every intervention must be logged, including agent decisions. Actor types: `agent`, `human`, `hybrid`.
