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
    "expert": "Research",
}

DOMAIN_HUES = {
    "mathematics": 42, "formal-sciences-and-logic": 185, "philosophy": 260,
    "computer-science": 200, "engineering": 28, "physics": 215, "chemistry": 0,
    "earth-and-space-sciences": 170, "biology": 120, "health-and-human-development": 148,
    "psychology": 280, "social-sciences": 60, "economics": 48, "practical-life-skills": 80,
    "history": 18, "language-and-communication": 155, "literature": 310,
    "arts-and-aesthetics": 335, "music": 290,
}


from parse_topic import parse_topic, parse_sections, meta_description, seo_meta_tags, SITE_BASE_URL, ANALYTICS_SNIPPET


def parse_topic_file(filepath):
    """Parse frontmatter and body sections from a topic markdown file."""
    data, body = parse_topic(filepath)
    if data is None:
        return None, {}
    return data, parse_sections(body)


def load_pedagogy_types():
    """Read _domain.yml files and return {domain: pedagogy_type}.
    Defaults to 'assessable' when the field is absent."""
    result = {}
    for yml in sorted(DOMAINS_DIR.glob("*/_domain.yml")):
        try:
            data = yaml.safe_load(yml.read_text(encoding="utf-8"))
            slug = data.get("domain", yml.parent.name)
            result[slug] = data.get("pedagogy_type", "assessable")
        except Exception:
            result[yml.parent.name] = "assessable"
    return result


def load_all_topics():
    """Load all topic data and body sections."""
    all_data = {}
    all_sections = {}
    for filepath in sorted(DOMAINS_DIR.rglob("*.md")):
        data, sections = parse_topic_file(filepath)
        if data and "id" in data:
            # Origin layer (reverse-D): kind:capacity nodes are a private substrate — never rendered
            # as pages, never scored as keystones, never emitted as competencyRequired. Excluding
            # them here propagates to every consumer of load_all_topics (topic pages, keystone) and
            # to build_graphs (capacity prereqs drop out via the `pid in all_data` guard).
            if data.get("kind") == "capacity":
                continue
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


def count_transitive_successors(tid, dependents_of):
    """Count all transitive successors (topics that depend on this one)."""
    visited = set()
    stack = list(sid for sid, _ in dependents_of.get(tid, []))
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        for sid, _ in dependents_of.get(node, []):
            stack.append(sid)
    return len(visited)


# Caret exponents -> <sup>. Conservative: only after an alphanumeric/closing
# bracket, and only simple exponents — {braced}, (parenthesized, non-nested),
# or a short bare token with optional leading minus (e^-x, 2^10, x^n).
_SUP_BRACE_RE = re.compile(r'(?<=[A-Za-z0-9)\]])\^\{([^{}]{1,40})\}')
_SUP_PAREN_RE = re.compile(r'(?<=[A-Za-z0-9)\]])\^\(([^()]{1,40})\)')
_SUP_BARE_RE = re.compile(r'(?<=[A-Za-z0-9)\]])\^(-?[A-Za-z0-9]{1,4})(?![A-Za-z0-9({])')


def superscript_carets(text):
    """Convert caret math notation (a^2, e^{-x}, 2^(n+1)) to <sup> markup."""
    text = _SUP_BRACE_RE.sub(r'<sup>\1</sup>', text)
    text = _SUP_PAREN_RE.sub(r'<sup>\1</sup>', text)
    return _SUP_BARE_RE.sub(r'<sup>\1</sup>', text)


def inline_markdown(text):
    """Process inline markdown (**bold**) in already-escaped HTML text."""
    return superscript_carets(re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text))


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
                content = superscript_carets(f"<strong>{parts[0]}</strong> — {parts[1]}")
            else:
                content = inline_markdown(content)
            html_lines.append(f"<li>{content}</li>")
        else:
            if in_list:
                html_lines.append("</ul>")
                in_list = False
            html_lines.append(f"<p>{inline_markdown(html_mod.escape(stripped))}</p>")

    if in_list:
        html_lines.append("</ul>")

    return "\n".join(html_lines)


def parse_questions_yaml(text):
    """Parse the YAML code block from a Questions section."""
    if not text:
        return []
    # Extract YAML from ```yaml ... ``` code block
    match = re.search(r'```ya?ml\s*\n(.*?)```', text, re.DOTALL)
    if not match:
        return []
    try:
        questions = yaml.safe_load(match.group(1))
        return questions if isinstance(questions, list) else []
    except yaml.YAMLError:
        return []


def generate_questions_page(tid, all_data, all_sections, questions):
    """Generate a standalone HTML page for a topic's question set."""
    data = all_data[tid]
    title = data.get("title", tid)
    domain = data.get("domain", "")
    hue = DOMAIN_HUES.get(domain, 0)

    questions_html_parts = []
    for i, q in enumerate(questions, 1):
        qtext = html_mod.escape(q.get("question", ""))
        qtype = q.get("type", "")
        explanation = html_mod.escape(q.get("explanation", ""))

        if qtype == "multiple-choice":
            options = q.get("options", [])
            answer_idx = q.get("answer", 0)
            options_html = ""
            for j, opt in enumerate(options):
                letter = chr(65 + j)  # A, B, C, D
                is_correct = ' data-correct="true"' if j == answer_idx else ''
                options_html += (
                    f'<div class="q-option" data-idx="{j}"{is_correct}>'
                    f'<span class="q-letter">{letter}</span>'
                    f'<span>{html_mod.escape(str(opt))}</span>'
                    f'</div>\n'
                )
            questions_html_parts.append(f"""
<div class="question-card" data-type="mc">
  <div class="q-number">Question {i} <span class="q-type-badge">Multiple Choice</span></div>
  <p class="q-text">{qtext}</p>
  <div class="q-options">{options_html}</div>
  <button class="reveal-btn" onclick="revealAnswer(this)">Show Answer</button>
  <div class="q-explanation hidden">
    <p>{explanation}</p>
  </div>
</div>""")

        elif qtype == "true-false":
            answer = q.get("answer", False)
            answer_str = "true" if answer else "false"
            questions_html_parts.append(f"""
<div class="question-card" data-type="tf">
  <div class="q-number">Question {i} <span class="q-type-badge">True / False</span></div>
  <p class="q-text">{qtext}</p>
  <div class="q-options">
    <div class="q-option" data-idx="true"{' data-correct="true"' if answer else ''}>
      <span class="q-letter">T</span><span>True</span>
    </div>
    <div class="q-option" data-idx="false"{' data-correct="true"' if not answer else ''}>
      <span class="q-letter">F</span><span>False</span>
    </div>
  </div>
  <button class="reveal-btn" onclick="revealAnswer(this)">Show Answer</button>
  <div class="q-explanation hidden">
    <p>Answer: <strong>{"True" if answer else "False"}</strong></p>
    <p>{explanation}</p>
  </div>
</div>""")

        elif qtype == "short-answer":
            answer_text = html_mod.escape(str(q.get("answer", "")))
            questions_html_parts.append(f"""
<div class="question-card" data-type="sa">
  <div class="q-number">Question {i} <span class="q-type-badge">Short Answer</span></div>
  <p class="q-text">{qtext}</p>
  <div class="q-sa-prompt">Think about your answer, then reveal below.</div>
  <button class="reveal-btn" onclick="revealAnswer(this)">Show Answer</button>
  <div class="q-explanation hidden">
    <div class="q-model-answer"><strong>Model answer:</strong> {answer_text}</div>
    <p>{explanation}</p>
  </div>
</div>""")

    all_questions_html = "\n".join(questions_html_parts)

    q_seo_block = seo_meta_tags(
        "Questions — " + title,
        "Practice questions for " + title + " on the Open Knowledge Graph.",
        "topics/" + tid + "-questions.html", og_type="article")

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Questions — {html_mod.escape(title)} — Open Knowledge Graph</title>
{q_seo_block}
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

h1 {{
  font-size:24px; color:#eee; margin-bottom:8px;
  border-left:4px solid hsl({hue},55%,50%);
  padding-left:16px;
}}
.subtitle {{
  font-size:14px; color:#667; margin-bottom:32px;
}}

.question-card {{
  background:#0e0e1a; border:1px solid #1a1a2e;
  border-radius:8px; padding:24px;
  margin-bottom:20px;
}}
.q-number {{
  font-size:12px; color:#667; text-transform:uppercase;
  letter-spacing:0.5px; margin-bottom:10px;
}}
.q-type-badge {{
  background:#151530; border:1px solid #252545;
  padding:2px 8px; border-radius:3px;
  font-size:10px; color:#889; margin-left:8px;
}}
.q-text {{
  font-size:16px; color:#dde; margin-bottom:16px; line-height:1.5;
}}
.q-options {{
  display:flex; flex-direction:column; gap:8px;
  margin-bottom:16px;
}}
.q-option {{
  display:flex; align-items:center; gap:12px;
  padding:10px 14px;
  background:#0a0a18; border:1px solid #1a1a2e;
  border-radius:6px; cursor:pointer;
  transition:border-color 0.2s, background 0.2s;
  font-size:14px; color:#bbc;
}}
.q-option:hover {{
  border-color:#333; background:#12122a;
}}
.q-option.selected {{
  border-color:hsl({hue},50%,45%);
  background:hsl({hue},30%,12%);
}}
.q-option.correct {{
  border-color:#4a7; background:rgba(68,170,119,0.1);
}}
.q-option.incorrect {{
  border-color:#a55; background:rgba(170,85,85,0.1);
}}
.q-letter {{
  width:24px; height:24px; border-radius:50%;
  background:#151530; border:1px solid #252545;
  display:flex; align-items:center; justify-content:center;
  font-size:12px; font-weight:600; color:#889;
  flex-shrink:0;
}}
.q-sa-prompt {{
  font-size:13px; color:#556; font-style:italic;
  margin-bottom:16px;
}}
.reveal-btn {{
  background:hsl({hue},30%,20%); color:hsl({hue},50%,70%);
  border:1px solid hsl({hue},30%,30%);
  padding:8px 20px; border-radius:6px;
  cursor:pointer; font-size:13px; font-weight:600;
  transition:background 0.2s;
}}
.reveal-btn:hover {{
  background:hsl({hue},30%,25%);
}}
.reveal-btn.used {{
  background:#151525; color:#556; border-color:#222;
  cursor:default;
}}
.q-explanation {{
  margin-top:16px; padding:16px;
  background:#0a0a18; border-left:3px solid hsl({hue},40%,40%);
  border-radius:0 6px 6px 0;
}}
.q-explanation p {{
  font-size:14px; color:#aab; margin-bottom:8px; line-height:1.6;
}}
.q-explanation p:last-child {{ margin-bottom:0; }}
.q-model-answer {{
  font-size:14px; color:#bcc; margin-bottom:12px;
  padding:10px 14px; background:#0e0e20; border-radius:4px;
}}
.hidden {{ display:none; }}

.score-bar {{
  display:flex; gap:12px; align-items:center;
  padding:16px 20px; margin-bottom:28px;
  background:#0e0e1a; border:1px solid #1a1a2e;
  border-radius:8px; font-size:14px; color:#889;
}}
.score-count {{
  font-weight:600; color:#eee; font-size:18px;
}}
</style>
</head>
<body>
<div class="container">

<div class="nav">
  <a href="{tid}.html">← Back to Topic</a>
  <a href="../radial-graph.html">Graph View</a>
  <a href="../index.html">All Domains</a>
</div>

<h1>Questions: {html_mod.escape(title)}</h1>
<p class="subtitle">{len(questions)} questions to test your understanding</p>

<div class="score-bar">
  Score: <span class="score-count" id="score">0</span> / {len(questions)}
</div>

{all_questions_html}

</div>
<script>
let score = 0;
const total = {len(questions)};

document.querySelectorAll('.q-option').forEach(opt => {{
  opt.addEventListener('click', function() {{
    const card = this.closest('.question-card');
    if (card.classList.contains('answered')) return;
    // Clear previous selection in this card
    card.querySelectorAll('.q-option').forEach(o => o.classList.remove('selected'));
    this.classList.add('selected');
  }});
}});

function revealAnswer(btn) {{
  const card = btn.closest('.question-card');
  if (card.classList.contains('answered')) return;
  card.classList.add('answered');
  btn.classList.add('used');
  btn.textContent = 'Answered';

  const explanation = card.querySelector('.q-explanation');
  explanation.classList.remove('hidden');

  // Grade the answer
  const selected = card.querySelector('.q-option.selected');
  const correct = card.querySelector('.q-option[data-correct="true"]');

  if (correct) {{
    correct.classList.add('correct');
    if (selected && selected === correct) {{
      score++;
    }} else if (selected) {{
      selected.classList.add('incorrect');
    }}
  }}

  document.getElementById('score').textContent = score;
}}
</script>
</body>
</html>"""


def _render_cta(is_reflective, tid, questions):
    """Build the CTA block beneath the explainer: quiz link for assessable
    topics, reflective card for reflective ones. Returns HTML or empty."""
    if is_reflective:
        quiz_anyway = (
            f"<a href='{tid}-questions.html' class='quiz-anyway'>Quiz me anyway &rarr;</a>"
            if questions else ""
        )
        return (
            "<div class='section'><div class='reflective-card'>"
            "<h3>What did you take from this?</h3>"
            "<p class='reflective-sub'>"
            "Topics in reflective domains aren't scored by quiz answers. "
            "Read, reflect, and mark when you've thought it through."
            "</p>"
            "<textarea id='reflectionText' placeholder='Optional: a thought, a quote, a question it raised...'></textarea>"
            "<div class='reflective-actions'>"
            "<button class='mark-read-btn' id='markReadBtn' onclick='markAsRead()'>Mark as read</button>"
            + quiz_anyway +
            "</div></div></div>"
        )
    if questions:
        return (
            "<div class='section'>"
            f"<a href='{tid}-questions.html' class='questions-link'>"
            f"Practice Questions <span class='q-count'>{len(questions)} questions</span>"
            "</a></div>"
        )
    return ""


def generate_topic_page(tid, all_data, all_sections, prereqs_of, dependents_of, depths, pedagogy_types=None, og_cards=frozenset()):
    """Generate HTML for a single topic detail page.

    *og_cards* is the set of topic ids that have a rendered share card in
    output/og/ (see render_og_cards.py); others fall back to the default card.
    """
    data = all_data[tid]
    sections = all_sections.get(tid, {})

    title = data.get("title", tid)
    domain = data.get("domain", "")
    course = data.get("course", "")
    stage = data.get("stage", "")
    tags = data.get("tags", [])

    hue = DOMAIN_HUES.get(domain, 0)
    pedagogy = (pedagogy_types or {}).get(domain, "assessable")
    is_reflective = (pedagogy == "reflective")
    domain_label = domain.replace("-", " ").title()
    course_label = course.replace("-", " ").title()
    stage_label = STAGE_LABELS.get(stage, stage)
    depth = depths.get(tid, 0)

    # Body sections
    core_idea = sections.get("Core Idea", "")
    how_learned = sections.get("How It's Best Learned", "")
    misconceptions = sections.get("Common Misconceptions", "")
    notes = sections.get("Notes", "")
    explainer = sections.get("Explainer", "")
    questions_raw = sections.get("Questions", "")
    questions = parse_questions_yaml(questions_raw)

    # Prerequisites
    direct_prereqs = prereqs_of.get(tid, [])
    chain = find_longest_chain(tid, prereqs_of, all_data)
    total_transitive = count_transitive_prereqs(tid, prereqs_of)

    # Successors
    direct_successors = dependents_of.get(tid, [])
    total_downstream = count_transitive_successors(tid, dependents_of)

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
            f'<a href="tags/{tag_to_slug(t)}.html" class="tag">{html_mod.escape(str(t))}</a>' for t in tags
        )

    # A6: hero stats row + "see on map" button
    stat_bits = []
    if total_downstream > 0:
        stat_bits.append(
            f'<div class="hero-stat"><span class="stat-num">{total_downstream:,}</span>'
            f'<span class="stat-label">topic{"s" if total_downstream != 1 else ""} build on this</span></div>')
    if total_transitive > 0:
        stat_bits.append(
            f'<div class="hero-stat"><span class="stat-num">{total_transitive:,}</span>'
            f'<span class="stat-label">prerequisite{"s" if total_transitive != 1 else ""} beneath it</span></div>')
    else:
        stat_bits.append(
            '<div class="hero-stat"><span class="stat-num">0</span>'
            '<span class="stat-label">prerequisites &mdash; a starting point</span></div>')
    stat_bits.append(f'<a class="map-btn" href="../radial-graph.html?focus={tid}">See this on the map &rarr;</a>')
    hero_stats_html = '<div class="hero-stats">' + "".join(stat_bits) + '</div>'

    # A6: compact neighbor strip — direct prereqs -> this topic -> successors
    def _strip_pill(pid):
        ptitle = all_data[pid].get("title", pid) if pid in all_data else pid
        pdomain = all_data[pid].get("domain", "") if pid in all_data else ""
        phue = DOMAIN_HUES.get(pdomain, 0)
        return (f'<a href="{pid}.html" class="chain-node" '
                f'style="border-color:hsl({phue},40%,40%)">{html_mod.escape(ptitle)}</a>')

    prereqs_by_rank = sorted(
        direct_prereqs,
        key=lambda x: (x[1] != "hard", all_data.get(x[0], {}).get("title", x[0])))
    succs_by_rank = sorted(
        direct_successors,
        key=lambda x: all_data.get(x[0], {}).get("title", x[0]))
    strip_bits = []
    if prereqs_by_rank:
        strip_bits.append("".join(_strip_pill(pid) for pid, _ in prereqs_by_rank[:2]))
        if len(prereqs_by_rank) > 2:
            strip_bits.append(f'<a href="#prerequisites" class="chain-more">+{len(prereqs_by_rank) - 2} more</a>')
        strip_bits.append('<span class="chain-arrow">&rarr;</span>')
    # "You are here" as a node dot — the title is the h1 directly above
    strip_bits.append(f'<span class="strip-dot" title="{html_mod.escape(title, quote=True)}"></span>')
    if succs_by_rank:
        strip_bits.append('<span class="chain-arrow">&rarr;</span>')
        strip_bits.append("".join(_strip_pill(sid) for sid, _ in succs_by_rank[:2]))
        if len(succs_by_rank) > 2:
            strip_bits.append(f'<a href="#leads-to" class="chain-more">+{len(succs_by_rank) - 2} more</a>')
    neighbor_strip_html = '<div class="neighbor-strip">' + "".join(strip_bits) + '</div>'

    # SEO: meta description from Core Idea, plus LearningResource JSON-LD
    description = meta_description(core_idea) or f"{title} — {course_label}, {domain_label}. Prerequisites and learning path on the Open Knowledge Graph."
    og_image = f"{SITE_BASE_URL}/og/{tid}.png" if tid in og_cards else None
    seo_block = seo_meta_tags(f"{title} — Open Knowledge Graph", description,
                              f"topics/{tid}.html", og_type="article", image=og_image)
    hard_prereq_titles = [
        all_data[pid].get("title", pid) for pid, ptype in direct_prereqs
        if ptype == "hard" and pid in all_data
    ]
    json_ld = {
        "@context": "https://schema.org",
        "@type": "LearningResource",
        "name": title,
        "description": description,
        "url": f"{SITE_BASE_URL}/topics/{tid}.html",
        "inLanguage": "en",
        "isAccessibleForFree": True,
        "license": "https://creativecommons.org/licenses/by-sa/4.0/",
        "educationalLevel": stage_label,
        "teaches": title,
        "isPartOf": {"@type": "Course", "name": course_label, "about": domain_label},
    }
    if hard_prereq_titles:
        json_ld["competencyRequired"] = hard_prereq_titles
    # Escape "</" so content containing "</script>" can't terminate the block
    json_ld_script = ('<script type="application/ld+json">'
                      + json.dumps(json_ld, ensure_ascii=False).replace('</', r'<\/')
                      + '</script>')

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{html_mod.escape(title)} — Open Knowledge Graph</title>
{seo_block}
{json_ld_script}
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
.breadcrumb a {{
  color:#89a; text-decoration:none; border-bottom:1px solid transparent;
  transition: color 0.2s, border-color 0.2s;
}}
.breadcrumb a:hover {{ color:#acd; border-bottom-color:#acd; }}
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
  text-decoration:none; transition:border-color 0.2s, color 0.2s;
}}
.tag:hover {{ border-color:#444; color:#aab; text-decoration:none; }}

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

.fluency-toggle {{
  display:inline-flex; align-items:center; gap:8px;
  padding:5px 14px; border-radius:16px;
  background:#151525; border:1px solid #252540;
  cursor:pointer; font-size:12px; color:#778;
  transition:all 0.2s; user-select:none;
}}
.fluency-toggle:hover {{ border-color:#444; color:#aab; }}
.fluency-toggle.known {{
  background:rgba(80,180,80,0.15); border-color:rgba(80,180,80,0.4);
  color:#6c6;
}}
.fluency-toggle .check {{ font-size:14px; }}
.fluency-score {{
  font-size:11px; color:#556; margin-left:4px;
}}

.goal-toggle {{
  display:inline-flex; align-items:center; gap:6px;
  padding:5px 14px; border-radius:16px;
  background:#151525; border:1px solid #252540;
  cursor:pointer; font-size:12px; color:#778;
  transition:all 0.2s; user-select:none;
}}
.goal-toggle:hover {{ border-color:#444; color:#aab; }}
.goal-toggle.active {{
  background:rgba(220,180,50,0.15); border-color:rgba(220,180,50,0.4);
  color:#db4;
}}
.goal-toggle .star {{ font-size:14px; }}

.site-context {{
  font-size:12.5px; color:#556; margin-bottom:20px;
}}
.site-context a {{ color:#7ab; }}

.hero-stats {{
  display:flex; gap:28px; align-items:center; flex-wrap:wrap;
  background:#0e0e1a; border:1px solid #1a1a2e; border-radius:8px;
  padding:14px 20px; margin:4px 0 14px;
}}
.hero-stat {{ display:flex; flex-direction:column; }}
.hero-stat .stat-num {{
  font-size:22px; font-weight:700; color:hsl({hue},55%,62%); line-height:1.2;
}}
.hero-stat .stat-label {{ font-size:11.5px; color:#667; }}
.map-btn {{
  margin-left:auto; font-size:13px; font-weight:600;
  color:hsl({hue},55%,65%); border:1px solid hsl({hue},35%,30%);
  padding:8px 14px; border-radius:6px; white-space:nowrap;
  transition:background 0.2s, border-color 0.2s;
}}
.map-btn:hover {{
  background:hsl({hue},35%,14%); border-color:hsl({hue},45%,45%);
  text-decoration:none;
}}

.neighbor-strip {{
  overflow-x:auto; white-space:nowrap;
  margin-bottom:18px; padding-bottom:4px;
}}
.neighbor-strip .chain-node {{
  margin-right:4px; max-width:190px;
  overflow:hidden; text-overflow:ellipsis; vertical-align:middle;
}}
.strip-dot {{
  display:inline-block; width:13px; height:13px; border-radius:50%;
  background:hsl({hue},60%,58%);
  box-shadow:0 0 10px hsla({hue},60%,58%,0.8);
  vertical-align:middle; margin:0 4px;
}}
.chain-more {{
  display:inline-block; font-size:12px; color:#667;
  padding:4px 8px; margin-right:4px; text-decoration:none;
}}
.chain-more:hover {{ color:#9cd; }}

.explainer-section {{
  background:#0e0e1a; border:1px solid #1a1a2e;
  border-radius:8px; padding:24px 28px;
  margin-bottom:32px;
}}
.explainer-section h2 {{
  font-size:16px; color:#889; text-transform:uppercase;
  letter-spacing:0.5px; margin-bottom:16px;
  padding-bottom:6px; border-bottom:1px solid #1a1a2e;
}}
.explainer-section p {{
  margin-bottom:12px; color:#bcc; font-size:15px; line-height:1.7;
}}
.explainer-section p:last-child {{ margin-bottom:0; }}

.questions-link {{
  display:inline-flex; align-items:center; gap:8px;
  padding:10px 20px;
  background:hsl({hue},30%,15%); border:1px solid hsl({hue},30%,25%);
  border-radius:8px; color:hsl({hue},50%,70%);
  font-size:14px; font-weight:600;
  text-decoration:none;
  transition:background 0.2s, border-color 0.2s;
}}
.questions-link:hover {{
  background:hsl({hue},30%,20%); border-color:hsl({hue},40%,35%);
  text-decoration:none; color:hsl({hue},50%,80%);
}}
.questions-link .q-count {{
  font-size:12px; font-weight:400; color:hsl({hue},30%,55%);
}}

.reflective-card {{
  background:rgba(20,22,32,0.6); border:1px solid hsl({hue},20%,25%);
  border-radius:10px; padding:20px 22px; margin-top:8px;
}}
.reflective-card h3 {{
  font-size:15px; color:hsl({hue},40%,72%); margin-bottom:6px;
  font-weight:600;
}}
.reflective-card .reflective-sub {{
  font-size:12px; color:#778; margin-bottom:14px;
}}
.reflective-card textarea {{
  width:100%; min-height:84px;
  background:rgba(0,0,0,0.3); border:1px solid #26263a;
  border-radius:6px; padding:9px 11px;
  color:#ccc; font-family:inherit; font-size:14px;
  resize:vertical; outline:none;
}}
.reflective-card textarea:focus {{
  border-color:hsl({hue},30%,40%);
}}
.reflective-card .reflective-actions {{
  display:flex; gap:14px; align-items:center; margin-top:12px;
  flex-wrap:wrap;
}}
.reflective-card .mark-read-btn {{
  background:hsl({hue},30%,25%); color:hsl({hue},55%,78%);
  border:1px solid hsl({hue},35%,38%);
  padding:9px 20px; border-radius:6px;
  font-size:13px; font-weight:600; cursor:pointer;
  transition:background 0.15s, color 0.15s;
}}
.reflective-card .mark-read-btn:hover {{
  background:hsl({hue},35%,32%); color:hsl({hue},60%,86%);
}}
.reflective-card .mark-read-btn.done {{
  background:rgba(80,160,80,0.18); color:#8d8; border-color:rgba(80,160,80,0.45);
}}
.reflective-card .quiz-anyway {{
  color:#677; font-size:12px; text-decoration:none;
  border-bottom:1px dotted #445;
}}
.reflective-card .quiz-anyway:hover {{ color:#9aa; border-bottom-color:#667; }}
</style>
</head>
<body>
<div class="container">

<div class="nav">
  <a href="../radial-graph.html">← Graph View</a>
  <a href="../index.html">All Domains</a>
</div>

<p class="site-context">A topic in the <a href="../index.html">Open Knowledge Graph</a> — a free, open map of {len(all_data):,} topics and the order to learn them in.</p>

<div class="breadcrumb">
  <a href="../{domain}-map.html">{html_mod.escape(domain_label)}</a> <span>›</span> <a href="../{domain}-map.html#{course}">{html_mod.escape(course_label)}</a>
</div>

<h1>{html_mod.escape(title)}</h1>

<div class="meta-row">
  <span class="stage-badge">{html_mod.escape(stage_label)}</span>
  <span class="depth-info">Depth {depth} in the knowledge graph</span>
  <span class="fluency-toggle" id="fluencyToggle" onclick="toggleKnown()">
    <span class="check" id="fluencyCheck">&#9744;</span>
    <span id="fluencyLabel">I know this</span>
    <span class="fluency-score" id="fluencyScore"></span>
  </span>
  <span class="goal-toggle" id="goalToggle" onclick="toggleGoal()">
    <span class="star" id="goalStar">&#9734;</span>
    <span id="goalLabel">Set as goal</span>
  </span>
</div>

{hero_stats_html}

{neighbor_strip_html}

{"<div class='tags'>" + tags_html + "</div>" if tags_html else ""}

<div class="section">
  <h2>Core Idea</h2>
  {markdown_to_html(core_idea) if core_idea else '<p class="empty-state">No description available yet.</p>'}
</div>

{"<div class='section'><h2>How It's Best Learned</h2>" + markdown_to_html(how_learned) + "</div>" if how_learned else ""}

{"<div class='section'><h2>Common Misconceptions</h2>" + markdown_to_html(misconceptions) + "</div>" if misconceptions else ""}

{"<div class='section'><h2>Notes</h2>" + markdown_to_html(notes) + "</div>" if notes else ""}

{"<div class='explainer-section'><h2>Explainer</h2>" + markdown_to_html(explainer) + "</div>" if explainer else ""}

{_render_cta(is_reflective, tid, questions)}

<div class="section">
  <h2>Prerequisite Chain</h2>
  {('<div class="chain-container">' + chain_html + '</div><p class="chain-meta">Longest path: ' + str(len(chain)) + ' steps &middot; ' + str(total_transitive) + ' total prerequisite topics</p>') if len(chain) > 1 else '<p class="empty-state">This is a foundational topic with no prerequisites.</p>'}
</div>

<div class="section" id="prerequisites">
  <h2>Prerequisites ({len(direct_prereqs)})</h2>
  {('<div class="prereq-list">' + prereq_html + '</div>') if prereq_html else '<p class="empty-state">No prerequisites — this is a starting point.</p>'}
</div>

<div class="section" id="leads-to">
  <h2>Leads To ({len(direct_successors)})</h2>
  {('<div class="prereq-list">' + successor_html + '</div>') if successor_html else '<p class="empty-state">No topics depend on this one yet.</p>'}
</div>

</div>

<script src="../js/fluency.js"></script>
<script>
(function() {{
  var TOPIC_ID = "{tid}";
  var toggle = document.getElementById("fluencyToggle");
  var check = document.getElementById("fluencyCheck");
  var label = document.getElementById("fluencyLabel");
  var scoreEl = document.getElementById("fluencyScore");

  function render() {{
    if (typeof OKGFluency === "undefined") {{ toggle.style.display = "none"; return; }}
    var score = OKGFluency.getScore(TOPIC_ID);
    var known = score >= 50;
    toggle.classList.toggle("known", known);
    check.innerHTML = known ? "&#9745;" : "&#9744;";
    label.textContent = known ? "Known" : "I know this";
    scoreEl.textContent = score > 0 ? score + "%" : "";
  }}

  window.toggleKnown = function() {{
    if (typeof OKGFluency === "undefined") return;
    var score = OKGFluency.getScore(TOPIC_ID);
    OKGFluency.setScore(TOPIC_ID, score >= 50 ? 0 : 85);
    render();
  }};

  // --- Reflective card ("mark as read" + optional reflection text) ---
  var REFLECTIONS_KEY = "okg-reflections";
  function loadReflections() {{
    try {{ return JSON.parse(localStorage.getItem(REFLECTIONS_KEY) || "{{}}"); }}
    catch (e) {{ return {{}}; }}
  }}
  function saveReflections(obj) {{
    try {{ localStorage.setItem(REFLECTIONS_KEY, JSON.stringify(obj)); }}
    catch (e) {{}}
  }}

  var reflectionText = document.getElementById("reflectionText");
  if (reflectionText) {{
    var rs = loadReflections();
    if (rs[TOPIC_ID]) reflectionText.value = rs[TOPIC_ID];
    // Persist on blur (avoid thrashing localStorage on every keystroke)
    reflectionText.addEventListener("blur", function () {{
      var store = loadReflections();
      var val = this.value.trim();
      if (val) store[TOPIC_ID] = val;
      else delete store[TOPIC_ID];
      saveReflections(store);
    }});
  }}

  window.markAsRead = function() {{
    if (typeof OKGFluency === "undefined") return;
    OKGFluency.setScore(TOPIC_ID, 100);
    // Persist any text the user typed but didn't blur yet
    if (reflectionText && reflectionText.value.trim()) {{
      var store = loadReflections();
      store[TOPIC_ID] = reflectionText.value.trim();
      saveReflections(store);
    }}
    var btn = document.getElementById("markReadBtn");
    if (btn) {{
      btn.textContent = "Marked as read \u2713";
      btn.classList.add("done");
    }}
    render();
  }};

  // --- Goal toggle ---
  var goalToggle = document.getElementById("goalToggle");
  var goalStar = document.getElementById("goalStar");
  var goalLabel = document.getElementById("goalLabel");

  function renderGoal() {{
    if (typeof OKGFluency === "undefined") {{ goalToggle.style.display = "none"; return; }}
    var isGoal = OKGFluency.isGoal(TOPIC_ID);
    goalToggle.classList.toggle("active", isGoal);
    goalStar.innerHTML = isGoal ? "&#9733;" : "&#9734;";
    goalLabel.textContent = isGoal ? "Goal" : "Set as goal";
  }}

  window.toggleGoal = function() {{
    if (typeof OKGFluency === "undefined") return;
    if (OKGFluency.isGoal(TOPIC_ID)) {{
      OKGFluency.removeGoal(TOPIC_ID);
    }} else {{
      OKGFluency.addGoal(TOPIC_ID);
    }}
    renderGoal();
  }};

  render();
  renderGoal();
}})();
</script>
</body>
</html>"""


def tag_to_slug(tag):
    """Convert a tag to a safe filename slug."""
    slug = str(tag).lower().strip()
    slug = re.sub(r'[^\w\s-]', '', slug)  # Remove special chars except hyphens
    slug = re.sub(r'[\s_]+', '-', slug)   # Spaces/underscores to hyphens
    slug = re.sub(r'-+', '-', slug).strip('-')
    return slug or 'other'


def build_tag_index(all_data):
    """Build a mapping of tag -> list of topic IDs."""
    tag_map = defaultdict(list)
    for tid, data in all_data.items():
        for tag in data.get("tags", []):
            tag_map[str(tag).lower()].append(tid)
    return tag_map


def generate_tag_page(tag, topic_ids, all_data):
    """Generate an HTML page listing all topics with a given tag."""
    # Sort topics by domain, then title
    sorted_topics = sorted(
        topic_ids,
        key=lambda tid: (
            all_data[tid].get("domain", ""),
            all_data[tid].get("title", tid),
        ),
    )

    # Group by domain
    by_domain = defaultdict(list)
    for tid in sorted_topics:
        by_domain[all_data[tid].get("domain", "other")].append(tid)

    items_html = []
    for domain in sorted(by_domain.keys()):
        domain_label = domain.replace("-", " ").title()
        hue = DOMAIN_HUES.get(domain, 0)
        items_html.append(
            f'<div class="domain-group">'
            f'<h3 style="color:hsl({hue},50%,65%)">{html_mod.escape(domain_label)}</h3>'
        )
        for tid in by_domain[domain]:
            title = all_data[tid].get("title", tid)
            stage = all_data[tid].get("stage", "")
            stage_label = STAGE_LABELS.get(stage, stage)
            items_html.append(
                f'<a href="../{tid}.html" class="topic-card">'
                f'<span class="topic-dot" style="background:hsl({hue},55%,50%)"></span>'
                f'<span class="topic-title">{html_mod.escape(title)}</span>'
                f'<span class="topic-stage">{html_mod.escape(stage_label)}</span>'
                f'</a>'
            )
        items_html.append('</div>')

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Tag: {html_mod.escape(tag)} — Open Knowledge Graph</title>
{ANALYTICS_SNIPPET}
<style>
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{
  background:#0a0a14; color:#ccc;
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;
  line-height:1.6;
}}
a {{ color:#7ab; text-decoration:none; }}
a:hover {{ color:#9cd; text-decoration:underline; }}
.container {{ max-width:820px; margin:0 auto; padding:40px 24px 80px; }}
.nav {{
  display:flex; gap:12px; margin-bottom:32px; font-size:13px;
}}
.nav a {{
  color:#556; padding:4px 10px;
  border:1px solid #222; border-radius:4px;
  transition:border-color 0.2s;
}}
.nav a:hover {{ border-color:#555; color:#aaa; text-decoration:none; }}
h1 {{ font-size:24px; color:#eee; margin-bottom:4px; }}
.subtitle {{ font-size:14px; color:#667; margin-bottom:28px; }}
.domain-group {{ margin-bottom:24px; }}
.domain-group h3 {{
  font-size:13px; text-transform:uppercase; letter-spacing:0.5px;
  margin-bottom:8px; padding-bottom:4px; border-bottom:1px solid #1a1a2e;
}}
.topic-card {{
  display:flex; align-items:center; gap:10px;
  padding:8px 14px;
  background:#0e0e1a; border:1px solid #1a1a2e;
  border-radius:6px; text-decoration:none;
  margin-bottom:4px;
  transition:border-color 0.2s, background 0.2s;
}}
.topic-card:hover {{ border-color:#333; background:#12122a; text-decoration:none; }}
.topic-dot {{ width:8px; height:8px; border-radius:50%; flex-shrink:0; }}
.topic-title {{ flex:1; color:#bbc; font-size:14px; }}
.topic-stage {{ font-size:11px; color:#556; }}
@media (max-width: 768px) {{
  .container {{ padding:20px 16px 60px; }}
  h1 {{ font-size:20px; }}
}}
</style>
</head>
<body>
<div class="container">
<div class="nav">
  <a href="../radial-graph.html">Graph View</a>
  <a href="../index.html">All Domains</a>
  <a href="index.html">All Tags</a>
</div>
<h1>#{html_mod.escape(tag)}</h1>
<p class="subtitle">{len(topic_ids)} topics</p>
{"".join(items_html)}
</div>
</body>
</html>"""


def generate_tag_index(tag_map):
    """Generate an index page listing all tags with topic counts."""
    # Sort tags by topic count (descending), then alphabetically
    sorted_tags = sorted(tag_map.keys(), key=lambda t: (-len(tag_map[t]), t))

    items = []
    for tag in sorted_tags:
        count = len(tag_map[tag])
        items.append(
            f'<a href="{tag_to_slug(tag)}.html" class="tag-card">'
            f'<span class="tag-name">{html_mod.escape(tag)}</span>'
            f'<span class="tag-count">{count}</span>'
            f'</a>'
        )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Tags — Open Knowledge Graph</title>
{ANALYTICS_SNIPPET}
<style>
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{
  background:#0a0a14; color:#ccc;
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;
  line-height:1.6;
}}
a {{ color:#7ab; text-decoration:none; }}
a:hover {{ color:#9cd; text-decoration:underline; }}
.container {{ max-width:820px; margin:0 auto; padding:40px 24px 80px; }}
.nav {{
  display:flex; gap:12px; margin-bottom:32px; font-size:13px;
}}
.nav a {{
  color:#556; padding:4px 10px;
  border:1px solid #222; border-radius:4px;
  transition:border-color 0.2s;
}}
.nav a:hover {{ border-color:#555; color:#aaa; text-decoration:none; }}
h1 {{ font-size:24px; color:#eee; margin-bottom:4px; }}
.subtitle {{ font-size:14px; color:#667; margin-bottom:28px; }}
.tag-grid {{
  display:flex; flex-wrap:wrap; gap:8px;
}}
.tag-card {{
  display:inline-flex; align-items:center; gap:8px;
  padding:6px 14px;
  background:#0e0e1a; border:1px solid #1a1a2e;
  border-radius:6px; text-decoration:none;
  transition:border-color 0.2s, background 0.2s;
}}
.tag-card:hover {{ border-color:#333; background:#12122a; text-decoration:none; }}
.tag-name {{ color:#bbc; font-size:14px; }}
.tag-count {{
  font-size:11px; color:#556;
  background:#151525; padding:1px 6px; border-radius:10px;
}}
@media (max-width: 768px) {{
  .container {{ padding:20px 16px 60px; }}
  h1 {{ font-size:20px; }}
}}
</style>
</head>
<body>
<div class="container">
<div class="nav">
  <a href="../radial-graph.html">Graph View</a>
  <a href="../index.html">All Domains</a>
</div>
<h1>Tags</h1>
<p class="subtitle">{len(tag_map)} tags across {sum(len(v) for v in tag_map.values())} topic-tag pairs</p>
<div class="tag-grid">
{"".join(items)}
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

    pedagogy_types = load_pedagogy_types()
    reflective_domains = sorted(d for d, t in pedagogy_types.items() if t == "reflective")
    print(f"Reflective domains: {', '.join(reflective_domains)}")

    TOPICS_DIR.mkdir(parents=True, exist_ok=True)

    # Share cards rendered earlier in CI by render_og_cards.py; topics with a
    # card get a per-topic og:image, the rest fall back to the default card.
    og_cards = frozenset(p.stem for p in (OUTPUT_DIR / "og").glob("*.png")) - {"default"}
    print(f"Found {len(og_cards)} rendered og:image cards")

    print(f"Generating {len(all_data)} topic pages...")
    count = 0
    q_count = 0
    for tid in sorted(all_data.keys()):
        html = generate_topic_page(
            tid, all_data, all_sections, prereqs_of, dependents_of, depths,
            pedagogy_types=pedagogy_types, og_cards=og_cards,
        )
        out = TOPICS_DIR / f"{tid}.html"
        out.write_text(html, encoding="utf-8")
        count += 1

        # Generate questions page if topic has questions
        sections = all_sections.get(tid, {})
        questions_raw = sections.get("Questions", "")
        questions = parse_questions_yaml(questions_raw)
        if questions:
            q_html = generate_questions_page(tid, all_data, all_sections, questions)
            q_out = TOPICS_DIR / f"{tid}-questions.html"
            q_out.write_text(q_html, encoding="utf-8")
            q_count += 1

        if count % 500 == 0:
            print(f"  {count}/{len(all_data)}...")

    # Generate tag pages
    print("Building tag index...")
    tag_map = build_tag_index(all_data)
    tags_dir = TOPICS_DIR / "tags"
    tags_dir.mkdir(exist_ok=True)

    for tag, tids in tag_map.items():
        tag_html = generate_tag_page(tag, tids, all_data)
        tag_out = tags_dir / f"{tag_to_slug(tag)}.html"
        tag_out.write_text(tag_html, encoding="utf-8")

    # Tag index page
    index_html = generate_tag_index(tag_map)
    (tags_dir / "index.html").write_text(index_html, encoding="utf-8")

    # Copy fluency.js to output
    fluency_src = ROOT / "lib" / "fluency.js"
    if fluency_src.exists():
        fluency_dst = OUTPUT_DIR / "js" / "fluency.js"
        fluency_dst.parent.mkdir(parents=True, exist_ok=True)
        import shutil
        shutil.copy2(fluency_src, fluency_dst)

    print(f"Done! {count} topic pages + {q_count} question pages + {len(tag_map)} tag pages in {TOPICS_DIR}")


if __name__ == "__main__":
    main()
