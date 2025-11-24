# Project Structure & Routing

## Domain-Based Architecture

This project uses **separate custom domains** for each event, all deployed from a single repository.

## Folder Structure

```
/
├── index.html                          # TGI site
├── gastroconecta2026/
│   ├── index.html                      # Gastro Conecta 2026 site
│   └── Save the date (Gastro & Nutri).jpg
├── assets/                             # Shared assets
│   ├── logos/                          # Organization logos
│   ├── speakers/                       # Speaker photos
│   ├── committee/                      # Committee photos
│   └── sponsors/                       # Sponsor logos
├── tgi/                                # TGI-specific assets
│   ├── LOGO-TGI.png
│   └── schedule/
└── vercel.json                         # Domain routing config
```

## Domain Routing

Configured in `vercel.json` using host-based rewrites:

| Domain                     | Serves         | File                            |
| -------------------------- | -------------- | ------------------------------- |
| `www.tgirecife.com.br`     | TGI            | `/index.html`                   |
| `gastroconecta2026.com.br` | Gastro Conecta | `/gastroconecta2026/index.html` |

## Path Strategy

**Use absolute paths from root:**

- ✅ `/assets/logos/logo.png` (works for all domains)
- ✅ `/tgi/LOGO-TGI.png` (TGI-specific)
- ✅ `/gastroconecta2026/image.jpg` (Gastro-specific)
- ❌ `../assets/logo.png` (breaks with domain routing)

## Adding New Event Sites

1. **Create folder**: `eventname/`
2. **Copy template**: Use existing `index.html`
3. **Update content**: Branding, colors, dates, etc.
4. **Fix paths**: Use absolute paths (`/assets/`)
5. **Add routing**: Update `vercel.json`:
   ```json
   {
     "source": "/(.*)",
     "has": [{ "type": "host", "value": "eventname.com.br" }],
     "destination": "/eventname/index.html"
   }
   ```
6. **Configure domain**: Add in Vercel Dashboard

## Asset Organization

- **Shared** (`/assets/`): Used across multiple events
- **Event-specific** (e.g., `/tgi/`, `/gastroconecta2026/`): Event logos, schedules
