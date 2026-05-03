# OCR Stop Gate: Faith in Mind

Use this file before stopping, yielding, or writing a status message during a long resumable OCR pass.

If the answer to all of the following is `yes`, you must not stop. You must relaunch the OCR loop instead.

1. Is the witness still incomplete on one or more required OCR engines?
2. Are page-level outputs still being saved cleanly?
3. Are the saved summaries either current or honestly reconcilable from the saved sidecars?
4. Has no new engine-level failure appeared beyond the already known timeout or warning pattern?
5. Does the package still validate after any required state updates?

If all five answers are `yes`, the required action is:

1. reconcile the newest saved extent
2. update state and logs honestly
3. rerun validation if state files changed
4. relaunch the unfinished OCR runner or runners immediately
5. do not return control to the human operator
6. do not stop in order to explain, summarize, reassure, or report progress

You may stop only if one of these is true:

- the witness has genuinely completed the four-engine OCR-compliance slice
- a new non-timeout engine failure has appeared
- package validation fails
- saved files and recorded summaries diverge in a way that is not safely reconcilable
- the human operator explicitly redirects the work
- clarification is genuinely required to avoid a risky or irreversible mistake

Forbidden stopping points:

- a shell timeout by itself
- a clean log-update checkpoint
- a successful validation run
- the feeling that a progress report is owed
- the desire to explain what happened while the OCR pass is still healthy and incomplete

For manual correction, comparison, and other non-OCR edition work, use `CONTINUATION_GATE.md`.
