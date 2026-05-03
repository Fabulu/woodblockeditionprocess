# Continuation Gate: Faith in Mind

Use this file before stopping, yielding, or writing a progress message during manual correction, comparison, or other bounded edition work.

Also open `STATUS_REPORT_GATE.md` before any progress, blocker, or closeout message. If `STATUS_REPORT_GATE.md` forbids the message, do not write it.

If the answer to all of the following is `yes`, you must not stop. You must continue the next bounded slice immediately.

1. Is the current edition task still active and incomplete?
2. Is there a clear next local step that does not require human judgment?
3. Does the package still validate after any required state updates?
4. Has no new blocker appeared that creates real uncertainty about the next edit or action?
5. Are you only tempted to stop because a page ended, a sub-slice closed cleanly, or a status summary feels owed?

If all five answers are `yes`, the required action is:

1. record the finished local change honestly
2. validate if state files changed
3. move directly into the next page, line, witness slice, or comparison slice
4. do not return control to the human operator
5. do not stop in order to explain what the next move would be
6. do not treat a neat narrative boundary as a task boundary

You may stop only if one of these is true:

- the requested job is genuinely complete
- a new blocker appears that requires human judgment
- package validation fails
- the evidence for the next reading is too weak and no other bounded productive slice is currently available
- the human operator explicitly redirects the work
- clarification is genuinely required to avoid a risky or irreversible mistake

Forbidden stopping points:

- finishing one page of a larger active run
- finishing one witness slice when another bounded slice is already ready
- a clean log-update checkpoint
- a successful validation run
- the feeling that a summary is owed
- writing `next I should...` when the next step is already available
- writing a message whose only content is that you should not be writing a message
