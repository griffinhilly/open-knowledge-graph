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

# Import branch X-positions from domain map tool
sys.path.insert(0, str(ROOT / "tools"))
from visualize_domain_map import COURSE_BRANCH_X

# --- Developmental stage → radial band mapping ---
# Maps the stage field to approximate age ranges and radial bands.
# Inner = youngest, outer = most advanced.
STAGE_BANDS = {
    "pre-formal":          (0.06, 0.18),   # ages ~2-5, preschool-K
    "concrete-operations": (0.14, 0.32),   # ages ~5-10, elementary
    "abstract-reasoning":  (0.28, 0.48),   # ages ~10-15, middle school
    "formal-systems":      (0.44, 0.68),   # ages ~15-22, HS through undergrad
    "advanced":            (0.64, 0.85),   # ages ~18-22+, upper-division
    "expert":              (0.82, 1.00),   # ages ~22+, graduate/research
}
DEFAULT_STAGE = "abstract-reasoning"
# Integer indices 0-5, consumed by fluency.js cold-start prior + alpha gradient.
STAGE_INDEX = {s: i for i, s in enumerate(STAGE_BANDS.keys())}

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
    "history",
    "language-and-communication",
    "literature",
    "arts-and-aesthetics",
    "music",
]

# Domain hue assignments (HSL degrees) — stride-8 permutation of 19
# evenly-spaced hues. Adjacent domains are ~152° apart. No warm/cool
# cluster even when topics drift across sector boundaries.
DOMAIN_HUES = {
    "mathematics":                   5,  # red
    "formal-sciences-and-logic":   157,  # green-teal
    "philosophy":                  309,  # magenta
    "computer-science":            100,  # lime-green
    "engineering":                 252,  # blue-violet
    "physics":                      43,  # amber
    "earth-and-space-sciences":    195,  # cyan
    "chemistry":                   347,  # red-pink
    "biology":                     138,  # green
    "health-and-human-development":290,  # purple
    "psychology":                   81,  # yellow-green
    "social-sciences":             233,  # blue
    "economics":                    24,  # orange
    "practical-life-skills":       176,  # teal-cyan
    "history":                     328,  # pink-magenta
    "language-and-communication":  119,  # green-lime
    "literature":                  271,  # violet
    "arts-and-aesthetics":          62,  # yellow
    "music":                       214,  # sky-blue
    "developmental-origins":        45,  # gold — origin-layer capacities (only with --with-origins)
}


from parse_topic import parse_frontmatter, parse_topic, parse_sections, seo_meta_tags

# --- Sprout shell (Phase 12B Cut 7) ---
# Single emoji per pre-formal domain. HERO_IMAGE_RETROFIT: replace with per-topic
# hero images once Persona A testers are available (see plans/phase-12-three-persona-redesign.md).
SPROUT_DOMAIN_EMOJI = {
    "arts-and-aesthetics":          "🎨",
    "biology":                      "🌱",
    "earth-and-space-sciences":     "🌍",
    "health-and-human-development": "💪",
    "language-and-communication":   "💬",
    "literature":                   "📖",
    "mathematics":                  "🔢",
    "music":                        "🎵",
    "psychology":                   "💙",
}


def load_sprout_topics():
    """Collect pre-formal topics with a short Core Idea snippet for SproutCard.

    Only domains in SPROUT_DOMAIN_EMOJI are included (the 9 domains with
    genuine pre-formal content). Core Idea is stripped of markdown and
    trimmed to ~280 chars — small enough to keep the inline JSON cheap
    and short enough for a 5-year-old's attention span.
    """
    topics = []
    for filepath in sorted(DOMAINS_DIR.rglob("*.md")):
        data, body = parse_topic(filepath)
        if not data or data.get("stage") != "pre-formal":
            continue
        domain = data.get("domain", "")
        if domain not in SPROUT_DOMAIN_EMOJI:
            continue
        sections = parse_sections(body)
        core = sections.get("Core Idea", "")
        core = re.sub(r"[*_`#>]", "", core)
        core = re.sub(r"\s+", " ", core).strip()
        if len(core) > 280:
            core = core[:277].rsplit(" ", 1)[0] + "..."
        topics.append({
            "id": data["id"],
            "title": data.get("title", data["id"]),
            "domain": domain,
            "emoji": SPROUT_DOMAIN_EMOJI[domain],
            "coreIdea": core,
        })
    return topics


def load_all_topics(include_caps=False):
    all_data = {}
    for filepath in sorted(DOMAINS_DIR.rglob("*.md")):
        data = parse_frontmatter(filepath)
        if data and "id" in data:
            if data.get("kind") == "capacity" and not include_caps:
                continue  # origin layer: not shown in the public radial (only with --with-origins)
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
                "pedagogy_type": data.get("pedagogy_type", "assessable"),
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


def compute_domain_local_depths(all_data):
    """Compute topological depth using only within-domain edges.

    Domain roots (topics with no same-domain prereqs) get depth 0 regardless
    of cross-domain prerequisites. This ensures foundational topics within
    each domain cluster near the center of the radial graph.
    """
    children_of = defaultdict(list)
    in_degree = defaultdict(int)

    for tid, data in all_data.items():
        domain = data.get("domain", "")
        for p in data.get("prerequisites", []):
            if isinstance(p, dict) and "id" in p:
                pid = p["id"]
                if pid in all_data and all_data[pid].get("domain", "") == domain:
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


def get_branch_x(course_id, domain_courses):
    """Get the branch X-position for a course (0.0-1.0).

    Uses COURSE_BRANCH_X mapping from domain maps where available,
    falls back to uniform spacing based on course order.
    """
    if course_id in COURSE_BRANCH_X:
        return COURSE_BRANCH_X[course_id]
    # Fallback: uniform spacing based on position in course list
    if course_id in domain_courses:
        idx = domain_courses.index(course_id)
        return (idx + 0.5) / max(len(domain_courses), 1)
    return 0.5


def compute_branch_flips(all_data, domain_order, sectors, configs):
    """Auto-detect branch flip per domain by minimizing cross-domain edge lengths.

    For each domain, tests both flip=False and flip=True. Measures total
    Euclidean distance of cross-domain edges to domains within 3 angular
    positions in either direction. Picks the flip that produces shorter edges.
    """
    n_domains = len(domain_order)
    domain_idx = {d: i for i, d in enumerate(domain_order)}

    # Build cross-domain edge list: (domain_a, course_a, domain_b, course_b)
    cross_edges = []
    for tid, data in all_data.items():
        domain_a = data.get("domain", "")
        course_a = data.get("course", "")
        if domain_a not in domain_idx:
            continue
        for p in data.get("prerequisites", []):
            if not isinstance(p, dict):
                continue
            pid = p.get("id")
            if pid and pid in all_data:
                pdata = all_data[pid]
                domain_b = pdata.get("domain", "")
                course_b = pdata.get("course", "")
                if domain_b != domain_a and domain_b in domain_idx:
                    cross_edges.append((domain_a, course_a, domain_b, course_b))

    flips = {}
    for domain in domain_order:
        di = domain_idx[domain]
        sector = sectors[domain]
        sector_width = sector["end"] - sector["start"]
        course_ids = [c["id"] for c in configs.get(domain, {}).get("courses", [])]

        # Find nearby domains (within 3 angular positions, wrapping)
        nearby = set()
        for offset in range(-3, 4):
            if offset == 0:
                continue
            ni = (di + offset) % n_domains
            nearby.add(domain_order[ni])

        # Filter edges: this domain ↔ nearby domains
        relevant_edges = [
            (da, ca, db, cb) for da, ca, db, cb in cross_edges
            if (da == domain and db in nearby) or (db == domain and da in nearby)
        ]

        if not relevant_edges:
            flips[domain] = False
            continue

        # Test both flips
        best_flip = False
        best_dist = float("inf")

        for flip in (False, True):
            total_dist = 0.0
            for da, ca, db, cb in relevant_edges:
                # Get angular position for topic in domain being tested
                if da == domain:
                    bx = get_branch_x(ca, course_ids)
                    if flip:
                        bx = 1.0 - bx
                    angle_a = sector["start"] + sector_width * bx
                    # Other domain uses its sector midpoint (we don't know its flip yet)
                    angle_b = sectors[db]["mid"]
                else:
                    bx = get_branch_x(cb, course_ids)
                    if flip:
                        bx = 1.0 - bx
                    angle_b = sector["start"] + sector_width * bx
                    angle_a = sectors[da]["mid"]

                # Angular distance (shortest arc)
                delta = abs(angle_a - angle_b)
                if delta > math.pi:
                    delta = 2 * math.pi - delta
                total_dist += delta

            if total_dist < best_dist:
                best_dist = total_dist
                best_flip = flip

        flips[domain] = best_flip

    return flips


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

    # Compute branch flips (auto-detected from cross-domain edge lengths)
    branch_flips = compute_branch_flips(all_data, domain_order, sectors, configs)
    print("  Branch flips (True = reversed):")
    for d in domain_order:
        print(f"    {d}: {'FLIP' if branch_flips[d] else 'normal'}")

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

        # Angular: use domain map branch X-positions for semantic sub-placement
        sector = sectors[domain]
        course_ids = [c["id"] for c in configs.get(domain, {}).get("courses", [])]
        sector_width = sector["end"] - sector["start"]

        # Get branch X (0.0-1.0) and apply flip
        bx = get_branch_x(course, course_ids)
        if branch_flips.get(domain, False):
            bx = 1.0 - bx

        # Map branch X to angle within sector (with small margin to avoid edges)
        margin = sector_width * 0.05
        base_angle = sector["start"] + margin + bx * (sector_width - 2 * margin)

        # Jitter for organic feel (scaled to course density)
        n_courses = max(len(course_ids), 1)
        angle_jitter = (random.random() - 0.5) * sector_width / n_courses * 0.3
        radial_jitter = (random.random() - 0.5) * (band_max - band_min) * max_radius * 0.05

        theta = base_angle + angle_jitter
        r = max(20, r + radial_jitter)

        x = r * math.cos(theta)
        y = r * math.sin(theta)

        positions[tid] = {
            "x": x, "y": y,
            "r": r, "theta": theta,
            "target_r": r,  # For radial spring-back
            "target_theta": base_angle,  # For angular spring-back (branch X position)
            "stage": stage,
        }

    # --with-origins: seed capacity nodes as a CENTRAL HUB — a tiny ring at the origin spread by angle,
    # NOT a domain wedge. target_r pins them to the center through the radial spring-back below, so the
    # 10 capacities stay clustered at r~18 while their edges fan out to every domain. (private variant)
    cap_present = sorted(tid for tid, d in all_data.items() if d.get("kind") == "capacity")
    HUB = "discernment-same-different"  # the root operation (every topic depends on it) sits dead-center
    ring = [c for c in cap_present if c != HUB]
    for i, tid in enumerate(ring):
        theta = (i / max(1, len(ring))) * 2 * math.pi
        rr = 24.0
        positions[tid] = {"x": rr * math.cos(theta), "y": rr * math.sin(theta),
                          "r": rr, "theta": theta, "target_r": rr,
                          "target_theta": theta, "stage": "proto-formal"}
    if HUB in cap_present:
        positions[HUB] = {"x": 0.001, "y": 0.0, "r": 0.0, "theta": 0.0,
                          "target_r": 0.0, "target_theta": 0.0, "stage": "proto-formal"}

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
        stage_name = data.get("stage", "") or DEFAULT_STAGE
        pedagogy_type = configs.get(domain, {}).get("pedagogy_type", "assessable")
        nodes.append({
            "id": tid,
            "title": data.get("title", tid),
            "domain": domain,
            "course": course,
            "stage": stage_name,
            "stageInt": STAGE_INDEX.get(stage_name, STAGE_INDEX[DEFAULT_STAGE]),
            "pedagogyType": pedagogy_type,
            "depth": depths.get(tid, 0),
            "kind": data.get("kind", "topic"),
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
            "abstract-reasoning": "Middle School",
            "formal-systems": "High School — Undergrad",
            "advanced": "Upper-Division",
            "expert": "Graduate / Research",
        }
        stage_rings.append({
            "label": label_map.get(stage, stage),
            "inner": round(band_min * 500, 1),
            "outer": round(band_max * 500, 1),
            "mid": round((band_min + band_max) / 2 * 500, 1),
        })

    sprout_topics = load_sprout_topics()

    graph_json = json.dumps({
        "nodes": nodes,
        "edges": edges,
        "sectors": sector_data,
        "stageRings": stage_rings,
        "maxDepth": max_depth,
        "sproutTopics": sprout_topics,
    })

    title = "Open Knowledge Graph"
    n_topics = len(nodes)
    n_edges = len(edges)
    n_domains = len(sector_data)

    # 19-row refine-your-map slider domain list (all 19, including practical-life-skills)
    refine_domains = []
    for d in DOMAIN_HUES.keys():
        label = configs.get(d, {}).get("title", d.replace("-", " ").title())
        refine_domains.append([d, label])
    refine_domains_json = json.dumps(refine_domains)

    radial_seo_block = seo_meta_tags(
        "Knowledge Map — Open Knowledge Graph",
        f"Interactive radial map of {n_topics:,} topics across {n_domains} domains, "
        "arranged from early childhood at the center to graduate research at the edge. "
        "Zoom in, search any topic, and trace its prerequisites.",
        "radial-graph.html")

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
<title>{title}</title>
{radial_seo_block}
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
#panel .panel-path {{
  margin-top:14px; padding-top:12px; border-top:1px solid #262636;
  display:flex; gap:8px;
}}
#panel .panel-path button {{
  background:#16223a; border:1px solid #2a3a55; border-radius:6px;
  padding:7px 10px; font-size:12px; color:#9cd; cursor:pointer;
}}
#panel .panel-path button:hover {{ background:#20304e; color:#cef; }}
#panel .panel-path .path-btn[data-act="ancestry"] {{ flex:1; }}
#panel .panel-path .copy {{ flex:0 0 auto; }}
#pathBanner {{
  position:fixed; top:16px; left:50%; transform:translateX(-50%);
  display:none; align-items:center; gap:12px;
  background:rgba(10,14,24,0.95); border:1px solid #2a3a55;
  border-radius:999px; padding:8px 16px; z-index:40;
  font-size:13px; color:#cde; max-width:92vw;
  box-shadow:0 4px 20px rgba(0,0,0,0.45);
}}
#pathBanner span {{ overflow:hidden; text-overflow:ellipsis; white-space:nowrap; }}
#pathBanner strong {{ color:#fff; }}
#pathBanner button {{
  flex:0 0 auto; background:none; border:1px solid #3a4a66;
  border-radius:6px; padding:4px 10px; font-size:12px; color:#9cd; cursor:pointer;
}}
#pathBanner button:hover {{ background:#20304e; color:#cef; }}
#pathBanner .pb-clear {{ color:#c99; border-color:#553; }}
#panel .panel-correction {{
  margin-top:14px; padding-top:12px; border-top:1px solid #262636;
  display:flex; gap:8px;
}}
#panel .panel-correction button {{
  flex:1; background:#1a2538; border:1px solid #2a3a55; border-radius:6px;
  padding:7px 10px; font-size:12px; color:#9cd; cursor:pointer;
}}
#panel .panel-correction button:hover {{ background:#24324a; color:#cef; }}
#panel .panel-correction .dontknow {{ background:rgba(220,80,80,0.08); border-color:rgba(220,80,80,0.3); color:#e99; }}
#panel .panel-correction .dontknow:hover {{ background:rgba(220,80,80,0.15); color:#fcc; }}
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
#controls button.active {{ background:#2a4a2a; border-color:#4a4; color:#8f8; }}
#stageCard {{
  position:fixed; top:50%; left:50%; transform:translate(-50%,-50%);
  background:rgba(18,18,28,0.97); border:1px solid #333;
  border-radius:12px; padding:22px 26px 18px; z-index:40;
  width:min(420px, calc(100vw - 32px));
  box-shadow:0 16px 48px rgba(0,0,0,0.5);
}}
#stageCard.stage-hidden {{ display:none; }}
#stageCard .stage-close {{
  position:absolute; top:6px; right:10px;
  background:none; border:none; color:#888; font-size:22px;
  cursor:pointer; padding:4px 8px; line-height:1;
}}
#stageCard .stage-close:hover {{ color:#eee; }}
#stageCard h3 {{ font-size:17px; color:#eee; margin-bottom:4px; padding-right:24px; }}
#stageCard .stage-sub {{ font-size:12px; color:#778; margin-bottom:20px; }}
#stageCard .stage-label {{
  text-align:center; margin-bottom:12px;
  font-size:15px; color:#9cd; font-weight:600; min-height:1.2em;
}}
#stageCard input[type=range] {{
  width:100%; accent-color:#6ab; cursor:pointer;
}}
#stageCard .stage-ticks {{
  display:flex; justify-content:space-between;
  margin-top:10px; font-size:9px; color:#556; letter-spacing:0.2px;
}}
#stageCard .stage-ticks span {{ flex:1; text-align:center; }}
#stageCard .stage-ticks span:first-child {{ text-align:left; }}
#stageCard .stage-ticks span:last-child {{ text-align:right; }}
#stageCard .stage-actions {{
  display:flex; gap:8px; margin-top:18px;
  padding-top:16px; border-top:1px solid #262636;
}}
#stageCard .stage-action-btn {{
  flex:1; text-align:center;
  background:#1a2538; border:1px solid #2a3a55; border-radius:6px;
  padding:8px 12px; font-size:13px; color:#9cd;
  text-decoration:none; cursor:pointer;
  transition:background 0.15s, color 0.15s;
}}
#stageCard .stage-action-btn:hover {{ background:#24324a; color:#cef; }}
#refineCard {{
  position:fixed; top:50%; left:50%; transform:translate(-50%,-50%);
  background:rgba(18,18,28,0.98); border:1px solid #333;
  border-radius:12px; padding:22px 26px 18px; z-index:42;
  width:min(480px, calc(100vw - 32px));
  max-height:calc(100vh - 60px);
  box-shadow:0 16px 48px rgba(0,0,0,0.5);
  display:flex; flex-direction:column;
}}
#refineCard.refine-hidden {{ display:none; }}
#refineCard .stage-close {{
  position:absolute; top:6px; right:10px;
  background:none; border:none; color:#888; font-size:22px;
  cursor:pointer; padding:4px 8px; line-height:1;
}}
#refineCard .stage-close:hover {{ color:#eee; }}
#refineCard h3 {{ font-size:17px; color:#eee; margin-bottom:4px; padding-right:24px; }}
#refineCard .refine-sub {{ font-size:12px; color:#778; margin-bottom:14px; }}
#refineCard .refine-rows {{
  flex:1 1 auto; overflow-y:auto; margin:0 -6px; padding:4px 6px;
  min-height:0;
}}
#refineCard .refine-row {{
  display:flex; align-items:center; gap:10px;
  padding:7px 0; border-bottom:1px solid #1a1a24;
}}
#refineCard .refine-row:last-child {{ border-bottom:none; }}
#refineCard .refine-row .refine-label {{
  flex:1 1 auto; font-size:12px; color:#aab;
  white-space:nowrap; overflow:hidden; text-overflow:ellipsis;
}}
#refineCard .refine-row input[type=range] {{
  flex:0 0 110px; accent-color:#6ab; cursor:pointer;
}}
#refineCard .refine-row .refine-value {{
  flex:0 0 56px; text-align:right;
  font-size:10px; color:#778; text-transform:uppercase; letter-spacing:0.3px;
}}
#refineCard .refine-footer {{
  margin-top:14px; padding-top:12px; border-top:1px solid #262636;
  display:flex; justify-content:flex-end; gap:8px;
}}
#refineCard .refine-footer button {{
  background:#1a2538; border:1px solid #2a3a55; border-radius:6px;
  padding:8px 18px; font-size:13px; color:#9cd; cursor:pointer;
}}
#refineCard .refine-footer button:hover {{ background:#24324a; color:#cef; }}
#nextStepCard {{
  position:fixed; right:16px; bottom:16px; width:280px; z-index:30;
  background:rgba(18,20,30,0.97); border:1px solid #2a3a55;
  border-radius:10px; padding:12px 14px 12px 16px;
  display:flex; flex-direction:column; gap:6px;
  box-shadow:0 8px 24px rgba(0,0,0,0.4);
}}
#nextStepCard.ns-hidden {{ display:none; }}
#nextStepCard .ns-label {{
  font-size:9px; color:#6a7da0; letter-spacing:0.6px;
  text-transform:uppercase;
}}
#nextStepCard .ns-title {{
  font-size:14px; color:#dde; font-weight:600; line-height:1.3;
}}
#nextStepCard .ns-meta {{ font-size:11px; color:#778; text-transform:capitalize; }}
#nextStepCard .ns-actions {{
  display:flex; gap:6px; align-items:center; margin-top:4px;
}}
#nextStepCard .ns-start {{
  flex:1; background:#1e3050; border:1px solid #3a5178; color:#cef;
  border-radius:6px; padding:6px 10px; font-size:12px;
  cursor:pointer; text-decoration:none; text-align:center;
}}
#nextStepCard .ns-start:hover {{ background:#284068; color:#def; }}
#nextStepCard .ns-close {{
  background:transparent; border:none; color:#667;
  font-size:18px; cursor:pointer; padding:0 6px; line-height:1;
}}
#nextStepCard .ns-close:hover {{ color:#aab; }}
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
  #controls {{ top:8px; right:8px; padding:6px 8px; }}
  #controls button {{ padding:8px 14px; font-size:14px; min-width:44px; min-height:44px; }}
  #panel {{
    position:fixed !important; left:0 !important; right:0 !important;
    bottom:0 !important; top:auto !important;
    max-width:100% !important; width:100% !important;
    max-height:50vh; border-radius:16px 16px 0 0; border-bottom:none;
    padding:16px 20px 24px; box-sizing:border-box;
  }}
  #panel .panel-close {{ top:12px; right:14px; font-size:24px; padding:8px; }}
  #pathBanner {{ top:8px; flex-wrap:wrap; justify-content:center; gap:8px; font-size:12px; padding:8px 12px; }}
  #pathBanner span {{ white-space:normal; flex-basis:100%; text-align:center; }}
  #search {{ width:calc(100vw - 32px); left:16px; transform:none; }}
  #search input {{ flex:1; width:auto; }}
  #tooltip {{ display:none !important; }}
  #stageCard {{ padding:18px 18px 14px; }}
  #stageCard h3 {{ font-size:15px; }}
  #stageCard .stage-ticks {{ font-size:8px; }}
  #refineCard {{ padding:16px 16px 12px; }}
  #refineCard h3 {{ font-size:15px; }}
  #refineCard .refine-row input[type=range] {{ flex:0 0 90px; }}
  #refineCard .refine-row .refine-value {{ flex:0 0 48px; font-size:9px; }}
  #nextStepCard {{ left:8px; right:8px; width:auto; bottom:8px; }}
}}

/* --- Sprout shell (Phase 12B Cut 7) --- */
#sproutShell {{
  position:fixed; inset:0; z-index:200;
  background:linear-gradient(180deg, #fff8ea 0%, #eaf5ff 100%);
  display:flex; flex-direction:column;
  font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  overflow:auto;
}}
#sproutShell.sprout-hidden {{ display:none; }}
.sprout-header {{
  display:flex; justify-content:space-between; align-items:center;
  padding:12px 16px; gap:8px;
}}
.sprout-header button {{
  background:#fff; border:2px solid #d0d0e0; border-radius:999px;
  padding:8px 14px; font-size:16px; cursor:pointer;
  min-height:44px; font-family:inherit;
}}
.sprout-escape {{ flex:1; max-width:260px; font-weight:600; color:#335; }}
.sprout-mute, .sprout-pin-btn {{ width:48px; padding:8px; }}
.sprout-main {{
  flex:1; display:flex; flex-direction:column; align-items:center; justify-content:center;
  padding:16px; text-align:center; gap:16px;
}}
.sprout-emoji {{ font-size:120px; line-height:1; }}
.sprout-title {{ font-size:36px; font-weight:800; color:#1a1a2e; margin:0; max-width:600px; }}
.sprout-core {{ font-size:20px; line-height:1.5; color:#334; margin:0; max-width:640px; }}
.sprout-buttons {{
  display:flex; gap:16px; justify-content:center; flex-wrap:wrap; margin-top:8px;
}}
.sprout-btn {{
  display:flex; flex-direction:column; align-items:center;
  background:#fff; border:4px solid #d0d0e0; border-radius:24px;
  padding:20px 28px; cursor:pointer; font-family:inherit;
  min-width:120px; min-height:120px;
  transition:transform 0.1s, border-color 0.1s;
}}
.sprout-btn:active {{ transform:scale(0.95); }}
.sprout-know {{ border-color:#8fd08f; }}
.sprout-kinda {{ border-color:#f4d67a; }}
.sprout-dunno {{ border-color:#f4a67a; }}
.sprout-btn-emoji {{ font-size:56px; line-height:1; }}
.sprout-btn-label {{ font-size:16px; font-weight:600; margin-top:6px; color:#334; }}
.sprout-book {{
  padding:8px 16px 24px; display:flex; justify-content:center;
}}
#sproutColoringBook {{ width:220px; height:220px; }}
#sproutColoringBook .wedge {{ stroke:#fff; stroke-width:1.5; transition:fill 0.3s; }}
#sproutColoringBook .wedge-label {{ font-size:8px; fill:#556; text-anchor:middle; pointer-events:none; font-weight:600; }}

#sproutPinModal {{
  position:fixed; inset:0; z-index:300;
  background:rgba(10, 10, 30, 0.6);
  display:flex; align-items:center; justify-content:center;
  font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
}}
#sproutPinModal.sprout-pin-hidden {{ display:none; }}
.sprout-pin-inner {{
  background:#fff; border-radius:16px; padding:24px; max-width:360px; width:90%;
  box-sizing:border-box;
}}
.sprout-pin-inner h2 {{ margin-top:0; font-size:20px; }}
.sprout-pin-inner p {{ color:#556; font-size:14px; line-height:1.4; }}
.sprout-pin-inner input {{
  font-size:28px; letter-spacing:10px; padding:12px; width:100%;
  text-align:center; border:2px solid #d0d0e0; border-radius:8px;
  box-sizing:border-box; margin:12px 0; font-family:inherit;
}}
.sprout-pin-actions {{ display:flex; gap:12px; }}
.sprout-pin-actions button {{
  flex:1; padding:12px; font-size:16px; cursor:pointer;
  border:2px solid #d0d0e0; border-radius:8px; background:#fff; font-family:inherit;
}}
.sprout-pin-error {{ color:#c33; font-size:14px; min-height:20px; margin-top:8px; }}
@media (max-width: 600px) {{
  .sprout-header {{ padding:10px 12px; }}
  .sprout-header button {{ font-size:14px; padding:8px 10px; }}
  .sprout-escape {{ max-width:none; }}
  .sprout-emoji {{ font-size:88px; }}
  .sprout-title {{ font-size:26px; }}
  .sprout-core {{ font-size:16px; }}
  .sprout-btn {{ min-width:92px; min-height:92px; padding:14px 18px; }}
  .sprout-btn-emoji {{ font-size:42px; }}
  .sprout-btn-label {{ font-size:13px; }}
  #sproutColoringBook {{ width:180px; height:180px; }}
}}
</style>
</head>
<body>

<canvas id="canvas"></canvas>
<div id="nav">
  <a href="index.html">All Domains</a>
</div>

<div id="stats">
  <h2>{title}</h2>
  <p id="statsLine">{n_topics} topics &middot; {n_edges} edges &middot; {n_domains} domains</p>
  <p id="helpText">Scroll to zoom &middot; Drag to pan &middot; Hover for details</p>
  <p style="margin-top:6px; color:#444;">Inner &rarr; early childhood &nbsp;&middot;&nbsp; Outer &rarr; graduate</p>
</div>

<div id="controls">
  <button onclick="resetView()">Reset</button>
  <button onclick="zoomBtn(1.3)">+</button>
  <button onclick="zoomBtn(0.7)">&minus;</button>
  <button id="fluencyBtn" onclick="toggleFluency()">Fluency</button>
  <button id="stageBtn" onclick="showStageCard()" title="Set your level">Level</button>
</div>
<div id="tooltip"></div>
<div id="panel"></div>
<div id="pathBanner"></div>
<div id="stageCard" class="stage-hidden">
  <button class="stage-close" onclick="hideStageCard()" aria-label="Dismiss">&times;</button>
  <h3>Make this yours</h3>
  <p class="stage-sub">Where are you in your learning? Slide to personalize the graph.</p>
  <div class="stage-label" id="stageLabel">Early Childhood</div>
  <input type="range" id="stageSlider" min="0" max="5" step="1" value="0" />
  <div class="stage-ticks">
    <span>Early</span>
    <span>Elem</span>
    <span>Middle</span>
    <span>HS</span>
    <span>College</span>
    <span>Grad</span>
  </div>
  <div class="stage-actions">
    <button type="button" class="stage-action-btn" onclick="showRefineCard()">Refine your map</button>
    <a href="quiz.html" class="stage-action-btn">Test yourself?</a>
  </div>
</div>

<div id="refineCard" class="refine-hidden">
  <button class="stage-close" onclick="hideRefineCard()" aria-label="Dismiss">&times;</button>
  <h3>Refine your map</h3>
  <p class="refine-sub">For precision: tell us what you already know in each domain. Adjusts how brightly each domain shows up.</p>
  <div class="refine-rows" id="refineRows"></div>
  <div class="refine-footer">
    <button type="button" onclick="hideRefineCard()">Done</button>
  </div>
</div>

<div id="nextStepCard" class="ns-hidden">
  <div class="ns-label">Your next step</div>
  <div class="ns-title" id="nsTitle"></div>
  <div class="ns-meta" id="nsMeta"></div>
  <div class="ns-actions">
    <a class="ns-start" id="nsStart" href="#">Start this</a>
    <button class="ns-close" onclick="hideNextStepCard()" aria-label="Dismiss">&times;</button>
  </div>
</div>
<div id="search">
  <input type="text" id="searchInput" placeholder="What do you want to understand?">
  <span class="count" id="searchCount"></span>
</div>

<div id="sproutShell" class="sprout-hidden">
  <header class="sprout-header">
    <button class="sprout-mute" onclick="toggleSproutTTS()" aria-label="Toggle sound" title="Sound">🔊</button>
    <button class="sprout-escape" onclick="exitSproutToMap()">See the full map</button>
    <button class="sprout-pin-btn" onclick="openParentPin()" aria-label="Parent settings" title="Parent settings">🔐</button>
  </header>
  <main class="sprout-main">
    <div class="sprout-emoji" id="sproutEmoji">🌱</div>
    <h1 class="sprout-title" id="sproutTitle"></h1>
    <p class="sprout-core" id="sproutCore"></p>
    <div class="sprout-buttons">
      <button class="sprout-btn sprout-know" onclick="sproutResponse('know')">
        <span class="sprout-btn-emoji">😊</span>
        <span class="sprout-btn-label">I know it</span>
      </button>
      <button class="sprout-btn sprout-kinda" onclick="sproutResponse('kinda')">
        <span class="sprout-btn-emoji">🤔</span>
        <span class="sprout-btn-label">Kinda</span>
      </button>
      <button class="sprout-btn sprout-dunno" onclick="sproutResponse('dunno')">
        <span class="sprout-btn-emoji">😕</span>
        <span class="sprout-btn-label">Dunno</span>
      </button>
    </div>
  </main>
  <aside class="sprout-book">
    <svg id="sproutColoringBook" viewBox="-110 -110 220 220" xmlns="http://www.w3.org/2000/svg"></svg>
  </aside>
</div>
<div id="sproutPinModal" class="sprout-pin-hidden">
  <div class="sprout-pin-inner">
    <h2 id="sproutPinTitle">Parent settings</h2>
    <p id="sproutPinDesc">Set a 4-digit PIN.</p>
    <input type="password" id="sproutPinInput" inputmode="numeric" pattern="[0-9]*" maxlength="4" autocomplete="off" />
    <div class="sprout-pin-actions">
      <button onclick="submitParentPin()">OK</button>
      <button onclick="closeParentPin()">Cancel</button>
    </div>
    <div class="sprout-pin-error" id="sproutPinError"></div>
  </div>
</div>

<script src="js/fluency.js"></script>
<script>
const data = {graph_json};

// --- Sprout mode detection (Phase 12B Cut 7) ---
// AND trigger: preset=sprout AND (no prior fluency data OR stage===0).
// Guards against a Persona C grad student accidentally tripping Sprout by
// dropping stage to 0 to debug the symmetric-decay bug.
const SPROUT_PIN_HASH_KEY = 'okg-sprout-pin-hash';
const SPROUT_PIN_SESSION_KEY = 'okg-sprout-pin-unlocked';

function detectSproutMode() {{
  var params = new URLSearchParams(window.location.search);
  if (params.get('preset') !== 'sprout') return false;
  var hasScores = false;
  try {{
    var raw = localStorage.getItem('okg-fluency');
    if (raw) {{
      var parsed = JSON.parse(raw);
      hasScores = parsed && Object.keys(parsed).length > 0;
    }}
  }} catch (e) {{}}
  if (!hasScores) return true;
  var stage = (typeof OKGFluency !== 'undefined') ? OKGFluency.getUserStage() : 3;
  return stage === 0;
}}

const isSproutMode = detectSproutMode();
if (isSproutMode && typeof OKGFluency !== 'undefined') {{
  OKGFluency.setUserStage(0);
}}

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
function zoomBtn(f) {{
  const newScale = Math.max(0.1, Math.min(20, camScale * f));
  const r = newScale / camScale;
  camX *= r; camY *= r;  // anchor at viewport center
  camScale = newScale; draw();
}}

// --- Fluency overlay ---
let showFluency = false;
let fluencyGraph = null;
let effectiveScores = null;
let frontierSet = null;

function buildFluencyGraph() {{
  var g = {{}};
  data.nodes.forEach(function(n) {{
    g[n.id] = {{
      prereqs: [],
      successors: [],
      course: n.course || '',
      domain: n.domain || '',
      pedagogyType: n.pedagogyType || 'assessable',
    }};
  }});
  data.edges.forEach(function(e) {{
    var type = e.type || 'hard';
    if (g[e.target]) g[e.target].prereqs.push({{id: e.source, type: type}});
    if (g[e.source]) g[e.source].successors.push({{id: e.target, type: type}});
  }});
  return g;
}}

function refreshFluency() {{
  if (typeof OKGFluency === 'undefined') return;
  if (!fluencyGraph) fluencyGraph = buildFluencyGraph();
  effectiveScores = OKGFluency.propagate(fluencyGraph);
  // Apply cold-start display floor from user stage + domain prior.
  // Does not write back to stored scores — floor is display-only.
  data.nodes.forEach(function(n) {{
    var floor = OKGFluency.computeFloor(n.stageInt, n.domain);
    if (floor > (effectiveScores[n.id] || 0)) effectiveScores[n.id] = floor;
  }});
  var ids = OKGFluency.findFrontier(fluencyGraph, effectiveScores);
  frontierSet = new Set(ids);
  if (typeof updateNextStepCard === 'function') updateNextStepCard();
}}

function toggleFluency() {{
  showFluency = !showFluency;
  if (showFluency) refreshFluency();
  document.getElementById('fluencyBtn').classList.toggle('active', showFluency);
  draw();
}}

const baseNodeRadius = Math.max(2, Math.min(4, 1600 / data.nodes.length));
// Damped zoom scaling: world-space radius shrinks as you zoom in,
// so screen-space size grows as sqrt(camScale) instead of linearly.
// At 10x zoom, nodes appear ~3.16x larger instead of 10x.
function getNodeRadius() {{ return baseNodeRadius / Math.sqrt(camScale); }}

function draw() {{
  const nodeRadius = getNodeRadius();
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
      {STAGE_BANDS['expert'][1] * 500 + 15} * Math.cos(s.start),
      {STAGE_BANDS['expert'][1] * 500 + 15} * Math.sin(s.start)
    );
    ctx.strokeStyle = "rgba(255,255,255,0.03)";
    ctx.lineWidth = 0.3;
    ctx.stroke();

    // Domain label at outer edge
    const labelR = {STAGE_BANDS['expert'][1] * 500 + 40};
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

  // Draw edges (suppressed further when a path reveal is active so the overlay pops)
  if (pathNodeSet) ctx.globalAlpha = 0.3;
  edgeData.forEach(e => {{
    ctx.beginPath();
    ctx.moveTo(e.s.x, e.s.y);
    ctx.lineTo(e.t.x, e.t.y);
    var capEdge = (e.s && e.s.kind === 'capacity') || (e.t && e.t.kind === 'capacity');
    if (capEdge) {{
      ctx.strokeStyle = "rgba(243,210,122,0.16)";   // origin-layer floor edges — gold
    }} else if (e.crossDomain) {{
      ctx.strokeStyle = "rgba(160,120,255,0.03)";
    }} else if (e.type === "soft") {{
      ctx.strokeStyle = "rgba(100,100,140,0.05)";
    }} else {{
      ctx.strokeStyle = "rgba(100,100,140,0.08)";
    }}
    ctx.lineWidth = capEdge ? 0.5 : 0.35;
    ctx.stroke();
  }});
  ctx.globalAlpha = 1.0;

  // Draw nodes
  var fluencyUserStage = (showFluency && typeof OKGFluency !== 'undefined')
    ? OKGFluency.getUserStage() : null;
  data.nodes.forEach(n => {{
    ctx.beginPath();
    ctx.arc(n.x, n.y, n.kind === 'capacity' ? nodeRadius * 4 : nodeRadius, 0, Math.PI * 2);
    var baseAlpha = 1.0;
    if (n.kind === 'capacity') {{
      ctx.fillStyle = 'hsl(45, 92%, 62%)';   // origin-layer capacity hub — gold
    }} else if (showFluency && effectiveScores) {{
      var score = effectiveScores[n.id] || 0;
      ctx.fillStyle = OKGFluency.fluencyColor(n.hue, score);
      // Alpha gradient: nodes far from user's declared stage fade out.
      // Frontier bonus keeps ready-to-learn topics visible across the gap.
      var stageDist = Math.abs((n.stageInt != null ? n.stageInt : 2) - fluencyUserStage);
      var frontierBonus = (frontierSet && frontierSet.has(n.id)) ? 0.2 : 0;
      baseAlpha = Math.min(1.0, Math.max(0.1, 1 - 0.3 * stageDist + frontierBonus));
    }} else {{
      ctx.fillStyle = `hsl(${{n.hue}}, 55%, ${{n.lightness}}%)`;
    }}
    // Path reveal dims everything outside the lit ancestry set.
    if (pathNodeSet && !pathNodeSet.has(n.id)) baseAlpha *= 0.12;
    ctx.globalAlpha = baseAlpha;
    ctx.fill();
    ctx.globalAlpha = 1.0;
    if (n.kind === 'capacity') {{
      ctx.strokeStyle = 'rgba(255,235,160,0.85)';
      ctx.lineWidth = 2 / Math.sqrt(camScale);
      ctx.stroke();
    }}
    if (showFluency && frontierSet && frontierSet.has(n.id)) {{
      ctx.strokeStyle = "rgba(255,200,50,0.9)";
      ctx.lineWidth = 1.5 / Math.sqrt(camScale);
      ctx.stroke();
    }}
  }});

  // --- Course labels (semantic zoom) ---
  if (camScale > 1.05) {{
    const scale = camScale * viewScale;
    // Viewport bounds in world coordinates
    const vL = -(W / 2 + camX) / scale;
    const vR = (W / 2 - camX) / scale;
    const vT = -(H / 2 + camY) / scale;
    const vB = (H / 2 - camY) / scale;

    // Compute dynamic centroids from VISIBLE nodes only
    const visCourseBuckets = {{}};
    data.nodes.forEach(n => {{
      if (n.x < vL || n.x > vR || n.y < vT || n.y > vB) return;
      const key = n.course || "";
      if (!visCourseBuckets[key]) visCourseBuckets[key] = {{ sx: 0, sy: 0, count: 0, hue: n.hue }};
      visCourseBuckets[key].sx += n.x;
      visCourseBuckets[key].sy += n.y;
      visCourseBuckets[key].count++;
    }});

    const visLabels = Object.entries(visCourseBuckets)
      .filter(([_, c]) => c.count >= 3)
      .map(([course, c]) => ({{
        label: course.replace(/-/g, " "),
        x: c.sx / c.count,
        y: c.sy / c.count,
        hue: c.hue,
        count: c.count,
      }}))
      .sort((a, b) => b.count - a.count);

    // Font size: readable on screen regardless of zoom
    const cFontSize = Math.max(3, Math.round(12 / camScale));
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";

    // Opacity ramps from 0 at 1.05x to full at 1.5x
    const labelAlpha = Math.min(1, (camScale - 1.05) / 0.45);

    // Collision avoidance
    const cPlaced = [];

    visLabels.forEach(c => {{
      ctx.font = `bold ${{cFontSize}}px sans-serif`;
      const tw = ctx.measureText(c.label).width;
      const halfW = tw / 2 + 2;

      let collides = false;
      for (const p of cPlaced) {{
        if (Math.abs(c.x - p.x) < (halfW + p.hw) && Math.abs(c.y - p.y) < cFontSize * 1.4) {{
          collides = true;
          break;
        }}
      }}
      if (collides) return;

      ctx.strokeStyle = `rgba(0,0,0,${{0.6 * labelAlpha}})`;
      ctx.lineWidth = 3;
      ctx.lineJoin = "round";
      ctx.strokeText(c.label, c.x, c.y);
      ctx.fillStyle = `hsla(${{c.hue}}, 45%, 70%, ${{0.85 * labelAlpha}})`;
      ctx.fillText(c.label, c.x, c.y);

      cPlaced.push({{ x: c.x, y: c.y, hw: halfW }});
    }});
  }}

  // Draw highlights for selected node (persists after click).
  // Suppressed during a path reveal — the ancestry overlay is the sole highlight,
  // otherwise the focal node's full prereq/successor fan clutters the dimmed view.
  const highlightTarget = selectedNode || hoveredNode;
  if (highlightTarget && !pathNodeSet) {{
    drawHighlight(highlightTarget);
  }}

  // Path reveal overlay (bright ancestry on top of the dimmed base)
  if (pathNodeSet) {{
    drawPathOverlay();
  }}

  // Draw search match highlights
  if (searchMatches.length > 0) {{
    searchMatches.forEach(n => {{
      ctx.beginPath();
      ctx.arc(n.x, n.y, nodeRadius * 3, 0, Math.PI * 2);
      ctx.fillStyle = `hsl(${{n.hue}}, 80%, ${{n.lightness + 15}}%)`;
      ctx.fill();
      ctx.strokeStyle = "rgba(255,255,100,0.8)";
      ctx.lineWidth = 1.5 / Math.sqrt(camScale);
      ctx.stroke();
    }});
    // Label single match
    if (searchMatches.length <= 5) {{
      const searchFontSize = Math.max(3, Math.round(9 / Math.sqrt(camScale)));
      searchMatches.forEach(n => {{
        ctx.font = `bold ${{searchFontSize}}px sans-serif`;
        ctx.fillStyle = "#fff";
        ctx.textAlign = "center";
        ctx.fillText(n.title, n.x, n.y - nodeRadius * 4 - 3 / Math.sqrt(camScale));
      }});
    }}
  }}

  ctx.restore();
  ctx.restore();
}}

function drawHighlight(node) {{
  const nodeRadius = getNodeRadius();
  // Highlight connected edges (blue=prereqs, orange=dependents)
  edgeData.forEach(ed => {{
    if (ed.s === node || ed.t === node) {{
      ctx.beginPath();
      ctx.moveTo(ed.s.x, ed.s.y);
      ctx.lineTo(ed.t.x, ed.t.y);
      ctx.strokeStyle = ed.t === node
        ? "rgba(80,180,255,0.6)"
        : "rgba(255,160,80,0.6)";
      ctx.lineWidth = 1.2 / Math.sqrt(camScale);
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
      ctx.lineWidth = 0.6 / Math.sqrt(camScale);
      ctx.stroke();
    }}
  }});

  // Main node highlight
  ctx.beginPath();
  ctx.arc(node.x, node.y, nodeRadius * 3, 0, Math.PI * 2);
  ctx.fillStyle = `hsl(${{node.hue}}, 80%, ${{node.lightness + 20}}%)`;
  ctx.fill();
  ctx.strokeStyle = "#fff";
  ctx.lineWidth = 1.5 / Math.sqrt(camScale);
  ctx.stroke();

  // Label — damped font size so it doesn't balloon at high zoom
  const labelFontSize = Math.max(3, Math.round(9 / Math.sqrt(camScale)));
  ctx.font = `bold ${{labelFontSize}}px sans-serif`;
  ctx.fillStyle = "#fff";
  ctx.textAlign = "center";
  ctx.fillText(node.title, node.x, node.y - nodeRadius * 4 - 3 / Math.sqrt(camScale));
}}

// --- Mouse interaction ---
let isDragging = false, dragStartX, dragStartY;
let lastTouchTime = 0;
let lastTapTime = 0, lastTapX = 0, lastTapY = 0;
let hoveredNode = null;
let selectedNode = null;
let searchMatches = [];

// --- Path engine state ---
// When a reveal is active, pathNodeSet holds the lit topic ids and pathEdges
// the bright ancestry edges (node-ref pairs); the base graph dims behind them.
let pathNodeSet = null;
let pathEdges = null;
let pathRevealId = null;        // the focal topic of the current reveal
const pathAncestryCache = {{}}; // id -> unbounded backward-BFS result (so "show full chain" is instant)

if (!isSproutMode) {{ draw(); }}

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
    if (pendingPathFrom && pendingPathFrom !== searchMatches[0].id) {{
      // Pairing mode: this search picks the second topic for a path.
      revealPath(pendingPathFrom, searchMatches[0].id);
      return;
    }}
    selectedNode = searchMatches[0];
    hoveredNode = searchMatches[0];
    centerOnNode(searchMatches[0], 3.5);
    showPanel(searchMatches[0], W / 2, H / 2);
    // A2: a search IS "show me what it takes to understand X."
    revealAncestry(searchMatches[0].id, 4);
  }} else {{
    selectedNode = null;
    if (pathNodeSet) clearPath();
    hidePanel();
  }}
  draw();
}});

document.addEventListener("keydown", (e) => {{
  if ((e.ctrlKey || e.metaKey) && e.key === "f") {{
    e.preventDefault();
    searchInput.focus();
    searchInput.select();
  }} else if (e.key === "Escape" && pathNodeSet) {{
    clearPath();
  }}
}});

function screenToWorld(sx, sy) {{
  return {{
    x: (sx - W / 2 - camX) / (camScale * viewScale),
    y: (sy - H / 2 - camY) / (camScale * viewScale),
  }};
}}

// Center the camera on a node at a given zoom. Single source of truth for
// camera centring (the ?focus=/?ancestry= handlers + search reuse it).
// screenDX shifts the node off dead-center (used by ancestry reveal so the
// right-docked panel doesn't cover the lit subtree).
function centerOnNode(node, scale, screenDX) {{
  camScale = scale;
  const s = camScale * viewScale;
  camX = (screenDX || 0) - node.x * s;
  camY = -node.y * s;
}}

// --- Full-graph lazy load ---
// The radial embeds only a filtered edge subset (within-domain + nearby
// cross-domain) to avoid a hairball, so ancestry that crosses domains needs
// the complete adjacency in js/graph.js (window.OKG_GRAPH, ~3.5MB). Load it
// once on the first reveal action — never on the cold path.
let _fullGraph = null, _fullGraphLoading = false;
const _fullGraphCbs = [];
function withFullGraph(cb) {{
  if (_fullGraph) {{ cb(_fullGraph); return; }}
  _fullGraphCbs.push(cb);
  if (_fullGraphLoading) return;
  _fullGraphLoading = true;
  const script = document.createElement('script');
  script.src = 'js/graph.js';
  script.onload = function () {{
    _fullGraph = window.OKG_GRAPH || {{}};
    _fullGraphLoading = false;
    const cbs = _fullGraphCbs.splice(0);
    cbs.forEach(function (f) {{ f(_fullGraph); }});
  }};
  script.onerror = function () {{
    _fullGraphLoading = false;
    _fullGraphCbs.splice(0);
    showPathBanner('<span>Couldn&rsquo;t load the full graph.</span>'
      + '<button class="pb-clear" onclick="clearPath()">Dismiss</button>');
  }};
  document.head.appendChild(script);
}}

// Unbounded backward BFS through prerequisites. graph.js stores compact
// {{d, c, p:[ids], s:[ids]}} (edge type is not retained in the full graph, so
// ancestry edges render uniformly). Returns hop depth per ancestor + edges.
function computeAncestry(G, startId) {{
  const hopOf = {{}};
  hopOf[startId] = 0;
  const queue = [startId];
  const edges = [];
  while (queue.length) {{
    const cur = queue.shift();
    const h = hopOf[cur];
    const entry = G[cur];
    if (!entry || !entry.p) continue;
    for (let i = 0; i < entry.p.length; i++) {{
      const pid = entry.p[i];
      if (!nodeMap[pid]) continue;        // skip dangling ids with no position
      edges.push({{ from: pid, to: cur, hop: h }});
      if (hopOf[pid] === undefined) {{ hopOf[pid] = h + 1; queue.push(pid); }}
    }}
  }}
  return {{ hopOf: hopOf, edges: edges }};
}}

// A3 — reveal a topic's prerequisite ancestry, capped at maxHops (Infinity = full chain).
function revealAncestry(nodeId, maxHops) {{
  const node = nodeMap[nodeId];
  if (!node) return;
  withFullGraph(function (G) {{
    let anc = pathAncestryCache[nodeId];
    if (!anc) {{ anc = computeAncestry(G, nodeId); pathAncestryCache[nodeId] = anc; }}

    const totalAncestors = Object.keys(anc.hopOf).length - 1;  // minus self
    if (totalAncestors === 0) {{
      // Always-answerable foundational case: nothing comes before it.
      pathNodeSet = null; pathEdges = null; pathRevealId = null;
      showPathBanner('<span><strong>' + escapeHtml(node.title)
        + '</strong> is a starting point &mdash; nothing comes before it.</span>'
        + '<button class="pb-clear" onclick="clearPath()">Clear</button>');
      draw();
      return;
    }}

    const nodeSet = new Set();
    for (const id in anc.hopOf) {{ if (anc.hopOf[id] <= maxHops) nodeSet.add(id); }}
    const edges = [];
    anc.edges.forEach(function (ed) {{
      if (ed.hop < maxHops) edges.push({{ s: nodeMap[ed.from], t: nodeMap[ed.to] }});
    }});

    pathNodeSet = nodeSet;
    pathEdges = edges;
    pathRevealId = nodeId;
    // Shift the focal node left of center on desktop so the docked panel
    // doesn't cover the inward-fanning ancestry (panel docks bottom on mobile).
    centerOnNode(node, 3.5, W > 768 ? -W * 0.16 : 0);

    const shown = nodeSet.size - 1;
    const hasMore = (maxHops !== Infinity) && (totalAncestors > shown);
    let banner = '<span>Showing what <strong>' + escapeHtml(node.title)
      + '</strong> builds on &mdash; ' + shown + ' topic' + (shown === 1 ? '' : 's')
      + (hasMore ? ' within ' + maxHops + ' steps' : ' (full chain)') + '.</span>';
    if (hasMore) {{
      banner += '<button onclick="revealAncestryFull()">Show full chain (' + totalAncestors + ')</button>';
    }}
    banner += '<button class="pb-clear" onclick="clearPath()">Clear</button>';
    showPathBanner(banner);
    draw();
  }});
}}

function revealAncestryFull() {{
  if (pathRevealId) revealAncestry(pathRevealId, Infinity);
}}

// ---- Session 2: A->B bridge path + no-path fallback ----
// pendingPathFrom: when set, the next topic the user selects becomes B and we
// run revealPath(from, B). pathPair: the [a,b] currently shown (for ?path= copy).
// pathEndpointSet: ids drawn with the big focal style (both endpoints + shared X).
let pendingPathFrom = null;
let pathPair = null;
let pathEndpointSet = null;

function startPathPairing(fromId) {{
  pendingPathFrom = fromId;
  const n = nodeMap[fromId];
  showPathBanner('<span>Pick a second topic to connect with <strong>'
    + escapeHtml(n ? n.title : fromId) + '</strong> &mdash; search or click any node.</span>'
    + '<button class="pb-clear" onclick="cancelPathPairing()">Cancel</button>');
}}

function cancelPathPairing() {{
  pendingPathFrom = null;
  clearPath();
}}

// One representative shortest chain from srcId up to dstId within an ancestry
// result whose edges point prereq(from) -> successor(to). BFS backward from dst.
function reconstructChain(anc, srcId, dstId) {{
  const prereqsOf = {{}};
  anc.edges.forEach(function (e) {{
    (prereqsOf[e.to] = prereqsOf[e.to] || []).push(e.from);
  }});
  const prev = {{}};
  const seen = {{}};
  seen[dstId] = true;
  const q = [dstId];
  while (q.length) {{
    const cur = q.shift();
    if (cur === srcId) break;
    const ps = prereqsOf[cur] || [];
    for (let i = 0; i < ps.length; i++) {{
      const p = ps[i];
      if (seen[p]) continue;
      seen[p] = true; prev[p] = cur; q.push(p);
    }}
  }}
  if (!seen[srcId]) return null;
  const nodes = [srcId];
  const edges = [];
  let cur = srcId;
  while (cur !== dstId) {{
    const nxt = prev[cur];
    if (nodeMap[cur] && nodeMap[nxt]) edges.push({{ s: nodeMap[cur], t: nodeMap[nxt] }});
    nodes.push(nxt);
    cur = nxt;
  }}
  return {{ nodes: nodes, edges: edges }};
}}

// Fit the camera to a set of node ids (used for two-topic surfaces where no
// single node is the focus). Mirrors centerOnNode's left-shift on desktop.
function fitNodes(ids) {{
  let minX = Infinity, minY = Infinity, maxX = -Infinity, maxY = -Infinity, cnt = 0;
  ids.forEach(function (id) {{
    const n = nodeMap[id]; if (!n) return;
    if (n.x < minX) minX = n.x; if (n.x > maxX) maxX = n.x;
    if (n.y < minY) minY = n.y; if (n.y > maxY) maxY = n.y;
    cnt++;
  }});
  if (!cnt) return;
  const cx = (minX + maxX) / 2, cy = (minY + maxY) / 2;
  const spanX = Math.max(maxX - minX, 1), spanY = Math.max(maxY - minY, 1);
  const pad = 1.4;
  const scaleX = (W * 0.6) / (spanX * viewScale * pad);
  const scaleY = (H * 0.6) / (spanY * viewScale * pad);
  camScale = Math.max(0.3, Math.min(3.5, Math.min(scaleX, scaleY)));
  const s = camScale * viewScale;
  camX = (W > 768 ? -W * 0.12 : 0) - cx * s;
  camY = -cy * s;
}}

// Entry point for both-topic surfaces. Determines bridge vs fallback.
function revealPath(aId, bId) {{
  pendingPathFrom = null;
  const na = nodeMap[aId], nb = nodeMap[bId];
  if (!na || !nb) return;
  if (aId === bId) {{ revealAncestry(aId, 4); return; }}
  hidePanel();  // the two-topic surface shouldn't be cluttered by a stale panel
  withFullGraph(function (G) {{
    const ancA = pathAncestryCache[aId] || (pathAncestryCache[aId] = computeAncestry(G, aId));
    const ancB = pathAncestryCache[bId] || (pathAncestryCache[bId] = computeAncestry(G, bId));

    // Bridge: one topic is a prerequisite-ancestor of the other.
    if (ancA.hopOf[bId] !== undefined) {{ renderChainPath(reconstructChain(ancA, bId, aId), nb, na, bId, aId); return; }}
    if (ancB.hopOf[aId] !== undefined) {{ renderChainPath(reconstructChain(ancB, aId, bId), na, nb, aId, bId); return; }}

    // No direct path: nearest shared ancestor minimizes combined hop distance.
    let bestX = null, bestCost = Infinity;
    for (const id in ancA.hopOf) {{
      if (ancB.hopOf[id] !== undefined && id !== aId && id !== bId) {{
        const cost = ancA.hopOf[id] + ancB.hopOf[id];
        if (cost < bestCost) {{ bestCost = cost; bestX = id; }}
      }}
    }}
    if (bestX) renderForkPath(ancA, ancB, aId, bId, bestX);
    else renderDisjoint(ancA, ancB, na, nb);
  }});
}}

function renderChainPath(chain, srcNode, dstNode, srcId, dstId) {{
  if (!chain) {{ clearPath(); return; }}
  pathNodeSet = new Set(chain.nodes);
  pathEdges = chain.edges;
  pathRevealId = null;
  pathEndpointSet = new Set([srcId, dstId]);
  pathPair = [srcId, dstId];
  fitNodes(chain.nodes);
  const steps = chain.nodes.length - 1;
  let banner = '<span>From <strong>' + escapeHtml(srcNode.title) + '</strong> to <strong>'
    + escapeHtml(dstNode.title) + '</strong>: ' + steps + ' prerequisite step' + (steps === 1 ? '' : 's')
    + ' &mdash; <strong>' + escapeHtml(srcNode.title) + '</strong> comes first.</span>';
  banner += pathCopyButton() + '<button class="pb-clear" onclick="clearPath()">Clear</button>';
  showPathBanner(banner);
  draw();
}}

// No-path fallback (the gate): A and B don't connect, but share an ancestor X.
function renderForkPath(ancA, ancB, aId, bId, xId) {{
  const chainA = reconstructChain(ancA, xId, aId);
  const chainB = reconstructChain(ancB, xId, bId);
  const nodes = new Set();
  const edges = [];
  [chainA, chainB].forEach(function (c) {{
    if (!c) return;
    c.nodes.forEach(function (n) {{ nodes.add(n); }});
    c.edges.forEach(function (e) {{ edges.push(e); }});
  }});
  nodes.add(aId); nodes.add(bId); nodes.add(xId);
  pathNodeSet = nodes;
  pathEdges = edges;
  pathRevealId = null;
  pathEndpointSet = new Set([aId, bId, xId]);
  pathPair = [aId, bId];
  fitNodes(Array.from(nodes));
  const na = nodeMap[aId], nb = nodeMap[bId], nx = nodeMap[xId];
  let banner = '<span><strong>' + escapeHtml(na.title) + '</strong> and <strong>' + escapeHtml(nb.title)
    + '</strong> don&rsquo;t connect directly &mdash; neither is a prerequisite for the other. '
    + 'Their nearest shared foundation is <strong>' + escapeHtml(nx.title) + '</strong>.</span>';
  banner += pathCopyButton() + '<button class="pb-clear" onclick="clearPath()">Clear</button>';
  showPathBanner(banner);
  draw();
}}

// Disjoint fallback: no shared ancestor at all. Show each topic's own roots.
function renderDisjoint(ancA, ancB, na, nb) {{
  const nodes = new Set([na.id, nb.id]);
  const edges = [];
  function addCapped(anc, cap) {{
    anc.edges.forEach(function (e) {{
      if (e.hop < cap) {{ nodes.add(e.from); nodes.add(e.to); edges.push({{ s: nodeMap[e.from], t: nodeMap[e.to] }}); }}
    }});
  }}
  addCapped(ancA, 2); addCapped(ancB, 2);
  pathNodeSet = nodes;
  pathEdges = edges;
  pathRevealId = null;
  pathEndpointSet = new Set([na.id, nb.id]);
  pathPair = [na.id, nb.id];
  fitNodes(Array.from(nodes));
  let banner = '<span><strong>' + escapeHtml(na.title) + '</strong> and <strong>' + escapeHtml(nb.title)
    + '</strong> come from independent foundations &mdash; they share no prerequisites. '
    + 'Showing what each one builds on separately.</span>';
  banner += pathCopyButton() + '<button class="pb-clear" onclick="clearPath()">Clear</button>';
  showPathBanner(banner);
  draw();
}}

function pathCopyButton() {{
  return '<button onclick="copyPathLink(this)" title="Copy a shareable link to this pair">Copy link</button>';
}}
function copyPathLink(btn) {{
  if (!pathPair) return;
  const url = location.origin + location.pathname + "?path="
    + encodeURIComponent(pathPair[0]) + "," + encodeURIComponent(pathPair[1]);
  const done = function () {{ btn.textContent = "Copied"; btn.disabled = true; }};
  if (navigator.clipboard && navigator.clipboard.writeText) {{
    navigator.clipboard.writeText(url).then(done, done);
  }} else {{
    const ta = document.createElement("textarea");
    ta.value = url; document.body.appendChild(ta); ta.select();
    try {{ document.execCommand("copy"); }} catch (err) {{}}
    document.body.removeChild(ta); done();
  }}
}}

function clearPath() {{
  pathNodeSet = null; pathEdges = null; pathRevealId = null;
  pathPair = null; pathEndpointSet = null; pendingPathFrom = null;
  hidePathBanner();
  draw();
}}

function showPathBanner(html) {{
  const b = document.getElementById('pathBanner');
  if (!b) return;
  b.innerHTML = html;
  b.style.display = 'flex';
}}
function hidePathBanner() {{
  const b = document.getElementById('pathBanner');
  if (b) b.style.display = 'none';
}}

function escapeHtml(s) {{
  return String(s).replace(/[&<>"]/g, function (c) {{
    return {{ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }}[c];
  }});
}}

// Draw the bright ancestry overlay on top of the dimmed base graph.
function drawPathOverlay() {{
  const nr = getNodeRadius();
  ctx.globalAlpha = 1.0;
  pathEdges.forEach(function (e) {{
    if (!e.s || !e.t) return;
    ctx.beginPath();
    ctx.moveTo(e.s.x, e.s.y);
    ctx.lineTo(e.t.x, e.t.y);
    ctx.strokeStyle = "rgba(120,200,255,0.55)";
    ctx.lineWidth = 1.0 / Math.sqrt(camScale);
    ctx.stroke();
  }});
  function isPathEndpoint(id) {{ return id === pathRevealId || (pathEndpointSet && pathEndpointSet.has(id)); }}
  pathNodeSet.forEach(function (id) {{
    const n = nodeMap[id];
    if (!n || isPathEndpoint(id)) return;
    ctx.beginPath();
    ctx.arc(n.x, n.y, nr * 1.8, 0, Math.PI * 2);
    ctx.fillStyle = `hsl(${{n.hue}}, 70%, ${{n.lightness + 12}}%)`;
    ctx.fill();
  }});
  // Emphasize endpoints: the single focal node (ancestry reveal) or both path
  // endpoints + their shared ancestor (two-topic surfaces).
  const ends = pathEndpointSet ? Array.from(pathEndpointSet) : (pathRevealId ? [pathRevealId] : []);
  ends.forEach(function (id) {{
    const s = nodeMap[id];
    if (!s) return;
    ctx.beginPath();
    ctx.arc(s.x, s.y, nr * 3, 0, Math.PI * 2);
    ctx.fillStyle = `hsl(${{s.hue}}, 85%, ${{s.lightness + 22}}%)`;
    ctx.fill();
    ctx.strokeStyle = "#fff";
    ctx.lineWidth = 1.5 / Math.sqrt(camScale);
    ctx.stroke();
  }});
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

  const hitRadius = Math.max(baseNodeRadius * 2.5, 12) / camScale;
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
    canvas.style.cursor = hoverR > {STAGE_BANDS['expert'][1] * 500 - 30} ? "pointer" : "grab";
  }}
}});

let dragMoved = false;
let mouseDownX = 0, mouseDownY = 0;
canvas.addEventListener("mousedown", (e) => {{
  if (Date.now() - lastTouchTime < 500) return;
  isDragging = true;
  dragMoved = false;
  dragStartX = e.clientX; dragStartY = e.clientY;
  mouseDownX = e.clientX; mouseDownY = e.clientY;
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

  // Path engine: reveal this topic's prerequisite ancestry + share a deep link.
  html += `<div class="panel-path">`;
  html += `<button class="path-btn" data-act="ancestry">Show what this builds on</button>`;
  html += `<button class="path-btn" data-act="pair">Connect to another topic&hellip;</button>`;
  html += `<button class="path-btn copy" data-act="copylink" title="Copy a shareable link">Copy link</button>`;
  html += `</div>`;

  // Fluency correction buttons: quick self-report from the panel.
  html += `<div class="panel-correction">`;
  html += `<button class="iknow" data-act="know">I know this</button>`;
  html += `<button class="dontknow" data-act="dontknow">I don't know this</button>`;
  html += `</div>`;

  panel.innerHTML = html;
  panel.style.display = "block";
  // Scale panel down at high zoom so it doesn't dominate the viewport
  const panelScale = camScale > 2 ? Math.max(0.55, 1 / Math.log2(camScale)) : 1;
  panel.style.transformOrigin = "top left";
  panel.style.transform = panelScale < 1 ? `scale(${{panelScale.toFixed(2)}})` : "";
  if (W > 768) {{
    // Position panel near click but keep on screen
    const effectiveW = 380 * panelScale;
    const effectiveH = 300 * panelScale;
    let px = screenX + 20, py = screenY - 20;
    if (px + effectiveW > W) px = screenX - effectiveW;
    if (py + effectiveH > H) py = H - effectiveH;
    if (py < 10) py = 10;
    panel.style.left = px + "px";
    panel.style.top = py + "px";
  }}

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

  // Path-engine handlers.
  panel.querySelectorAll(".panel-path button").forEach(btn => {{
    btn.addEventListener("click", () => {{
      const act = btn.getAttribute("data-act");
      if (act === "ancestry") {{
        btn.textContent = "Loading\\u2026";
        revealAncestry(node.id, 4);
      }} else if (act === "pair") {{
        startPathPairing(node.id);
      }} else if (act === "copylink") {{
        const url = location.origin + location.pathname + "?ancestry=" + encodeURIComponent(node.id);
        const done = function () {{ btn.textContent = "Copied"; btn.disabled = true; }};
        if (navigator.clipboard && navigator.clipboard.writeText) {{
          navigator.clipboard.writeText(url).then(done, done);
        }} else {{
          const ta = document.createElement("textarea");
          ta.value = url; document.body.appendChild(ta); ta.select();
          try {{ document.execCommand("copy"); }} catch (err) {{}}
          document.body.removeChild(ta); done();
        }}
      }}
    }});
  }});

  // Fluency self-report handlers: apply immediately + refresh visuals.
  panel.querySelectorAll(".panel-correction button").forEach(btn => {{
    btn.addEventListener("click", () => {{
      if (typeof OKGFluency === 'undefined') return;
      const act = btn.getAttribute("data-act");
      if (act === "know") OKGFluency.setScore(node.id, 100);
      else if (act === "dontknow") OKGFluency.setScore(node.id, 0);
      if (!showFluency) {{
        toggleFluency();  // auto-enable fluency so the user sees the effect
      }} else {{
        refreshFluency();
        draw();
      }}
      if (typeof updateNextStepCard === 'function') updateNextStepCard();
      btn.textContent = "Saved";
      btn.disabled = true;
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
      if (pendingPathFrom && pendingPathFrom !== hoveredNode.id) {{
        revealPath(pendingPathFrom, hoveredNode.id);
        return;
      }}
      showPanel(hoveredNode, e.clientX, e.clientY);
    }} else {{
      hidePanel();
      // Check if click is in the outer ring (domain label area)
      const wp = screenToWorld(e.clientX, e.clientY);
      const clickR = Math.hypot(wp.x, wp.y);
      if (clickR > {STAGE_BANDS['expert'][1] * 500 - 30}) {{
        let clickAngle = Math.atan2(wp.y, wp.x);
        if (clickAngle < 0) clickAngle += Math.PI * 2;
        for (const s of data.sectors) {{
          let start = s.start, end = s.end;
          if (start < 0) start += Math.PI * 2;
          if (end < 0) end += Math.PI * 2;
          if (clickAngle >= start && clickAngle <= end) {{
            window.location.href = s.domain + "-map.html";
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
    const dx = e.clientX - mouseDownX;
    const dy = e.clientY - mouseDownY;
    if (Math.abs(dx) > 3 || Math.abs(dy) > 3) dragMoved = true;
  }}
}});
canvas.addEventListener("wheel", (e) => {{
  e.preventDefault();
  const factor = e.deltaY > 0 ? 0.9 : 1.1;
  const newScale = Math.max(0.1, Math.min(20, camScale * factor));
  const r = newScale / camScale;
  // Anchor zoom at cursor position
  camX = camX * r + (e.clientX - W / 2) * (1 - r);
  camY = camY * r + (e.clientY - H / 2) * (1 - r);
  camScale = newScale;
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
      // Double-tap to zoom
      const now = Date.now();
      if (now - lastTapTime < 300 && Math.hypot(lastTouchX - lastTapX, lastTouchY - lastTapY) < 30) {{
        camScale = Math.min(20, camScale * 2.5);
        lastTapTime = 0;
        hidePanel();
        draw();
      }} else {{
        lastTapTime = now;
        lastTapX = lastTouchX; lastTapY = lastTouchY;
        // Tap — do hit detection at touch point (generous radius)
        const p = screenToWorld(lastTouchX, lastTouchY);
        let closest = null, closestDist = Infinity;
        data.nodes.forEach(n => {{
          const d = Math.hypot(n.x - p.x, n.y - p.y);
          if (d < closestDist) {{ closestDist = d; closest = n; }}
        }});
        const hitRadius = Math.max(baseNodeRadius * 3, 18) / camScale;
        if (closest && closestDist < hitRadius) {{
          if (pendingPathFrom && pendingPathFrom !== closest.id) {{
            revealPath(pendingPathFrom, closest.id);
            return;
          }}
          hoveredNode = closest;
          draw();
          showPanel(closest, lastTouchX, lastTouchY);
        }} else {{
          hoveredNode = null;
          draw();
          hidePanel();
          // Check if tap is in outer ring (domain label area)
          const wp = screenToWorld(lastTouchX, lastTouchY);
          const tapR = Math.hypot(wp.x, wp.y);
          if (tapR > {STAGE_BANDS['expert'][1] * 500 - 30}) {{
            let tapAngle = Math.atan2(wp.y, wp.x);
            if (tapAngle < 0) tapAngle += Math.PI * 2;
            for (const s of data.sectors) {{
              let start = s.start, end = s.end;
              if (start < 0) start += Math.PI * 2;
              if (end < 0) end += Math.PI * 2;
              if (tapAngle >= start && tapAngle <= end) {{
                window.location.href = s.domain + "-map.html";
                break;
              }}
            }}
          }}
        }}
      }}
    }}
  }} else if (e.touches.length === 1) {{
    lastTouchX = e.touches[0].clientX;
    lastTouchY = e.touches[0].clientY;
    lastPinchDist = 0;
  }}
}}, {{ passive: false }});

// Touch device: update help text and search placeholder
if ("ontouchstart" in window || navigator.maxTouchPoints > 0) {{
  const ht = document.getElementById("helpText");
  if (ht) ht.textContent = "Pinch to zoom \u00b7 Drag to pan \u00b7 Tap for details \u00b7 Double-tap to zoom in";
  const si = document.getElementById("searchInput");
  if (si) si.placeholder = "Search topics...";
}}

// --- Stage slider card (Cut 2) ---
const STAGE_LABELS = [
  'Early Childhood',
  'Elementary',
  'Middle School',
  'High School',
  'College',
  'Graduate',
];
const STAGE_CARD_DISMISSED_KEY = 'okg-stage-card-dismissed';

// --- Refine your map (Cut 4 step 6) ---
const REFINE_DOMAINS = {refine_domains_json};
const REFINE_POSITIONS = [
  {{label: 'None',    mul: 0.2}},
  {{label: 'Some',    mul: 0.6}},
  {{label: 'Default', mul: 1.0}},
  {{label: 'Strong',  mul: 1.4}},
  {{label: 'Expert',  mul: 1.8}},
];

function showStageCard() {{
  var card = document.getElementById('stageCard');
  if (card) card.classList.remove('stage-hidden');
}}

function hideStageCard() {{
  var card = document.getElementById('stageCard');
  if (card) card.classList.add('stage-hidden');
  try {{ localStorage.setItem(STAGE_CARD_DISMISSED_KEY, '1'); }} catch (e) {{}}
}}

function initStageSlider() {{
  if (typeof OKGFluency === 'undefined') return;
  var slider = document.getElementById('stageSlider');
  var label = document.getElementById('stageLabel');
  if (!slider || !label) return;

  var current = OKGFluency.getUserStage();
  slider.value = current;
  label.textContent = STAGE_LABELS[current];

  slider.addEventListener('input', function () {{
    var val = parseInt(this.value, 10);
    label.textContent = STAGE_LABELS[val];
    OKGFluency.setUserStage(val);
    // Auto-enable fluency on first slider interaction so the graph responds
    if (!showFluency) {{
      toggleFluency();  // this also calls draw()
    }} else {{
      refreshFluency();
      draw();
    }}
  }});

  // Stop canvas drag/pan from capturing events on the card itself
  var card = document.getElementById('stageCard');
  if (card) {{
    ['mousedown', 'touchstart', 'touchmove', 'wheel'].forEach(function (ev) {{
      card.addEventListener(ev, function (e) {{ e.stopPropagation(); }}, {{ passive: true }});
    }});
  }}

  // First-visit auto-show removed (Jun 2026): the card covered the map's
  // center before a new visitor saw anything. Entry point is the Level button.
}}

if (!isSproutMode) {{ initStageSlider(); }}

// --- Retention corner card: "Your next step" (Cut 4 step 4) ---
const NEXT_STEP_DISMISSED_KEY = 'okg-next-step-dismissed';
const SEED_COMPLETED_KEY = 'okg-seed-completed';

function shouldShowNextStep() {{
  try {{
    if (sessionStorage.getItem(NEXT_STEP_DISMISSED_KEY) === '1') return false;
  }} catch (e) {{}}
  try {{
    if (localStorage.getItem(SEED_COMPLETED_KEY) === '1') return true;
  }} catch (e) {{}}
  if (typeof OKGFluency === 'undefined') return false;
  var goals = OKGFluency.loadGoals() || [];
  return goals.length > 0;
}}

function computeNextStep() {{
  if (typeof OKGFluency === 'undefined') return null;
  if (!fluencyGraph) fluencyGraph = buildFluencyGraph();
  if (!effectiveScores) {{
    // Mirror refreshFluency's propagate + floor apply without triggering draw loops
    effectiveScores = OKGFluency.propagate(fluencyGraph);
    data.nodes.forEach(function (n) {{
      var floor = OKGFluency.computeFloor(n.stageInt, n.domain);
      if (floor > (effectiveScores[n.id] || 0)) effectiveScores[n.id] = floor;
    }});
    frontierSet = new Set(OKGFluency.findFrontier(fluencyGraph, effectiveScores));
  }}

  // Stale topics take priority: if the user has touched-then-drifted work
  // sitting in the 50-85 fluency band for >3 weeks, surface the oldest first.
  var staleIds = OKGFluency.findStaleTopics ? OKGFluency.findStaleTopics() : [];
  if (staleIds.length > 0) {{
    for (var si = 0; si < staleIds.length; si++) {{
      var stnode = nodeMap[staleIds[si]];
      if (stnode) return {{node: stnode, reason: 'review'}};
    }}
  }}

  var goals = OKGFluency.loadGoals() || [];
  var onPath = {{}};
  if (goals.length > 0) {{
    var storedScores = OKGFluency.loadScores();
    for (var gi = 0; gi < goals.length; gi++) {{
      var path = OKGFluency.computePathToGoal(fluencyGraph, storedScores, goals[gi]) || [];
      for (var pi = 0; pi < path.length; pi++) onPath[path[pi]] = true;
    }}
  }}

  var frontierIds = OKGFluency.findFrontier(fluencyGraph, effectiveScores) || [];
  var best = null, bestScore = -Infinity;
  var cap = Math.min(50, frontierIds.length);
  for (var i = 0; i < cap; i++) {{
    var nid = frontierIds[i];
    var fnode = fluencyGraph[nid];
    if (!fnode) continue;
    var prereqs = fnode.prereqs || [];
    var prereqAvg = 100;
    if (prereqs.length > 0) {{
      var sum = 0;
      for (var k = 0; k < prereqs.length; k++) sum += (effectiveScores[prereqs[k]] || 0);
      prereqAvg = sum / prereqs.length;
    }}
    var outDegree = (fnode.successors || []).length;
    var logConn = Math.log(1 + outDegree);
    var goalBonus = onPath[nid] ? 2.0 : 1.0;
    var score = prereqAvg * logConn * goalBonus;
    if (score > bestScore) {{ bestScore = score; best = nid; }}
  }}
  if (!best) return null;
  return {{node: nodeMap[best] || null, reason: 'next'}};
}}

function updateNextStepCard() {{
  var card = document.getElementById('nextStepCard');
  if (!card) return;
  if (!shouldShowNextStep()) {{
    card.classList.add('ns-hidden');
    return;
  }}
  var result = computeNextStep();
  if (!result || !result.node) {{
    card.classList.add('ns-hidden');
    return;
  }}
  var node = result.node;
  var reason = result.reason || 'next';
  var labelEl = document.querySelector('#nextStepCard .ns-label');
  var startEl = document.getElementById('nsStart');
  if (reason === 'review') {{
    if (labelEl) labelEl.textContent = 'Review this';
    if (startEl) startEl.textContent = 'Review';
  }} else {{
    if (labelEl) labelEl.textContent = 'Your next step';
    if (startEl) startEl.textContent = 'Start this';
  }}
  document.getElementById('nsTitle').textContent = node.title;
  var meta = node.course ? node.course.replace(/-/g, ' ') : (node.domain || '').replace(/-/g, ' ');
  document.getElementById('nsMeta').textContent = meta;
  if (startEl) startEl.href = 'topics/' + node.id + '.html';
  card.classList.remove('ns-hidden');
}}

function hideNextStepCard() {{
  var card = document.getElementById('nextStepCard');
  if (card) card.classList.add('ns-hidden');
  try {{ sessionStorage.setItem(NEXT_STEP_DISMISSED_KEY, '1'); }} catch (e) {{}}
}}

if (!isSproutMode) {{ updateNextStepCard(); }}

// --- Refine your map ---
function priorToPosition(prior) {{
  var best = 2, minDiff = Infinity;
  for (var i = 0; i < REFINE_POSITIONS.length; i++) {{
    var diff = Math.abs(REFINE_POSITIONS[i].mul - prior);
    if (diff < minDiff) {{ minDiff = diff; best = i; }}
  }}
  return best;
}}

function showRefineCard() {{
  var stageCard = document.getElementById('stageCard');
  if (stageCard) stageCard.classList.add('stage-hidden');
  var card = document.getElementById('refineCard');
  if (!card) return;
  card.classList.remove('refine-hidden');
  initRefineSliders();
}}

function hideRefineCard() {{
  var card = document.getElementById('refineCard');
  if (card) card.classList.add('refine-hidden');
  if (typeof OKGFluency !== 'undefined') {{
    if (typeof showFluency !== 'undefined' && !showFluency) {{
      toggleFluency();
    }} else {{
      refreshFluency();
      draw();
    }}
  }}
}}

function initRefineSliders() {{
  if (typeof OKGFluency === 'undefined') return;
  var container = document.getElementById('refineRows');
  if (!container || container.children.length > 0) return;  // already built
  var current = OKGFluency.getDomainPrior() || {{}};

  REFINE_DOMAINS.forEach(function (pair) {{
    var slug = pair[0], label = pair[1];
    var pos = (current[slug] != null) ? priorToPosition(current[slug]) : 2;

    var row = document.createElement('div');
    row.className = 'refine-row';

    var labelEl = document.createElement('span');
    labelEl.className = 'refine-label';
    labelEl.textContent = label;

    var input = document.createElement('input');
    input.type = 'range';
    input.min = '0'; input.max = '4'; input.step = '1';
    input.value = String(pos);
    input.setAttribute('data-domain', slug);

    var value = document.createElement('span');
    value.className = 'refine-value';
    value.id = 'rv-' + slug;
    value.textContent = REFINE_POSITIONS[pos].label;

    row.appendChild(labelEl);
    row.appendChild(input);
    row.appendChild(value);
    container.appendChild(row);

    input.addEventListener('input', function () {{
      var p = parseInt(this.value, 10);
      document.getElementById('rv-' + slug).textContent = REFINE_POSITIONS[p].label;
      var priors = OKGFluency.getDomainPrior() || {{}};
      priors[slug] = REFINE_POSITIONS[p].mul;
      OKGFluency.setDomainPrior(priors);
    }});
  }});

  // Stop canvas drag/pan from eating events inside the card
  var card = document.getElementById('refineCard');
  if (card) {{
    ['mousedown', 'touchstart', 'touchmove', 'wheel'].forEach(function (ev) {{
      card.addEventListener(ev, function (e) {{ e.stopPropagation(); }}, {{ passive: true }});
    }});
  }}
}}

// --- Sprout shell functions (Phase 12B Cut 7) ---
// Only active when isSproutMode. Runs after all other definitions so it can
// reference buildFluencyGraph / loadScores freely without hoisting concerns.
// Merged metadata: [label, hue] per pre-formal domain.
const SPROUT_META = {{
  'arts-and-aesthetics':          ['Art',      62],
  'biology':                      ['Life',    130],
  'earth-and-space-sciences':     ['Earth',   195],
  'health-and-human-development': ['Body',    345],
  'language-and-communication':   ['Words',    25],
  'literature':                   ['Stories',   5],
  'mathematics':                  ['Math',    210],
  'music':                        ['Music',   214],
  'psychology':                   ['Feelings',300],
}};
const SPROUT_DOMAINS = Object.keys(SPROUT_META);

var sproutCurrentTopic = null;
var sproutMuted = false;

function pickSproutTopic() {{
  if (!data.sproutTopics || data.sproutTopics.length === 0) return null;
  var scores = (typeof OKGFluency !== 'undefined') ? OKGFluency.loadScores() : {{}};
  var unseen = data.sproutTopics.filter(function (t) {{
    var s = scores[t.id];
    return s === undefined || s < 50;
  }});
  var pool = unseen.length > 0 ? unseen : data.sproutTopics;
  return pool[Math.floor(Math.random() * pool.length)];
}}

function speakSprout(text) {{
  if (sproutMuted) return;
  if (typeof window.speechSynthesis === 'undefined') return;
  try {{
    window.speechSynthesis.cancel();
    var utter = new SpeechSynthesisUtterance(text);
    utter.rate = 0.9;
    utter.pitch = 1.1;
    window.speechSynthesis.speak(utter);
  }} catch (e) {{}}
}}

function renderSproutShell() {{
  var shell = document.getElementById('sproutShell');
  if (!shell) return;
  shell.classList.remove('sprout-hidden');
  var topic = pickSproutTopic();
  if (!topic) return;
  sproutCurrentTopic = topic;
  // HERO_IMAGE_RETROFIT: replace emoji with per-topic hero image once Persona A
  // testers exist. See plans/phase-12-three-persona-redesign.md Cut 7 dialectic.
  document.getElementById('sproutEmoji').textContent = topic.emoji || '🌱';
  document.getElementById('sproutTitle').textContent = topic.title;
  document.getElementById('sproutCore').textContent = topic.coreIdea || '';
  speakSprout(topic.title + '. ' + (topic.coreIdea || ''));
  renderColoringBook();
}}

function sproutResponse(answer) {{
  if (!sproutCurrentTopic || typeof OKGFluency === 'undefined') return;
  var score = answer === 'know' ? 90 : (answer === 'kinda' ? 60 : 20);
  OKGFluency.setScore(sproutCurrentTopic.id, score);
  renderSproutShell();
}}

function renderColoringBook() {{
  var svg = document.getElementById('sproutColoringBook');
  if (!svg) return;
  while (svg.firstChild) svg.removeChild(svg.firstChild);
  var scores = (typeof OKGFluency !== 'undefined') ? OKGFluency.loadScores() : {{}};

  var domainTotal = {{}}, domainProgress = {{}};
  for (var i = 0; i < SPROUT_DOMAINS.length; i++) {{
    domainTotal[SPROUT_DOMAINS[i]] = 0;
    domainProgress[SPROUT_DOMAINS[i]] = 0;
  }}
  (data.sproutTopics || []).forEach(function (t) {{
    if (domainTotal[t.domain] == null) return;
    domainTotal[t.domain] += 1;
    var s = scores[t.id];
    if (s != null && s >= 70) domainProgress[t.domain] += 1;
  }});

  var n = SPROUT_DOMAINS.length;
  var outerR = 90, innerR = 22;
  for (var k = 0; k < n; k++) {{
    var d = SPROUT_DOMAINS[k];
    var a0 = (k / n) * Math.PI * 2 - Math.PI / 2;
    var a1 = ((k + 1) / n) * Math.PI * 2 - Math.PI / 2;
    var total = domainTotal[d] || 1;
    var progress = domainProgress[d] || 0;
    var frac = Math.min(1, progress / total);
    appendSproutWedge(svg, a0, a1, innerR, outerR, '#e8e8f0');
    if (frac > 0) {{
      var fillR = innerR + (outerR - innerR) * frac;
      appendSproutWedge(svg, a0, a1, innerR, fillR, 'hsl(' + ((SPROUT_META[d] || [,0])[1]) + ', 65%, 62%)');
    }}
    var midA = (a0 + a1) / 2;
    var lr = outerR + 10;
    var label = document.createElementNS('http://www.w3.org/2000/svg', 'text');
    label.setAttribute('class', 'wedge-label');
    label.setAttribute('x', (Math.cos(midA) * lr).toFixed(1));
    label.setAttribute('y', (Math.sin(midA) * lr + 3).toFixed(1));
    label.textContent = (SPROUT_META[d] || [d])[0];
    svg.appendChild(label);
  }}
}}

function appendSproutWedge(svg, a0, a1, r0, r1, fill) {{
  var x0o = Math.cos(a0) * r1, y0o = Math.sin(a0) * r1;
  var x1o = Math.cos(a1) * r1, y1o = Math.sin(a1) * r1;
  var x0i = Math.cos(a0) * r0, y0i = Math.sin(a0) * r0;
  var x1i = Math.cos(a1) * r0, y1i = Math.sin(a1) * r0;
  var large = (a1 - a0) > Math.PI ? 1 : 0;
  var path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
  var pathD = 'M ' + x0o.toFixed(1) + ' ' + y0o.toFixed(1)
    + ' A ' + r1 + ' ' + r1 + ' 0 ' + large + ' 1 ' + x1o.toFixed(1) + ' ' + y1o.toFixed(1)
    + ' L ' + x1i.toFixed(1) + ' ' + y1i.toFixed(1)
    + ' A ' + r0 + ' ' + r0 + ' 0 ' + large + ' 0 ' + x0i.toFixed(1) + ' ' + y0i.toFixed(1)
    + ' Z';
  path.setAttribute('d', pathD);
  path.setAttribute('class', 'wedge');
  path.setAttribute('fill', fill);
  svg.appendChild(path);
}}

function toggleSproutTTS() {{
  sproutMuted = !sproutMuted;
  var btn = document.querySelector('.sprout-mute');
  if (btn) btn.textContent = sproutMuted ? '🔇' : '🔊';
  if (sproutMuted && typeof window.speechSynthesis !== 'undefined') {{
    window.speechSynthesis.cancel();
  }}
}}

// --- Parent PIN (opt-in, SHA-256 via SubtleCrypto) ---
function sproutSha256(text) {{
  if (!(window.crypto && window.crypto.subtle)) return Promise.resolve('');
  var enc = new TextEncoder().encode(text);
  return window.crypto.subtle.digest('SHA-256', enc).then(function (buf) {{
    var arr = Array.from(new Uint8Array(buf));
    return arr.map(function (b) {{ return b.toString(16).padStart(2, '0'); }}).join('');
  }});
}}

function hasParentPin() {{
  try {{ return !!localStorage.getItem(SPROUT_PIN_HASH_KEY); }} catch (e) {{ return false; }}
}}

function sproutPinUnlocked() {{
  try {{ return sessionStorage.getItem(SPROUT_PIN_SESSION_KEY) === '1'; }} catch (e) {{ return false; }}
}}

function openParentPin() {{
  var modal = document.getElementById('sproutPinModal');
  if (!modal) return;
  var titleEl = document.getElementById('sproutPinTitle');
  var descEl = document.getElementById('sproutPinDesc');
  var errEl = document.getElementById('sproutPinError');
  var input = document.getElementById('sproutPinInput');
  if (errEl) {{ errEl.textContent = ''; errEl.style.color = ''; }}
  if (input) input.value = '';
  if (hasParentPin()) {{
    titleEl.textContent = 'Enter parent PIN';
    descEl.textContent = 'Enter your 4-digit PIN to unlock parent settings and leave Sprout mode.';
  }} else {{
    titleEl.textContent = 'Set a parent PIN';
    descEl.textContent = 'Create a 4-digit PIN to lock this screen so your child stays in Sprout mode. Optional — leave blank and press Cancel to skip.';
  }}
  modal.classList.remove('sprout-pin-hidden');
  if (input) setTimeout(function () {{ input.focus(); }}, 50);
}}

function closeParentPin() {{
  var modal = document.getElementById('sproutPinModal');
  if (modal) modal.classList.add('sprout-pin-hidden');
}}

function submitParentPin() {{
  var input = document.getElementById('sproutPinInput');
  var errEl = document.getElementById('sproutPinError');
  if (!input || !errEl) return;
  var pin = input.value.trim();
  if (hasParentPin()) {{
    if (!/^\d{{4}}$/.test(pin)) {{ errEl.textContent = 'Enter your 4-digit PIN.'; return; }}
    sproutSha256(pin).then(function (h) {{
      var stored = '';
      try {{ stored = localStorage.getItem(SPROUT_PIN_HASH_KEY) || ''; }} catch (e) {{}}
      if (h && h === stored) {{
        try {{ sessionStorage.setItem(SPROUT_PIN_SESSION_KEY, '1'); }} catch (e) {{}}
        closeParentPin();
        exitSproutToMap();
      }} else {{
        errEl.textContent = 'Wrong PIN.';
      }}
    }});
  }} else {{
    if (pin === '') {{ closeParentPin(); return; }}
    if (!/^\d{{4}}$/.test(pin)) {{ errEl.textContent = 'PIN must be 4 digits.'; return; }}
    sproutSha256(pin).then(function (h) {{
      try {{ localStorage.setItem(SPROUT_PIN_HASH_KEY, h); }} catch (e) {{}}
      closeParentPin();
    }});
  }}
}}

function exitSproutToMap() {{
  if (hasParentPin() && !sproutPinUnlocked()) {{
    openParentPin();
    return;
  }}
  var url = new URL(window.location.href);
  url.searchParams.delete('preset');
  window.location.href = url.toString();
}}

if (isSproutMode) {{
  // Hide adult-mode surfaces so Sprout is the only thing visible.
  ['canvas', 'stats', 'nav', 'controls', 'search', 'tooltip', 'panel',
   'stageCard', 'refineCard', 'nextStepCard'].forEach(function (id) {{
    var el = document.getElementById(id);
    if (el) el.style.display = 'none';
  }});
  renderSproutShell();
}}

// ?focus=<topic-id> deep link (topic pages' "See this on the map" button):
// center the camera on the topic, select it, open its panel. ?ancestry=<id>
// additionally fires the A3 reveal on arrival (B4 shareable subgraph URLs).
(function () {{
  if (isSproutMode) return;
  var params = new URLSearchParams(window.location.search);
  // ?path=<a>,<b> — two-topic relationship surface (bridge or no-path fallback).
  var pathParam = params.get('path');
  if (pathParam) {{
    var ids = pathParam.split(',').map(function (s) {{ return s.trim(); }});
    if (ids.length === 2 && nodeMap[ids[0]] && nodeMap[ids[1]]) {{
      revealPath(ids[0], ids[1]);
      return;
    }}
  }}
  var ancestryId = params.get('ancestry');
  var targetId = ancestryId || params.get('focus');
  if (!targetId) return;
  var node = nodeMap[targetId];
  if (!node) return;
  centerOnNode(node, ancestryId ? 3.5 : 5);
  selectedNode = node;
  hoveredNode = node;
  draw();
  showPanel(node, W / 2, H / 2);
  if (ancestryId) revealAncestry(node.id, 4);
}})();

</script>
</body>
</html>"""


def main():
    parser = argparse.ArgumentParser(description="Radial knowledge graph visualization")
    parser.add_argument("--output", help="Output file path")
    parser.add_argument("--with-origins", action="store_true",
                        help="PRIVATE variant: include the origin-layer capacities as a central hub")
    args = parser.parse_args()

    print("Loading topics...")
    all_data = load_all_topics(include_caps=args.with_origins)
    configs = load_domain_configs()
    print(f"Loaded {len(all_data)} topics across {len(configs)} domains")

    print("Computing depths...")
    depths = compute_depths(all_data)
    local_depths = compute_domain_local_depths(all_data)

    print("Computing radial layout...")
    positions, sectors, domain_order = build_radial_layout(all_data, configs, local_depths)

    print("Generating HTML...")
    html = generate_radial_html(all_data, configs, depths, positions, sectors, domain_order)

    default_name = "radial-with-origins.html" if args.with_origins else "radial-graph.html"
    out = Path(args.output) if args.output else OUTPUT_DIR / default_name
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    print(f"Saved: {out}")

    # Copy fluency.js to output
    fluency_src = ROOT / "lib" / "fluency.js"
    if fluency_src.exists():
        fluency_dst = OUTPUT_DIR / "js" / "fluency.js"
        fluency_dst.parent.mkdir(parents=True, exist_ok=True)
        import shutil
        shutil.copy2(fluency_src, fluency_dst)

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
