from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(r"C:\woodblocks\Faith_in_Mind_Critical_Edition")
PROCESS = ROOT / "provenance" / "faith-in-mind" / "process"
CORRECTION_LOG = PROCESS / "correction-log.md"
TRANSLATION_DIFF_LOG = PROCESS / "translation-diff-log.md"

LINE_LOCUS_RE = re.compile(r"T1-p\d{3}\.l\d{2}a?")
TABLE_ROW_RE = re.compile(r"^\|")
DATE_ROW_RE = re.compile(r"^\|\s*\d{4}-\d{2}-\d{2}\s*\|")
STEP_ROW_RE = re.compile(r"^\|\s*\d+\s*\|")


def extract_correction_loci(text: str) -> set[str]:
    loci: set[str] = set()
    for line in text.splitlines():
        if DATE_ROW_RE.match(line):
            loci.update(LINE_LOCUS_RE.findall(line))
    return loci


def extract_translation_loci(text: str) -> set[str]:
    loci: set[str] = set()
    for line in text.splitlines():
        if STEP_ROW_RE.match(line):
            loci.update(LINE_LOCUS_RE.findall(line))
    return loci


def main() -> int:
    correction_loci = extract_correction_loci(CORRECTION_LOG.read_text(encoding="utf-8", errors="replace"))
    translation_loci = extract_translation_loci(TRANSLATION_DIFF_LOG.read_text(encoding="utf-8", errors="replace"))

    missing = sorted(correction_loci - translation_loci)
    if missing:
        raise SystemExit(
            "Faith in Mind translation sync audit failed. Missing translation-diff coverage for: "
            + ", ".join(missing)
        )

    print("Faith in Mind translation sync audit passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
