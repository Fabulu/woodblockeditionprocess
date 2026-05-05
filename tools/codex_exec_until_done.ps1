param(
    [Parameter(Position = 0)]
    [string]$Prompt,

    [string]$PromptFile,

    [string]$ProjectRoot = "C:\woodblocks\Faith_in_Mind_Critical_Edition",

    [string]$CodexWorkingDir = "C:\woodblocks",

    [switch]$Ephemeral,

    [int]$MaxRuns = 0,

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
        '(?i)\bstronger direct-image-separation phase was exhausted\b',
        '(?i)\bstronger direct image separation phase was exhausted\b',
        '(?i)\bexhausted without new safe `?T1`? text changes\b',
        '(?i)\bpackage was already at the required stop state\b',
        '(?i)\balready reflects completion of the requested stronger direct-image-separation phase\b',
        '(?i)\balready reflects the completed stronger direct-image-separation pass\b',
        '(?i)\balready reflects completion of the requested 12-locus visual-evidence workbench phase\b',
        '(?i)\balready reflects completion of the requested 12-locus visual-evidence workbench\b',
        '(?i)\bvisual-evidence workbench phase was exhausted\b',
        '(?i)\bvisual evidence workbench phase was exhausted\b',
        '(?i)\bpackage state already reflects completion of the requested 12-locus visual-evidence workbench phase\b',
        '(?i)\bthe recorded workbench covers all 12 target holdouts\b',
        '(?i)\blocus-specific corroborative-evidence phase was exhausted\b',
        '(?i)\blocus specific corroborative evidence phase was exhausted\b',
        '(?i)\bbounded corroborative-evidence phase was exhausted\b',
        '(?i)\bbounded corroborative evidence phase was exhausted\b',
        '(?i)\balready reflects completion of the requested locus-specific corroborative-evidence phase\b',
        '(?i)\balready reflects completion of the requested locus specific corroborative evidence phase\b',
        '(?i)\bbroad corroborative hunt .* was exhausted\b',
        '(?i)\bbroad corroborative-hunt .* was exhausted\b',
        '(?i)\biterative broad corroborative hunt .* was exhausted\b',
        '(?i)\biterative broad corroborative-hunt .* was exhausted\b',
        '(?i)\balready reflects completion of the requested broad corroborative hunt\b',
        '(?i)\balready reflects completion of the requested iterative broad corroborative hunt\b',
        '(?i)\balready contains the completed continuation\b',
        '(?i)\balready includes the continuation you asked for\b',
        '(?i)\bcurrent package state already includes the continuation you asked for\b',
        '(?i)\bcurrent package state already includes the continuation\b',
        '(?i)\bthis continuation was completed\b',
        '(?i)\bstate no longer has 9 holdouts; it has 8\b',
        '(?i)\bno longer has 9 holdouts; it has 8\b',
        '(?i)\bno further bounded productive correction slice is currently available anywhere in the remaining unresolved queue\b',
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

function Test-RetriableCodexFailure {
    param(
        [string]$LastMessage,
        [string[]]$JsonLines
    )

    $retryPatterns = @(
        '(?i)\bstream disconnected before completion\b',
        '(?i)\berror sending request for url\b',
        '(?i)\bconnection reset\b',
        '(?i)\bconnection aborted\b',
        '(?i)\btemporarily unavailable\b',
        '(?i)\btimeout\b',
        '(?i)\btimed out\b'
    )

    $candidateTexts = @()
    if (-not [string]::IsNullOrWhiteSpace($LastMessage)) {
        $candidateTexts += $LastMessage
    }
    if ($JsonLines) {
        $candidateTexts += ($JsonLines -join "`n")
    }

    foreach ($text in $candidateTexts) {
        foreach ($pattern in $retryPatterns) {
            if ($text -match $pattern) {
                return @{
                    Retry = $true
                    Reason = $pattern
                }
            }
        }
    }

    return @{
        Retry = $false
        Reason = "non_retriable_failure"
    }
}

$promptText = Get-PromptText
$tmpDir = Join-Path $ProjectRoot ".tmp_codex_gate"
New-Item -ItemType Directory -Force -Path $tmpDir | Out-Null

$suppressedLogPath = Join-Path $ProjectRoot "provenance\faith-in-mind\process\suppressed-codex-reports.log"
$loopLogPath = Join-Path $ProjectRoot "provenance\faith-in-mind\process\until-done-wrapper.log"

$runCount = 0
$useRunCap = $MaxRuns -gt 0

while ((-not $useRunCap) -or ($runCount -lt $MaxRuns)) {
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
        $retryDecision = Test-RetriableCodexFailure -LastMessage $lastMessage -JsonLines $jsonLines
        if ($retryDecision.Retry) {
            [Console]::Out.WriteLine("[$timestamp] run $runCount exited $exitCode due to transient transport failure ($($retryDecision.Reason)); relaunching after $SleepSeconds seconds")
            Start-Sleep -Seconds $SleepSeconds
            continue
        }

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

if ($useRunCap) {
    throw "Reached MaxRuns=$MaxRuns without hitting a terminal stop condition."
}
