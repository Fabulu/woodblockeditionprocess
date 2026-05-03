param(
    [Parameter(Position = 0)]
    [string]$Prompt,

    [string]$PromptFile,

    [string]$ProjectRoot = "C:\woodblocks\Faith_in_Mind_Critical_Edition",

    [string]$CodexWorkingDir = "C:\woodblocks",

    [switch]$Ephemeral,

    [int]$MaxRuns = 100,

    [int]$SleepSeconds = 5
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

function Get-PromptText {
    if ($PromptFile) {
        $resolvedPromptFile = $ExecutionContext.SessionState.Path.GetUnresolvedProviderPathFromPSPath($PromptFile)
        return [System.IO.File]::ReadAllText($resolvedPromptFile, [System.Text.Encoding]::UTF8)
    }
    if ($Prompt) {
        return $Prompt
    }
    throw "Provide -Prompt or -PromptFile."
}

function Test-TerminalStop {
    param([string]$Text)

    if ([string]::IsNullOrWhiteSpace($Text)) {
        return @{
            Stop = $false
            Reason = "empty_message"
        }
    }

    $stopPatterns = @(
        '(?i)\bentire remaining unresolved package queue is actually exhausted\b',
        '(?i)\bentire remaining package queue is actually exhausted\b',
        '(?i)\bpackage-level evidence wall\b',
        '(?i)\bpackage level evidence wall\b',
        '(?i)\bpackage-local manual-correction queue is exhausted by a real evidence wall\b',
        '(?i)\bcurrent package-local manual-correction queue is exhausted by a real evidence wall\b',
        '(?i)\bglobal package-level stop\b',
        '(?i)\bworkflow queue is exhausted\b',
        '(?i)\bqueue is exhausted\b',
        '(?i)\bactive remaining page\/locus queue is actually exhausted\b',
        '(?i)\bgate file requires stopping\b',
        '(?i)\bneeds user input\b',
        '(?i)\bmissing external evidence\b',
        '(?i)\bpackage validation fails? and .* cannot repair\b',
        '(?i)\bstopped because .* queue is exhausted\b',
        '(?i)\bstopped because .* gate\b',
        '(?i)\bstopped because .* package-level\b',
        '(?i)\bstopped because .* package level\b',
        '(?i)\bstopped because .* evidence wall\b.*\bpackage\b'
    )

    foreach ($pattern in $stopPatterns) {
        if ($Text -match $pattern) {
            return @{
                Stop = $true
                Reason = $pattern
            }
        }
    }

    return @{
        Stop = $false
        Reason = "continue"
    }
}

$promptText = Get-PromptText
$tmpDir = Join-Path $ProjectRoot ".tmp_codex_gate"
New-Item -ItemType Directory -Force -Path $tmpDir | Out-Null

$suppressedLogPath = Join-Path $ProjectRoot "provenance\faith-in-mind\process\suppressed-codex-reports.log"
$loopLogPath = Join-Path $ProjectRoot "provenance\faith-in-mind\process\until-done-wrapper.log"

$runCount = 0

while ($runCount -lt $MaxRuns) {
    $runCount += 1
    $timestamp = Get-Date -Format "yyyyMMdd-HHmmss"
    $jsonlPath = Join-Path $tmpDir "codex-exec-$timestamp.jsonl"
    $lastMessagePath = Join-Path $tmpDir "codex-last-$timestamp.txt"

    $args = @(
        "exec",
        "--json",
        "--color", "never",
        "--cd", $ProjectRoot,
        "--output-last-message", $lastMessagePath
    )

    if ($Ephemeral) {
        $args += "--ephemeral"
    }

    $args += $promptText

    [Console]::Out.WriteLine("[$timestamp] starting run $runCount")

    $savedErrorAction = $ErrorActionPreference
    $ErrorActionPreference = "Continue"
    $jsonLines = & codex @args 2>&1
    $ErrorActionPreference = $savedErrorAction
    $exitCode = $LASTEXITCODE
    $jsonLines | Set-Content -Path $jsonlPath -Encoding UTF8

    $lastMessage = ""
    if (Test-Path $lastMessagePath) {
        $lastMessage = Get-Content -Raw -Path $lastMessagePath -Encoding UTF8
    }

    $entry = @(
        "## $timestamp",
        "run: $runCount",
        "exit_code: $exitCode",
        "jsonl: $jsonlPath",
        "last_message_file: $lastMessagePath",
        "message:",
        $lastMessage.TrimEnd(),
        ""
    ) -join "`r`n"

    Add-Content -Path $suppressedLogPath -Value $entry -Encoding UTF8
    Add-Content -Path $loopLogPath -Value $entry -Encoding UTF8

    if ($exitCode -ne 0) {
        [Console]::Out.WriteLine("[$timestamp] stopping after run $runCount because codex exited $exitCode")
        if (-not [string]::IsNullOrWhiteSpace($lastMessage)) {
            [Console]::Out.Write($lastMessage)
            if (-not $lastMessage.EndsWith("`n")) {
                [Console]::Out.WriteLine()
            }
        }
        exit $exitCode
    }

    $stopDecision = Test-TerminalStop -Text $lastMessage
    if ($stopDecision.Stop) {
        [Console]::Out.WriteLine("[$timestamp] stopping after run $runCount because terminal condition matched: $($stopDecision.Reason)")
        if (-not [string]::IsNullOrWhiteSpace($lastMessage)) {
            [Console]::Out.Write($lastMessage)
            if (-not $lastMessage.EndsWith("`n")) {
                [Console]::Out.WriteLine()
            }
        }
        exit 0
    }

    [Console]::Out.WriteLine("[$timestamp] run $runCount ended without a terminal stop condition; relaunching after $SleepSeconds seconds")
    Start-Sleep -Seconds $SleepSeconds
}

throw "Reached MaxRuns=$MaxRuns without hitting a terminal stop condition."
