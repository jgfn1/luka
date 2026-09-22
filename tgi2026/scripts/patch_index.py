#!/usr/bin/env python3
"""Inject the generated fragments into index.html between the marker comments.

The Portuguese schedule rows and the speaker cards are the only generated
regions; every other string in the page (including the EN/ES dictionaries) is
maintained by hand.

Run from the repository root:

    python3 tgi2026/scripts/generate_content.py
    python3 tgi2026/scripts/patch_index.py
"""

import re
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
INDEX = BASE / "index.html"
BUILD = BASE / "build"

REGIONS = {
    "schedule:16-10": BUILD / "schedule-16-10.html",
    "schedule:17-10": BUILD / "schedule-17-10.html",
    "speakers": BUILD / "speakers.html",
    "schedule:i18n": BUILD / "schedule-i18n.js",
}


def main() -> None:
    page = INDEX.read_text(encoding="utf-8")
    for marker, source in REGIONS.items():
        open_tag, close_tag = (
            (f"/* {marker} */", f"/* /{marker} */")
            if source.suffix == ".js"
            else (f"<!-- {marker} -->", f"<!-- /{marker} -->")
        )
        pattern = re.compile(
            rf"({re.escape(open_tag)}\n).*?({re.escape(close_tag)})", re.DOTALL
        )
        if not pattern.search(page):
            raise SystemExit(f"marcador ausente em index.html: {marker}")
        body = source.read_text(encoding="utf-8")
        page = pattern.sub(lambda m: m.group(1) + body + m.group(2), page, count=1)
        print(f"{marker}: {body.count(chr(10))} linhas")
    INDEX.write_text(page, encoding="utf-8")


if __name__ == "__main__":
    main()
