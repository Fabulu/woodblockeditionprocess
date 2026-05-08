from __future__ import annotations

import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(r"C:\woodblocks\Faith_in_Mind_Critical_Edition")
TEI_PATH = ROOT / "xml-open" / "ce" / "faith-in-mind" / "faith-in-mind.xml"
APPARATUS_PATH = ROOT / "xml-open" / "ce" / "faith-in-mind" / "apparatus.json"
NS = {"tei": "http://www.tei-c.org/ns/1.0"}
LOCUS_URI_RE = re.compile(r"^urn:locus:T1-p\d{3}(?:\.l\d{2}a?)?$")


def main() -> int:
    root = ET.parse(TEI_PATH).getroot()

    line_nodes = root.findall(".//tei:body//tei:l", NS)
    if len(line_nodes) != 71:
        raise SystemExit(f"Expected 71 poem lines, found {len(line_nodes)}.")

    expected_numbers = [str(i) for i in range(1, 72)]
    actual_numbers = [node.get("n") for node in line_nodes]
    if actual_numbers != expected_numbers:
        raise SystemExit("Poem line numbering is not sequential from 1 to 71.")

    bad_corresp: list[str] = []
    for node in line_nodes:
        corresp = node.get("corresp", "")
        if not LOCUS_URI_RE.match(corresp):
            bad_corresp.append(f"line {node.get('n')}: {corresp}")
        if corresp.startswith("#"):
            raise SystemExit(f"Same-document fragment corresp is not allowed here: {corresp}")

    if bad_corresp:
        raise SystemExit("Invalid TEI locus pointers: " + "; ".join(bad_corresp))

    omission_lines = [node for node in line_nodes if node.get("type") == "omission_judgment"]
    if len(omission_lines) != 1 or omission_lines[0].get("n") != "66":
        raise SystemExit("Expected exactly one omission_judgment line at n=66.")

    apparatus = json.loads(APPARATUS_PATH.read_text(encoding="utf-8"))
    if apparatus.get("apparatus_type") != "selective_poem_level":
        raise SystemExit("Apparatus type must be selective_poem_level.")
    if apparatus.get("base_witness") != "T1":
        raise SystemExit("Apparatus base_witness must be T1.")

    tei_loci = {node.get("corresp", "").removeprefix("urn:locus:") for node in line_nodes}
    tei_loci.add("T1-p075")
    for entry in apparatus.get("entries", []):
        locus = entry.get("locus")
        if locus not in tei_loci:
            raise SystemExit(f"Apparatus locus not represented in TEI text: {locus}")

    print("Faith in Mind TEI structural QA passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
