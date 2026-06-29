#!/usr/bin/env python3
"""Analyze programming-fundamentals course for duplicate topics and produce a merge plan.

Reads all .md files in domains/computer-science/programming-fundamentals/,
groups them by semantic similarity, counts cross-domain references, picks winners,
and outputs a JSON merge plan to stdout.
"""

import json
import re
import sys
from collections import defaultdict
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
PF_DIR = PROJECT_ROOT / "domains" / "computer-science" / "programming-fundamentals"
DOMAINS_DIR = PROJECT_ROOT / "domains"

# ---------------------------------------------------------------------------
# YAML frontmatter parsing (manual — avoids PyYAML dependency for simple cases)
# ---------------------------------------------------------------------------

def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Extract YAML frontmatter dict and body from a markdown file."""
    if not text.startswith("---"):
        return {}, text
    end = text.find("---", 3)
    if end == -1:
        return {}, text
    fm_text = text[3:end].strip()
    body = text[end + 3:].strip()
    return parse_simple_yaml(fm_text), body


def parse_simple_yaml(text: str) -> dict:
    """Parse the subset of YAML used in OKG frontmatter."""
    result = {}
    current_key = None
    current_list = None

    for line in text.split("\n"):
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue

        # List item under current key
        if stripped.startswith("- ") and current_key is not None:
            value = stripped[2:].strip()
            # Could be "id: something" (dict-style) or "- some-value" (plain)
            if ":" in value:
                parts = value.split(":", 1)
                k, v = parts[0].strip(), parts[1].strip()
                if current_list is not None:
                    # Check if this is a new dict item or continuation
                    if not current_list or not isinstance(current_list[-1], dict) or k in current_list[-1]:
                        current_list.append({k: v})
                    else:
                        current_list[-1][k] = v
            else:
                if current_list is not None:
                    current_list.append(value)
            continue

        # Continuation of dict inside list item (e.g., "  type: hard")
        if current_list and stripped.count(":") == 1 and not stripped.startswith("-"):
            indent = len(line) - len(line.lstrip())
            if indent >= 2 and current_list and isinstance(current_list[-1], dict):
                k, v = stripped.split(":", 1)
                current_list[-1][k.strip()] = v.strip()
                continue

        # Top-level key: value
        if ":" in stripped:
            k, v = stripped.split(":", 1)
            k, v = k.strip(), v.strip()
            if v:
                result[k] = v
                current_key = k
                current_list = None
            else:
                # Start of a list or nested block
                current_key = k
                current_list = []
                result[k] = current_list

    return result


# ---------------------------------------------------------------------------
# File reading
# ---------------------------------------------------------------------------

def read_topic_file(path: Path) -> dict | None:
    """Read a topic .md file and return structured data."""
    try:
        text = path.read_text(encoding="utf-8")
    except Exception as e:
        print(f"WARNING: Could not read {path}: {e}", file=sys.stderr)
        return None

    fm, body = parse_frontmatter(text)
    if not fm.get("id"):
        return None

    # Extract prerequisites as list of IDs
    prereqs = []
    raw_prereqs = fm.get("prerequisites", [])
    if isinstance(raw_prereqs, list):
        for item in raw_prereqs:
            if isinstance(item, dict):
                prereqs.append(item.get("id", ""))
            elif isinstance(item, str):
                prereqs.append(item)

    # Extract builds-toward as list of IDs
    builds = []
    raw_builds = fm.get("builds-toward", [])
    if isinstance(raw_builds, list):
        for item in raw_builds:
            if isinstance(item, dict):
                builds.append(item.get("id", item.get("", "")))
            elif isinstance(item, str):
                builds.append(item)

    # Extract Core Idea section
    core_idea = ""
    match = re.search(r"## Core Idea\s*\n(.+?)(?:\n## |\Z)", body, re.DOTALL)
    if match:
        core_idea = match.group(1).strip()

    # First sentence of Core Idea
    first_sentence = ""
    if core_idea:
        # Split on period followed by space or end
        sent_match = re.match(r"(.+?\.)\s", core_idea)
        if sent_match:
            first_sentence = sent_match.group(1)
        else:
            first_sentence = core_idea.split("\n")[0]

    return {
        "id": fm["id"],
        "title": fm.get("title", ""),
        "status": fm.get("status", "draft"),
        "stage": fm.get("stage", ""),
        "prerequisites": prereqs,
        "builds_toward": builds,
        "core_idea": core_idea,
        "first_sentence": first_sentence,
        "file": path.name,
        "path": str(path),
    }


# ---------------------------------------------------------------------------
# Reference counting across all domains
# ---------------------------------------------------------------------------

def count_references(topic_ids: set[str], domains_dir: Path) -> dict[str, int]:
    """Count how many OTHER files reference each topic ID in prereqs/builds-toward."""
    ref_counts = defaultdict(int)

    for md_file in domains_dir.rglob("*.md"):
        try:
            text = md_file.read_text(encoding="utf-8")
        except Exception:
            continue

        fm, _ = parse_frontmatter(text)
        file_id = fm.get("id", "")

        # Gather all referenced IDs from this file
        referenced = set()
        raw_prereqs = fm.get("prerequisites", [])
        if isinstance(raw_prereqs, list):
            for item in raw_prereqs:
                if isinstance(item, dict):
                    referenced.add(item.get("id", ""))
                elif isinstance(item, str):
                    referenced.add(item)

        raw_builds = fm.get("builds-toward", [])
        if isinstance(raw_builds, list):
            for item in raw_builds:
                if isinstance(item, dict):
                    referenced.add(item.get("id", ""))
                elif isinstance(item, str):
                    referenced.add(item)

        # Count references to our target IDs (excluding self-references)
        for tid in referenced:
            if tid in topic_ids and tid != file_id:
                ref_counts[tid] += 1

    return dict(ref_counts)


# ---------------------------------------------------------------------------
# Similarity / grouping
# ---------------------------------------------------------------------------

def strip_prefix(topic_id: str) -> str:
    """Strip common course prefix from a topic ID."""
    if topic_id.startswith("programming-fundamentals-"):
        return topic_id[len("programming-fundamentals-"):]
    return topic_id


def stem(word: str) -> str:
    """Minimal stemming: reduce words to a comparable root.

    Not a proper linguistic stemmer — just enough to equate common variants
    like 'exception/exceptions', 'recursive/recursion', 'class/classes'.
    Uses a two-pass approach: suffix removal then prefix truncation.
    """
    w = word.lower()
    # Apply at most one suffix removal, longest match first
    # Minimum residual is 4 chars to avoid over-stripping short words
    suffixes = [
        "ations", "ation", "tions", "tion", "sions", "sion",
        "ments", "ment", "ness", "ence", "ance",
        "ives", "ive", "ous",
        "ting", "sing", "ning", "ling", "ring", "ving", "zing", "ging",
        "ing",
        "ies", "es", "ed", "ly", "s",
    ]
    for suffix in suffixes:
        if w.endswith(suffix) and len(w) - len(suffix) >= 4:
            w = w[: -len(suffix)]
            break

    # Truncate to 5 chars to collapse remaining close variants
    if len(w) > 5:
        w = w[:5]
    return w


def stem_set(words: set[str] | list[str]) -> set[str]:
    """Stem a collection of words into a set of stems."""
    return {stem(w) for w in words}


FILLER_WORDS = {"and", "the", "a", "an", "of", "in", "to", "with", "your", "or", "for", "is", "are"}
# For IDs, keep "for", "while", "do" etc. — they're meaningful in programming context
ID_FILLER_WORDS = {"and", "the", "a", "an", "of", "in", "to", "with"}


def normalize_id(topic_id: str) -> str:
    """Strip prefix, remove fillers, stem each word, join preserving order."""
    cleaned = strip_prefix(topic_id)
    words = [w for w in cleaned.lower().split("-") if w not in ID_FILLER_WORDS]
    if not words:
        words = cleaned.lower().split("-")
    return "".join(stem(w) for w in words)


def id_words(topic_id: str) -> set[str]:
    """Get the stemmed set of meaningful hyphen-delimited words from a prefix-stripped ID."""
    cleaned = strip_prefix(topic_id)
    raw = set(cleaned.lower().split("-"))
    meaningful = raw - ID_FILLER_WORDS
    return stem_set(meaningful) if meaningful else stem_set(raw)


def title_words(title: str) -> set[str]:
    """Get the stemmed set of meaningful words from a title."""
    t = title.lower()
    t = re.sub(r"[^a-z0-9\s]", "", t)
    raw = set(t.split())
    meaningful = raw - FILLER_WORDS - {"basics", "basic", "intro", "introduction", "introducing", "fundamentals"}
    return stem_set(meaningful) if meaningful else stem_set(raw)


def sentence_words(sentence: str) -> set[str]:
    """Get stemmed content words from a sentence."""
    t = sentence.lower()
    t = re.sub(r"[^a-z0-9\s]", "", t)
    raw = set(t.split())
    meaningful = raw - FILLER_WORDS - {"that", "this", "which", "from", "by", "it", "its", "on", "at", "as", "be", "an"}
    return stem_set(meaningful) if meaningful else stem_set(raw)


def jaccard(set_a: set, set_b: set) -> float:
    """Jaccard similarity between two sets."""
    if not set_a or not set_b:
        return 0.0
    return len(set_a & set_b) / len(set_a | set_b)


# Stems of core programming concepts — when two IDs differ by one of these,
# they're about genuinely different topics (e.g., "for" vs "while", "array" vs "list")
CORE_CONCEPT_STEMS = stem_set({
    "for", "while", "do", "if", "else", "switch", "class", "object", "function",
    "method", "array", "list", "string", "integer", "float", "boolean", "recursion",
    "file", "exception", "variable", "scope", "type", "return", "parameter",
    "nested", "break", "continue",
})


def compute_similarity(a: dict, b: dict) -> float:
    """Compute a similarity score between two topics. Higher = more similar."""
    score = 0.0

    norm_a = normalize_id(a["id"])
    norm_b = normalize_id(b["id"])

    # Exact normalized ID match (after prefix strip + hyphen removal)
    if norm_a == norm_b:
        score += 5.0
    # One normalized ID is a substring of the other
    elif norm_a in norm_b or norm_b in norm_a:
        score += 3.0
    else:
        # Stemmed word overlap from hyphen-split IDs (require 2+ shared words)
        iw_a = id_words(a["id"])
        iw_b = id_words(b["id"])
        overlap_count = len(iw_a & iw_b)
        j = jaccard(iw_a, iw_b)
        # Penalty: if BOTH sides contribute different core concepts to the
        # symmetric difference, they're likely about genuinely different things
        # (e.g., "for-loop-iteration" vs "while-loop-iteration" — "for" vs "while")
        only_a = (iw_a - iw_b) & CORE_CONCEPT_STEMS
        only_b = (iw_b - iw_a) & CORE_CONCEPT_STEMS
        core_clash = len(only_a) > 0 and len(only_b) > 0
        if overlap_count >= 2 and j >= 0.5 and not core_clash:
            score += 3.0 * j
        elif overlap_count >= 2 and j >= 0.5 and core_clash:
            score += 1.5 * j  # reduced score when core concepts clash
        elif overlap_count >= 2 and (iw_a <= iw_b or iw_b <= iw_a):
            score += 2.0

    # Title comparison (stemmed words, fillers removed; require 2+ shared words)
    tw_a = title_words(a["title"])
    tw_b = title_words(b["title"])
    t_overlap = len(tw_a & tw_b)
    tj = jaccard(tw_a, tw_b)
    if t_overlap >= 2 and tj >= 0.4:
        score += 2.5 * tj
    elif t_overlap >= 2 and (tw_a <= tw_b or tw_b <= tw_a):
        score += 1.5

    # First sentence comparison (stemmed content words)
    if a["first_sentence"] and b["first_sentence"]:
        sw_a = sentence_words(a["first_sentence"][:100])
        sw_b = sentence_words(b["first_sentence"][:100])
        sj = jaccard(sw_a, sw_b)
        if sj >= 0.3:
            score += 2.0 * sj  # up to 2.0 for perfect sentence overlap

    return score


SIMILARITY_THRESHOLD = 2.5


def group_topics(topics: list[dict]) -> list[list[dict]]:
    """Group topics by semantic similarity using star clustering.

    Each cluster has a seed pair. A topic joins a cluster only if it is
    directly similar to at least one of the seed pair members. Clusters
    never merge after creation — this prevents transitive chains from
    bridging unrelated concepts (e.g., for-loops and while-loops linked
    through generic "loop-patterns").
    """
    n = len(topics)

    # Compute all pairwise similarities above threshold
    sim_cache: dict[tuple[int, int], float] = {}
    edges: list[tuple[float, int, int]] = []
    for i in range(n):
        for j in range(i + 1, n):
            sim = compute_similarity(topics[i], topics[j])
            if sim >= SIMILARITY_THRESHOLD:
                sim_cache[(i, j)] = sim
                sim_cache[(j, i)] = sim
                edges.append((sim, i, j))

    # Sort edges strongest first
    edges.sort(reverse=True)

    # Star clustering: seed from strongest edges, assign by seed similarity
    cluster_of: dict[int, int] = {}  # topic index -> cluster id
    clusters: dict[int, list[int]] = {}  # cluster id -> member indices
    seeds: dict[int, tuple[int, int]] = {}  # cluster id -> (seed1, seed2)
    next_cluster = 0

    for sim, i, j in edges:
        ci = cluster_of.get(i)
        cj = cluster_of.get(j)

        if ci is None and cj is None:
            # Create new cluster with i,j as seeds
            cluster_of[i] = next_cluster
            cluster_of[j] = next_cluster
            clusters[next_cluster] = [i, j]
            seeds[next_cluster] = (i, j)
            next_cluster += 1

        elif ci is not None and cj is None:
            # j wants to join i's cluster — only if j matches a seed
            s1, s2 = seeds[ci]
            if sim_cache.get((j, s1), 0) >= SIMILARITY_THRESHOLD or \
               sim_cache.get((j, s2), 0) >= SIMILARITY_THRESHOLD:
                clusters[ci].append(j)
                cluster_of[j] = ci

        elif ci is None and cj is not None:
            # i wants to join j's cluster — only if i matches a seed
            s1, s2 = seeds[cj]
            if sim_cache.get((i, s1), 0) >= SIMILARITY_THRESHOLD or \
               sim_cache.get((i, s2), 0) >= SIMILARITY_THRESHOLD:
                clusters[cj].append(i)
                cluster_of[i] = cj

        # If both already assigned (to same or different clusters), skip.
        # Clusters never merge.

    # Collect all groups (including singletons)
    grouped = set()
    result = []
    for cid, members in clusters.items():
        result.append(members)
        grouped.update(members)

    for i in range(n):
        if i not in grouped:
            result.append([i])

    return result


# ---------------------------------------------------------------------------
# Winner selection
# ---------------------------------------------------------------------------

STATUS_PRIORITY = {"validated": 2, "draft": 1, "reference": 0, "": 0}


def pick_winner(group: list[dict], ref_counts: dict[str, int]) -> tuple[dict, list[dict]]:
    """Pick the best topic from a duplicate group."""
    def sort_key(t):
        return (
            STATUS_PRIORITY.get(t["status"], 0),
            ref_counts.get(t["id"], 0),
            -len(t["id"]),  # shorter ID is better (negative because we want ascending sort for shorter)
        )

    ranked = sorted(group, key=sort_key, reverse=True)
    winner = ranked[0]
    losers = ranked[1:]
    return winner, losers


# ---------------------------------------------------------------------------
# Concept name derivation
# ---------------------------------------------------------------------------

def derive_concept_name(group: list[dict]) -> str:
    """Derive a human-readable concept name for the group."""
    # Use the shortest ID (after stripping prefix) as the concept name
    ids = [t["id"] for t in group]
    cleaned = []
    for tid in ids:
        c = tid
        if c.startswith("programming-fundamentals-"):
            c = c[len("programming-fundamentals-"):]
        cleaned.append(c)
    return min(cleaned, key=len)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    # 1. Read all .md files in programming-fundamentals
    topics = []
    for md_file in sorted(PF_DIR.glob("*.md")):
        topic = read_topic_file(md_file)
        if topic:
            topics.append(topic)

    if not topics:
        print("ERROR: No topic files found.", file=sys.stderr)
        sys.exit(1)

    print(f"Read {len(topics)} topic files from programming-fundamentals/", file=sys.stderr)

    # 2. Count references across all domains
    all_ids = {t["id"] for t in topics}
    print(f"Counting references across all domains...", file=sys.stderr)
    ref_counts = count_references(all_ids, DOMAINS_DIR)
    print(f"Found references for {len(ref_counts)} topic IDs", file=sys.stderr)

    # 3. Group by similarity
    group_indices = group_topics(topics)

    # Separate singletons from duplicate groups
    duplicate_groups = []
    singletons = []
    for indices in group_indices:
        if len(indices) == 1:
            singletons.append(topics[indices[0]]["file"])
        else:
            group = [topics[i] for i in indices]
            duplicate_groups.append(group)

    # 4. Build merge plan
    output_groups = []
    total_files_to_delete = 0

    for group in duplicate_groups:
        winner, losers = pick_winner(group, ref_counts)
        concept = derive_concept_name(group)

        # For each loser, identify unique prereqs/builds-toward not in winner
        winner_prereqs = set(winner["prerequisites"])
        winner_builds = set(winner["builds_toward"])

        loser_entries = []
        for loser in losers:
            unique_prereqs = [p for p in loser["prerequisites"] if p not in winner_prereqs]
            unique_builds = [b for b in loser["builds_toward"] if b not in winner_builds]
            loser_entries.append({
                "id": loser["id"],
                "file": loser["file"],
                "title": loser["title"],
                "status": loser["status"],
                "refs": ref_counts.get(loser["id"], 0),
                "unique_prereqs": unique_prereqs,
                "unique_builds_toward": unique_builds,
            })

        total_files_to_delete += len(losers)

        output_groups.append({
            "concept": concept,
            "winner": {
                "id": winner["id"],
                "file": winner["file"],
                "title": winner["title"],
                "status": winner["status"],
                "refs": ref_counts.get(winner["id"], 0),
            },
            "losers": loser_entries,
        })

    # Sort groups by size (largest first), then concept name
    output_groups.sort(key=lambda g: (-len(g["losers"]), g["concept"]))
    singletons.sort()

    plan = {
        "groups": output_groups,
        "singletons": singletons,
        "total_files": len(topics),
        "total_groups": len(duplicate_groups),
        "files_to_delete": total_files_to_delete,
    }

    print(json.dumps(plan, indent=2))


if __name__ == "__main__":
    main()
