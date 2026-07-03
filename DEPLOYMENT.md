# Deployment Guide

Complete guide for deploying the event sites with custom domains on Vercel.

## Overview

- A **single Vercel project** serves multiple custom domains plus the portfolio.
- Routing is configured entirely in `vercel.json`:
  - **Rewrites** map each domain (host) to its event folder.
  - **Redirects** strip the folder name from the public URL on custom domains.
  - **Headers** add baseline security headers to every response.
- The portfolio lives in `/portfolio/` (there is no root `index.html`) so the
  host-based rules work cleanly on custom domains. In production the default URL
  is [automaitdev.vercel.app](https://automaitdev.vercel.app/); preview deploys on
  other `*.vercel.app` hostnames also serve the portfolio.
- `cleanUrls` is enabled and `trailingSlash` is disabled.
- Deployments run automatically on push to `main`.

## Domains

| Domain                                | Site            | Folder                |
| ------------------------------------- | --------------- | --------------------- |
| `tgirecife.com.br`                    | TGI             | `/tgi/`               |
| `www.tgirecife.com.br`                | TGI             | `/tgi/`               |
| `gastroconecta2026.com.br`            | Gastro Conecta  | `/gastroconecta2026/` |
| `www.gastroconecta2026.com.br`        | Gastro Conecta  | `/gastroconecta2026/` |
| `congressoendoginecorecife.com.br`    | Endogineco 2026 | `/endogineco2026/`    |
| `www.congressoendoginecorecife.com.br`| Endogineco 2026 | `/endogineco2026/`    |
| `oncodermarecife2026.com.br`          | Oncoderma 2026  | `/oncoderma2026/`     |
| `www.oncodermarecife2026.com.br`      | Oncoderma 2026  | `/oncoderma2026/`     |
| `spmpq.com.br`                        | SPMPQ 2026      | `/spmpq/`             |
| `www.spmpq.com.br`                    | SPMPQ 2026      | `/spmpq/`             |
| `recifetorax2026.com.br`              | Recife Tórax 2026 | `/recifetorax2026/` |
| `www.recifetorax2026.com.br`          | Recife Tórax 2026 | `/recifetorax2026/` |
| `automaitdev.vercel.app`              | Portfolio       | `/portfolio/`         |
| `*.vercel.app` (other preview URLs)   | Portfolio       | `/portfolio/`         |

## Setup Steps

### 1. Deploy to Vercel

```bash
# First time
vercel

# Subsequent deploys
git push origin main  # Auto-deploys
```

### 2. Add Custom Domains

In the Vercel Dashboard:

1. Go to **Project Settings** → **Domains**.
2. Click **Add Domain**.
3. Add each domain (apex + `www.`):
   - `tgirecife.com.br` + `www.tgirecife.com.br`
   - `gastroconecta2026.com.br` + `www.gastroconecta2026.com.br`
   - `congressoendoginecorecife.com.br` + `www.congressoendoginecorecife.com.br`
   - `oncodermarecife2026.com.br` + `www.oncodermarecife2026.com.br`
   - `spmpq.com.br` + `www.spmpq.com.br`
   - `recifetorax2026.com.br` + `www.recifetorax2026.com.br`

> Any domain or rule you add in the Dashboard must also have matching rewrite and
> redirect entries in `vercel.json` (see "Adding a New Domain" below).

### 3. Configure DNS

For each domain, add DNS records:

**CNAME (recommended)**

```
Type: CNAME
Name: @ or leave blank
Value: cname.vercel-dns.com
```

**A Record (alternative)**

```
Type: A
Name: @
Value: 76.76.21.21
```

**WWW Subdomain**

```
Type: CNAME
Name: www
Value: cname.vercel-dns.com
```

### 4. Wait for SSL

- Vercel auto-provisions SSL certificates.
- This usually takes 5–10 minutes after DNS is configured.
- HTTPS is enabled automatically.

## How It Works

### Rewrites (host → folder)

`vercel.json` uses host-based rewrites so the URL stays clean on the custom
domain:

```json
{
  "source": "/:path((?!tgi).*)*",
  "has": [{ "type": "host", "value": "www.tgirecife.com.br" }],
  "destination": "/tgi/:path*"
}
```

### Redirects (strip folder name)

Matching redirects ensure the folder name never appears in the public URL:

```json
{ "source": "/tgi", "has": [{ "type": "host", "value": "tgirecife.com.br" }], "destination": "/", "permanent": true },
{ "source": "/tgi/:path*", "has": [{ "type": "host", "value": "tgirecife.com.br" }], "destination": "/:path*", "permanent": true }
```

### Security Headers

Applied to every response (`source: "/(.*)"`):

```json
{ "key": "X-Content-Type-Options", "value": "nosniff" },
{ "key": "X-Frame-Options", "value": "DENY" },
{ "key": "X-XSS-Protection", "value": "1; mode=block" }
```

### Asset Paths

Use **relative paths within each event folder**:

- ✅ `assets/logo.png` (inside `/tgi/`, served as `tgirecife.com.br/assets/logo.png`)
- ✅ `sponsors/logo.png` (inside `/gastroconecta2026/`)
- ❌ `../assets/logo.png`

## Adding a New Domain

For a new event domain, add both a rewrite and the two redirects for each host
(apex and `www.`):

```json
// rewrite
{
  "source": "/:path((?!eventname).*)*",
  "has": [{ "type": "host", "value": "eventname.com.br" }],
  "destination": "/eventname/:path*"
}

// redirects
{ "source": "/eventname", "has": [{ "type": "host", "value": "eventname.com.br" }], "destination": "/", "permanent": true },
{ "source": "/eventname/:path*", "has": [{ "type": "host", "value": "eventname.com.br" }], "destination": "/:path*", "permanent": true }
```

Then add the domain in the Vercel Dashboard and configure its DNS.

## Troubleshooting

### Domain Not Resolving

- Check DNS records point to Vercel.
- Wait up to 48 hours for DNS propagation.
- Verify the domain is added in the Vercel Dashboard.
- Run: `dig yourdomain.com.br`.

### SSL Certificate Issues

- Wait 10–15 minutes after adding the domain.
- Check the certificate status in the Vercel Dashboard.
- Ensure DNS is correct.

### 404 Errors

- Verify the rewrite/redirect rules in `vercel.json`.
- Check that file paths are correct.
- Ensure the domain is added in Vercel.
- Check the browser console for errors.

### Asset Loading Issues

- Use relative paths within the event folder.
- Check the browser Network tab for 404s.
- Verify assets exist in the correct location.
- Clear the browser cache.

## Local Testing

```bash
# Start local dev server
vercel dev

# Portfolio: http://localhost:3000/  (or automaitdev.vercel.app in production)
# Or modify /etc/hosts to test domain routing:
# 127.0.0.1 tgirecife.com.br
# 127.0.0.1 www.tgirecife.com.br
# 127.0.0.1 gastroconecta2026.com.br
# 127.0.0.1 congressoendoginecorecife.com.br
# 127.0.0.1 www.oncodermarecife2026.com.br
# 127.0.0.1 www.spmpq.com.br
# 127.0.0.1 www.recifetorax2026.com.br
```

## Build Configuration

- **Framework**: Other (static HTML)
- **Build Command**: None
- **Output Directory**: `.` (repository root)
- **Install Command**: None
