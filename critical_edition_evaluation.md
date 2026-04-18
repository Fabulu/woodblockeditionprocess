# Evaluation of Woodblock Edition Process & AI-Driven Critical Editions

## Part 1 — Is AI Alone Enough for a Real Critical Edition?

**Short answer:**  
AI can power a critical edition pipeline, but it cannot yet be trusted as the sole editor.

**Stronger formulation:**
> AI can be the engine. It should not be the unquestioned editor.

### Why not fully AI-driven?

A real critical edition requires:
- distinguishing OCR noise vs real variants
- handling damaged scans and weird glyphs
- separating commentary from base text
- reasoning about transmission (omission, expansion, smoothing, contamination)
- knowing when the evidence is weak

AI is currently bad at:
- uncertainty handling
- epistemic humility
- not hallucinating clean answers

### What AI *is* good at

- OCR assistance
- witness triage
- segmentation
- variant collation
- clustering readings
- proposing relationships
- surfacing suspicious passages
- drafting apparatus notes
- logging provenance

### What AI should not do alone

- finalize readings silently
- normalize uncertain characters without audit
- collapse ambiguity
- pretend certainty

### Correct model

> AI proposes, human audits, system records.

or

> AI drives the car, human keeps hands near the wheel.

### Realistic future

Not:
> “AI makes the edition”

But:
> “AI produces a fully inspectable editorial argument at scale”

---

## Part 2 — Evaluation of Your Process

## Can This Become Something Real?

Yes — with some tweaks and active correction, you can build something **real**.

You already have:
- Process discipline
- Provenance awareness
- Multi-witness thinking
- Layer separation

Most projects fail to achieve even one.

---

## What Makes It “Real”

> A third party can inspect your edition and disagree with you without reverse-engineering your process.

That is the threshold.

---

## Non-Negotiable Improvements

### 1. Single Source of Truth

Fix documentation drift:
- `current-state.md` is authoritative
- everything else derives from it

---

### 2. Explicit Evidence Basis

Every change must record:
- source (scan, OCR, witness, etc.)
- strength of evidence

---

### 3. Hard Stage Separation

- Recon
- Transcription
- Collation
- Edition

Never mix them.

---

### 4. Preserve Uncertainty

Do NOT:
- smooth ambiguity
- collapse variants early

DO:
- track unresolved loci
- mark weak readings

---

## What You’re Actually Building

Not:
> AI makes a critical edition

But:
> A system that produces a fully inspectable editorial argument

---

## Why Your Idea Is Actually New

Most projects:
- preserve rigor
- hide process

You:
- preserve rigor
- expose process

Your UI ideas (slider, hover, timeline) are:
> interfaces to the apparatus

---

## Brutal Reality

If you:
- allow drift
- let AI silently decide
- hide uncertainty

→ becomes AI slop

If you:
- enforce discipline
- track evidence
- preserve uncertainty

→ becomes credible

---

## Final Verdict

Yes, you can build something real.

The core requirement:

> Every editorial decision must be traceable, reversible, and inspectable.
