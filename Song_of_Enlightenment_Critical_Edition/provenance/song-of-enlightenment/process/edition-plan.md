# Edition Plan

## Scope

Produce a poem-first OpenZen critical edition of `永嘉證道歌` with:

- witness provenance
- scan and source-rights tracking
- machine-auditable process history
- selective apparatus
- synchronized Chinese and English change tracking
- evented anchor capture for future ReadZen time travel and evidence jumps

## Startup order

1. witness hunt
2. acquisition and rights locking
3. witness family map
4. OCR-first transcription
5. comparison and correction
6. apparatus and TEI package
7. ReadZen render handoff

## Initial witness priorities

1. inherited exact anthology witness in `四部録`
2. standalone exact witness lead from NDL / Commons
3. additional exact or near-exact Korean / Japanese print witnesses
4. later commentary witnesses
5. translation or reception witnesses

## Constraints

- no lamp records in the main edition scope
- commentary remains secondary until the poem witness base is secure
- translation must stay synchronized with every accepted Chinese change
- every accepted or rejected text-changing decision must carry an anchor packet
- the OCR-first phase must satisfy ReadZen tiered evidence capture:
  - page and line anchors for every poem line
  - character-tier evidence for apparatus or character-contested loci
  - PaddleOCR `return_word_box: True` when OCR is run on active witnesses
