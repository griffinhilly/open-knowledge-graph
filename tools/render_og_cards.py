#!/usr/bin/env python3
"""Render og:image share cards (1200x630 PNG) for hub topics + site default.

purpose: every shared OKG link unfurls as a designed card instead of a bare URL
inputs:  domains/**/*.md (topic corpus, via generate_topic_pages loaders)
outputs: output/og/<topic-id>.png for the top-N hub topics, output/og/default.png
last_run: 2026-06-12 (initial build)

Ranking: transitive-successor count ("unlocks N topics") — the same stat the
topic pages display. Render order is deterministic (count desc, id asc).

Renderer: headless Chrome via playwright (NCP native-HTML/CSS pipeline).
Tries the system Chrome channel first (preinstalled on GitHub runners and on
the dev box), falls back to playwright's bundled chromium. Exits non-zero on
any render failure so CI fails loudly instead of silently shipping no cards.

Usage:
    python tools/render_og_cards.py              # default card + top 1000
    python tools/render_og_cards.py --top 250    # smaller batch
    python tools/render_og_cards.py --default-only
"""

import argparse
import html
import sys
from pathlib import Path

from generate_topic_pages import (
    DOMAIN_HUES, STAGE_LABELS,
    load_all_topics, build_graphs,
    count_transitive_successors, find_longest_chain,
)

ROOT = Path(__file__).resolve().parent.parent
OG_DIR = ROOT / "output" / "og"

FONT_STACK = '"Segoe UI", Roboto, "Liberation Sans", Helvetica, Arial, sans-serif'


def card_shell(hue, body):
    """Shared 1200x630 chrome: dark site background + domain-hue glow."""
    return f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><style>
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{
  width:1200px; height:630px; overflow:hidden;
  background:#0a0a14;
  background-image:radial-gradient(ellipse 900px 500px at 85% 0%, hsla({hue},60%,50%,0.14), transparent 70%);
  color:#ccc; font-family:{FONT_STACK};
  display:flex; flex-direction:column; padding:60px 64px 52px;
}}
.eyebrow-row {{ display:flex; justify-content:space-between; align-items:baseline; }}
.eyebrow {{ font-size:22px; letter-spacing:4px; color:#667; font-weight:600; }}
.domain {{ font-size:24px; font-weight:600; color:hsl({hue},55%,62%); }}
.title-block {{ flex:1; display:flex; flex-direction:column; justify-content:center; min-height:0; }}
.title {{ color:#f2f2f5; font-weight:700; line-height:1.12; letter-spacing:-0.5px; }}
.chain {{ display:flex; align-items:center; gap:14px; margin-top:36px; flex-wrap:nowrap; }}
.chain-pill {{
  font-size:24px; color:#9ab; padding:10px 22px; white-space:nowrap;
  border:2px solid #2a2a3a; border-radius:999px;
  max-width:380px; overflow:hidden; text-overflow:ellipsis;
}}
.chain-pill.current {{
  color:#fff; border-color:hsl({hue},55%,55%);
  background:hsla({hue},55%,50%,0.15); font-weight:600;
}}
.chain-dot {{
  display:inline-block; width:22px; height:22px; border-radius:50%;
  background:hsl({hue},60%,58%);
  box-shadow:0 0 20px hsla({hue},60%,58%,0.9), 0 0 44px hsla({hue},60%,58%,0.4);
}}
.chain-arrow {{ color:#445; font-size:26px; }}
.bottom-row {{ display:flex; justify-content:space-between; align-items:flex-end; }}
.stat {{ font-size:30px; color:#889; }}
.stat .num {{ font-size:54px; font-weight:700; color:hsl({hue},60%,62%); margin-right:14px; }}
.site {{ font-size:26px; color:#556; }}
</style></head><body>{body}</body></html>"""


def topic_card_html(tid, all_data, prereqs_of, unlocks):
    data = all_data[tid]
    title = data.get("title", tid)
    domain = data.get("domain", "")
    hue = DOMAIN_HUES.get(domain, 210)
    domain_label = domain.replace("-", " ").title()

    n = len(title)
    size = 84 if n <= 28 else 68 if n <= 52 else 54

    # Chain ends in a glowing node dot (this topic) rather than repeating the
    # title — the full title is the card's hero line directly above.
    chain = find_longest_chain(tid, prereqs_of, all_data)
    pills = []
    tail = chain[-3:-1] if len(chain) > 1 else []  # up to 2 ancestors
    if len(chain) > len(tail) + 1:
        pills.append('<span class="chain-arrow">&middot;&middot;&middot;</span>')
    for cid, ctitle in tail:
        pills.append(f'<span class="chain-pill">{html.escape(ctitle)}</span>')
        pills.append('<span class="chain-arrow">&rarr;</span>')
    pills.append('<span class="chain-dot"></span>')
    chain_html = "".join(pills)
    if len(chain) <= 1:
        chain_html = ('<span class="chain-dot"></span>'
                      '<span class="chain-pill" style="border-color:hsla(0,0%,100%,0.08);max-width:none">'
                      'Starting point &mdash; no prerequisites</span>')

    stat = (f'<span class="num">{unlocks:,}</span> topic{"s" if unlocks != 1 else ""} build on this'
            if unlocks > 0 else
            f'<span class="num">{len(chain) - 1:,}</span> steps to get here')

    body = f"""
<div class="eyebrow-row">
  <span class="eyebrow">OPEN KNOWLEDGE GRAPH</span>
  <span class="domain">{html.escape(domain_label)}</span>
</div>
<div class="title-block">
  <div class="title" style="font-size:{size}px">{html.escape(title)}</div>
  <div class="chain">{chain_html}</div>
</div>
<div class="bottom-row">
  <span class="stat">{stat}</span>
  <span class="site">openknowledgegraph.com</span>
</div>"""
    return card_shell(hue, body)


def default_card_html(n_topics, n_domains):
    body = f"""
<div class="eyebrow-row">
  <span class="eyebrow">OPEN KNOWLEDGE GRAPH</span>
</div>
<div class="title-block">
  <div class="title" style="font-size:76px">What do you need to learn first?</div>
  <div class="chain" style="margin-top:30px">
    <span class="chain-pill" style="font-size:28px;max-width:none">A free, open map of {n_topics:,} topics &mdash; and the order to learn them in</span>
  </div>
</div>
<div class="bottom-row">
  <span class="stat"><span class="num">{n_topics:,}</span> topics &middot; {n_domains} domains</span>
  <span class="site">openknowledgegraph.com</span>
</div>"""
    return card_shell(210, body)


def launch_browser(p):
    try:
        return p.chromium.launch(channel="chrome")
    except Exception:
        return p.chromium.launch()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--top", type=int, default=1000,
                    help="number of hub topics to render (by transitive successors)")
    ap.add_argument("--default-only", action="store_true",
                    help="render only the site-wide default card")
    ap.add_argument("--ids", nargs="*", default=None,
                    help="render only these topic ids (debugging/selective regen)")
    args = ap.parse_args()

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("ERROR: playwright required. Install with: pip install playwright")
        sys.exit(1)

    print("Loading topics...")
    all_data, _ = load_all_topics()
    prereqs_of, dependents_of = build_graphs(all_data)
    n_domains = len({d.get("domain") for d in all_data.values() if d.get("domain")})

    targets = []
    if args.ids:
        targets = [(count_transitive_successors(tid, dependents_of), tid)
                   for tid in args.ids if tid in all_data]
        print(f"Rendering default card + {len(targets)} requested cards...")
    elif not args.default_only:
        ranked = sorted(
            ((count_transitive_successors(tid, dependents_of), tid) for tid in all_data),
            key=lambda x: (-x[0], x[1]),
        )
        targets = ranked[: args.top]
        print(f"Rendering default card + top {len(targets)} hub cards...")
    else:
        print("Rendering default card only...")

    OG_DIR.mkdir(parents=True, exist_ok=True)
    failures = 0
    with sync_playwright() as p:
        browser = launch_browser(p)
        page = browser.new_page(viewport={"width": 1200, "height": 630})

        page.set_content(default_card_html(len(all_data), n_domains))
        page.screenshot(path=str(OG_DIR / "default.png"))

        for i, (unlocks, tid) in enumerate(targets, 1):
            try:
                page.set_content(topic_card_html(tid, all_data, prereqs_of, unlocks))
                page.screenshot(path=str(OG_DIR / f"{tid}.png"))
            except Exception as e:
                failures += 1
                print(f"  FAIL {tid}: {e}")
            if i % 100 == 0:
                print(f"  {i}/{len(targets)}...")
        browser.close()

    print(f"Done: {len(targets) - failures + 1} cards in {OG_DIR}")
    if failures:
        print(f"ERROR: {failures} cards failed to render")
        sys.exit(1)


if __name__ == "__main__":
    main()
