#!/usr/bin/env python3
"""Generate a radial knowledge graph visualization.

Top-down torus layout:
- Inner ring = early childhood / foundational topics
- Outer ring = graduate / advanced topics
- Radial position = developmental stage (age-based), not topological depth
- Domains form organic clouds via polar force simulation
- Adjacent domains share the most cross-domain edges
- Interactive: zoom, pan, hover for details

Usage:
    python tools/visualize_radial.py                    # Generate radial full graph
    python tools/visualize_radial.py --output my.html   # Custom output path
"""

import sys
import re
import json
import math
import random
import argparse
from pathlib import Path
from collections import defaultdict, deque

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML required. Install with: pip install pyyaml")
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent
DOMAINS_DIR = ROOT / "domains"
OUTPUT_DIR = ROOT / "output"

# --- Developmental stage → radial band mapping ---
# Maps the stage field to approximate age ranges and radial bands.
# Inner = youngest, outer = most advanced.
STAGE_BANDS = {
    "pre-formal":          (0.08, 0.25),   # ages ~4-7, K-1st
    "concrete-operations": (0.18, 0.47),   # ages ~7-12, 2nd-6th
    "abstract-reasoning":  (0.38, 0.70),   # ages ~12-16, 7th-10th
    "formal-systems":      (0.60, 0.90),   # ages ~16-22, 11th-college
    "advanced":            (0.82, 1.00),   # ages ~22+, graduate
}
DEFAULT_STAGE = "abstract-reasoning"

# --- Curated domain ordering ---
# Designed so related domains are adjacent and cross-domain edges stay short.
# STEM core → natural sciences → life sciences → social sciences → humanities → arts → back to STEM
DOMAIN_ORDER = [
    "mathematics",
    "formal-sciences-and-logic",
    "philosophy",
    "computer-science",
    "engineering",
    "physics",
    "earth-and-space-sciences",
    "chemistry",
    "biology",
    "health-and-human-development",
    "psychology",
    "social-sciences",
    "economics",
    "practical-life-skills",
    "history",
    "language-and-communication",
    "literature",
    "arts-and-aesthetics",
    "music",
]

# Domain hue assignments (HSL degrees) — hand-tuned for visual distinction
DOMAIN_HUES = {
    "mathematics":                42,
    "formal-sciences-and-logic": 185,
    "philosophy":                260,
    "computer-science":          200,
    "engineering":                28,
    "physics":                   215,
    "chemistry":                   0,
    "earth-and-space-sciences":  170,
    "biology":                   120,
    "health-and-human-development": 148,
    "psychology":                280,
    "social-sciences":            60,
    "economics":                  48,
    "practical-life-skills":      80,
    "history":                    18,
    "language-and-communication": 155,
    "literature":                310,
    "arts-and-aesthetics":       335,
    "music":                     290,
}


def parse_frontmatter(filepath):
    text = filepath.read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not match:
        return None
    try:
        return yaml.safe_load(match.group(1))
    except yaml.YAMLError:
        return None


def load_all_topics():
    all_data = {}
    for filepath in sorted(DOMAINS_DIR.rglob("*.md")):
        data = parse_frontmatter(filepath)
        if data and "id" in data:
            all_data[data["id"]] = data
    return all_data


def load_domain_configs():
    configs = {}
    for domain_dir in sorted(DOMAINS_DIR.iterdir()):
        if domain_dir.is_dir() and (domain_dir / "_domain.yml").exists():
            data = yaml.safe_load(
                (domain_dir / "_domain.yml").read_text(encoding="utf-8")
            )
            courses = data.get("courses", [])
            course_list = []
            for c in courses:
                if isinstance(c, dict) and "id" in c:
                    course_list.append({
                        "id": c["id"],
                        "title": c.get("title", c["id"]),
                        "stage": c.get("stage", DEFAULT_STAGE),
                    })
            configs[domain_dir.name] = {
                "title": data.get("title", domain_dir.name),
                "courses": course_list,
            }
    return configs


def get_topic_stage(data, configs):
    """Determine a topic's developmental stage from its own field or its course config."""
    # Topic-level stage takes priority
    stage = data.get("stage", "")
    if stage and stage in STAGE_BANDS:
        return stage

    # Fall back to course-level stage from _domain.yml
    domain = data.get("domain", "")
    course = data.get("course", "")
    if domain in configs:
        for c in configs[domain]["courses"]:
            if c["id"] == course:
                return c.get("stage", DEFAULT_STAGE)

    return DEFAULT_STAGE


def compute_depths(all_data):
    """Compute topological depth for each topic (longest path from any root)."""
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


def build_radial_layout(all_data, configs, depths):
    """Compute positions using developmental-stage radial bands and polar force simulation."""

    random.seed(42)  # Reproducible layout

    # --- Phase 1: Assign initial positions ---
    domain_order = [d for d in DOMAIN_ORDER if d in configs]
    n_domains = len(domain_order)

    # Angular sectors — proportional to topic count, with gaps
    gap_angle = math.radians(1.2)
    total_gap = gap_angle * n_domains
    usable_angle = 2 * math.pi - total_gap

    domain_counts = defaultdict(int)
    for data in all_data.values():
        domain_counts[data.get("domain", "")] += 1
    total_topics = sum(domain_counts[d] for d in domain_order)

    sectors = {}
    current_angle = 0
    for d in domain_order:
        frac = domain_counts.get(d, 1) / total_topics
        sector_angle = usable_angle * frac
        sectors[d] = {
            "start": current_angle,
            "end": current_angle + sector_angle,
            "mid": current_angle + sector_angle / 2,
        }
        current_angle += sector_angle + gap_angle

    # Radial layout parameters
    max_radius = 500

    # Compute stage-local depth range for fine positioning within each band
    stage_depths = defaultdict(list)  # stage -> list of (depth, tid)
    topic_stages = {}
    for tid, data in all_data.items():
        stage = get_topic_stage(data, configs)
        topic_stages[tid] = stage
        stage_depths[stage].append(depths.get(tid, 0))

    stage_depth_ranges = {}
    for stage, depth_list in stage_depths.items():
        stage_depth_ranges[stage] = (min(depth_list), max(depth_list))

    # Assign initial (r, theta) for each topic
    positions = {}
    for tid, data in all_data.items():
        domain = data.get("domain", "")
        course = data.get("course", "")
        stage = topic_stages[tid]

        if domain not in sectors:
            continue

        # Radial: developmental stage band
        band_min, band_max = STAGE_BANDS.get(stage, (0.4, 0.6))
        d_min, d_max = stage_depth_ranges.get(stage, (0, 1))
        d = depths.get(tid, 0)

        # Position within band based on depth within that stage
        if d_max > d_min:
            depth_frac = (d - d_min) / (d_max - d_min)
        else:
            depth_frac = 0.5
        r = (band_min + depth_frac * (band_max - band_min)) * max_radius

        # Angular: course sub-sector within domain sector
        sector = sectors[domain]
        course_ids = [c["id"] for c in configs.get(domain, {}).get("courses", [])]
        n_courses = len(course_ids)

        if course in course_ids:
            course_idx = course_ids.index(course)
        else:
            course_idx = 0

        sector_width = sector["end"] - sector["start"]
        if n_courses > 0:
            course_frac = (course_idx + 0.5) / n_courses
        else:
            course_frac = 0.5

        base_angle = sector["start"] + sector_width * course_frac

        # Jitter for organic feel (radial jitter kept small to preserve depth ordering)
        angle_jitter = (random.random() - 0.5) * sector_width / max(n_courses, 1) * 0.5
        radial_jitter = (random.random() - 0.5) * (band_max - band_min) * max_radius * 0.05

        theta = base_angle + angle_jitter
        r = max(20, r + radial_jitter)

        x = r * math.cos(theta)
        y = r * math.sin(theta)

        positions[tid] = {
            "x": x, "y": y,
            "r": r, "theta": theta,
            "target_r": r,  # For radial spring-back
            "target_theta": base_angle,  # For angular spring-back (sector center for this course)
            "stage": stage,
        }

    # --- Phase 2: Polar force simulation ---
    # Allow angular drift toward cross-domain connections.
    # Constrain radial position to developmental band (strong spring).
    print("  Running polar force simulation...")

    # Build edge list
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

    iterations = 80
    node_ids = list(positions.keys())
    n = len(node_ids)

    # Spatial grid for repulsion
    for it in range(iterations):
        alpha = 0.5 * (1 - it / iterations)

        # Grid-based repulsion
        cell_size = 25
        grid = defaultdict(list)
        for tid in node_ids:
            p = positions[tid]
            gx = int(p["x"] / cell_size)
            gy = int(p["y"] / cell_size)
            grid[(gx, gy)].append(tid)

        for (gx, gy), cell in grid.items():
            # Check this cell and neighbors
            neighbors = []
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    neighbors.extend(grid.get((gx + dx, gy + dy), []))

            for i, a_id in enumerate(cell):
                pa = positions[a_id]
                for b_id in neighbors:
                    if a_id >= b_id:
                        continue
                    pb = positions[b_id]
                    ddx = pb["x"] - pa["x"]
                    ddy = pb["y"] - pa["y"]
                    dist = math.hypot(ddx, ddy)
                    min_dist = 12
                    if dist < min_dist and dist > 0.01:
                        force = (min_dist - dist) * 0.25 * alpha / dist
                        pa["x"] -= ddx * force
                        pa["y"] -= ddy * force
                        pb["x"] += ddx * force
                        pb["y"] += ddy * force

        # Edge attraction (stronger for cross-domain)
        for src, tgt, cross in edge_list:
            ps = positions[src]
            pt = positions[tgt]
            dx = pt["x"] - ps["x"]
            dy = pt["y"] - ps["y"]
            strength = 0.008 if cross else 0.003
            fx = dx * strength * alpha
            fy = dy * strength * alpha
            ps["x"] += fx
            ps["y"] += fy
            pt["x"] -= fx
            pt["y"] -= fy

        # Soft prerequisite radial ordering: push prereqs inward, successors outward
        for src, tgt, cross in edge_list:
            ps = positions[src]
            pt = positions[tgt]
            rs = math.hypot(ps["x"], ps["y"])
            rt = math.hypot(pt["x"], pt["y"])
            if rs < 1 or rt < 1:
                continue
            # Only apply when prereq is at same or greater radius than successor
            if rs >= rt:
                overlap = (rs - rt) + 5  # 5px minimum separation target
                nudge = overlap * 0.006 * alpha
                # Push prereq inward (scale toward origin)
                ps["x"] *= max(0.95, 1 - nudge / rs)
                ps["y"] *= max(0.95, 1 - nudge / rs)
                # Push successor outward
                pt["x"] *= min(1.05, 1 + nudge / rt)
                pt["y"] *= min(1.05, 1 + nudge / rt)

        # Radial spring-back to developmental band
        for tid in node_ids:
            p = positions[tid]
            current_r = math.hypot(p["x"], p["y"])
            if current_r < 1:
                current_r = 1
            target_r = p["target_r"]
            # Pull toward target radius
            ratio = 1 + (target_r - current_r) / current_r * 0.15
            p["x"] *= ratio
            p["y"] *= ratio

        # Angular spring-back to domain sector
        for tid in node_ids:
            p = positions[tid]
            current_r = math.hypot(p["x"], p["y"])
            if current_r < 1:
                continue
            current_theta = math.atan2(p["y"], p["x"])
            target_theta = p["target_theta"]
            # Shortest angular distance
            delta = (target_theta - current_theta + math.pi) % (2 * math.pi) - math.pi
            # Apply angular correction (rotate toward target)
            correction = delta * 0.02
            new_theta = current_theta + correction
            p["x"] = current_r * math.cos(new_theta)
            p["y"] = current_r * math.sin(new_theta)

    # Update r and theta after simulation
    for tid in node_ids:
        p = positions[tid]
        p["r"] = math.hypot(p["x"], p["y"])
        p["theta"] = math.atan2(p["y"], p["x"])

    return positions, sectors, domain_order


def generate_radial_html(all_data, configs, depths, positions, sectors, domain_order):
    """Generate the interactive radial visualization HTML."""

    max_depth = max(depths.values()) if depths else 1

    nodes = []
    edges = []

    for tid, data in all_data.items():
        if tid not in positions:
            continue
        pos = positions[tid]
        domain = data.get("domain", "")
        course = data.get("course", "")
        hue = DOMAIN_HUES.get(domain, 0)

        # Lightness varies by radial position (inner=dimmer, outer=brighter)
        r_frac = pos["r"] / 500
        lightness = 35 + r_frac * 30

        tags = data.get("tags", [])
        nodes.append({
            "id": tid,
            "title": data.get("title", tid),
            "domain": domain,
            "course": course,
            "stage": data.get("stage", ""),
            "depth": depths.get(tid, 0),
            "x": round(pos["x"], 2),
            "y": round(pos["y"], 2),
            "hue": hue,
            "lightness": round(lightness, 1),
            "tags": [str(t).lower() for t in tags] if tags else [],
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

    # Sector arcs for domain labels
    sector_data = []
    for d in domain_order:
        if d not in sectors:
            continue
        s = sectors[d]
        hue = DOMAIN_HUES.get(d, 0)
        label = configs.get(d, {}).get("title", d.replace("-", " ").title())
        sector_data.append({
            "domain": d,
            "label": label,
            "start": round(s["start"], 4),
            "end": round(s["end"], 4),
            "mid": round(s["mid"], 4),
            "hue": hue,
        })

    # Stage ring labels
    stage_rings = []
    for stage, (band_min, band_max) in STAGE_BANDS.items():
        label_map = {
            "pre-formal": "Early Childhood",
            "concrete-operations": "Elementary",
            "abstract-reasoning": "Middle & High School",
            "formal-systems": "College",
            "advanced": "Graduate",
        }
        stage_rings.append({
            "label": label_map.get(stage, stage),
            "inner": round(band_min * 500, 1),
            "outer": round(band_max * 500, 1),
            "mid": round((band_min + band_max) / 2 * 500, 1),
        })

    graph_json = json.dumps({
        "nodes": nodes,
        "edges": edges,
        "sectors": sector_data,
        "stageRings": stage_rings,
        "maxDepth": max_depth,
    })

    title = "Open Knowledge Graph"
    n_topics = len(nodes)
    n_edges = len(edges)
    n_domains = len(sector_data)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
<title>{title}</title>
<style>
* {{ margin:0; padding:0; box-sizing:border-box; }}
html, body {{ overflow:hidden; touch-action:none; }}
body {{ background:#08080f; font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif; color:#ccc; }}
canvas {{ display:block; position:relative; cursor:grab; touch-action:none; }}
#stats {{
  position:fixed; top:16px; left:16px;
  background:rgba(8,8,15,0.9); border:1px solid #222;
  border-radius:8px; padding:12px 16px; z-index:10;
}}
#stats h2 {{ font-size:15px; color:#ddd; margin-bottom:4px; }}
#stats p {{ font-size:11px; color:#555; line-height:1.5; }}
#tooltip {{
  position:fixed; display:none;
  background:rgba(15,15,30,0.95); border:1px solid #444;
  border-radius:6px; padding:8px 12px;
  z-index:20; pointer-events:none; max-width:320px;
}}
#tooltip h4 {{ font-size:13px; color:#eee; margin-bottom:3px; }}
#tooltip .meta {{ font-size:10px; color:#888; line-height:1.4; }}
#panel {{
  position:fixed; display:none;
  background:rgba(10,10,20,0.95); border:1px solid #444;
  border-radius:8px; padding:16px 20px;
  z-index:30; max-width:380px; max-height:70vh; overflow-y:auto;
}}
#panel .panel-close {{
  position:absolute; top:6px; right:10px;
  background:none; border:none; color:#888; font-size:20px;
  cursor:pointer; padding:2px 6px; line-height:1;
}}
#panel .panel-close:hover {{ color:#eee; }}
#panel h3 {{
  font-size:15px; margin-bottom:8px; padding-right:24px;
}}
#panel h3 a {{ color:#eee; text-decoration:none; border-bottom:1px solid #555; }}
#panel h3 a:hover {{ color:#9cd; border-bottom-color:#9cd; }}
#panel .panel-meta {{ font-size:11px; color:#777; margin-bottom:12px; }}
#panel .panel-section {{ margin-bottom:10px; }}
#panel .panel-section h4 {{ font-size:11px; color:#667; text-transform:uppercase; letter-spacing:0.5px; margin-bottom:4px; }}
#panel .panel-item {{
  display:flex; align-items:center; gap:6px;
  padding:3px 0; font-size:12px; color:#aab; cursor:pointer;
}}
#panel .panel-item:hover {{ color:#dde; }}
#panel .panel-dot {{ width:6px; height:6px; border-radius:50%; flex-shrink:0; }}
#panel .panel-badge {{
  font-size:9px; padding:1px 4px; border-radius:3px;
  font-weight:600; text-transform:uppercase; margin-left:auto;
}}
#panel .panel-badge.hard {{ background:rgba(220,80,80,0.15); color:#c66; }}
#panel .panel-badge.soft {{ background:rgba(80,160,220,0.15); color:#6ab; }}
#controls {{
  position:fixed; top:16px; right:16px;
  background:rgba(8,8,15,0.9); border:1px solid #222;
  border-radius:8px; padding:6px 10px; z-index:10;
  display:flex; gap:4px;
}}
#controls button {{
  background:#151525; border:1px solid #333; border-radius:4px;
  padding:4px 12px; cursor:pointer; font-size:13px; color:#aaa;
}}
#controls button:hover {{ background:#252540; color:#ddd; }}
#nav {{
  position:fixed; top:16px; left:50%; transform:translateX(-50%);
  background:rgba(8,8,15,0.9); border:1px solid #222;
  border-radius:8px; padding:6px 14px; z-index:10;
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
  background:rgba(8,8,15,0.9); border:1px solid #222;
  border-radius:8px; padding:6px 14px; z-index:10;
  display:flex; gap:8px; align-items:center;
}}
#search input {{
  background:#151525; border:1px solid #333; border-radius:4px;
  padding:5px 10px; font-size:13px; color:#ccc; width:260px;
  outline:none;
}}
#search input:focus {{ border-color:#556; }}
#search .count {{ font-size:11px; color:#556; white-space:nowrap; }}
@media (max-width: 768px) {{
  #stats {{ top:8px; left:8px; padding:6px 10px; max-width:60vw; }}
  #stats h2 {{ font-size:12px; }}
  #stats p {{ font-size:9px; }}
  #stats p ~ p {{ display:none; }}
  #nav {{ top:auto; bottom:60px; left:8px; transform:none; padding:4px 8px; gap:6px; }}
  #nav a {{ font-size:11px; padding:4px 8px; }}
  #controls {{ top:8px; right:8px; }}
  #controls button {{ padding:4px 10px; font-size:13px; }}
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
  <a href="full-graph-hierarchy.html">Hierarchy Graph</a>
</div>

<div id="stats">
  <h2>{title}</h2>
  <p>{n_topics} topics &middot; {n_edges} edges &middot; {n_domains} domains</p>
  <p>Scroll to zoom &middot; Drag to pan &middot; Hover for details</p>
  <p style="margin-top:6px; color:#444;">Inner &rarr; early childhood &nbsp;&middot;&nbsp; Outer &rarr; graduate</p>
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

const nodeMap = {{}};
data.nodes.forEach((n, i) => {{ n.idx = i; nodeMap[n.id] = n; }});

const viewScale = Math.min(W, H) / 1200;

const edgeData = data.edges.map(e => ({{
  s: nodeMap[e.source],
  t: nodeMap[e.target],
  type: e.type,
  crossDomain: nodeMap[e.source] && nodeMap[e.target] &&
               nodeMap[e.source].domain !== nodeMap[e.target].domain,
}})).filter(e => e.s && e.t);

let camX = 0, camY = 0, camScale = 1;
function resetView() {{ camX = 0; camY = 0; camScale = 1; draw(); }}
function zoomBtn(f) {{ camScale = Math.max(0.1, Math.min(20, camScale * f)); draw(); }}

const nodeRadius = Math.max(2, Math.min(4, 1600 / data.nodes.length));

function draw() {{
  ctx.save();
  ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  ctx.clearRect(0, 0, W, H);
  ctx.fillStyle = "#08080f";
  ctx.fillRect(0, 0, W, H);

  ctx.save();
  ctx.translate(W / 2 + camX, H / 2 + camY);
  ctx.scale(camScale * viewScale, camScale * viewScale);

  // Draw stage ring labels (no hard boundary lines — bands overlap)
  data.stageRings.forEach(ring => {{
    ctx.font = "7px sans-serif";
    ctx.fillStyle = "rgba(255,255,255,0.10)";
    ctx.textAlign = "left";
    ctx.textBaseline = "middle";
    ctx.fillText(ring.label, ring.mid + 4, -2);
  }});

  // Draw subtle sector dividers and domain labels
  data.sectors.forEach(s => {{
    // Sector divider
    ctx.beginPath();
    ctx.moveTo(
      {STAGE_BANDS['pre-formal'][0] * 500 - 15} * Math.cos(s.start),
      {STAGE_BANDS['pre-formal'][0] * 500 - 15} * Math.sin(s.start)
    );
    ctx.lineTo(
      {STAGE_BANDS['advanced'][1] * 500 + 15} * Math.cos(s.start),
      {STAGE_BANDS['advanced'][1] * 500 + 15} * Math.sin(s.start)
    );
    ctx.strokeStyle = "rgba(255,255,255,0.03)";
    ctx.lineWidth = 0.3;
    ctx.stroke();

    // Domain label at outer edge
    const labelR = {STAGE_BANDS['advanced'][1] * 500 + 40};
    const lx = labelR * Math.cos(s.mid);
    const ly = labelR * Math.sin(s.mid);
    ctx.save();
    ctx.translate(lx, ly);
    let rot = s.mid;
    if (rot > Math.PI / 2 && rot < 3 * Math.PI / 2) rot += Math.PI;
    ctx.rotate(rot);
    ctx.font = "bold 8px sans-serif";
    ctx.fillStyle = `hsla(${{s.hue}}, 50%, 60%, 0.7)`;
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";
    ctx.fillText(s.label, 0, 0);
    ctx.restore();
  }});

  // Draw edges
  edgeData.forEach(e => {{
    ctx.beginPath();
    ctx.moveTo(e.s.x, e.s.y);
    ctx.lineTo(e.t.x, e.t.y);
    if (e.crossDomain) {{
      ctx.strokeStyle = "rgba(160,120,255,0.03)";
    }} else if (e.type === "soft") {{
      ctx.strokeStyle = "rgba(100,100,140,0.05)";
    }} else {{
      ctx.strokeStyle = "rgba(100,100,140,0.08)";
    }}
    ctx.lineWidth = 0.35;
    ctx.stroke();
  }});

  // Draw nodes
  data.nodes.forEach(n => {{
    ctx.beginPath();
    ctx.arc(n.x, n.y, nodeRadius, 0, Math.PI * 2);
    ctx.fillStyle = `hsl(${{n.hue}}, 55%, ${{n.lightness}}%)`;
    ctx.fill();
  }});

  // Draw highlights for selected node (persists after click)
  const highlightTarget = selectedNode || hoveredNode;
  if (highlightTarget) {{
    drawHighlight(highlightTarget);
  }}

  // Draw search match highlights
  if (searchMatches.length > 0) {{
    searchMatches.forEach(n => {{
      ctx.beginPath();
      ctx.arc(n.x, n.y, nodeRadius * 3, 0, Math.PI * 2);
      ctx.fillStyle = `hsl(${{n.hue}}, 80%, ${{n.lightness + 15}}%)`;
      ctx.fill();
      ctx.strokeStyle = "rgba(255,255,100,0.8)";
      ctx.lineWidth = 1.5;
      ctx.stroke();
    }});
    // Label single match
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
  // Highlight connected edges (blue=prereqs, orange=dependents)
  edgeData.forEach(ed => {{
    if (ed.s === node || ed.t === node) {{
      ctx.beginPath();
      ctx.moveTo(ed.s.x, ed.s.y);
      ctx.lineTo(ed.t.x, ed.t.y);
      ctx.strokeStyle = ed.t === node
        ? "rgba(80,180,255,0.6)"
        : "rgba(255,160,80,0.6)";
      ctx.lineWidth = 1.2;
      ctx.stroke();
    }}
  }});

  // Highlight connected nodes
  edgeData.forEach(ed => {{
    const other = ed.s === node ? ed.t : ed.t === node ? ed.s : null;
    if (other) {{
      ctx.beginPath();
      ctx.arc(other.x, other.y, nodeRadius * 2, 0, Math.PI * 2);
      ctx.fillStyle = `hsl(${{other.hue}}, 70%, ${{other.lightness + 12}}%)`;
      ctx.fill();
      ctx.strokeStyle = "rgba(255,255,255,0.3)";
      ctx.lineWidth = 0.6;
      ctx.stroke();
    }}
  }});

  // Main node highlight
  ctx.beginPath();
  ctx.arc(node.x, node.y, nodeRadius * 3, 0, Math.PI * 2);
  ctx.fillStyle = `hsl(${{node.hue}}, 80%, ${{node.lightness + 20}}%)`;
  ctx.fill();
  ctx.strokeStyle = "#fff";
  ctx.lineWidth = 1.5;
  ctx.stroke();

  // Label
  ctx.font = "bold 9px sans-serif";
  ctx.fillStyle = "#fff";
  ctx.textAlign = "center";
  ctx.fillText(node.title, node.x, node.y - nodeRadius * 4 - 3);
}}

// --- Mouse interaction ---
let isDragging = false, dragStartX, dragStartY;
let lastTouchTime = 0;
let hoveredNode = null;
let selectedNode = null;
let searchMatches = [];

draw();

// --- Search ---
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
}});

function screenToWorld(sx, sy) {{
  return {{
    x: (sx - W / 2 - camX) / (camScale * viewScale),
    y: (sy - H / 2 - camY) / (camScale * viewScale),
  }};
}}

canvas.addEventListener("mousemove", (e) => {{
  if (Date.now() - lastTouchTime < 500) return;
  if (isDragging) {{
    camX += e.clientX - dragStartX;
    camY += e.clientY - dragStartY;
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
    // Show pointer cursor when hovering outer ring (domain labels)
    const wp = screenToWorld(e.clientX, e.clientY);
    const hoverR = Math.hypot(wp.x, wp.y);
    canvas.style.cursor = hoverR > {STAGE_BANDS['advanced'][1] * 500 - 30} ? "pointer" : "grab";
  }}
}});

let dragMoved = false;
canvas.addEventListener("mousedown", (e) => {{
  if (Date.now() - lastTouchTime < 500) return;
  isDragging = true;
  dragMoved = false;
  dragStartX = e.clientX; dragStartY = e.clientY;
  canvas.style.cursor = "grabbing";
}});
const panel = document.getElementById("panel");

function showPanel(node, screenX, screenY) {{
  selectedNode = node;
  // Find prereqs and successors from edge data
  const prereqs = edgeData.filter(e => e.t === node).map(e => ({{
    id: e.s.id, title: e.s.title, hue: e.s.hue, type: e.type
  }}));
  const succs = edgeData.filter(e => e.s === node).map(e => ({{
    id: e.t.id, title: e.t.title, hue: e.t.hue, type: e.type
  }}));

  const domainLabel = node.domain ? node.domain.replace(/-/g, " ") : "";
  const courseLabel = node.course ? node.course.replace(/-/g, " ") : "";

  let html = `<button class="panel-close" onclick="hidePanel()">&times;</button>`;
  html += `<h3><a href="topics/${{node.id}}.html" target="_blank">${{node.title}}</a></h3>`;
  html += `<div class="panel-meta">${{domainLabel}} &middot; ${{courseLabel}}</div>`;

  if (prereqs.length) {{
    html += `<div class="panel-section"><h4>Prerequisites (${{prereqs.length}})</h4>`;
    prereqs.forEach(p => {{
      html += `<div class="panel-item" data-id="${{p.id}}"><span class="panel-dot" style="background:hsl(${{p.hue}},55%,50%)"></span>${{p.title}}<span class="panel-badge ${{p.type}}">${{p.type}}</span></div>`;
    }});
    html += `</div>`;
  }}

  if (succs.length) {{
    html += `<div class="panel-section"><h4>Leads To (${{succs.length}})</h4>`;
    succs.forEach(s => {{
      html += `<div class="panel-item" data-id="${{s.id}}"><span class="panel-dot" style="background:hsl(${{s.hue}},55%,50%)"></span>${{s.title}}<span class="panel-badge ${{s.type}}">${{s.type}}</span></div>`;
    }});
    html += `</div>`;
  }}

  panel.innerHTML = html;
  panel.style.display = "block";
  // Position panel near click but keep on screen
  let px = screenX + 20, py = screenY - 20;
  if (px + 400 > W) px = screenX - 400;
  if (py + 300 > H) py = H - 300;
  if (py < 10) py = 10;
  panel.style.left = px + "px";
  panel.style.top = py + "px";

  // Click on prereq/successor item to select that node
  panel.querySelectorAll(".panel-item").forEach(el => {{
    el.addEventListener("click", () => {{
      const targetId = el.getAttribute("data-id");
      const targetNode = nodeMap[targetId];
      if (targetNode) {{
        hoveredNode = targetNode;
        draw();
        showPanel(targetNode, px, py);
      }}
    }});
  }});

  draw();
}}

function hidePanel() {{
  selectedNode = null;
  panel.style.display = "none";
  draw();
}}

canvas.addEventListener("mouseup", (e) => {{
  if (Date.now() - lastTouchTime < 500) return;
  isDragging = false;
  canvas.style.cursor = "grab";
  if (!dragMoved) {{
    if (hoveredNode) {{
      showPanel(hoveredNode, e.clientX, e.clientY);
    }} else {{
      hidePanel();
      // Check if click is in the outer ring (domain label area)
      const wp = screenToWorld(e.clientX, e.clientY);
      const clickR = Math.hypot(wp.x, wp.y);
      if (clickR > {STAGE_BANDS['advanced'][1] * 500 - 30}) {{
        let clickAngle = Math.atan2(wp.y, wp.x);
        if (clickAngle < 0) clickAngle += Math.PI * 2;
        for (const s of data.sectors) {{
          let start = s.start, end = s.end;
          if (start < 0) start += Math.PI * 2;
          if (end < 0) end += Math.PI * 2;
          if (clickAngle >= start && clickAngle <= end) {{
            window.location.href = s.domain + "-hierarchy.html";
            break;
          }}
        }}
      }}
    }}
  }}
}});

document.addEventListener("keydown", (e) => {{
  if (e.key === "Escape") {{
    hidePanel();
    searchInput.value = "";
    searchMatches = [];
    searchCount.textContent = "";
    searchInput.blur();
    draw();
  }}
}});
canvas.addEventListener("mousemove", (e) => {{
  if (Date.now() - lastTouchTime < 500) return;
  if (isDragging) {{
    const dx = e.clientX - dragStartX;
    const dy = e.clientY - dragStartY;
    if (Math.abs(dx) > 3 || Math.abs(dy) > 3) dragMoved = true;
  }}
}});
canvas.addEventListener("wheel", (e) => {{
  e.preventDefault();
  const factor = e.deltaY > 0 ? 0.9 : 1.1;
  camScale = Math.max(0.1, Math.min(20, camScale * factor));
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
    // Track total displacement from start — 15px threshold for touch
    const totalDx = e.touches[0].clientX - touchStartX;
    const totalDy = e.touches[0].clientY - touchStartY;
    if (Math.hypot(totalDx, totalDy) > 15) dragMoved = true;
    draw();
  }} else if (e.touches.length === 2) {{
    const dist = touchDist(e.touches);
    const c = touchCenter(e.touches);
    // Pinch zoom anchored at pinch center
    if (lastPinchDist > 0) {{
      const factor = dist / lastPinchDist;
      const oldScale = camScale;
      camScale = Math.max(0.1, Math.min(20, camScale * factor));
      const r = camScale / oldScale;
      camX = camX * r + (c.x - W / 2) * (1 - r);
      camY = camY * r + (c.y - H / 2) * (1 - r);
    }}
    // Two-finger pan
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
</script>
</body>
</html>"""


def main():
    parser = argparse.ArgumentParser(description="Radial knowledge graph visualization")
    parser.add_argument("--output", help="Output file path")
    args = parser.parse_args()

    print("Loading topics...")
    all_data = load_all_topics()
    configs = load_domain_configs()
    print(f"Loaded {len(all_data)} topics across {len(configs)} domains")

    print("Computing depths...")
    depths = compute_depths(all_data)

    print("Computing radial layout...")
    positions, sectors, domain_order = build_radial_layout(all_data, configs, depths)

    print("Generating HTML...")
    html = generate_radial_html(all_data, configs, depths, positions, sectors, domain_order)

    out = Path(args.output) if args.output else OUTPUT_DIR / "radial-graph.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    print(f"Saved: {out}")

    # Print layout summary
    stage_counts = defaultdict(int)
    for tid in positions:
        stage = get_topic_stage(all_data[tid], configs)
        stage_counts[stage] += 1
    print("\nTopics per developmental ring:")
    for stage in STAGE_BANDS:
        print(f"  {stage:25s}  {stage_counts.get(stage, 0):4d} topics")
    print(f"\nDomain ordering:")
    for i, d in enumerate(domain_order):
        print(f"  {i + 1:2}. {d}")


if __name__ == "__main__":
    main()
