"""Scan all topic files for missing ## Questions and ## Explainer sections."""

import os
from collections import defaultdict

DOMAINS_DIR = "C:/Users/griff/Projects/griffin/open-knowledge-graph/domains"
TOOLS_DIR = "C:/Users/griff/Projects/griffin/open-knowledge-graph/tools"

SKIP_FILES = {"_domain.yml"}

missing_questions = []  # list of (domain, course, filename, rel_path)
missing_explainers = []
missing_both = []
total_topics = 0

# Walk all domain directories
for domain in sorted(os.listdir(DOMAINS_DIR)):
    domain_path = os.path.join(DOMAINS_DIR, domain)
    if not os.path.isdir(domain_path):
        continue
    for course in sorted(os.listdir(domain_path)):
        course_path = os.path.join(domain_path, course)
        if not os.path.isdir(course_path):
            continue
        for fname in sorted(os.listdir(course_path)):
            if fname in SKIP_FILES:
                continue
            if not fname.endswith(".md"):
                continue
            fpath = os.path.join(course_path, fname)
            if not os.path.isfile(fpath):
                continue

            total_topics += 1
            with open(fpath, "r", encoding="utf-8") as f:
                content = f.read()

            has_questions = "\n## Questions" in content
            has_explainer = "\n## Explainer" in content

            rel_path = f"domains/{domain}/{course}/{fname}"

            if not has_questions and not has_explainer:
                missing_both.append(rel_path)
            if not has_questions:
                missing_questions.append(rel_path)
            if not has_explainer:
                missing_explainers.append(rel_path)

# Group by domain/course
def group_by_domain_course(paths):
    grouped = defaultdict(list)
    for p in paths:
        parts = p.split("/")
        key = f"{parts[1]}/{parts[2]}"
        grouped[key].append(parts[3])
    return grouped

mq_grouped = group_by_domain_course(missing_questions)
me_grouped = group_by_domain_course(missing_explainers)

# Print summary
print("=" * 70)
print("MISSING SECTIONS SCAN RESULTS")
print("=" * 70)
print(f"Total topic files scanned: {total_topics}")
print(f"Missing ## Questions:      {len(missing_questions)}")
print(f"Missing ## Explainer:      {len(missing_explainers)}")
print(f"Missing BOTH:              {len(missing_both)}")
print()

# Questions detail
print("=" * 70)
print(f"TOPICS MISSING ## Questions ({len(missing_questions)} total)")
print("=" * 70)
for dc in sorted(mq_grouped.keys()):
    files = mq_grouped[dc]
    print(f"\n  {dc}/ ({len(files)} topics)")
    for f in files:
        print(f"    - {f}")

print()

# Explainer detail
print("=" * 70)
print(f"TOPICS MISSING ## Explainer ({len(missing_explainers)} total)")
print("=" * 70)
for dc in sorted(me_grouped.keys()):
    files = me_grouped[dc]
    print(f"\n  {dc}/ ({len(files)} topics)")
    for f in files:
        print(f"    - {f}")

# Save to files
with open(os.path.join(TOOLS_DIR, "tmp_missing_questions.txt"), "w", encoding="utf-8") as f:
    for p in missing_questions:
        f.write(p + "\n")

with open(os.path.join(TOOLS_DIR, "tmp_missing_explainers.txt"), "w", encoding="utf-8") as f:
    for p in missing_explainers:
        f.write(p + "\n")

print()
print(f"Saved: tools/tmp_missing_questions.txt ({len(missing_questions)} paths)")
print(f"Saved: tools/tmp_missing_explainers.txt ({len(missing_explainers)} paths)")
