from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--paddle-dir", type=Path, required=True)
    return parser.parse_args()


def center_of_box(box: Any) -> tuple[float, float]:
    if not isinstance(box, list) or not box:
        return (0.0, 0.0)
    xs: list[float] = []
    ys: list[float] = []
    for point in box:
        if isinstance(point, (list, tuple)) and len(point) >= 2:
            try:
                xs.append(float(point[0]))
                ys.append(float(point[1]))
            except Exception:
                continue
    if not xs or not ys:
        return (0.0, 0.0)
    return (sum(xs) / len(xs), sum(ys) / len(ys))


def load_entries(payload: Any) -> list[tuple[str, tuple[float, float]]]:
    if not isinstance(payload, dict):
        return []
    source = payload
    if isinstance(payload.get("res"), dict):
        source = payload["res"]

    texts = source.get("rec_texts") or []
    boxes = source.get("rec_boxes") or source.get("dt_polys") or []
    if not isinstance(texts, list):
        texts = [texts]
    if not isinstance(boxes, list):
        boxes = []
    entries: list[tuple[str, tuple[float, float]]] = []
    for index, text in enumerate(texts):
        box = boxes[index] if index < len(boxes) else []
        entries.append((str(text), center_of_box(box)))
    return entries


def main() -> None:
    args = parse_args()
    paddle_dir = args.paddle_dir.resolve()
    extracted_dir = paddle_dir / "extracted-text"
    ordered_dir = paddle_dir / "column-ordered-text"
    extracted_dir.mkdir(parents=True, exist_ok=True)
    ordered_dir.mkdir(parents=True, exist_ok=True)

    extracted_readme = extracted_dir / "README.md"
    if not extracted_readme.exists():
        extracted_readme.write_text(
            "# Extracted Paddle Text\n\n"
            "These files are derived from the saved paddleocr JSON outputs by reading `rec_texts`.\n"
            "The raw saved Paddle `.txt` companions are not treated as the stable text surface for this pass.\n",
            encoding="utf-8",
        )

    ordered_readme = ordered_dir / "README.md"
    if not ordered_readme.exists():
        ordered_readme.write_text(
            "# Paddle Column-Ordered Support Text\n\n"
            "These files are derived from saved paddleocr JSON outputs for a high-resolution T1 support pass.\n\n"
            "They are support text only, built from OCR geometry:\n\n"
            "- detections are sorted by x-center descending\n"
            "- ties are sorted by y-center ascending\n",
            encoding="utf-8",
        )

    summary: dict[str, Any] = {"files": []}

    for json_path in sorted(paddle_dir.glob("T1-p*.json")):
        payload = json.loads(json_path.read_text(encoding="utf-8"))
        entries = load_entries(payload)
        extracted_lines = [text for text, _ in entries]
        ordered_lines = [text for text, _ in sorted(entries, key=lambda item: (-item[1][0], item[1][1]))]

        extracted_path = extracted_dir / f"{json_path.stem}.txt"
        ordered_path = ordered_dir / f"{json_path.stem}.txt"
        extracted_path.write_text("\n".join(extracted_lines), encoding="utf-8")
        ordered_path.write_text("\n".join(ordered_lines), encoding="utf-8")
        summary["files"].append(
            {
                "page": json_path.stem,
                "extracted_count": len(extracted_lines),
                "ordered_count": len(ordered_lines),
            }
        )
        print(f"{json_path.stem}: derived", flush=True)

    (ordered_dir / "run-summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
