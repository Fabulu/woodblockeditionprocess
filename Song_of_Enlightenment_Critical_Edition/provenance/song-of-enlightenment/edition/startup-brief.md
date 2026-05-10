# Startup Brief

This package starts from a strong poem-first assumption:

- exact poem witness first
- commentary second
- translation third

The initial task is not OCR or editing. It is to build a trustworthy witness family map for `永嘉證道歌`.

The first acquisition priority is the strongest standalone exact witness beyond the inherited `四部録` anthology copy.

Do not stop after one acquisition.

For this text, the startup rule is:

1. pin the strongest standalone witness
2. immediately widen the exact witness family
3. split category-level witness families into file-level witness objects
4. keep watching for exact witnesses outside the first category clusters
5. log second-wave commentary-family leads while the hunt is still warm
6. widen into Korean, anthology, and manuscript families before copy-text lock
7. keep derivative anthology branches separate from the main anthology line
8. only then stabilize the family map and consider copy-text lock

That startup rule has now been satisfied far enough to enter OCR preflight.

The next startup rule is:

1. start OCR from the held first-tier exact core, not from commentary or derivative controls
2. require page-plus-line anchors for every poem locus from the first OCR tranche
3. require PaddleOCR `return_word_box: True` so character-level evidence can be retained for contested loci
4. require `evidence_tier` and `char_coverage` fields in anchor planning from the start
5. keep `YJG-W12` open as a capture blocker without letting it block OCR on the already held core
