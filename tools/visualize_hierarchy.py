#!/usr/bin/env python3
"""Generate hierarchical knowledge graph visualizations.

Produces Math Academy-style graph(s):
- Small dot nodes colored by course, packed tightly
- Y-position determined by course order (basics at top, advanced at bottom)
- Force simulation for X-spreading within each rank
- Dense cross-connections visible
- Labels appear on hover only
- Interactive zoom/pan

Usage:
    python tools/visualize_hierarchy.py --domain mathematics
    python tools/visualize_hierarchy.py --domain physics
    python tools/visualize_hierarchy.py --course algebra-1
    python tools/visualize_hierarchy.py --all          # Generate one HTML per domain + index
    python tools/visualize_hierarchy.py                # Full cross-domain graph
"""

import sys
import re
import json
import argparse
import colorsys
import math
import random
from pathlib import Path
from collections import defaultdict, deque


def smart_title(slug):
    """Title-case a slug, but don't capitalize letters after digits (1st, 2nd, 3rd)."""
    words = slug.replace("-", " ").split()
    return " ".join(w if w[0].isdigit() else w.capitalize() for w in words if w)

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML required. Install with: pip install pyyaml")
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent
DOMAINS_DIR = ROOT / "domains"
OUTPUT_DIR = ROOT / "output"

# Domain hue assignments (evenly spaced around the color wheel)
DOMAIN_HUES = {
    "mathematics": 0.10,
    "computer-science": 0.55,
    "physics": 0.60,
    "chemistry": 0.00,
    "biology": 0.30,
    "earth-and-space-sciences": 0.48,
    "engineering": 0.08,
    "economics": 0.14,
    "psychology": 0.75,
    "health-and-human-development": 0.35,
    "history": 0.05,
    "philosophy": 0.68,
    "social-sciences": 0.18,
    "language-and-communication": 0.42,
    "literature": 0.85,
    "music": 0.78,
    "arts-and-aesthetics": 0.92,
    "formal-sciences-and-logic": 0.52,
    "practical-life-skills": 0.22,
}

# --- Scatter X-axis domain ordering ---
# Folded-curated: humanities left, math center, STEM right.
# Derived via dialectic process (10 proposers, 4 counters, 3 judges).
# Score: 3,206 linear edge distance (45.8% improvement over curated-as-linear).
DOMAIN_ORDER = [
    "history",
    "arts-and-aesthetics",
    "literature",
    "language-and-communication",
    "music",
    "practical-life-skills",
    "psychology",
    "social-sciences",
    "economics",
    "mathematics",
    "computer-science",
    "formal-sciences-and-logic",
    "engineering",
    "physics",
    "chemistry",
    "earth-and-space-sciences",
    "biology",
    "health-and-human-development",
    "philosophy",
]

# --- Developmental stage ordering (Y-axis) ---
# Band heights are computed dynamically (proportional to topic count, with floor).
# This list defines the ORDER only.
STAGE_ORDER = [
    "pre-formal",
    "concrete-operations",
    "abstract-reasoning",
    "formal-systems",
    "advanced",
]
DEFAULT_STAGE = "abstract-reasoning"
# Minimum band height as fraction of canvas (prevents tiny stages from being illegible)
MIN_BAND_FRAC = 0.07

# Domain hues in HSL degrees (hand-tuned, from radial view)
SCATTER_HUES = {
    "mathematics": 42,
    "formal-sciences-and-logic": 185,
    "philosophy": 260,
    "computer-science": 200,
    "engineering": 28,
    "physics": 215,
    "chemistry": 0,
    "earth-and-space-sciences": 170,
    "biology": 120,
    "health-and-human-development": 148,
    "psychology": 280,
    "social-sciences": 60,
    "economics": 48,
    "practical-life-skills": 80,
    "history": 18,
    "language-and-communication": 155,
    "literature": 310,
    "arts-and-aesthetics": 335,
    "music": 290,
}


def generate_course_colors(domain, courses):
    """Generate distinct colors for courses within a domain.

    Uses the domain's base hue and varies saturation/lightness per course.
    """
    base_hue = DOMAIN_HUES.get(domain, 0.5)
    n = len(courses)
    colors = {}
    for i, course_id in enumerate(courses):
        # Vary hue slightly within domain range, plus saturation/lightness
        hue = (base_hue + (i / max(n, 1)) * 0.12 - 0.06) % 1.0
        sat = 0.55 + (i % 3) * 0.15
        light = 0.50 + ((i // 3) % 2) * 0.12
        r, g, b = colorsys.hls_to_rgb(hue, light, sat)
        colors[course_id] = f"#{int(r*255):02x}{int(g*255):02x}{int(b*255):02x}"
    return colors


def load_domain_config(domain):
    """Load course list and ordering from _domain.yml."""
    domain_file = DOMAINS_DIR / domain / "_domain.yml"
    if not domain_file.exists():
        return [], {}
    data = yaml.safe_load(domain_file.read_text(encoding="utf-8"))
    courses = data.get("courses", [])
    course_ids = [c["id"] for c in courses if isinstance(c, dict) and "id" in c]
    course_titles = {c["id"]: c.get("title", c["id"]) for c in courses if isinstance(c, dict)}
    return course_ids, course_titles


def load_all_domain_configs():
    """Load configs for all domains."""
    configs = {}
    for domain_dir in sorted(DOMAINS_DIR.iterdir()):
        if domain_dir.is_dir() and (domain_dir / "_domain.yml").exists():
            course_ids, course_titles = load_domain_config(domain_dir.name)
            configs[domain_dir.name] = {
                "course_ids": course_ids,
                "course_titles": course_titles,
            }
    return configs


def parse_frontmatter(filepath):
    text = filepath.read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not match:
        return None
    try:
        return yaml.safe_load(match.group(1))
    except yaml.YAMLError:
        return None


def get_topic_stage(data, configs):
    """Determine a topic's developmental stage from its own field or its course config."""
    stage = data.get("stage", "")
    if stage and stage in STAGE_ORDER:
        return stage
    domain = data.get("domain", "")
    course = data.get("course", "")
    if domain in configs:
        for c in configs[domain].get("courses", []):
            cid = c["id"] if isinstance(c, dict) else c
            cstage = c.get("stage", DEFAULT_STAGE) if isinstance(c, dict) else DEFAULT_STAGE
            if cid == course:
                return cstage
    return DEFAULT_STAGE


def load_all_topics():
    """Load all topic frontmatter as dict keyed by ID."""
    all_data = {}
    for filepath in sorted(DOMAINS_DIR.rglob("*.md")):
        data = parse_frontmatter(filepath)
        if data and "id" in data:
            all_data[data["id"]] = data
    return all_data


def load_graph(domain_filter=None, course_filter=None):
    nodes = {}
    edges = []

    for filepath in sorted(DOMAINS_DIR.rglob("*.md")):
        data = parse_frontmatter(filepath)
        if data is None or "id" not in data:
            continue

        domain = data.get("domain", "")
        course = data.get("course", "")

        if domain_filter and domain != domain_filter:
            continue
        if course_filter and course != course_filter:
            continue

        topic_id = data["id"]
        tags = data.get("tags", [])
        nodes[topic_id] = {
            "id": topic_id,
            "title": data.get("title", topic_id),
            "domain": domain,
            "course": course,
            "stage": data.get("stage", ""),
            "tags": [str(t).lower() for t in tags] if tags else [],
        }

        for prereq in data.get("prerequisites", []):
            if isinstance(prereq, dict) and "id" in prereq:
                edges.append({
                    "source": prereq["id"],
                    "target": topic_id,
                    "type": prereq.get("type", "hard"),
                })

    # Filter edges to only include nodes in our set
    # For single-domain view, include phantom nodes for cross-domain prereqs
    all_ids = set(nodes.keys())
    if domain_filter:
        # Add phantom nodes for external prereqs so edges render
        for edge in edges:
            if edge["source"] not in all_ids:
                nodes[edge["source"]] = {
                    "id": edge["source"],
                    "title": smart_title(edge["source"]),
                    "domain": "external",
                    "course": "external",
                    "stage": "",
                }
                all_ids.add(edge["source"])

    edges = [e for e in edges if e["source"] in all_ids and e["target"] in all_ids]
    return list(nodes.values()), edges


def compute_depths(nodes, edges):
    """Compute topological depth for each node (longest path from any root)."""
    children = defaultdict(list)
    in_degree = defaultdict(int)

    for e in edges:
        children[e["source"]].append(e["target"])
        in_degree[e["target"]] += 1

    depth = {}
    queue = deque()
    for n in nodes:
        nid = n["id"]
        if in_degree[nid] == 0:
            depth[nid] = 0
            queue.append(nid)

    while queue:
        nid = queue.popleft()
        for child in children[nid]:
            new_depth = depth.get(nid, 0) + 1
            if child not in depth or new_depth > depth[child]:
                depth[child] = new_depth
                queue.append(child)

    for n in nodes:
        if n["id"] not in depth:
            depth[n["id"]] = 0

    return depth


def compute_depths_from_data(all_data):
    """Compute topological depth from raw topic data dict (like radial view)."""
    children_of = defaultdict(list)
    in_degree = defaultdict(int)
    for tid, data in all_data.items():
        for p in data.get("prerequisites", []):
            if isinstance(p, dict) and "id" in p:
                pid = p["id"]
                if pid in all_data:
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


def compute_proportional_bands(stage_counts, canvas_height):
    """Compute proportional stage band boundaries with minimum height floor."""
    total = sum(stage_counts.get(s, 0) for s in STAGE_ORDER)
    if total == 0:
        total = 1

    # Raw proportional heights
    raw = {}
    for s in STAGE_ORDER:
        raw[s] = max(stage_counts.get(s, 0) / total, 0.001)

    # Apply minimum floor, redistribute from largest bands
    min_frac = MIN_BAND_FRAC
    heights = dict(raw)
    deficit = 0
    for s in STAGE_ORDER:
        if heights[s] < min_frac:
            deficit += min_frac - heights[s]
            heights[s] = min_frac

    if deficit > 0:
        # Take from bands above the floor, proportionally
        above = {s: h for s, h in heights.items() if h > min_frac}
        above_total = sum(above.values())
        if above_total > 0:
            for s in above:
                heights[s] -= deficit * (above[s] / above_total)

    # Build band boundaries with thin overlap zones
    overlap = 15 / canvas_height  # 15px overlap between adjacent bands
    bands = {}
    current_y = 0.01  # small top margin
    for i, s in enumerate(STAGE_ORDER):
        band_start = current_y - (overlap if i > 0 else 0)
        band_end = current_y + heights[s]
        bands[s] = (band_start, band_end)
        current_y = band_end

    return bands


def build_scatter_layout(all_data, configs, depths):
    """Compute (x, y) positions for scatter layout.

    X = domain similarity (folded-curated ordering, proportional sectors)
    Y = developmental stage bands (proportional to topic count) + depth within band
    """
    random.seed(42)

    domain_order = [d for d in DOMAIN_ORDER if d in configs]
    n_domains = len(domain_order)

    # X-axis: domain sectors proportional to topic count
    domain_counts = defaultdict(int)
    for data in all_data.values():
        domain_counts[data.get("domain", "")] += 1
    total_topics = sum(domain_counts[d] for d in domain_order)

    gap_width = 40
    total_gap = gap_width * (n_domains - 1) if n_domains > 1 else 0
    canvas_width = 4000
    usable_width = canvas_width - total_gap

    sectors = {}
    current_x = 0
    for d in domain_order:
        frac = domain_counts.get(d, 1) / max(total_topics, 1)
        sector_width = usable_width * frac
        sectors[d] = {
            "start": current_x,
            "end": current_x + sector_width,
            "mid": current_x + sector_width / 2,
            "width": sector_width,
        }
        current_x += sector_width + gap_width

    # Y-axis: proportional stage bands
    canvas_height = 3500

    # Resolve stages and compute per-stage depth ranges
    topic_stages = {}
    stage_counts = defaultdict(int)
    stage_depths = defaultdict(list)
    for tid, data in all_data.items():
        stage = get_topic_stage(data, configs)
        topic_stages[tid] = stage
        stage_counts[stage] += 1
        stage_depths[stage].append(depths.get(tid, 0))

    stage_depth_ranges = {}
    for stage, depth_list in stage_depths.items():
        stage_depth_ranges[stage] = (min(depth_list), max(depth_list))

    # Compute proportional band boundaries
    bands = compute_proportional_bands(stage_counts, canvas_height)

    # Assign initial positions
    positions = {}
    for tid, data in all_data.items():
        domain = data.get("domain", "")
        course = data.get("course", "")
        stage = topic_stages.get(tid, DEFAULT_STAGE)

        if domain not in sectors:
            continue

        # X: course sub-sector within domain
        sector = sectors[domain]
        course_list = configs.get(domain, {}).get("courses", [])
        course_ids = [c["id"] if isinstance(c, dict) else c for c in course_list]
        n_courses = len(course_ids)

        course_idx = course_ids.index(course) if course in course_ids else 0
        course_frac = (course_idx + 0.5) / max(n_courses, 1)

        base_x = sector["start"] + sector["width"] * course_frac
        x_jitter = (random.random() - 0.5) * sector["width"] / max(n_courses, 1) * 0.4
        x = base_x + x_jitter

        # Y: proportional stage band + normalized depth within band
        band_min, band_max = bands.get(stage, (0.35, 0.65))
        d_min, d_max = stage_depth_ranges.get(stage, (0, 1))
        d = depths.get(tid, 0)
        depth_frac = (d - d_min) / (d_max - d_min) if d_max > d_min else 0.5

        # Deterministic micro-jitter from topic ID hash (breaks Y collisions)
        id_hash = hash(tid) & 0xFFFFFFFF
        micro_jitter = ((id_hash % 1000) / 1000.0 - 0.5) * 0.02

        y_frac = band_min + (depth_frac + micro_jitter) * (band_max - band_min)
        y_frac = max(band_min, min(band_max, y_frac))
        base_y = y_frac * canvas_height
        y = base_y

        positions[tid] = {
            "x": x, "y": y,
            "baseX": base_x, "baseY": base_y,
        }

    # Force simulation
    edge_list = []
    for tid, data in all_data.items():
        if tid not in positions:
            continue
        for p in data.get("prerequisites", []):
            if isinstance(p, dict) and "id" in p:
                pid = p["id"]
                if pid in positions:
                    cross = data.get("domain", "") != all_data[pid].get("domain", "")
                    edge_list.append((pid, tid, cross))

    print("  Running scatter force simulation...")
    node_ids = list(positions.keys())
    iterations = 60

    for it in range(iterations):
        alpha = 0.5 * (1 - it / iterations)

        # Grid repulsion
        cell_size = 30
        grid = defaultdict(list)
        for tid in node_ids:
            p = positions[tid]
            grid[(int(p["x"] / cell_size), int(p["y"] / cell_size))].append(tid)

        for (gx, gy), cell in grid.items():
            neighbors = []
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    neighbors.extend(grid.get((gx + dx, gy + dy), []))
            for a_id in cell:
                pa = positions[a_id]
                for b_id in neighbors:
                    if a_id >= b_id:
                        continue
                    pb = positions[b_id]
                    ddx = pb["x"] - pa["x"]
                    ddy = pb["y"] - pa["y"]
                    dist = math.hypot(ddx, ddy)
                    min_dist = 14
                    if 0.01 < dist < min_dist:
                        force = (min_dist - dist) * 0.25 * alpha / dist
                        pa["x"] -= ddx * force
                        pa["y"] -= ddy * force
                        pb["x"] += ddx * force
                        pb["y"] += ddy * force

        # Edge attraction (stronger cross-domain)
        for src, tgt, cross in edge_list:
            ps, pt = positions[src], positions[tgt]
            dx = pt["x"] - ps["x"]
            dy = pt["y"] - ps["y"]
            strength = 0.006 if cross else 0.003
            fx = dx * strength * alpha
            fy = dy * strength * alpha
            ps["x"] += fx; ps["y"] += fy
            pt["x"] -= fx; pt["y"] -= fy

        # Spring back to base
        for tid in node_ids:
            p = positions[tid]
            p["x"] += (p["baseX"] - p["x"]) * 0.06
            p["y"] += (p["baseY"] - p["y"]) * 0.10

    return positions, sectors, domain_order, topic_stages, canvas_width, canvas_height, bands


def generate_html(nodes, edges, title="Open Knowledge Graph",
                  course_colors=None, course_order=None):
    if course_colors is None:
        course_colors = {}
    if course_order is None:
        course_order = []

    depths = compute_depths(nodes, edges)
    max_depth = max(depths.values()) if depths else 0
    default_color = "#AAAAAA"

    # Build course order index
    order_map = {c: i for i, c in enumerate(course_order)}

    for n in nodes:
        n["depth"] = depths.get(n["id"], 0)
        n["color"] = course_colors.get(n["course"], default_color)
        n["courseIdx"] = order_map.get(n["course"], len(course_order))

    nodes.sort(key=lambda n: (n["courseIdx"], n["depth"]))

    courses_present = sorted(
        set(n["course"] for n in nodes if n["course"] not in ("unknown", "external")),
        key=lambda c: order_map.get(c, 99)
    )

    legend_items = []
    for course in courses_present:
        color = course_colors.get(course, default_color)
        label = smart_title(course)
        legend_items.append({"color": color, "label": label})

    graph_json = json.dumps({
        "nodes": nodes,
        "edges": edges,
        "legend": legend_items,
        "maxDepth": max_depth,
    })

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
<title>{title}</title>
<style>
* {{ margin:0; padding:0; box-sizing:border-box; }}
html, body {{ overflow:hidden; touch-action:none; }}
body {{ background:#1a1a2e; font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif; color:#ccc; }}
canvas {{ display:block; position:relative; touch-action:none; }}
#legend {{
  position:fixed; bottom:16px; left:16px;
  background:rgba(26,26,46,0.92); border:1px solid #333;
  border-radius:8px; padding:10px 14px;
  z-index:10; pointer-events:auto;
  max-height:80vh; overflow-y:auto;
}}
#legend h3 {{ font-size:12px; color:#888; margin-bottom:6px; letter-spacing:0.5px; text-transform:uppercase; }}
.legend-row {{ display:flex; align-items:center; gap:6px; margin:2px 0; }}
.legend-dot {{ width:10px; height:10px; border-radius:50%; flex-shrink:0; }}
.legend-label {{ font-size:11px; color:#aaa; }}
#stats {{
  position:fixed; top:16px; left:16px;
  background:rgba(26,26,46,0.92); border:1px solid #333;
  border-radius:8px; padding:10px 14px; z-index:10;
}}
#stats h2 {{ font-size:14px; color:#ddd; margin-bottom:2px; }}
#stats p {{ font-size:11px; color:#777; }}
#tooltip {{
  position:fixed; display:none;
  background:rgba(30,30,50,0.95); border:1px solid #555;
  border-radius:6px; padding:8px 12px;
  z-index:20; pointer-events:none; max-width:300px;
}}
#tooltip h4 {{ font-size:12px; color:#eee; margin-bottom:3px; }}
#tooltip .meta {{ font-size:10px; color:#888; }}
#panel {{
  position:fixed; display:none;
  background:rgba(30,30,50,0.95); border:1px solid #555;
  border-radius:8px; padding:12px 16px;
  z-index:30; max-width:380px; max-height:70vh; overflow-y:auto;
}}
#panel .panel-close {{
  position:absolute; top:6px; right:10px;
  background:none; border:none; color:#888; font-size:20px;
  cursor:pointer; padding:2px 6px; line-height:1;
}}
#panel .panel-close:hover {{ color:#eee; }}
#panel h3 {{ font-size:14px; color:#eee; margin-bottom:4px; padding-right:24px; }}
#panel h3 a {{ color:#7af; text-decoration:none; }}
#panel h3 a:hover {{ text-decoration:underline; }}
#panel .panel-meta {{ font-size:10px; color:#888; margin-bottom:8px; }}
#panel .panel-section {{ margin-top:8px; }}
#panel .panel-section h4 {{ font-size:11px; color:#999; text-transform:uppercase; letter-spacing:0.5px; margin-bottom:4px; }}
#panel .panel-item {{
  display:flex; align-items:center; gap:6px;
  padding:3px 4px; border-radius:4px; cursor:pointer;
  transition:background 0.15s;
}}
#panel .panel-item:hover {{ background:rgba(255,255,255,0.08); }}
#panel .panel-dot {{ width:8px; height:8px; border-radius:50%; flex-shrink:0; }}
#panel .panel-title {{ font-size:12px; color:#ccc; flex:1; }}
#panel .panel-badge {{
  font-size:9px; padding:1px 5px; border-radius:3px;
  text-transform:uppercase; letter-spacing:0.3px; flex-shrink:0;
}}
.panel-badge.hard {{ background:rgba(255,100,100,0.2); color:#f88; }}
.panel-badge.soft {{ background:rgba(100,180,255,0.2); color:#8bf; }}
#controls {{
  position:fixed; top:16px; right:16px;
  background:rgba(26,26,46,0.92); border:1px solid #333;
  border-radius:8px; padding:6px 10px; z-index:10;
  display:flex; gap:4px;
}}
#controls button {{
  background:#2a2a4a; border:1px solid #444; border-radius:4px;
  padding:3px 10px; cursor:pointer; font-size:13px; color:#ccc;
}}
#controls button:hover {{ background:#3a3a5a; }}
#nav {{
  position:fixed; top:16px; left:50%; transform:translateX(-50%);
  background:rgba(26,26,46,0.92); border:1px solid #333;
  border-radius:8px; padding:6px 14px; z-index:10;
  display:flex; gap:12px;
}}
#nav a {{
  color:#aaa; text-decoration:none; font-size:13px;
  padding:2px 8px; border-radius:4px;
  transition:color 0.2s, background 0.2s;
}}
#nav a:hover {{ color:#eee; background:rgba(255,255,255,0.08); }}
#search {{
  position:fixed; bottom:16px; left:50%; transform:translateX(-50%);
  background:rgba(26,26,46,0.92); border:1px solid #333;
  border-radius:8px; padding:6px 14px; z-index:10;
  display:flex; gap:8px; align-items:center;
}}
#search input {{
  background:#2a2a4a; border:1px solid #444; border-radius:4px;
  padding:5px 10px; font-size:13px; color:#ccc; width:260px;
  outline:none;
}}
#search input:focus {{ border-color:#667; }}
#search .count {{ font-size:11px; color:#667; white-space:nowrap; }}
@media (max-width: 768px) {{
  #stats {{ padding:6px 10px; }}
  #stats h2 {{ font-size:12px; }}
  #stats p {{ font-size:10px; }}
  #legend {{ max-height:30vh; font-size:10px; padding:6px 10px; }}
  #legend h3 {{ font-size:10px; margin-bottom:4px; }}
  .legend-dot {{ width:8px; height:8px; }}
  .legend-label {{ font-size:10px; }}
  #nav {{ padding:4px 8px; gap:6px; }}
  #nav a {{ font-size:11px; padding:2px 4px; }}
  #controls button {{ padding:3px 8px; font-size:11px; }}
  #panel {{ max-width:calc(100vw - 32px); left:16px !important; right:16px !important; }}
  #search {{ width:calc(100vw - 32px); left:16px; transform:none; }}
  #search input {{ flex:1; width:auto; }}
  #tooltip {{ max-width:200px; font-size:11px; }}
}}
</style>
</head>
<body>

<canvas id="canvas"></canvas>

<div id="stats">
  <h2>{title}</h2>
  <p>{len(nodes)} topics &middot; {len(edges)} edges &middot; {max_depth + 1} layers</p>
  <p>Scroll to zoom &middot; Drag to pan &middot; Hover for details &middot; Click to open topic</p>
</div>

<div id="legend"></div>
<div id="nav">
  <a href="index.html">All Domains</a>
  <a href="radial-graph.html">Radial Graph</a>
</div>
<div id="controls">
  <button onclick="resetView()">Reset</button>
  <button onclick="zoomBtn(1.3)">+</button>
  <button onclick="zoomBtn(0.7)">&minus;</button>
</div>
<div id="tooltip"></div>
<div id="panel"></div>
<div id="search">
  <input type="text" id="searchInput" placeholder="Search topics... (Ctrl+F)">
  <span class="count" id="searchCount"></span>
</div>

<script>
const data = {graph_json};
const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");
const tooltip = document.getElementById("tooltip");
const panel = document.getElementById("panel");
let selectedNode = null;
let searchMatches = [];

let W, H, dpr;
function resize() {{
  dpr = window.devicePixelRatio || 1;
  W = window.innerWidth; H = window.innerHeight;
  canvas.width = W * dpr; canvas.height = H * dpr;
  canvas.style.width = W + "px"; canvas.style.height = H + "px";
  ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
}}
resize();
window.addEventListener("resize", () => {{ resize(); draw(); }});

// Build legend
const legendEl = document.getElementById("legend");
let lhtml = '<h3>Courses</h3>';
data.legend.forEach(l => {{
  lhtml += `<div class="legend-row"><span class="legend-dot" style="background:${{l.color}}"></span><span class="legend-label">${{l.label}}</span></div>`;
}});
legendEl.innerHTML = lhtml;

// Index nodes
const nodeMap = {{}};
data.nodes.forEach((n, i) => {{ n.idx = i; nodeMap[n.id] = n; }});

// Layout: course-based Y bands, bottom-to-top
const graphH = H * 0.88;
const graphW = W * 0.92;

const courseBands = {{}};
data.nodes.forEach(n => {{
  if (!courseBands[n.courseIdx]) courseBands[n.courseIdx] = [];
  courseBands[n.courseIdx].push(n);
}});

const courseIndices = Object.keys(courseBands).map(Number).sort((a, b) => a - b);
const numBands = courseIndices.length;
const bandSpacing = numBands > 1 ? graphH / (numBands - 1) : 0;

const maxBandSize = Math.max(...Object.values(courseBands).map(b => b.length));

const courseDepthRanges = {{}};
courseIndices.forEach(ci => {{
  const band = courseBands[ci];
  const depths = band.map(n => n.depth);
  courseDepthRanges[ci] = {{ min: Math.min(...depths), max: Math.max(...depths) }};
}});

courseIndices.forEach((ci, bandIdx) => {{
  const band = courseBands[ci];
  const bandCenterY = H * 0.06 + bandIdx * bandSpacing;
  const bandWidth = graphW * (0.10 + 0.90 * (band.length / maxBandSize));
  const dr = courseDepthRanges[ci];
  const depthRange = dr.max - dr.min;
  const subLayerH = bandSpacing * 0.7;

  band.sort((a, b) => a.depth - b.depth);

  band.forEach((n, i) => {{
    const spacing = band.length > 1 ? bandWidth / (band.length - 1) : 0;
    n.x = (W - bandWidth) / 2 + i * spacing;
    const depthFrac = depthRange > 0 ? (n.depth - dr.min) / depthRange : 0.5;
    n.y = bandCenterY - subLayerH / 2 + depthFrac * subLayerH;
    n.y += (Math.random() - 0.5) * subLayerH * 0.3;
    n.baseY = n.y;
  }});
}});

// Force simulation
const nodeRadius = Math.max(3, Math.min(5.5, 2000 / data.nodes.length));
const iterations = Math.min(150, Math.max(40, 8000 / data.nodes.length));

for (let iter = 0; iter < iterations; iter++) {{
  const alpha = 0.4 * (1 - iter / iterations);

  // Repulsion — use grid-based spatial hashing for large graphs
  const cellSize = nodeRadius * 8;
  const grid = {{}};
  data.nodes.forEach(n => {{
    const gx = Math.floor(n.x / cellSize);
    const gy = Math.floor(n.y / cellSize);
    const key = gx + "," + gy;
    if (!grid[key]) grid[key] = [];
    grid[key].push(n);
  }});

  data.nodes.forEach(a => {{
    const gx = Math.floor(a.x / cellSize);
    const gy = Math.floor(a.y / cellSize);
    for (let dx = -1; dx <= 1; dx++) {{
      for (let dy = -1; dy <= 1; dy++) {{
        const key = (gx + dx) + "," + (gy + dy);
        const cell = grid[key];
        if (!cell) continue;
        cell.forEach(b => {{
          if (a.idx >= b.idx) return;
          let ddx = b.x - a.x;
          let ddy = b.y - a.y;
          const dist = Math.hypot(ddx, ddy);
          const minDist = nodeRadius * 5;
          if (dist < minDist && dist > 0.01) {{
            const force = (minDist - dist) * 0.3 * alpha / dist;
            a.x -= ddx * force;
            a.y -= ddy * force;
            b.x += ddx * force;
            b.y += ddy * force;
          }}
        }});
      }}
    }}
  }});

  // Attraction along edges
  data.edges.forEach(e => {{
    const s = nodeMap[e.source], t = nodeMap[e.target];
    if (!s || !t) return;
    const dx = t.x - s.x;
    const dy = t.y - s.y;
    const fx = dx * 0.005 * alpha;
    const fy = dy * 0.002 * alpha;
    s.x += fx; t.x -= fx;
    s.y += fy; t.y -= fy;
  }});

  // Pull Y back toward base
  data.nodes.forEach(n => {{
    n.y += (n.baseY - n.y) * 0.08;
    n.x += (W / 2 - n.x) * 0.003 * alpha;
  }});
}}

// Camera
let camX = 0, camY = 0, camScale = 1;
function resetView() {{
  camX = 0; camY = 0; camScale = 1;
  draw();
}}
function zoomBtn(f) {{
  camScale *= f;
  draw();
}}

const edgeData = data.edges.map(e => ({{
  s: nodeMap[e.source],
  t: nodeMap[e.target],
  type: e.type,
}})).filter(e => e.s && e.t);

function draw() {{
  ctx.save();
  ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  ctx.clearRect(0, 0, W, H);
  ctx.fillStyle = "#1a1a2e";
  ctx.fillRect(0, 0, W, H);

  ctx.save();
  ctx.translate(W / 2 + camX, H / 2 + camY);
  ctx.scale(camScale, camScale);
  ctx.translate(-W / 2, -H / 2);

  edgeData.forEach(e => {{
    ctx.beginPath();
    ctx.moveTo(e.s.x, e.s.y);
    ctx.lineTo(e.t.x, e.t.y);
    if (e.type === "soft") {{
      ctx.strokeStyle = "rgba(120,120,160,0.08)";
      ctx.setLineDash([3, 3]);
    }} else {{
      ctx.strokeStyle = "rgba(120,120,160,0.14)";
      ctx.setLineDash([]);
    }}
    ctx.lineWidth = 0.5;
    ctx.stroke();
    ctx.setLineDash([]);
  }});

  data.nodes.forEach(n => {{
    ctx.beginPath();
    ctx.arc(n.x, n.y, nodeRadius, 0, Math.PI * 2);
    ctx.fillStyle = n.color;
    ctx.fill();
    ctx.strokeStyle = "rgba(255,255,255,0.08)";
    ctx.lineWidth = 0.3;
    ctx.stroke();
  }});

  // Draw highlights for selected or hovered node
  const highlightTarget = selectedNode || hoveredNode;
  if (highlightTarget) {{
    drawHighlight(highlightTarget);
  }}

  // Draw search match highlights
  if (searchMatches.length > 0) {{
    searchMatches.forEach(n => {{
      ctx.beginPath();
      ctx.arc(n.x, n.y, nodeRadius * 3, 0, Math.PI * 2);
      ctx.fillStyle = n.color;
      ctx.fill();
      ctx.strokeStyle = "rgba(255,255,100,0.8)";
      ctx.lineWidth = 1.5;
      ctx.stroke();
    }});
    if (searchMatches.length <= 5) {{
      searchMatches.forEach(n => {{
        ctx.font = "bold 9px sans-serif";
        ctx.fillStyle = "#fff";
        ctx.textAlign = "center";
        ctx.fillText(n.title, n.x, n.y - nodeRadius * 4 - 3);
      }});
    }}
  }}

  ctx.restore();
  ctx.restore();
}}

function drawHighlight(node) {{
  ctx.save();
  ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  ctx.translate(W / 2 + camX, H / 2 + camY);
  ctx.scale(camScale, camScale);
  ctx.translate(-W / 2, -H / 2);

  edgeData.forEach(ed => {{
    if (ed.s === node || ed.t === node) {{
      ctx.beginPath();
      ctx.moveTo(ed.s.x, ed.s.y);
      ctx.lineTo(ed.t.x, ed.t.y);
      ctx.strokeStyle = ed.t === node
        ? "rgba(80,180,255,0.6)"
        : "rgba(255,160,80,0.6)";
      ctx.lineWidth = 1.5;
      ctx.stroke();
    }}
  }});

  ctx.beginPath();
  ctx.arc(node.x, node.y, nodeRadius * 2, 0, Math.PI * 2);
  ctx.fillStyle = node.color;
  ctx.fill();
  ctx.strokeStyle = "#fff";
  ctx.lineWidth = 1.5;
  ctx.stroke();

  ctx.font = "bold 11px sans-serif";
  ctx.fillStyle = "#fff";
  ctx.textAlign = "center";
  ctx.fillText(node.title, node.x, node.y - nodeRadius * 2.5 - 4);

  ctx.restore();
}}

let hoveredNode = null;
draw();

// Mouse interaction
let isDragging = false, dragStartX, dragStartY;
let lastTouchTime = 0;  // Block synthetic mouse events after touch

function screenToWorld(sx, sy) {{
  return {{
    x: (sx - W / 2 - camX) / camScale + W / 2,
    y: (sy - H / 2 - camY) / camScale + H / 2,
  }};
}}

canvas.addEventListener("mousemove", (e) => {{
  if (Date.now() - lastTouchTime < 500) return;
  if (isDragging) {{
    const dx = e.clientX - dragStartX;
    const dy = e.clientY - dragStartY;
    if (Math.abs(dx) > 3 || Math.abs(dy) > 3) dragMoved = true;
    camX += dx; camY += dy;
    dragStartX = e.clientX;
    dragStartY = e.clientY;
    draw();
    tooltip.style.display = "none";
    return;
  }}

  const p = screenToWorld(e.clientX, e.clientY);
  let closest = null, closestDist = Infinity;
  data.nodes.forEach(n => {{
    const d = Math.hypot(n.x - p.x, n.y - p.y);
    if (d < closestDist) {{ closestDist = d; closest = n; }}
  }});

  const hitRadius = Math.max(nodeRadius * 1.5, 8) / camScale;
  if (closest && closestDist < hitRadius) {{
    if (hoveredNode !== closest) {{
      hoveredNode = closest;
      draw();
    }}
    const domainLabel = closest.domain ? closest.domain.replace(/-/g, " ") : "";
    const courseLabel = closest.course ? closest.course.replace(/-/g, " ") : "";
    tooltip.innerHTML = `<h4>${{closest.title}}</h4><div class="meta">${{domainLabel}} &middot; ${{courseLabel}}<br>${{closest.stage || "N/A"}} &middot; Layer ${{closest.depth}} of ${{data.maxDepth}}</div>`;
    tooltip.style.display = "block";
    tooltip.style.left = (e.clientX + 14) + "px";
    tooltip.style.top = (e.clientY - 8) + "px";
  }} else {{
    if (hoveredNode) {{ hoveredNode = null; draw(); }}
    tooltip.style.display = "none";
  }}
}});

let dragMoved = false;
canvas.addEventListener("mousedown", (e) => {{
  if (Date.now() - lastTouchTime < 500) return;
  isDragging = true;
  dragMoved = false;
  dragStartX = e.clientX;
  dragStartY = e.clientY;
  canvas.style.cursor = "grabbing";
}});
function showPanel(node, sx, sy) {{
  selectedNode = node;
  draw();
  const prereqs = edgeData.filter(e => e.t === node);
  const successors = edgeData.filter(e => e.s === node);
  const domainLabel = node.domain ? node.domain.replace(/-/g, " ") : "";
  const courseLabel = node.course ? node.course.replace(/-/g, " ") : "";
  let html = `<button class="panel-close" onclick="hidePanel()">&times;</button>`;
  html += `<h3><a href="topics/${{node.id}}.html" target="_blank">${{node.title}}</a></h3>`;
  html += `<div class="panel-meta">${{domainLabel}} &middot; ${{courseLabel}}</div>`;
  if (prereqs.length > 0) {{
    html += `<div class="panel-section"><h4>Prerequisites (${{prereqs.length}})</h4>`;
    prereqs.forEach(e => {{
      html += `<div class="panel-item" data-id="${{e.s.id}}">`;
      html += `<span class="panel-dot" style="background:${{e.s.color}}"></span>`;
      html += `<span class="panel-title">${{e.s.title}}</span>`;
      html += `<span class="panel-badge ${{e.type}}">${{e.type}}</span>`;
      html += `</div>`;
    }});
    html += `</div>`;
  }}
  if (successors.length > 0) {{
    html += `<div class="panel-section"><h4>Successors (${{successors.length}})</h4>`;
    successors.forEach(e => {{
      html += `<div class="panel-item" data-id="${{e.t.id}}">`;
      html += `<span class="panel-dot" style="background:${{e.t.color}}"></span>`;
      html += `<span class="panel-title">${{e.t.title}}</span>`;
      html += `<span class="panel-badge ${{e.type}}">${{e.type}}</span>`;
      html += `</div>`;
    }});
    html += `</div>`;
  }}
  if (prereqs.length === 0 && successors.length === 0) {{
    html += `<div class="panel-section" style="color:#666;">No connections</div>`;
  }}
  panel.innerHTML = html;
  panel.style.display = "block";
  panel.style.position = "fixed";
  let px = sx + 20, py = sy - 20;
  if (px + 390 > W) px = sx - 400;
  if (py + 300 > H) py = H - 320;
  if (py < 10) py = 10;
  if (px < 10) px = 10;
  panel.style.left = px + "px";
  panel.style.top = py + "px";
  panel.querySelectorAll(".panel-item").forEach(el => {{
    el.addEventListener("click", () => {{
      const tid = el.getAttribute("data-id");
      const target = nodeMap[tid];
      if (target) showPanel(target, parseInt(panel.style.left), parseInt(panel.style.top));
    }});
  }});
}}

function hidePanel() {{
  panel.style.display = "none";
  selectedNode = null;
  draw();
}}

canvas.addEventListener("mouseup", (e) => {{
  if (Date.now() - lastTouchTime < 500) return;
  isDragging = false;
  canvas.style.cursor = "default";
  if (!dragMoved && hoveredNode) {{
    showPanel(hoveredNode, e.clientX, e.clientY);
  }} else if (!dragMoved) {{
    hidePanel();
  }}
}});
canvas.addEventListener("wheel", (e) => {{
  e.preventDefault();
  const factor = e.deltaY > 0 ? 0.9 : 1.1;
  camScale *= factor;
  camScale = Math.max(0.1, Math.min(10, camScale));
  draw();
}}, {{ passive: false }});

// Prevent iOS WebKit from intercepting touch events for native gestures
document.addEventListener("touchmove", (e) => {{
  if (!e.target.closest("#legend, #panel")) e.preventDefault();
}}, {{ passive: false }});

// Touch support: single-finger pan, two-finger pinch-to-zoom
let lastPinchDist = 0;
let lastTouchX = 0, lastTouchY = 0;
let touchStartX = 0, touchStartY = 0;

function touchDist(t) {{
  const [a, b] = [t[0], t[1]];
  return Math.hypot(a.clientX - b.clientX, a.clientY - b.clientY);
}}
function touchCenter(t) {{
  const [a, b] = [t[0], t[1]];
  return {{ x: (a.clientX + b.clientX) / 2, y: (a.clientY + b.clientY) / 2 }};
}}

canvas.addEventListener("touchstart", (e) => {{
  e.preventDefault();
  if (e.touches.length === 1) {{
    lastTouchX = e.touches[0].clientX;
    lastTouchY = e.touches[0].clientY;
    touchStartX = lastTouchX;
    touchStartY = lastTouchY;
    isDragging = true;
    dragMoved = false;
  }} else if (e.touches.length === 2) {{
    lastPinchDist = touchDist(e.touches);
    const c = touchCenter(e.touches);
    lastTouchX = c.x; lastTouchY = c.y;
    dragMoved = true;
  }}
  tooltip.style.display = "none";
}}, {{ passive: false }});

canvas.addEventListener("touchmove", (e) => {{
  e.preventDefault();
  if (e.touches.length === 1 && isDragging) {{
    const dx = e.touches[0].clientX - lastTouchX;
    const dy = e.touches[0].clientY - lastTouchY;
    camX += dx; camY += dy;
    lastTouchX = e.touches[0].clientX;
    lastTouchY = e.touches[0].clientY;
    const totalDx = e.touches[0].clientX - touchStartX;
    const totalDy = e.touches[0].clientY - touchStartY;
    if (Math.hypot(totalDx, totalDy) > 15) dragMoved = true;
    draw();
  }} else if (e.touches.length === 2) {{
    const dist = touchDist(e.touches);
    const c = touchCenter(e.touches);
    if (lastPinchDist > 0) {{
      const factor = dist / lastPinchDist;
      const oldScale = camScale;
      camScale = Math.max(0.1, Math.min(10, camScale * factor));
      const r = camScale / oldScale;
      camX = camX * r + (c.x - W / 2) * (1 - r);
      camY = camY * r + (c.y - H / 2) * (1 - r);
    }}
    camX += c.x - lastTouchX;
    camY += c.y - lastTouchY;
    lastPinchDist = dist;
    lastTouchX = c.x; lastTouchY = c.y;
    dragMoved = true;
    draw();
  }}
}}, {{ passive: false }});

canvas.addEventListener("touchend", (e) => {{
  e.preventDefault();
  lastTouchTime = Date.now();
  if (e.touches.length === 0) {{
    isDragging = false;
    lastPinchDist = 0;
    if (!dragMoved) {{
      // Tap — do hit detection at touch point
      const p = screenToWorld(lastTouchX, lastTouchY);
      let closest = null, closestDist = Infinity;
      data.nodes.forEach(n => {{
        const d = Math.hypot(n.x - p.x, n.y - p.y);
        if (d < closestDist) {{ closestDist = d; closest = n; }}
      }});
      const hitRadius = Math.max(nodeRadius * 3, 18) / camScale;
      if (closest && closestDist < hitRadius) {{
        hoveredNode = closest;
        draw();
        showPanel(closest, lastTouchX, lastTouchY);
      }} else {{
        hoveredNode = null;
        draw();
        hidePanel();
      }}
    }}
  }} else if (e.touches.length === 1) {{
    lastTouchX = e.touches[0].clientX;
    lastTouchY = e.touches[0].clientY;
    lastPinchDist = 0;
  }}
}}, {{ passive: false }});

const searchInput = document.getElementById("searchInput");
const searchCount = document.getElementById("searchCount");

searchInput.addEventListener("input", () => {{
  const q = searchInput.value.trim().toLowerCase();
  if (q.length < 2) {{
    searchMatches = [];
    searchCount.textContent = "";
    hidePanel();
    draw();
    return;
  }}
  searchMatches = data.nodes.filter(n =>
    n.title.toLowerCase().includes(q) ||
    n.id.toLowerCase().includes(q) ||
    n.course.toLowerCase().includes(q) ||
    (n.tags && n.tags.some(t => t.includes(q)))
  );
  searchCount.textContent = searchMatches.length + " match" + (searchMatches.length !== 1 ? "es" : "");
  if (searchMatches.length === 1) {{
    selectedNode = searchMatches[0];
    hoveredNode = searchMatches[0];
    showPanel(searchMatches[0], W / 2, H / 2);
  }} else {{
    selectedNode = null;
    hidePanel();
  }}
  draw();
}});

document.addEventListener("keydown", (e) => {{
  if ((e.ctrlKey || e.metaKey) && e.key === "f") {{
    e.preventDefault();
    searchInput.focus();
    searchInput.select();
  }}
  if (e.key === "Escape") {{
    hidePanel();
    searchInput.value = "";
    searchMatches = [];
    searchCount.textContent = "";
    searchInput.blur();
    draw();
  }}
}});
</script>
</body>
</html>"""


def generate_scatter_html(all_data, configs, depths, positions, sectors,
                          domain_order, topic_stages, canvas_width, canvas_height,
                          bands):
    """Generate the interactive scatter visualization HTML."""
    max_depth = max(depths.values()) if depths else 1

    nodes = []
    edges = []
    for tid, data in all_data.items():
        if tid not in positions:
            continue
        pos = positions[tid]
        domain = data.get("domain", "")
        hue = SCATTER_HUES.get(domain, 0)
        stage = topic_stages.get(tid, DEFAULT_STAGE)
        band_min, band_max = bands.get(stage, (0.35, 0.65))
        band_frac = (pos["y"] / canvas_height - band_min) / max(band_max - band_min, 0.01)
        lightness = 32 + band_frac * 28

        nodes.append({
            "id": tid,
            "title": data.get("title", tid),
            "domain": domain,
            "course": data.get("course", ""),
            "stage": stage,
            "depth": depths.get(tid, 0),
            "x": round(pos["x"], 1),
            "y": round(pos["y"], 1),
            "hue": hue,
            "lightness": round(lightness, 1),
        })

        for p in data.get("prerequisites", []):
            if isinstance(p, dict) and "id" in p:
                pid = p["id"]
                if pid in positions:
                    edges.append({
                        "source": pid,
                        "target": tid,
                        "type": p.get("type", "hard"),
                    })

    sector_data = []
    for d in domain_order:
        if d not in sectors:
            continue
        s = sectors[d]
        hue = SCATTER_HUES.get(d, 0)
        label = configs.get(d, {}).get("title", smart_title(d))
        if isinstance(label, str) and not label[0].isupper():
            label = smart_title(d)
        sector_data.append({
            "domain": d,
            "label": label,
            "start": round(s["start"], 1),
            "end": round(s["end"], 1),
            "mid": round(s["mid"], 1),
            "hue": hue,
        })

    stage_labels = {
        "pre-formal": "Early Childhood",
        "concrete-operations": "Elementary",
        "abstract-reasoning": "Middle & High School",
        "formal-systems": "College",
        "advanced": "Graduate",
    }
    stage_band_data = []
    for i, stage in enumerate(STAGE_ORDER):
        band_min, band_max = bands.get(stage, (0.0, 1.0))
        stage_band_data.append({
            "label": stage_labels.get(stage, stage),
            "yStart": round(band_min * canvas_height, 1),
            "yEnd": round(band_max * canvas_height, 1),
            "yMid": round((band_min + band_max) / 2 * canvas_height, 1),
            "idx": i,
        })

    n_topics = len(nodes)
    n_edges = len(edges)
    n_domains = len(sector_data)
    title = "Open Knowledge Graph — All Domains"

    graph_json = json.dumps({
        "nodes": nodes,
        "edges": edges,
        "sectors": sector_data,
        "stageBands": stage_band_data,
        "canvasWidth": canvas_width,
        "canvasHeight": canvas_height,
        "maxDepth": max_depth,
    })

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
<title>{title}</title>
<style>
* {{ margin:0; padding:0; box-sizing:border-box; }}
html, body {{ overflow:hidden; touch-action:none; }}
body {{ background:#0d0d1a; font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif; color:#ccc; }}
canvas {{ display:block; position:relative; cursor:grab; touch-action:none; }}
#stats {{
  position:fixed; bottom:16px; left:16px;
  background:rgba(13,13,26,0.92); border:1px solid #222;
  border-radius:8px; padding:10px 14px; z-index:30;
}}
#stats h2 {{ font-size:14px; color:#ddd; margin-bottom:2px; }}
#stats p {{ font-size:11px; color:#555; }}
#tooltip {{
  position:fixed; display:none;
  background:rgba(15,15,30,0.95); border:1px solid #444;
  border-radius:6px; padding:8px 12px;
  z-index:40; pointer-events:none; max-width:320px;
}}
#tooltip h4 {{ font-size:13px; color:#eee; margin-bottom:3px; }}
#tooltip .meta {{ font-size:10px; color:#888; line-height:1.4; }}
#panel {{
  position:fixed; display:none;
  background:rgba(30,30,50,0.95); border:1px solid #555;
  border-radius:8px; padding:12px 16px;
  z-index:50; max-width:380px; max-height:70vh; overflow-y:auto;
}}
#panel .panel-close {{
  position:absolute; top:6px; right:10px;
  background:none; border:none; color:#888; font-size:20px;
  cursor:pointer; padding:2px 6px; line-height:1;
}}
#panel .panel-close:hover {{ color:#eee; }}
#panel h3 {{ font-size:14px; color:#eee; margin-bottom:4px; padding-right:24px; }}
#panel h3 a {{ color:#7af; text-decoration:none; }}
#panel h3 a:hover {{ text-decoration:underline; }}
#panel .panel-meta {{ font-size:10px; color:#888; margin-bottom:8px; }}
#panel .panel-section {{ margin-top:8px; }}
#panel .panel-section h4 {{ font-size:11px; color:#999; text-transform:uppercase; letter-spacing:0.5px; margin-bottom:4px; }}
#panel .panel-item {{
  display:flex; align-items:center; gap:6px;
  padding:3px 4px; border-radius:4px; cursor:pointer;
  transition:background 0.15s;
}}
#panel .panel-item:hover {{ background:rgba(255,255,255,0.08); }}
#panel .panel-dot {{ width:8px; height:8px; border-radius:50%; flex-shrink:0; }}
#panel .panel-title {{ font-size:12px; color:#ccc; flex:1; }}
#panel .panel-badge {{
  font-size:9px; padding:1px 5px; border-radius:3px;
  text-transform:uppercase; letter-spacing:0.3px; flex-shrink:0;
}}
.panel-badge.hard {{ background:rgba(255,100,100,0.2); color:#f88; }}
.panel-badge.soft {{ background:rgba(100,180,255,0.2); color:#8bf; }}
#controls {{
  position:fixed; bottom:16px; right:16px;
  background:rgba(13,13,26,0.92); border:1px solid #222;
  border-radius:8px; padding:6px 10px; z-index:30;
  display:flex; gap:4px;
}}
#controls button {{
  background:#151525; border:1px solid #333; border-radius:4px;
  padding:4px 12px; cursor:pointer; font-size:13px; color:#aaa;
}}
#controls button:hover {{ background:#252540; color:#ddd; }}
#nav {{
  position:fixed; top:8px; left:8px;
  background:rgba(13,13,26,0.92); border:1px solid #222;
  border-radius:8px; padding:6px 14px; z-index:30;
  display:flex; gap:12px;
}}
#nav a {{
  color:#888; text-decoration:none; font-size:13px;
  padding:2px 8px; border-radius:4px;
  transition:color 0.2s, background 0.2s;
}}
#nav a:hover {{ color:#eee; background:rgba(255,255,255,0.08); }}
#search {{
  position:fixed; bottom:16px; left:50%; transform:translateX(-50%);
  background:rgba(26,26,46,0.92); border:1px solid #333;
  border-radius:8px; padding:6px 14px; z-index:10;
  display:flex; gap:8px; align-items:center;
}}
#search input {{
  background:#2a2a4a; border:1px solid #444; border-radius:4px;
  padding:5px 10px; font-size:13px; color:#ccc; width:260px;
  outline:none;
}}
#search input:focus {{ border-color:#667; }}
#search .count {{ font-size:11px; color:#667; white-space:nowrap; }}
@media (max-width: 768px) {{
  #stats {{ padding:6px 10px; }}
  #stats h2 {{ font-size:12px; }}
  #stats p {{ font-size:10px; }}
  #legend {{ max-height:30vh; font-size:10px; padding:6px 10px; }}
  #legend h3 {{ font-size:10px; margin-bottom:4px; }}
  .legend-dot {{ width:8px; height:8px; }}
  .legend-label {{ font-size:10px; }}
  #nav {{ padding:4px 8px; gap:6px; }}
  #nav a {{ font-size:11px; padding:2px 4px; }}
  #controls button {{ padding:3px 8px; font-size:11px; }}
  #panel {{ max-width:calc(100vw - 32px); left:16px !important; right:16px !important; }}
  #search {{ width:calc(100vw - 32px); left:16px; transform:none; }}
  #search input {{ flex:1; width:auto; }}
  #tooltip {{ max-width:200px; font-size:11px; }}
}}
</style>
</head>
<body>
<canvas id="canvas"></canvas>
<div id="nav">
  <a href="index.html">All Domains</a>
  <a href="radial-graph.html">Radial Graph</a>
</div>
<div id="stats">
  <h2>{title}</h2>
  <p>{n_topics} topics &middot; {n_edges} edges &middot; {n_domains} domains</p>
  <p>Scroll to pan &middot; Ctrl+Scroll to zoom &middot; Drag to pan &middot; Hover for details</p>
  <p style="margin-top:4px; color:#444;">Top &rarr; basics &nbsp;&middot;&nbsp; Bottom &rarr; advanced</p>
</div>
<div id="controls">
  <button onclick="resetView()">Reset</button>
  <button onclick="zoomBtn(1.3)">+</button>
  <button onclick="zoomBtn(0.7)">&minus;</button>
</div>
<div id="tooltip"></div>
<div id="panel"></div>
<div id="search">
  <input type="text" id="searchInput" placeholder="Search topics... (Ctrl+F)">
  <span class="count" id="searchCount"></span>
</div>

<script>
const data = {graph_json};
const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");
const tooltip = document.getElementById("tooltip");
const panel = document.getElementById("panel");
let selectedNode = null;
let searchMatches = [];

let W, H, dpr;
function resize() {{
  dpr = window.devicePixelRatio || 1;
  W = window.innerWidth; H = window.innerHeight;
  canvas.width = W * dpr; canvas.height = H * dpr;
  canvas.style.width = W + "px"; canvas.style.height = H + "px";
  ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
}}
resize();
window.addEventListener("resize", () => {{ resize(); initCamera(); draw(); }});

const nodeMap = {{}};
data.nodes.forEach((n, i) => {{ n.idx = i; nodeMap[n.id] = n; }});

const SIDEBAR_W = 120;
const HEADER_H = 55;

let camScale, camOffX, camOffY;
function initCamera() {{
  camScale = (W - SIDEBAR_W - 20) / data.canvasWidth;
  camOffX = SIDEBAR_W + 10;
  camOffY = HEADER_H + 10;
}}
initCamera();

function resetView() {{ initCamera(); draw(); }}
function zoomBtn(f) {{
  const cx = W / 2, cy = H / 2;
  const wx = (cx - camOffX) / camScale;
  const wy = (cy - camOffY) / camScale;
  camScale = Math.max(0.05, Math.min(5, camScale * f));
  camOffX = cx - wx * camScale;
  camOffY = cy - wy * camScale;
  draw();
}}

function worldToScreenX(wx) {{ return wx * camScale + camOffX; }}
function worldToScreenY(wy) {{ return wy * camScale + camOffY; }}
function screenToWorldX(sx) {{ return (sx - camOffX) / camScale; }}
function screenToWorldY(sy) {{ return (sy - camOffY) / camScale; }}

const edgeData = data.edges.map(e => ({{
  s: nodeMap[e.source],
  t: nodeMap[e.target],
  type: e.type,
  crossDomain: nodeMap[e.source] && nodeMap[e.target] &&
               nodeMap[e.source].domain !== nodeMap[e.target].domain,
}})).filter(e => e.s && e.t);

const nodeRadius = Math.max(2, Math.min(4.5, 1800 / data.nodes.length));

function draw() {{
  ctx.save();
  ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  ctx.clearRect(0, 0, W, H);
  ctx.fillStyle = "#0d0d1a";
  ctx.fillRect(0, 0, W, H);

  // Stage band backgrounds (alternating)
  data.stageBands.forEach(band => {{
    const y1 = worldToScreenY(band.yStart);
    const y2 = worldToScreenY(band.yEnd);
    if (y2 < HEADER_H || y1 > H) return;
    ctx.fillStyle = band.idx % 2 === 0 ? "rgba(255,255,255,0.012)" : "rgba(0,0,0,0)";
    ctx.fillRect(SIDEBAR_W, Math.max(y1, HEADER_H), W - SIDEBAR_W, Math.min(y2, H) - Math.max(y1, HEADER_H));
  }});

  // Sector dividers
  data.sectors.forEach(s => {{
    const sx = worldToScreenX(s.start);
    if (sx < SIDEBAR_W || sx > W) return;
    ctx.beginPath();
    ctx.moveTo(sx, HEADER_H);
    ctx.lineTo(sx, H);
    ctx.strokeStyle = "rgba(255,255,255,0.035)";
    ctx.lineWidth = 0.5;
    ctx.stroke();
  }});

  // Stage band dividers
  data.stageBands.forEach(band => {{
    const sy = worldToScreenY(band.yStart);
    if (sy < HEADER_H || sy > H) return;
    ctx.beginPath();
    ctx.moveTo(SIDEBAR_W, sy);
    ctx.lineTo(W, sy);
    ctx.strokeStyle = "rgba(255,255,255,0.035)";
    ctx.lineWidth = 0.5;
    ctx.stroke();
  }});

  // Edges
  edgeData.forEach(e => {{
    const sx1 = worldToScreenX(e.s.x), sy1 = worldToScreenY(e.s.y);
    const sx2 = worldToScreenX(e.t.x), sy2 = worldToScreenY(e.t.y);
    if (Math.max(sx1, sx2) < SIDEBAR_W || Math.min(sx1, sx2) > W) return;
    if (Math.max(sy1, sy2) < HEADER_H || Math.min(sy1, sy2) > H) return;
    ctx.beginPath();
    ctx.moveTo(sx1, sy1);
    ctx.lineTo(sx2, sy2);
    if (e.crossDomain) {{
      ctx.strokeStyle = "rgba(160,120,255,0.04)";
    }} else if (e.type === "soft") {{
      ctx.strokeStyle = "rgba(100,100,140,0.05)";
    }} else {{
      ctx.strokeStyle = "rgba(100,100,140,0.09)";
    }}
    ctx.lineWidth = 0.4;
    ctx.stroke();
  }});

  // Nodes
  data.nodes.forEach(n => {{
    const sx = worldToScreenX(n.x), sy = worldToScreenY(n.y);
    if (sx < SIDEBAR_W - 5 || sx > W + 5 || sy < HEADER_H - 5 || sy > H + 5) return;
    ctx.beginPath();
    ctx.arc(sx, sy, nodeRadius, 0, Math.PI * 2);
    ctx.fillStyle = `hsl(${{n.hue}}, 55%, ${{n.lightness}}%)`;
    ctx.fill();
  }});

  // Header background
  ctx.fillStyle = "rgba(13,13,26,0.96)";
  ctx.fillRect(0, 0, W, HEADER_H);

  // Domain labels (rotated)
  data.sectors.forEach(s => {{
    const sx = worldToScreenX(s.mid);
    if (sx < SIDEBAR_W - 10 || sx > W + 10) return;
    ctx.save();
    ctx.translate(sx, HEADER_H - 6);
    ctx.rotate(-0.9);
    ctx.font = "bold 9px sans-serif";
    ctx.fillStyle = `hsla(${{s.hue}}, 50%, 60%, 0.85)`;
    ctx.textAlign = "right";
    ctx.textBaseline = "bottom";
    ctx.fillText(s.label, 0, 0);
    ctx.restore();
  }});

  // Sidebar background
  ctx.fillStyle = "rgba(13,13,26,0.96)";
  ctx.fillRect(0, 0, SIDEBAR_W, H);

  // Stage labels
  data.stageBands.forEach(band => {{
    const sy = worldToScreenY(band.yMid);
    if (sy < HEADER_H - 10 || sy > H + 10) return;
    ctx.font = "10px sans-serif";
    ctx.fillStyle = "rgba(255,255,255,0.45)";
    ctx.textAlign = "right";
    ctx.textBaseline = "middle";
    ctx.fillText(band.label, SIDEBAR_W - 8, sy);
  }});

  // Corner patch (overlap of header + sidebar)
  ctx.fillStyle = "rgba(13,13,26,0.98)";
  ctx.fillRect(0, 0, SIDEBAR_W, HEADER_H);

  // Draw highlights for selected or hovered node
  const highlightTarget = selectedNode || hoveredNode;
  if (highlightTarget) {{
    drawHighlight(highlightTarget);
  }}

  // Draw search match highlights
  if (searchMatches.length > 0) {{
    searchMatches.forEach(n => {{
      const sx = worldToScreenX(n.x), sy = worldToScreenY(n.y);
      ctx.beginPath();
      ctx.arc(sx, sy, nodeRadius * 3, 0, Math.PI * 2);
      ctx.fillStyle = `hsl(${{n.hue}}, 80%, ${{n.lightness + 15}}%)`;
      ctx.fill();
      ctx.strokeStyle = "rgba(255,255,100,0.8)";
      ctx.lineWidth = 1.5;
      ctx.stroke();
    }});
    if (searchMatches.length <= 5) {{
      searchMatches.forEach(n => {{
        const sx = worldToScreenX(n.x), sy = worldToScreenY(n.y);
        ctx.font = "bold 9px sans-serif";
        ctx.fillStyle = "#fff";
        ctx.textAlign = "center";
        ctx.fillText(n.title, sx, sy - nodeRadius * 4 - 3);
      }});
    }}
  }}

  ctx.restore();
}}

function drawHighlight(node) {{
  // Highlight connected edges (blue=prereqs, orange=dependents)
  edgeData.forEach(ed => {{
    if (ed.s === node || ed.t === node) {{
      const sx1 = worldToScreenX(ed.s.x), sy1 = worldToScreenY(ed.s.y);
      const sx2 = worldToScreenX(ed.t.x), sy2 = worldToScreenY(ed.t.y);
      ctx.save();
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      ctx.beginPath();
      ctx.moveTo(sx1, sy1);
      ctx.lineTo(sx2, sy2);
      ctx.strokeStyle = ed.t === node
        ? "rgba(80,180,255,0.6)"
        : "rgba(255,160,80,0.6)";
      ctx.lineWidth = 1.5;
      ctx.stroke();
      ctx.restore();
    }}
  }});

  // Highlight connected nodes
  ctx.save();
  ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  edgeData.forEach(ed => {{
    const other = ed.s === node ? ed.t : ed.t === node ? ed.s : null;
    if (other) {{
      const ox = worldToScreenX(other.x), oy = worldToScreenY(other.y);
      ctx.beginPath();
      ctx.arc(ox, oy, nodeRadius * 2.2, 0, Math.PI * 2);
      ctx.fillStyle = `hsl(${{other.hue}}, 70%, ${{other.lightness + 12}}%)`;
      ctx.fill();
      ctx.strokeStyle = "rgba(255,255,255,0.25)";
      ctx.lineWidth = 0.5;
      ctx.stroke();
    }}
  }});

  // Main node highlight
  const hx = worldToScreenX(node.x), hy = worldToScreenY(node.y);
  ctx.beginPath();
  ctx.arc(hx, hy, nodeRadius * 3, 0, Math.PI * 2);
  ctx.fillStyle = `hsl(${{node.hue}}, 80%, ${{node.lightness + 20}}%)`;
  ctx.fill();
  ctx.strokeStyle = "#fff";
  ctx.lineWidth = 1.5;
  ctx.stroke();

  // Label
  ctx.font = "bold 10px sans-serif";
  ctx.fillStyle = "#fff";
  ctx.textAlign = "center";
  ctx.fillText(node.title, hx, hy - nodeRadius * 4 - 4);
  ctx.restore();
}}

let hoveredNode = null;
draw();

// --- Mouse interaction ---
let isDragging = false, dragStartX, dragStartY, dragMoved = false;
let lastTouchTime = 0;

canvas.addEventListener("mousemove", (e) => {{
  if (Date.now() - lastTouchTime < 500) return;
  if (isDragging) {{
    const dx = e.clientX - dragStartX;
    const dy = e.clientY - dragStartY;
    if (Math.abs(dx) > 3 || Math.abs(dy) > 3) dragMoved = true;
    camOffX += dx; camOffY += dy;
    dragStartX = e.clientX;
    dragStartY = e.clientY;
    draw();
    tooltip.style.display = "none";
    return;
  }}

  const wx = screenToWorldX(e.clientX);
  const wy = screenToWorldY(e.clientY);
  let closest = null, closestDist = Infinity;
  data.nodes.forEach(n => {{
    const d = Math.hypot(n.x - wx, n.y - wy);
    if (d < closestDist) {{ closestDist = d; closest = n; }}
  }});

  const hitRadius = Math.max(nodeRadius * 2.5, 12) / camScale;
  if (closest && closestDist < hitRadius) {{
    if (hoveredNode !== closest) {{
      hoveredNode = closest;
      draw();
    }}

    const stageLabels = {{
      "pre-formal": "Early Childhood",
      "concrete-operations": "Elementary",
      "abstract-reasoning": "Middle/High School",
      "formal-systems": "College",
      "advanced": "Graduate",
    }};
    const domainLabel = closest.domain ? closest.domain.replace(/-/g, " ") : "";
    const courseLabel = closest.course ? closest.course.replace(/-/g, " ") : "";
    const stageLabel = stageLabels[closest.stage] || closest.stage || "";
    tooltip.innerHTML = `<h4>${{closest.title}}</h4><div class="meta">${{domainLabel}} &middot; ${{courseLabel}}<br>${{stageLabel}} &middot; Depth ${{closest.depth}}</div>`;
    tooltip.style.display = "block";
    tooltip.style.left = (e.clientX + 14) + "px";
    tooltip.style.top = (e.clientY - 8) + "px";
  }} else {{
    if (hoveredNode) {{ hoveredNode = null; draw(); }}
    tooltip.style.display = "none";
    canvas.style.cursor = "grab";
  }}
}});

canvas.addEventListener("mousedown", (e) => {{
  if (Date.now() - lastTouchTime < 500) return;
  isDragging = true;
  dragMoved = false;
  dragStartX = e.clientX; dragStartY = e.clientY;
  canvas.style.cursor = "grabbing";
}});
function showPanel(node, sx, sy) {{
  selectedNode = node;
  draw();
  const prereqs = edgeData.filter(e => e.t === node);
  const successors = edgeData.filter(e => e.s === node);
  const domainLabel = node.domain ? node.domain.replace(/-/g, " ") : "";
  const courseLabel = node.course ? node.course.replace(/-/g, " ") : "";
  let html = `<button class="panel-close" onclick="hidePanel()">&times;</button>`;
  html += `<h3><a href="topics/${{node.id}}.html" target="_blank">${{node.title}}</a></h3>`;
  html += `<div class="panel-meta">${{domainLabel}} &middot; ${{courseLabel}}</div>`;
  if (prereqs.length > 0) {{
    html += `<div class="panel-section"><h4>Prerequisites (${{prereqs.length}})</h4>`;
    prereqs.forEach(e => {{
      html += `<div class="panel-item" data-id="${{e.s.id}}">`;
      html += `<span class="panel-dot" style="background:hsl(${{e.s.hue}}, 55%, ${{e.s.lightness}}%)"></span>`;
      html += `<span class="panel-title">${{e.s.title}}</span>`;
      html += `<span class="panel-badge ${{e.type}}">${{e.type}}</span>`;
      html += `</div>`;
    }});
    html += `</div>`;
  }}
  if (successors.length > 0) {{
    html += `<div class="panel-section"><h4>Successors (${{successors.length}})</h4>`;
    successors.forEach(e => {{
      html += `<div class="panel-item" data-id="${{e.t.id}}">`;
      html += `<span class="panel-dot" style="background:hsl(${{e.t.hue}}, 55%, ${{e.t.lightness}}%)"></span>`;
      html += `<span class="panel-title">${{e.t.title}}</span>`;
      html += `<span class="panel-badge ${{e.type}}">${{e.type}}</span>`;
      html += `</div>`;
    }});
    html += `</div>`;
  }}
  if (prereqs.length === 0 && successors.length === 0) {{
    html += `<div class="panel-section" style="color:#666;">No connections</div>`;
  }}
  panel.innerHTML = html;
  panel.style.display = "block";
  let px = sx + 20, py = sy - 20;
  if (px + 390 > W) px = sx - 400;
  if (py + 300 > H) py = H - 320;
  if (py < 10) py = 10;
  if (px < 10) px = 10;
  panel.style.left = px + "px";
  panel.style.top = py + "px";
  panel.querySelectorAll(".panel-item").forEach(el => {{
    el.addEventListener("click", () => {{
      const tid = el.getAttribute("data-id");
      const target = nodeMap[tid];
      if (target) showPanel(target, parseInt(panel.style.left), parseInt(panel.style.top));
    }});
  }});
}}

function hidePanel() {{
  panel.style.display = "none";
  selectedNode = null;
  draw();
}}

canvas.addEventListener("mouseup", (e) => {{
  if (Date.now() - lastTouchTime < 500) return;
  isDragging = false;
  canvas.style.cursor = "grab";
  if (!dragMoved && hoveredNode) {{
    showPanel(hoveredNode, e.clientX, e.clientY);
  }} else if (!dragMoved) {{
    hidePanel();
  }}
}});
canvas.addEventListener("wheel", (e) => {{
  e.preventDefault();
  if (e.ctrlKey || e.metaKey) {{
    // Zoom toward cursor
    const factor = e.deltaY > 0 ? 0.9 : 1.1;
    const wx = screenToWorldX(e.clientX);
    const wy = screenToWorldY(e.clientY);
    camScale = Math.max(0.05, Math.min(5, camScale * factor));
    camOffX = e.clientX - wx * camScale;
    camOffY = e.clientY - wy * camScale;
  }} else {{
    // Scroll: vertical pan (shift = horizontal)
    if (e.shiftKey) {{
      camOffX -= e.deltaY;
    }} else {{
      camOffY -= e.deltaY;
    }}
  }}
  draw();
}}, {{ passive: false }});

// Prevent iOS WebKit from intercepting touch events for native gestures
document.addEventListener("touchmove", (e) => {{
  if (!e.target.closest("#legend, #panel")) e.preventDefault();
}}, {{ passive: false }});

// Touch support: single-finger pan, two-finger pinch-to-zoom
let lastPinchDist = 0;
let lastTouchX = 0, lastTouchY = 0;
let touchStartX = 0, touchStartY = 0;

function touchDist(t) {{
  const [a, b] = [t[0], t[1]];
  return Math.hypot(a.clientX - b.clientX, a.clientY - b.clientY);
}}
function touchCenter(t) {{
  const [a, b] = [t[0], t[1]];
  return {{ x: (a.clientX + b.clientX) / 2, y: (a.clientY + b.clientY) / 2 }};
}}

canvas.addEventListener("touchstart", (e) => {{
  e.preventDefault();
  if (e.touches.length === 1) {{
    lastTouchX = e.touches[0].clientX;
    lastTouchY = e.touches[0].clientY;
    touchStartX = lastTouchX;
    touchStartY = lastTouchY;
    isDragging = true;
    dragMoved = false;
  }} else if (e.touches.length === 2) {{
    lastPinchDist = touchDist(e.touches);
    const c = touchCenter(e.touches);
    lastTouchX = c.x; lastTouchY = c.y;
    dragMoved = true;
  }}
  tooltip.style.display = "none";
}}, {{ passive: false }});

canvas.addEventListener("touchmove", (e) => {{
  e.preventDefault();
  if (e.touches.length === 1 && isDragging) {{
    const dx = e.touches[0].clientX - lastTouchX;
    const dy = e.touches[0].clientY - lastTouchY;
    camOffX += dx; camOffY += dy;
    lastTouchX = e.touches[0].clientX;
    lastTouchY = e.touches[0].clientY;
    const totalDx = e.touches[0].clientX - touchStartX;
    const totalDy = e.touches[0].clientY - touchStartY;
    if (Math.hypot(totalDx, totalDy) > 15) dragMoved = true;
    draw();
  }} else if (e.touches.length === 2) {{
    const dist = touchDist(e.touches);
    const c = touchCenter(e.touches);
    if (lastPinchDist > 0) {{
      const factor = dist / lastPinchDist;
      const wx = (c.x - camOffX) / camScale;
      const wy = (c.y - camOffY) / camScale;
      camScale = Math.max(0.05, Math.min(5, camScale * factor));
      camOffX = c.x - wx * camScale;
      camOffY = c.y - wy * camScale;
    }}
    camOffX += c.x - lastTouchX;
    camOffY += c.y - lastTouchY;
    lastPinchDist = dist;
    lastTouchX = c.x; lastTouchY = c.y;
    dragMoved = true;
    draw();
  }}
}}, {{ passive: false }});

canvas.addEventListener("touchend", (e) => {{
  e.preventDefault();
  lastTouchTime = Date.now();
  if (e.touches.length === 0) {{
    isDragging = false;
    lastPinchDist = 0;
    if (!dragMoved) {{
      // Tap — do hit detection at touch point
      const wx = screenToWorldX(lastTouchX);
      const wy = screenToWorldY(lastTouchY);
      let closest = null, closestDist = Infinity;
      data.nodes.forEach(n => {{
        const d = Math.hypot(n.x - wx, n.y - wy);
        if (d < closestDist) {{ closestDist = d; closest = n; }}
      }});
      const hitRadius = Math.max(nodeRadius * 3, 18) / camScale;
      if (closest && closestDist < hitRadius) {{
        hoveredNode = closest;
        draw();
        showPanel(closest, lastTouchX, lastTouchY);
      }} else {{
        hoveredNode = null;
        draw();
        hidePanel();
      }}
    }}
  }} else if (e.touches.length === 1) {{
    lastTouchX = e.touches[0].clientX;
    lastTouchY = e.touches[0].clientY;
    lastPinchDist = 0;
  }}
}}, {{ passive: false }});

const searchInput = document.getElementById("searchInput");
const searchCount = document.getElementById("searchCount");

searchInput.addEventListener("input", () => {{
  const q = searchInput.value.trim().toLowerCase();
  if (q.length < 2) {{
    searchMatches = [];
    searchCount.textContent = "";
    hidePanel();
    draw();
    return;
  }}
  searchMatches = data.nodes.filter(n =>
    n.title.toLowerCase().includes(q) ||
    n.id.toLowerCase().includes(q) ||
    n.course.toLowerCase().includes(q) ||
    (n.tags && n.tags.some(t => t.includes(q)))
  );
  searchCount.textContent = searchMatches.length + " match" + (searchMatches.length !== 1 ? "es" : "");
  if (searchMatches.length === 1) {{
    selectedNode = searchMatches[0];
    hoveredNode = searchMatches[0];
    showPanel(searchMatches[0], W / 2, H / 2);
  }} else {{
    selectedNode = null;
    hidePanel();
  }}
  draw();
}});

document.addEventListener("keydown", (e) => {{
  if ((e.ctrlKey || e.metaKey) && e.key === "f") {{
    e.preventDefault();
    searchInput.focus();
    searchInput.select();
  }}
  if (e.key === "Escape") {{
    hidePanel();
    searchInput.value = "";
    searchMatches = [];
    searchCount.textContent = "";
    searchInput.blur();
    draw();
  }}
}});
</script>
</body>
</html>"""


def generate_index_html(domains_info):
    """Generate an index page linking to all domain visualizations."""
    rows = ""
    total_topics = 0
    total_edges = 0
    for domain, info in sorted(domains_info.items()):
        label = smart_title(domain)
        rows += f'<a href="{domain}-hierarchy.html" class="domain-card">'
        rows += f'<h3>{label}</h3>'
        rows += f'<p>{info["topics"]} topics &middot; {info["edges"]} edges &middot; {info["courses"]} courses</p>'
        rows += '</a>\n'
        total_topics += info["topics"]
        total_edges += info["edges"]

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Open Knowledge Graph</title>
<style>
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{
  background:#1a1a2e; color:#ccc;
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;
  padding:40px;
}}
h1 {{ color:#eee; margin-bottom:8px; font-size:28px; }}
.subtitle {{ color:#777; margin-bottom:30px; font-size:14px; }}
.grid {{
  display:grid; grid-template-columns:repeat(auto-fill, minmax(280px, 1fr));
  gap:16px; max-width:1200px;
}}
.domain-card {{
  display:block; text-decoration:none;
  background:rgba(40,40,70,0.6); border:1px solid #333;
  border-radius:8px; padding:16px 20px;
  transition:border-color 0.2s, background 0.2s;
}}
.domain-card:hover {{
  border-color:#666; background:rgba(50,50,80,0.8);
}}
.domain-card h3 {{ color:#ddd; font-size:16px; margin-bottom:4px; }}
.domain-card p {{ color:#888; font-size:12px; }}
.full-link {{
  display:inline-block; margin-top:24px; padding:10px 20px;
  background:#2a2a5a; border:1px solid #555; border-radius:6px;
  color:#ccc; text-decoration:none; font-size:14px;
}}
.full-link:hover {{ background:#3a3a6a; border-color:#777; }}
</style>
</head>
<body>
<h1>Open Knowledge Graph</h1>
<p class="subtitle">{total_topics} topics across {len(domains_info)} domains &middot; {total_edges} prerequisite edges</p>
<div class="grid">
{rows}
</div>
<div style="margin-top:24px; display:flex; gap:12px; flex-wrap:wrap;">
<a href="radial-graph.html" class="full-link" style="background:#3a2a6a;">View Radial Graph (All Domains)</a>
<a href="full-graph-hierarchy.html" class="full-link">View Hierarchy Graph (All Domains)</a>
</div>
</body>
</html>"""


def main():
    parser = argparse.ArgumentParser(description="Hierarchical knowledge graph visualization")
    parser.add_argument("--domain", help="Filter by domain")
    parser.add_argument("--course", help="Filter by course")
    parser.add_argument("--output", help="Output file path")
    parser.add_argument("--all", action="store_true", help="Generate all domain HTMLs + index")
    args = parser.parse_args()

    configs = load_all_domain_configs()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    if args.all:
        # Generate per-domain visualizations
        domains_info = {}
        for domain, cfg in sorted(configs.items()):
            print(f"Generating {domain}...")
            course_ids = cfg["course_ids"]
            colors = generate_course_colors(domain, course_ids)
            nodes, edges = load_graph(domain_filter=domain)
            if not nodes:
                continue

            title = f"Open Knowledge Graph — {smart_title(domain)}"
            html = generate_html(nodes, edges, title=title,
                                course_colors=colors, course_order=course_ids)
            out = OUTPUT_DIR / f"{domain}-hierarchy.html"
            out.write_text(html, encoding="utf-8")

            domains_info[domain] = {
                "topics": len(nodes),
                "edges": len(edges),
                "courses": len(course_ids),
            }
            print(f"  {len(nodes)} topics, {len(edges)} edges -> {out.name}")

        # Generate full cross-domain scatter graph
        print("Generating full cross-domain scatter graph...")
        all_data = load_all_topics()

        # Load configs with stage info (radial-compatible format)
        scatter_configs = {}
        for domain_dir in sorted(DOMAINS_DIR.iterdir()):
            if domain_dir.is_dir() and (domain_dir / "_domain.yml").exists():
                ddata = yaml.safe_load(
                    (domain_dir / "_domain.yml").read_text(encoding="utf-8")
                )
                courses = ddata.get("courses", [])
                course_list = []
                for c in courses:
                    if isinstance(c, dict) and "id" in c:
                        course_list.append({
                            "id": c["id"],
                            "title": c.get("title", c["id"]),
                            "stage": c.get("stage", DEFAULT_STAGE),
                        })
                scatter_configs[domain_dir.name] = {
                    "title": ddata.get("title", domain_dir.name),
                    "courses": course_list,
                }

        depths = compute_depths_from_data(all_data)
        positions, sectors, domain_order, topic_stages, cw, ch, bands = \
            build_scatter_layout(all_data, scatter_configs, depths)

        html = generate_scatter_html(
            all_data, scatter_configs, depths, positions, sectors,
            domain_order, topic_stages, cw, ch, bands)
        out = OUTPUT_DIR / "full-graph-hierarchy.html"
        out.write_text(html, encoding="utf-8")
        print(f"  {len(all_data)} topics -> {out.name}")

        # Generate index
        index_html = generate_index_html(domains_info)
        index_out = OUTPUT_DIR / "index.html"
        index_out.write_text(index_html, encoding="utf-8")
        print(f"\nIndex page -> {index_out}")
        print(f"Done! {len(domains_info)} domain pages + full graph + index")

    else:
        # Single domain/course/full generation
        domain = args.domain
        course = args.course

        if domain and domain in configs:
            course_ids = configs[domain]["course_ids"]
            colors = generate_course_colors(domain, course_ids)
        elif course:
            # Find which domain this course belongs to
            for d, cfg in configs.items():
                if course in cfg["course_ids"]:
                    domain = d
                    course_ids = cfg["course_ids"]
                    colors = generate_course_colors(d, course_ids)
                    break
            else:
                colors = {}
                course_ids = []
        else:
            # Full graph
            course_ids = []
            colors = {}
            for d, cfg in sorted(configs.items()):
                cids = cfg["course_ids"]
                course_ids.extend(cids)
                colors.update(generate_course_colors(d, cids))

        nodes, edges = load_graph(domain_filter=domain, course_filter=course)
        print(f"Loaded {len(nodes)} topics, {len(edges)} edges")

        if not nodes:
            print("No topics found.")
            return

        name = course or domain or "full-graph"
        title = f"Open Knowledge Graph — {smart_title(name)}"
        out = Path(args.output) if args.output else OUTPUT_DIR / f"{name}-hierarchy.html"

        html = generate_html(nodes, edges, title=title,
                            course_colors=colors, course_order=course_ids)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(html, encoding="utf-8")
        print(f"Saved: {out}")


if __name__ == "__main__":
    main()
