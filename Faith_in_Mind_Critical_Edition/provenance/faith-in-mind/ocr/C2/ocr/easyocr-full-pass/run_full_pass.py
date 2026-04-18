from __future__ import annotations

import json
import time
from pathlib import Path
from typing import Any

import easyocr


PAGE_DIR = Path(r"C:\woodblocks\Faith_in_Mind_Critical_Edition\provenance\faith-in-mind\ocr\C2\page-images")
OUT_DIR = Path(__file__).resolve().parent
RUN_SUMMARY = OUT_DIR / "run-summary.json"


def normalize(obj: Any) -> Any:
    if isinstance(obj, (str, int, float, bool)) or obj is None:
        return obj
    if hasattr(obj, "item"):
        try:
            return obj.item()
        except Exception:
            pass
    if isinstance(obj, (list, tuple)):
        return [normalize(x) for x in obj]
    if isinstance(obj, dict):
        return {str(k): normalize(v) for k, v in obj.items()}
    return str(obj)


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    started = time.time()
    reader = easyocr.Reader(["ch_tra", "en"], gpu=False)
    pages = sorted(PAGE_DIR.glob("C2-p*.png"))
    if RUN_SUMMARY.exists():
        summary = json.loads(RUN_SUMMARY.read_text(encoding="utf-8"))
        summary["resumed"] = True
    else:
        summary = {
            "engine": "easyocr",
            "scope": "full-pass",
            "languages": ["ch_tra", "en"],
            "gpu": False,
            "input_dir": str(PAGE_DIR),
            "resumed": False,
            "total_pages": len(pages),
            "pages_with_text": 0,
            "no_text_pages": [],
            "error_count": 0,
            "errors": [],
            "output_dir": str(OUT_DIR),
            "elapsed_seconds": 0,
        }

    for page in pages:
        page_id = page.stem
        json_path = OUT_DIR / f"{page_id}.json"
        txt_path = OUT_DIR / f"{page_id}.txt"
        if json_path.exists() and txt_path.exists():
            continue
        try:
            result = reader.readtext(str(page), detail=1)
            normalized = []
            texts = []
            for item in result:
                if len(item) >= 3:
                    box, text, score = item[:3]
                else:
                    box, text, score = None, "", None
                normalized.append({"box": normalize(box), "text": str(text), "score": normalize(score)})
                texts.append(str(text))
            json_path.write_text(
                json.dumps({"page_id": page_id, "source_image": page.name, "results": normalized}, ensure_ascii=False, indent=2),
                encoding="utf-8",
            )
            txt_path.write_text("\n".join(texts), encoding="utf-8")
            if texts:
                summary["pages_with_text"] += 1
            else:
                summary["no_text_pages"].append(page_id)
            print(f"{page_id}: ok text_count={len(texts)}", flush=True)
        except Exception as exc:
            summary["error_count"] += 1
            summary["errors"].append({"page_id": page_id, "error_type": type(exc).__name__, "error": str(exc)})
            print(f"{page_id}: error {type(exc).__name__}", flush=True)
        summary["elapsed_seconds"] = round(time.time() - started, 3)
        RUN_SUMMARY.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
