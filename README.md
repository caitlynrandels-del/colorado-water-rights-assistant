# Colorado Water Rights Research Assistant

A clean, professional research tool for Colorado water rights attorneys and practitioners. It provides fast search of decreed water rights and current administrative calls using the official Colorado Division of Water Resources (DWR) / CDSS public REST API.

**Not affiliated with the State of Colorado. Not legal advice.**

## Features

- Search decreed water rights (Net Amounts) by WDID, structure name, county, or water source
- View statewide active administrative calls
- Local browser watchlist
- Direct links to official DWR detail pages
- Professional, mobile-friendly interface
- Clear disclaimer and links to official resources

## Quick Start (Local)

1. Download `index.html`
2. Open it in any modern browser
3. Search (example: WDID `2400586` or structure name “Peoples”)

**Note:** The browser version uses a free public CORS proxy so it can call the DWR API. For the most reliable experience, deploy it as a real website (see below) or run the optional local server.

## Deploy as a Real Website (Recommended)

This is a pure static site. You can host it for free in a few minutes:

### Easiest options (2026)
- **Netlify Drop** — Drag the folder (or just `index.html`) onto [https://app.netlify.com/drop](https://app.netlify.com/drop). Instant live URL. Claim with a free account for a permanent site.
- **Cloudflare Pages** — Best long-term free option (unlimited static bandwidth). Connect a GitHub repo or upload directly.
- **GitHub Pages** — Push to a public repository and enable Pages. Free custom domain supported.
- **Vercel** — Simple for personal use (Hobby plan is non-commercial).

After deployment you get a real HTTPS URL you can bookmark, share, or put on a custom domain.

### Optional: Local Server (No CORS Proxy)

If you want the most reliable API access without relying on a public proxy, use the included Python server:

```bash
pip install flask flask-cors requests
python server.py
```

Then open `http://localhost:5000`.

## Official Data Sources

- [DWR Online Tools](https://dwr.state.co.us/Tools)
- [CDSS](https://cdss.colorado.gov/)
- [CDSS REST API Help](https://dwr.state.co.us/Rest/GET/Help)
- [cowaterrights.com](https://cowaterrights.com/) (excellent free guide)

## Disclaimer

This tool is for research convenience only. Always verify information in official DWR records and water court decrees, and consult a licensed Colorado water rights attorney for legal advice. Data is provided by the State of Colorado and is used here under the public API terms.

---

Built as a finished research assistant for professional use. Feel free to customize the branding, add your firm name, or extend the features.
