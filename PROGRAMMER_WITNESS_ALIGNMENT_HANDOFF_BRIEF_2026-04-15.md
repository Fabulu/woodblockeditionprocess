# Programmer Brief: Witness Alignment Handoff Contract

Date: 2026-04-15
Audience: architect, implementer, viewer programmer
Purpose: define how the edition pipeline will hand witness outputs to the program so the program can reliably compare witnesses at a locus.

## Core requirement

The program must be able to answer:

- what does witness `X` read at edition locus `Y`?

This is now a hard delivery requirement.

The pipeline will not hand off only loose witness text files.

It will hand off:

- definitive witness text artifacts
- machine-readable witness registry data
- machine-readable witness-to-locus alignment data

## What not to assume

Do not assume:

- every witness can be forced into the same visual line breaks as the critical text
- every witness has one clean line for every critical-text line
- commentary witnesses, anthology witnesses, or damaged witnesses will align one-to-one by display line

That assumption will fail often.

The contract is machine-readable alignment, not visual sameness.

## Preferred model

Preferred contract:

- one shared edition `locus_id` space
- the critical text uses those `locus_id`s
- the apparatus uses those `locus_id`s
- each delivered witness can answer its reading at that `locus_id`

Ideal result:

- `getWitnessReading(witnessId, locusId)` returns a stable payload without the UI having to infer anything from raw files

## Required fallback model

If exact one-line-to-one-line alignment is not possible, the fallback is:

- stable witness text file
- stable witness-local anchors
- a locus map from edition `locus_id` to witness-local span
- explicit gap or uncertainty statuses

Witness-local anchors may be:

- page-line ids
- segment ids
- token-span ids
- other stable witness-internal anchors

Each mapping record should be able to say:

- `locus_id`
- `witness_id`
- `start_anchor`
- `end_anchor`
- `status`

Recommended status values:

- `present`
- `omitted`
- `lacuna`
- `unreadable`
- `uncertain_span`

## Expected delivered artifacts

At minimum, expect these:

### 1. `witnesses.json`

Registry of all delivered witnesses.

Each witness entry should include:

- `witness_id`
- `siglum`
- `label`
- `role`
- `definitive_text_file`
- `text_status`
- `completeness`
- `confidence`
- `alignment_mode`
- `locus_map_file`

Recommended `alignment_mode` values:

- `direct_locus`
- `locus_to_span`
- `page_line_map`

### 2. definitive witness text files

Human-readable and copyable.

Examples:

- `witness-texts/T1.txt`
- `witness-texts/T4.txt`

### 3. witness locus companion

Machine-readable companion for locus lookup.

Examples:

- `witness-texts/T1.loci.json`
- `witness-texts/T4.loci.json`

This companion should let the app open the witness at a locus without scraping OCR working folders.

### 4. apparatus / reading payload

The app may also use:

- `apparatus.json`
- derived `witness-readings.json`

But witness alignment must not depend on the UI inventing mappings at runtime.

## Recommended witness locus payload shape

Either of these is acceptable.

### Option A: direct per-locus reading

```json
{
  "witness_id": "T1",
  "loci": [
    {
      "locus_id": "fim-0027",
      "status": "present",
      "text": "須臾返照勝卻前空"
    }
  ]
}
```

### Option B: locus-to-span mapping

```json
{
  "witness_id": "T1",
  "anchors": {
    "T1-p027.l01": {
      "text": "須臾返照勝卻前空"
    }
  },
  "loci": [
    {
      "locus_id": "fim-0027",
      "status": "present",
      "start_anchor": "T1-p027.l01",
      "end_anchor": "T1-p027.l01"
    }
  ]
}
```

## Viewer behavior expected

The viewer should be able to:

1. open witness comparison from a critical-text locus
2. ask for all witness readings at that locus
3. show differing witnesses first
4. expand to all witnesses
5. show omissions, lacunae, and unreadable coverage honestly
6. open the full delivered witness text for a selected siglum
7. copy a witness reading or the whole comparison block

## What the viewer must not do

Do not make the UI:

- infer alignment from filenames
- scrape OCR working directories
- derive witness comparison from timeline data
- assume every witness has the same visible line layout

## Handling unresolved alignment

If a witness or a locus cannot yet be aligned confidently:

- expose that honestly in the payload
- do not fabricate a clean mapping

Acceptable unresolved states:

- witness delivered, locus unresolved
- witness partially aligned
- witness aligned only by span, not by exact line

Unacceptable:

- silent fallback to guessed matching

## Practical reading of the contract

For the program, the real rule is:

- compare by shared `locus_id`
- display by witness-local text
- navigate by witness-local anchors when needed

That gives us robust witness comparison even when the physical witnesses do not share the same lineation.
