from __future__ import annotations

import json
import sys
import time
import urllib.request
from pathlib import Path


def load_manifest(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def extract_rendering_urls(manifest: dict) -> list[str]:
    sequences = manifest.get("sequences", [])
    if not sequences:
        raise ValueError("manifest has no sequences")
    canvases = sequences[0].get("canvases", [])
    if not canvases:
        raise ValueError("manifest has no canvases")

    urls: list[str] = []
    for canvas in canvases:
        rendering = canvas.get("rendering", [])
        if rendering:
            first = rendering[0]
            url = first.get("@id") or first.get("id")
            if url:
                urls.append(url)
                continue

        images = canvas.get("images", [])
        if images:
            resource = images[0].get("resource", {})
            url = resource.get("@id") or resource.get("id")
            if url:
                urls.append(url)
                continue

        raise ValueError(f"canvas {canvas.get('label')} has no downloadable image URL")
    return urls


def download(url: str, out_path: Path) -> None:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "woodblocks-song-of-enlightenment-harvester/1.0"},
    )
    with urllib.request.urlopen(request) as response:
        data = response.read()
    out_path.write_bytes(data)


def main() -> int:
    if len(sys.argv) != 3:
        print("usage: python harvest_iiif_manifest_images.py <manifest.json> <output-dir>")
        return 2

    manifest_path = Path(sys.argv[1]).resolve()
    output_dir = Path(sys.argv[2]).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    manifest = load_manifest(manifest_path)
    urls = extract_rendering_urls(manifest)

    for idx, url in enumerate(urls, start=1):
        out_path = output_dir / f"page-{idx:04d}.jpg"
        if out_path.exists() and out_path.stat().st_size > 0:
            continue
        download(url, out_path)
        time.sleep(0.2)

    print(f"HARVESTED {len(urls)} images to {output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
