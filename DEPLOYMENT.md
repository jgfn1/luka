# Deployment Guide

Complete guide for deploying multiple event sites with custom domains on Vercel.

## Overview

- Single Vercel project serves multiple custom domains
- Domain-based routing in `vercel.json`
- Automatic deployments on push to `main`

## Domains

| Domain                     | Site           | File                            |
| -------------------------- | -------------- | ------------------------------- |
| `www.tgirecife.com.br`     | TGI            | `/index.html`                   |
| `gastroconecta2026.com.br` | Gastro Conecta | `/gastroconecta2026/index.html` |

## Setup Steps

### 1. Deploy to Vercel

```bash
# First time
vercel

# Subsequent deploys
git push origin main  # Auto-deploys
```

### 2. Add Custom Domains

In Vercel Dashboard:

1. Go to **Project Settings** → **Domains**
2. Click **Add Domain**
3. Add each domain:
   - `tgirecife.com.br` + `www.tgirecife.com.br`
   - `gastroconecta2026.com.br` + `www.gastroconecta2026.com.br`

### 3. Configure DNS

For each domain, add DNS records:

**CNAME (Recommended)**

```
Type: CNAME
Name: @ or leave blank
Value: cname.vercel-dns.com
```

**A Record (Alternative)**

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

- Vercel auto-provisions SSL certificates
- Takes 5-10 minutes after DNS is configured
- HTTPS enabled automatically

## How It Works

### Domain Routing

`vercel.json` uses host-based rewrites:

```json
{
  "rewrites": [
    {
      "source": "/(.*)",
      "has": [{ "type": "host", "value": "gastroconecta2026.com.br" }],
      "destination": "/gastroconecta2026/index.html"
    }
  ]
}
```

### Asset Paths

Use **absolute paths** from root:

- ✅ `/assets/logo.png`
- ✅ `/tgi/schedule.pdf`
- ❌ `../assets/logo.png`

## Troubleshooting

### Domain Not Resolving

- Check DNS records point to Vercel
- Wait up to 48 hours for DNS propagation
- Verify domain added in Vercel dashboard
- Run: `dig yourdomain.com.br`

### SSL Certificate Issues

- Wait 10-15 minutes after adding domain
- Check certificate status in Vercel dashboard
- Ensure DNS is correct
- Try clearing Vercel cache

### 404 Errors

- Verify routing in `vercel.json`
- Check file paths are correct
- Ensure domain is added in Vercel
- Check browser console for errors

### Asset Loading Issues

- Use absolute paths (`/assets/`)
- Check browser Network tab for 404s
- Verify assets exist in correct location
- Clear browser cache

## Local Testing

```bash
# Start local dev server
vercel dev

# Access at localhost:3000
# Or modify /etc/hosts to test domain routing:
# 127.0.0.1 gastroconecta2026.com.br
# 127.0.0.1 tgirecife.com.br
```

## Build Configuration

- **Framework**: Other (static HTML)
- **Build Command**: None
- **Output Directory**: `.` (root)
- **Install Command**: None
