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
        nodes[topic_id] = {
            "id": topic_id,
            "title": data.get("title", topic_id),
            "domain": domain,
            "course": course,
            "stage": data.get("stage", ""),
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
                    "title": edge["source"].replace("-", " ").title(),
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
        label = course.replace("-", " ").title()
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
<title>{title}</title>
<style>
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{ background:#1a1a2e; font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif; overflow:hidden; color:#ccc; }}
canvas {{ display:block; }}
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

  ctx.restore();
  ctx.restore();
}}

draw();

// Mouse interaction
let isDragging = false, dragStartX, dragStartY;
let hoveredNode = null;

function screenToWorld(sx, sy) {{
  return {{
    x: (sx - W / 2 - camX) / camScale + W / 2,
    y: (sy - H / 2 - camY) / camScale + H / 2,
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

  const hitRadius = Math.max(nodeRadius * 1.5, 8) / camScale;
  if (closest && closestDist < hitRadius) {{
    if (hoveredNode !== closest) {{
      hoveredNode = closest;
      draw();
      ctx.save();
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      ctx.translate(W / 2 + camX, H / 2 + camY);
      ctx.scale(camScale, camScale);
      ctx.translate(-W / 2, -H / 2);

      edgeData.forEach(ed => {{
        if (ed.s === closest || ed.t === closest) {{
          ctx.beginPath();
          ctx.moveTo(ed.s.x, ed.s.y);
          ctx.lineTo(ed.t.x, ed.t.y);
          ctx.strokeStyle = ed.t === closest
            ? "rgba(80,180,255,0.6)"
            : "rgba(255,160,80,0.6)";
          ctx.lineWidth = 1.5;
          ctx.stroke();
        }}
      }});

      ctx.beginPath();
      ctx.arc(closest.x, closest.y, nodeRadius * 2, 0, Math.PI * 2);
      ctx.fillStyle = closest.color;
      ctx.fill();
      ctx.strokeStyle = "#fff";
      ctx.lineWidth = 1.5;
      ctx.stroke();

      ctx.font = "bold 11px sans-serif";
      ctx.fillStyle = "#fff";
      ctx.textAlign = "center";
      ctx.fillText(closest.title, closest.x, closest.y - nodeRadius * 2.5 - 4);

      ctx.restore();
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
  isDragging = true;
  dragMoved = false;
  dragStartX = e.clientX;
  dragStartY = e.clientY;
  canvas.style.cursor = "grabbing";
}});
canvas.addEventListener("mouseup", (e) => {{
  isDragging = false;
  canvas.style.cursor = "default";
  if (!dragMoved && hoveredNode) {{
    window.open("topics/" + hoveredNode.id + ".html", "_blank");
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
  camScale *= factor;
  camScale = Math.max(0.1, Math.min(10, camScale));
  draw();
}}, {{ passive: false }});
</script>
</body>
</html>"""


def generate_index_html(domains_info):
    """Generate an index page linking to all domain visualizations."""
    rows = ""
    total_topics = 0
    total_edges = 0
    for domain, info in sorted(domains_info.items()):
        label = domain.replace("-", " ").title()
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

            title = f"Open Knowledge Graph — {domain.replace('-', ' ').title()}"
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

        # Generate full graph
        print("Generating full cross-domain graph...")
        all_course_order = []
        all_colors = {}
        for domain, cfg in sorted(configs.items()):
            course_ids = cfg["course_ids"]
            colors = generate_course_colors(domain, course_ids)
            all_course_order.extend(course_ids)
            all_colors.update(colors)

        nodes, edges = load_graph()
        title = "Open Knowledge Graph — All Domains"
        html = generate_html(nodes, edges, title=title,
                            course_colors=all_colors, course_order=all_course_order)
        out = OUTPUT_DIR / "full-graph-hierarchy.html"
        out.write_text(html, encoding="utf-8")
        print(f"  {len(nodes)} topics, {len(edges)} edges -> {out.name}")

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
        title = f"Open Knowledge Graph — {name.replace('-', ' ').title()}"
        out = Path(args.output) if args.output else OUTPUT_DIR / f"{name}-hierarchy.html"

        html = generate_html(nodes, edges, title=title,
                            course_colors=colors, course_order=course_ids)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(html, encoding="utf-8")
        print(f"Saved: {out}")


if __name__ == "__main__":
    main()
