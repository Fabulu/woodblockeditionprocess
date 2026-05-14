from __future__ import annotations

import subprocess
import sys
import argparse
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
RUNNER = ROOT / "scripts" / "run_witness_ocr.py"
PY314 = Path(r"C:\Users\Fabian Trunz\AppData\Local\Programs\Python\Python314\python.exe")
PY312 = Path(r"C:\Users\Fabian Trunz\AppData\Local\Programs\Python\Python312\python.exe")

REMAINING_FIRST_TIER = [
    {
        "witness_id": "YJG-W2",
        "image_dir": ROOT / "provenance" / "song-of-enlightenment" / "witnesses" / "YJG-W2-ndl-1694-standalone" / "images",
    },
    {
        "witness_id": "YJG-W4C",
        "image_dir": ROOT / "provenance" / "song-of-enlightenment" / "witnesses" / "YJG-W4C-wzlib-433459" / "images",
    },
    {
        "witness_id": "YJG-W4F",
        "image_dir": ROOT / "provenance" / "song-of-enlightenment" / "witnesses" / "YJG-W4F-wzlib-433359" / "images",
    },
    {
        "witness_id": "YJG-W4G",
        "image_dir": ROOT / "provenance" / "song-of-enlightenment" / "witnesses" / "YJG-W4G-wzlib-433439" / "images",
    },
    {
        "witness_id": "YJG-W8",
        "image_dir": ROOT / "provenance" / "song-of-enlightenment" / "witnesses" / "YJG-W8-korcis-1474-samhwasa" / "images",
    },
    {
        "witness_id": "YJG-W9",
        "image_dir": ROOT / "provenance" / "song-of-enlightenment" / "witnesses" / "YJG-W9-korcis-1647-standalone" / "images",
    },
]

ENGINES = ["rapidocr", "paddleocr", "easyocr", "tesseract"]


def engine_python(engine: str) -> str:
    if engine == "paddleocr" and PY312.exists():
        return str(PY312)
    if engine in {"rapidocr", "easyocr", "tesseract"} and PY314.exists():
        return str(PY314)
    return sys.executable


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--witness", action="append", dest="witness_ids")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    selected = set(args.witness_ids or [])
    failures = []
    queue = [
        witness for witness in REMAINING_FIRST_TIER if not selected or witness["witness_id"] in selected
    ]
    for witness in queue:
        for engine in ENGINES:
            out_dir = (
                ROOT
                / "provenance"
                / "song-of-enlightenment"
                / "ocr"
                / witness["witness_id"]
                / "ocr"
                / engine
            )
            command = [
                engine_python(engine),
                str(RUNNER),
                "--witness-id",
                witness["witness_id"],
                "--image-dir",
                str(witness["image_dir"]),
                "--out-dir",
                str(out_dir),
                "--engine",
                engine,
                "--resume",
            ]
            proc = subprocess.run(command)
            if proc.returncode != 0:
                failures.append(
                    {
                        "witness_id": witness["witness_id"],
                        "engine": engine,
                        "returncode": proc.returncode,
                    }
                )
    if failures:
        print(failures)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
