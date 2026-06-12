#!/usr/bin/env python3
"""Validate the SEO surface of every generated page — deterministically, not by sample.

purpose: full-corpus check that the pages the distribution strategy depends on
         are individually well-formed (meta description, canonical, og:title,
         parseable LearningResource JSON-LD) and that sitemap.xml is complete.
inputs:  output/ (generated site), output/sitemap.xml
outputs: pass/fail exit code + violation summary on stdout
last_run: every CI deploy (.github/workflows/deploy-pages.yml), after sitemap step

Exists because sample-verification on a 15k-page surface is the failure mode:
a malformed long-tail poisons the SEO asset silently (retro 2026-06-12).

Usage:
    python tools/validate_seo.py
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = ROOT / "output"
TOPICS_DIR = OUTPUT_DIR / "topics"

sys.path.insert(0, str(ROOT / "tools"))
from parse_topic import SITE_BASE_URL

HEAD_BYTES = 65536  # head section incl. JSON-LD comfortably fits

DESC_RE = re.compile(r'<meta name="description" content="([^"]*)"')
CANON_RE = re.compile(r'<link rel="canonical" href="([^"]*)"')
OG_TITLE_RE = re.compile(r'<meta property="og:title" content="([^"]*)"')
OG_IMG_RE = re.compile(r'<meta property="og:image" content="([^"]*)"')
JSONLD_RE = re.compile(r'<script type="application/ld\+json">(.*?)</script>', re.DOTALL)
MIN_TOPIC_PAGES = 15000  # tripwire against silently-empty generation


def check_page(path, rel_url, expect_jsonld):
    """Return list of violation strings for one page."""
    head = path.read_text(encoding="utf-8", errors="replace")[:HEAD_BYTES]
    violations = []

    m = DESC_RE.search(head)
    if not m or not m.group(1).strip():
        violations.append("missing/empty meta description")

    m = CANON_RE.search(head)
    expected = SITE_BASE_URL + "/" + rel_url
    if not m:
        violations.append("missing canonical")
    elif m.group(1) != expected:
        violations.append(f"canonical mismatch: {m.group(1)!r} != {expected!r}")

    if not OG_TITLE_RE.search(head):
        violations.append("missing og:title")

    m = OG_IMG_RE.search(head)
    if not m:
        violations.append("missing og:image")
    else:
        # og:image must point at a file that actually shipped (per-topic card
        # or og/default.png) — a dangling card URL renders as a blank unfurl.
        img_rel = m.group(1).replace(SITE_BASE_URL, "").lstrip("/")
        if not (OUTPUT_DIR / img_rel).exists():
            violations.append(f"og:image file absent: {img_rel}")

    if expect_jsonld:
        m = JSONLD_RE.search(head)
        if not m:
            violations.append("missing JSON-LD")
        else:
            try:
                ld = json.loads(m.group(1))
                if ld.get("@type") != "LearningResource":
                    violations.append(f"JSON-LD @type is {ld.get('@type')!r}")
                if not ld.get("educationalLevel"):
                    violations.append("JSON-LD missing educationalLevel")
            except json.JSONDecodeError as e:
                violations.append(f"JSON-LD does not parse: {e}")

    return violations


def main():
    failures = {}  # rel_url -> [violations]

    def record(rel_url, violations):
        if violations:
            failures[rel_url] = violations

    # 1. Topic + question pages — expected set derived from domains/ ground truth.
    # Files in output/topics NOT in the expected set are orphans from deleted/
    # renamed topics; they accumulate locally (the generator never deletes) but
    # cannot ship via CI's fresh build, so they warn rather than fail.
    topic_stems = set()
    for f in (ROOT / "domains").rglob("*.md"):
        if not f.name.startswith("_"):
            topic_stems.add(f.stem)
    expected_stems = topic_stems | {s + "-questions" for s in topic_stems}

    topic_pages = sorted(TOPICS_DIR.glob("*.html"))
    n_topics = 0
    orphans = 0
    for p in topic_pages:
        if p.stem not in expected_stems:
            orphans += 1
            continue
        # A "-questions" suffix only marks a question page if the base is a real
        # topic — 5 actual topics have IDs ending in "-questions" themselves.
        is_question_page = (p.stem.endswith("-questions")
                            and p.stem[:-len("-questions")] in topic_stems)
        if not is_question_page:
            n_topics += 1
        record(f"topics/{p.name}", check_page(p, f"topics/{p.name}",
                                              expect_jsonld=not is_question_page))

    if orphans:
        print(f"WARNING: {orphans} orphan page(s) in output/topics (no source topic; "
              "stale local build artifacts — safe to delete, never deployed by CI)")
    if n_topics < MIN_TOPIC_PAGES:
        failures["<corpus>"] = [f"only {n_topics} topic pages found (tripwire: {MIN_TOPIC_PAGES})"]

    # 2. Main pages
    for name, rel in [("index.html", ""), ("radial-graph.html", "radial-graph.html"),
                      ("quiz.html", "quiz.html")]:
        p = OUTPUT_DIR / name
        if p.exists():
            record(name, check_page(p, rel, expect_jsonld=False))
        else:
            failures[name] = ["file missing"]

    # 3. Sitemap completeness: every listed URL must exist as a file; count sane
    sitemap = OUTPUT_DIR / "sitemap.xml"
    if not sitemap.exists():
        failures["sitemap.xml"] = ["file missing"]
    else:
        locs = re.findall(r"<loc>([^<]+)</loc>", sitemap.read_text(encoding="utf-8"))
        if len(locs) < MIN_TOPIC_PAGES:
            failures.setdefault("sitemap.xml", []).append(
                f"only {len(locs)} URLs (tripwire: {MIN_TOPIC_PAGES}; the Jun-11 wrong-glob bug produced 22)")
        missing = 0
        for loc in locs:
            rel = loc.replace(SITE_BASE_URL, "").lstrip("/")
            target = OUTPUT_DIR / (rel if rel else "index.html")
            if not target.exists():
                missing += 1
                if missing <= 5:
                    failures.setdefault("sitemap.xml", []).append(f"listed but absent: {rel}")
        if missing > 5:
            failures.setdefault("sitemap.xml", []).append(f"...and {missing - 5} more absent files")

    # Report
    total_checked = len(topic_pages) + 3 + 1
    if failures:
        print(f"SEO VALIDATION FAILED — {len(failures)} page(s) with violations "
              f"(of {total_checked} checked):")
        for rel_url, violations in list(failures.items())[:10]:
            print(f"  {rel_url}:")
            for v in violations[:4]:
                print(f"    - {v}")
        if len(failures) > 10:
            print(f"  ...and {len(failures) - 10} more pages")
        sys.exit(1)
    print(f"SEO validation passed: {len(topic_pages)} topic/question pages + main pages "
          f"+ sitemap ({n_topics} topics) all well-formed.")


if __name__ == "__main__":
    main()
