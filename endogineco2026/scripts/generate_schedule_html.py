#!/usr/bin/env python3
"""Generate schedule table HTML from programacao-preliminar-2026.csv."""
import csv
import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "schedule" / "programacao-preliminar-2026.csv"


def esc(text: str) -> str:
    return html.escape((text or "").strip())


def br(text: str) -> str:
    return esc(text).replace("\n", "<br />")


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


def tr_row(time: str, activity: str, speaker: str, col3_label: str = "Palestrante") -> str:
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


def parse_sections():
    with CSV_PATH.open(newline="", encoding="utf-8") as f:
        rows = list(csv.reader(f))

    sections = []
    current = None
    auditorium = None

    def flush():
        nonlocal current
        if current and current.get("auditoriums"):
            sections.append(current)
        current = None

    for row in rows:
        if not row or all(not (c or "").strip() for c in row):
            continue
        time = row[0] if len(row) > 0 else ""
        activity = row[1] if len(row) > 1 else ""
        speaker = row[2] if len(row) > 2 else ""

        if "CONGRESSO ENDOGINECO" in (time + activity):
            continue

        if time.strip().lower() == "horário" or time.strip().lower() == "horario":
            day = activity.strip()
            flush()
            current = {"day": day, "auditoriums": []}
            auditorium = None
            continue

        if not current:
            continue

        aud_match = re.match(r"^(AUDITÓRIO [AB]|AUDITORIO [AB]|FOYER)\s*$", time.strip(), re.I)
        if aud_match or (
            len(row) >= 1
            and re.match(r"^AUDITÓRIO [AB]\s*$", (time or "").strip(), re.I)
            and not activity.strip()
        ):
            auditorium = time.strip() or activity.strip()
            current["auditoriums"].append({"name": auditorium, "rows": []})
            continue

        if "Quinta" in current["day"]:
            prefix = None
            for p in ("AUDITÓRIO C", "AUDITÓRIO A", "AUDITÓRIO B", "FOYER"):
                if p in activity.upper():
                    prefix = p
                    break
            if prefix:
                found = next((a for a in current["auditoriums"] if a["name"] == prefix), None)
                if not found:
                    current["auditoriums"].append({"name": prefix, "rows": []})
                    found = current["auditoriums"][-1]
                found["rows"].append((time, activity, speaker))
            else:
                active = current["auditoriums"][-1] if current["auditoriums"] else None
                if not active:
                    current["auditoriums"].append({"name": "Pré-congresso", "rows": []})
                    active = current["auditoriums"][-1]
                active["rows"].append((time, activity, speaker))
        else:
            if not current["auditoriums"]:
                current["auditoriums"].append({"name": "Abertura", "rows": []})
            current["auditoriums"][-1]["rows"].append((time, activity, speaker))

    flush()
    return sections


def render_panel(section, col3="Palestrante"):
    parts = []
    for aud in section["auditoriums"]:
        label = aud["name"]
        is_quinta = "Quinta" in section["day"]
        if label.startswith("AUDITÓRIO C"):
            label = (
                "Auditório C — Curso de USG Mapeamento de Endometriose"
                if is_quinta
                else "Auditório C"
            )
        elif label.startswith("AUDITÓRIO A"):
            label = (
                "Auditório A — A Videocirurgia na Oncoginecologia"
                if is_quinta
                else "Auditório A"
            )
        elif label.startswith("AUDITÓRIO B"):
            label = (
                "Auditório B — Curso de Nutrição para Pacientes com Endometriose"
                if is_quinta
                else "Auditório B"
            )
        elif label.startswith("AUDITÓRIO"):
            label = label.replace("AUDITÓRIO", "Auditório")
        elif label == "FOYER":
            label = (
                "Foyer — Curso de Sutura Dry Lab em Sutura Endoscópica"
                if is_quinta
                else "Foyer"
            )
        elif label == "Abertura":
            label = "Abertura do congresso"
        parts.append(f'          <p class="aud-label">{esc(label)}</p>')
        parts.append('          <div class="schedule-scroll">')
        parts.append('            <table class="schedule-table">')
        w_time = "155px" if "Sexta" in section["day"] or "Sábado" in section["day"] else "140px"
        parts.append(
            f'              <thead><tr><th style="width:{w_time}">Horário</th>'
            f"<th>Atividade</th><th style=\"width:220px\">{col3}</th></tr></thead>"
        )
        parts.append("              <tbody>")
        for time, activity, speaker in aud["rows"]:
            parts.append("                " + tr_row(time, activity, speaker, col3))
        parts.append("              </tbody>")
        parts.append("            </table>")
        parts.append("          </div>")
        parts.append("")
    return "\n".join(parts)


def main():
    sections = parse_sections()
    panel_ids = ["quinta", "sexta", "sabado"]
    for sec, pid in zip(sections, panel_ids):
        col3 = (
            "Coordenação / Palestrante"
            if "Quinta" in sec["day"]
            else "Palestrante"
        )
        print(f"<!-- PANEL {pid} -->")
        print(render_panel(sec, col3))


if __name__ == "__main__":
    main()
