"""Generate social images and icons for turningcircle.co.uk.

Run from the repo root after adding or changing an article:

    python tools/make-images.py

What it does:
- assets/og/default.png (1200x630): site card for pages without their own image
- assets/og/<slug>.png (1200x630): one per root-level article, from its frontmatter title
- assets/img/favicon-32.png and assets/img/apple-touch-icon.png

Font sources live in assets/fonts/src/ (variable TTFs). If they are missing the
script falls back to Georgia, which changes the look but still produces output.
"""

import re
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "assets" / "fonts" / "src"
OG_DIR = ROOT / "assets" / "og"
IMG_DIR = ROOT / "assets" / "img"

SLATE = (26, 30, 36)
AMBER = (217, 119, 54)
PAPER = (250, 248, 244)
GREY = (156, 160, 168)

SKIP = {"index.md", "about.md", "404.md"}


def font_path(name, windows_fallback):
    p = SRC / name
    if p.exists():
        return p
    alt = Path("C:/Windows/Fonts") / windows_fallback
    if alt.exists():
        return alt
    raise SystemExit(f"font not found: {name}")


FRAUNCES = font_path("Fraunces.ttf", "georgiab.ttf")
NEWSREADER = font_path("Newsreader.ttf", "georgia.ttf")
NEWSREADER_I = font_path("Newsreader-Italic.ttf", "georgiai.ttf")


def load_font(path, size, wght=None, opsz=None):
    f = ImageFont.truetype(str(path), size)
    try:
        axes = f.get_variation_axes()
        values = []
        for ax in axes:
            name = ax.get("name", b"")
            if isinstance(name, bytes):
                name = name.decode("utf-8", "ignore")
            name = name.lower()
            if "weight" in name and wght is not None:
                values.append(wght)
            elif "optical" in name and opsz is not None:
                values.append(opsz)
            else:
                values.append(ax.get("default"))
        f.set_variation_by_axes(values)
    except Exception:
        pass
    return f


def parse_frontmatter(text):
    m = re.match(r"^---\r?\n(.*?)\r?\n---", text, re.S)
    if not m:
        return {}
    out = {}
    for line in m.group(1).splitlines():
        mm = re.match(r'^([\w-]+):\s*"(.*)"\s*$', line)
        if mm:
            out[mm.group(1)] = mm.group(2)
    return out


def wrap(draw, text, font, max_width):
    lines, current = [], ""
    for word in text.split():
        candidate = (current + " " + word).strip()
        if draw.textlength(candidate, font=font) <= max_width or not current:
            current = candidate
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def tracked_text(draw, xy, text, font, fill, tracking):
    x, y = xy
    for ch in text:
        draw.text((x, y), ch, font=font, fill=fill)
        x += draw.textlength(ch, font=font) + tracking


def og_card(path, title=None, tagline=None):
    W, H = 1200, 630
    M = 84
    img = Image.new("RGB", (W, H), SLATE)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W, 10], fill=AMBER)

    mark = load_font(FRAUNCES, 30, wght=560, opsz=60)
    tracked_text(d, (M, 86), "TURNINGCIRCLE", mark, AMBER, 10)
    d.rectangle([M, 148, M + 64, 151], fill=AMBER)

    if title:
        size = 84
        while size >= 54:
            f = load_font(FRAUNCES, size, wght=600, opsz=144)
            lines = wrap(d, title, f, W - 2 * M)
            if len(lines) <= 4:
                break
            size -= 6
        line_height = int(size * 1.14)
        total = line_height * len(lines)
        y = max(190, 352 - total // 2)
        for line in lines:
            d.text((M, y), line, font=f, fill=PAPER)
            y += line_height
    else:
        big = load_font(FRAUNCES, 136, wght=640, opsz=144)
        d.text((M - 6, 200), "Turning", font=big, fill=PAPER)
        offset = d.textlength("Turning", font=big)
        d.text((M - 6 + offset, 200), "Circle", font=big, fill=AMBER)
        if tagline:
            sf = load_font(NEWSREADER_I, 46, wght=400, opsz=30)
            d.text((M, 404), tagline, font=sf, fill=GREY)

    d.rectangle([M, 566, W - M, 567], fill=(64, 69, 78))
    foot = load_font(NEWSREADER, 26, wght=400, opsz=16)
    tag = load_font(NEWSREADER_I, 26, wght=400, opsz=20)
    d.text((M, 586), "turningcircle.co.uk", font=foot, fill=GREY)
    label = "Independent UK car coverage"
    d.text((W - M - d.textlength(label, font=tag), 586), label, font=tag, fill=GREY)

    path.parent.mkdir(parents=True, exist_ok=True)
    img.save(path, "PNG")
    print("wrote", path.relative_to(ROOT))


def icon(path, size, rounded):
    s = size
    img = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    if rounded:
        d.rounded_rectangle([0, 0, s - 1, s - 1], radius=max(2, int(s * 0.21)), fill=(*SLATE, 255))
    else:
        d.rectangle([0, 0, s - 1, s - 1], fill=(*SLATE, 255))
    c = s / 2
    r = s * 0.27
    w = max(2, round(s * 0.095))
    d.arc([c - r, c - r, c + r, c + r], start=-90, end=180, fill=AMBER, width=w)
    a = s * 0.15
    x, y = c - r, c
    d.polygon([(x, y - a * 0.95), (x - a * 0.6, y + a * 0.55), (x + a * 0.6, y + a * 0.55)], fill=AMBER)
    path.parent.mkdir(parents=True, exist_ok=True)
    img.save(path, "PNG")
    print("wrote", path.relative_to(ROOT))


def main():
    og_card(OG_DIR / "default.png", tagline="The UK car market, read properly.")
    for md in sorted(ROOT.glob("*.md")):
        if md.name in SKIP:
            continue
        fm = parse_frontmatter(md.read_text(encoding="utf-8"))
        if not fm.get("title"):
            continue
        og_card(OG_DIR / f"{md.stem}.png", title=fm["title"])
    icon(IMG_DIR / "favicon-32.png", 32, rounded=True)
    icon(IMG_DIR / "apple-touch-icon.png", 180, rounded=False)


if __name__ == "__main__":
    main()
