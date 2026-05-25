from pathlib import Path
from datetime import date, timedelta
from xml.etree.ElementTree import Element, SubElement, tostring
from html import escape
import re

BASE_URL = "https://brightlane.github.io/crossout/"
OUT = Path("docs")
AFFILIATE = "https://unbounce.partnerlinks.io/q0s9bd15hjtx"
SITE_NAME = "Crossout"
BLOG_DAYS = 60

PAGES = [
    {
        "slug": "",
        "title": "Unbounce Landing Page Reviews and Guides",
        "desc": "Affiliate site for Unbounce reviews, comparisons, pricing, and landing page conversion tips.",
        "keyword": "unbounce landing page builder",
        "robots": "index,follow",
    },
    {
        "slug": "unbounce-review",
        "title": "Unbounce Review",
        "desc": "A practical review of Unbounce for landing pages and conversion-focused campaigns.",
        "keyword": "unbounce review",
        "robots": "index,follow",
    },
    {
        "slug": "unbounce-pricing",
        "title": "Unbounce Pricing",
        "desc": "Unbounce pricing, trial details, and plan fit for marketers and agencies.",
        "keyword": "unbounce pricing",
        "robots": "index,follow",
    },
    {
        "slug": "unbounce-features",
        "title": "Unbounce Features",
        "desc": "Landing pages, A/B testing, Smart Traffic, and integrations in Unbounce.",
        "keyword": "unbounce features",
        "robots": "index,follow",
    },
    {
        "slug": "unbounce-vs-leadpages",
        "title": "Unbounce vs Leadpages",
        "desc": "Compare two landing page builders for conversion-focused use cases.",
        "keyword": "unbounce vs leadpages",
        "robots": "index,follow",
    },
    {
        "slug": "unbounce-vs-clickfunnels",
        "title": "Unbounce vs ClickFunnels",
        "desc": "Choose between landing page optimization and full funnel software.",
        "keyword": "unbounce vs clickfunnels",
        "robots": "index,follow",
    },
    {
        "slug": "best-landing-page-builder",
        "title": "Best Landing Page Builder",
        "desc": "Find the best landing page builder for lead gen and paid traffic.",
        "keyword": "best landing page builder",
        "robots": "index,follow",
    },
    {
        "slug": "landing-page-cro",
        "title": "Landing Page CRO Guide",
        "desc": "Practical conversion rate optimization advice for landing pages.",
        "keyword": "landing page cro",
        "robots": "index,follow",
    },
    {
        "slug": "agency-playbook",
        "title": "Agency Playbook",
        "desc": "How agencies can use Unbounce for client landing pages and campaigns.",
        "keyword": "unbounce agency",
        "robots": "index,follow",
    },
    {
        "slug": "start-here",
        "title": "Start Here",
        "desc": "The fastest path to trying Unbounce and building your first page.",
        "keyword": "try unbounce",
        "robots": "index,follow",
    },
]

NAV = [
    ("Home", BASE_URL),
    ("Review", BASE_URL + "unbounce-review/"),
    ("Pricing", BASE_URL + "unbounce-pricing/"),
    ("Start Here", BASE_URL + "start-here/"),
]

def ensure(path):
    path.parent.mkdir(parents=True, exist_ok=True)

def canonical(slug):
    return BASE_URL if slug == "" else BASE_URL + slug + "/"

def safe(s):
    return escape(s, quote=True)

def render_template(title, desc, canonical_url, body, robots="index,follow"):
    nav = " | ".join([f'<a href="{u}">{n}</a>' for n, u in NAV])
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{safe(title)}</title>
<meta name="description" content="{safe(desc)}">
<link rel="canonical" href="{canonical_url}">
<meta name="robots" content="{robots}">
<meta property="og:type" content="website">
<meta property="og:title" content="{safe(title)}">
<meta property="og:description" content="{safe(desc)}">
<meta property="og:url" content="{canonical_url}">
<meta property="og:site_name" content="{SITE_NAME}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{safe(title)}">
<meta name="twitter:description" content="{safe(desc)}">
<link rel="stylesheet" href="{BASE_URL}assets/style.css">
</head>
<body>
<header><nav>{nav}</nav></header>
<main>
{body}
</main>
<footer>
  <p>Affiliate disclosure: some links are sponsored/affiliate links.</p>
</footer>
</body>
</html>'''

def home_body():
    links = "".join([f'<li><a href="{canonical(p["slug"])}">{safe(p["title"])}</a></li>' for p in PAGES[1:]])
    return f'''
<h1>Unbounce affiliate site</h1>
<p>Built to convert search traffic into trial clicks and signups using comparison pages, reviews, and daily blog posts.</p>
<p><a href="{AFFILIATE}" rel="sponsored nofollow">Start Unbounce free trial</a></p>
<h2>Core pages</h2>
<ul>{links}</ul>
<h2>Why Unbounce</h2>
<p>Unbounce focuses on landing page creation, A/B testing, and optimization features for marketers.</p>
'''

def inner_body(title, keyword):
    return f'''
<h1>{safe(title)}</h1>
<p>Target keyword: <strong>{safe(keyword)}</strong></p>
<p>Use this page to explain the problem, the solution, and why Unbounce is a strong fit.</p>
<p><a href="{AFFILIATE}" rel="sponsored nofollow">Try Unbounce now</a></p>
<h2>Use cases</h2>
<ul>
<li>Lead generation.</li>
<li>Agency client landing pages.</li>
<li>Paid traffic conversion optimization.</li>
</ul>
'''

def blog_index(posts):
    items = "".join([f'<li><a href="{BASE_URL}blog/{p["slug"]}/">{safe(p["title"])}</a> — {p["date"]}</li>' for p in posts])
    return f"<h1>Blog</h1><p>Fresh daily posts about landing pages, CRO, and paid traffic.</p><ul>{items}</ul>"

def blog_post(title, date_str, excerpt, affiliate_link):
    return f'''
<h1>{safe(title)}</h1>
<p>{date_str}</p>
<p>{safe(excerpt)}</p>
<p><a href="{affiliate_link}" rel="sponsored nofollow">Start your Unbounce trial</a></p>
'''

def build_sitemap(urls):
    root = Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
    for u in urls:
        url = SubElement(root, "url")
        SubElement(url, "loc").text = u
        SubElement(url, "lastmod").text = date.today().isoformat()
    return '<?xml version="1.0" encoding="UTF-8"?>\n' + tostring(root, encoding="unicode")

def make_blog_posts():
    posts = []
    today = date.today()
    for i in range(BLOG_DAYS):
        d = today - timedelta(days=i)
        slug = d.isoformat()
        title = f"{d:%B %d, %Y} — Landing Page Tip"
        excerpt = (
            "A short daily post about landing pages, CRO, and paid traffic performance. "
            "Use this space to explain one tactic, one example, and one reason Unbounce can help."
        )
        posts.append({"slug": slug, "title": title, "date": d.isoformat(), "excerpt": excerpt})
    return posts

def build_og_image_stub():
    (OUT / "assets").mkdir(parents=True, exist_ok=True)
    css = """
body{font-family:system-ui,-apple-system,Segoe UI,Roboto,sans-serif;max-width:900px;margin:40px auto;padding:0 16px;line-height:1.6;color:#111}
nav a{margin-right:12px}
a{color:#0b57d0}
h1,h2,h3{line-height:1.2}
code,pre{background:#f6f8fa;border-radius:8px}
footer{margin-top:40px;padding-top:20px;border-top:1px solid #e5e7eb;color:#555}
"""
    (OUT / "assets" / "style.css").write_text(css, encoding="utf-8")

def main():
    OUT.mkdir(exist_ok=True)
    build_og_image_stub()
    urls = []

    for p in PAGES:
        slug = p["slug"]
        target_dir = OUT if slug == "" else OUT / slug
        ensure(target_dir / "index.html")
        body = home_body() if slug == "" else inner_body(p["title"], p["keyword"])
        html = render_template(
            p["title"],
            p["desc"],
            canonical(slug),
            body,
            robots=p["robots"],
        )
        (target_dir / "index.html").write_text(html, encoding="utf-8")
        urls.append(canonical(slug))

    posts = make_blog_posts()
    ensure(OUT / "blog" / "index.html")
    (OUT / "blog" / "index.html").write_text(
        render_template(
            "Blog",
            "Daily blog index for landing page, CRO, and affiliate content.",
            BASE_URL + "blog/",
            blog_index(posts),
        ),
        encoding="utf-8",
    )
    urls.append(BASE_URL + "blog/")

    for post in posts:
        post_dir = OUT / "blog" / post["slug"]
        ensure(post_dir / "index.html")
        html = render_template(
            post["title"],
            "Daily blog post",
            BASE_URL + f'blog/{post["slug"]}/',
            blog_post(post["title"], post["date"], post["excerpt"], AFFILIATE),
        )
        (post_dir / "index.html").write_text(html, encoding="utf-8")
        urls.append(BASE_URL + f'blog/{post["slug"]}/')

    (OUT / "404.html").write_text(
        render_template(
            "Page not found",
            "404 page for broken links and missing URLs.",
            BASE_URL + "404.html",
            '<h1>404</h1><p>That page does not exist.</p><p><a href="/crossout/">Go home</a></p>',
            robots="noindex,nofollow",
        ),
        encoding="utf-8",
    )

    (OUT / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\nSitemap: {BASE_URL}sitemap.xml\n",
        encoding="utf-8",
    )

    (OUT / "llms.txt").write_text(
        f"""# {SITE_NAME}
Site: {BASE_URL}
Topic: Unbounce affiliate pages, reviews, comparisons, landing page CRO, and daily blog posts.
Important URLs:
- {BASE_URL}
- {BASE_URL}unbounce-review/
- {BASE_URL}unbounce-pricing/
- {BASE_URL}start-here/
- {BASE_URL}blog/
""",
        encoding="utf-8",
    )

    (OUT / "sitemap.xml").write_text(build_sitemap(urls), encoding="utf-8")

if __name__ == "__main__":
    main()
