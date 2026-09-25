"""Turn one source photo into the sizes and formats the site serves.

    python tools/make-photos.py <source-image> <slug|stock-name> [--credit "Pexels"]

Writes assets/img/<name>-{400,800,1600}.jpg and .webp, then prints the frontmatter
line to paste into the article:

    hero: "/assets/img/<name>"
    heroCredit: "Pexels"

Sizes match the design: 1600 for a lead or article hero, 800 for cards,
400 for the small thumbnails in the river and rails.
"""
import sys
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "img"
SIZES = (1600, 800, 400)
RATIO = 9 / 16  # everything is cropped to a 16:9 frame


def crop_to_ratio(im, ratio=RATIO):
    w, h = im.size
    target = h * ratio
    if w > target:                       # too wide - trim the sides
        left = (w - target) / 2
        return im.crop((int(left), 0, int(left + target), h))
    target_h = w / ratio                 # too tall - trim top and bottom
    top = (h - target_h) / 2
    return im.crop((0, int(top), w, int(top + target_h)))


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        return 1
    src = Path(sys.argv[1])
    name = sys.argv[2]
    credit = ""
    if "--credit" in sys.argv:
        credit = sys.argv[sys.argv.index("--credit") + 1]

    im = Image.open(src).convert("RGB")
    im = crop_to_ratio(im)
    OUT.mkdir(parents=True, exist_ok=True)
    main_w = None
    for w in SIZES:
        h = round(w * RATIO)
        r = im.resize((w, h), Image.LANCZOS)
        jpg = OUT / f"{name}-{w}.jpg"
        webp = OUT / f"{name}-{w}.webp"
        # the 1600 copy is the one printed to the page, so keep it crisp
        r.save(jpg, "JPEG", quality=86, optimize=True, progressive=True)
        r.save(webp, "WEBP", quality=80, method=6)
        if w == 1600:
            main_w = jpg
        print(f"  {jpg.name:34} {jpg.stat().st_size // 1024:4}KB    {webp.name:34} {webp.stat().st_size // 1024:4}KB")

    print(f"\nfrontmatter for the article:\n  hero: \"/assets/img/{name}\"")
    if credit:
        print(f'  heroCredit: "{credit}"')
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
