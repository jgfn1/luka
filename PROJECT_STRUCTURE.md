# Project Structure & Routing

## Domain-Based Architecture

This repository hosts **several independent event sites** plus a developer
portfolio, all deployed from a single Vercel project. Each event maps to its own
custom domain. The portfolio lives in `/portfolio/` (there is no root
`index.html`) and is served on the project's default `*.vercel.app` URL.

`vercel.json` does the routing in three layers:

1. **Rewrites** — map each custom domain (host) to its event folder internally,
   without changing the browser URL.
2. **Redirects** — strip the folder name from the public URL on custom domains
   (e.g. `tgirecife.com.br/tgi/x` → `tgirecife.com.br/x`).
3. **Headers** — apply baseline security headers to every response.

`cleanUrls` is enabled and `trailingSlash` is disabled.

## Folder Structure

```
/
├── portfolio/
│   └── index.html                      # Automa IT & Development portfolio (EN/PT/ES)
├── tgi/
│   ├── index.html                      # III Simpósio TGI
│   ├── LOGO-TGI.png
│   └── assets/
│       ├── committee/ speakers/ sponsors/ logos/
│       └── programacao_completa.pdf
├── gastroconecta2026/
│   ├── index.html                      # Gastro Conecta & Nutri Conecta 2026
│   ├── committee/ speakers/ sponsors/
│   ├── schedule_resumes/
│   └── logo-gastro.png  logo-nutri.png  favicon.svg
├── endogineco2026/
│   ├── index.html                      # Congresso Internacional Endogineco 2026
│   ├── assets/ committee/ speakers/ organizers/ institutional-support/
│   ├── sponsors/ resumes/              # reserved for future assets (may be empty)
│   ├── schedule/ (+ backup/)
│   ├── pre-congress/ scientific-papers/ previous-edition/
│   └── scripts/                        # Python schedule generators
├── oncoderma2026/
│   ├── index.html                      # II Simpósio Oncoderma Recife
│   ├── assets/ committee/ speakers/ sponsors/ organizers/
│   ├── schedule/ (+ backup/)
│   └── resumes/
└── vercel.json                         # Routing, redirects, and headers
```

## Domain Routing

Each custom domain is rewritten (host-based) to its event folder; the matching
default URL falls through to the portfolio:

| Domain                                                              | Serves          | Folder              |
| ------------------------------------------------------------------ | --------------- | ------------------- |
| `tgirecife.com.br`, `www.tgirecife.com.br`                         | TGI             | `/tgi/`             |
| `gastroconecta2026.com.br`, `www.gastroconecta2026.com.br`         | Gastro Conecta  | `/gastroconecta2026/` |
| `congressoendoginecorecife.com.br`, `www.…`                        | Endogineco 2026 | `/endogineco2026/`  |
| `oncodermarecife2026.com.br`, `www.oncodermarecife2026.com.br`     | Oncoderma 2026  | `/oncoderma2026/`   |
| `*.vercel.app` (default, incl. `automaitdev.vercel.app`)           | Portfolio       | `/portfolio/`       |

Redirects mirror these hosts to remove the folder prefix from public URLs, so
`tgirecife.com.br/tgi` and `tgirecife.com.br/tgi/<path>` permanently redirect to
`tgirecife.com.br/` and `tgirecife.com.br/<path>`.

## Path Strategy

**Use relative paths within each event folder:**

- ✅ `assets/logo.png` (TGI: inside `/tgi/`)
- ✅ `sponsors/logo.png` (Gastro: inside `/gastroconecta2026/`)
- ❌ `../assets/logo.png` (breaks with domain routing)

When a custom domain is configured, Vercel rewrites `example.com/path` to
`/eventfolder/path` internally without changing the browser URL. Relative paths
in the event's `index.html` therefore resolve correctly on the custom domain.

## Adding New Event Sites

1. **Create folder**: `eventname/`
2. **Copy template**: start from an existing `index.html`.
3. **Update content**: branding, colors, dates, speakers, etc.
4. **Fix paths**: keep all assets inside the event folder and use relative paths.
5. **Add a rewrite** (host → folder) to `vercel.json`:
   ```json
   {
     "source": "/:path((?!eventname).*)*",
     "has": [{ "type": "host", "value": "eventname.com.br" }],
     "destination": "/eventname/:path*"
   }
   ```
6. **Add the matching redirects** (strip the folder name from the public URL):
   ```json
   { "source": "/eventname", "has": [{ "type": "host", "value": "eventname.com.br" }], "destination": "/", "permanent": true },
   { "source": "/eventname/:path*", "has": [{ "type": "host", "value": "eventname.com.br" }], "destination": "/:path*", "permanent": true }
   ```
   Repeat both the rewrite and the redirects for the `www.` host.
7. **Configure the domain**: add it in the Vercel Dashboard.

## Asset Organization

- **Per event**: event-specific images, PDFs, and data files live in
  subfolders such as `committee/`, `speakers/`, `sponsors/`, `organizers/`,
  `schedule/`, `resumes/`, and `assets/`.
- **No shared root assets**: each event is fully self-contained in its folder.
- **Empty folders**: some directories (e.g. `endogineco2026/sponsors/`,
  `endogineco2026/resumes/`) are documented and kept in the repo even without
  files yet, so future sponsor logos or speaker CVs have a fixed location.

## Helper Scripts (Endogineco)

`endogineco2026/scripts/` contains Python utilities used to build the schedule
section of that site from CSV source files:

- `generate_schedule_html.py` — generates schedule table HTML from the
  `schedule/` and `pre-congress/` CSV files.
- `patch_schedule_in_index.py` — runs the generator and patches the rendered
  panels back into `endogineco2026/index.html`.

These scripts are authoring helpers only; they are not part of the Vercel build.
