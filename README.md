# Luka Plan Event Websites

Multi-site repository of landing pages for medical and scientific events. Each
event is a self-contained static site served from its own custom domain, and all
sites are deployed from this single repository on Vercel.

The sites are developed by **Automa IT & Development** for the client
**Luka Plan Promoções e Eventos**, the producer of the events.

## Active Projects

### III Simpósio TGI

- **Domain**: [www.tgirecife.com.br](https://www.tgirecife.com.br/)
- **Topic**: Gastrointestinal oncology
- **Date**: October 31 – November 1, 2025
- **Location**: Novotel Recife Marina
- **Folder**: `/tgi/`
- **Languages**: PT, EN, ES, FR

### Gastro Conecta & Nutri Conecta 2026

- **Domain**: [gastroconecta2026.com.br](https://www.gastroconecta2026.com.br/)
- **Topic**: Gastrointestinal tract and nutrition
- **Date**: March 27, 2026
- **Location**: Novotel Recife Marina
- **Folder**: `/gastroconecta2026/`
- **Languages**: PT, EN, FR

### II Simpósio Oncoderma Recife

- **Domain**: [www.oncodermarecife2026.com.br](https://www.oncodermarecife2026.com.br/)
- **Topic**: Cutaneous oncology
- **Date**: June 5, 2026
- **Location**: Hospital Santa Joana Recife
- **Folder**: `/oncoderma2026/`
- **Languages**: PT

### Congresso Internacional Endogineco 2026

- **Domain**: [www.congressoendoginecorecife.com.br](https://www.congressoendoginecorecife.com.br/)
- **Topic**: Gynecology and endoscopy
- **Date**: August 27–29, 2026
- **Location**: Recife
- **Folder**: `/endogineco2026/`
- **Languages**: PT

### Portfolio (Automa IT & Development)

- **Default domain**: served on the project's `*.vercel.app` URL
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
├── portfolio/                 # Automa IT & Development portfolio (default Vercel URL)
│   └── index.html
├── tgi/                       # III Simpósio TGI (tgirecife.com.br)
│   ├── index.html
│   ├── LOGO-TGI.png
│   └── assets/                # committee, speakers, sponsors, logos, PDFs
├── gastroconecta2026/         # Gastro Conecta & Nutri Conecta 2026
│   ├── index.html
│   ├── committee/  speakers/  sponsors/  schedule_resumes/
│   └── logos & favicon
├── endogineco2026/            # Congresso Internacional Endogineco 2026
│   ├── index.html
│   ├── committee/  speakers/  organizers/  institutional-support/
│   ├── schedule/  pre-congress/  scientific-papers/  previous-edition/
│   └── scripts/               # Python schedule generators
├── oncoderma2026/             # II Simpósio Oncoderma Recife
│   ├── index.html
│   ├── committee/  speakers/  sponsors/  organizers/  schedule/  resumes/
│   └── assets/
├── vercel.json                # Domain routing, redirects, and headers
├── DEPLOYMENT.md              # Deployment & DNS guide
└── PROJECT_STRUCTURE.md       # Routing & folder conventions
```

Each event folder is self-contained: all of its images, PDFs, and data files
live inside that folder, and there are no shared root-level assets.

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

## Contact

**Client — Luka Plan Promoções e Eventos**

- Email: eventos@lukaplan.com.br
- Instagram: [@lukaplan\_](https://instagram.com/lukaplan_)

**Developer — Automa IT & Development**

- WhatsApp: [+55 81 99546-0140](https://wa.me/5581995460140)
