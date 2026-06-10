# Project Structure & Routing

## Domain-Based Architecture

This project uses **separate custom domains** for each event, all deployed from a single repository. The root `index.html` serves as the Luka Plan portfolio on the default Vercel URL.

## Folder Structure

```
/
├── index.html                          # Luka Plan portfolio
├── tgi/
│   ├── index.html                      # III Simpósio TGI
│   ├── LOGO-TGI.png
│   └── assets/                         # TGI images, PDFs, sponsors
├── gastroconecta2026/
│   └── index.html                      # Gastro Conecta 2026
├── endogineco2026/
│   └── index.html                      # Congresso Endogineco 2026
├── oncoderma2026/
│   └── index.html                      # II Simpósio Oncoderma Recife
└── vercel.json                         # Domain routing config
```

## Domain Routing

Configured in `vercel.json` using host-based redirects:

| Domain                             | Serves          | File                            |
| ---------------------------------- | --------------- | ------------------------------- |
| `tgirecife.com.br`                 | TGI             | `/tgi/index.html`               |
| `www.tgirecife.com.br`             | TGI             | `/tgi/index.html`               |
| `gastroconecta2026.com.br`         | Gastro Conecta  | `/gastroconecta2026/index.html` |
| `congressoendoginecorecife.com.br` | Endogineco 2026 | `/endogineco2026/index.html`    |
| `oncodermarecife2026.com.br`       | Oncoderma 2026  | `/oncoderma2026/index.html`     |
| `*.vercel.app` (default)           | Portfolio       | `/index.html`                   |

## Path Strategy

**Use relative paths within each event folder:**

- ✅ `assets/logo.png` (TGI: inside `/tgi/`)
- ✅ `sponsors/logo.png` (Gastro: inside `/gastroconecta2026/`)
- ✅ `/gastroconecta2026/image.jpg` (absolute, only when linking across folders)
- ❌ `../assets/logo.png` (breaks with domain routing)

When a custom domain is configured, Vercel redirects `example.com/path` to `/eventfolder/path` internally. Relative paths in the event `index.html` resolve correctly on the custom domain.

## Adding New Event Sites

1. **Create folder**: `eventname/`
2. **Copy template**: Use existing `index.html`
3. **Update content**: Branding, colors, dates, etc.
4. **Fix paths**: Use relative paths within the event folder
5. **Add routing**: Update `vercel.json`:
   ```json
   {
     "source": "/:path((?!eventname).*)*",
     "has": [{ "type": "host", "value": "eventname.com.br" }],
     "destination": "/eventname/:path*",
     "permanent": false
   }
   ```
6. **Configure domain**: Add in Vercel Dashboard

## Asset Organization

- **Per event** (e.g. `/tgi/assets/`, `/gastroconecta2026/sponsors/`): Event-specific images, PDFs, schedules
- **No shared root assets**: Each event is self-contained in its folder
