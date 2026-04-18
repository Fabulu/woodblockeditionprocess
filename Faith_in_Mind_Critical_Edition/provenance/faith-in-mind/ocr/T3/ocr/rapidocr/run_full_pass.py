from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from rapidocr_onnxruntime import RapidOCR


PAGE_DIR = Path(r"C:\woodblocks\Faith_in_Mind_Sengcan_Kyoto_RB00016909\images")
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

    pages = sorted(PAGE_DIR.glob("RB00016909_*.jpg"))
    summary: dict[str, Any] = {
        "engine": "RapidOCR",
        "witness_id": "T3",
        "input_dir": str(PAGE_DIR),
        "pages_total": len(pages),
        "pages_with_text": 0,
        "pages_without_text": [],
        "errors": [],
        "pages": [],
    }

    for index, page in enumerate(pages, start=1):
        page_id = f"T3-p{index:03d}"
        json_path = OUT_DIR / f"{page_id}.json"
        txt_path = OUT_DIR / f"{page_id}.txt"
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
                json.dumps({"page_id": page_id, "source_image": page.name, "results": records, "timing": normalize(elapsed)}, ensure_ascii=False, indent=2),
                encoding="utf-8",
            )
            txt_path.write_text("\n".join(texts), encoding="utf-8")
            summary["pages"].append(
                {
                    "page_id": page_id,
                    "text_count": len(texts),
                    "timing": normalize(elapsed),
                }
            )
            if texts:
                summary["pages_with_text"] += 1
            else:
                summary["pages_without_text"].append(page_id)
            print(f"{page_id}: ok text_count={len(texts)}", flush=True)
        except Exception as exc:
            summary["errors"].append(
                {
                    "page_id": page_id,
                    "error_type": type(exc).__name__,
                    "error": str(exc),
                }
            )
            print(f"{page_id}: error {type(exc).__name__}", flush=True)

        RUN_SUMMARY.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
