#!/usr/bin/env python3
"""Generate knowledge maps with boxed labels.

Course-level: topics within one course, ordered by within-course depth.
Domain-level: courses stacked top-to-bottom, topics within each by depth.
Barycenter ordering minimizes edge crossings on the X-axis.

Usage:
    python tools/visualize_domain_map.py --domain mathematics --course algebra-1
    python tools/visualize_domain_map.py --domain mathematics --all-courses
    python tools/visualize_domain_map.py --domain mathematics
    python tools/visualize_domain_map.py --all
"""

import sys
import re
import json
import argparse
import math
import yaml
from pathlib import Path
from collections import defaultdict, deque

ROOT = Path(__file__).resolve().parent.parent
DOMAINS_DIR = ROOT / "domains"
OUTPUT_DIR = ROOT / "output"

# Layout constants
BOX_MARGIN = 16        # horizontal gap between boxes
LAYER_SPACING = 55     # vertical gap between depth layers
GAP_LAYER_SPACING = 30 # vertical gap for empty layers (course boundaries)
CHAR_WIDTH_RATIO = 0.58  # char width / font size ratio for sans-serif
BOX_PAD_X = 14         # horizontal padding inside box
BOX_PAD_Y = 10         # vertical padding inside box
BASE_FONT = 10
MIN_BOX_W = 55
MAX_BOX_W = 220


# Branch X-positions: latent left-right embedding per course.
# Each domain has a natural left-right axis (see comments).
# Courses not listed here get auto-derived from _domain.yml ordering.
COURSE_BRANCH_X = {
    # Mathematics: discrete/structure (left) → analysis/continuous (right)
    "kindergarten": 0.45, "1st-grade": 0.48, "2nd-grade": 0.50,
    "3rd-grade": 0.50, "4th-grade": 0.52, "5th-grade": 0.50,
    "prealgebra": 0.45, "algebra-1": 0.40, "geometry": 0.55,
    "algebra-2": 0.42, "precalculus": 0.55,
    "discrete-math": 0.10, "methods-of-proof": 0.25,
    "linear-algebra": 0.35, "abstract-algebra": 0.20,
    "calculus-1": 0.60, "calculus-2": 0.63,
    "multivariable-calculus": 0.65, "probability-and-statistics": 0.82,
    "graph-theory-and-combinatorics": 0.08, "number-theory": 0.15,
    "topology": 0.38, "differential-equations": 0.58,
    "real-analysis": 0.62, "complex-analysis": 0.68,
    "measure-theory-and-functional-analysis": 0.65,
    "probability-and-mathematical-statistics": 0.85, "numerical-analysis": 0.80,
    # Physics: theoretical/fundamental (left) → applied/phenomenological (right)
    "conceptual-physics": 0.05, "classical-mechanics": 0.20,
    "modern-physics": 0.30, "quantum-mechanics": 0.25,
    "statistical-mechanics": 0.75, "waves-and-optics": 0.50,
    "electricity-and-magnetism": 0.60, "electrodynamics": 0.65,
    "thermodynamics": 0.80, "physical-science": 0.95,
    # Computer Science: theoretical (left) → systems (right)
    "theory-of-computation": 0.05, "compilers": 0.15,
    "data-structures-and-algorithms": 0.25, "artificial-intelligence": 0.35,
    "programming-fundamentals": 0.45, "computer-architecture": 0.60,
    "computer-networking": 0.70, "operating-systems": 0.78,
    "distributed-systems": 0.88, "databases": 0.95,
    # Biology: molecular (left) → ecological (right)
    "genetics-and-molecular-biology": 0.05, "biochemistry": 0.12,
    "cell-biology": 0.20, "immunology": 0.30,
    "microbiology": 0.38, "neuroscience": 0.45,
    "physiology": 0.55, "evolutionary-biology": 0.65,
    "living-things": 0.75, "life-science": 0.82,
    "ecology-and-evolution": 0.95,
    # Chemistry: physical/theoretical (left) → analytical (right)
    "physical-chemistry": 0.05, "properties-of-matter": 0.22,
    "introductory-chemistry": 0.38, "general-chemistry": 0.50,
    "organic-chemistry": 0.70, "analytical-chemistry": 0.95,
    # Earth & Space: surface (left) → deep space (right)
    "earth-and-weather": 0.05, "meteorology-and-climate": 0.18,
    "climate-science": 0.28, "oceanography": 0.38,
    "earth-science": 0.48, "geology": 0.58,
    "geophysics": 0.70, "planetary-science": 0.82, "astronomy": 0.95,
    # Economics: micro (left) → macro (right)
    "microeconomics": 0.05, "advanced-microeconomics": 0.18,
    "financial-economics": 0.35, "econometrics": 0.55,
    "development-economics": 0.70, "macroeconomics": 0.82,
    "advanced-macroeconomics": 0.95,
    # Engineering: theoretical (left) → applied (right)
    "engineering-principles": 0.05, "statics-and-dynamics": 0.20,
    "materials-science": 0.35, "fluid-mechanics": 0.50,
    "signals-and-systems": 0.58, "circuits-and-electronics": 0.65,
    "thermodynamics-engineering": 0.75, "control-systems": 0.85,
    "design-and-build": 0.95,
    # Formal Sciences: foundational (left) → abstract (right)
    "patterns-and-logic": 0.05, "reasoning-and-proof": 0.18,
    "propositional-and-predicate-logic": 0.35, "set-theory": 0.52,
    "computability-and-complexity": 0.68, "model-theory": 0.82,
    "category-theory": 0.95,
    # Health: individual body (left) → population (right)
    "my-body": 0.05, "anatomy-and-physiology": 0.18,
    "pathophysiology": 0.30, "nutrition-science": 0.42,
    "health-foundations": 0.55, "child-development": 0.68,
    "epidemiology": 0.82, "public-health": 0.95,
    # History: methods then ancient (left) → modern (right)
    "historical-methods": 0.05, "historiography": 0.18,
    "ancient-civilizations": 0.32, "medieval-world": 0.50,
    "early-modern-period": 0.72, "modern-history": 0.95,
    # Language: structure (left) → performance (right)
    "early-language-foundations": 0.05, "grammar-and-syntax": 0.22,
    "linguistics": 0.40, "advanced-linguistics": 0.50,
    "rhetoric-and-composition": 0.68, "public-speaking": 0.95,
    # Literature: analysis (left) → creative genres (right)
    "critical-theory": 0.05, "comparative-literature": 0.18,
    "literary-analysis": 0.35, "poetry": 0.55, "fiction": 0.72, "drama": 0.95,
    # Music: theory (left) → practice (right)
    "music-theory-fundamentals": 0.05, "advanced-music-theory": 0.18,
    "harmony-and-voice-leading": 0.32, "music-history": 0.50,
    "ear-training": 0.72, "composition": 0.95,
    # Philosophy: formal/logical (left) → applied/practical (right)
    "logic-and-critical-thinking": 0.05, "philosophy-of-language": 0.15,
    "epistemology": 0.28, "metaphysics": 0.40, "philosophy-of-mind": 0.50,
    "philosophy-of-science": 0.60, "ethics": 0.75,
    "political-philosophy": 0.85, "applied-rationality": 0.95,
    # Practical Life: personal/financial (left) → digital (right)
    "financial-literacy": 0.05, "cooking-and-nutrition": 0.35,
    "home-maintenance": 0.65, "digital-literacy": 0.95,
    # Psychology: biological (left) → social (right)
    "biological-psychology": 0.05, "cognitive-neuroscience": 0.18,
    "cognitive-psychology": 0.32, "psychometrics": 0.45,
    "research-methods-psychology": 0.55, "clinical-psychology": 0.68,
    "developmental-psychology": 0.78, "social-psychology": 0.95,
    # Social Sciences: individual/cultural (left) → structural (right)
    "anthropology": 0.05, "research-methods-social-science": 0.20,
    "sociology": 0.35, "sociological-theory": 0.45,
    "human-geography": 0.65, "international-relations-theory": 0.78,
    "political-science": 0.95,
    # Arts: foundations (left) → applied (right)
    "visual-elements-and-principles": 0.05, "aesthetic-theory": 0.22,
    "art-history": 0.42, "drawing-and-painting": 0.68, "design-principles": 0.95,
}


def smart_title(slug):
    words = slug.replace("-", " ").split()
    return " ".join(w if w[0].isdigit() else w.capitalize() for w in words if w)


def parse_frontmatter(filepath):
    try:
        text = filepath.read_text(encoding="utf-8")
    except Exception:
        return None
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not m:
        return None
    raw = yaml.safe_load(m.group(1))
    if not isinstance(raw, dict) or "id" not in raw:
        return None
    data = {}
    for field in ("id", "title", "domain", "course", "stage"):
        if field in raw:
            data[field] = str(raw[field])
    tags = raw.get("tags", [])
    data["tags"] = [str(t) for t in tags] if isinstance(tags, list) else []
    prereqs = []
    for p in raw.get("prerequisites", []) or []:
        if isinstance(p, dict) and "id" in p:
            prereqs.append({
                "id": str(p["id"]),
                "type": str(p.get("type", "hard")),
            })
    data["prerequisites"] = prereqs
    return data


def parse_domain_yml(filepath):
    raw = yaml.safe_load(filepath.read_text(encoding="utf-8"))
    if not isinstance(raw, dict):
        return {"courses": []}
    data = {}
    if "title" in raw:
        data["title"] = str(raw["title"])
    courses = []
    for c in raw.get("courses", []) or []:
        if isinstance(c, dict) and "id" in c:
            cid = str(c["id"])
            courses.append({
                "id": cid,
                "title": str(c.get("title", "") or smart_title(cid)),
                "stage": str(c.get("stage", "") or "abstract-reasoning"),
            })
    data["courses"] = courses
    return data


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

def count_cross_domain_edges(domain_nids):
    """Count cross-domain edges for each node in a domain.

    Scans ALL domains to find edges where one endpoint is in domain_nids
    and the other is not. Returns dict: node_id -> count of cross-domain edges.
    """
    cross_counts = defaultdict(int)
    for fp in sorted(DOMAINS_DIR.rglob("*.md")):
        d = parse_frontmatter(fp)
        if not d:
            continue
        tid = d["id"]
        for p in d.get("prerequisites", []):
            pid = p["id"]
            # Edge: pid -> tid (pid is prereq of tid)
            if pid in domain_nids and tid not in domain_nids:
                cross_counts[pid] += 1  # domain node is depended on from outside
            elif tid in domain_nids and pid not in domain_nids:
                cross_counts[tid] += 1  # domain node depends on outside


    return cross_counts


def load_domain(domain, course_filter=None):
    """Load topics, edges, and config for a domain (optionally filtered to one course)."""
    domain_dir = DOMAINS_DIR / domain
    if not domain_dir.exists():
        return {}, [], {}

    config = parse_domain_yml(domain_dir / "_domain.yml")
    course_stages = {c["id"]: c["stage"] for c in config.get("courses", [])}
    course_ids = [c["id"] for c in config.get("courses", [])]
    course_titles = {c["id"]: c["title"] for c in config.get("courses", [])}

    nodes = {}
    edges = []
    for fp in sorted(domain_dir.rglob("*.md")):
        d = parse_frontmatter(fp)
        if not d or d.get("domain") != domain:
            continue
        if course_filter and d.get("course") != course_filter:
            continue
        tid = d["id"]
        stage = d.get("stage", "") or course_stages.get(d.get("course", ""), "")
        nodes[tid] = {
            "id": tid,
            "title": d.get("title", tid),
            "course": d.get("course", ""),
            "stage": stage,
            "tags": d.get("tags", []),
        }
        for p in d.get("prerequisites", []):
            edges.append({
                "source": p["id"],
                "target": tid,
                "type": p.get("type", "hard"),
            })

    nids = set(nodes.keys())
    edges = [e for e in edges if e["source"] in nids and e["target"] in nids]
    return nodes, edges, {
        "course_ids": course_ids,
        "course_titles": course_titles,
        "course_stages": course_stages,
        "title": config.get("title", smart_title(domain)),
    }


# ---------------------------------------------------------------------------
# Graph analysis
# ---------------------------------------------------------------------------

def compute_depth(nodes, edges):
    """Longest path from any root to each node."""
    nids = set(nodes.keys())
    children = defaultdict(list)
    in_deg = defaultdict(int)
    for e in edges:
        s, t = e["source"], e["target"]
        children[s].append(t)
        in_deg[t] += 1
    depth = {}
    q = deque()
    for nid in nids:
        if in_deg[nid] == 0:
            depth[nid] = 0
            q.append(nid)
    while q:
        nid = q.popleft()
        for c in children[nid]:
            nd = depth[nid] + 1
            if c not in depth or nd > depth[c]:
                depth[c] = nd
                q.append(c)
    for nid in nids:
        if nid not in depth:
            depth[nid] = 0
    return depth


def compute_course_depths(nodes, edges, course_ids):
    """Within-course depth for every node. Returns (depth_map, course_max_depth)."""
    course_nodes = defaultdict(set)
    for nid, node in nodes.items():
        course_nodes[node["course"]].add(nid)

    course_edges = defaultdict(list)
    for e in edges:
        s, t = e["source"], e["target"]
        if s in nodes and t in nodes and nodes[s]["course"] == nodes[t]["course"]:
            course_edges[nodes[s]["course"]].append(e)

    depth = {}
    course_max = {}
    for cid in course_ids:
        cnids = course_nodes.get(cid, set())
        if not cnids:
            course_max[cid] = 0
            continue
        cnodes = {nid: nodes[nid] for nid in cnids}
        cdepth = compute_depth(cnodes, course_edges[cid])
        depth.update(cdepth)
        course_max[cid] = max(cdepth.values()) if cdepth else 0

    return depth, course_max


def compute_connectivity(nodes, edges):
    """Weighted connectivity: out-degree (being a prereq) counts 2x.

    Topics that are prerequisites to many others are more foundational
    and deserve more visual prominence than topics that merely have
    many prerequisites flowing into them.
    """
    in_deg = defaultdict(int)
    out_deg = defaultdict(int)
    nids = set(nodes.keys())
    for e in edges:
        if e["source"] in nids:
            out_deg[e["source"]] += 1
        if e["target"] in nids:
            in_deg[e["target"]] += 1
    return {nid: out_deg.get(nid, 0) * 2 + in_deg.get(nid, 0)
            for nid in nodes}


# ---------------------------------------------------------------------------
# Box dimensions
# ---------------------------------------------------------------------------

def estimate_box_dims(nodes, connectivity):
    """Box dimensions scaled by connectivity (area ~ degree).

    Uses fixed ceiling (DEGREE_CEILING=25) so sizing is consistent
    across course-level and domain-level views.
    Degree 1: 60x18, 8px font.  Degree 13: ~170x36, 14px font.
    Area ratio for degree 13 vs 2: ~5x (matching target).
    Text truncated by JS if it exceeds box width.
    """
    DEGREE_CEILING = 25
    dims = {}
    for nid, node in nodes.items():
        deg = max(connectivity.get(nid, 0), 1)
        norm = min((deg - 1) / DEGREE_CEILING, 1.0)  # linear 0..1

        font_size = max(8, round(8 + 12 * norm))      # 8 to 20
        w = round(60 + 220 * norm, 1)                  # 60 to 280
        h = round(18 + 37 * norm, 1)                   # 18 to 55
        dims[nid] = {
            "w": w,
            "h": h,
            "fontSize": font_size,
            "degree": deg,
            "scale": round(1 + 3 * norm, 2),
        }
    return dims


# ---------------------------------------------------------------------------
# Barycenter layered layout (Sugiyama-style)
# ---------------------------------------------------------------------------

def compute_layered_layout(nodes, edges, depth_map, box_dims, course_branch_x=None):
    """Barycenter ordering with branch-seeded horizontal embedding."""
    if course_branch_x is None:
        course_branch_x = {}
    # Group by depth layer
    layers = defaultdict(list)
    for nid in nodes:
        layers[depth_map.get(nid, 0)].append(nid)
    max_d = max(depth_map.values()) if depth_map else 0

    # Adjacency
    nids = set(nodes.keys())
    children_of = defaultdict(list)
    parents_of = defaultdict(list)
    for e in edges:
        s, t = e["source"], e["target"]
        if s in nids and t in nids:
            children_of[s].append(t)
            parents_of[t].append(s)

    # Initial sort by course branch position (if available), then title
    # branch_x provides a latent left-right embedding per course
    branch_x = {}
    for nid, node in nodes.items():
        branch_x[nid] = course_branch_x.get(node.get("course", ""), 0.5)

    for d in range(max_d + 1):
        layers[d].sort(key=lambda nid: (branch_x.get(nid, 0.5),
                                         nodes[nid]["title"].lower()))

    # Initial X: spread based on branch position (not sequential from 0)
    x_pos = {}
    ref_width = 2000  # reference canvas width for initial spread
    for d in range(max_d + 1):
        for nid in layers[d]:
            x_pos[nid] = branch_x.get(nid, 0.5) * ref_width

    # Place sequentially in sort order (respecting overlap), anchored
    # on the layer's connected-neighbor centroid instead of x=0
    def place_layer(d):
        if not layers[d]:
            return
        # Compute anchor from connected neighbors
        nbr_xs = []
        for nid in layers[d]:
            for p in parents_of[nid]:
                if p in x_pos:
                    nbr_xs.append(x_pos[p])
            for c in children_of[nid]:
                if c in x_pos:
                    nbr_xs.append(x_pos[c])
        anchor = sum(nbr_xs) / len(nbr_xs) if nbr_xs else ref_width / 2

        # Compute total layer width
        total_w = sum(box_dims[nid]["w"] + BOX_MARGIN for nid in layers[d])
        x = anchor - total_w / 2
        for nid in layers[d]:
            w = box_dims[nid]["w"]
            x_pos[nid] = x + w / 2
            x += w + BOX_MARGIN

    # Barycenter iterations with centroid-anchored placement
    for _ in range(25):
        # Top-down pass
        for d in range(1, max_d + 1):
            bary = {}
            for nid in layers[d]:
                ps = [p for p in parents_of[nid] if p in x_pos]
                bary[nid] = (sum(x_pos[p] for p in ps) / len(ps)) if ps else x_pos[nid]
            layers[d].sort(key=lambda nid: bary[nid])
            place_layer(d)
        # Bottom-up pass
        for d in range(max_d - 1, -1, -1):
            bary = {}
            for nid in layers[d]:
                cs = [c for c in children_of[nid] if c in x_pos]
                bary[nid] = (sum(x_pos[c] for c in cs) / len(cs)) if cs else x_pos[nid]
            layers[d].sort(key=lambda nid: bary[nid])
            place_layer(d)

    # Neighbor-drift: stronger (40%) now that anchoring is correct
    for _ in range(10):
        for d in range(max_d + 1):
            if not layers[d]:
                continue
            for nid in layers[d]:
                nbrs = [p for p in parents_of[nid] if p in x_pos] + \
                       [c for c in children_of[nid] if c in x_pos]
                if not nbrs:
                    continue
                target = sum(x_pos[n] for n in nbrs) / len(nbrs)
                x_pos[nid] += (target - x_pos[nid]) * 0.4
            # Resolve overlaps (maintain barycenter order)
            for i in range(1, len(layers[d])):
                nid = layers[d][i]
                prev = layers[d][i - 1]
                min_x = x_pos[prev] + box_dims[prev]["w"] / 2 + BOX_MARGIN + box_dims[nid]["w"] / 2
                if x_pos[nid] < min_x:
                    x_pos[nid] = min_x

    # Normalize: ensure all positions are positive, compute canvas width
    all_lefts = [x_pos[nid] - box_dims[nid]["w"] / 2 for nid in nodes if nid in x_pos]
    min_x = min(all_lefts) if all_lefts else 0
    if min_x < 30:
        shift = 30 - min_x
        for nid in x_pos:
            x_pos[nid] += shift
    canvas_w = max(x_pos[nid] + box_dims[nid]["w"] / 2 for nid in nodes if nid in x_pos) + 30

    # Y positions (skip empty layers with smaller gap)
    y = 40
    y_pos = {}
    for d in range(max_d + 1):
        if not layers[d]:
            y += GAP_LAYER_SPACING
            continue
        max_h = max(box_dims[nid]["h"] for nid in layers[d])
        for nid in layers[d]:
            y_pos[nid] = y + max_h / 2
        y += max_h + LAYER_SPACING
    canvas_h = y + 30

    # Combine
    positions = {}
    for nid in nodes:
        if nid in x_pos and nid in y_pos:
            positions[nid] = {"x": round(x_pos[nid], 1), "y": round(y_pos[nid], 1)}

    return positions, round(canvas_w), round(canvas_h)


# ---------------------------------------------------------------------------
# Colors
# ---------------------------------------------------------------------------

def get_branch_x(course_ids):
    """Get horizontal branch positions for courses.

    Uses manual COURSE_BRANCH_X mappings where available (math),
    falls back to evenly-spaced positions from _domain.yml ordering.
    """
    n = max(len(course_ids), 1)
    result = {}
    has_manual = any(c in COURSE_BRANCH_X for c in course_ids)
    for i, cid in enumerate(course_ids):
        if cid in COURSE_BRANCH_X:
            result[cid] = COURSE_BRANCH_X[cid]
        elif has_manual:
            result[cid] = 0.5  # domain has some manual entries; default center
        else:
            # Auto: spread evenly across 0.1-0.9
            result[cid] = 0.1 + 0.8 * i / max(n - 1, 1)
    return result


def generate_course_colors(n_courses):
    """Generate n distinct HSL colors using golden angle spacing.

    Each successive course is ~137.5° from the previous on the hue wheel.
    This maximizes visual separation for any number of courses — no two
    adjacent courses will have similar hues regardless of count.
    """
    GOLDEN_ANGLE = 137.508
    colors = []
    for i in range(n_courses):
        hue = (i * GOLDEN_ANGLE + 15) % 360
        sat = 55 + (i % 3) * 10       # 55, 65, 75
        lit = 50 + ((i // 3) % 3) * 7  # 50, 57, 64
        colors.append(f"hsl({int(hue)},{sat}%,{lit}%)")
    return colors


# ---------------------------------------------------------------------------
# HTML generation
# ---------------------------------------------------------------------------

def generate_html(domain, title, nodes, edges, positions, box_dims, canvas_w,
                  canvas_h, depth_map, course_ids, course_colors, course_titles,
                  course_separators=None, is_course_map=False,
                  cross_counts=None):
    """Generate self-contained HTML with boxed-label canvas visualization."""

    # Build node list
    node_list = []
    for nid, node in sorted(nodes.items()):
        if nid not in positions:
            continue
        p = positions[nid]
        bd = box_dims[nid]
        cidx = course_ids.index(node["course"]) if node["course"] in course_ids else 0
        xd = cross_counts.get(nid, 0) if cross_counts else 0
        node_list.append({
            "id": nid,
            "title": node["title"],
            "course": node["course"],
            "stage": node.get("stage", ""),
            "tags": node.get("tags", []),
            "depth": depth_map.get(nid, 0),
            "x": p["x"],
            "y": p["y"],
            "w": bd["w"],
            "h": bd["h"],
            "fontSize": bd["fontSize"],
            "degree": bd["degree"],
            "crossDomain": xd,
            "color": course_colors[cidx] if cidx < len(course_colors) else "hsl(0,0%,50%)",
        })

    pos_ids = set(positions.keys())
    edge_list = [
        {"source": e["source"], "target": e["target"], "type": e["type"]}
        for e in edges if e["source"] in pos_ids and e["target"] in pos_ids
    ]

    # Legend — only courses with topics
    legend = []
    courses_present = set(n["course"] for n in node_list)
    for i, cid in enumerate(course_ids):
        if cid in courses_present:
            legend.append({
                "color": course_colors[i] if i < len(course_colors) else "hsl(0,0%,50%)",
                "label": course_titles.get(cid, smart_title(cid)),
            })

    graph_json = json.dumps({
        "nodes": node_list,
        "edges": edge_list,
        "legend": legend,
        "courseSeparators": course_separators or [],
        "canvasW": canvas_w,
        "canvasH": canvas_h,
        "maxDepth": max(depth_map.values()) if depth_map else 0,
        "isCourseMap": is_course_map,
    })

    n_topics = len(node_list)
    n_edges = len(edge_list)
    n_courses = len(legend)

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
canvas {{ display:block; touch-action:none; }}
#legend {{
  position:fixed; bottom:16px; left:16px;
  background:rgba(26,26,46,0.92); border:1px solid #333;
  border-radius:8px; padding:10px 14px;
  z-index:10; max-height:80vh; overflow-y:auto;
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
#controls button.active {{ background:#2a4a2a; border-color:#4a4; color:#8f8; }}
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
  padding:5px 10px; font-size:13px; color:#ccc; width:260px; outline:none;
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
  #nav a {{ font-size:11px; padding:4px 8px; }}
  #controls {{ padding:6px 8px; }}
  #controls button {{ padding:8px 14px; font-size:14px; min-width:44px; min-height:44px; }}
  #panel {{
    position:fixed !important; left:0 !important; right:0 !important;
    bottom:0 !important; top:auto !important;
    max-width:100% !important; width:100% !important;
    max-height:50vh; border-radius:16px 16px 0 0; border-bottom:none;
    padding:16px 20px 24px; box-sizing:border-box;
  }}
  #panel .panel-close {{ top:12px; right:14px; font-size:24px; padding:8px; }}
  #search {{ width:calc(100vw - 32px); left:16px; transform:none; }}
  #search input {{ flex:1; width:auto; }}
  #tooltip {{ display:none !important; }}
}}
</style>
</head>
<body>

<canvas id="canvas"></canvas>

<div id="stats">
  <h2>{title}</h2>
  <p>{n_topics} topics &middot; {n_edges} edges &middot; {n_courses} course{"" if n_courses == 1 else "s"}</p>
  <p id="helpText">Scroll to zoom &middot; Drag to pan &middot; Hover for details &middot; Click to open</p>
</div>

<div id="legend"></div>
<div id="nav">
  <a href="index.html">All Domains</a>
  <a href="{domain}-map.html">Domain Map</a>
  <a href="radial-graph.html">Radial</a>
</div>
<div id="controls">
  <button onclick="resetView()">Reset</button>
  <button onclick="zoomBtn(1.3)">+</button>
  <button onclick="zoomBtn(0.7)">&minus;</button>
  <button id="fluencyBtn" onclick="toggleFluency()">Fluency</button>
</div>
<div id="tooltip"></div>
<div id="panel"></div>
<div id="search">
  <input type="text" id="searchInput" placeholder="Search topics... (Ctrl+F)">
  <span class="count" id="searchCount"></span>
</div>

<script src="js/fluency.js"></script>
<script>
var data = {graph_json};
var canvas = document.getElementById("canvas");
var ctx = canvas.getContext("2d");
var tooltip = document.getElementById("tooltip");
var panel = document.getElementById("panel");
var selectedNode = null;
var searchMatches = [];

var W, H, dpr;
function resize() {{
  dpr = window.devicePixelRatio || 1;
  W = window.innerWidth; H = window.innerHeight;
  canvas.width = W * dpr; canvas.height = H * dpr;
  canvas.style.width = W + "px"; canvas.style.height = H + "px";
  ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
}}
resize();

// Legend
var legendEl = document.getElementById("legend");
var lhtml = '<h3>Courses</h3>';
data.legend.forEach(function(l) {{
  lhtml += '<div class="legend-row"><span class="legend-dot" style="background:'
    + l.color + '"></span><span class="legend-label">' + l.label + '</span></div>';
}});
legendEl.innerHTML = lhtml;

// Index nodes
var nodeMap = {{}};
data.nodes.forEach(function(n, i) {{ n.idx = i; nodeMap[n.id] = n; }});

// Edge data
var edgeData = data.edges.map(function(e) {{
  return {{ s: nodeMap[e.source], t: nodeMap[e.target], type: e.type }};
}}).filter(function(e) {{ return e.s && e.t; }});

// Fluency
var showFluency = false;
var fluencyGraph = null;
var effectiveScores = null;
var frontierSet = null;

function buildFluencyGraph() {{
  var g = {{}};
  data.nodes.forEach(function(n) {{
    g[n.id] = {{ prereqs: [], successors: [], course: n.course || '' }};
  }});
  data.edges.forEach(function(e) {{
    if (g[e.target]) g[e.target].prereqs.push(e.source);
    if (g[e.source]) g[e.source].successors.push(e.target);
  }});
  return g;
}}

function refreshFluency() {{
  if (typeof OKGFluency === 'undefined') return;
  if (!fluencyGraph) fluencyGraph = buildFluencyGraph();
  effectiveScores = OKGFluency.propagate(fluencyGraph);
  var ids = OKGFluency.findFrontier(fluencyGraph, effectiveScores);
  frontierSet = new Set(ids);
}}

function toggleFluency() {{
  showFluency = !showFluency;
  if (showFluency) refreshFluency();
  document.getElementById('fluencyBtn').classList.toggle('active', showFluency);
  draw();
}}

// Camera
var gw = data.canvasW;
var gh = data.canvasH;
var camScale, camX, camY;

function resetView() {{
  camScale = Math.min(W / (gw + 80), H / (gh + 80)) * 0.92;
  camX = (W / 2 - gw / 2) * camScale;
  camY = (H / 2 - gh / 2) * camScale;
}}
resetView();

// Anchor support: pan/zoom to a course section via URL hash (e.g. #algebra-1)
function panToCourse(courseId) {{
  var courseNodes = data.nodes.filter(function(n) {{ return n.course === courseId; }});
  if (courseNodes.length === 0) return false;
  var minX = Infinity, minY = Infinity, maxX = -Infinity, maxY = -Infinity;
  courseNodes.forEach(function(n) {{
    if (n.x < minX) minX = n.x;
    if (n.y < minY) minY = n.y;
    if (n.x + (n.w || 60) > maxX) maxX = n.x + (n.w || 60);
    if (n.y + (n.h || 20) > maxY) maxY = n.y + (n.h || 20);
  }});
  var pad = 80;
  var bw = maxX - minX + pad * 2;
  var bh = maxY - minY + pad * 2;
  camScale = Math.min(W / bw, H / bh) * 0.85;
  var cx = (minX + maxX) / 2;
  var cy = (minY + maxY) / 2;
  camX = W / 2 - cx * camScale;
  camY = H / 2 - cy * camScale;
  return true;
}}

if (location.hash) {{
  var courseId = location.hash.substring(1);
  panToCourse(courseId);
}}

window.addEventListener("resize", function() {{ resize(); resetView(); draw(); }});

function zoomBtn(f) {{
  var oldScale = camScale;
  camScale = Math.max(0.05, Math.min(20, camScale * f));
  var r = camScale / oldScale;
  camX = camX * r;
  camY = camY * r;
  draw();
}}

// Coordinate transforms
function screenToWorld(sx, sy) {{
  return {{
    x: (sx - W / 2 - camX) / camScale + W / 2,
    y: (sy - H / 2 - camY) / camScale + H / 2,
  }};
}}

// Helpers
function roundRect(x, y, w, h, r) {{
  ctx.beginPath();
  ctx.moveTo(x + r, y);
  ctx.lineTo(x + w - r, y);
  ctx.arcTo(x + w, y, x + w, y + r, r);
  ctx.lineTo(x + w, y + h - r);
  ctx.arcTo(x + w, y + h, x + w - r, y + h, r);
  ctx.lineTo(x + r, y + h);
  ctx.arcTo(x, y + h, x, y + h - r, r);
  ctx.lineTo(x, y + r);
  ctx.arcTo(x, y, x + r, y, r);
  ctx.closePath();
}}

// --- Drawing ---
var _rafId = 0;
function requestDraw() {{
  if (!_rafId) _rafId = requestAnimationFrame(function() {{ _rafId = 0; draw(); }});
}}
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

  // (Course separators removed — box colors convey course identity)

  // Viewport culling bounds (world coordinates)
  var vpLeft = (0 - W / 2 - camX) / camScale + W / 2;
  var vpRight = (W - W / 2 - camX) / camScale + W / 2;
  var vpTop = (0 - H / 2 - camY) / camScale + H / 2;
  var vpBottom = (H - H / 2 - camY) / camScale + H / 2;
  var vpPad = 100;

  // Edges (bezier curves from bottom of source to top of target)
  var skipSoft = camScale < 0.2;
  edgeData.forEach(function(e) {{
    if (skipSoft && e.type === "soft") return;
    // Cull edges fully outside viewport
    if (e.s.x < vpLeft - vpPad && e.t.x < vpLeft - vpPad) return;
    if (e.s.x > vpRight + vpPad && e.t.x > vpRight + vpPad) return;
    if (e.s.y < vpTop - vpPad && e.t.y < vpTop - vpPad) return;
    if (e.s.y > vpBottom + vpPad && e.t.y > vpBottom + vpPad) return;
    var sx = e.s.x, sy = e.s.y + e.s.h / 2;
    var tx = e.t.x, ty = e.t.y - e.t.h / 2;
    var midY = (sy + ty) / 2;
    ctx.beginPath();
    ctx.moveTo(sx, sy);
    ctx.bezierCurveTo(sx, midY, tx, midY, tx, ty);
    if (e.type === "soft") {{
      ctx.strokeStyle = "rgba(120,120,160,0.08)";
      ctx.setLineDash([4, 4]);
    }} else {{
      ctx.strokeStyle = "rgba(120,120,160,0.15)";
      ctx.setLineDash([]);
    }}
    ctx.lineWidth = 0.8;
    ctx.stroke();
    ctx.setLineDash([]);
  }});

  // Nodes (boxed labels)
  var showText = camScale > 0.25;
  data.nodes.forEach(function(n) {{
    // Viewport culling
    if (n.x + n.w / 2 < vpLeft - vpPad || n.x - n.w / 2 > vpRight + vpPad ||
        n.y + n.h / 2 < vpTop - vpPad || n.y - n.h / 2 > vpBottom + vpPad) return;
    var bx = n.x - n.w / 2, by = n.y - n.h / 2;
    roundRect(bx, by, n.w, n.h, 4);
    if (showFluency && effectiveScores) {{
      ctx.fillStyle = OKGFluency.masteryColor(effectiveScores[n.id] || 0);
    }} else {{
      ctx.fillStyle = n.color;
    }}
    ctx.fill();
    if (showFluency && frontierSet && frontierSet.has(n.id)) {{
      ctx.strokeStyle = "rgba(255,200,50,0.9)";
      ctx.lineWidth = 2;
    }} else {{
      ctx.strokeStyle = "rgba(255,255,255,0.12)";
      ctx.lineWidth = 0.5;
    }}
    ctx.stroke();

    // Label text — scale font to fit within box (no truncation)
    if (showText) {{
      var fs = n.fontSize;
      var maxW = n.w - 6;
      ctx.font = fs + "px sans-serif";
      // Shrink font if title exceeds box width
      var tw = ctx.measureText(n.title).width;
      if (tw > maxW && maxW > 0) {{
        fs = Math.max(5, Math.floor(fs * maxW / tw));
        ctx.font = fs + "px sans-serif";
      }}
      ctx.textAlign = "center";
      ctx.textBaseline = "middle";
      ctx.strokeStyle = "rgba(0,0,0,0.6)";
      ctx.lineWidth = 2.5;
      ctx.lineJoin = "round";
      ctx.strokeText(n.title, n.x, n.y);
      ctx.fillStyle = "#fff";
      ctx.fillText(n.title, n.x, n.y);
    }}

    // Cross-domain badge: small purple dot at top-right corner
    if (n.crossDomain > 0 && camScale > 0.15) {{
      var bdr = Math.max(3, Math.min(6, n.crossDomain / 10 + 3));
      ctx.beginPath();
      ctx.arc(n.x + n.w / 2 - 1, n.y - n.h / 2 + 1, bdr, 0, Math.PI * 2);
      ctx.fillStyle = "rgba(180,120,255,0.8)";
      ctx.fill();
      if (camScale > 0.5 && bdr >= 4) {{
        ctx.font = "bold " + Math.max(6, bdr) + "px sans-serif";
        ctx.textAlign = "center"; ctx.textBaseline = "middle";
        ctx.fillStyle = "#fff";
        ctx.fillText(n.crossDomain, n.x + n.w / 2 - 1, n.y - n.h / 2 + 1);
      }}
    }}
  }});

  // Highlight selected/hovered
  var ht = selectedNode || hoveredNode;
  if (ht) drawHighlight(ht);

  // Search highlights
  if (searchMatches.length > 0) {{
    searchMatches.forEach(function(n) {{
      var bx = n.x - n.w / 2 - 3, by = n.y - n.h / 2 - 3;
      roundRect(bx, by, n.w + 6, n.h + 6, 6);
      ctx.strokeStyle = "rgba(255,255,100,0.8)";
      ctx.lineWidth = 2;
      ctx.stroke();
    }});
    if (searchMatches.length <= 5) {{
      ctx.font = "bold 10px sans-serif";
      ctx.fillStyle = "#ff8";
      ctx.textAlign = "center";
      searchMatches.forEach(function(n) {{
        ctx.fillText(n.title, n.x, n.y - n.h / 2 - 8);
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

  // Highlight connected edges
  edgeData.forEach(function(ed) {{
    if (ed.s === node || ed.t === node) {{
      var sx = ed.s.x, sy = ed.s.y + ed.s.h / 2;
      var tx = ed.t.x, ty = ed.t.y - ed.t.h / 2;
      var midY = (sy + ty) / 2;
      ctx.beginPath();
      ctx.moveTo(sx, sy);
      ctx.bezierCurveTo(sx, midY, tx, midY, tx, ty);
      ctx.strokeStyle = ed.t === node
        ? "rgba(80,180,255,0.7)"
        : "rgba(255,160,80,0.7)";
      ctx.lineWidth = 2;
      ctx.stroke();
    }}
  }});

  // Opaque box covers base label cleanly
  var bx = node.x - node.w / 2, by = node.y - node.h / 2;
  roundRect(bx, by, node.w, node.h, 4);
  if (showFluency && effectiveScores) {{
    ctx.fillStyle = OKGFluency.masteryColor(effectiveScores[node.id] || 0);
  }} else {{
    ctx.fillStyle = node.color;
  }}
  ctx.fill();
  // White border (slightly larger)
  roundRect(bx - 2, by - 2, node.w + 4, node.h + 4, 5);
  ctx.strokeStyle = "#fff";
  ctx.lineWidth = 2;
  ctx.stroke();

  // Full title at larger font (can extend beyond box borders)
  ctx.font = "bold " + (node.fontSize + 2) + "px sans-serif";
  ctx.textAlign = "center";
  ctx.textBaseline = "middle";
  ctx.strokeStyle = "rgba(0,0,0,0.7)";
  ctx.lineWidth = 3;
  ctx.lineJoin = "round";
  ctx.strokeText(node.title, node.x, node.y);
  ctx.fillStyle = "#fff";
  ctx.fillText(node.title, node.x, node.y);

  ctx.restore();
}}

var hoveredNode = null;
draw();

// --- Hit testing (rectangle-based) ---
function hitTest(wx, wy) {{
  for (var i = data.nodes.length - 1; i >= 0; i--) {{
    var n = data.nodes[i];
    if (wx >= n.x - n.w / 2 && wx <= n.x + n.w / 2 &&
        wy >= n.y - n.h / 2 && wy <= n.y + n.h / 2) {{
      return n;
    }}
  }}
  return null;
}}

// --- Mouse interaction ---
var isDragging = false, dragStartX, dragStartY;
var dragMoved = false;
var mouseDownX = 0, mouseDownY = 0;
var lastTouchTime = 0;
var lastTapTime = 0, lastTapX = 0, lastTapY = 0;

canvas.addEventListener("mousemove", function(e) {{
  if (Date.now() - lastTouchTime < 500) return;
  if (isDragging) {{
    var dx = e.clientX - dragStartX;
    var dy = e.clientY - dragStartY;
    if (Math.abs(e.clientX - mouseDownX) > 3 || Math.abs(e.clientY - mouseDownY) > 3)
      dragMoved = true;
    camX += dx; camY += dy;
    dragStartX = e.clientX; dragStartY = e.clientY;
    requestDraw();
    tooltip.style.display = "none";
    return;
  }}

  var p = screenToWorld(e.clientX, e.clientY);
  var hit = hitTest(p.x, p.y);

  // Expand hit zone at low zoom
  if (!hit) {{
    var expand = Math.max(0, 8 / camScale);
    for (var i = data.nodes.length - 1; i >= 0; i--) {{
      var n = data.nodes[i];
      if (p.x >= n.x - n.w / 2 - expand && p.x <= n.x + n.w / 2 + expand &&
          p.y >= n.y - n.h / 2 - expand && p.y <= n.y + n.h / 2 + expand) {{
        hit = n; break;
      }}
    }}
  }}

  if (hit) {{
    if (hoveredNode !== hit) {{ hoveredNode = hit; draw(); }}
    var cl = hit.course ? hit.course.replace(/-/g, " ") : "";
    tooltip.innerHTML = '<h4>' + hit.title + '</h4><div class="meta">'
      + cl + ' &middot; ' + hit.degree + ' connections' + (hit.crossDomain ? ' (+' + hit.crossDomain + ' cross-domain)' : '')
      + ' &middot; Depth ' + hit.depth + '</div>';
    tooltip.style.display = "block";
    tooltip.style.left = (e.clientX + 14) + "px";
    tooltip.style.top = (e.clientY - 8) + "px";
    canvas.style.cursor = "pointer";
  }} else {{
    if (hoveredNode) {{ hoveredNode = null; draw(); }}
    tooltip.style.display = "none";
    canvas.style.cursor = "default";
  }}
}});

canvas.addEventListener("mousedown", function(e) {{
  if (Date.now() - lastTouchTime < 500) return;
  isDragging = true; dragMoved = false;
  dragStartX = e.clientX; dragStartY = e.clientY;
  mouseDownX = e.clientX; mouseDownY = e.clientY;
  canvas.style.cursor = "grabbing";
}});

canvas.addEventListener("mouseup", function(e) {{
  if (Date.now() - lastTouchTime < 500) return;
  isDragging = false;
  canvas.style.cursor = "default";
  if (!dragMoved && hoveredNode) {{
    showPanel(hoveredNode, e.clientX, e.clientY);
  }} else if (!dragMoved) {{
    hidePanel();
  }}
}});

canvas.addEventListener("wheel", function(e) {{
  e.preventDefault();
  var factor = e.deltaY > 0 ? 0.9 : 1.1;
  var oldScale = camScale;
  camScale = Math.max(0.05, Math.min(20, camScale * factor));
  var r = camScale / oldScale;
  camX = camX * r + (e.clientX - W / 2) * (1 - r);
  camY = camY * r + (e.clientY - H / 2) * (1 - r);
  requestDraw();
}}, {{ passive: false }});

// --- Panel ---
function showPanel(node, sx, sy) {{
  selectedNode = node;
  draw();
  var prereqs = edgeData.filter(function(e) {{ return e.t === node; }});
  var successors = edgeData.filter(function(e) {{ return e.s === node; }});
  var cl = node.course ? node.course.replace(/-/g, " ") : "";
  var html = '<button class="panel-close" onclick="hidePanel()">&times;</button>';
  html += '<h3><a href="topics/' + node.id + '.html" target="_blank">' + node.title + '</a></h3>';
  html += '<div class="panel-meta">' + cl + ' &middot; ' + node.degree + ' connections' + (node.crossDomain ? ' (+' + node.crossDomain + ' cross-domain)' : '') + ' &middot; depth ' + node.depth + '</div>';
  if (prereqs.length > 0) {{
    html += '<div class="panel-section"><h4>Prerequisites (' + prereqs.length + ')</h4>';
    prereqs.forEach(function(e) {{
      html += '<div class="panel-item" data-id="' + e.s.id + '">'
        + '<span class="panel-dot" style="background:' + e.s.color + '"></span>'
        + '<span class="panel-title">' + e.s.title + '</span>'
        + '<span class="panel-badge ' + e.type + '">' + e.type + '</span></div>';
    }});
    html += '</div>';
  }}
  if (successors.length > 0) {{
    html += '<div class="panel-section"><h4>Successors (' + successors.length + ')</h4>';
    successors.forEach(function(e) {{
      html += '<div class="panel-item" data-id="' + e.t.id + '">'
        + '<span class="panel-dot" style="background:' + e.t.color + '"></span>'
        + '<span class="panel-title">' + e.t.title + '</span>'
        + '<span class="panel-badge ' + e.type + '">' + e.type + '</span></div>';
    }});
    html += '</div>';
  }}
  if (prereqs.length === 0 && successors.length === 0) {{
    html += '<div class="panel-section" style="color:#666;">No connections</div>';
  }}
  panel.innerHTML = html;
  panel.style.display = "block";
  if (W > 768) {{
    var px = sx + 20, py = sy - 20;
    if (px + 390 > W) px = sx - 400;
    if (py + 300 > H) py = H - 320;
    if (py < 10) py = 10;
    if (px < 10) px = 10;
    panel.style.left = px + "px";
    panel.style.top = py + "px";
  }}
  panel.querySelectorAll(".panel-item").forEach(function(el) {{
    el.addEventListener("click", function() {{
      var tid = el.getAttribute("data-id");
      var target = nodeMap[tid];
      if (target) showPanel(target, parseInt(panel.style.left), parseInt(panel.style.top));
    }});
  }});
}}

function hidePanel() {{
  panel.style.display = "none";
  selectedNode = null;
  draw();
}}

// --- Touch support ---
document.addEventListener("touchmove", function(e) {{
  if (!e.target.closest("#legend, #panel")) e.preventDefault();
}}, {{ passive: false }});

var lastPinchDist = 0;
var lastTouchX = 0, lastTouchY = 0;
var touchStartX = 0, touchStartY = 0;

function touchDist(t) {{
  return Math.hypot(t[0].clientX - t[1].clientX, t[0].clientY - t[1].clientY);
}}
function touchCenter(t) {{
  return {{ x: (t[0].clientX + t[1].clientX) / 2, y: (t[0].clientY + t[1].clientY) / 2 }};
}}

canvas.addEventListener("touchstart", function(e) {{
  e.preventDefault();
  if (e.touches.length === 1) {{
    lastTouchX = e.touches[0].clientX; lastTouchY = e.touches[0].clientY;
    touchStartX = lastTouchX; touchStartY = lastTouchY;
    isDragging = true; dragMoved = false;
  }} else if (e.touches.length === 2) {{
    lastPinchDist = touchDist(e.touches);
    var c = touchCenter(e.touches);
    lastTouchX = c.x; lastTouchY = c.y;
    dragMoved = true;
  }}
  tooltip.style.display = "none";
}}, {{ passive: false }});

canvas.addEventListener("touchmove", function(e) {{
  e.preventDefault();
  if (e.touches.length === 1 && isDragging) {{
    var dx = e.touches[0].clientX - lastTouchX;
    var dy = e.touches[0].clientY - lastTouchY;
    camX += dx; camY += dy;
    lastTouchX = e.touches[0].clientX; lastTouchY = e.touches[0].clientY;
    if (Math.hypot(e.touches[0].clientX - touchStartX, e.touches[0].clientY - touchStartY) > 15)
      dragMoved = true;
    requestDraw();
  }} else if (e.touches.length === 2) {{
    var dist = touchDist(e.touches);
    var c = touchCenter(e.touches);
    if (lastPinchDist > 0) {{
      var factor = dist / lastPinchDist;
      var oldScale = camScale;
      camScale = Math.max(0.05, Math.min(20, camScale * factor));
      var r = camScale / oldScale;
      camX = camX * r + (c.x - W / 2) * (1 - r);
      camY = camY * r + (c.y - H / 2) * (1 - r);
    }}
    camX += c.x - lastTouchX; camY += c.y - lastTouchY;
    lastPinchDist = dist;
    lastTouchX = c.x; lastTouchY = c.y;
    dragMoved = true;
    requestDraw();
  }}
}}, {{ passive: false }});

canvas.addEventListener("touchend", function(e) {{
  e.preventDefault();
  lastTouchTime = Date.now();
  if (e.touches.length === 0) {{
    isDragging = false; lastPinchDist = 0;
    if (!dragMoved) {{
      // Double-tap to zoom
      var now = Date.now();
      if (now - lastTapTime < 300 && Math.hypot(lastTouchX - lastTapX, lastTouchY - lastTapY) < 30) {{
        var oldScale = camScale;
        camScale = Math.min(20, camScale * 2.5);
        var r = camScale / oldScale;
        camX = camX * r + (lastTouchX - W / 2) * (1 - r);
        camY = camY * r + (lastTouchY - H / 2) * (1 - r);
        lastTapTime = 0;
        hidePanel();
        draw();
      }} else {{
        lastTapTime = now;
        lastTapX = lastTouchX; lastTapY = lastTouchY;
        // Tap — hit detection with expanded touch targets
        var p = screenToWorld(lastTouchX, lastTouchY);
        var hit = hitTest(p.x, p.y);
        if (!hit) {{
          var expand = Math.max(12, 12 / camScale);
          for (var i = data.nodes.length - 1; i >= 0; i--) {{
            var n = data.nodes[i];
            if (p.x >= n.x - n.w / 2 - expand && p.x <= n.x + n.w / 2 + expand &&
                p.y >= n.y - n.h / 2 - expand && p.y <= n.y + n.h / 2 + expand) {{
              hit = n; break;
            }}
          }}
        }}
        if (hit) {{
          hoveredNode = hit; draw();
          showPanel(hit, lastTouchX, lastTouchY);
        }} else {{
          hoveredNode = null; draw(); hidePanel();
        }}
      }}
    }}
  }} else if (e.touches.length === 1) {{
    lastTouchX = e.touches[0].clientX; lastTouchY = e.touches[0].clientY;
    lastPinchDist = 0;
  }}
}}, {{ passive: false }});

// --- Search ---
var searchInput = document.getElementById("searchInput");
var searchCount = document.getElementById("searchCount");

searchInput.addEventListener("input", function() {{
  var q = searchInput.value.trim().toLowerCase();
  if (q.length < 2) {{
    searchMatches = []; searchCount.textContent = "";
    hidePanel(); draw(); return;
  }}
  searchMatches = data.nodes.filter(function(n) {{
    return n.title.toLowerCase().indexOf(q) >= 0
      || n.id.toLowerCase().indexOf(q) >= 0
      || n.course.toLowerCase().indexOf(q) >= 0
      || (n.tags && n.tags.some(function(t) {{ return t.indexOf(q) >= 0; }}));
  }});
  searchCount.textContent = searchMatches.length + " match"
    + (searchMatches.length !== 1 ? "es" : "");
  if (searchMatches.length >= 1 && searchMatches.length <= 20) {{
    // Pan/zoom to show all matches
    var minX = Infinity, minY = Infinity, maxX = -Infinity, maxY = -Infinity;
    searchMatches.forEach(function(n) {{
      if (n.x - n.w/2 < minX) minX = n.x - n.w/2;
      if (n.y - n.h/2 < minY) minY = n.y - n.h/2;
      if (n.x + n.w/2 > maxX) maxX = n.x + n.w/2;
      if (n.y + n.h/2 > maxY) maxY = n.y + n.h/2;
    }});
    var pad = 100;
    var bw = maxX - minX + pad * 2;
    var bh = maxY - minY + pad * 2;
    camScale = Math.min(W / bw, H / bh) * 0.85;
    camScale = Math.max(0.05, Math.min(20, camScale));
    var cx = (minX + maxX) / 2;
    var cy = (minY + maxY) / 2;
    camX = W / 2 - cx * camScale;
    camY = H / 2 - cy * camScale;
  }}
  if (searchMatches.length === 1) {{
    selectedNode = searchMatches[0]; hoveredNode = searchMatches[0];
    showPanel(searchMatches[0], W / 2, H / 2);
  }} else {{
    selectedNode = null; hidePanel();
  }}
  draw();
}});

document.addEventListener("keydown", function(e) {{
  if ((e.ctrlKey || e.metaKey) && e.key === "f") {{
    e.preventDefault(); searchInput.focus(); searchInput.select();
  }}
  if (e.key === "Escape") {{
    hidePanel(); searchInput.value = "";
    searchMatches = []; searchCount.textContent = "";
    searchInput.blur(); draw();
  }}
}});

// Touch device: update help text and search placeholder
if ("ontouchstart" in window || navigator.maxTouchPoints > 0) {{
  var ht = document.getElementById("helpText");
  if (ht) ht.textContent = "Pinch to zoom \u00b7 Drag to pan \u00b7 Tap for details \u00b7 Double-tap to zoom in";
  searchInput.placeholder = "Search topics...";
}}
</script>
</body>
</html>"""


# ---------------------------------------------------------------------------
# Entry points
# ---------------------------------------------------------------------------

def generate_course_map(domain, course_id):
    """Generate knowledge map for a single course."""
    nodes, edges, config = load_domain(domain, course_filter=course_id)
    if not nodes:
        return None, {}

    course_ids = config["course_ids"]
    course_titles = config["course_titles"]
    course_title = course_titles.get(course_id, smart_title(course_id))

    conn = compute_connectivity(nodes, edges)
    box_dims = estimate_box_dims(nodes, conn)
    depth_map = compute_depth(nodes, edges)
    positions, cw, ch = compute_layered_layout(
        nodes, edges, depth_map, box_dims, get_branch_x(course_ids))

    colors = generate_course_colors(len(course_ids))
    title = f"{course_title} \u2014 Knowledge Map"
    html = generate_html(
        domain, title, nodes, edges, positions, box_dims, cw, ch,
        depth_map, course_ids, colors, course_titles,
        is_course_map=True)

    out = OUTPUT_DIR / f"{domain}-{course_id}-map.html"
    out.write_text(html, encoding="utf-8")

    n_edges = len([e for e in edges
                   if e["source"] in positions and e["target"] in positions])
    max_d = max(depth_map.values()) if depth_map else 0
    return out, {
        "topics": len(nodes), "edges": n_edges,
        "max_depth": max_d, "canvas": f"{cw}x{ch}",
    }


def generate_domain_map(domain):
    """Generate knowledge map for full domain (courses stacked top-to-bottom)."""
    nodes, edges, config = load_domain(domain)
    if not nodes:
        return None, {}

    course_ids = config["course_ids"]
    course_titles = config["course_titles"]
    domain_title = config["title"]

    conn = compute_connectivity(nodes, edges)
    # Add cross-domain edges to connectivity for proper sizing
    print("  Counting cross-domain edges for sizing...")
    cross_counts = count_cross_domain_edges(set(nodes.keys()))
    for nid in conn:
        conn[nid] += cross_counts.get(nid, 0)
    box_dims = estimate_box_dims(nodes, conn)
    course_stages = config.get("course_stages", {})

    # Tier-based layout (from dialectic review):
    # Group courses by developmental stage → tiers.
    # Within each tier, courses overlap ~50% vertically (side-by-side).
    # Between tiers, ~25% overlap. Barycenter handles X ordering.
    # This naturally groups similarly-complex courses (e.g., LinAlg, MV Calc,
    # Methods of Proof, Prob&Stats are all formal-systems).
    WITHIN_OVERLAP = 0.5   # courses in same tier share this much Y-space
    BETWEEN_OVERLAP = 0.25  # bleed between adjacent tiers

    within_depth, course_max = compute_course_depths(nodes, edges, course_ids)

    # Build tiers from stage metadata
    stage_order = ["pre-formal", "concrete-operations", "abstract-reasoning",
                   "formal-systems", "advanced", "expert"]
    tiers = []
    for stage in stage_order:
        tier_courses = [c for c in course_ids
                        if course_stages.get(c, "abstract-reasoning") == stage]
        if tier_courses:
            tiers.append((stage, tier_courses))

    # Compute course Y-starts
    course_y_start = {}
    y = 0
    for stage, tier_courses in tiers:
        tier_span = max(course_max.get(c, 0) + 1 for c in tier_courses)
        n = len(tier_courses)
        # Minimum stagger: at least 50% of average course span between starts,
        # but capped so tiers with many courses don't over-expand.
        avg_span = sum(course_max.get(c, 0) + 1 for c in tier_courses) / max(n, 1)
        min_total = avg_span * 0.5 * max(n - 1, 1)
        natural = tier_span * (1 - WITHIN_OVERLAP)
        stagger_range = max(natural, min(min_total, tier_span * 1.5))

        for i, cid in enumerate(tier_courses):
            stagger = stagger_range * i / max(n - 1, 1) if n > 1 else 0
            course_y_start[cid] = int(y + stagger)

        eff_height = tier_span + (stagger_range * (n - 1) / n if n > 1 else 0)
        y += eff_height * (1 - BETWEEN_OVERLAP)

    # Topic depth = course start + within-course depth
    depth_map = {}
    for nid, node in nodes.items():
        cid = node["course"]
        depth_map[nid] = course_y_start.get(cid, 0) + within_depth.get(nid, 0)

    # Row splitting: double depths to create sub-layer slots, then
    # recursively split wide layers until no layer exceeds ~1.5x median.
    for nid in depth_map:
        depth_map[nid] *= 3
    split_n = 0
    for _pass in range(3):  # up to 3 rounds of splitting
        lc = defaultdict(list)
        for nid in depth_map:
            lc[depth_map[nid]].append(nid)
        sizes = sorted(len(v) for v in lc.values())
        med = sizes[len(sizes) // 2] if sizes else 10
        threshold = max(int(med * 1.5), 8)
        threshold = min(threshold, 20)  # absolute max row width
        did_split = False
        for d in sorted(lc.keys()):
            nids = lc[d]
            if len(nids) > threshold:
                nids.sort(key=lambda n: box_dims[n]["degree"], reverse=True)
                for nid in nids[len(nids) // 2:]:
                    depth_map[nid] += 1
                split_n += 1
                did_split = True
        if not did_split:
            break

    max_depth = max(depth_map.values()) if depth_map else 0
    print(f"  Tier layout: {len(tiers)} tiers, {max_depth} layers "
          f"({split_n} rows split), {len(nodes)} nodes...")
    positions, cw, ch = compute_layered_layout(
        nodes, edges, depth_map, box_dims, get_branch_x(course_ids))

    colors = generate_course_colors(len(course_ids))

    title = f"Knowledge Map \u2014 {domain_title}"
    html = generate_html(
        domain, title, nodes, edges, positions, box_dims, cw, ch,
        depth_map, course_ids, colors, course_titles,
        is_course_map=False, cross_counts=cross_counts)

    out = OUTPUT_DIR / f"{domain}-map.html"
    out.write_text(html, encoding="utf-8")

    n_edges = len([e for e in edges
                   if e["source"] in positions and e["target"] in positions])
    max_d = max(depth_map.values()) if depth_map else 0
    return out, {
        "topics": len(nodes), "edges": n_edges,
        "courses": len(course_ids), "max_depth": max_d,
        "canvas": f"{cw}x{ch}",
    }


def main():
    parser = argparse.ArgumentParser(
        description="Generate knowledge maps with boxed labels")
    parser.add_argument("--domain", help="Domain name")
    parser.add_argument("--course", help="Single course within domain")
    parser.add_argument("--all-courses", action="store_true",
                        help="Generate maps for all courses in a domain")
    parser.add_argument("--all", action="store_true",
                        help="Generate domain maps for all domains")
    args = parser.parse_args()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    if args.all:
        count = 0
        for d in sorted(DOMAINS_DIR.iterdir()):
            if d.is_dir() and (d / "_domain.yml").exists():
                print(f"Generating {d.name} domain map...")
                out, stats = generate_domain_map(d.name)
                if out:
                    print(f"  {stats['topics']} topics, {stats['edges']} edges, "
                          f"depth {stats['max_depth']}, {stats['canvas']}")
                    count += 1
        print(f"\nDone! {count} domain maps generated.")

    elif args.domain and args.all_courses:
        nodes, _, config = load_domain(args.domain)
        cids = config["course_ids"]
        count = 0
        for cid in cids:
            print(f"Generating {args.domain}/{cid}...")
            out, stats = generate_course_map(args.domain, cid)
            if out:
                print(f"  {stats['topics']} topics, {stats['edges']} edges, "
                      f"depth {stats['max_depth']}, {stats['canvas']}")
                count += 1
        print(f"\nDone! {count} course maps generated.")

    elif args.domain and args.course:
        print(f"Generating {args.domain}/{args.course}...")
        out, stats = generate_course_map(args.domain, args.course)
        if out:
            print(f"  {stats['topics']} topics, {stats['edges']} edges, "
                  f"depth {stats['max_depth']}, canvas {stats['canvas']}")
            print(f"Saved: {out}")
        else:
            print("No topics found.")
            sys.exit(1)

    elif args.domain:
        print(f"Generating {args.domain} domain map...")
        out, stats = generate_domain_map(args.domain)
        if out:
            print(f"  {stats['topics']} topics, {stats['edges']} edges, "
                  f"depth {stats['max_depth']}, canvas {stats['canvas']}")
            print(f"Saved: {out}")
        else:
            print("No topics found.")
            sys.exit(1)

    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
