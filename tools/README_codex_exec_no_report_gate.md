# Codex Exec No-Report Gate

This wrapper is a practical substitute for client-side hooks in Codex when running long, interruption-sensitive edition work.

## What it does

- runs `codex exec --json`
- captures the final assistant message
- suppresses that message on successful runs by default
- only prints the final message if:
  - Codex exits non-zero
  - the final message looks like a blocking failure
  - you explicitly pass `-AllowReport`

Suppressed successful closeouts are still logged to:

- `Faith_in_Mind_Critical_Edition/provenance/faith-in-mind/process/suppressed-codex-reports.log`

## What it does not do

- it does not change interactive `codex` or desktop-app behavior
- it is not a true pre-send hook inside the Codex client
- it cannot prove semantic completion; it only blocks routine successful closeouts from reaching the terminal

## Usage

From `C:\woodblocks`:

```powershell
.\tools\codex_exec_no_report_gate.ps1 -PromptFile .\my-prompt.txt
```

To let the final message through intentionally:

```powershell
.\tools\codex_exec_no_report_gate.ps1 -PromptFile .\my-prompt.txt -AllowReport
```

## Why this exists

The current local Codex installation exposes:

- `C:\Users\Fabian Trunz\.codex\config.toml`
- `C:\Users\Fabian Trunz\.codex\rules\default.rules`

but no visible user-configurable pre-send hook mechanism comparable to Claude Code hooks.
