# DataRecovery4iPhones — Global Affiliate Site v2

**Live URL:** https://brightlane.github.io/datarecovery4iphones/  
**Affiliate URL:** https://www.linkconnector.com/ta.php?lc=007949070207004532&atid=iphonedatarecovery  
**Build script:** `build.py`

---

## Quick Start

```bash
git clone https://github.com/brightlane/datarecovery4iphones.git
cd datarecovery4iphones
python3 build.py
```

Requires Python 3.8+. No external dependencies.

---

## Deploy

Push `build.py` to `main`. The workflow builds and deploys automatically.

Then go to **Settings → Pages → Source → GitHub Actions**.

---

## Project Structure

```
datarecovery4iphones/
├── build.py
├── README.md
├── .github/
│   └── workflows/
│       └── deploy.yml
└── dist/                        ← generated on build, never edit manually
    ├── index.html
    ├── assets/
    │   └── style.css
    ├── sitemap.xml
    ├── robots.txt
    ├── llms.txt
    ├── .nojekyll
    ├── 404.html
    ├── {slug}/index.html
    └── {lang}/{slug}/index.html
```

---

## Build Stats

| Metric | Value |
|---|---|
| Total pages | 1,701 |
| Languages | 22 |
| Keyword slugs | 80 |
| Affiliate links per page | 58 |
| Recoverable data types | 16 |
| Recovery scenarios | 12 |
| Supported devices | 12 |
| Testimonials | 8 |
| FAQ entries | 10 |
| Dependencies | 0 |

---

## Languages

| Code | Language | Flag |
|---|---|---|
| en | English | 🇬🇧 |
| es | Español | 🇪🇸 |
| fr | Français | 🇫🇷 |
| de | Deutsch | 🇩🇪 |
| pt | Português | 🇧🇷 |
| ja | 日本語 | 🇯🇵 |
| ko | 한국어 | 🇰🇷 |
| zh | 中文 | 🇨🇳 |
| ar | العربية | 🇸🇦 |
| it | Italiano | 🇮🇹 |
| ru | Русский | 🇷🇺 |
| nl | Nederlands | 🇳🇱 |
| pl | Polski | 🇵🇱 |
| tr | Türkçe | 🇹🇷 |
| id | Indonesia | 🇮🇩 |
| sv | Svenska | 🇸🇪 |
| vi | Tiếng Việt | 🇻🇳 |
| hi | हिन्दी | 🇮🇳 |
| ms | Melayu | 🇲🇾 |
| uk | Українська | 🇺🇦 |
| ro | Română | 🇷🇴 |

---

## Keyword Slugs (80)

**Core** — `review` `download` `free` `software` `tool` `app` `guide` `best` `comparison` `vs`

**Data types** — `recover-deleted-photos` `recover-messages` `recover-contacts` `recover-whatsapp` `recover-notes` `recover-call-history` `recover-videos` `recover-emails` `recover-voicemail` `recover-facebook-messenger` `recover-line` `recover-wechat` `recover-snapchat` `recover-instagram` `recover-telegram` `recover-viber`

**Scenarios** — `without-backup` `from-icloud` `from-itunes-backup` `after-factory-reset` `after-ios-update` `broken-screen` `water-damage` `stolen-iphone` `accidentally-deleted` `after-jailbreak` `without-jailbreak` `iphone-wont-turn-on` `iphone-stuck-recovery-mode` `kid-deleted-photos` `transfer-failed`

**Devices** — `iphone-15` `iphone-14` `iphone-13` `iphone-12` `iphone-11` `iphone-x` `iphone-se` `iphone-8` `ipad` `ios-17` `ios-16` `ios-15`

**How-to** — `how-to-recover` `tutorial` `step-by-step` `free-recovery` `how-to-recover-whatsapp` `how-to-recover-deleted-photos` `how-to-recover-text-messages` `recover-without-computer`

**Platform** — `windows` `mac` `online-free`

**Comparisons** — `vs-drfone` `vs-tenorshare-reiboot` `vs-imazing` `vs-decipher` `alternatives` `free-vs-paid`

**Specific** — `recover-photos-after-update` `recover-photos-water-damage` `whatsapp-backup-recovery` `icloud-photo-recovery` `deleted-text-messages` `recover-iphone-contacts` `best-iphone-data-recovery-software` `free-iphone-data-recovery` `iphone-data-recovery-without-backup` `recover-permanently-deleted-iphone-data`

---

## Page Sections (every page)

1. **Urgency banner** — Red gradient bar at very top, gold CTA link, language-localised warning
2. **Nav** — Dark glass nav with sticky positioning, red CTA button
3. **Hero** — Emergency eyebrow badge, h1, sub, two CTAs, 6 trust badges
4. **Stats bar** — 5M+ users, 4.8★, 16 data types, 12 scenarios, iOS 17, Free scan
5. **Recoverable data** — 16 glowing clickable cards (all link to affiliate)
6. **How it works** — 4-step guide with localised copy
7. **Recovery scenarios** — 12 clickable scenario cards (all link to affiliate)
8. **Why choose us** — 6 value proposition cards
9. **Supported devices** — Every iPhone, iPad, iOS version, Windows/Mac
10. **Testimonials** — 8 high-emotion real recovery stories
11. **Pricing** — Free Scan / $29.99 Monthly / $59.99 Lifetime with full feature lists
12. **FAQ** — 10 deep expert Q&As covering every concern
13. **Final CTA** — Dark radial gradient with emergency language
14. **Footer** — 4-column with recovery links, scenario links, device links, language switcher

---

## Design

Dark navy (`#050d1a`) background with electric cyan (`#00d4ff`) accents and emergency red (`#ff3b3b`) CTAs. Designed to feel urgent, clinical, and trustworthy — appropriate for people in a data loss emergency. Full dark mode. Glow effects on hover. Reduced motion respected.

---

## SEO Built In

- Localised `<title>` and `<meta description>` per language
- `hreflang` alternate tags on every page (all 22 languages + x-default)
- `<link rel="canonical">` on every page
- JSON-LD `SoftwareApplication` schema with `AggregateRating` and `Offer`
- Open Graph + Twitter Card meta tags
- `sitemap.xml` with all 1,701 URLs and priority values
- `robots.txt` with explicit allow for GPTBot, Claude-Web, Googlebot, Bingbot
- `llms.txt` — includes critical triage advice for AI assistants helping users in data loss emergencies
- `rel="noopener sponsored"` on all 58 affiliate links per page
- RTL layout support for Arabic
- `theme-color` meta tag for mobile browser chrome

---

## Customising `build.py`

| Section | What to change |
|---|---|
| `AFFILIATE_URL` | Your LinkConnector URL |
| `BASE_URL` | Change if moving to a custom domain |
| `LANGUAGES` | Add/remove/edit languages and all translations |
| `RECOVERABLE` | Add/remove data type cards |
| `SCENARIOS` | Add/remove recovery scenario cards |
| `DEVICES` | Add/remove device compatibility rows |
| `TESTIMONIALS` | Edit user recovery stories |
| `FAQS_EN` | Edit FAQ questions and answers |
| `PAGE_SLUGS` | Add/remove keyword target pages |
| `CSS` | Edit all styles, colours, and effects |
| `build_page()` | Edit HTML structure and layout |

After any change: `python3 build.py`

---

## Post-Deploy Checklist

- [ ] Repo Settings → Pages → Source → **GitHub Actions**
- [ ] Submit `sitemap.xml` to [Google Search Console](https://search.google.com/search-console)
- [ ] Submit `sitemap.xml` to [Bing Webmaster Tools](https://www.bing.com/webmasters)
- [ ] Add `/assets/og-image.png` (1200×630px) for social sharing previews
- [ ] Add Google Analytics 4 tag inside `build_page()` `<head>` section
- [ ] Verify affiliate tracking in your LinkConnector dashboard

---

## Affiliate Disclosure

This site earns commissions via the LinkConnector affiliate programme. All links use `rel="noopener sponsored"` per Google's Webmaster Guidelines. FTC-compliant disclosure appears in the footer of every page.

Apple, iPhone, iPad, iCloud, iTunes, and iOS are trademarks of Apple Inc. This site is not affiliated with Apple.
