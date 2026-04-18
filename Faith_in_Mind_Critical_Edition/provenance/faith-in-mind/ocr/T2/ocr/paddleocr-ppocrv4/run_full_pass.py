from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from paddleocr import PaddleOCR


BASE_DIR = Path(__file__).resolve().parent
PAGE_DIR = Path(r"C:\woodblocks\Faith_in_Mind_Critical_Edition\provenance\faith-in-mind\ocr\T2\ocr-input-120dpi")
OUT_DIR = BASE_DIR
RUN_SUMMARY = OUT_DIR / "run-summary-full.json"


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


def load_existing_summary() -> dict[str, Any]:
    if RUN_SUMMARY.exists():
        return json.loads(RUN_SUMMARY.read_text(encoding="utf-8"))
    return {
        "engine": "PaddleOCR",
        "ocr_version": "PP-OCRv4",
        "lang": "ch",
        "device": "cpu",
        "enable_hpi": False,
        "enable_mkldnn": False,
        "cpu_threads": 1,
        "python": "3.12",
        "input_basis_note": "used the logged 120 DPI JPEG OCR derivatives for T2 because the full-resolution rendered PNG pages were too large for stable PIL-based OCR loading on this workstation",
        "status": "running",
        "page_results": [],
    }


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    summary = load_existing_summary()
    seen = {entry["page"] for entry in summary.get("page_results", [])}

    ocr = PaddleOCR(
        lang="ch",
        ocr_version="PP-OCRv4",
        device="cpu",
        enable_hpi=False,
        enable_mkldnn=False,
        cpu_threads=1,
    )

    pages = sorted(PAGE_DIR.glob("T2-p*.jpg"))
    for page in pages:
        page_id = page.stem
        json_path = OUT_DIR / f"{page_id}.json"
        txt_path = OUT_DIR / f"{page_id}.txt"

        if page_id in seen and json_path.exists() and txt_path.exists():
            continue

        page_result: dict[str, Any] = {"page": page_id, "source_image": page.name}
        try:
            result = list(ocr.predict(str(page)))
            item = result[0] if result else None
            obj = normalize(getattr(item, "json", item))
            if callable(obj):
                obj = normalize(obj())
            if obj is None:
                obj = {"repr": repr(item)}

            if isinstance(obj, dict):
                texts = obj.get("rec_texts") or obj.get("rec_text") or []
                if not isinstance(texts, list):
                    texts = [str(texts)]
            else:
                texts = [repr(item)]

            json_path.write_text(
                json.dumps(obj, ensure_ascii=False, indent=2),
                encoding="utf-8",
            )
            txt_path.write_text(
                "\n".join(str(t) for t in texts),
                encoding="utf-8",
            )
            page_result["status"] = "success"
            page_result["json_path"] = json_path.name
            page_result["txt_path"] = txt_path.name
            page_result["text_count"] = len(texts)
        except Exception as exc:
            page_result["status"] = "error"
            page_result["error_type"] = type(exc).__name__
            page_result["error"] = str(exc)

        summary["page_results"] = [
            entry for entry in summary.get("page_results", []) if entry["page"] != page_id
        ]
        summary["page_results"].append(page_result)
        summary["page_results"].sort(key=lambda entry: entry["page"])
        RUN_SUMMARY.write_text(
            json.dumps(summary, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        print(f"{page_id}: {page_result['status']}", flush=True)

    total = len(pages)
    success_count = sum(1 for entry in summary["page_results"] if entry["status"] == "success")
    error_count = sum(1 for entry in summary["page_results"] if entry["status"] == "error")
    summary["total_pages"] = total
    summary["success_pages"] = success_count
    summary["error_pages"] = error_count
    summary["status"] = "completed"
    RUN_SUMMARY.write_text(
        json.dumps(summary, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"done success={success_count} error={error_count}", flush=True)


if __name__ == "__main__":
    main()
