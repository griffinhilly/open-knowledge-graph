#!/usr/bin/env python3
"""Fix orphan and island topics by adding soft prerequisite edges.

For each orphan (no prereqs, nothing depends on it) and each island component
(disconnected from the main graph), find an appropriate topic to link to and
add it as a soft prerequisite.

Usage:
    python tools/fix_orphans_islands.py
    python tools/fix_orphans_islands.py --dry-run   # Preview without writing
"""

import sys
import io
import re
import json
import argparse
from pathlib import Path
from collections import defaultdict

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML required. Install with: pip install pyyaml")
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent
DOMAINS_DIR = ROOT / "domains"

# Stage ordering for comparison (lower = earlier/more foundational)
STAGE_ORDER = {
    "pre-formal": 0,
    "concrete-operations": 1,
    "abstract-reasoning": 2,
    "formal-systems": 3,
    "advanced": 4,
    "expert": 5,
}

# Domain affinity: domains that share conceptual overlap get bonus points
# when making cross-domain connections. Higher = more related.
DOMAIN_AFFINITY = {
    ("arts-and-aesthetics", "philosophy"): 40,
    ("arts-and-aesthetics", "history"): 30,
    ("arts-and-aesthetics", "literature"): 25,
    ("arts-and-aesthetics", "psychology"): 15,
    ("arts-and-aesthetics", "music"): 20,
    ("computer-science", "formal-sciences-and-logic"): 35,
    ("computer-science", "mathematics"): 30,
    ("computer-science", "engineering"): 20,
    ("engineering", "physics"): 30,
    ("engineering", "mathematics"): 25,
    ("engineering", "chemistry"): 15,
    ("physics", "mathematics"): 30,
    ("physics", "chemistry"): 20,
    ("physics", "earth-and-space-sciences"): 15,
    ("chemistry", "biology"): 20,
    ("biology", "health-and-human-development"): 25,
    ("biology", "chemistry"): 20,
    ("psychology", "social-sciences"): 25,
    ("psychology", "philosophy"): 20,
    ("psychology", "health-and-human-development"): 20,
    ("economics", "social-sciences"): 25,
    ("economics", "mathematics"): 15,
    ("history", "social-sciences"): 20,
    ("history", "philosophy"): 15,
    ("language-and-communication", "literature"): 25,
    ("language-and-communication", "philosophy"): 15,
    ("literature", "history"): 15,
    ("literature", "philosophy"): 20,
    ("music", "physics"): 10,
    ("music", "mathematics"): 10,
    ("practical-life-skills", "economics"): 10,
    ("social-sciences", "philosophy"): 20,
    ("social-sciences", "history"): 20,
    ("health-and-human-development", "psychology"): 20,
}


def get_domain_affinity(domain_a, domain_b):
    """Get affinity score between two domains (symmetric)."""
    if domain_a == domain_b:
        return 50
    return max(
        DOMAIN_AFFINITY.get((domain_a, domain_b), 0),
        DOMAIN_AFFINITY.get((domain_b, domain_a), 0),
    )


def parse_frontmatter(filepath):
    """Extract YAML frontmatter and body from a Markdown file."""
    text = filepath.read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not match:
        return None, "", text
    try:
        data = yaml.safe_load(match.group(1))
    except yaml.YAMLError:
        return None, "", text
    body = text[match.end():]
    return data, body, text


def load_all_topics():
    """Parse every topic file. Returns dict keyed by topic ID."""
    all_data = {}
    for filepath in sorted(DOMAINS_DIR.rglob("*.md")):
        if filepath.name.startswith("_"):
            continue
        data, body, full_text = parse_frontmatter(filepath)
        if data is None or "id" not in data:
            continue
        tid = data["id"]
        data["_filepath"] = str(filepath)
        all_data[tid] = data
    return all_data


def build_graphs(all_data):
    """Build prerequisite and reverse-dependency graphs."""
    prereq_of = defaultdict(list)
    depended_by = defaultdict(list)
    for tid, data in all_data.items():
        for p in data.get("prerequisites", []):
            if isinstance(p, dict) and "id" in p:
                pid = p["id"]
                if pid in all_data:
                    prereq_of[tid].append(pid)
                    depended_by[pid].append(tid)
    return prereq_of, depended_by


def find_components(all_data, prereq_of):
    """Find weakly-connected components using undirected BFS.
    Returns list of sets, sorted largest-first."""
    adj = defaultdict(set)
    all_ids = set(all_data.keys())
    for tid in all_ids:
        for pid in prereq_of.get(tid, []):
            adj[tid].add(pid)
            adj[pid].add(tid)

    visited = set()
    components = []
    for start in sorted(all_ids):
        if start in visited:
            continue
        component = set()
        stack = [start]
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            component.add(node)
            for neighbor in adj[node]:
                if neighbor not in visited:
                    stack.append(neighbor)
        components.append(component)

    components.sort(key=len, reverse=True)
    return components


def score_prerequisite_candidate(candidate_data, target_data, in_degree):
    """Score a candidate topic as a prerequisite for the target topic.
    Higher score = better candidate.
    """
    score = 0
    cid = candidate_data["id"]
    cand_domain = candidate_data.get("domain", "")
    target_domain = target_data.get("domain", "")

    # Same course is strongly preferred
    if candidate_data.get("course") == target_data.get("course"):
        score += 100

    # Same domain but different course
    elif cand_domain == target_domain:
        score += 50

    # Cross-domain: use affinity scoring
    else:
        affinity = get_domain_affinity(cand_domain, target_domain)
        score += affinity  # 0-40 based on domain relatedness

    # Tag overlap: shared tags indicate conceptual connection
    cand_tags = set(candidate_data.get("tags", []) or [])
    target_tags = set(target_data.get("tags", []) or [])
    if cand_tags and target_tags:
        overlap = len(cand_tags & target_tags)
        score += overlap * 10  # Each shared tag = 10 points

    # Earlier or same stage preferred (foundational topics)
    target_stage = STAGE_ORDER.get(target_data.get("stage", ""), 2)
    cand_stage = STAGE_ORDER.get(candidate_data.get("stage", ""), 2)

    if cand_stage < target_stage:
        score += 30  # Earlier stage = more foundational
    elif cand_stage == target_stage:
        score += 15  # Same stage = reasonable peer
    else:
        score -= 20  # Later stage = probably wrong direction

    # Higher in-degree = more foundational (more things depend on it)
    score += min(in_degree.get(cid, 0), 30)  # Cap at 30 to avoid domination

    # Fewer prerequisites = more foundational
    prereqs = candidate_data.get("prerequisites", [])
    if isinstance(prereqs, list):
        num_prereqs = len([p for p in prereqs if isinstance(p, dict)])
    else:
        num_prereqs = 0
    if num_prereqs == 0:
        score += 10  # Root topic bonus
    elif num_prereqs <= 3:
        score += 5

    return score


def find_best_prereq(target_id, target_data, candidate_pool, all_data,
                     in_degree, exclude_ids=None):
    """Find the best prerequisite from candidate_pool for target topic.
    Returns (best_id, best_score) or (None, -1).
    """
    if exclude_ids is None:
        exclude_ids = set()

    domain = target_data.get("domain", "")
    course = target_data.get("course", "")

    # Tier candidates: same course > same domain > related domain > other
    same_course = []
    same_domain = []
    related_domain = []

    for cid in candidate_pool:
        if cid == target_id or cid in exclude_ids:
            continue
        if cid not in all_data:
            continue
        cdata = all_data[cid]
        cdomain = cdata.get("domain", "")
        if cdata.get("course") == course:
            same_course.append(cid)
        elif cdomain == domain:
            same_domain.append(cid)
        elif get_domain_affinity(cdomain, domain) > 0:
            related_domain.append(cid)

    # Score candidates in priority tiers
    best_id = None
    best_score = -999

    for tier in [same_course, same_domain, related_domain]:
        if not tier:
            continue
        for cid in tier:
            cdata = all_data[cid]
            score = score_prerequisite_candidate(cdata, target_data, in_degree)
            if score > best_score:
                best_score = score
                best_id = cid
        if best_id is not None:
            break

    # If no related domain found, fall back to any candidate but use
    # top-scoring hubs only (limit search to top 200 by in-degree)
    if best_id is None:
        hub_candidates = sorted(
            [cid for cid in candidate_pool
             if cid != target_id and cid not in exclude_ids
             and cid in all_data],
            key=lambda x: in_degree.get(x, 0),
            reverse=True
        )[:200]
        for cid in hub_candidates:
            cdata = all_data[cid]
            score = score_prerequisite_candidate(cdata, target_data, in_degree)
            if score > best_score:
                best_score = score
                best_id = cid

    return best_id, best_score


def add_prerequisite_to_file(filepath, prereq_id, dry_run=False):
    """Add a soft prerequisite to a topic file's frontmatter.
    Returns True if modification was made (or would be made in dry-run).
    """
    text = Path(filepath).read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not match:
        print(f"  WARNING: Could not parse frontmatter in {filepath}",
              file=sys.stderr)
        return False

    fm_text = match.group(1)
    body = text[match.end():]

    # Parse existing frontmatter to check for duplicates
    data = yaml.safe_load(fm_text)
    if data is None:
        return False

    existing_prereqs = data.get("prerequisites", [])
    if isinstance(existing_prereqs, list):
        for p in existing_prereqs:
            if isinstance(p, dict) and p.get("id") == prereq_id:
                return False  # Already has this prerequisite

    new_prereq_entry = f"- id: {prereq_id}\n  type: soft"

    if "prerequisites: []" in fm_text:
        # Empty list -> replace with new prerequisite
        new_fm = fm_text.replace(
            "prerequisites: []",
            f"prerequisites:\n{new_prereq_entry}"
        )
    elif re.search(r"^prerequisites:\s*$", fm_text, re.MULTILINE):
        # Bare "prerequisites:" key -- check for existing entries on next lines
        lines = fm_text.split("\n")
        new_lines = []
        inserted = False
        for i, line in enumerate(lines):
            new_lines.append(line)
            if not inserted and re.match(r"^prerequisites:\s*$", line):
                # Check if next line has existing entries
                if (i + 1 < len(lines)
                        and lines[i + 1].startswith("- ")):
                    # Has existing entries -- find end of block, append there
                    j = i + 1
                    while j < len(lines) and (
                            lines[j].startswith("- ")
                            or lines[j].startswith("  ")):
                        new_lines.append(lines[j])
                        j += 1
                    new_lines.append(new_prereq_entry)
                    new_lines.extend(lines[j:])
                    inserted = True
                    break
                else:
                    new_lines.append(new_prereq_entry)
                    inserted = True
        new_fm = "\n".join(new_lines)
    elif "prerequisites:" in fm_text:
        # Has prerequisites with existing entries
        lines = fm_text.split("\n")
        new_lines = []
        in_prereqs = False
        inserted = False
        for i, line in enumerate(lines):
            if not inserted and re.match(r"^prerequisites:", line):
                in_prereqs = True
                new_lines.append(line)
                continue
            if in_prereqs and not inserted:
                if line.startswith("- ") or line.startswith("  "):
                    new_lines.append(line)
                    # Check if next line exits the block
                    if (i + 1 >= len(lines) or (
                            not lines[i + 1].startswith("- ")
                            and not lines[i + 1].startswith("  "))):
                        new_lines.append(new_prereq_entry)
                        inserted = True
                        in_prereqs = False
                else:
                    new_lines.append(new_prereq_entry)
                    new_lines.append(line)
                    inserted = True
                    in_prereqs = False
            else:
                new_lines.append(line)
        if in_prereqs and not inserted:
            new_lines.append(new_prereq_entry)
        new_fm = "\n".join(new_lines)
    else:
        # No prerequisites field -- add after course
        lines = fm_text.split("\n")
        new_lines = []
        inserted = False
        for line in lines:
            new_lines.append(line)
            if not inserted and line.startswith("course:"):
                new_lines.append(f"prerequisites:\n{new_prereq_entry}")
                inserted = True
        if not inserted:
            new_lines.append(f"prerequisites:\n{new_prereq_entry}")
        new_fm = "\n".join(new_lines)

    new_text = f"---\n{new_fm}\n---\n{body}"

    if dry_run:
        return True

    Path(filepath).write_text(new_text, encoding="utf-8")
    return True


def main():
    parser = argparse.ArgumentParser(
        description="Fix orphan and island topics")
    parser.add_argument("--dry-run", action="store_true",
                        help="Preview changes without writing files")
    args = parser.parse_args()

    # Load QA report
    qa_path = ROOT / "tools" / "qa_report.json"
    print(f"Loading QA report from {qa_path}...")
    with open(qa_path, "r", encoding="utf-8") as f:
        qa_report = json.load(f)

    orphans_list = qa_report["orphans"]
    islands_data = qa_report["islands"]

    print(f"QA report: {len(orphans_list)} orphans, "
          f"{len(islands_data)} domains with island components")

    # Load all topics and build graphs
    print("Loading all topics...")
    all_data = load_all_topics()
    print(f"Loaded {len(all_data)} topics")

    prereq_of, depended_by = build_graphs(all_data)

    # Compute in-degree for scoring
    in_degree = {tid: len(deps) for tid, deps in depended_by.items()}

    # Find GLOBAL connected components
    print("Finding connected components...")
    components = find_components(all_data, prereq_of)
    main_component = components[0]
    island_components = components[1:]

    print(f"Main component: {len(main_component)} topics")
    print(f"Island components: {len(island_components)} "
          f"(total {sum(len(c) for c in island_components)} topics)")

    # Build lookup: topic_id -> component index
    topic_to_comp_idx = {}
    for i, comp in enumerate(components):
        for tid in comp:
            topic_to_comp_idx[tid] = i

    # Track all changes
    changes = []
    skipped = []
    # Track which topics we've already fixed (to avoid double-processing)
    fixed_topics = set()

    # ========== PHASE 1: Fix orphans ==========
    print(f"\n{'='*60}")
    print(f"PHASE 1: Fixing {len(orphans_list)} orphan topics")
    print(f"{'='*60}")

    orphan_ids = set(o["id"] for o in orphans_list)

    for orphan in orphans_list:
        oid = orphan["id"]
        if oid not in all_data:
            skipped.append((oid, "not found in loaded topics"))
            continue

        odata = all_data[oid]

        # Find best prerequisite from the main component
        best_id, best_score = find_best_prereq(
            oid, odata, main_component, all_data, in_degree,
            exclude_ids=orphan_ids
        )

        if best_id is None:
            skipped.append((oid, "no candidates found"))
            continue

        filepath = odata["_filepath"]
        success = add_prerequisite_to_file(filepath, best_id,
                                           dry_run=args.dry_run)

        if success:
            best_data = all_data[best_id]
            action = "WOULD ADD" if args.dry_run else "ADDED"
            print(f"  {action}: {oid}")
            print(f"    <- {best_id} (score={best_score}, "
                  f"course={best_data.get('course')}, "
                  f"stage={best_data.get('stage')}, "
                  f"in-degree={in_degree.get(best_id, 0)})")
            changes.append({
                "topic": oid,
                "added_prereq": best_id,
                "type": "orphan",
                "score": best_score,
            })
            fixed_topics.add(oid)
        else:
            skipped.append((oid, "file modification failed or already exists"))

    # ========== PHASE 2: Fix island components ==========
    print(f"\n{'='*60}")
    print(f"PHASE 2: Fixing {len(island_components)} island components")
    print(f"{'='*60}")

    for comp_idx, island_comp in enumerate(island_components):
        # Check if any topic in this component was already fixed as an orphan
        already_fixed = [tid for tid in island_comp if tid in fixed_topics]
        if already_fixed:
            print(f"  Component {comp_idx+1} (size={len(island_comp)}): "
                  f"already connected via orphan fix of {already_fixed[0]}")
            continue

        # Get domain info for display
        domain_counts = defaultdict(int)
        for tid in island_comp:
            domain_counts[all_data[tid].get("domain", "?")] += 1
        primary_domain = max(domain_counts, key=domain_counts.get)
        sample = sorted(island_comp)[:3]

        # Find the best bridge: for each topic in the island, find its best
        # prereq from the main component, then pick the pair with best score
        best_bridge = None
        best_bridge_prereq = None
        best_bridge_score = -999

        for tid in island_comp:
            if tid not in all_data:
                continue
            tdata = all_data[tid]

            prereq_id, prereq_score = find_best_prereq(
                tid, tdata, main_component, all_data, in_degree
            )

            if prereq_id is None:
                continue

            # Prefer bridge topics with fewer existing prereqs (cleaner link)
            existing = len(prereq_of.get(tid, []))
            adjusted = prereq_score - (existing * 5)

            if adjusted > best_bridge_score:
                best_bridge_score = adjusted
                best_bridge = tid
                best_bridge_prereq = prereq_id

        if best_bridge is None or best_bridge_prereq is None:
            skipped.append(
                (f"island-comp-{comp_idx+1} ({primary_domain})",
                 f"no bridge candidate found for {sample}")
            )
            continue

        filepath = all_data[best_bridge]["_filepath"]
        success = add_prerequisite_to_file(filepath, best_bridge_prereq,
                                           dry_run=args.dry_run)

        if success:
            prereq_data = all_data[best_bridge_prereq]
            action = "WOULD ADD" if args.dry_run else "ADDED"
            print(f"  Component {comp_idx+1} (size={len(island_comp)}, "
                  f"domain={primary_domain}): {action}")
            print(f"    {best_bridge}")
            print(f"      <- {best_bridge_prereq} (score={best_bridge_score}, "
                  f"course={prereq_data.get('course')}, "
                  f"stage={prereq_data.get('stage')}, "
                  f"in-degree={in_degree.get(best_bridge_prereq, 0)})")
            changes.append({
                "topic": best_bridge,
                "added_prereq": best_bridge_prereq,
                "type": "island",
                "component_size": len(island_comp),
                "score": best_bridge_score,
                "domain": primary_domain,
            })
            fixed_topics.add(best_bridge)
        else:
            skipped.append(
                (f"island-{best_bridge}",
                 "file modification failed or prereq already exists")
            )

    # ========== Summary ==========
    print(f"\n{'='*60}")
    print("SUMMARY")
    print(f"{'='*60}")
    orphan_fixes = [c for c in changes if c["type"] == "orphan"]
    island_fixes = [c for c in changes if c["type"] == "island"]
    island_topics_connected = sum(
        c.get("component_size", 1) for c in island_fixes
    )

    action = "Would modify" if args.dry_run else "Modified"
    print(f"  {action} {len(changes)} topic files:")
    print(f"    Orphan fixes:  {len(orphan_fixes)} topics connected")
    print(f"    Island fixes:  {len(island_fixes)} edges added "
          f"(connecting {island_topics_connected} topics)")
    print(f"  Skipped: {len(skipped)}")
    for sid, reason in skipped:
        print(f"    - {sid}: {reason}")

    if args.dry_run:
        print(f"\n  (Dry run -- no files were modified. "
              f"Remove --dry-run to apply changes.)")

    return 0


if __name__ == "__main__":
    sys.exit(main())
