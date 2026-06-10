# Luka Plan Event Websites

Multi-site repository for event landing pages. Each event has its own custom domain.

## Active Projects

### III Simpósio TGI

- **Domain**: [www.tgirecife.com.br](https://www.tgirecife.com.br/)
- **Date**: October 31 - November 1, 2025
- **Location**: Novotel Recife Marina
- **File**: `/tgi/index.html`

### Gastro Conecta 2026

- **Domain**: [gastroconecta2026.com.br](http://gastroconecta2026.com.br/)
- **Date**: March 27, 2026
- **File**: `/gastroconecta2026/index.html`

### Congresso Endogineco 2026

- **Domain**: [www.congressoendoginecorecife.com.br](https://www.congressoendoginecorecife.com.br/)
- **Date**: 27–29 de agosto de 2026
- **File**: `/endogineco2026/index.html`

### II Simpósio Oncoderma Recife

- **Domain**: [www.oncodermarecife2026.com.br](https://www.oncodermarecife2026.com.br/)
- **Date**: June 5, 2026
- **File**: `/oncoderma2026/index.html`

## Tech Stack

- Pure HTML5/CSS3/Vanilla JavaScript
- No framework dependencies
- Multi-language support (PT, EN, ES, FR) on selected sites
- Fully responsive design
- Domain-based routing via Vercel

## Project Structure

```
/
├── portfolio/                 # Luka Plan portfolio (default Vercel URL)
│   └── index.html
├── tgi/                       # III Simpósio TGI (tgirecife.com.br)
│   ├── index.html
│   ├── LOGO-TGI.png
│   └── assets/
├── gastroconecta2026/         # Gastro Conecta 2026
├── endogineco2026/            # Congresso Endogineco 2026
├── oncoderma2026/             # II Simpósio Oncoderma Recife
└── vercel.json                # Domain routing config
```

## Deployment

All sites deploy from a single Vercel project. Domain-based routing serves the correct site based on the domain.

**Setup**:

1. Push to `main` branch
2. Add custom domains in Vercel Dashboard
3. Configure DNS to point to Vercel
4. SSL certificates are automatic

## Local Development

Open HTML files directly in browser:

- Portfolio: `/portfolio/index.html`
- TGI: `/tgi/index.html`
- Gastro Conecta: `/gastroconecta2026/index.html`
- Endogineco 2026: `/endogineco2026/index.html`
- Oncoderma 2026: `/oncoderma2026/index.html`

Or use `vercel dev` for domain routing testing.

## Adding New Event Sites

1. Create folder: `eventname/`
2. Copy existing `index.html` as template
3. Update branding, colors, content
4. Use relative paths within the event folder (e.g. `assets/logo.png`)
5. Add domain routing to `vercel.json`
6. Configure custom domain in Vercel

## Contact

**Luka Plan Promoções e Eventos**

- Email: eventos@lukaplan.com.br
- Instagram: [@lukaplan\_](https://instagram.com/lukaplan_)
