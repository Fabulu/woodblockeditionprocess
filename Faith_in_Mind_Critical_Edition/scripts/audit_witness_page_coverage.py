from __future__ import annotations

import csv
import re
from pathlib import Path


ROOT = Path(r"C:\woodblocks\Faith_in_Mind_Critical_Edition")
PAGE_MAP = ROOT / "provenance" / "faith-in-mind" / "ocr" / "T1" / "page-map.csv"
TRANSCRIPTION = (
    ROOT
    / "provenance"
    / "faith-in-mind"
    / "transcription"
    / "corrected"
    / "T1-corrected-pass1-working.txt"
)
REPORT = (
    ROOT
    / "provenance"
    / "faith-in-mind"
    / "process"
    / "WITNESS_PAGE_COVERAGE_AUDIT.md"
)

PAGE_MARKER_RE = re.compile(r"^\[\[page:(T1-p\d{3})\]\]$")


def load_active_pages() -> tuple[list[str], set[str]]:
    ordered: list[str] = []
    known: set[str] = set()
    with PAGE_MAP.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            page_id = (row.get("page_id") or "").strip()
            if not page_id:
                continue
            known.add(page_id)
            role = (row.get("content_role") or "").strip().lower()
            if role == "blank":
                continue
            ordered.append(page_id)
    return ordered, known


def load_transcription_pages() -> list[str]:
    pages: list[str] = []
    for line in TRANSCRIPTION.read_text(encoding="utf-8").splitlines():
        match = PAGE_MARKER_RE.match(line.strip())
        if match:
            pages.append(match.group(1))
    return pages


def main() -> int:
    active_pages, known_pages = load_active_pages()
    transcription_pages = load_transcription_pages()

    if not active_pages:
        raise SystemExit("No active witness pages found in page-map.csv.")
    if not transcription_pages:
        raise SystemExit("No page markers found in corrected transcription.")

    transcription_set = set(transcription_pages)
    active_set = set(active_pages)

    missing = [page for page in active_pages if page not in transcription_set]
    unknown = [page for page in transcription_pages if page not in known_pages]

    out: list[str] = []
    out.append("# Witness Page Coverage Audit")
    out.append("")
    out.append(
        "Audit basis: `ocr/T1/page-map.csv` vs `transcription/corrected/T1-corrected-pass1-working.txt`."
    )
    out.append(
        f"Active non-blank witness range: `{active_pages[0]}` to `{active_pages[-1]}`."
    )
    out.append(f"Active non-blank pages checked: `{len(active_pages)}`.")
    out.append("")

    if missing:
        out.append("## Missing Transcription Pages")
        out.append("")
        for page in missing:
            out.append(
                f"- `{page}` is active in `page-map.csv` but has no `[[page:{page}]]` marker in the corrected transcription."
            )
        out.append("")

    if unknown:
        out.append("## Unknown Transcription Pages")
        out.append("")
        for page in unknown:
            out.append(
                f"- `{page}` is marked in the corrected transcription but has no matching `page_id` in `page-map.csv`."
            )
        out.append("")

    if not missing and not unknown:
        out.append("## Result")
        out.append("")
        out.append(
            "- Witness page coverage is complete for the active non-blank `T1` span."
        )
        out.append("")

    REPORT.write_text("\n".join(out), encoding="utf-8")
    print(REPORT)
    return 1 if missing or unknown else 0


if __name__ == "__main__":
    raise SystemExit(main())
