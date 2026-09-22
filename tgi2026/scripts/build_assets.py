#!/usr/bin/env python3
"""Derive the site image assets from the two source artworks.

Both source files are JPEGs with a light lavender background. The logo and the
promotional card are knocked out by luminance so they can be placed over any
background, and the Open Graph card is recomposed at 1200x630.

Run from the repository root:

    python3 tgi2026/scripts/build_assets.py
"""

from pathlib import Path

from PIL import Image

BASE = Path(__file__).resolve().parent.parent
ASSETS = BASE / "assets"

# Luminance window that separates the artwork from the lavender backdrop.
ALPHA_OPAQUE_BELOW = 150.0
ALPHA_CLEAR_ABOVE = 195.0

# Column where the dotted arc ends and the wordmark begins (source pixels).
ARC_END_X = 390

LAVENDER_TOP = (247, 243, 253)
LAVENDER_BOTTOM = (214, 190, 245)


def knockout(image: Image.Image) -> Image.Image:
    """Turn the light backdrop into transparency, keeping soft edges."""
    rgb = image.convert("RGB")
    lum = rgb.convert("L")
    src, gray = rgb.load(), lum.load()
    out = Image.new("RGBA", rgb.size)
    dst = out.load()
    span = ALPHA_CLEAR_ABOVE - ALPHA_OPAQUE_BELOW
    for y in range(rgb.size[1]):
        for x in range(rgb.size[0]):
            level = gray[x, y]
            if level <= ALPHA_OPAQUE_BELOW:
                alpha = 255
            elif level >= ALPHA_CLEAR_ABOVE:
                alpha = 0
            else:
                alpha = int(round(255 * (ALPHA_CLEAR_ABOVE - level) / span))
            r, g, b = src[x, y]
            dst[x, y] = (r, g, b, alpha)
    return out


def trim(image: Image.Image) -> Image.Image:
    box = image.getbbox()
    return image.crop(box) if box else image


def scaled_to_width(image: Image.Image, width: int) -> Image.Image:
    height = round(image.height * width / image.width)
    return image.resize((width, height), Image.LANCZOS)


def lavender_backdrop(size: tuple[int, int]) -> Image.Image:
    width, height = size
    canvas = Image.new("RGB", size)
    pixels = canvas.load()
    for y in range(height):
        t = y / max(1, height - 1)
        row = tuple(
            round(LAVENDER_TOP[i] + (LAVENDER_BOTTOM[i] - LAVENDER_TOP[i]) * t)
            for i in range(3)
        )
        for x in range(width):
            pixels[x, y] = row
    return canvas


def main() -> None:
    logo = trim(knockout(Image.open(ASSETS / "tgi2026-logo.jpeg")))
    logo.save(ASSETS / "logo-tgi2026.png")

    emblem = trim(logo.crop((0, 0, ARC_END_X, logo.height)))
    emblem.save(ASSETS / "emblem-tgi2026.png")

    side = max(emblem.size) + 48
    favicon = Image.new("RGBA", (side, side), (0, 0, 0, 0))
    favicon.alpha_composite(
        emblem, ((side - emblem.width) // 2, (side - emblem.height) // 2)
    )
    favicon.resize((512, 512), Image.LANCZOS).save(ASSETS / "favicon.png")

    card = knockout(Image.open(ASSETS / "promotional-card.jpeg"))
    # Date + venue block, read off the promotional card (source rows 640-815).
    date_block = trim(card.crop((60, 640, 1200, 815)))

    og = lavender_backdrop((1200, 630)).convert("RGBA")
    og_logo = scaled_to_width(logo, 780)
    og.alpha_composite(og_logo, ((1200 - og_logo.width) // 2, 95))
    og_date = scaled_to_width(date_block, 660)
    og.alpha_composite(og_date, ((1200 - og_date.width) // 2, 410))
    og.convert("RGB").save(ASSETS / "og-tgi2026.png")

    for path in (
        "logo-tgi2026.png",
        "emblem-tgi2026.png",
        "favicon.png",
        "og-tgi2026.png",
    ):
        print(path, Image.open(ASSETS / path).size)


if __name__ == "__main__":
    main()
