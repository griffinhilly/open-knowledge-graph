#!/usr/bin/env python3
"""Deduplicate programming-fundamentals topics.

For each merge group:
1. Updates all references across domains/ (prerequisites and builds-toward)
2. Merges unique prereqs/builds-toward from losers into winner
3. Renames winner file if ID changes (e.g., removing verbose prefix)
4. Deletes loser files
5. Prints summary
"""

import os
import re
import sys
from pathlib import Path
from collections import defaultdict

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML required. Install with: pip install pyyaml")
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent
DOMAINS_DIR = ROOT / "domains"
PF_DIR = DOMAINS_DIR / "computer-science" / "programming-fundamentals"

# =============================================================================
# CANONICAL MAPPING
# =============================================================================
# Each entry: (winner_id, rename_to_or_None, [loser_ids])
#
# winner_id: the file that currently exists and whose content we keep
# rename_to: if not None, rename the winner file + update its ID to this
# loser_ids: files that get merged into the winner then deleted
#
# CRITICAL: distinct concepts are NOT merged. See comments.
# =============================================================================

MERGE_GROUPS = [
    # --- while-loops (do-while-loops is SEPARATE) ---
    ("while-loops", None, [
        "while-loop-iteration",
        "programming-fundamentals-while-loops",
        "while-loop-patterns-and-termination",
    ]),

    # --- exceptions ---
    ("error-handling-exceptions", None, [
        "programming-fundamentals-exceptions-intro",
        "managing-errors-with-exceptions",
        "exception-basics-and-error-handling",
        "programming-fundamentals-try-catch-finally",
    ]),

    # --- functions (call-stack, decomposing, design-contracts are SEPARATE) ---
    ("functions-defining-calling", None, [
        "programming-fundamentals-function-definition",
        "function-definition-and-calls",
    ]),

    # --- return-values ---
    ("return-values", None, [
        "return-values-and-function-returns",
        "programming-fundamentals-return-values",
        "return-values-and-results",
    ]),

    # --- variable-scope (scope-shadowing-and-lifetime is SEPARATE) ---
    ("variable-scope", None, [
        "programming-fundamentals-variable-scope",
        "variable-scope-and-binding",
    ]),

    # --- arithmetic operators ---
    # arithmetic-operators-and-precedence has most refs (3) among clean IDs
    # rename to arithmetic-operators for cleaner ID
    ("arithmetic-operators-and-precedence", "arithmetic-operators", [
        "arithmetic-operators-intro",
        "programming-fundamentals-arithmetic-operators",
    ]),

    # --- arrays-and-lists ---
    ("arrays-and-lists", None, [
        "arrays-lists-and-collections",
        "programming-fundamentals-arrays-and-lists",
        "arrays-and-indexed-collections",
    ]),

    # --- array-indexing ---
    # programming-fundamentals-array-indexing is the only one specifically about indexing
    # accessing-and-modifying-elements is also about indexing/element access
    # Merge both into a clean "array-indexing" ID
    ("programming-fundamentals-array-indexing", "array-indexing", [
        "accessing-and-modifying-elements",
    ]),

    # --- comparison operators ---
    # comparison-operators-and-boolean-tests has 3 refs, clean-ish name
    # rename to comparison-operators
    ("comparison-operators-and-boolean-tests", "comparison-operators", [
        "comparison-operators-and-relations",
        "programming-fundamentals-comparison-operators",
    ]),

    # --- for-loops ---
    ("for-loops", None, [
        "programming-fundamentals-for-loops",
        "for-loop-iteration",
        "for-loop-patterns-and-iteration",
    ]),

    # --- conditionals ---
    ("conditional-statements", None, [
        "programming-fundamentals-if-else-statements",
        "conditional-statements-branching",
    ]),

    # --- logical-operators ---
    # logical-operators-and-gates has 5 refs, rename to logical-operators
    ("logical-operators-and-gates", "logical-operators", [
        "programming-fundamentals-logical-operators",
        "logical-operators-and-boolean-algebra",
    ]),

    # --- primitive types ---
    ("primitive-data-types", None, [
        "programming-fundamentals-primitive-types",
        "primitive-types-integers-floats-strings",
    ]),

    # --- string-operations ---
    ("string-operations", None, [
        "programming-fundamentals-string-operations",
        "string-operations-and-methods",
    ]),

    # --- recursion (recursion-basics is most referenced at 21) ---
    ("recursion-basics", None, [
        "programming-fundamentals-recursion-basics",
        "recursion-and-recursive-calls",
        "recursion-thinking-recursively",
    ]),

    # --- variables ---
    ("variables-and-assignment", None, [
        "programming-fundamentals-variables-assignment",
    ]),

    # --- type-conversion ---
    ("type-conversion", None, [
        "programming-fundamentals-type-conversion",
    ]),

    # --- nested-loops ---
    ("nested-loops", None, [
        "nested-loops-and-deep-iteration",
    ]),

    # --- loop-control ---
    ("loop-control-statements", None, [
        "programming-fundamentals-loop-control-statements",
    ]),

    # --- parameters ---
    ("parameters-and-arguments", None, [
        "programming-fundamentals-parameters-arguments",
        "function-parameters-passing-data",
    ]),

    # --- program-structure ---
    # program-structure-and-flow has 4 refs, rename to program-structure
    ("program-structure-and-flow", "program-structure", [
        "program-structure-and-anatomy",
    ]),

    # --- intro-to-classes ---
    ("intro-to-classes", None, [
        "introducing-objects-and-classes",
    ]),

    # --- file-io ---
    ("file-io-basics", None, [
        "programming-fundamentals-file-io",
    ]),

    # --- strings-intro ---
    # string-basics has 5 refs
    ("string-basics", None, [
        "programming-fundamentals-strings-introduction",
        "string-text-representation",
        "strings-as-character-sequences",
        "character-and-string-basics",
    ]),

    # --- debugging ---
    ("debugging-basics", None, [
        "debugging-finding-and-fixing-bugs",
    ]),

    # --- input-output ---
    # basic-input-output has 8 refs, rename to input-output
    ("basic-input-output", "input-output", [
        "input-output-console-operations",
        "programming-fundamentals-console-io",
    ]),

    # --- boolean ---
    # boolean-type-and-truth-values has 4 refs, rename to boolean-logic
    ("boolean-type-and-truth-values", "boolean-logic", [
        "boolean-logic-programming",
    ]),

    # --- else-if-chains / conditional-logic-chains ---
    # else-if-chains has 2 refs, conditional-logic-chains has 3 refs
    # Both are about multi-way branching beyond basic if-else
    # Keep else-if-chains as the canonical name (matches the ~40 list)
    ("else-if-chains", None, [
        "conditional-logic-chains",
        "if-else-branching-logic",
        "programming-fundamentals-nested-conditions",
    ]),

    # --- numeric-types ---
    # integer-and-floating-point-types has 3 refs
    # working-with-numbers-integers-floats has 2 refs
    # These are both about int/float types specifically
    # Keep integer-and-floating-point-types, rename to numeric-types
    # Actually -- these overlap heavily with primitive-data-types.
    # But they're specifically about numeric types detail. Merge into primitive-data-types?
    # No -- the user listed numeric-types as a separate singleton group.
    # But it's NOT in the ~40 canonical list. Merge into primitive-data-types.
    # Wait, looking again: the user's instruction says "keep integer-and-floating-point-types OR
    # working-with-numbers-integers-floats (pick most referenced), delete the other"
    # So we keep them as a topic but merge the two into one.
    # But it's not in the ~40 list... I'll keep it as a separate topic since the user said to.
    # Actually the user said ~40, not exactly 40. These are distinct enough.
    # Merge the two into one. Neither name is in the ~40 list so pick the cleaner one.
    ("integer-and-floating-point-types", "numeric-types", [
        "working-with-numbers-integers-floats",
    ]),

    # --- methods/OOP ---
    ("methods-and-attributes", None, [
        "methods-objects-and-messages",
    ]),

    # --- operators-and-expressions ---
    # operators-and-expressions has 7 refs, expressions-and-evaluation has 1
    # operator-precedence-and-evaluation has 2, programming-fundamentals-operator-precedence has 2
    # These are all about the same concept: operators, expressions, and precedence
    ("operators-and-expressions", None, [
        "expressions-and-evaluation",
        "operator-precedence-and-evaluation",
        "programming-fundamentals-operator-precedence",
    ]),

    # --- switch ---
    ("switch-statements", None, [
        "programming-fundamentals-switch-case",
    ]),

    # --- loop-patterns ---
    # loop-design-and-invariants has 5 refs
    # programming-fundamentals-loop-patterns has 3 refs
    # Both are about loop design patterns. Merge.
    ("loop-design-and-invariants", None, [
        "programming-fundamentals-loop-patterns",
    ]),

    # --- iterating-over-collections ---
    # iterating-over-collections has 2 refs
    # programming-fundamentals-iteration-collections has 4 refs
    # Keep iterating-over-collections (cleaner ID, in the ~40 list)
    ("iterating-over-collections", None, [
        "programming-fundamentals-iteration-collections",
    ]),

    # --- hello-world ---
    # hello-world-your-first-program should be renamed to hello-world (cleaner)
    ("hello-world-your-first-program", "hello-world", []),

    # --- variable extras ---
    # variable-declaration-syntax and variable-names-and-conventions
    # These are about specific sub-aspects of variables-and-assignment.
    # They're not in the canonical ~40 list. Merge into variables-and-assignment.
    ("variables-and-assignment", None, [
        "variable-declaration-syntax",
        "variable-names-and-conventions",
    ]),
]

# =============================================================================
# Build the full mapping
# =============================================================================

def build_id_map():
    """Build old_id -> new_id mapping from MERGE_GROUPS."""
    id_map = {}  # old_id -> new_id (the final canonical ID)

    for winner_id, rename_to, loser_ids in MERGE_GROUPS:
        final_id = rename_to if rename_to else winner_id
        # Map winner to its final ID (might be itself or a rename)
        if rename_to:
            id_map[winner_id] = final_id
        # Map all losers to the final ID
        for loser_id in loser_ids:
            id_map[loser_id] = final_id

    return id_map


def parse_frontmatter(filepath):
    """Extract YAML frontmatter and body from a Markdown file."""
    text = filepath.read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not match:
        return None, text
    try:
        data = yaml.safe_load(match.group(1))
    except yaml.YAMLError:
        return None, text
    body = text[match.end():]
    return data, body


def write_frontmatter(filepath, data, body):
    """Write YAML frontmatter + body back to file."""
    # Custom YAML dump that preserves nice formatting
    lines = ["---"]

    # Write fields in a specific order
    field_order = ["id", "title", "domain", "course", "prerequisites",
                   "builds-toward", "tags", "stage", "status"]

    for field in field_order:
        if field not in data:
            continue
        val = data[field]

        if field == "prerequisites":
            lines.append("prerequisites:")
            if isinstance(val, list):
                for item in val:
                    if isinstance(item, dict):
                        lines.append(f"- id: {item['id']}")
                        lines.append(f"  type: {item.get('type', 'hard')}")
                    else:
                        lines.append(f"- {item}")
            continue

        if field == "builds-toward":
            lines.append("builds-toward:")
            if isinstance(val, list):
                for item in val:
                    lines.append(f"- {item}")
            continue

        if field == "tags":
            lines.append("tags:")
            if isinstance(val, list):
                for item in val:
                    lines.append(f"- {item}")
            continue

        # Simple scalar
        if isinstance(val, str) and (":" in val or '"' in val or "'" in val):
            lines.append(f'{field}: "{val}"')
        else:
            lines.append(f"{field}: {val}")

    lines.append("---")
    lines.append("")

    full_text = "\n".join(lines) + body
    filepath.write_text(full_text, encoding="utf-8")


def update_references_in_file(filepath, id_map, stats):
    """Update prerequisite and builds-toward references in a single file."""
    data, body = parse_frontmatter(filepath)
    if data is None:
        return False

    changed = False

    # Update prerequisites
    prereqs = data.get("prerequisites", [])
    if isinstance(prereqs, list):
        for i, prereq in enumerate(prereqs):
            if isinstance(prereq, dict) and "id" in prereq:
                old_id = prereq["id"]
                if old_id in id_map:
                    new_id = id_map[old_id]
                    prereq["id"] = new_id
                    changed = True
                    stats["ref_updates"].append(
                        f"  {filepath.relative_to(ROOT)}: prereq {old_id} -> {new_id}"
                    )

    # Deduplicate prerequisites (same ID might appear after merging)
    if isinstance(prereqs, list):
        seen_ids = set()
        deduped = []
        for prereq in prereqs:
            if isinstance(prereq, dict):
                pid = prereq.get("id")
                # Also skip self-references
                topic_id = data.get("id", filepath.stem)
                if pid and pid not in seen_ids and pid != topic_id:
                    seen_ids.add(pid)
                    deduped.append(prereq)
                elif pid in seen_ids or pid == topic_id:
                    changed = True
            else:
                deduped.append(prereq)
        data["prerequisites"] = deduped

    # Update builds-toward
    builds = data.get("builds-toward", [])
    if isinstance(builds, list):
        new_builds = []
        for target in builds:
            if isinstance(target, str) and target in id_map:
                new_target = id_map[target]
                if new_target != target:
                    changed = True
                    stats["ref_updates"].append(
                        f"  {filepath.relative_to(ROOT)}: builds-toward {target} -> {new_target}"
                    )
                new_builds.append(new_target)
            else:
                new_builds.append(target)

        # Deduplicate builds-toward and remove self-references
        topic_id = data.get("id", filepath.stem)
        seen = set()
        deduped_builds = []
        for b in new_builds:
            if isinstance(b, str) and b not in seen and b != topic_id:
                seen.add(b)
                deduped_builds.append(b)
            elif b in seen or b == topic_id:
                changed = True
        data["builds-toward"] = deduped_builds

    if changed:
        write_frontmatter(filepath, data, body)

    return changed


def merge_metadata(winner_path, loser_paths, final_id, id_map, stats):
    """Merge unique prereqs/builds-toward from losers into winner."""
    winner_data, winner_body = parse_frontmatter(winner_path)
    if winner_data is None:
        print(f"  WARNING: Could not parse winner {winner_path}")
        return

    # Collect existing winner prereq IDs and builds-toward
    winner_prereq_ids = set()
    winner_prereqs = winner_data.get("prerequisites", [])
    if isinstance(winner_prereqs, list):
        for p in winner_prereqs:
            if isinstance(p, dict):
                pid = p.get("id", "")
                # Resolve through id_map
                winner_prereq_ids.add(id_map.get(pid, pid))

    winner_builds = set()
    builds = winner_data.get("builds-toward", [])
    if isinstance(builds, list):
        for b in builds:
            if isinstance(b, str):
                winner_builds.add(id_map.get(b, b))

    # Collect all loser IDs (including the winner's old ID if renamed)
    all_group_ids = set()
    all_group_ids.add(final_id)
    if winner_data.get("id") != final_id:
        all_group_ids.add(winner_data.get("id", ""))
    for lp in loser_paths:
        all_group_ids.add(lp.stem)

    # Merge from each loser
    merged_prereqs = []
    merged_builds = []

    for loser_path in loser_paths:
        loser_data, _ = parse_frontmatter(loser_path)
        if loser_data is None:
            continue

        # Merge prereqs
        loser_prereqs = loser_data.get("prerequisites", [])
        if isinstance(loser_prereqs, list):
            for p in loser_prereqs:
                if isinstance(p, dict) and "id" in p:
                    pid = p["id"]
                    resolved = id_map.get(pid, pid)
                    # Don't add if: already in winner, is self-ref, or is another group member
                    if (resolved not in winner_prereq_ids and
                        resolved not in all_group_ids and
                        resolved != final_id):
                        winner_prereq_ids.add(resolved)
                        merged_prereqs.append({"id": resolved, "type": p.get("type", "soft")})
                        stats["merged_prereqs"].append(
                            f"  {final_id}: added prereq {resolved} (from {loser_path.stem})"
                        )

        # Merge builds-toward
        loser_builds = loser_data.get("builds-toward", [])
        if isinstance(loser_builds, list):
            for b in loser_builds:
                if isinstance(b, str):
                    resolved = id_map.get(b, b)
                    if (resolved not in winner_builds and
                        resolved not in all_group_ids and
                        resolved != final_id):
                        winner_builds.add(resolved)
                        merged_builds.append(resolved)
                        stats["merged_builds"].append(
                            f"  {final_id}: added builds-toward {resolved} (from {loser_path.stem})"
                        )

    # Apply merges to winner data
    if merged_prereqs:
        existing = winner_data.get("prerequisites", [])
        if not isinstance(existing, list):
            existing = []
        # Resolve existing prereqs through id_map first
        resolved_existing = []
        seen = set()
        for p in existing:
            if isinstance(p, dict) and "id" in p:
                resolved_id = id_map.get(p["id"], p["id"])
                if resolved_id not in seen and resolved_id not in all_group_ids:
                    p["id"] = resolved_id
                    seen.add(resolved_id)
                    resolved_existing.append(p)
        winner_data["prerequisites"] = resolved_existing + merged_prereqs

    if merged_builds:
        existing = winner_data.get("builds-toward", [])
        if not isinstance(existing, list):
            existing = []
        resolved_existing = []
        seen = set()
        for b in existing:
            if isinstance(b, str):
                resolved = id_map.get(b, b)
                if resolved not in seen and resolved not in all_group_ids:
                    seen.add(resolved)
                    resolved_existing.append(resolved)
        winner_data["builds-toward"] = resolved_existing + merged_builds

    # Update the winner's own ID if renamed
    if final_id != winner_data.get("id"):
        winner_data["id"] = final_id

    # Also resolve the winner's own prereqs and builds through id_map
    # (in case they reference other losers not in this group)
    prereqs = winner_data.get("prerequisites", [])
    if isinstance(prereqs, list):
        seen = set()
        deduped = []
        for p in prereqs:
            if isinstance(p, dict) and "id" in p:
                p["id"] = id_map.get(p["id"], p["id"])
                if p["id"] not in seen and p["id"] != final_id and p["id"] not in all_group_ids:
                    seen.add(p["id"])
                    deduped.append(p)
                elif p["id"] == final_id or p["id"] in all_group_ids:
                    pass  # skip self-refs
        winner_data["prerequisites"] = deduped

    builds_list = winner_data.get("builds-toward", [])
    if isinstance(builds_list, list):
        seen = set()
        deduped = []
        for b in builds_list:
            if isinstance(b, str):
                resolved = id_map.get(b, b)
                if resolved not in seen and resolved != final_id and resolved not in all_group_ids:
                    seen.add(resolved)
                    deduped.append(resolved)
        winner_data["builds-toward"] = deduped

    write_frontmatter(winner_path, winner_data, winner_body)


def main():
    print("=" * 70)
    print("DEDUP MERGE: programming-fundamentals")
    print("=" * 70)

    id_map = build_id_map()

    stats = {
        "ref_updates": [],
        "merged_prereqs": [],
        "merged_builds": [],
        "files_deleted": [],
        "files_renamed": [],
    }

    # Verify all referenced files exist
    print("\n[1/5] Verifying files exist...")
    missing = []
    for winner_id, rename_to, loser_ids in MERGE_GROUPS:
        winner_path = PF_DIR / f"{winner_id}.md"
        if not winner_path.exists():
            missing.append(f"  WINNER missing: {winner_id}")
        for lid in loser_ids:
            loser_path = PF_DIR / f"{lid}.md"
            if not loser_path.exists():
                missing.append(f"  LOSER missing: {lid}")

    if missing:
        print("ABORT: Missing files:")
        for m in missing:
            print(m)
        return 1
    print(f"  All {sum(1 + len(losers) for _, _, losers in MERGE_GROUPS)} files verified.")

    # Step 1: Update all references across ALL domains
    print("\n[2/5] Updating references across all domains...")
    all_md_files = sorted(DOMAINS_DIR.rglob("*.md"))
    files_updated = 0
    for md_file in all_md_files:
        if update_references_in_file(md_file, id_map, stats):
            files_updated += 1
    print(f"  Updated {files_updated} files with {len(stats['ref_updates'])} reference changes.")

    # Step 2: Merge metadata from losers into winners
    print("\n[3/5] Merging metadata from losers into winners...")
    for winner_id, rename_to, loser_ids in MERGE_GROUPS:
        if not loser_ids:
            continue
        winner_path = PF_DIR / f"{winner_id}.md"
        loser_paths = [PF_DIR / f"{lid}.md" for lid in loser_ids]
        final_id = rename_to if rename_to else winner_id
        merge_metadata(winner_path, loser_paths, final_id, id_map, stats)
    print(f"  Merged {len(stats['merged_prereqs'])} prereqs, {len(stats['merged_builds'])} builds-toward entries.")

    # Step 3: Rename winner files if needed
    print("\n[4/5] Renaming files...")
    for winner_id, rename_to, loser_ids in MERGE_GROUPS:
        if not rename_to:
            continue
        old_path = PF_DIR / f"{winner_id}.md"
        new_path = PF_DIR / f"{rename_to}.md"
        if old_path.exists():
            old_path.rename(new_path)
            stats["files_renamed"].append(f"  {winner_id}.md -> {rename_to}.md")
            print(f"  Renamed {winner_id}.md -> {rename_to}.md")

    # Step 4: Delete loser files
    print("\n[5/5] Deleting loser files...")
    for winner_id, rename_to, loser_ids in MERGE_GROUPS:
        for lid in loser_ids:
            loser_path = PF_DIR / f"{lid}.md"
            if loser_path.exists():
                loser_path.unlink()
                stats["files_deleted"].append(lid)
    print(f"  Deleted {len(stats['files_deleted'])} files.")

    # Summary
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)

    remaining = len(list(PF_DIR.glob("*.md")))
    print(f"\nRemaining topic files: {remaining}")
    print(f"Files deleted: {len(stats['files_deleted'])}")
    print(f"Files renamed: {len(stats['files_renamed'])}")
    print(f"Reference updates: {len(stats['ref_updates'])}")
    print(f"Merged prereqs: {len(stats['merged_prereqs'])}")
    print(f"Merged builds-toward: {len(stats['merged_builds'])}")

    if stats["files_renamed"]:
        print("\nRenamed files:")
        for r in stats["files_renamed"]:
            print(r)

    if stats["merged_prereqs"]:
        print("\nMerged prerequisites:")
        for m in stats["merged_prereqs"]:
            print(m)

    if stats["merged_builds"]:
        print("\nMerged builds-toward:")
        for m in stats["merged_builds"]:
            print(m)

    print("\nRemaining files:")
    for f in sorted(PF_DIR.glob("*.md")):
        print(f"  {f.stem}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
