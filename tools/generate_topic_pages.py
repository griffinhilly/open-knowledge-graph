#!/usr/bin/env python3
"""Generate individual detail pages for every topic in the knowledge graph.

Each page includes:
- Title, domain, course, stage metadata
- Core Idea, How It's Best Learned, Common Misconceptions
- Full prerequisite chain (longest path from root)
- All direct prerequisites with links
- All direct successors (topics that depend on this one)

Usage:
    python tools/generate_topic_pages.py
"""

import sys
import re
import json
import html as html_mod
from pathlib import Path
from collections import defaultdict, deque

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML required.")
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent
DOMAINS_DIR = ROOT / "domains"
OUTPUT_DIR = ROOT / "output"
TOPICS_DIR = OUTPUT_DIR / "topics"

STAGE_LABELS = {
    "pre-formal": "Early Childhood",
    "concrete-operations": "Elementary",
    "abstract-reasoning": "Middle & High School",
    "formal-systems": "College",
    "advanced": "Graduate",
}

DOMAIN_HUES = {
    "mathematics": 42, "formal-sciences-and-logic": 185, "philosophy": 260,
    "computer-science": 200, "engineering": 28, "physics": 215, "chemistry": 0,
    "earth-and-space-sciences": 170, "biology": 120, "health-and-human-development": 148,
    "psychology": 280, "social-sciences": 60, "economics": 48, "practical-life-skills": 80,
    "history": 18, "language-and-communication": 155, "literature": 310,
    "arts-and-aesthetics": 335, "music": 290,
}


def parse_topic_file(filepath):
    """Parse frontmatter and body sections from a topic markdown file."""
    text = filepath.read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not match:
        return None, {}

    try:
        data = yaml.safe_load(match.group(1))
    except yaml.YAMLError:
        return None, {}

    body = text[match.end():]

    # Parse body into sections
    sections = {}
    current_section = None
    current_lines = []

    for line in body.splitlines():
        header_match = re.match(r"^##\s+(.+)$", line)
        if header_match:
            if current_section:
                sections[current_section] = "\n".join(current_lines).strip()
            current_section = header_match.group(1).strip()
            current_lines = []
        elif current_section:
            current_lines.append(line)
        # Skip lines before first section header (usually just the H1 title)

    if current_section:
        sections[current_section] = "\n".join(current_lines).strip()

    return data, sections


def load_all_topics():
    """Load all topic data and body sections."""
    all_data = {}
    all_sections = {}
    for filepath in sorted(DOMAINS_DIR.rglob("*.md")):
        data, sections = parse_topic_file(filepath)
        if data and "id" in data:
            all_data[data["id"]] = data
            all_sections[data["id"]] = sections
    return all_data, all_sections


def build_graphs(all_data):
    """Build prerequisite and dependent graphs."""
    prereqs_of = defaultdict(list)   # tid -> [(prereq_id, type)]
    dependents_of = defaultdict(list)  # tid -> [(dependent_id, type)]

    for tid, data in all_data.items():
        for p in data.get("prerequisites", []):
            if isinstance(p, dict) and "id" in p:
                pid = p["id"]
                ptype = p.get("type", "hard")
                if pid in all_data:
                    prereqs_of[tid].append((pid, ptype))
                    dependents_of[pid].append((tid, ptype))

    return prereqs_of, dependents_of


def compute_depths(all_data, prereqs_of):
    """Compute topological depth for each topic."""
    children_of = defaultdict(list)
    in_degree = defaultdict(int)

    for tid in all_data:
        for pid, _ in prereqs_of.get(tid, []):
            children_of[pid].append(tid)
            in_degree[tid] += 1

    depth = {}
    queue = deque()
    for tid in all_data:
        if in_degree[tid] == 0:
            depth[tid] = 0
            queue.append(tid)

    while queue:
        nid = queue.popleft()
        for child in children_of[nid]:
            new_depth = depth.get(nid, 0) + 1
            if child not in depth or new_depth > depth[child]:
                depth[child] = new_depth
                queue.append(child)

    for tid in all_data:
        if tid not in depth:
            depth[tid] = 0

    return depth


def find_longest_chain(tid, prereqs_of, all_data):
    """Find the longest prerequisite chain ending at this topic.

    Returns a list of (topic_id, title) from root to this topic.
    """
    # BFS/DFS to find longest path from any root to tid
    # Use dynamic programming: longest path ending at each node
    # We need to trace back from tid

    # First compute depth of all ancestors
    ancestors = set()
    stack = [tid]
    while stack:
        node = stack.pop()
        if node in ancestors:
            continue
        ancestors.add(node)
        for pid, _ in prereqs_of.get(node, []):
            stack.append(pid)

    # Topological sort of ancestors
    in_deg = defaultdict(int)
    children = defaultdict(list)
    for node in ancestors:
        for pid, _ in prereqs_of.get(node, []):
            if pid in ancestors:
                children[pid].append(node)
                in_deg[node] += 1

    topo = []
    q = deque([n for n in ancestors if in_deg[n] == 0])
    while q:
        n = q.popleft()
        topo.append(n)
        for c in children[n]:
            in_deg[c] -= 1
            if in_deg[c] == 0:
                q.append(c)

    # Longest path ending at each node
    dist = {n: 0 for n in ancestors}
    parent = {n: None for n in ancestors}
    for n in topo:
        for c in children[n]:
            if dist[n] + 1 > dist[c]:
                dist[c] = dist[n] + 1
                parent[c] = n

    # Trace back from tid
    chain = []
    current = tid
    while current is not None:
        title = all_data[current].get("title", current) if current in all_data else current
        chain.append((current, title))
        current = parent.get(current)

    chain.reverse()
    return chain


def count_transitive_prereqs(tid, prereqs_of):
    """Count all transitive prerequisites."""
    visited = set()
    stack = list(pid for pid, _ in prereqs_of.get(tid, []))
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        for pid, _ in prereqs_of.get(node, []):
            stack.append(pid)
    return len(visited)


def markdown_to_html(text):
    """Simple markdown-to-HTML conversion for topic body text."""
    if not text:
        return ""

    lines = text.split("\n")
    html_lines = []
    in_list = False

    for line in lines:
        stripped = line.strip()
        if not stripped:
            if in_list:
                html_lines.append("</ul>")
                in_list = False
            html_lines.append("")
            continue

        # List items
        if stripped.startswith("- "):
            if not in_list:
                html_lines.append("<ul>")
                in_list = True
            content = html_mod.escape(stripped[2:])
            # Bold the part before the em dash if present
            if " — " in content:
                parts = content.split(" — ", 1)
                content = f"<strong>{parts[0]}</strong> — {parts[1]}"
            html_lines.append(f"<li>{content}</li>")
        else:
            if in_list:
                html_lines.append("</ul>")
                in_list = False
            html_lines.append(f"<p>{html_mod.escape(stripped)}</p>")

    if in_list:
        html_lines.append("</ul>")

    return "\n".join(html_lines)


def generate_topic_page(tid, all_data, all_sections, prereqs_of, dependents_of, depths):
    """Generate HTML for a single topic detail page."""
    data = all_data[tid]
    sections = all_sections.get(tid, {})

    title = data.get("title", tid)
    domain = data.get("domain", "")
    course = data.get("course", "")
    stage = data.get("stage", "")
    tags = data.get("tags", [])

    hue = DOMAIN_HUES.get(domain, 0)
    domain_label = domain.replace("-", " ").title()
    course_label = course.replace("-", " ").title()
    stage_label = STAGE_LABELS.get(stage, stage)
    depth = depths.get(tid, 0)

    # Body sections
    core_idea = sections.get("Core Idea", "")
    how_learned = sections.get("How It's Best Learned", "")
    misconceptions = sections.get("Common Misconceptions", "")
    notes = sections.get("Notes", "")

    # Prerequisites
    direct_prereqs = prereqs_of.get(tid, [])
    chain = find_longest_chain(tid, prereqs_of, all_data)
    total_transitive = count_transitive_prereqs(tid, prereqs_of)

    # Successors (direct only)
    direct_successors = dependents_of.get(tid, [])

    # Build prerequisite chain HTML
    chain_html = ""
    if len(chain) > 1:
        chain_items = []
        for i, (cid, ctitle) in enumerate(chain):
            is_current = cid == tid
            cdomain = all_data[cid].get("domain", "") if cid in all_data else ""
            chue = DOMAIN_HUES.get(cdomain, 0)
            if is_current:
                chain_items.append(
                    f'<span class="chain-node current" style="border-color:hsl({chue},50%,50%)">'
                    f'{html_mod.escape(ctitle)}</span>'
                )
            else:
                chain_items.append(
                    f'<a href="{cid}.html" class="chain-node" style="border-color:hsl({chue},40%,40%)">'
                    f'{html_mod.escape(ctitle)}</a>'
                )

        chain_html = '<span class="chain-arrow"> → </span>'.join(chain_items)

    # Direct prerequisites HTML
    prereq_html = ""
    if direct_prereqs:
        items = []
        for pid, ptype in sorted(direct_prereqs, key=lambda x: x[1]):
            ptitle = all_data[pid].get("title", pid) if pid in all_data else pid
            pdomain = all_data[pid].get("domain", "") if pid in all_data else ""
            phue = DOMAIN_HUES.get(pdomain, 0)
            badge = "hard" if ptype == "hard" else "soft"
            items.append(
                f'<a href="{pid}.html" class="prereq-card">'
                f'<span class="prereq-dot" style="background:hsl({phue},55%,50%)"></span>'
                f'<span class="prereq-title">{html_mod.escape(ptitle)}</span>'
                f'<span class="prereq-badge {badge}">{badge}</span>'
                f'</a>'
            )
        prereq_html = "\n".join(items)

    # Successors HTML
    successor_html = ""
    if direct_successors:
        items = []
        for sid, stype in sorted(direct_successors, key=lambda x: all_data.get(x[0], {}).get("title", "")):
            stitle = all_data[sid].get("title", sid) if sid in all_data else sid
            sdomain = all_data[sid].get("domain", "") if sid in all_data else ""
            shue = DOMAIN_HUES.get(sdomain, 0)
            badge = "hard" if stype == "hard" else "soft"
            items.append(
                f'<a href="{sid}.html" class="prereq-card">'
                f'<span class="prereq-dot" style="background:hsl({shue},55%,50%)"></span>'
                f'<span class="prereq-title">{html_mod.escape(stitle)}</span>'
                f'<span class="prereq-badge {badge}">{badge}</span>'
                f'</a>'
            )
        successor_html = "\n".join(items)

    # Tags HTML
    tags_html = ""
    if tags:
        tags_html = " ".join(
            f'<span class="tag">{html_mod.escape(str(t))}</span>' for t in tags
        )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{html_mod.escape(title)} — Open Knowledge Graph</title>
<style>
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{
  background:#0a0a14; color:#ccc;
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;
  line-height:1.6;
}}
a {{ color:#7ab; text-decoration:none; }}
a:hover {{ color:#9cd; text-decoration:underline; }}

.container {{
  max-width:820px; margin:0 auto; padding:40px 24px 80px;
}}

.nav {{
  display:flex; gap:12px; margin-bottom:32px; font-size:13px;
}}
.nav a {{
  color:#556; padding:4px 10px;
  border:1px solid #222; border-radius:4px;
  transition:border-color 0.2s;
}}
.nav a:hover {{ border-color:#555; color:#aaa; text-decoration:none; }}

.breadcrumb {{
  font-size:13px; color:#556; margin-bottom:8px;
}}
.breadcrumb span {{ color:#445; }}

h1 {{
  font-size:28px; color:#eee; margin-bottom:8px;
  border-left:4px solid hsl({hue},55%,50%);
  padding-left:16px;
}}

.meta-row {{
  display:flex; gap:12px; align-items:center; flex-wrap:wrap;
  margin-bottom:24px; font-size:12px;
}}
.stage-badge {{
  background:hsl({hue},30%,20%); color:hsl({hue},50%,70%);
  padding:3px 10px; border-radius:12px; font-weight:600;
}}
.depth-info {{ color:#556; }}

.tags {{ display:flex; gap:6px; flex-wrap:wrap; margin-bottom:28px; }}
.tag {{
  background:#151525; border:1px solid #252540;
  padding:2px 8px; border-radius:4px;
  font-size:11px; color:#667;
}}

.section {{
  margin-bottom:32px;
}}
.section h2 {{
  font-size:16px; color:#889; text-transform:uppercase;
  letter-spacing:0.5px; margin-bottom:12px;
  padding-bottom:6px; border-bottom:1px solid #1a1a2e;
}}
.section p {{
  margin-bottom:10px; color:#bbb; font-size:15px;
}}
.section ul {{
  margin:8px 0 12px 20px; color:#aab;
}}
.section li {{
  margin-bottom:6px; font-size:14px;
}}

.chain-container {{
  background:#0e0e1a; border:1px solid #1a1a2e;
  border-radius:8px; padding:16px 20px;
  overflow-x:auto; white-space:nowrap;
  margin-bottom:12px;
}}
.chain-node {{
  display:inline-block; padding:4px 10px;
  border:1px solid #333; border-radius:6px;
  font-size:12px; color:#aab;
  text-decoration:none;
  transition:background 0.2s;
}}
.chain-node:hover {{ background:#1a1a30; text-decoration:none; }}
.chain-node.current {{
  background:#1a1a30; color:#eee; font-weight:600;
  border-width:2px;
}}
.chain-arrow {{ color:#334; font-size:14px; margin:0 2px; }}
.chain-meta {{ font-size:12px; color:#445; margin-top:8px; }}

.prereq-list {{
  display:flex; flex-direction:column; gap:6px;
}}
.prereq-card {{
  display:flex; align-items:center; gap:10px;
  padding:8px 14px;
  background:#0e0e1a; border:1px solid #1a1a2e;
  border-radius:6px; text-decoration:none;
  transition:border-color 0.2s, background 0.2s;
}}
.prereq-card:hover {{
  border-color:#333; background:#12122a;
  text-decoration:none;
}}
.prereq-dot {{
  width:8px; height:8px; border-radius:50%; flex-shrink:0;
}}
.prereq-title {{
  flex:1; color:#bbc; font-size:14px;
}}
.prereq-badge {{
  font-size:10px; padding:2px 6px; border-radius:3px;
  font-weight:600; text-transform:uppercase;
}}
.prereq-badge.hard {{
  background:rgba(220,80,80,0.15); color:#c66;
}}
.prereq-badge.soft {{
  background:rgba(80,160,220,0.15); color:#6ab;
}}

.empty-state {{
  color:#445; font-size:13px; font-style:italic;
  padding:12px 0;
}}
</style>
</head>
<body>
<div class="container">

<div class="nav">
  <a href="../radial-graph.html">← Graph View</a>
  <a href="../index.html">All Domains</a>
</div>

<div class="breadcrumb">
  {html_mod.escape(domain_label)} <span>›</span> {html_mod.escape(course_label)}
</div>

<h1>{html_mod.escape(title)}</h1>

<div class="meta-row">
  <span class="stage-badge">{html_mod.escape(stage_label)}</span>
  <span class="depth-info">Depth {depth} in the knowledge graph</span>
</div>

{"<div class='tags'>" + tags_html + "</div>" if tags_html else ""}

<div class="section">
  <h2>Core Idea</h2>
  {markdown_to_html(core_idea) if core_idea else '<p class="empty-state">No description available yet.</p>'}
</div>

{"<div class='section'><h2>How It's Best Learned</h2>" + markdown_to_html(how_learned) + "</div>" if how_learned else ""}

{"<div class='section'><h2>Common Misconceptions</h2>" + markdown_to_html(misconceptions) + "</div>" if misconceptions else ""}

{"<div class='section'><h2>Notes</h2>" + markdown_to_html(notes) + "</div>" if notes else ""}

<div class="section">
  <h2>Prerequisite Chain</h2>
  {('<div class="chain-container">' + chain_html + '</div><p class="chain-meta">Longest path: ' + str(len(chain)) + ' steps &middot; ' + str(total_transitive) + ' total prerequisite topics</p>') if len(chain) > 1 else '<p class="empty-state">This is a foundational topic with no prerequisites.</p>'}
</div>

<div class="section">
  <h2>Prerequisites ({len(direct_prereqs)})</h2>
  {('<div class="prereq-list">' + prereq_html + '</div>') if prereq_html else '<p class="empty-state">No prerequisites — this is a starting point.</p>'}
</div>

<div class="section">
  <h2>Leads To ({len(direct_successors)})</h2>
  {('<div class="prereq-list">' + successor_html + '</div>') if successor_html else '<p class="empty-state">No topics depend on this one yet.</p>'}
</div>

</div>
</body>
</html>"""


def main():
    print("Loading topics...")
    all_data, all_sections = load_all_topics()
    print(f"Loaded {len(all_data)} topics")

    print("Building graphs...")
    prereqs_of, dependents_of = build_graphs(all_data)
    depths = compute_depths(all_data, prereqs_of)

    TOPICS_DIR.mkdir(parents=True, exist_ok=True)

    print(f"Generating {len(all_data)} topic pages...")
    count = 0
    for tid in sorted(all_data.keys()):
        html = generate_topic_page(
            tid, all_data, all_sections, prereqs_of, dependents_of, depths
        )
        out = TOPICS_DIR / f"{tid}.html"
        out.write_text(html, encoding="utf-8")
        count += 1
        if count % 500 == 0:
            print(f"  {count}/{len(all_data)}...")

    print(f"Done! {count} topic pages in {TOPICS_DIR}")


if __name__ == "__main__":
    main()
