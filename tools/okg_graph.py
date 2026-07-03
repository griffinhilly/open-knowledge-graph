#!/usr/bin/env python3
"""Shared graph parser and cache for OKG tools.

Purpose: Parse all 15K+ topic files once and cache the result as JSON.
         Subsequent generators load the cache instead of re-parsing YAML.
Inputs:  domains/ directory (15K+ .md files with YAML frontmatter)
Outputs: output/.cache/graph.json (~8MB)

Usage:
    # Build cache (CI runs this once before all generators)
    python tools/okg_graph.py --build-cache

    # As a module in other tools
    from okg_graph import load_graph_data, load_domain_configs
    topics, configs = load_graph_data()
"""

import json
import re
import sys
import time
from collections import defaultdict
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML required. Install with: pip install pyyaml")
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent
DOMAINS_DIR = ROOT / "domains"
CACHE_DIR = ROOT / "output" / ".cache"
CACHE_PATH = CACHE_DIR / "graph.json"


def parse_frontmatter(filepath):
    """Parse YAML frontmatter from a topic markdown file.

    Returns dict of frontmatter fields, or None on failure.
    """
    text = filepath.read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not match:
        return None
    try:
        data = yaml.safe_load(match.group(1))
        if not isinstance(data, dict):
            return None
        return data
    except yaml.YAMLError:
        return None


def parse_topic_file(filepath):
    """Parse frontmatter AND body sections from a topic markdown file.

    Returns (data_dict, sections_dict) where sections maps heading -> content.
    Use this for generators that need body content (topic pages, questions).
    """
    text = filepath.read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not match:
        return None, {}
    try:
        data = yaml.safe_load(match.group(1))
    except yaml.YAMLError:
        return None, {}

    body = text[match.end():]
    sections = {}
    current_section = None
    current_lines = []

    for line in body.splitlines():
        header_match = re.match(r"^##\s+(.+)$", line)
        if header_match:
            if current_section:
                sections[current_section] = "\n".join(current_lines).strip()
            current_section = header_match.group(1).strip()
            current_lines = []
        elif current_section:
            current_lines.append(line)

    if current_section:
        sections[current_section] = "\n".join(current_lines).strip()

    return data, sections


def extract_questions(body_text):
    """Extract questions from a ## Questions YAML code block in body text.

    Returns list of question dicts, or empty list on failure.
    """
    match = re.search(r"## Questions\s*\n+```ya?ml\s*\n(.*?)```", body_text, re.DOTALL)
    if not match:
        return []
    try:
        questions = yaml.safe_load(match.group(1))
        return questions if isinstance(questions, list) else []
    except yaml.YAMLError:
        return []


def extract_core_idea(body_text):
    """Pull the first 1-2 sentences from the ## Core Idea section."""
    match = re.search(r"## Core Idea\s*\n+(.*?)(?=\n## |\Z)", body_text, re.DOTALL)
    if not match:
        return ""
    text = re.sub(r"\s+", " ", match.group(1).strip())
    sentences = re.split(r"(?<=[.!?])\s+", text)
    if len(sentences) >= 2:
        return sentences[0] + " " + sentences[1]
    return sentences[0] if sentences else ""


def load_domain_configs(domains_dir=None):
    """Load all _domain.yml configs.

    Returns dict: domain_name -> {title, courses: [{id, title, stage}, ...]}
    """
    domains_dir = Path(domains_dir) if domains_dir else DOMAINS_DIR
    configs = {}
    for domain_dir in sorted(domains_dir.iterdir()):
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
                        "stage": c.get("stage", "formal-systems"),
                    })
            configs[domain_dir.name] = {
                "title": data.get("title", domain_dir.name),
                "courses": course_list,
            }
    return configs


def load_all_frontmatter(domains_dir=None):
    """Load frontmatter from all topic files by parsing YAML.

    Returns dict: topic_id -> frontmatter dict
    """
    domains_dir = Path(domains_dir) if domains_dir else DOMAINS_DIR
    topics = {}
    for filepath in sorted(domains_dir.rglob("*.md")):
        if filepath.name.startswith("_"):
            continue
        data = parse_frontmatter(filepath)
        if data and "id" in data:
            topics[data["id"]] = data
    return topics


def build_edges(topics):
    """Build edge list from prerequisite data.

    Returns list of {source, target, type, cross_domain} dicts.
    """
    edges = []
    for tid, data in topics.items():
        prereqs = data.get("prerequisites") or []
        if not isinstance(prereqs, list):
            continue
        for p in prereqs:
            if isinstance(p, dict):
                pid = p.get("id", "")
                ptype = p.get("type", "hard")
            else:
                pid = str(p)
                ptype = "hard"
            if pid in topics:
                cross = topics[pid].get("domain", "") != data.get("domain", "")
                edges.append({
                    "source": pid,
                    "target": tid,
                    "type": ptype,
                    "cross_domain": cross,
                })
    return edges


def build_graph_stats(topics, edges):
    """Compute per-domain stats from topics and edges."""
    domain_stats = {}
    for data in topics.values():
        domain = data.get("domain", "")
        if domain not in domain_stats:
            domain_stats[domain] = {"topics": 0, "edges": 0, "courses": set()}
        domain_stats[domain]["topics"] += 1
        course = data.get("course", "")
        if course:
            domain_stats[domain]["courses"].add(course)

    for edge in edges:
        target_domain = topics.get(edge["target"], {}).get("domain", "")
        if target_domain in domain_stats:
            domain_stats[target_domain]["edges"] += 1

    # Convert sets to counts for JSON serialization
    for stats in domain_stats.values():
        stats["courses"] = len(stats["courses"])

    return domain_stats


def build_cache_data(domains_dir=None):
    """Build complete graph data from filesystem. Returns serializable dict."""
    t0 = time.time()
    topics = load_all_frontmatter(domains_dir)
    t1 = time.time()
    configs = load_domain_configs(domains_dir)
    edges = build_edges(topics)
    domain_stats = build_graph_stats(topics, edges)
    t2 = time.time()

    print(f"  Parsed {len(topics)} topics in {t1-t0:.1f}s")
    print(f"  Built {len(edges)} edges + stats in {t2-t1:.1f}s")

    return {
        "topics": topics,
        "configs": configs,
        "edges": edges,
        "domain_stats": domain_stats,
    }


def save_cache(data, cache_path=None):
    """Save graph data to JSON cache."""
    cache_path = Path(cache_path) if cache_path else CACHE_PATH
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    cache_path.write_text(json.dumps(data, separators=(",", ":")), encoding="utf-8")
    size_kb = cache_path.stat().st_size / 1024
    print(f"  Cache written: {cache_path.name} ({size_kb:.0f} KB)")


def load_cache(cache_path=None):
    """Load graph data from JSON cache. Returns None if cache doesn't exist."""
    cache_path = Path(cache_path) if cache_path else CACHE_PATH
    if not cache_path.exists():
        return None
    return json.loads(cache_path.read_text(encoding="utf-8"))


def load_graph_data(domains_dir=None, cache_path=None):
    """Load graph data, preferring cache if available.

    Returns (topics_dict, configs_dict) where:
      - topics_dict: {topic_id -> frontmatter dict}
      - configs_dict: {domain_name -> {title, courses}}

    The full cache (with edges and stats) is available via load_cache().
    """
    cached = load_cache(cache_path)
    if cached:
        return cached["topics"], cached["configs"]
    topics = load_all_frontmatter(domains_dir)
    configs = load_domain_configs(domains_dir)
    return topics, configs


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="OKG shared graph parser")
    parser.add_argument("--build-cache", action="store_true",
                        help="Parse all topics and write JSON cache")
    parser.add_argument("--cache-path", type=str, default=None,
                        help="Custom cache output path")
    args = parser.parse_args()

    if args.build_cache:
        print("Building graph cache...")
        data = build_cache_data()
        save_cache(data, args.cache_path)
        stats = data["domain_stats"]
        total_topics = sum(s["topics"] for s in stats.values())
        total_edges = len(data["edges"])
        print(f"  {total_topics} topics, {total_edges} edges, {len(data['configs'])} domains")
    else:
        parser.print_help()
