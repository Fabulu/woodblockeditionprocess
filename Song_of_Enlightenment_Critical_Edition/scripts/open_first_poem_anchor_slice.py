from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
PROCESS_DIR = ROOT / "provenance" / "song-of-enlightenment" / "process"


@dataclass(frozen=True)
class PageTemplate:
    start: int
    end: int
    bbox: tuple[float, float, float, float]
    line_count: int
    page_note: str
    line_note: str


@dataclass(frozen=True)
class WitnessTemplate:
    witness_id: str
    source_asset_dir: str
    source_download_url: str
    pages: tuple[PageTemplate, ...]


WITNESSES: tuple[WitnessTemplate, ...] = (
    WitnessTemplate(
        witness_id="YJG-W16",
        source_asset_dir="provenance/song-of-enlightenment/witnesses/YJG-W16-toyo-exact-standalone/images",
        source_download_url="https://kokusho.nijl.ac.jp/biblio/300094276/manifest",
        pages=(
            PageTemplate(
                start=4,
                end=4,
                bbox=(0.53, 0.55, 0.31, 0.42),
                line_count=4,
                page_note=(
                    "Opening mixed page. The indexed poem locus is the right-hand framed block only; "
                    "top prose and the blank facing area remain outside the poem-band anchor."
                ),
                line_note=(
                    "Opening-page provisional line column inside the right-hand framed poem block. "
                    "Exact line edges remain subject to the first comparison pass."
                ),
            ),
            PageTemplate(
                start=5,
                end=53,
                bbox=(0.08, 0.22, 0.36, 0.65),
                line_count=5,
                page_note=(
                    "Interior poem page. The indexed locus is the main left-hand framed block; "
                    "adjacent facing-page capture remains out of scope for this first register opening."
                ),
                line_note=(
                    "Interior-page provisional line column inside the main framed poem block. "
                    "This first opening records stable right-to-left column loci before comparison-level refinement."
                ),
            ),
            PageTemplate(
                start=54,
                end=54,
                bbox=(0.10, 0.30, 0.31, 0.57),
                line_count=4,
                page_note=(
                    "Closing poem page. The poem remains in the main left-hand frame; no separate afterword is opened here."
                ),
                line_note=(
                    "Closing-page provisional line column inside the confirmed final poem frame. "
                    "The first comparison pass may tighten the final line edges."
                ),
            ),
        ),
    ),
    WitnessTemplate(
        witness_id="YJG-W17",
        source_asset_dir="provenance/song-of-enlightenment/witnesses/YJG-W17-berkeley-exact-standalone/images",
        source_download_url="https://kokusho.nijl.ac.jp/biblio/100175027/manifest",
        pages=(
            PageTemplate(
                start=4,
                end=4,
                bbox=(0.03, 0.47, 0.40, 0.49),
                line_count=3,
                page_note=(
                    "Opening mixed page. The indexed poem locus is the main left-hand framed block only; "
                    "library marks and title-side matter outside the frame remain excluded."
                ),
                line_note=(
                    "Opening-page provisional line column inside the framed poem block. "
                    "Title-to-body delimitation remains an early comparison watchpoint."
                ),
            ),
            PageTemplate(
                start=5,
                end=56,
                bbox=(0.11, 0.17, 0.42, 0.76),
                line_count=5,
                page_note=(
                    "Interior poem page. The indexed locus is the main left-hand framed block; "
                    "the adjacent facing-page capture is not opened as part of this first slice."
                ),
                line_note=(
                    "Interior-page provisional line column inside the main framed poem block. "
                    "These rows establish the first stable page-plus-line register without claiming character-tier certainty."
                ),
            ),
            PageTemplate(
                start=57,
                end=57,
                bbox=(0.12, 0.28, 0.33, 0.60),
                line_count=4,
                page_note=(
                    "Closing page still poem-bearing to the end of the captured witness tranche."
                ),
                line_note=(
                    "Closing-page provisional line column inside the surviving poem frame. "
                    "Final compressed closing lines remain open to later tightening."
                ),
            ),
        ),
    ),
    WitnessTemplate(
        witness_id="YJG-W22",
        source_asset_dir="provenance/song-of-enlightenment/witnesses/YJG-W22-nijl-1641-standalone/images",
        source_download_url="https://kokusho.nijl.ac.jp/biblio/200009070/manifest",
        pages=(
            PageTemplate(
                start=4,
                end=4,
                bbox=(0.57, 0.37, 0.29, 0.56),
                line_count=4,
                page_note=(
                    "Opening mixed page. The indexed poem locus is the right-hand framed block only; "
                    "outer title-side matter remains excluded."
                ),
                line_note=(
                    "Opening-page provisional line column inside the right-hand framed poem block. "
                    "Opening title/body transition remains on the early character-tier watchlist."
                ),
            ),
            PageTemplate(
                start=5,
                end=62,
                bbox=(0.14, 0.28, 0.33, 0.60),
                line_count=4,
                page_note=(
                    "Interior poem page. The indexed locus is the main left-hand framed block; "
                    "adjacent facing-page capture remains outside the current anchor opening."
                ),
                line_note=(
                    "Interior-page provisional line column inside the main framed poem block. "
                    "This is the first stable line map for the NIJL tranche, not a final comparison-resolved geometry."
                ),
            ),
            PageTemplate(
                start=63,
                end=63,
                bbox=(0.14, 0.24, 0.33, 0.63),
                line_count=4,
                page_note=(
                    "Closing mixed page. The poem remains inside the main left-hand frame only; "
                    "upper prose and the adjacent afterword-side block remain excluded."
                ),
                line_note=(
                    "Closing-page provisional line column inside the main poem frame. "
                    "This is the clearest mixed boundary locus in tranche 1 and remains open to later graph-level tightening if needed."
                ),
            ),
        ),
    ),
)


def locus_bbox_for_line(bbox: tuple[float, float, float, float], line_index: int, line_count: int) -> list[float]:
    x, y, width, height = bbox
    column_width = width / line_count
    x0 = x + ((line_count - line_index - 1) * column_width)
    return [round(x0, 6), round(y, 6), round(column_width, 6), round(height, 6)]


def page_id_for(witness_id: str, page_number: int) -> str:
    return f"{witness_id}-p{page_number:04d}"


def emit_anchor_rows() -> list[dict]:
    rows: list[dict] = []
    for witness in WITNESSES:
        for template in witness.pages:
            for page_number in range(template.start, template.end + 1):
                page_id = page_id_for(witness.witness_id, page_number)
                source_asset_path = f"{witness.source_asset_dir}/page-{page_number:04d}.jpg"
                band_locus_id = f"{page_id}.poem-band"
                rows.append(
                    {
                        "anchor_id": f"{band_locus_id}@{witness.witness_id}",
                        "witness_id": witness.witness_id,
                        "page_id": page_id,
                        "locus_id": band_locus_id,
                        "source_asset_path": source_asset_path,
                        "source_download_url": witness.source_download_url,
                        "source_kind": "page_image",
                        "page_number": page_number,
                        "page_bbox": [0.0, 0.0, 1.0, 1.0],
                        "locus_bbox": list(template.bbox),
                        "polygon": None,
                        "crop_asset_path": None,
                        "ocr_region_ref": None,
                        "evidence_tier": "page",
                        "char_coverage": "not_applicable",
                        "char_boxes": [],
                        "notes": template.page_note,
                    }
                )
                for line_index in range(template.line_count):
                    locus_id = f"{page_id}.l{line_index + 1:02d}"
                    rows.append(
                        {
                            "anchor_id": f"{locus_id}@{witness.witness_id}",
                            "witness_id": witness.witness_id,
                            "page_id": page_id,
                            "locus_id": locus_id,
                            "source_asset_path": source_asset_path,
                            "source_download_url": witness.source_download_url,
                            "source_kind": "page_image",
                            "page_number": page_number,
                            "page_bbox": [0.0, 0.0, 1.0, 1.0],
                            "locus_bbox": locus_bbox_for_line(template.bbox, line_index, template.line_count),
                            "polygon": None,
                            "crop_asset_path": None,
                            "ocr_region_ref": None,
                            "evidence_tier": "line",
                            "char_coverage": "not_applicable",
                            "char_boxes": [],
                            "notes": template.line_note,
                        }
                    )
    return rows


def write_anchor_register(rows: list[dict]) -> None:
    output = PROCESS_DIR / "anchor-base-register.jsonl"
    with output.open("w", encoding="utf-8", newline="\n") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False))
            handle.write("\n")


def write_line_map(rows: list[dict]) -> None:
    output = PROCESS_DIR / "poem-line-map.md"
    page_rows = [row for row in rows if row["locus_id"].endswith(".poem-band")]
    line_rows = [row for row in rows if ".l" in row["locus_id"]]

    lines: list[str] = [
        "# First Poem Line Map",
        "",
        "Date: `2026-05-11`",
        "Status: first stable page-plus-line opening from the confirmed poem-bearing spans",
        "",
        "## Scope",
        "",
        "- Witnesses opened in this slice: `YJG-W16`, `YJG-W17`, `YJG-W22`",
        "- Output surface opened here: `provenance/song-of-enlightenment/process/anchor-base-register.jsonl`",
        "- Geometry posture: provisional page-band plus line-column anchors only; no character boxes were fabricated",
        "",
        "## Method",
        "",
        "- The confirmed poem-bearing spans from `anchor-planning.md` were kept fixed.",
        "- The first register opening uses the indexed main framed poem block only, not the adjacent facing-page capture visible in some witness photos.",
        "- Page-tier coverage is recorded via one `.poem-band` row per page.",
        "- Line-tier coverage is recorded via right-to-left provisional column loci inside that page's confirmed main poem block.",
        "- Mixed opening or closing pages stay explicitly provisional in notes rather than being promoted to false final segmentation.",
        "",
        "## Witness Map",
        "",
    ]

    for witness in WITNESSES:
        witness_page_rows = [row for row in page_rows if row["witness_id"] == witness.witness_id]
        witness_line_rows = [row for row in line_rows if row["witness_id"] == witness.witness_id]
        lines.extend(
            [
                f"### `{witness.witness_id}`",
                "",
                f"- Page-tier rows opened: `{len(witness_page_rows)}`",
                f"- Line-tier rows opened: `{len(witness_line_rows)}`",
                f"- Source asset directory: `{witness.source_asset_dir}`",
                "",
            ]
        )
        for template in witness.pages:
            page_range = f"`page-{template.start:04d}`" if template.start == template.end else f"`page-{template.start:04d}` through `page-{template.end:04d}`"
            lines.extend(
                [
                    f"- {page_range}: `{template.line_count}` provisional line loci per indexed page block",
                    f"  - bbox: `{list(template.bbox)}`",
                    f"  - note: {template.page_note}",
                ]
            )
        lines.append("")

    lines.extend(
        [
            "## Row Totals",
            "",
            f"- Page-tier rows: `{len(page_rows)}`",
            f"- Line-tier rows: `{len(line_rows)}`",
            f"- Total rows opened: `{len(rows)}`",
            "",
            "## Next Slice Consequence",
            "",
            "- The next bounded slice should begin real exact-witness comparison and transcription against these opened loci, starting with the mixed opening pages and the `YJG-W22` closing boundary page `page-0063`.",
        ]
    )

    output.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    rows = emit_anchor_rows()
    write_anchor_register(rows)
    write_line_map(rows)
    print(f"opened {len(rows)} anchor-base rows")


if __name__ == "__main__":
    main()
