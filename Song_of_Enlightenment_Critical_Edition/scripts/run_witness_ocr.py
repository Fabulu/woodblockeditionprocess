from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
TESSERACT_EXE = Path(r"C:\Program Files\Tesseract-OCR\tesseract.exe")
TESSDATA_CANDIDATES = [
    ROOT.parent / "Faith_in_Mind_Critical_Edition" / "provenance" / "faith-in-mind" / "ocr" / "T1" / "tessdata",
    ROOT.parent / "Transcriptions" / "Wumenguan_1632_NDL_Commons" / "tessdata",
    ROOT.parent / "Transcriptions" / "Wumen_Huikai_NDL_Commons" / "tessdata",
]


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


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("--witness-id", required=True)
    parser.add_argument("--image-dir", required=True)
    parser.add_argument("--out-dir", required=True)
    parser.add_argument("--engine", required=True, choices=["rapidocr", "paddleocr", "easyocr", "tesseract"])
    parser.add_argument("--glob", default="page-*.jpg")
    parser.add_argument("--lang", default="ch")
    parser.add_argument("--resume", action="store_true")
    return parser


def load_summary(path: Path, witness_id: str, image_dir: Path, engine: str, lang: str) -> dict[str, Any]:
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    return {
        "engine": engine,
        "witness_id": witness_id,
        "input_dir": str(image_dir),
        "lang": lang,
        "status": "running",
        "started_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "pages_total": 0,
        "pages_with_text": 0,
        "pages_without_text": [],
        "errors": [],
        "pages": [],
    }


def write_summary(path: Path, summary: dict[str, Any]) -> None:
    path.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")


def extract_paddle_texts(obj: Any) -> list[str]:
    if isinstance(obj, dict):
        texts = (
            obj.get("rec_texts")
            or obj.get("rec_text")
            or obj.get("res", {}).get("rec_texts")
            or obj.get("res", {}).get("rec_text")
            or []
        )
        if isinstance(texts, list):
            return [str(t) for t in texts]
        if texts:
            return [str(texts)]
        return []
    return []


def run_rapidocr(engine: Any, page: Path) -> tuple[dict[str, Any], list[str]]:
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
            records.append({"box": normalize(box), "text": str(text), "score": normalize(score)})
    payload = {"page_id": page.stem, "source_image": page.name, "results": records, "timing": normalize(elapsed)}
    return payload, texts


def run_paddleocr(engine: Any, page: Path) -> tuple[dict[str, Any], list[str]]:
    result = list(engine.predict(str(page)))
    item = result[0] if result else None
    obj = normalize(getattr(item, "json", item))
    if callable(obj):
        obj = normalize(obj())
    if obj is None:
        obj = {"repr": repr(item)}
    texts = extract_paddle_texts(obj)
    return obj, texts


def run_easyocr(reader: Any, page: Path) -> tuple[dict[str, Any], list[str]]:
    result = reader.readtext(str(page), detail=1)
    records = []
    texts = []
    for item in result:
        if len(item) >= 3:
            box, text, score = item[:3]
        else:
            box, text, score = None, "", None
        records.append({"box": normalize(box), "text": str(text), "score": normalize(score)})
        texts.append(str(text))
    payload = {"page_id": page.stem, "source_image": page.name, "results": records}
    return payload, texts


def run_tesseract(page: Path) -> tuple[dict[str, Any], list[str]]:
    tessdata_prefix = next((path for path in TESSDATA_CANDIDATES if (path / "chi_tra.traineddata").exists()), None)
    if tessdata_prefix is None:
        raise RuntimeError("No chi_tra.traineddata found in known tessdata locations.")
    command = [str(TESSERACT_EXE), str(page), "stdout", "-l", "chi_tra", "--psm", "6"]
    env = dict(os.environ)
    env["TESSDATA_PREFIX"] = str(tessdata_prefix)
    proc = subprocess.run(command, capture_output=True, text=True, encoding="utf-8", errors="replace", env=env)
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or f"tesseract exited {proc.returncode}")
    text = proc.stdout
    payload = {
        "page_id": page.stem,
        "source_image": page.name,
        "stdout_length": len(text),
        "stderr": proc.stderr,
        "tessdata_prefix": str(tessdata_prefix),
    }
    return payload, [line for line in text.splitlines() if line.strip()]


def main() -> int:
    args = build_parser().parse_args()
    image_dir = Path(args.image_dir)
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    summary_path = out_dir / "run-summary.json"

    pages = sorted(image_dir.glob(args.glob))
    summary = load_summary(summary_path, args.witness_id, image_dir, args.engine, args.lang)
    summary["pages_total"] = len(pages)
    summary["image_glob"] = args.glob
    summary["root"] = str(ROOT)
    if args.engine == "paddleocr":
        summary["return_word_box"] = True
        summary["env"] = {"PADDLE_PDX_DISABLE_MODEL_SOURCE_CHECK": "True"}

    engine_obj: Any = None
    if args.engine == "rapidocr":
        from rapidocr_onnxruntime import RapidOCR

        engine_obj = RapidOCR()
    elif args.engine == "paddleocr":
        os.environ.setdefault("PADDLE_PDX_DISABLE_MODEL_SOURCE_CHECK", "True")
        from paddleocr import PaddleOCR

        engine_obj = PaddleOCR(
            lang=args.lang,
            ocr_version="PP-OCRv4",
            device="cpu",
            enable_hpi=False,
            enable_mkldnn=False,
            cpu_threads=1,
            return_word_box=True,
        )
    elif args.engine == "easyocr":
        import easyocr

        engine_obj = easyocr.Reader(["ch_tra", "en"], gpu=False)

    existing = {entry["page_id"] for entry in summary.get("pages", [])}
    started = time.time()

    for page in pages:
        page_id = page.stem
        json_path = out_dir / f"{page_id}.json"
        txt_path = out_dir / f"{page_id}.txt"
        if args.resume and page_id in existing and json_path.exists() and txt_path.exists():
            continue

        result_row: dict[str, Any] = {"page_id": page_id, "source_image": page.name}
        try:
            if args.engine == "rapidocr":
                payload, texts = run_rapidocr(engine_obj, page)
            elif args.engine == "paddleocr":
                payload, texts = run_paddleocr(engine_obj, page)
            elif args.engine == "easyocr":
                payload, texts = run_easyocr(engine_obj, page)
            else:
                payload, texts = run_tesseract(page)

            json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
            txt_path.write_text("\n".join(texts), encoding="utf-8")
            result_row["status"] = "success"
            result_row["json_path"] = json_path.name
            result_row["txt_path"] = txt_path.name
            result_row["text_count"] = len(texts)
        except Exception as exc:
            result_row["status"] = "error"
            result_row["error_type"] = type(exc).__name__
            result_row["error"] = str(exc)
            summary["errors"] = [entry for entry in summary.get("errors", []) if entry.get("page_id") != page_id]
            summary["errors"].append(
                {"page_id": page_id, "error_type": type(exc).__name__, "error": str(exc)}
            )

        summary["pages"] = [entry for entry in summary.get("pages", []) if entry.get("page_id") != page_id]
        summary["pages"].append(result_row)
        summary["pages"].sort(key=lambda entry: entry["page_id"])
        summary["pages_with_text"] = sum(
            1 for entry in summary["pages"] if entry.get("status") == "success" and entry.get("text_count", 0) > 0
        )
        summary["pages_without_text"] = [
            entry["page_id"]
            for entry in summary["pages"]
            if entry.get("status") == "success" and entry.get("text_count", 0) == 0
        ]
        summary["elapsed_seconds"] = round(time.time() - started, 3)
        write_summary(summary_path, summary)
        print(f"{args.witness_id} {args.engine} {page_id}: {result_row['status']}", flush=True)

    summary["status"] = "completed"
    summary["elapsed_seconds"] = round(time.time() - started, 3)
    write_summary(summary_path, summary)
    return 0


if __name__ == "__main__":
    sys.exit(main())
