#!/usr/bin/env python3
"""Turn the CSV sources into the HTML fragments used by index.html.

Writes to tgi2026/build/ (not deployed):

    schedule-16-10.html   schedule rows for day one
    schedule-17-10.html   schedule rows for day two
    speakers.html         one card per faculty member
    speakers.json         the same records, for reference

Run from the repository root:

    python3 tgi2026/scripts/generate_content.py
"""

from __future__ import annotations

import csv
import html
import json
import re
import unicodedata
from pathlib import Path

from schedule_i18n import LABELS, ROLES, TITLES, lookup

BASE = Path(__file__).resolve().parent.parent
BUILD = BASE / "build"
LANGS = ("pt", "en", "es")

DISCUSSION = {"DISCUSSÃO"}
BREAKS = {"COFFEE BREAK", "ALMOÇO"}
MILESTONES = {"ABERTURA", "ENCERRAMENTO"}

# resumes.csv carries a few typos and inconsistent labels for the same role.
ROLE_FIXES = {
    "Oncologista Clinico": "Oncologista Clínico",
    "Cirurgião abdominal": "Cirurgião Abdominal",
    "Cirugiao Hepatobiliar": "Cirurgião Hepatobiliar",
    "Cirurgião geral": "Cirurgião Geral",
    "Preparador físico": "Preparador Físico",
    "PET": "Medicina Nuclear",
    "Enfermeira": "Enfermeira",
}

# Names that resumes.csv abbreviates or that carry a country suffix.
NAME_FIXES = {
    "Luis Felipe": "Luis Felipe Carvalho",
    "Simone Fumolaro - IT": "Simone Fumolaro",
    "Antônio de Padua": "Antônio de Pádua",
    "Cristiane Violet": "Christiane Violet",
}

REGIONS = {"Simone Fumolaro": "Itália"}

# Roles missing from resumes.csv but stated in the program.
ROLE_FALLBACKS = {"Gustavo Fernandes": "Oncologista"}
# Prefer the specialty used in the scientific programme over the résumé label.
ROLE_OVERRIDES = {"Gustavo Lima": "Gastroenterologista"}

# Kept verbatim when a fully uppercase title is converted to title case.
ACRONYMS = {
    "GI", "HCC", "CEC", "CG", "QT", "CPS", "BCLC", "PET", "TGI", "IT", "A",
    "GLP-1", "18.2",
}
LOWERCASE_WORDS = {
    "a", "à", "às", "ao", "aos", "as", "com", "da", "das", "de", "do", "dos",
    "e", "em", "na", "nas", "no", "nos", "o", "os", "ou", "para", "por", "sem",
}
# Typos carried over from the source spreadsheets.
TEXT_FIXES = {
    "Multidisciplinariedade": "Multidisciplinaridade",
    "Adenocarcioma": "Adenocarcinoma",
    "gastrico": "gástrico",
    "metastatico": "metastático",
    "Caludina": "Claudina",
    "colangio carcinoma": "colangiocarcinoma",
    "parenquima": "parênquima",
    "cirurgicas": "cirúrgicas",
    "hepaticas": "hepáticas",
    "multi visceral": "multivisceral",
    # Satellite sessions are named inconsistently across the two spreadsheets.
    "SIMPÓSIO SATÉLITE BRISTOL - HCC": "SIMPÓSIO SATÉLITE - BRISTOL (HCC)",
    "SIMPÓSIO ROCHE": "SIMPÓSIO SATÉLITE - ROCHE",
    "SIMPOSIO": "SIMPÓSIO",
}
# Typos and missing accents in the résumé spreadsheet.
BIO_FIXES = {
    "Clincia": "Clínica",
    "Residencia": "Residência",
    "Medico": "Médico",
    "clinica": "clínica",
    "Clinica": "Clínica",
    "clinico": "clínico",
    "Oncoclinicas": "Oncoclínicas",
    "do Hospitais": "dos Hospitais",
    "Câncer Center-Houston tx-USA": "Cancer Center, Houston/TX, EUA",
    "títular": "titular",
    "Gastrintestinal": "Gastrointestinal",
    "aciencias": "Ciências",
    "Memvro": "Membro",
    "Swizterland": "Switzerland",
    "nao transmissíveis": "não transmissíveis",
    "inflação e dor": "inflamação e dor",
}
BRANDS = {
    "ASTRAZENECA": "AstraZeneca",
    "BRISTOL": "Bristol",
    "ROCHE": "Roche",
    "SERVIER": "Servier",
    "DAIICHI": "Daiichi",
}

# Placeholders in the CSV where a name has not been confirmed yet.
TBD = "A definir"
TBD_TOKENS = {
    "cirurgiao", "cirugiao", "oncologista", "oncologista-clinico", "radiologista",
    "patologista", "enfermeira", "nutricionista",
}

SPECIALTY_GROUPS = [
    ("oncologia", "Oncologia Clínica", ("Oncologista",)),
    ("cirurgia", "Cirurgia", ("Cirurgião",)),
    ("coloproctologia", "Coloproctologia", ("Coloproctologista",)),
    ("hepatologia", "Gastro-Hepatologia", ("Hepatologista", "Gastroenterologista", "Gastro Hepatologista")),
    ("radiologia", "Radiologia", ("Radiologista",)),
    ("patologia", "Patologia", ("Patologista",)),
    ("radioterapia", "Radioterapia", ("Radioterapeuta",)),
    ("nuclear", "Medicina Nuclear", ("Medicina Nuclear",)),
    ("nutricao", "Nutrição", ("Nutricionista", "Nutróloga")),
    ("enfermagem", "Enfermagem", ("Enfermeira",)),
    ("endocrinologia", "Endocrinologia", ("Endocrinologista",)),
    ("fisica", "Preparação Física", ("Preparador Físico",)),
]


def squash(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def slugify(text: str) -> str:
    norm = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", norm.lower())).strip("-")


def split_name_role(raw: str) -> tuple[str, str]:
    raw = squash(raw)
    match = re.match(r"^(.*?)\s*\(([^)]*)\)\s*$", raw)
    if not match:
        return NAME_FIXES.get(raw, raw), ""
    name, role = squash(match.group(1)), squash(match.group(2))
    name = NAME_FIXES.get(name, name)
    for wrong, right in ROLE_FIXES.items():
        if role.lower() == wrong.lower():
            role = right
            break
    return name, role


def pretty(text: str) -> str:
    """Tame the shouty, inconsistent punctuation of the source spreadsheets."""
    text = squash(text).replace("”", "").replace("“", "")
    for wrong, right in TEXT_FIXES.items():
        text = re.sub(rf"\b{re.escape(wrong)}\b", right, text)
    text = re.sub(r"\s+([,;:?!])", r"\1", text)
    text = re.sub(r"(?<=\w)\s+-\s+(?=\w)", " — ", text)

    words = text.split(" ")
    if not any(len(word) >= 4 and word.isupper() for word in words):
        return text

    out = []
    for index, word in enumerate(words):
        core = word.strip(".,:;?!—-()[]")
        if core.upper() in BRANDS:
            out.append(word.replace(core, BRANDS[core.upper()]))
        elif not word.isupper() or core.upper() in ACRONYMS:
            out.append(word)
        elif index and core.lower() in LOWERCASE_WORDS:
            out.append(word.lower())
        elif len(core) < 4:
            out.append(word)
        else:
            out.append(word.capitalize())
    return " ".join(out)


def people_list(raw: str, lang: str = "pt") -> str:
    """Render a `Nome (Especialidade), Nome (Especialidade)` string as chips."""
    tbd = lookup(LABELS, TBD, lang)
    raw = squash(raw)
    if not raw:
        return f'<span class="session-person session-person--tbd">{tbd}</span>'
    chips = []
    for token in re.split(r",(?![^(]*\))", raw):
        token = squash(token)
        if not token:
            continue
        name, role = split_name_role(token)
        if slugify(name) in TBD_TOKENS and not role:
            chips.append(f'<span class="session-person session-person--tbd">{tbd}</span>')
            continue
        chip = f'<span class="session-person">{html.escape(name)}'
        if role:
            chip += f' <em>{html.escape(lookup(ROLES, role, lang))}</em>'
        chips.append(chip + "</span>")
    return "".join(chips)


def specialty_keys(role: str) -> list[str]:
    keys = [
        key
        for key, _, needles in SPECIALTY_GROUPS
        if any(re.search(rf"\b{re.escape(needle)}\b", role, re.I) for needle in needles)
    ]
    return keys or ["outros"]


# ── schedule ────────────────────────────────────────────────────────────────

def read_rows(path: Path) -> list[list[str]]:
    rows = []
    with path.open(encoding="utf-8-sig") as handle:
        for raw in csv.reader(handle):
            cells = [squash(cell) for cell in raw]
            while cells and not cells[-1]:
                cells.pop()
            if cells:
                rows.append(cells)
    return rows


def pad_clock(text: str) -> str:
    """`8:00` -> `08:00`, so the time column stays aligned."""
    return re.sub(r"\b(\d):(\d{2})\b", r"0\1:\2", text)


def split_time(cell: str) -> tuple[str, str]:
    """`08:15 - 08:25 (10 min)` -> (`08:15 – 08:25`, `10 min`)."""
    match = re.match(r"^(.*?)\s*\(([^)]*)\)\s*$", cell)
    if not match:
        return pad_clock(cell.replace(" - ", " – ")), ""
    duration = re.sub(r"^0(?=\d)", "", squash(match.group(2)))
    return pad_clock(squash(match.group(1)).replace(" - ", " – ")), duration


def parse_panel(cell: str) -> dict[str, str]:
    """Split a `Mesa N – title / Presidente: … / Moderadores: …` header."""
    president = moderators = ""
    rest = cell
    match = re.search(r"Moderador(?:es)?:\s*", rest)
    if match:
        moderators = squash(rest[match.end():])
        rest = rest[: match.start()]
    match = re.search(r"Presidente:\s*", rest)
    if match:
        president = squash(rest[match.end():])
        rest = rest[: match.start()]
    return {"title": squash(rest), "president": president, "moderators": moderators}


def speaker_cell(raw: str, lang: str = "pt") -> str:
    name, role = split_name_role(raw.replace("*Online*", "").strip())
    if not name:
        return ""
    if slugify(name) in TBD_TOKENS and not role:
        return f'<span class="speaker-name speaker-name--tbd">{lookup(LABELS, TBD, lang)}</span>'
    out = f'<span class="speaker-name">{html.escape(name)}</span>'
    if role:
        out += f'<span class="speaker-role">{html.escape(lookup(ROLES, role, lang))}</span>'
    if "*Online*" in raw:
        out += f'<span class="speaker-online">{lookup(LABELS, "Online", lang)}</span>'
    return out


def title_html(text: str, lang: str) -> str:
    """Portuguese comes straight from the CSV; translations are authored as HTML."""
    return html.escape(text) if lang == "pt" else lookup(TITLES, text, lang)


def render_schedule(path: Path, lang: str = "pt") -> str:
    rows = read_rows(path)[1:]  # drop the date banner
    out: list[str] = []
    for cells in rows:
        first = cells[0]
        activity = cells[1] if len(cells) > 1 else ""
        speaker = cells[2] if len(cells) > 2 else ""

        if len(cells) == 1 and first.lower().startswith("mesa"):
            panel = parse_panel(first)
            tag, _, title = panel["title"].partition("–")
            number = squash(tag).split()[-1]
            meta = (
                f'<div class="session-meta"><span>{lookup(LABELS, "Presidente", lang)}</span>'
                f'{people_list(panel["president"], lang)}</div>'
                f'<div class="session-meta"><span>{lookup(LABELS, "Moderadores", lang)}</span>'
                f'{people_list(panel["moderators"], lang)}</div>'
            )
            out.append(
                '<tr><td colspan="3" class="session-header">'
                f'<span class="session-tag">{lookup(LABELS, "Mesa", lang)} {number}</span>'
                f'<strong>{title_html(pretty(title), lang)}</strong>{meta}</td></tr>'
            )
            continue

        label, duration = split_time(first)
        time_cell = html.escape(label)
        if duration:
            duration = lookup(LABELS, duration, lang)
            time_cell += f'<br /><span class="session-duration">{html.escape(duration)}</span>'

        upper = activity.upper()
        if upper in MILESTONES:
            out.append(
                f'<tr><td>{time_cell}</td><td colspan="2" class="session-milestone">'
                f'<strong>{lookup(LABELS, upper, lang)}</strong></td></tr>'
            )
        elif upper in BREAKS:
            out.append(
                f'<tr><td>{time_cell}</td><td colspan="2" class="session-break">'
                f'<strong>{lookup(LABELS, upper, lang)}</strong></td></tr>'
            )
        elif upper in DISCUSSION:
            out.append(
                f'<tr><td>{time_cell}</td><td colspan="2" class="session-discussion">'
                f'{lookup(LABELS, "Discussão", lang)}</td></tr>'
            )
        elif "SIMPÓSIO" in upper or "SIMPOSIO" in upper:
            title = activity
            chair = ""
            match = re.match(r"^Chairman\s*-\s*(.*?)\s+(SIMP[ÓO]SIO.*)$", activity, re.I)
            if match:
                chair, title = squash(match.group(1)), squash(match.group(2))
            body = f'<strong>{title_html(pretty(title), lang)}</strong>'
            if chair:
                body += (
                    f'<div class="session-meta"><span>{lookup(LABELS, "Chairman", lang)}</span>'
                    f'{people_list(chair, lang)}</div>'
                )
            if speaker:
                body += f'<div class="session-speaker-line">{speaker_cell(speaker, lang)}</div>'
            out.append(
                f'<tr><td>{time_cell}</td><td colspan="2" class="session-sponsor">{body}</td></tr>'
            )
        else:
            out.append(
                f'<tr><td>{time_cell}</td><td>{title_html(pretty(activity), lang)}</td>'
                f'<td>{speaker_cell(speaker, lang)}</td></tr>'
            )
    return "\n".join(out)


# ── speakers ────────────────────────────────────────────────────────────────

def photo_index() -> dict[str, Path]:
    index: dict[str, Path] = {}
    for path in sorted((BASE / "speakers").iterdir()):
        if path.is_file():
            index[path.stem] = path
    return index


def match_photo(name: str, index: dict[str, Path]) -> str:
    slug = slugify(name)
    for stem, path in index.items():
        if stem == slug or stem.startswith(slug + "-"):
            return f"speakers/{path.name}"
    return ""


def fix_bio(line: str) -> str:
    line = line.replace("\u2060", "").replace("\ufeff", "")
    for wrong, right in BIO_FIXES.items():
        line = re.sub(rf"(?<!\w){re.escape(wrong)}(?!\w)", right, line)
    return line


def read_resumes() -> list[dict]:
    index = photo_index()
    people: list[dict] = []
    with (BASE / "resumes" / "resumes.csv").open(encoding="utf-8-sig") as handle:
        reader = csv.reader(handle)
        next(reader)
        for row in reader:
            if not row or not squash(row[0]):
                continue
            name, role = split_name_role(row[0])
            role = ROLE_OVERRIDES.get(name) or role or ROLE_FALLBACKS.get(name, "")
            bio = [squash(line) for line in (row[1] if len(row) > 1 else "").splitlines()]
            bio = [fix_bio(line.rstrip(";").strip()) for line in bio if line]
            people.append(
                {
                    "name": name,
                    "role": role,
                    "region": REGIONS.get(name, ""),
                    "photo": match_photo(name, index),
                    "bio": bio,
                    "specialties": specialty_keys(role),
                    "slug": slugify(name),
                }
            )
    people.sort(key=lambda person: slugify(person["name"]))
    return people


def render_speakers(people: list[dict]) -> str:
    cards = []
    for person in people:
        attrs = [
            'class="speaker-card"',
            'type="button"',
            f'data-name="{html.escape(person["name"], quote=True)}"',
            f'data-role="{html.escape(person["role"], quote=True)}"',
            f'data-region="{html.escape(person["region"], quote=True)}"',
            *(
                f'data-{field}-{lang}="{html.escape(value, quote=True)}"'
                for field, table in (("role", ROLES), ("region", LABELS))
                for lang in ("en", "es")
                if (value := lookup(table, person[field], lang)) != person[field]
            ),
            f'data-photo="{html.escape(person["photo"], quote=True)}"',
            f'data-specialty="{" ".join(person["specialties"])}"',
            f'data-search="{html.escape(slugify(person["name"] + " " + person["role"]), quote=True)}"',
            "data-bio='" + html.escape(json.dumps(person["bio"], ensure_ascii=False), quote=True) + "'",
        ]
        if person["photo"]:
            media = (
                f'<img src="{person["photo"]}" alt="{html.escape(person["name"], quote=True)}" loading="lazy" />'
            )
        else:
            media = '<span class="speaker-initials" aria-hidden="true">' + html.escape(
                "".join(part[0] for part in person["name"].split()[:2]).upper()
            ) + "</span>"
        meta = html.escape(person["role"]) if person["role"] else ""
        if person["region"]:
            meta = f"{meta} · {html.escape(person['region'])}" if meta else html.escape(person["region"])
        cards.append(
            f'<button {" ".join(attrs)}>'
            f'<span class="speaker-photo">{media}</span>'
            f'<span class="speaker-body"><span class="speaker-card-name">{html.escape(person["name"])}</span>'
            f'<span class="speaker-card-role">{meta}</span></span></button>'
        )
    return "\n".join(cards)


DAYS = {"16-10": "sch.day1", "17-10": "sch.day2"}


def main() -> None:
    BUILD.mkdir(exist_ok=True)
    rendered: dict[str, dict[str, str]] = {}
    for day in DAYS:
        source = BASE / "schedule" / f"programacao-{day}.csv"
        rendered[day] = {lang: render_schedule(source, lang) for lang in LANGS}
        (BUILD / f"schedule-{day}.html").write_text(rendered[day]["pt"] + "\n", encoding="utf-8")

    # EN/ES rows live inside the translations object in index.html.
    lines = []
    for lang in ("en", "es"):
        for day, key in DAYS.items():
            body = rendered[day][lang]
            lines.append(f'      translations.{lang}["{key}"] = `\n{body}`;')
    (BUILD / "schedule-i18n.js").write_text("\n".join(lines) + "\n", encoding="utf-8")

    people = read_resumes()
    dropped = [person["name"] for person in people if not person["photo"] and not person["bio"]]
    people = [person for person in people if person["photo"] or person["bio"]]
    (BUILD / "speakers.html").write_text(render_speakers(people) + "\n", encoding="utf-8")
    (BUILD / "speakers.json").write_text(
        json.dumps(people, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    missing = [person["name"] for person in people if not person["photo"]]
    no_bio = [person["name"] for person in people if not person["bio"]]
    print(f"{len(people)} pessoas")
    print(f"sem foto ({len(missing)}): {', '.join(missing) or '—'}")
    print(f"sem currículo ({len(no_bio)}): {', '.join(no_bio) or '—'}")
    print(f"cards omitidos — só nome ({len(dropped)}): {', '.join(dropped) or '—'}")


if __name__ == "__main__":
    main()
