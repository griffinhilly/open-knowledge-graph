#!/usr/bin/env python3
"""Convert agent JSON output to topic .md files and apply cross-domain edits."""

import json
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: pyyaml required. Install with: pip install pyyaml")
    sys.exit(1)

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
DOMAINS_DIR = PROJECT_ROOT / "domains"


def generate_topic_file(topic: dict, domain_dir: Path) -> Path:
    """Create a single topic .md file from a topic dict."""
    course_dir = domain_dir / topic["course"]
    course_dir.mkdir(parents=True, exist_ok=True)
    filepath = course_dir / f"{topic['id']}.md"

    # Build frontmatter dict (ordered to match project convention)
    fm = {
        "id": topic["id"],
        "title": topic["title"],
        "domain": topic["domain"],
        "course": topic["course"],
        "prerequisites": topic.get("prerequisites", []),
    }
    if topic.get("builds_toward"):
        fm["builds-toward"] = topic["builds_toward"]
    if topic.get("tags"):
        fm["tags"] = topic["tags"]
    if topic.get("stage"):
        fm["stage"] = topic["stage"]
    fm["status"] = topic.get("status", "draft")
    if topic.get("aliases"):
        fm["aliases"] = topic["aliases"]

    # Build body
    body_parts = [f"# {topic['title']}\n"]
    body_parts.append(f"\n## Core Idea\n{topic.get('core_idea', 'TODO')}\n")
    if topic.get("how_best_learned"):
        body_parts.append(f"\n## How It's Best Learned\n{topic['how_best_learned']}\n")
    if topic.get("common_misconceptions"):
        body_parts.append(f"\n## Common Misconceptions\n{topic['common_misconceptions']}\n")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write("---\n")
        yaml.dump(fm, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
        f.write("---\n\n")
        f.write("".join(body_parts))

    return filepath


def generate_domain_config(config: dict, domain_dir: Path) -> Path:
    """Create _domain.yml for a new domain."""
    domain_dir.mkdir(parents=True, exist_ok=True)
    filepath = domain_dir / "_domain.yml"
    with open(filepath, "w", encoding="utf-8") as f:
        yaml.dump(config, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
    return filepath


def process_output(json_path: Path, fallback_domain: str = None) -> list[Path]:
    """Process an agent's JSON output file. Returns list of created file paths.

    Handles both:
      - {"domain": "...", "topics": [...]}  (expected format)
      - [...] (bare array of topics — fallback_domain used for domain_dir)
    """
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Handle bare array output
    if isinstance(data, list):
        if not fallback_domain:
            raise ValueError("Got bare array but no fallback_domain specified")
        topics = data
        domain = fallback_domain
        domain_config = None
    else:
        topics = data.get("topics", [])
        domain = data.get("domain", fallback_domain)
        domain_config = data.get("domain_config")

    if not domain:
        raise ValueError("No domain specified in JSON or as fallback")

    domain_dir = DOMAINS_DIR / domain
    created = []

    # Create domain config if present
    if domain_config:
        p = generate_domain_config(domain_config, domain_dir)
        created.append(p)

    # Create topic files
    for topic in topics:
        # Ensure domain field is set
        if "domain" not in topic:
            topic["domain"] = domain
        p = generate_topic_file(topic, domain_dir)
        created.append(p)

    return created


# =========================================================================
# Cross-domain edit applicator
# =========================================================================

def parse_frontmatter(filepath: Path) -> tuple[dict, str]:
    """Read a topic .md file and return (frontmatter_dict, body_text)."""
    text = filepath.read_text(encoding="utf-8")
    match = re.match(r'^---\n(.*?)\n---\n?(.*)', text, re.DOTALL)
    if not match:
        raise ValueError(f"No YAML frontmatter found in {filepath}")
    fm = yaml.safe_load(match.group(1))
    body = match.group(2)
    return fm, body


def write_frontmatter(filepath: Path, fm: dict, body: str):
    """Write topic .md file with updated frontmatter."""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("---\n")
        yaml.dump(fm, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
        f.write("---\n")
        f.write(body)


def apply_crosslink_edits(edits_json_path: Path) -> int:
    """Apply cross-domain link edits from a review agent's output.

    Expected JSON format: list of edit objects:
    [
      {
        "topic_id": "some-topic",
        "domain": "physics",
        "course": "classical-mechanics",
        "add_prerequisites": [{"id": "calculus-derivative", "type": "soft"}],
        "add_builds_toward": ["some-other-topic"]
      }
    ]

    Returns count of topics modified.
    """
    with open(edits_json_path, "r", encoding="utf-8") as f:
        edits = json.load(f)

    if not isinstance(edits, list):
        edits = edits.get("edits", [])

    modified = 0
    for edit in edits:
        topic_id = edit.get("topic_id")
        domain = edit.get("domain")
        course = edit.get("course")
        if not all([topic_id, domain, course]):
            continue

        filepath = DOMAINS_DIR / domain / course / f"{topic_id}.md"
        if not filepath.exists():
            continue

        try:
            fm, body = parse_frontmatter(filepath)
        except Exception:
            continue

        changed = False

        # Add prerequisites
        for prereq in edit.get("add_prerequisites", []):
            existing_ids = {p["id"] for p in fm.get("prerequisites", [])}
            if prereq["id"] not in existing_ids:
                fm.setdefault("prerequisites", []).append(prereq)
                changed = True

        # Add builds-toward
        for bt in edit.get("add_builds_toward", []):
            existing_bt = fm.get("builds-toward", [])
            if bt not in existing_bt:
                fm.setdefault("builds-toward", []).append(bt)
                changed = True

        if changed:
            write_frontmatter(filepath, fm, body)
            modified += 1

    return modified


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python generator.py <output.json> [fallback-domain]")
        print("  python generator.py --apply-edits <edits.json>")
        sys.exit(1)

    if sys.argv[1] == "--apply-edits":
        edits_path = Path(sys.argv[2])
        count = apply_crosslink_edits(edits_path)
        print(f"Modified {count} topic files")
    else:
        json_path = Path(sys.argv[1])
        fallback = sys.argv[2] if len(sys.argv) > 2 else None
        created = process_output(json_path, fallback_domain=fallback)
        print(f"Created {len(created)} files:")
        for f in created:
            print(f"  {f.relative_to(PROJECT_ROOT)}")
