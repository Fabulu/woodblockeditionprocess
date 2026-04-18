from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from rapidocr_onnxruntime import RapidOCR


PAGE_DIR = Path(r"C:\woodblocks\Faith_in_Mind_Critical_Edition\provenance\faith-in-mind\ocr\C1\page-images")
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
    engine = RapidOCR()

    pages = sorted(PAGE_DIR.glob("C1-p*.png"))
    if RUN_SUMMARY.exists():
        summary = json.loads(RUN_SUMMARY.read_text(encoding="utf-8"))
        summary["resumed"] = True
    else:
        summary = {
            "engine": "RapidOCR",
            "witness_id": "C1",
            "input_dir": str(PAGE_DIR),
            "pages_total": len(pages),
            "pages_with_text": 0,
            "pages_without_text": [],
            "errors": [],
            "pages": [],
            "resumed": False,
        }

    for page in pages:
        page_id = page.stem
        json_path = OUT_DIR / f"{page_id}.json"
        txt_path = OUT_DIR / f"{page_id}.txt"
        if json_path.exists() and txt_path.exists():
            continue
        try:
            result, elapsed = engine(str(page))
            records = []
            texts = []
            if result:
                for item in result:
                    if len(item) >= 3:
                        box, text, score = item[:3]
                    else:
                        box, text, score = None, "", None
                    texts.append(str(text))
                    records.append(
                        {
                            "box": normalize(box),
                            "text": str(text),
                            "score": normalize(score),
                        }
                    )
            json_path.write_text(
                json.dumps(
                    {"page_id": page_id, "source_image": page.name, "results": records, "timing": normalize(elapsed)},
                    ensure_ascii=False,
                    indent=2,
                ),
                encoding="utf-8",
            )
            txt_path.write_text("\n".join(texts), encoding="utf-8")
            summary["pages"].append({"page_id": page_id, "text_count": len(texts), "timing": normalize(elapsed)})
            if texts:
                summary["pages_with_text"] += 1
            else:
                summary["pages_without_text"].append(page_id)
            print(f"{page_id}: ok text_count={len(texts)}", flush=True)
        except Exception as exc:
            summary["errors"].append({"page_id": page_id, "error_type": type(exc).__name__, "error": str(exc)})
            print(f"{page_id}: error {type(exc).__name__}", flush=True)

        RUN_SUMMARY.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
