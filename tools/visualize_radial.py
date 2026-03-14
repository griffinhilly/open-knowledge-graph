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
    "pre-formal":          (0.10, 0.22),   # ages ~4-7, K-1st
    "concrete-operations": (0.22, 0.42),   # ages ~7-12, 2nd-6th
    "abstract-reasoning":  (0.42, 0.65),   # ages ~12-16, 7th-10th
    "formal-systems":      (0.65, 0.85),   # ages ~16-22, 11th-college
    "advanced":            (0.85, 1.00),   # ages ~22+, graduate
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
    "chemistry",
    "earth-and-space-sciences",
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

        # Jitter for organic feel
        angle_jitter = (random.random() - 0.5) * sector_width / max(n_courses, 1) * 0.5
        radial_jitter = (random.random() - 0.5) * (band_max - band_min) * max_radius * 0.08

        theta = base_angle + angle_jitter
        r = max(20, r + radial_jitter)

        x = r * math.cos(theta)
        y = r * math.sin(theta)

        positions[tid] = {
            "x": x, "y": y,
            "r": r, "theta": theta,
            "target_r": r,  # For radial spring-back
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
            ps["y"] -= fy  # Slight asymmetry to prevent collapse
            pt["x"] -= fx
            pt["y"] += fy

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
<title>{title}</title>
<style>
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{ background:#08080f; font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif; overflow:hidden; color:#ccc; }}
canvas {{ display:block; cursor:grab; }}
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
</style>
</head>
<body>

<canvas id="canvas"></canvas>

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

  // Draw stage rings (concentric bands)
  data.stageRings.forEach(ring => {{
    // Ring band
    ctx.beginPath();
    ctx.arc(0, 0, ring.outer, 0, Math.PI * 2);
    ctx.strokeStyle = "rgba(255,255,255,0.03)";
    ctx.lineWidth = 0.5;
    ctx.stroke();

    // Ring label (at right side)
    ctx.font = "7px sans-serif";
    ctx.fillStyle = "rgba(255,255,255,0.12)";
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

  ctx.restore();
  ctx.restore();
}}

draw();

// --- Mouse interaction ---
let isDragging = false, dragStartX, dragStartY;
let hoveredNode = null;

function screenToWorld(sx, sy) {{
  return {{
    x: (sx - W / 2 - camX) / (camScale * viewScale),
    y: (sy - H / 2 - camY) / (camScale * viewScale),
  }};
}}

canvas.addEventListener("mousemove", (e) => {{
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
      ctx.save();
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      ctx.translate(W / 2 + camX, H / 2 + camY);
      ctx.scale(camScale * viewScale, camScale * viewScale);

      // Highlight connected edges (blue=prereqs, orange=dependents)
      edgeData.forEach(ed => {{
        if (ed.s === closest || ed.t === closest) {{
          ctx.beginPath();
          ctx.moveTo(ed.s.x, ed.s.y);
          ctx.lineTo(ed.t.x, ed.t.y);
          ctx.strokeStyle = ed.t === closest
            ? "rgba(80,180,255,0.6)"
            : "rgba(255,160,80,0.6)";
          ctx.lineWidth = 1.2;
          ctx.stroke();
        }}
      }});

      // Highlight connected nodes
      edgeData.forEach(ed => {{
        const other = ed.s === closest ? ed.t : ed.t === closest ? ed.s : null;
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
      ctx.arc(closest.x, closest.y, nodeRadius * 3, 0, Math.PI * 2);
      ctx.fillStyle = `hsl(${{closest.hue}}, 80%, ${{closest.lightness + 20}}%)`;
      ctx.fill();
      ctx.strokeStyle = "#fff";
      ctx.lineWidth = 1.5;
      ctx.stroke();

      // Label
      ctx.font = "bold 9px sans-serif";
      ctx.fillStyle = "#fff";
      ctx.textAlign = "center";
      ctx.fillText(closest.title, closest.x, closest.y - nodeRadius * 4 - 3);

      ctx.restore();
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
  isDragging = true;
  dragMoved = false;
  dragStartX = e.clientX; dragStartY = e.clientY;
  canvas.style.cursor = "grabbing";
}});
canvas.addEventListener("mouseup", (e) => {{
  isDragging = false;
  canvas.style.cursor = "grab";
  // Click (not drag) → open detail page or domain hierarchy
  if (!dragMoved) {{
    if (hoveredNode) {{
      window.open("topics/" + hoveredNode.id + ".html", "_blank");
    }} else {{
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
canvas.addEventListener("mousemove", (e) => {{
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
