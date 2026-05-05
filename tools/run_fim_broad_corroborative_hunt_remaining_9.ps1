param(
    [switch]$Ephemeral,
    [int]$MaxRuns = 250,
    [int]$SleepSeconds = 5
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$repoRoot = "C:\woodblocks"
$promptFile = Join-Path $repoRoot "tools\continue_fim_broad_corroborative_hunt_remaining_9.txt"
$wrapper = Join-Path $repoRoot "tools\codex_exec_until_done.ps1"

$args = @(
    "-ExecutionPolicy", "Bypass",
    "-File", $wrapper,
    "-PromptFile", $promptFile,
    "-MaxRuns", $MaxRuns,
    "-SleepSeconds", $SleepSeconds
)

if ($Ephemeral) {
    $args += "-Ephemeral"
}

& powershell @args
exit $LASTEXITCODE
