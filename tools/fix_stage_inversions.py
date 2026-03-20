"""
Fix stage inversions: promote topics whose stage is less advanced than their
most-advanced prerequisite's stage.

Stage ordering: pre-formal(0) < concrete-operations(1) < abstract-reasoning(2)
              < formal-systems(3) < advanced(4)
"""

import os
import re
import sys

DOMAINS_DIR = os.path.join(os.path.dirname(__file__), '..', 'domains')
DOMAINS_DIR = os.path.normpath(DOMAINS_DIR)

STAGE_ORDER = {
    'pre-formal': 0,
    'concrete-operations': 1,
    'abstract-reasoning': 2,
    'formal-systems': 3,
    'advanced': 4,
}
STAGE_NAME = {v: k for k, v in STAGE_ORDER.items()}


def load_all_topics():
    """Load all topic files, return dict of topic_id -> {stage, prereqs, filepath}."""
    topics = {}
    for root, dirs, files in os.walk(DOMAINS_DIR):
        for fname in files:
            if not fname.endswith('.md') or fname.startswith('_'):
                continue
            fpath = os.path.join(root, fname)
            with open(fpath, 'r', encoding='utf-8') as f:
                content = f.read()

            # Extract id
            m_id = re.search(r'^id:\s*(.+)$', content, re.MULTILINE)
            if not m_id:
                continue
            topic_id = m_id.group(1).strip()

            # Extract stage
            m_stage = re.search(r'^stage:\s*(.+)$', content, re.MULTILINE)
            if not m_stage:
                continue
            stage = m_stage.group(1).strip()

            # Extract prerequisite IDs
            prereqs = re.findall(r'-\s*id:\s*(.+)', content)
            prereqs = [p.strip() for p in prereqs if p.strip() != topic_id]

            topics[topic_id] = {
                'stage': stage,
                'prereqs': prereqs,
                'filepath': fpath,
            }
    return topics


def fix_inversions(topics):
    """Find and fix stage inversions. Returns list of changes made."""
    changes = []
    changed = True

    # Iterate until no more changes (cascading promotions)
    pass_num = 0
    while changed:
        changed = False
        pass_num += 1
        for topic_id, info in topics.items():
            current_rank = STAGE_ORDER.get(info['stage'])
            if current_rank is None:
                continue

            max_prereq_rank = -1
            max_prereq_id = None
            for prereq_id in info['prereqs']:
                prereq_info = topics.get(prereq_id)
                if prereq_info is None:
                    continue
                prereq_rank = STAGE_ORDER.get(prereq_info['stage'], -1)
                if prereq_rank > max_prereq_rank:
                    max_prereq_rank = prereq_rank
                    max_prereq_id = prereq_id

            if max_prereq_rank > current_rank:
                new_stage = STAGE_NAME[max_prereq_rank]
                old_stage = info['stage']
                changes.append({
                    'topic_id': topic_id,
                    'filepath': info['filepath'],
                    'old_stage': old_stage,
                    'new_stage': new_stage,
                    'reason': f'prereq "{max_prereq_id}" is at {STAGE_NAME[max_prereq_rank]}',
                    'pass': pass_num,
                })
                info['stage'] = new_stage
                changed = True

    return changes


def apply_changes(changes):
    """Write stage changes back to files using regex replacement."""
    # Group by filepath (a topic only appears once)
    for change in changes:
        fpath = change['filepath']
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Replace stage line in YAML frontmatter (between --- markers)
        new_content = re.sub(
            r'^(stage:\s*).+$',
            r'\g<1>' + change['new_stage'],
            content,
            count=1,
            flags=re.MULTILINE,
        )

        if new_content != content:
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(new_content)


def main():
    print("Loading all topics...")
    topics = load_all_topics()
    print(f"Loaded {len(topics)} topics.")

    print("\nChecking for stage inversions...")
    changes = fix_inversions(topics)

    if not changes:
        print("No stage inversions found.")
        return

    print(f"\nFound {len(changes)} stage inversions to fix:\n")
    for c in changes:
        print(f"  [{c['topic_id']}]")
        print(f"    {c['old_stage']} -> {c['new_stage']} (pass {c['pass']})")
        print(f"    reason: {c['reason']}")
        print(f"    file: {c['filepath']}")
        print()

    apply_changes(changes)
    print(f"Applied {len(changes)} stage promotions.")


if __name__ == '__main__':
    main()
