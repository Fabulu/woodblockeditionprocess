from __future__ import annotations

import argparse
from pathlib import Path

from lxml import etree as ET


DEFAULT_SCHEMA = Path(r"C:\woodblocks\schemas\openzentexts-tei.rng")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate an OpenZen-style TEI file against the shared Relax NG schema."
    )
    parser.add_argument("xml_path", help="Path to the TEI XML file to validate.")
    parser.add_argument(
        "--schema",
        default=str(DEFAULT_SCHEMA),
        help="Path to the Relax NG schema. Defaults to C:\\woodblocks\\schemas\\openzentexts-tei.rng.",
    )
    args = parser.parse_args()

    xml_path = Path(args.xml_path)
    schema_path = Path(args.schema)

    schema = ET.RelaxNG(ET.parse(str(schema_path)))
    doc = ET.parse(str(xml_path))
    if not schema.validate(doc):
      err = schema.error_log.last_error
      raise SystemExit(f"OpenZen TEI schema validation failed for {xml_path}: line {err.line}: {err.message}")

    print(f"OpenZen TEI schema validation passed: {xml_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
