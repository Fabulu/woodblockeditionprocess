from __future__ import annotations

import subprocess
from pathlib import Path


ROOT = Path(r"C:\woodblocks\Faith_in_Mind_Critical_Edition")
PAGE_COVERAGE_AUDIT = ROOT / "scripts" / "audit_witness_page_coverage.py"
TEI_QA = ROOT / "scripts" / "validate_faith_in_mind_tei.py"
TRANSLATION_SYNC_AUDIT = ROOT / "scripts" / "audit_translation_sync.py"


def main() -> int:
    subprocess.run(["python", str(PAGE_COVERAGE_AUDIT)], check=True)
    subprocess.run(["python", str(TEI_QA)], check=True)
    subprocess.run(["python", str(TRANSLATION_SYNC_AUDIT)], check=True)
    print("Faith in Mind package validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
