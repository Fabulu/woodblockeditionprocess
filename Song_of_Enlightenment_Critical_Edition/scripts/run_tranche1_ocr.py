from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
RUNNER = ROOT / "scripts" / "run_witness_ocr.py"
PY314 = Path(r"C:\Users\Fabian Trunz\AppData\Local\Programs\Python\Python314\python.exe")
PY312 = Path(r"C:\Users\Fabian Trunz\AppData\Local\Programs\Python\Python312\python.exe")

TRANCHE_1 = [
    {
        "witness_id": "YJG-W16",
        "image_dir": ROOT / "provenance" / "song-of-enlightenment" / "witnesses" / "YJG-W16-toyo-exact-standalone" / "images",
    },
    {
        "witness_id": "YJG-W17",
        "image_dir": ROOT / "provenance" / "song-of-enlightenment" / "witnesses" / "YJG-W17-berkeley-exact-standalone" / "images",
    },
    {
        "witness_id": "YJG-W22",
        "image_dir": ROOT / "provenance" / "song-of-enlightenment" / "witnesses" / "YJG-W22-nijl-1641-standalone" / "images",
    },
]

ENGINES = ["rapidocr", "paddleocr", "easyocr", "tesseract"]


def engine_python(engine: str) -> str:
    if engine == "paddleocr" and PY312.exists():
        return str(PY312)
    if engine in {"rapidocr", "easyocr", "tesseract"} and PY314.exists():
        return str(PY314)
    return sys.executable


def main() -> int:
    failures = []
    for witness in TRANCHE_1:
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
                failures.append({"witness_id": witness["witness_id"], "engine": engine, "returncode": proc.returncode})
    if failures:
        print(failures)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
