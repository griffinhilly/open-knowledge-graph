#!/usr/bin/env python3
"""Reconcile builds-toward / prerequisite mismatches in the Open Knowledge Graph.

Implements the decisions from the dialectic review:
- Tier 1: Fix 11 MERGE references, Remove 20+13 bad builds-toward entries
- Tier 2: Remove 13 cycle-creating builds-toward entries
- Tier 4: Add ~800-860 same-course soft prereqs (with filters)
- Tier 5: Add ~105 cross-course soft prereqs

Usage:
    python tools/reconcile.py --dry-run    # Show what would change
    python tools/reconcile.py --apply      # Apply changes
"""

import json
import re
import sys
from collections import defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DOMAINS_DIR = ROOT / "domains"

# ============================================================
# TIER 1: MERGE mappings (fix builds-toward to point at correct existing ID)
# ============================================================
MERGE_MAP = {
    "exponential-functions": "exponential-functions-and-graphs",
    "parallel-lines-transversals": "parallel-lines-and-transversals",
    "completing-the-square": "solving-quadratic-equations-completing-the-square",
    "complex-numbers": "complex-numbers-intro",
    "conic-sections": "conic-sections-overview",
    "continuity": "continuity-definition",
    "exponential-growth": "exponential-growth-and-decay",
    "histograms": "histograms-and-frequency-distributions",
    "rational-equations": "solving-rational-equations",
    "rational-functions": "graphing-rational-functions",
    "asymptotes": "rational-functions-and-asymptotes",
    # Additional merges from analysis
    "arithmetic-series": "arithmetic-sequences-and-series",
    "addition-within-1000": "three-digit-addition",
    "ratio-concept": "ratios",
    "number-line-integers": "integers-and-number-line",
    "transformations-of-functions": "function-transformations",
    "geometry-proofs": "coordinate-geometry-proofs",
    "distance-formula": "segment-and-distance",
    "precalculus-conics": "conic-sections-overview",
    "precalculus-polynomial-theory": "polynomial-division-review",
    "infinite-series": "series-definition-and-partial-sums",
    "calculus-limits": "limit-definition-intuitive",
    "calculus-derivatives": "derivative-as-slope-of-tangent",
    "calculus-integrals": "riemann-sums",
    "trigonometric-functions": "trigonometric-ratios-review",
    "geometry-angles": "angle-basics-and-classification",
    "volume-of-cylinders": "volume-of-prisms-and-cylinders",
    "geometry-area": "area-of-regular-polygons",
    "similar-figures": "similar-triangles-aa",
    "geometry-similarity": "similar-triangles-aa",
    "statistics-probability": "probability-axioms",
    "surface-area-prisms-cylinders": "surface-area-of-prisms",
    "narrative-arc-and-pacing": "narrative-pacing",
    "extended-metaphor-in-poetry": "allegory-and-extended-metaphor",
    "microbial-pathogenesis": "host-pathogen-interactions",
    "partial-products-multiplication-3rd": "estimation-in-multiplication",
    "statistics-descriptive": "measures-of-spread",
}

# ============================================================
# TIER 1 + 2: REMOVE these builds-toward targets entirely
# ============================================================
REMOVE_TARGETS = {
    # Tier 1: Vague/course-level references
    "algebra-2-rational-functions", "algebra-2-systems", "algebra-2-variation",
    "calculus-applications", "calculus-series",
    "linear-algebra-course", "probability-and-statistics-course",
    "precalculus-applications",
    "analytic-geometry", "data-analysis",
    "geometry-3d", "tolerance-and-error",
    "scientific-notation-operations",  # Will be created later; for now keep as dangling
    # Actually, let's NOT remove ones that will be created. Remove only truly vague ones.
}

# Recalculate: only remove the ones that are truly vague/course-level
REMOVE_TARGETS = {
    "algebra-2-rational-functions", "algebra-2-systems", "algebra-2-variation",
    "calculus-applications", "calculus-series",
    "linear-algebra-course", "probability-and-statistics-course",
    "precalculus-applications",
    "analytic-geometry", "data-analysis",
    "geometry-3d", "tolerance-and-error",
}

# ============================================================
# TIER 2: Cycle-creating builds-toward entries to remove
# ============================================================
CYCLE_REMOVALS = {
    "commutative-property-multiplication": "multiplication-facts-within-100",
    "medieval-mali-empire": "trans-saharan-trade",
    "naturalistic-observation": "reliability-in-measurement",
    "puberty-and-adolescent-physical-development": "adolescent-brain-and-behavioral-development",
    "shutdown-and-breakeven": "perfect-competition",
    "nash-equilibrium-microeconomics": "oligopoly-and-strategic-behavior",
    "f-test-joint-significance": "multiple-regression-model",
    "demand-curve-derivation": "price-elasticity-of-demand",
    "biostatistics-in-public-health": "epidemiologic-study-designs",
    "chain-rule-multivariable": "gradient-vector",
    "two-stage-least-squares": "causal-inference-econometrics",
    "paleography-and-document-reading": "source-criticism",
    "volcanoes-and-volcanism": "rock-cycle",
}

# ============================================================
# TIER 5: Cross-course dismissals (do NOT add these as prereqs)
# ============================================================
CROSS_COURSE_DISMISS = {
    ("cultural-diffusion-geography", "globalization-cultural-change"),
    ("demographic-transition-model", "urbanization-and-city-life"),
}


def parse_file(filepath):
    """Read file, extract frontmatter dict and full text."""
    text = filepath.read_text(encoding="utf-8")
    match = re.match(r"^(---\s*\n)(.*?\n)(---\s*\n)", text, re.DOTALL)
    if not match:
        return None, text
    try:
        data = yaml.safe_load(match.group(2))
    except yaml.YAMLError:
        return None, text
    return data, text


def rewrite_frontmatter(filepath, old_text, old_data, new_data):
    """Rewrite YAML frontmatter preserving the markdown body."""
    match = re.match(r"^---\s*\n.*?\n---\s*\n", old_text, re.DOTALL)
    if not match:
        return old_text
    body = old_text[match.end():]

    # Custom YAML dump that matches the project's style
    lines = ["---\n"]

    # Preserve field order from original
    field_order = ["id", "title", "domain", "course", "prerequisites",
                   "builds-toward", "tags", "aliases", "external-refs",
                   "stage", "status"]
    written = set()
    for field in field_order:
        if field in new_data:
            lines.append(dump_field(field, new_data[field]))
            written.add(field)
    # Any remaining fields
    for field in new_data:
        if field not in written:
            lines.append(dump_field(field, new_data[field]))

    lines.append("---\n")
    return "".join(lines) + body


def dump_field(key, value):
    """Dump a single YAML field in project style."""
    if key == "prerequisites":
        if not value:
            return "prerequisites: []\n"
        result = "prerequisites:\n"
        for prereq in value:
            result += f"- id: {prereq['id']}\n  type: {prereq['type']}\n"
        return result
    elif key == "builds-toward":
        if not value:
            return "builds-toward: []\n"
        result = "builds-toward:\n"
        for item in value:
            result += f"- {item}\n"
        return result
    elif key == "tags":
        if not value:
            return "tags: []\n"
        result = "tags:\n"
        for tag in value:
            result += f"- {tag}\n"
        return result
    elif key == "aliases":
        if not value:
            return "aliases: []\n"
        result = "aliases:\n"
        for alias in value:
            result += f"- {alias}\n"
        return result
    elif key == "external-refs":
        if not value:
            return "external-refs: []\n"
        result = "external-refs:\n"
        for ref in value:
            result += f"- title: {ref.get('title', '')}\n  url: {ref.get('url', '')}\n"
        return result
    elif isinstance(value, str) and (":" in value or "'" in value or '"' in value
                                      or value.startswith("{") or value.startswith("[")):
        # Quote strings that need it
        escaped = value.replace("'", "''")
        return f"{key}: '{escaped}'\n"
    else:
        return f"{key}: {value}\n"


def would_create_cycle(prereq_graph, source_id, target_id):
    """Check if adding source_id as prereq of target_id creates a cycle."""
    visited = set()
    stack = [source_id]
    while stack:
        node = stack.pop()
        if node == target_id:
            return True
        if node in visited:
            continue
        visited.add(node)
        for prereq in prereq_graph.get(node, []):
            stack.append(prereq)
    return False


def get_transitive_prereqs(prereq_graph, topic_id, cache):
    """Get all transitive prerequisites (memoized)."""
    if topic_id in cache:
        return cache[topic_id]
    result = set()
    for p in prereq_graph.get(topic_id, []):
        result.add(p)
        result |= get_transitive_prereqs(prereq_graph, p, cache)
    cache[topic_id] = result
    return result


def main():
    dry_run = "--dry-run" in sys.argv
    apply = "--apply" in sys.argv

    if not dry_run and not apply:
        print("Usage: python tools/reconcile.py --dry-run | --apply")
        return 1

    # ========== PHASE 1: Load all topics ==========
    all_data = {}
    all_paths = {}
    all_texts = {}
    prereq_graph = defaultdict(list)

    for filepath in sorted(DOMAINS_DIR.rglob("*.md")):
        data, text = parse_file(filepath)
        if data is None:
            continue
        topic_id = data.get("id")
        if not topic_id:
            continue
        all_data[topic_id] = data
        all_paths[topic_id] = filepath
        all_texts[topic_id] = text
        prereqs = data.get("prerequisites", [])
        if isinstance(prereqs, list):
            for p in prereqs:
                if isinstance(p, dict) and "id" in p:
                    prereq_graph[topic_id].append(p["id"])

    print(f"Loaded {len(all_data)} topics\n")

    # Track all changes
    changes = defaultdict(list)  # topic_id -> list of change descriptions
    modified_data = {}  # topic_id -> new data dict

    # ========== PHASE 2: Tier 1 - MERGE references ==========
    merge_count = 0
    for topic_id, data in all_data.items():
        builds = data.get("builds-toward", [])
        if not isinstance(builds, list):
            continue
        new_builds = []
        changed = False
        for target in builds:
            if target in MERGE_MAP:
                new_target = MERGE_MAP[target]
                if new_target in all_data:
                    new_builds.append(new_target)
                    changes[topic_id].append(f"MERGE builds-toward: {target} -> {new_target}")
                    merge_count += 1
                    changed = True
                else:
                    new_builds.append(target)  # Keep if merge target doesn't exist
            else:
                new_builds.append(target)
        if changed:
            if topic_id not in modified_data:
                modified_data[topic_id] = dict(data)
            modified_data[topic_id]["builds-toward"] = new_builds

    print(f"Tier 1 MERGE: {merge_count} references redirected")

    # ========== PHASE 3: Tier 1 - REMOVE vague references ==========
    remove_count = 0
    for topic_id, data in all_data.items():
        current = modified_data.get(topic_id, data)
        builds = current.get("builds-toward", [])
        if not isinstance(builds, list):
            continue
        new_builds = []
        changed = False
        for target in builds:
            if target in REMOVE_TARGETS:
                changes[topic_id].append(f"REMOVE builds-toward: {target} (vague/course-level)")
                remove_count += 1
                changed = True
            else:
                new_builds.append(target)
        if changed:
            if topic_id not in modified_data:
                modified_data[topic_id] = dict(data)
            modified_data[topic_id]["builds-toward"] = new_builds

    print(f"Tier 1 REMOVE: {remove_count} vague references removed")

    # ========== PHASE 4: Tier 2 - Remove cycle builds-toward ==========
    cycle_count = 0
    for source_id, target_id in CYCLE_REMOVALS.items():
        if source_id not in all_data:
            continue
        current = modified_data.get(source_id, all_data[source_id])
        builds = current.get("builds-toward", [])
        if target_id in builds:
            new_builds = [b for b in builds if b != target_id]
            if source_id not in modified_data:
                modified_data[source_id] = dict(all_data[source_id])
            modified_data[source_id]["builds-toward"] = new_builds
            changes[source_id].append(f"REMOVE builds-toward: {target_id} (would create cycle)")
            cycle_count += 1

    print(f"Tier 2 CYCLES: {cycle_count} cycle-creating references removed")

    # ========== PHASE 5: Tier 4+5 - Add soft prereqs ==========
    # Build the full mismatch list (same logic as reconcile_analyze.py)
    transitive_cache = {}
    add_prereq_count = 0
    skip_transitive = 0
    skip_cycle = 0
    skip_bidirectional = 0
    skip_dismiss = 0
    flagged_direction = 0

    # Collect all builds-toward pairs where target exists but doesn't have source as prereq
    pairs_to_evaluate = []
    for topic_id, data in all_data.items():
        builds = data.get("builds-toward", [])
        if not isinstance(builds, list):
            continue
        for target_id in builds:
            if not isinstance(target_id, str):
                continue
            if target_id not in all_data:
                continue  # Dangling - handled separately
            if (topic_id, target_id) in CROSS_COURSE_DISMISS:
                skip_dismiss += 1
                continue
            # Check if source_id is in CYCLE_REMOVALS for this target
            if CYCLE_REMOVALS.get(topic_id) == target_id:
                continue  # Already handled

            target_data = all_data[target_id]
            target_prereqs = target_data.get("prerequisites", [])
            target_prereq_ids = [p.get("id") for p in target_prereqs if isinstance(p, dict)]

            if topic_id not in target_prereq_ids:
                same_domain = data.get("domain") == target_data.get("domain")
                same_course = data.get("course") == target_data.get("course")

                if not same_domain:
                    continue  # No cross-domain cases exist, but be safe

                pairs_to_evaluate.append((topic_id, target_id, same_course))

    # Now evaluate each pair
    for source_id, target_id, same_course in pairs_to_evaluate:
        # Check if already transitive
        trans = get_transitive_prereqs(prereq_graph, target_id, transitive_cache)
        if source_id in trans:
            skip_transitive += 1
            continue

        # Check if would create cycle
        if would_create_cycle(prereq_graph, source_id, target_id):
            skip_cycle += 1
            continue

        # Check bidirectional: does target also build-toward source?
        target_builds = all_data[target_id].get("builds-toward", [])
        if source_id in target_builds:
            skip_bidirectional += 1
            changes[target_id].append(
                f"FLAG bidirectional: {source_id} <-> {target_id} (skipped, needs review)")
            continue

        # Add soft prereq
        if target_id not in modified_data:
            modified_data[target_id] = dict(all_data[target_id])
        current_prereqs = list(modified_data[target_id].get("prerequisites", []))
        current_prereqs.append({"id": source_id, "type": "soft"})
        modified_data[target_id]["prerequisites"] = current_prereqs

        # Update prereq_graph for subsequent cycle checks
        prereq_graph[target_id].append(source_id)

        label = "same-course" if same_course else "cross-course"
        changes[target_id].append(f"ADD soft prereq: {source_id} ({label})")
        add_prereq_count += 1

    print(f"\nTier 4+5 ADD soft prereqs: {add_prereq_count}")
    print(f"  Skipped (already transitive): {skip_transitive}")
    print(f"  Skipped (would create cycle): {skip_cycle}")
    print(f"  Skipped (bidirectional): {skip_bidirectional}")
    print(f"  Skipped (dismissed): {skip_dismiss}")

    # ========== PHASE 6: Summary ==========
    total_files = len(modified_data)
    print(f"\nTotal files to modify: {total_files}")

    if dry_run:
        print("\n=== DRY RUN - No files modified ===\n")
        # Show sample changes
        shown = 0
        for topic_id, change_list in sorted(changes.items()):
            if shown >= 30:
                print(f"  ... and {len(changes) - 30} more topics")
                break
            for c in change_list:
                print(f"  {topic_id}: {c}")
            shown += 1
        return 0

    if apply:
        print("\n=== APPLYING CHANGES ===\n")
        files_written = 0
        for topic_id, new_data in modified_data.items():
            filepath = all_paths[topic_id]
            old_text = all_texts[topic_id]
            old_data = all_data[topic_id]
            new_text = rewrite_frontmatter(filepath, old_text, old_data, new_data)
            filepath.write_text(new_text, encoding="utf-8")
            files_written += 1

        print(f"Written {files_written} files")

        # Save change log
        log_path = ROOT / "tools" / "reconcile_log.json"
        with open(log_path, "w", encoding="utf-8") as f:
            json.dump(dict(changes), f, indent=2)
        print(f"Change log: {log_path}")

        return 0


if __name__ == "__main__":
    sys.exit(main() or 0)
