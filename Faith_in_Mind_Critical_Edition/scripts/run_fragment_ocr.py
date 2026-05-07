from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(r"C:\woodblocks\Faith_in_Mind_Critical_Edition")
WORKBENCH = ROOT / "provenance" / "faith-in-mind" / "process" / "visual-workbench-holdouts"
OUT_ROOT = ROOT / "provenance" / "faith-in-mind" / "process" / "fragment-ocr-2026-05-07"

TARGETS = {
    "T1-p012.l02": [
        WORKBENCH / "T1-p012" / "T1-p012-l02-exact-rot90-mirror-hi.png",
        WORKBENCH / "T1-p012" / "T1-p012-l02-exact-rot90-mirror-bw.png",
        WORKBENCH / "T1-p012" / "T1-p012-l02-wide-rot90-mirror-hi.png",
        WORKBENCH / "T1-p012" / "T1-p012-l02-wide-rot90-mirror-bw.png",
    ],
    "T1-p029.l06": [
        WORKBENCH / "T1-p029" / "T1-p029-l06-exact-rot90-mirror-hi.png",
        WORKBENCH / "T1-p029" / "T1-p029-l06-exact-rot90-mirror-bw.png",
        WORKBENCH / "T1-p029" / "T1-p029-l06-wide-rot90-mirror-hi.png",
        WORKBENCH / "T1-p029" / "T1-p029-l06-wide-rot90-mirror-bw.png",
    ],
}


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def run_rapidocr(out_dir: Path) -> None:
    from rapidocr_onnxruntime import RapidOCR

    engine = RapidOCR()
    summary_lines: list[str] = []
    for locus, images in TARGETS.items():
        for image_path in images:
            result, _ = engine(str(image_path))
            payload = {
                "locus": locus,
                "image": str(image_path),
                "engine": "rapidocr",
                "results": result or [],
            }
            out_path = out_dir / f"{image_path.stem}.json"
            out_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
            texts = [row[1] for row in (result or [])]
            summary_lines.append(f"{image_path.name}: {' | '.join(texts) if texts else '<no text>'}")
    (out_dir / "summary.txt").write_text("\n".join(summary_lines) + "\n", encoding="utf-8")


def run_paddle(out_dir: Path) -> None:
    from paddleocr import PaddleOCR

    engine = PaddleOCR(use_textline_orientation=True, lang="ch")
    summary_lines: list[str] = []
    for locus, images in TARGETS.items():
        for image_path in images:
            result = engine.predict(str(image_path))
            payload = {
                "locus": locus,
                "image": str(image_path),
                "engine": "paddleocr",
                "results": result,
            }
            out_path = out_dir / f"{image_path.stem}.json"
            out_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, default=str), encoding="utf-8")
            texts: list[str] = []
            for block in result or []:
                if isinstance(block, dict):
                    rec_texts = block.get("rec_texts") or []
                    texts.extend(str(x) for x in rec_texts if x)
                else:
                    try:
                        rec_texts = getattr(block, "get", lambda _k, _d=None: [])("rec_texts", [])
                        texts.extend(str(x) for x in rec_texts if x)
                    except Exception:
                        pass
            summary_lines.append(f"{image_path.name}: {' | '.join(texts) if texts else '<no text>'}")
    (out_dir / "summary.txt").write_text("\n".join(summary_lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--engine", choices=["rapidocr", "paddle"], required=True)
    args = parser.parse_args()

    out_dir = OUT_ROOT / args.engine
    ensure_dir(out_dir)
    if args.engine == "rapidocr":
        run_rapidocr(out_dir)
    else:
        run_paddle(out_dir)


if __name__ == "__main__":
    main()
