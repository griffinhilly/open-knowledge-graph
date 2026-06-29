#!/usr/bin/env python3
"""Generate output/sitemap.xml and output/robots.txt.

purpose: SEO discovery surface — one <url> entry per main page, domain map,
         and topic detail page so search engines can index the full site.
inputs:  domains/*/_domain.yml (domain list), domains/*/*.md (topic IDs)
outputs: output/sitemap.xml, output/robots.txt
last_run: every CI deploy (.github/workflows/deploy-pages.yml)

Included: index, radial-graph, quiz, keystones, 19 domain maps, all topic pages.
Excluded by design: tag pages and per-topic question pages (list/quiz shells —
thin-content risk; they remain crawlable via in-site links).

Note: this site is a GitHub *project* page, so crawlers never read
output/robots.txt (robots.txt is host-root only). It is emitted anyway for
a future custom-domain move. Until then the sitemap must be submitted
manually via Google Search Console / Bing Webmaster Tools.

Usage:
    python tools/generate_sitemap.py
"""

import sys
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parent.parent
DOMAINS_DIR = ROOT / "domains"
OUTPUT_DIR = ROOT / "output"

sys.path.insert(0, str(ROOT / "tools"))
from parse_topic import SITE_BASE_URL

SITEMAP_URL_LIMIT = 50_000  # sitemaps.org hard cap per file


def collect_paths():
    """Return site-relative paths for every page the sitemap should list."""
    paths = ["", "radial-graph.html", "quiz.html", "keystones.html"]

    import yaml
    def _is_hidden(domain_dir):
        try:
            cfg = yaml.safe_load((domain_dir / "_domain.yml").read_text(encoding="utf-8"))
            return bool(isinstance(cfg, dict) and cfg.get("hidden"))
        except Exception:
            return False

    # Origin layer: skip hidden meta-domains (developmental-origins) — capacity pages are a private
    # substrate, not rendered or indexed (reverse-D).
    domains = sorted(
        d.name for d in DOMAINS_DIR.iterdir()
        if d.is_dir() and (d / "_domain.yml").exists() and not _is_hidden(d)
    )
    paths.extend(f"{d}-map.html" for d in domains)

    topic_ids = sorted(
        f.stem for d in domains for f in (DOMAINS_DIR / d).rglob("*.md")
        if not f.name.startswith("_")
    )
    paths.extend(f"topics/{tid}.html" for tid in topic_ids)
    return paths


def main():
    paths = collect_paths()
    if len(paths) > SITEMAP_URL_LIMIT:
        print(f"ERROR: {len(paths)} URLs exceeds the {SITEMAP_URL_LIMIT} "
              "per-file sitemap limit — split into a sitemap index.")
        sys.exit(1)

    entries = "\n".join(
        f"  <url><loc>{escape(SITE_BASE_URL + '/' + p)}</loc></url>"
        for p in paths
    )
    sitemap = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{entries}\n"
        "</urlset>\n"
    )

    robots = (
        "User-agent: *\n"
        "Allow: /\n"
        "\n"
        f"Sitemap: {SITE_BASE_URL}/sitemap.xml\n"
    )

    OUTPUT_DIR.mkdir(exist_ok=True)
    (OUTPUT_DIR / "sitemap.xml").write_text(sitemap, encoding="utf-8")
    (OUTPUT_DIR / "robots.txt").write_text(robots, encoding="utf-8")
    # CNAME keeps the Pages custom domain pinned (derived from SITE_BASE_URL)
    host = SITE_BASE_URL.split("//", 1)[1].split("/", 1)[0]
    (OUTPUT_DIR / "CNAME").write_text(host + "\n", encoding="utf-8")
    print(f"Wrote sitemap.xml ({len(paths)} URLs), robots.txt, CNAME to {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
