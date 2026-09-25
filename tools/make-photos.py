"""Turn one source photo into every size the site serves.

    python tools/make-photos.py <source-image> <slug|stock-name> [--credit "Pexels"]

Writes into assets/img/:
    <name>-{400,800,1600}.jpg   16:9, the article hero and the cards
    <name>-{400,800,1600}.webp  same images, WebP (40% smaller)
    <name>-og.jpg               1200x630, cropped wider for social cards

then prints the frontmatter to paste into the article:

    hero: "/assets/img/<name>"
    heroCredit: "Pexels"

An article with a hero uses the photograph for its social card; articles
without one keep their generated typographic card.
"""
import sys
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "img"
SIZES = (1600, 800, 400)
RATIO = 9 / 16          # the page frames are 16:9
OG_SIZE = (1200, 630)   # the social card, cropped wider


def crop_to(im, ratio):
    w, h = im.size
    if w / h > ratio:                       # too wide - trim the sides
        target = h * ratio
        left = (w - target) / 2
        return im.crop((int(left), 0, int(left + target), h))
    target_h = w / ratio                    # too tall - trim top and bottom
    top = (h - target_h) / 2
    return im.crop((0, int(top), w, int(top + target_h)))


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        return 1
    src, name = Path(sys.argv[1]), sys.argv[2]
    credit = ""
    if "--credit" in sys.argv:
        credit = sys.argv[sys.argv.index("--credit") + 1]

    original = Image.open(src).convert("RGB")
    OUT.mkdir(parents=True, exist_ok=True)

    page = crop_to(original, RATIO)
    for w in SIZES:
        h = round(w * RATIO)
        r = page.resize((w, h), Image.LANCZOS)
        jpg, webp = OUT / f"{name}-{w}.jpg", OUT / f"{name}-{w}.webp"
        r.save(jpg, "JPEG", quality=86, optimize=True, progressive=True)
        r.save(webp, "WEBP", quality=80, method=6)
        print(f"  {jpg.name:32} {jpg.stat().st_size // 1024:4}KB   {webp.name:32} {webp.stat().st_size // 1024:4}KB")

    og = crop_to(original, OG_SIZE[0] / OG_SIZE[1]).resize(OG_SIZE, Image.LANCZOS)
    og_path = OUT / f"{name}-og.jpg"
    og.save(og_path, "JPEG", quality=84, optimize=True, progressive=True)
    print(f"  {og_path.name:32} {og_path.stat().st_size // 1024:4}KB   (1200x630 social card)")

    print(f"\nfrontmatter for the article:\n  hero: \"/assets/img/{name}\"")
    if credit:
        print(f'  heroCredit: "{credit}"')
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
