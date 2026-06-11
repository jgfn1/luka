# Luka Plan Event Websites

Monorepo of landing pages for medical and scientific events produced by **Luka
Plan Promoções e Eventos**. Each event is a self-contained static site on its own
custom domain; all sites deploy from this single Vercel project.

Developed and maintained by **Automa IT & Development**. This repository is
scoped to the Luka Plan client — future clients will have their own repositories
with the same technical pattern (one repo per client, host-based routing in
`vercel.json`).

## Active Projects

### III Simpósio TGI

- **Domain**: [www.tgirecife.com.br](https://www.tgirecife.com.br/)
- **Topic**: Gastrointestinal oncology
- **Date**: October 31 – November 1, 2025 (2 days)
- **Location**: Novotel Recife Marina
- **Folder**: `/tgi/`
- **Languages**: PT, EN, ES, FR

### Gastro Conecta & Nutri Conecta 2026

- **Domain**: [gastroconecta2026.com.br](https://gastroconecta2026.com.br/)
- **Topic**: Gastrointestinal tract and nutrition
- **Date**: March 27, 2026 (1 day)
- **Location**: Novotel Recife Marina
- **Folder**: `/gastroconecta2026/`
- **Languages**: PT, EN, FR

### II Simpósio Oncoderma Recife

- **Domain**: [www.oncodermarecife2026.com.br](https://www.oncodermarecife2026.com.br/)
- **Topic**: Cutaneous oncology
- **Date**: June 5, 2026 (1 day)
- **Location**: Hospital Santa Joana Recife
- **Folder**: `/oncoderma2026/`
- **Languages**: PT

### Congresso Internacional Endogineco 2026

- **Domain**: [www.congressoendoginecorecife.com.br](https://www.congressoendoginecorecife.com.br/)
- **Topic**: Gynecology and endoscopy
- **Date**: August 27–29, 2026 (3 days)
- **Location**: Recife
- **Folder**: `/endogineco2026/`
- **Languages**: PT

### Portfolio (Automa IT & Development)

- **Default URL**: [lukaplan.vercel.app](https://lukaplan.vercel.app/) (also any
  other `*.vercel.app` hostname for this project)
- **Folder**: `/portfolio/`
- **Languages**: EN, PT, ES

## Tech Stack

- Pure HTML5 / CSS3 / vanilla JavaScript — no framework, no build step
- Each site is a single self-contained `index.html` plus local assets
- Per-site client-side language switchers (where applicable)
- Fully responsive design
- Host-based routing and redirects via `vercel.json`
- Optional Python helper scripts for generating schedule tables (Endogineco)

## Project Structure

```
/
├── portfolio/                 # Automa portfolio (default Vercel URL)
│   └── index.html
├── tgi/                       # III Simpósio TGI (tgirecife.com.br)
│   ├── index.html
│   ├── LOGO-TGI.png
│   └── assets/                # committee, speakers, sponsors, logos, PDFs
├── gastroconecta2026/         # Gastro Conecta & Nutri Conecta 2026
│   ├── index.html
│   ├── committee/  speakers/  sponsors/  schedule_resumes/
│   └── logo-gastro.png  logo-nutri.png  favicon.svg
├── endogineco2026/            # Congresso Internacional Endogineco 2026
│   ├── index.html
│   ├── assets/  committee/  speakers/  organizers/  institutional-support/
│   ├── sponsors/  resumes/   # reserved for future client assets (may be empty)
│   ├── schedule/  pre-congress/  scientific-papers/  previous-edition/
│   └── scripts/               # Python schedule generators
├── oncoderma2026/             # II Simpósio Oncoderma Recife
│   ├── index.html
│   ├── assets/  committee/  speakers/  sponsors/  organizers/
│   ├── schedule/  resumes/
│   └── (…)
├── vercel.json                # Domain routing, redirects, and headers
├── DEPLOYMENT.md              # Deployment & DNS guide
└── PROJECT_STRUCTURE.md       # Routing & folder conventions
```

Each event folder is self-contained: images, PDFs, and data files live inside
that folder. There are no shared root-level assets. Some subfolders (e.g.
`endogineco2026/sponsors/`, `endogineco2026/resumes/`) are kept in the tree even
when empty, so incoming sponsor logos or speaker CVs have a defined place.

## Deployment

All sites deploy from a single Vercel project. Host-based rules in `vercel.json`
serve the correct event folder for each domain, and redirects keep the folder
name out of the public URL. See [DEPLOYMENT.md](DEPLOYMENT.md) for the full
guide.

**Setup summary**:

1. Push to the `main` branch (auto-deploys).
2. Add the custom domains in the Vercel Dashboard.
3. Point each domain's DNS to Vercel.
4. SSL certificates are provisioned automatically.

## Local Development

Open any site's `index.html` directly in a browser:

- Portfolio: `/portfolio/index.html`
- TGI: `/tgi/index.html`
- Gastro Conecta: `/gastroconecta2026/index.html`
- Endogineco 2026: `/endogineco2026/index.html`
- Oncoderma 2026: `/oncoderma2026/index.html`

Or run `vercel dev` to test host-based routing and redirects locally.

## Adding New Event Sites

1. Create a folder: `eventname/`
2. Copy an existing `index.html` as a template.
3. Update branding, colors, dates, and content.
4. Keep all assets inside the event folder and reference them with relative
   paths (e.g. `assets/logo.png`).
5. Add the host-based redirect and rewrite rules to `vercel.json`.
6. Configure the custom domain in the Vercel Dashboard.

See [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) for the routing conventions.
