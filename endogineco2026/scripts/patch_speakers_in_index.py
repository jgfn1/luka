#!/usr/bin/env python3
"""Regenerate speaker cards in index.html from palestrantes.csv and speakers/ photos."""

from __future__ import annotations

import csv
import html
import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CSV_PATH = ROOT / "speakers" / "palestrantes.csv"
SPEAKERS_DIR = ROOT / "speakers"
INDEX_PATH = ROOT / "index.html"
PLACEHOLDER = "speakers/placeholder.svg"

# Names whose photo filename does not match the CSV name slug.
PHOTO_OVERRIDES: dict[str, str] = {
    "Andreiza Billar": "speakers/andreissa-paiva-ce.jpg",
    "Cicilia Pontes": "speakers/cecilia-pontes-pe.jpg",
    "Fábio Ohara": "speakers/fabio-ohara-sp.jpg",
    "Giuliano Borell": "speakers/giuliano-borrelli-sp.jpg",
    "Gilcélia Barbieri": "speakers/gilcelia-barbieri-pe.jpeg",
    "Mônica Zomer": "speakers/monica-zomer-kondo-pa.jpg",
    "Patrick Bellilis": "speakers/patrick-bellelis-sp.jpeg",
    "Marina Muniz": "speakers/mariana-muniz-pe.jpg",
}


def strip_accents(text: str) -> str:
    normalized = unicodedata.normalize("NFD", text)
    return "".join(ch for ch in normalized if unicodedata.category(ch) != "Mn")


def normalize_key(text: str) -> str:
    text = strip_accents(text.lower())
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return " ".join(text.split())


def parse_name_field(field: str) -> tuple[str, str]:
    field = field.strip()
    match = re.match(r"^(.*?)\s*-\s*(.+)$", field)
    if match:
        return match.group(1).strip(), match.group(2).strip()
    return field.strip().rstrip(",").strip(), ""


def bio_to_items(bio: str) -> list[str]:
    if not bio or not bio.strip():
        return []
    items: list[str] = []
    for line in bio.replace("\r\n", "\n").split("\n"):
        line = line.strip()
        if not line:
            continue
        line = re.sub(r"^[⁠\u2060\u200b\u200c\u200d\ufeff]+", "", line)
        items.append(line)
    return items


def load_speakers() -> list[tuple[str, str, list[str]]]:
    rows: list[tuple[str, str, list[str]]] = []
    with CSV_PATH.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            name, region = parse_name_field(row["NOME"])
            bio = bio_to_items(row.get("CURRÍCULO", "") or "")
            rows.append((name, region, bio))
    return rows


def build_photo_index() -> dict[str, str]:
    index: dict[str, str] = {}
    for path in sorted(SPEAKERS_DIR.iterdir()):
        if path.suffix.lower() not in {".jpg", ".jpeg", ".png", ".webp"}:
            continue
        rel = f"speakers/{path.name}"
        key = normalize_key(path.stem.replace("-", " "))
        index[key] = rel
        # Also index without trailing region token (e.g. "ana carolina serafim pe" -> "ana carolina serafim")
        parts = key.split()
        if len(parts) >= 2 and len(parts[-1]) <= 3:
            index[" ".join(parts[:-1])] = rel
    return index


def find_photo(name: str, region: str, photo_index: dict[str, str]) -> str | None:
    if name in PHOTO_OVERRIDES:
        return PHOTO_OVERRIDES[name]

    candidates = [
        normalize_key(f"{name} {region}".strip()),
        normalize_key(name),
    ]
    for key in candidates:
        if key in photo_index:
            return photo_index[key]

    name_parts = normalize_key(name).split()
    best: str | None = None
    best_score = 0
    for key, rel in photo_index.items():
        if not all(part in key.split() for part in name_parts):
            continue
        score = len(name_parts)
        if region and normalize_key(region) in key.split():
            score += 1
        if score > best_score:
            best_score = score
            best = rel
    return best


def render_card(name: str, region: str, bio: list[str], photo: str | None) -> str:
    photo_path = photo or PLACEHOLDER
    bio_json = html.escape(json.dumps(bio, ensure_ascii=False), quote=True)
    aria = html.escape(name, quote=True)
    region_text = html.escape(region)
    name_text = html.escape(name)
    content_class = (
        "netflix-card-content netflix-card-content--speaker-placeholder"
        if not photo
        else "netflix-card-content"
    )
    return f"""
          <div class="netflix-card netflix-card--speaker" tabindex="0" role="button" aria-haspopup="dialog" aria-label="{aria}" data-speaker-name="{aria}" data-speaker-region="{region_text}" data-speaker-photo="{photo_path}" data-speaker-bio="{bio_json}">
            <div class="netflix-card-bg" style="background-image:url('{photo_path}');" role="img" aria-label="Foto de {aria}"></div>
            <div class="netflix-card-overlay"></div>
            <div class="{content_class}">
              <h3>{name_text}</h3>
              <p>{region_text}</p>
              <button type="button" class="netflix-card-saiba-mais" data-i18n="speakers.learnMore">Saiba mais</button>
            </div>
          </div>"""


def patch_index(cards_html: str) -> None:
    content = INDEX_PATH.read_text(encoding="utf-8")
    pattern = re.compile(
        r'(<div class="netflix-carousel" id="speakers-carousel">)\s*\n.*?\n(\s*</div>\s*\n\s*<button class="netflix-arrow netflix-arrow-next" id="speakers-next")',
        re.DOTALL,
    )
    replacement = rf"\1\n{cards_html}\n\2"
    updated, count = pattern.subn(replacement, content, count=1)
    if count != 1:
        raise SystemExit("Could not locate speakers carousel in index.html")
    INDEX_PATH.write_text(updated, encoding="utf-8")


def is_confirmed(name: str, region: str, bio: list[str], photo_index: dict[str, str]) -> bool:
    return bool(bio) or find_photo(name, region, photo_index) is not None


def main() -> None:
    speakers = load_speakers()
    photo_index = build_photo_index()
    confirmed = [
        (name, region, bio)
        for name, region, bio in speakers
        if is_confirmed(name, region, bio, photo_index)
    ]
    cards = [
        render_card(name, region, bio, find_photo(name, region, photo_index))
        for name, region, bio in confirmed
    ]
    patch_index("\n".join(cards))
    with_photo = sum(
        1 for name, region, _ in confirmed if find_photo(name, region, photo_index)
    )
    with_bio = sum(1 for _, _, bio in confirmed if bio)
    skipped = len(speakers) - len(confirmed)
    print(
        f"Updated {len(confirmed)} confirmed speakers "
        f"({with_photo} with photo, {with_bio} with bio, "
        f"{len(confirmed) - with_photo} with placeholder only). "
        f"Skipped {skipped} unconfirmed."
    )


if __name__ == "__main__":
    main()
