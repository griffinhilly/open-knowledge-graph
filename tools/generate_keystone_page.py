#!/usr/bin/env python3
"""Generate the keystone leaderboard page — "The 50 most powerful things to learn."

purpose: stage-banded leaderboard of the topics whose mastery unlocks the most,
         under the locked scoring (Jun 12, 2026): hop-decayed reach with a
         cross-domain bonus, ranked within developmental-stage bands
inputs:  domains/**/*.md (via generate_topic_pages loaders)
outputs: output/keystones.html
last_run: every CI deploy (.github/workflows/deploy-pages.yml)

Scoring (state on page; keep prose + code in sync):
    score(t) = sum over descendants d within 6 hops of
               0.6^(hop-1) * (1 + [domain(d) != domain(t)])
Edge-audited Jun 12, 2026: all direct successor edges of the top-15-per-stage
candidates were reviewed (1,464 edges, 10.1% corrected) before first publish.
"""

import html as html_mod
import sys
from collections import deque
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from generate_topic_pages import DOMAIN_HUES, load_all_topics, build_graphs
from parse_topic import seo_meta_tags, SITE_BASE_URL

ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = ROOT / "output"

LAM, HORIZON, BETA = 0.6, 6, 1.0

# (section title, stages included, row count) — sums to 50
BANDS = [
    ("Foundations", ["pre-formal"], 6,
     "What a child learns before school — and how far it reaches."),
    ("Elementary", ["concrete-operations"], 10,
     "The grade-school ideas the rest of the map stands on."),
    ("Middle & High School", ["abstract-reasoning"], 10,
     "Where abstraction starts paying compound interest."),
    ("College", ["formal-systems"], 14,
     "The undergraduate workhorses that open the most doors."),
    ("Graduate & Beyond", ["advanced", "expert"], 10,
     "Past the textbook frontier, reach narrows but deepens."),
]


def score_all(all_data, dependents_of):
    results = {}
    for t in all_data:
        t_domain = all_data[t].get("domain", "")
        seen = {t}
        q = deque([(t, 0)])
        total = 0.0
        reach = 0
        cross = set()
        while q:
            cur, hop = q.popleft()
            if hop >= HORIZON:
                continue
            for d, _typ in dependents_of.get(cur, []):
                if d in seen or d not in all_data:
                    continue
                seen.add(d)
                reach += 1
                d_domain = all_data[d].get("domain", "")
                is_cross = d_domain != t_domain
                if is_cross:
                    cross.add(d_domain)
                total += (LAM ** hop) * (1 + BETA * is_cross)
                q.append((d, hop + 1))
        results[t] = (total, reach, len(cross))
    return results


def domain_chip(domain):
    hue = DOMAIN_HUES.get(domain, 210)
    label = domain.replace("-", " ").title()
    return (f'<span class="chip" style="color:hsl({hue},55%,65%);'
            f'border-color:hsl({hue},35%,32%)">{html_mod.escape(label)}</span>')


def render_row(rank, tid, data, score, reach, n_cross, band_max):
    title = data.get("title", tid)
    domain = data.get("domain", "")
    hue = DOMAIN_HUES.get(domain, 210)
    pct = max(2, round(score / band_max * 100)) if band_max else 0
    return f"""<a class="row" href="topics/{tid}.html">
  <span class="rank">{rank}</span>
  <span class="row-main">
    <span class="row-title">{html_mod.escape(title)}</span>
    <span class="row-meta">{domain_chip(domain)}
      <span class="reach">reaches <strong>{reach:,}</strong> topics
      across <strong>{n_cross + 1}</strong> domains</span></span>
    <span class="bar"><span class="bar-fill" style="width:{pct}%;
      background:hsl({hue},55%,52%)"></span></span>
  </span>
</a>"""


def main():
    print("Loading topics...")
    all_data, _ = load_all_topics()
    _, dependents_of = build_graphs(all_data)
    print(f"Scoring {len(all_data)} topics...")
    scores = score_all(all_data, dependents_of)

    sections_html = []
    total_rows = 0
    for title, stages, count, blurb in BANDS:
        members = sorted(
            (t for t in all_data if all_data[t].get("stage") in stages),
            key=lambda t: -scores[t][0])[:count]
        if not members:
            continue
        band_max = scores[members[0]][0]
        rows = []
        for i, t in enumerate(members, total_rows + 1):
            s, reach, n_cross = scores[t]
            rows.append(render_row(i, t, all_data[t], s, reach, n_cross, band_max))
        total_rows += len(members)
        sections_html.append(f"""<section>
<h2>{html_mod.escape(title)}</h2>
<p class="blurb">{html_mod.escape(blurb)}</p>
{"".join(rows)}
</section>""")

    n_topics = len(all_data)
    description = ("The 50 most powerful things to learn — the topics that "
                   "unlock the most across all of human knowledge, ranked by "
                   f"prerequisite reach over {n_topics:,} mapped topics.")
    seo = seo_meta_tags("The 50 Most Powerful Things to Learn — Open Knowledge Graph",
                        description, "keystones.html",
                        image=f"{SITE_BASE_URL}/og/keystones.png")

    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>The 50 Most Powerful Things to Learn — Open Knowledge Graph</title>
{seo}
<style>
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{
  background:#0a0a14; color:#ccc;
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;
  line-height:1.6;
}}
a {{ color:#7ab; text-decoration:none; }}
.container {{ max-width:780px; margin:0 auto; padding:48px 24px 80px; }}
.nav {{ display:flex; gap:12px; margin-bottom:36px; font-size:13px; }}
.nav a {{ color:#556; padding:4px 10px; border:1px solid #222; border-radius:4px; }}
.nav a:hover {{ border-color:#555; color:#aaa; }}
h1 {{ font-size:34px; color:#f0f0f4; line-height:1.2; letter-spacing:-0.5px; }}
.subtitle {{ color:#778; font-size:16px; margin:14px 0 8px; }}
.methodology {{
  font-size:12.5px; color:#556; margin:18px 0 8px;
  background:#0e0e1a; border:1px solid #1a1a2e; border-radius:8px;
  padding:12px 16px;
}}
.methodology a {{ color:#7ab; }}
section {{ margin-top:44px; }}
h2 {{
  font-size:15px; letter-spacing:2.5px; text-transform:uppercase;
  color:#99a; border-bottom:1px solid #1a1a2e; padding-bottom:8px;
}}
.blurb {{ font-size:13px; color:#556; margin:6px 0 14px; }}
.row {{
  display:flex; gap:16px; align-items:flex-start;
  padding:11px 12px; margin:0 -12px; border-radius:8px;
}}
.row:hover {{ background:#11111f; text-decoration:none; }}
.rank {{
  font-size:18px; font-weight:700; color:#445; min-width:34px;
  text-align:right; line-height:1.45; font-variant-numeric:tabular-nums;
}}
.row-main {{ flex:1; min-width:0; }}
.row-title {{ display:block; font-size:16.5px; font-weight:600; color:#dde; }}
.row:hover .row-title {{ color:#fff; }}
.row-meta {{
  display:flex; gap:10px; align-items:center; flex-wrap:wrap;
  font-size:12px; color:#667; margin-top:3px;
}}
.chip {{
  border:1px solid; border-radius:999px; padding:1px 9px;
  font-size:11px; font-weight:600;
}}
.reach strong {{ color:#9ab; font-weight:600; }}
.bar {{
  display:block; height:3px; background:#16161f;
  border-radius:2px; margin-top:7px; overflow:hidden;
}}
.bar-fill {{ display:block; height:100%; border-radius:2px; }}
.footer {{
  margin-top:56px; font-size:12.5px; color:#445;
  border-top:1px solid #1a1a2e; padding-top:16px;
}}
.footer a {{ color:#7ab; }}
</style>
</head>
<body>
<div class="container">

<div class="nav">
  <a href="index.html">← All Domains</a>
  <a href="radial-graph.html">Graph View</a>
  <a href="quiz.html">Find Your Level</a>
</div>

<h1>The 50 Most Powerful Things to Learn</h1>
<p class="subtitle">Out of {n_topics:,} mapped topics, these unlock the most —
ranked by how much of human knowledge depends on them, at every level from
preschool to the research frontier.</p>

<div class="methodology">
<strong>How this is ranked:</strong> each topic is scored by the topics that
list it as a prerequisite, directly or downstream — a successor one step away
counts fully, each further step counts 0.6× as much (out to six steps), and
successors in a <em>different</em> domain count double. Topics compete within
their own learning stage, so graduate ideas aren't drowned out by the sheer
size of the elementary tree. Every direct edge behind these rankings was
hand-audited before publishing. Disagree with an edge?
<a href="https://github.com/griffinhilly/open-knowledge-graph/issues">File an issue</a> —
the graph is open data.
</div>

{"".join(sections_html)}

<p class="footer">Built from the <a href="index.html">Open Knowledge Graph</a> —
a free, open map of {n_topics:,} topics and the order to learn them in.
CC BY-SA 4.0. <a href="https://github.com/griffinhilly/open-knowledge-graph">Source on GitHub</a>.</p>

</div>
</body>
</html>"""

    out = OUTPUT_DIR / "keystones.html"
    out.write_text(page, encoding="utf-8")
    print(f"Wrote {out} ({total_rows} rows)")


if __name__ == "__main__":
    main()
