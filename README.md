# Woodblock Edition Process

[![License: MIT](https://img.shields.io/badge/License-MIT-green)](LICENSE)

A documented critical edition pipeline for Chinese Zen texts — from woodblock scan to provenance-verified, freely-licensed TEI XML. This repo contains **126 witness folders** across **50+ text families**, sourced from institutional digital archives worldwide.

Finished editions flow into [OpenZen](https://github.com/Fabulu/OpenZenTexts) and are readable in [Read Zen](https://github.com/Fabulu/ReadZen) (desktop) and [readzen.pages.dev](https://readzen.pages.dev) (web).

## Active Editions

### Wumenguan 無門關 (Gateless Barrier) — Published

The 1632 NDL woodblock reading edition is complete and published:

- **Primary witness**: NDL 12865429 (1632 woodblock, Wikimedia Commons, PD-old, ~188MB scan)
- **Secondary witness**: Waseda 1752 printing (WUL-bunko31_e1102) for cross-verification
- **Tertiary witness**: NDL Wumen Huikai Recorded Sayings (NDL2537788) for voice corroboration
- **Edition**: TEI XML with aligned line identifiers, CC0 1.0 license, no CBETA material
- **Published at**: [OpenZenTexts/xml-open/pd/wumenguan-1632](https://github.com/Fabulu/OpenZenTexts/tree/main/xml-open/pd/wumenguan-1632)
- **Read it**: [readzen.pages.dev/pd.wumenguan-1632](https://readzen.pages.dev/pd.wumenguan-1632)

Total witness coverage: **13 witnesses** from NDL, Waseda, Korea National Library, and Wikisource, spanning editions from 1632 to 1882.

### Faith in Mind 信心銘 (Xinxin Ming) — In Progress

A multi-witness critical edition with apparatus, currently in witness-freeze and scaffold phase:

- **30 locked witness items** across 4 families:
  - Standalone 三祖大師信心銘 texts
  - Four 四部録 anthology witnesses (Kyoto 1629 + 1631 printings, NDL, Waseda)
  - 四部録抄 derivative branch (2 witnesses)
  - 入衆日用 branch
- **17 commentary/translation controls** for editorial context
- **5 secondary source-tradition controls** (景徳伝燈録 variants, supplementary anthologies)
- Sources: Kyoto University RMDA, NDL, Waseda, Korea Commons
- Status: witness metadata locked, pending OCR and segmentation
- Key files: `FAITH_IN_MIND_WITNESSES.md`, `FAITH_IN_MIND_STEMMA.md`

## Scale

- **126 witness folders** — woodblock scans, library digitizations, and vetted free-text witnesses
- **50+ text families** — classical Zen compositions (500–1500 CE)
- **25 workflow documents** — protocols, specs, briefs, and process logs
- Sources: NDL, NLC, CADAL, Kyoto University, Korea National Library, Harvard-Yenching, Waseda, Wikisource

### Most-witnessed texts

| Text | Chinese | Witnesses | Status |
|------|---------|-----------|--------|
| Faith in Mind | 信心銘 | 30 (across families) | Scaffold phase |
| Wumenguan | 無門關 | 13 | Published (1632 edition) |
| Blue Cliff Record | 碧巖錄 | 5 | Seeking additional witnesses |
| Jingde Lamp Record | 景德傳燈錄 | 5 | Witness collection |
| Book of Serenity | 從容錄 | 4 | Seeking additional witnesses |
| Linji Record | 臨濟錄 | 4 | Witness collection |
| Huangbo texts | 黃檗 | 3 | Witness collection |

## The Edition Pipeline

```
Witness acquisition → Rights verification → OCR / transcription
    → Segmentation → Collation → Apparatus → TEI packaging
        → Provenance manifest → OpenZen intake → Read Zen
```

Every intervention is logged with actor type (`human`, `agent`, `hybrid`). The pipeline is designed for agent-assisted work: point a coding agent at the guided workflow and it will walk through the process step by step.

### Quick start

```
Make a critical edition of {FolderName}.
Follow CRITICAL_EDITION_GUIDED_WORKFLOW.md and ask me how many witnesses
to find before locking the witness set.
```

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
| `STANDARD_TRANSCRIPTION_WORKFLOW.md` | Standard operating procedure |
| `EDITION_AGENT_MASTER_INSTRUCTIONS.md` | Master instructions for edition agents |
| `EDITION_FORENSIC_PROVENANCE_PROTOCOL.md` | Provenance verification protocol |
| `ZEN_TEXT_WORKLIST.md` | Acquisition tracking for all target texts |
| `SOURCES.md` | Library and digital collection source list |

## Downstream

| Destination | What it receives |
|-------------|-----------------|
| [OpenZenTexts](https://github.com/Fabulu/OpenZenTexts) | TEI XML with apparatus, provenance manifests, witness delivery registry |
| [Read Zen desktop](https://github.com/Fabulu/ReadZen) | Witness comparison viewer, critical edition time-travel, provenance browser |
| [readzen.pages.dev](https://readzen.pages.dev) | Web reader for published editions |

## Repo Rules

- **Self-contained** — all workflow documents live here, not in external checkouts
- **No absolute paths** — use repo-relative paths or repo-name-relative paths
- **Attribution** — each witness README records source page, download path, rights basis, and relocatability metadata
- **Logging** — every intervention logged with actor type (`agent`, `human`, `hybrid`)
- **Rights-first** — all witnesses vetted for open/commercial compatibility; unclear-rights material excluded
