from __future__ import annotations

import json
import os
import subprocess
from pathlib import Path


PAGE_DIR = Path(r"C:\woodblocks\Faith_in_Mind_Critical_Edition\provenance\faith-in-mind\ocr\C4\page-images")
OUT_DIR = Path(__file__).resolve().parent
RUN_SUMMARY = OUT_DIR / "run-summary.json"
TESSERACT_EXE = Path(r"C:\Program Files\Tesseract-OCR\tesseract.exe")
TESSDATA_PREFIX = Path(r"C:\woodblocks\Faith_in_Mind_Critical_Edition\provenance\faith-in-mind\ocr\T1\tessdata")


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    pages = sorted(PAGE_DIR.glob("C4-p*.png"))
    if RUN_SUMMARY.exists():
        summary = json.loads(RUN_SUMMARY.read_text(encoding="utf-8"))
        summary["resumed"] = True
    else:
        summary = {
            "engine": "Tesseract",
            "witness_id": "C4",
            "input_dir": str(PAGE_DIR),
            "tesseract_exe": str(TESSERACT_EXE),
            "lang": "chi_tra",
            "psm": 6,
            "tessdata_prefix": str(TESSDATA_PREFIX),
            "pages_total": len(pages),
            "pages_with_text": 0,
            "pages_without_text": [],
            "errors": [],
            "warnings": [],
            "pages": [],
            "resumed": False,
        }

    env = dict(os.environ)
    env["TESSDATA_PREFIX"] = str(TESSDATA_PREFIX)

    for page in pages:
        page_id = page.stem
        txt_path = OUT_DIR / f"{page_id}.txt"
        if txt_path.exists():
            continue
        command = [str(TESSERACT_EXE), str(page), "stdout", "-l", "chi_tra", "--psm", "6"]
        proc = subprocess.run(command, capture_output=True, text=True, encoding="utf-8", errors="replace", env=env)
        if proc.returncode != 0:
            summary["errors"].append({"page_id": page_id, "returncode": proc.returncode, "stderr": proc.stderr})
            print(f"{page_id}: error", flush=True)
        else:
            txt_path.write_text(proc.stdout, encoding="utf-8")
            summary["pages"].append({"page_id": page_id, "text_length": len(proc.stdout), "returncode": proc.returncode})
            if proc.stdout.strip():
                summary["pages_with_text"] += 1
            else:
                summary["pages_without_text"].append(page_id)
            if proc.stderr.strip():
                summary["warnings"].append({"page_id": page_id, "stderr": proc.stderr})
            print(f"{page_id}: ok text_length={len(proc.stdout)}", flush=True)
        RUN_SUMMARY.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
