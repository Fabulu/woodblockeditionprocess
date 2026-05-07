from __future__ import annotations

from pathlib import Path
from shutil import copy2

from PIL import Image, ImageOps


ROOT = Path(r"C:\woodblocks\Faith_in_Mind_Critical_Edition")
PROCESS = ROOT / "provenance" / "faith-in-mind" / "process"
WORKBENCH = PROCESS / "visual-workbench-holdouts"
PAGE_IMAGES = ROOT / "provenance" / "faith-in-mind" / "ocr" / "T1" / "page-images"


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def copy_alias(src: Path, dst: Path) -> None:
    ensure_dir(dst.parent)
    copy2(src, dst)


def save_rot_variants(src: Path, stem: str) -> None:
    im = Image.open(src)
    rot90 = im.rotate(90, expand=True)
    rot90.save(src.with_name(f"{stem}-rot90.png"))
    mirror = ImageOps.mirror(rot90)
    mirror.save(src.with_name(f"{stem}-rot90-mirror.png"))
    hi_base = mirror.convert("RGB")
    ImageOps.autocontrast(hi_base).save(src.with_name(f"{stem}-rot90-mirror-hi.png"))
    ImageOps.autocontrast(hi_base.convert("L")).save(src.with_name(f"{stem}-rot90-mirror-bw.png"))


def crop_and_save(page: Path, box: tuple[int, int, int, int], dst: Path) -> None:
    ensure_dir(dst.parent)
    im = Image.open(page)
    im.crop(box).save(dst)


def expand_box(
    box: tuple[int, int, int, int],
    pad_x: int,
    pad_y: int,
    max_w: int,
    max_h: int,
) -> tuple[int, int, int, int]:
    x1, y1, x2, y2 = box
    return (
        max(0, x1 - pad_x),
        max(0, y1 - pad_y),
        min(max_w, x2 + pad_x),
        min(max_h, y2 + pad_y),
    )


def regenerate_p007() -> None:
    target = WORKBENCH / "T1-p007"
    ensure_dir(target)
    copy_alias(PROCESS / "tmp-T1-p007-bbox02.png", target / "T1-p007-l03-context.png")
    copy_alias(
        PROCESS / "tmp-T1-p007-bbox02-rot90-mirror-hi.png",
        target / "T1-p007-l03-context-rot90-mirror-hi.png",
    )
    copy_alias(PROCESS / "tmp-T1-p007-bbox02-rot90.png", target / "T1-p007-l03-context-rot90.png")
    copy_alias(PROCESS / "tmp-T1-p007-bbox08.png", target / "T1-p007-l12-context.png")
    copy_alias(
        PROCESS / "tmp-T1-p007-bbox08-rot90-mirror-hi.png",
        target / "T1-p007-l12-context-rot90-mirror-hi.png",
    )
    copy_alias(PROCESS / "tmp-T1-p007-bbox08-rot90.png", target / "T1-p007-l12-context-rot90.png")


def regenerate_p029() -> None:
    target = WORKBENCH / "T1-p029"
    ensure_dir(target)
    page = PAGE_IMAGES / "T1-p029.png"
    im = Image.open(page)
    width, height = im.size
    # RapidOCR catches the short l06 fragment directly.
    exact_box = (854, 431, 981, 693)
    wide_box = expand_box(exact_box, pad_x=160, pad_y=180, max_w=width, max_h=height)
    context_box = expand_box(exact_box, pad_x=250, pad_y=1400, max_w=width, max_h=height)
    crop_and_save(page, exact_box, target / "T1-p029-l06-exact.png")
    crop_and_save(page, wide_box, target / "T1-p029-l06-wide.png")
    crop_and_save(page, context_box, target / "T1-p029-l06-context.png")
    save_rot_variants(target / "T1-p029-l06-context.png", "T1-p029-l06-context")
    save_rot_variants(target / "T1-p029-l06-wide.png", "T1-p029-l06-wide")
    save_rot_variants(target / "T1-p029-l06-exact.png", "T1-p029-l06-exact")
    Image.open(target / "T1-p029-l06-exact.png").rotate(270, expand=True).save(
        target / "T1-p029-l06-exact-rot270.png"
    )
    copy_alias(PROCESS / "tmp-T1-p029-fa-jian-column.png", target / "T1-p029-l06-reference-fa-jian-column.png")


def regenerate_p012() -> None:
    target = WORKBENCH / "T1-p012"
    ensure_dir(target)
    page = PAGE_IMAGES / "T1-p012.png"
    im = Image.open(page)
    width, height = im.size
    # RapidOCR isolates the short l02 strip directly on the original page.
    exact_box = (304, 313, 982, 449)
    crop_and_save(page, expand_box(exact_box, pad_x=70, pad_y=45, max_w=width, max_h=height), target / "T1-p012-l02-exact.png")
    crop_and_save(page, expand_box(exact_box, pad_x=300, pad_y=110, max_w=width, max_h=height), target / "T1-p012-l02-wide.png")
    crop_and_save(page, expand_box(exact_box, pad_x=320, pad_y=420, max_w=width, max_h=height), target / "T1-p012-l02-context.png")
    crop_and_save(page, (0, max(0, exact_box[1] - 80), width, height - 100), target / "T1-p012-l02-fullcol-context.png")
    save_rot_variants(target / "T1-p012-l02-exact.png", "T1-p012-l02-exact")
    save_rot_variants(target / "T1-p012-l02-wide.png", "T1-p012-l02-wide")
    save_rot_variants(target / "T1-p012-l02-context.png", "T1-p012-l02-context")


def main() -> None:
    regenerate_p007()
    regenerate_p029()
    regenerate_p012()
    print("regenerated remaining helper crops")


if __name__ == "__main__":
    main()
