#!/usr/bin/env python3
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"
GEN = ROOT / "scripts" / "generate_schedule_html.py"

html = subprocess.check_output(["python3", str(GEN)], text=True)
chunks = {}
for part in html.split("<!-- PANEL "):
    if not part.strip():
        continue
    pid, body = part.split(" -->", 1)
    chunks[pid.strip()] = body.strip()

index = INDEX.read_text(encoding="utf-8")
for pid in ("quinta", "sexta", "sabado"):
    pattern = rf'(<div class="day-panel[^"]*" id="panel-{pid}">)(.*?)(</div>\s*<!-- /panel-{pid} -->)'
    if pid not in chunks:
        raise SystemExit(f"missing panel {pid}")
    replacement = rf"\1\n{chunks[pid]}\n        \3"
    index, n = re.subn(pattern, replacement, index, count=1, flags=re.DOTALL)
    if n != 1:
        raise SystemExit(f"panel {pid} replace failed ({n})")

INDEX.write_text(index, encoding="utf-8")
print("Patched schedule panels:", ", ".join(chunks.keys()))
