from __future__ import annotations

import json
import urllib.error
import sys
import time
import urllib.request
from pathlib import Path


def load_manifest(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def extract_canvas_url_v2(canvas: dict) -> str | None:
    rendering = canvas.get("rendering", [])
    if rendering:
        first = rendering[0]
        url = first.get("@id") or first.get("id")
        if url:
            return url

    images = canvas.get("images", [])
    if images:
        resource = images[0].get("resource", {})
        url = resource.get("@id") or resource.get("id")
        if url:
            return url
    return None


def extract_canvas_url_v3(canvas: dict) -> str | None:
    items = canvas.get("items", [])
    for page in items:
        anno_items = page.get("items", [])
        for anno in anno_items:
            body = anno.get("body", {})
            if isinstance(body, list):
                for candidate in body:
                    services = candidate.get("service", [])
                    if services:
                        first_service = services[0]
                        service_id = first_service.get("id") or first_service.get("@id")
                        if service_id:
                            return f"{service_id}/full/full/0/default.jpg"
                    url = candidate.get("id") or candidate.get("@id")
                    if url:
                        return url
            else:
                services = body.get("service", [])
                if services:
                    first_service = services[0]
                    service_id = first_service.get("id") or first_service.get("@id")
                    if service_id:
                        return f"{service_id}/full/full/0/default.jpg"
                url = body.get("id") or body.get("@id")
                if url:
                    return url
    return None


def extract_rendering_urls(manifest: dict) -> list[str]:
    canvases: list[dict]
    if "items" in manifest:
        canvases = manifest.get("items", [])
        if not canvases:
            raise ValueError("manifest has no items")
        extractor = extract_canvas_url_v3
    else:
        sequences = manifest.get("sequences", [])
        if not sequences:
            raise ValueError("manifest has no sequences")
        canvases = sequences[0].get("canvases", [])
        if not canvases:
            raise ValueError("manifest has no canvases")
        extractor = extract_canvas_url_v2

    urls: list[str] = []
    for canvas in canvases:
        url = extractor(canvas)
        if url:
            urls.append(url)
            continue
        raise ValueError(f"canvas {canvas.get('label')} has no downloadable image URL")
    return urls


def download(url: str, out_path: Path, attempts: int = 5) -> None:
    last_error: Exception | None = None
    for attempt in range(1, attempts + 1):
        try:
            request = urllib.request.Request(
                url,
                headers={"User-Agent": "woodblocks-song-of-enlightenment-harvester/1.0"},
            )
            with urllib.request.urlopen(request) as response:
                data = response.read()
            out_path.write_bytes(data)
            return
        except (urllib.error.HTTPError, urllib.error.URLError, OSError) as exc:
            last_error = exc
            if attempt == attempts:
                break
            if isinstance(exc, urllib.error.HTTPError) and exc.code == 429:
                time.sleep(min(60, attempt * 15))
            else:
                time.sleep(min(10, attempt * 2))
    assert last_error is not None
    raise last_error


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
        time.sleep(2.0)

    print(f"HARVESTED {len(urls)} images to {output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
