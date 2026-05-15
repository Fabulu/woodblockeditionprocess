from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
PROCESS_DIR = ROOT / "provenance" / "song-of-enlightenment" / "process"
WITNESS_DIR = ROOT / "provenance" / "song-of-enlightenment" / "witnesses"
XML_DIR = ROOT / "xml-open" / "ce" / "song-of-enlightenment"


REQUIRED_FILES = [
    PROCESS_DIR / "current-state.md",
    PROCESS_DIR / "edition-plan.md",
    PROCESS_DIR / "process-log.md",
    PROCESS_DIR / "decision-log.md",
    PROCESS_DIR / "human-log.md",
    PROCESS_DIR / "publication-checklist.md",
    PROCESS_DIR / "prior-editions-register.md",
    PROCESS_DIR / "interedition-overlap-log.md",
    PROCESS_DIR / "interedition-precedence-table.json",
    PROCESS_DIR / "unresolved-loci.md",
    PROCESS_DIR / "correction-log.md",
    PROCESS_DIR / "translation-diff-log.md",
    PROCESS_DIR / "ocr-consensus-log.md",
    PROCESS_DIR / "rejected-readings-log.md",
    PROCESS_DIR / "translation-reasoning-log.md",
    PROCESS_DIR / "character-provenance-log.md",
    PROCESS_DIR / "anchor-base-register.jsonl",
    PROCESS_DIR / "anchor-event-log.jsonl",
    WITNESS_DIR / "witness-register.md",
    WITNESS_DIR / "acquisition-metadata.md",
    XML_DIR / "README.md",
    XML_DIR / "process.json",
    XML_DIR / "timeline.json",
    XML_DIR / "manifest.json",
    XML_DIR / "apparatus.json",
    XML_DIR / "documents.json",
    XML_DIR / "stats.json",
    XML_DIR / "song-of-enlightenment.xml",
    ROOT / "provenance" / "song-of-enlightenment" / "edition" / "working-critical-text.md",
    ROOT / "provenance" / "song-of-enlightenment" / "edition" / "editorial-method.md",
    ROOT / "provenance" / "song-of-enlightenment" / "edition" / "editorial-introduction.md",
    ROOT / "provenance" / "song-of-enlightenment" / "edition" / "commentary-secondary-track.md",
]


def fail(message: str) -> int:
    print(f"VALIDATION FAILED: {message}")
    return 1


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def main() -> int:
    missing = [str(path.relative_to(ROOT)) for path in REQUIRED_FILES if not path.exists()]
    if missing:
        return fail(f"missing required files: {missing}")

    process_json = load_json(XML_DIR / "process.json")
    timeline = load_json(XML_DIR / "timeline.json")
    manifest = load_json(XML_DIR / "manifest.json")
    documents = load_json(XML_DIR / "documents.json")
    stats = load_json(XML_DIR / "stats.json")

    required_process_keys = [
        "project",
        "current_phase",
        "current_slice",
        "last_completed_slice",
        "next_required_action",
        "next_required_slice",
        "last_text_changed_event",
    ]
    for key in required_process_keys:
        if key not in process_json:
            return fail(f"process.json missing key: {key}")

    if "events" not in timeline or not isinstance(timeline["events"], list):
        return fail("timeline.json missing events list")
    if len(timeline["events"]) < 2:
        return fail("timeline.json should contain at least two startup events")

    if "witnesses" not in manifest or not isinstance(manifest["witnesses"], list):
        return fail("manifest.json missing witnesses list")

    if "documents" not in documents or not isinstance(documents["documents"], list):
        return fail("documents.json missing documents list")

    if "project" not in stats:
        return fail("stats.json missing project block")

    validator = ROOT.parent / "tools" / "validate_openzentexts_tei.py"
    tei_path = XML_DIR / "song-of-enlightenment.xml"
    try:
        subprocess.run(
            [sys.executable, str(validator), str(tei_path)],
            check=True,
            capture_output=True,
            text=True,
        )
    except subprocess.CalledProcessError as exc:
        return fail(exc.stderr.strip() or exc.stdout.strip() or "TEI validation failed")

    print("VALIDATION PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
