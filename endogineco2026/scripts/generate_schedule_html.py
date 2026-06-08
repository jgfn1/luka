#!/usr/bin/env python3
"""Generate schedule table HTML from CSV files."""
import csv
import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONGRESS_CSV = ROOT / "schedule" / "programacao-preliminar-2026.csv"
PRECONGRESS_DIR = ROOT / "pre-congress"

PRECONGRESS_COURSES = [
    {
        "id": "videocirurgia",
        "csv": "programacao-a-videocirurgia-na-oncologia.csv",
    },
    {
        "id": "nutricao",
        "csv": "programacao-nutricao-para-pacientes-com-endometriose.csv",
    },
    {
        "id": "usg",
        "csv": "programacao-usg-mapeamento-de-endometriose.csv",
    },
    {
        "id": "sutura",
        "csv": "programacao-sutura-dry-lab-em-sutura-endoscopica.csv",
    },
]


def esc(text: str) -> str:
    return html.escape((text or "").strip())


def br(text: str) -> str:
    return esc(text).replace("\n", "<br />")


def day_key(day_label: str) -> str | None:
    d = (day_label or "").lower()
    if "sexta" in d:
        return "sexta"
    if "sábado" in d or "sabado" in d:
        return "sabado"
    if "quinta" in d:
        return "quinta"
    return None


def is_header_row(time: str, activity: str) -> bool:
    a = activity.upper()
    if re.match(r"^(AUDITÓRIO|AUDITORIO|FOYER)\b", a):
        return True
    if a.startswith("MESA ") and ("PRESIDENTE" in a.upper() or "DEBATEDOR" in a.upper()):
        return True
    if "VÍDEOS SHOWS" in a or "VIDEO SHOWS" in a.upper():
        return True
    if "UROGINECOLOGIA EM FOCO" in a:
        return True
    if "CONFERÊNCIAS" in a or "CONFERENCIAS" in a:
        return True
    if "CROSS FIRE" in a and "O que" in activity:
        return True
    if "TRIPLO CROSS FIRE" in a:
        return True
    return False


def row_kind(time: str, activity: str, speaker: str) -> str:
    a = activity.upper()
    t = time.upper()
    if t == "PODCAST" or a == "PODCAST":
        return "podcast"
    if "CERIMÔNIA" in a or "CERIMONIA" in a:
        return "ceremony"
    if "CIRURGIAS AO VIVO" in a:
        return "live"
    if any(
        k in a
        for k in (
            "COFFEE BREAK",
            "INTERVALO",
            "BRUNCH",
            "CREDENCIAMENTO",
            "ABERTURA",
            "DISCUSSÃO",
            "DISCUSSAO",
            "ENCERRAMENTO",
            "FEIJOADA",
            "SIMPÓSIO PATROCINADO",
        )
    ):
        return "break"
    if a == "DISCUSSÃO" or a == "DISCUSSAO":
        return "break"
    return "talk"


def tr_row(time: str, activity: str, speaker: str) -> str:
    time = (time or "").strip()
    activity = (activity or "").strip()
    speaker = (speaker or "").strip()

    if is_header_row(time, activity):
        label = f"<strong>{br(time)}</strong><br />" if time else ""
        return (
            f'<tr><td colspan="3" class="session-header">{label}'
            f"{br(activity)}</td></tr>"
        )

    kind = row_kind(time, activity, speaker)

    if kind == "podcast":
        return '<tr><td colspan="3" class="session-podcast">🎙️ <strong>PODCAST</strong></td></tr>'

    if kind == "ceremony":
        return f'<tr><td colspan="3" class="session-break"><strong>{br(activity)}</strong></td></tr>'

    if not activity and time:
        return (
            f"<tr><td>{br(time)}</td>"
            f'<td colspan="2" class="session-live"><strong>CONTINUAÇÃO</strong></td></tr>'
        )

    if kind == "break" and not speaker:
        if time:
            return (
                f"<tr><td>{br(time)}</td>"
                f'<td colspan="2" class="session-break"><strong>{br(activity)}</strong></td></tr>'
            )
        return f'<tr><td colspan="3" class="session-break"><strong>{br(activity)}</strong></td></tr>'

    if kind == "live":
        body = br(activity)
        if speaker:
            body += f'<div style="font-weight:400;margin-top:.5rem;font-size:.88rem;line-height:1.45">{br(speaker)}</div>'
        if time:
            return (
                f"<tr><td>{br(time)}</td>"
                f'<td colspan="2" class="session-live"><strong>{br(activity.split(chr(10))[0])}</strong>'
                f'{("" if not speaker else f"<div style=\'font-weight:400;margin-top:.35rem;font-size:.88rem;line-height:1.45\'>{br(speaker)}</div>")}'
                f"</td></tr>"
            )
        return f'<tr><td colspan="3" class="session-live"><strong>{body}</strong></td></tr>'

    sp = f'<td class="speaker-name">{br(speaker)}</td>' if speaker else "<td></td>"
    return f"<tr><td>{br(time)}</td><td>{br(activity)}</td>{sp}</tr>"


def is_auditorium_row(time: str, activity: str) -> bool:
    t = (time or "").strip()
    a = (activity or "").strip()
    if re.match(r"^AUDITÓRIO [AB]\s*$", t, re.I):
        return True
    if re.match(r"^AUDITÓRIO [AB]\s*$", a, re.I) and not t:
        return True
    return False


def auditorium_label(name: str) -> str:
    label = name.strip()
    if label.startswith("AUDITÓRIO"):
        return label.replace("AUDITÓRIO", "Auditório")
    if label == "Abertura":
        return "Abertura do congresso"
    return label


def parse_csv_rows(csv_path: Path):
    with csv_path.open(newline="", encoding="utf-8") as f:
        return list(csv.reader(f))


def parse_congress_sections():
    rows = parse_csv_rows(CONGRESS_CSV)
    days: dict[str, dict] = {}
    current_key = None

    def ensure_auditorium(day: dict, name: str):
        found = next((a for a in day["auditoriums"] if a["name"] == name), None)
        if not found:
            day["auditoriums"].append({"name": name, "rows": []})
            found = day["auditoriums"][-1]
        return found

    for row in rows:
        if not row or all(not (c or "").strip() for c in row):
            continue
        time = row[0] if len(row) > 0 else ""
        activity = row[1] if len(row) > 1 else ""
        speaker = row[2] if len(row) > 2 else ""

        if "CONGRESSO ENDOGINECO" in (time + activity):
            continue

        if time.strip().lower() in ("horário", "horario"):
            key = day_key(activity)
            if key is None or key == "quinta":
                current_key = None
                continue
            if key not in days:
                days[key] = {"day": activity.strip(), "day_key": key, "auditoriums": []}
            current_key = key
            continue

        if not current_key:
            continue

        day = days[current_key]

        if is_auditorium_row(time, activity):
            aud_name = (time or activity).strip()
            ensure_auditorium(day, aud_name)
            continue

        if not day["auditoriums"]:
            ensure_auditorium(day, "Abertura")

        active = day["auditoriums"][-1]
        active["rows"].append((time, activity, speaker))

    return [days[k] for k in ("sexta", "sabado") if k in days]


def parse_precongress_section(csv_path: Path):
    rows = parse_csv_rows(csv_path)
    program_rows = []
    started = False

    for row in rows:
        if not row or all(not (c or "").strip() for c in row):
            continue
        time = row[0] if len(row) > 0 else ""
        activity = row[1] if len(row) > 1 else ""
        speaker = row[2] if len(row) > 2 else ""

        upper = (time + activity).upper()
        if "PRÉ CONGRESSO" in upper or "PRE CONGRESSO" in upper:
            continue
        if "CONGRESSO ENDOGINECO" in upper:
            continue
        if time.strip().lower() in ("horário", "horario"):
            started = True
            continue
        if not started:
            continue
        program_rows.append((time, activity, speaker))

    return {
        "auditoriums": [{"name": "Programação", "rows": program_rows}],
    }


def render_panel(section, col3="Palestrante", hide_single_label=True):
    parts = []
    auditoriums = section["auditoriums"]
    for aud in auditoriums:
        if hide_single_label and len(auditoriums) == 1 and aud["name"] == "Programação":
            pass
        else:
            parts.append(f'          <p class="aud-label">{esc(auditorium_label(aud["name"]))}</p>')
        parts.append('          <div class="schedule-scroll">')
        parts.append('            <table class="schedule-table">')
        w_time = "155px"
        parts.append(
            f'              <thead><tr><th style="width:{w_time}">Horário</th>'
            f'<th>Atividade</th><th style="width:220px">{col3}</th></tr></thead>'
        )
        parts.append("              <tbody>")
        for time, activity, speaker in aud["rows"]:
            parts.append("                " + tr_row(time, activity, speaker))
        parts.append("              </tbody>")
        parts.append("            </table>")
        parts.append("          </div>")
        parts.append("")
    return "\n".join(parts)


def emit_panels(mode: str):
    if mode == "congress":
        sections = parse_congress_sections()
        for sec in sections:
            print(f"<!-- PANEL {sec['day_key']} -->")
            print(render_panel(sec, "Palestrante", hide_single_label=False))
    elif mode == "precongress":
        for course in PRECONGRESS_COURSES:
            csv_path = PRECONGRESS_DIR / course["csv"]
            if not csv_path.exists():
                raise SystemExit(f"missing pre-congress CSV: {csv_path}")
            section = parse_precongress_section(csv_path)
            print(f"<!-- PANEL {course['id']} -->")
            print(render_panel(section, "Palestrante", hide_single_label=True))
    else:
        raise SystemExit(f"unknown mode: {mode}")


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "congress"
    emit_panels(mode)


if __name__ == "__main__":
    main()
