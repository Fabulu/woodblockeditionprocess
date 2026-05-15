from __future__ import annotations

from pathlib import Path
import html


ROOT = Path(__file__).resolve().parent.parent
PROCESS_DIR = ROOT / "provenance" / "song-of-enlightenment" / "process"
EDITION_DIR = ROOT / "provenance" / "song-of-enlightenment" / "edition"
XML_DIR = ROOT / "xml-open" / "ce" / "song-of-enlightenment"


def parse_translation_rows() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    path = PROCESS_DIR / "translation-diff-log.md"
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("| `"):
            continue
        parts = [part.strip() for part in line.split("|")]
        if len(parts) < 8:
            continue
        locus = parts[2].replace("`", "")
        zh = parts[4].replace("`", "")
        en = parts[6].replace("`", "")
        if zh and zh != "not yet transcribed":
            rows.append({"locus": locus, "zh": zh, "en": en})
    return rows


def build_working_text(rows: list[dict[str, str]]) -> None:
    lines = [
        "# Working Critical Text: Song of Enlightenment",
        "",
        "Date: `2026-05-15`",
        "Status: `active`",
        "",
        "This is the current stabilized poem-first reading text extracted from the synchronized Chinese and English frontier in `translation-diff-log.md`. It reflects the accepted grouped poem loci carried into the edition package, not a fresh full variant collation.",
        "",
    ]
    for index, row in enumerate(rows, start=1):
        lines.append(f"{index}. `{row['zh']}`  ")
        lines.append(f"   English: {row['en']}  ")
        lines.append(f"   Locus: `{row['locus']}`")
    (EDITION_DIR / "working-critical-text.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def build_tei(rows: list[dict[str, str]]) -> None:
    witness_lines = [
        ('YJG-W22', 'Selected copy-text and earliest complete independent exact witness held as a full local image tranche.'),
        ('YJG-W16', 'Primary clean shared exact comparison witness for much of the stabilized interior.'),
        ('YJG-W17', 'Primary clean shared exact comparison witness with strong closing control.'),
        ('YJG-W2', 'Commentary-bearing first-tier exact control with stable opening and closing span.'),
        ('YJG-W4C', 'Short-tranche exact control with stable opening and closing span.'),
        ('YJG-W4F', 'Commentary-bearing first-tier exact control with stable opening and closing span.'),
        ('YJG-W4G', 'First-tier exact closure and witness-class control.'),
        ('YJG-W8', 'Korean exact closure and witness-class control.'),
        ('YJG-W9', 'Korean exact closure and witness-class control.'),
    ]
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<?xml-model href="../../../../schemas/openzentexts-tei.rng" type="application/xml" schematypens="http://relaxng.org/ns/structure/1.0"?>',
        '<TEI xmlns="http://www.tei-c.org/ns/1.0" xml:lang="zh-Hant">',
        "  <teiHeader>",
        "    <fileDesc>",
        "      <titleStmt>",
        "        <title>Song of Enlightenment</title>",
        "        <title xml:lang=\"zh-Hant\">永嘉證道歌</title>",
        "        <author>Traditionally attributed to Yongjia Xuanjue</author>",
        "      </titleStmt>",
        "      <publicationStmt>",
        "        <publisher>Song of Enlightenment critical edition package</publisher>",
        "        <date when=\"2026-05-15\">2026-05-15</date>",
        "        <availability status=\"unknown\">",
        "          <p>Publication-form research release candidate. No separate public license statement is supplied in this TEI file.</p>",
        "        </availability>",
        "        <p>Poem-first critical edition assembled from the stabilized Song of Enlightenment witness package and synchronized translation frontier on 2026-05-15.</p>",
        "      </publicationStmt>",
        "      <sourceDesc>",
        "        <listWit>",
    ]
    for wit_id, note in witness_lines:
        lines.append(f'          <witness xml:id="{wit_id}">{html.escape(note)}</witness>')
    lines.extend(
        [
            "        </listWit>",
            "      </sourceDesc>",
            "    </fileDesc>",
            "    <encodingDesc>",
            "      <projectDesc>",
            "        <p>This TEI publishes the poem only. Commentary-bearing, derivative anthology, and reception witnesses remain preserved as secondary controls and do not drive the main poem body.</p>",
            "      </projectDesc>",
            "      <editorialDecl>",
            "        <p>The edition uses a poem-first best-witness model. YJG-W22 is the selected copy-text at witness level, but clean shared exact agreement in YJG-W16 and YJG-W17 controls much of the stabilized interior, while additional first-tier exact witnesses reinforce boundary and witness-class judgments.</p>",
            "      </editorialDecl>",
            "    </encodingDesc>",
            "    <revisionDesc>",
            "      <change when=\"2026-05-15\">First populated poem-first TEI edition created from the stabilized translation-synced reading text and selective apparatus layer.</change>",
            "    </revisionDesc>",
            "  </teiHeader>",
            "  <text>",
            "    <front>",
            "      <div type=\"editorial_note\" xml:id=\"ed-note\">",
            "        <head>Editorial Note</head>",
            "        <p>The present edition is poem-first. The package preserves broad witness acquisition, OCR, and secondary control work, but the edited text below contains only the stabilized poem loci carried into the current critical reading text.</p>",
            "      </div>",
            "      <div type=\"editorial_summary\" xml:id=\"ed-summary\">",
            "        <head>Summary of Method</head>",
            "        <p>The reading text follows the selected YJG-W22 witness at witness level, but it does not mechanically follow every local page where YJG-W16 and YJG-W17 preserve a cleaner shared exact interior basis. Additional first-tier exact witnesses now reinforce opening, closing, and witness-class judgments without forcing further adopted text change.</p>",
            "      </div>",
            "    </front>",
            "    <body>",
            "      <div type=\"poem\" xml:id=\"song-of-enlightenment\">",
            "        <head>永嘉證道歌</head>",
            "        <lg type=\"poem\">",
        ]
    )
    for index, row in enumerate(rows, start=1):
        lines.append(
            f'          <l n="{index}" corresp="urn:locus:{row["locus"]}">{html.escape(row["zh"])}</l>'
        )
    lines.extend(
        [
            "        </lg>",
            "      </div>",
            "    </body>",
            "    <back>",
            "      <div type=\"apparatus_note\" xml:id=\"apparatus-summary\">",
            "        <head>Apparatus Summary</head>",
            "        <p>The machine-readable apparatus is stored separately in <ref target=\"apparatus.json\">apparatus.json</ref>. It is a selective poem-level apparatus recording only the material grouped judgments accepted into this release; it does not pretend to be a full witness-by-witness collation.</p>",
            "      </div>",
            "      <div type=\"commentary_note\" xml:id=\"commentary-secondary-note\">",
            "        <head>Secondary Controls</head>",
            "        <p>Commentary-bearing, derivative anthology, and blocked witnesses remain preserved as secondary controls for witness ecology, boundary support, and later research. They do not form part of the main edited poem text.</p>",
            "      </div>",
            "    </back>",
            "  </text>",
            "</TEI>",
        ]
    )
    (XML_DIR / "song-of-enlightenment.xml").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    rows = parse_translation_rows()
    build_working_text(rows)
    build_tei(rows)


if __name__ == "__main__":
    main()
