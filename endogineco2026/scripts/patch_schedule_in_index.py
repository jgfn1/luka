#!/usr/bin/env python3
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"
GEN = ROOT / "scripts" / "generate_schedule_html.py"

CONGRESS_PANELS = ("sexta", "sabado")
PRECONGRESS_PANELS = ("videocirurgia", "nutricao", "usg", "sutura")

PANEL_TBODY_I18N: dict[str, tuple[str, ...]] = {
    "sexta": ("sch.openCongress", "sch.friAudA", "sch.friAudB"),
    "sabado": ("sch.satAudA", "sch.satAudB"),
    "videocirurgia": ("sch.preVideocirurgia",),
    "nutricao": ("sch.preNutricao",),
    "usg": ("sch.preUsg",),
    "sutura": ("sch.preSutura",),
}


def load_panels(mode: str) -> dict[str, str]:
    html = subprocess.check_output(["python3", str(GEN), mode], text=True)
    chunks = {}
    for part in html.split("<!-- PANEL "):
        if not part.strip():
            continue
        pid, body = part.split(" -->", 1)
        chunks[pid.strip()] = body.strip()
    return chunks


def inject_tbody_i18n(panel_html: str, i18n_keys: tuple[str, ...]) -> str:
    tbodies = list(re.finditer(r"<tbody>", panel_html))
    if len(tbodies) != len(i18n_keys):
        raise SystemExit(
            f"tbody/i18n mismatch: expected {len(i18n_keys)}, found {len(tbodies)}"
        )
    out = panel_html
    for match, key in reversed(list(zip(tbodies, i18n_keys))):
        start = match.start()
        out = out[:start] + f'<tbody data-i18n="{key}">' + out[start + len("<tbody>") :]
    return out


def patch_panels(index: str, panel_ids: tuple[str, ...], chunks: dict[str, str]) -> str:
    for pid in panel_ids:
        pattern = rf'(<div class="day-panel[^"]*" id="panel-{pid}">)(.*?)(</div>\s*<!-- /panel-{pid} -->)'
        if pid not in chunks:
            raise SystemExit(f"missing panel {pid}")
        body = chunks[pid]
        if pid in PANEL_TBODY_I18N:
            body = inject_tbody_i18n(body, PANEL_TBODY_I18N[pid])
        replacement = rf"\1\n{body}\n        \3"
        index, n = re.subn(pattern, replacement, index, count=1, flags=re.DOTALL)
        if n != 1:
            raise SystemExit(f"panel {pid} replace failed ({n})")
    return index


def main():
    index = INDEX.read_text(encoding="utf-8")
    congress = load_panels("congress")
    precongress = load_panels("precongress")

    index = patch_panels(index, CONGRESS_PANELS, congress)
    index = patch_panels(index, PRECONGRESS_PANELS, precongress)

    INDEX.write_text(index, encoding="utf-8")
    print(
        "Patched schedule panels:",
        ", ".join(CONGRESS_PANELS + PRECONGRESS_PANELS),
    )


if __name__ == "__main__":
    main()
