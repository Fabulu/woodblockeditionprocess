from __future__ import annotations

import argparse
import json
from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
WITNESSES = [
    {
        "witness_id": "YJG-W2",
        "pdf_path": ROOT
        / "provenance/song-of-enlightenment/witnesses/YJG-W2-ndl-1694-standalone/source/YJG-W2-ndl-1694-standalone.pdf",
        "image_dir": ROOT
        / "provenance/song-of-enlightenment/witnesses/YJG-W2-ndl-1694-standalone/images",
    },
    {
        "witness_id": "YJG-W4C",
        "pdf_path": ROOT
        / "provenance/song-of-enlightenment/witnesses/YJG-W4C-wzlib-433459/source/YJG-W4C-wzlib-433459.pdf",
        "image_dir": ROOT
        / "provenance/song-of-enlightenment/witnesses/YJG-W4C-wzlib-433459/images",
    },
    {
        "witness_id": "YJG-W4F",
        "pdf_path": ROOT
        / "provenance/song-of-enlightenment/witnesses/YJG-W4F-wzlib-433359/source/YJG-W4F-wzlib-433359.pdf",
        "image_dir": ROOT
        / "provenance/song-of-enlightenment/witnesses/YJG-W4F-wzlib-433359/images",
    },
    {
        "witness_id": "YJG-W4G",
        "pdf_path": ROOT
        / "provenance/song-of-enlightenment/witnesses/YJG-W4G-wzlib-433439/source/YJG-W4G-wzlib-433439.pdf",
        "image_dir": ROOT
        / "provenance/song-of-enlightenment/witnesses/YJG-W4G-wzlib-433439/images",
    },
    {
        "witness_id": "YJG-W8",
        "pdf_path": ROOT
        / "provenance/song-of-enlightenment/witnesses/YJG-W8-korcis-1474-samhwasa/source/YJG-W8-korcis-1474-samhwasa.pdf",
        "image_dir": ROOT
        / "provenance/song-of-enlightenment/witnesses/YJG-W8-korcis-1474-samhwasa/images",
    },
    {
        "witness_id": "YJG-W9",
        "pdf_path": ROOT
        / "provenance/song-of-enlightenment/witnesses/YJG-W9-korcis-1647-standalone/source/YJG-W9-korcis-1647-standalone.pdf",
        "image_dir": ROOT
        / "provenance/song-of-enlightenment/witnesses/YJG-W9-korcis-1647-standalone/images",
    },
    {
        "witness_id": "YJG-W21",
        "pdf_path": ROOT
        / "provenance/song-of-enlightenment/witnesses/YJG-W21-korcis-1576-seobongsa/source/YJG-W21-korcis-1576-seobongsa.pdf",
        "image_dir": ROOT
        / "provenance/song-of-enlightenment/witnesses/YJG-W21-korcis-1576-seobongsa/images",
    },
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Render the deferred Song first-tier PDF witnesses into local page JPGs."
    )
    parser.add_argument(
        "--dpi",
        type=int,
        default=300,
        help="Render DPI for the generated JPG pages (default: 300).",
    )
    parser.add_argument(
        "--witness",
        action="append",
        dest="witness_ids",
        help="Optional witness ID filter; may be repeated.",
    )
    return parser.parse_args()


def render_witness(pdf_path: Path, image_dir: Path, dpi: int) -> dict:
    image_dir.mkdir(parents=True, exist_ok=True)
    with fitz.open(pdf_path) as doc:
        page_count = doc.page_count
        if page_count <= 0:
            raise RuntimeError("PDF opened but exposed no renderable pages")

        written = 0
        skipped = 0
        for index in range(page_count):
            out_path = image_dir / f"page-{index + 1:04d}.jpg"
            if out_path.exists():
                skipped += 1
                continue
            pix = doc.load_page(index).get_pixmap(dpi=dpi, alpha=False)
            pix.save(out_path)
            written += 1

    return {
        "page_count": page_count,
        "written": written,
        "skipped": skipped,
        "image_dir": str(image_dir.relative_to(ROOT)).replace("\\", "/"),
    }


def main() -> int:
    args = parse_args()
    selected = set(args.witness_ids or [])
    queue = [
        witness
        for witness in WITNESSES
        if not selected or witness["witness_id"] in selected
    ]

    results: list[dict] = []
    failed = False
    for witness in queue:
        result = {"witness_id": witness["witness_id"]}
        try:
            result.update(
                render_witness(
                    pdf_path=witness["pdf_path"],
                    image_dir=witness["image_dir"],
                    dpi=args.dpi,
                )
            )
            result["status"] = "rendered"
        except Exception as exc:  # pragma: no cover - operational reporting
            failed = True
            result["status"] = "blocked"
            result["error"] = str(exc)
        results.append(result)

    print(json.dumps({"dpi": args.dpi, "results": results}, ensure_ascii=False, indent=2))
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
