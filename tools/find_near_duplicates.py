#!/usr/bin/env python3
"""Find near-duplicate topic IDs within each course.

Detects pairs where one ID is a substring/prefix of another, or where
IDs differ only by a suffix like '-intro', '-basics', numbers vs words, etc.
"""

import os
import re
from pathlib import Path
from collections import defaultdict
from difflib import SequenceMatcher

DOMAINS_DIR = Path(__file__).parent.parent / "domains"


def normalize_id(topic_id):
    """Normalize an ID for fuzzy matching."""
    # Remove common suffixes
    suffixes = [
        "-intro", "-introduction", "-basics", "-overview", "-fundamentals",
        "-advanced", "-detailed", "-concepts", "-principles",
    ]
    normalized = topic_id
    for s in suffixes:
        if normalized.endswith(s):
            normalized = normalized[: -len(s)]
            break

    # Normalize number words to digits
    word_to_num = {
        "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
        "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9",
        "ten": "10", "eleven": "11", "twelve": "12", "thirteen": "13",
        "fourteen": "14", "fifteen": "15", "sixteen": "16", "seventeen": "17",
        "eighteen": "18", "nineteen": "19", "twenty": "20",
    }
    parts = normalized.split("-")
    parts = [word_to_num.get(p, p) for p in parts]
    normalized = "-".join(parts)

    return normalized


def find_near_dupes_in_course(course_dir):
    """Find near-duplicate pairs within a single course."""
    topic_ids = []
    for f in course_dir.glob("*.md"):
        if f.name.startswith("_"):
            continue
        topic_ids.append(f.stem)

    if len(topic_ids) < 2:
        return []

    dupes = []
    normalized = {tid: normalize_id(tid) for tid in topic_ids}

    for i, id_a in enumerate(topic_ids):
        for id_b in topic_ids[i + 1 :]:
            norm_a = normalized[id_a]
            norm_b = normalized[id_b]

            # Check if normalized forms match
            if norm_a == norm_b:
                dupes.append((id_a, id_b, "normalized-match"))
                continue

            # Check if one is a prefix of the other
            if norm_a.startswith(norm_b) or norm_b.startswith(norm_a):
                dupes.append((id_a, id_b, "prefix-match"))
                continue

            # Check high similarity (>0.85)
            ratio = SequenceMatcher(None, norm_a, norm_b).ratio()
            if ratio > 0.85:
                dupes.append((id_a, id_b, f"similar-{ratio:.2f}"))

    return dupes


def main():
    total_dupes = 0
    for domain_dir in sorted(DOMAINS_DIR.iterdir()):
        if not domain_dir.is_dir() or domain_dir.name.startswith("."):
            continue
        for course_dir in sorted(domain_dir.iterdir()):
            if not course_dir.is_dir() or course_dir.name.startswith("_"):
                continue
            dupes = find_near_dupes_in_course(course_dir)
            if dupes:
                for id_a, id_b, reason in dupes:
                    print(f"  {domain_dir.name}/{course_dir.name}: {id_a} <-> {id_b} ({reason})")
                    total_dupes += 1

    print(f"\nTotal near-duplicate pairs found: {total_dupes}")


if __name__ == "__main__":
    main()
