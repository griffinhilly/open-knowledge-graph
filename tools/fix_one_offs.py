"""
Fix specific one-off prerequisite ID issues:

1. busy-beaver-function: prereq "undecidability-and-gödel" (with ö U+00F6)
   -> The target file also uses ö in its ID, but IDs should be ASCII-only.
   -> Fix the prereq to use ASCII "undecidability-and-godel" and also fix
      the target file's ID and filename to match.

2. expense-tracking-and-categorization: prereq "collecting-organizing-data-3rd"
   -> Doesn't exist. Actual topic is "collecting-and-organizing-data-3rd".
   -> Fix the prereq ID.
"""

import os
import re
import unicodedata

DOMAINS_DIR = os.path.join(os.path.dirname(__file__), '..', 'domains')
DOMAINS_DIR = os.path.normpath(DOMAINS_DIR)


def build_topic_lookup():
    """Build a dict of topic_id -> filepath for all topics."""
    lookup = {}
    for root, dirs, files in os.walk(DOMAINS_DIR):
        for fname in files:
            if not fname.endswith('.md') or fname.startswith('_'):
                continue
            fpath = os.path.join(root, fname)
            with open(fpath, 'r', encoding='utf-8') as f:
                content = f.read()
            m = re.search(r'^id:\s*(.+)$', content, re.MULTILINE)
            if m:
                tid = m.group(1).strip()
                lookup[tid] = fpath
    return lookup


def ascii_normalize(s):
    """Convert unicode chars to closest ASCII equivalent."""
    # Decompose unicode, drop combining marks, encode to ASCII
    nfkd = unicodedata.normalize('NFKD', s)
    return nfkd.encode('ascii', 'ignore').decode('ascii')


def fix_busy_beaver(lookup):
    """Fix the ö in undecidability-and-gödel prereq and target file."""
    changes = []

    bad_id = 'undecidability-and-g\u00f6del'
    good_id = 'undecidability-and-godel'

    # --- Fix 1a: Rename the target file's ID ---
    if bad_id in lookup:
        target_path = lookup[bad_id]
        with open(target_path, 'r', encoding='utf-8') as f:
            content = f.read()

        new_content = re.sub(
            r'^(id:\s*)' + re.escape(bad_id) + r'$',
            r'\g<1>' + good_id,
            content,
            count=1,
            flags=re.MULTILINE,
        )

        if new_content != content:
            with open(target_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"  Fixed target file ID: {bad_id!r} -> {good_id!r}")
            print(f"    file: {target_path}")
            changes.append(('target-id', target_path, bad_id, good_id))

        # Rename the file itself
        target_dir = os.path.dirname(target_path)
        old_fname = os.path.basename(target_path)
        new_fname = ascii_normalize(old_fname)
        if new_fname != old_fname:
            new_path = os.path.join(target_dir, new_fname)
            os.rename(target_path, new_path)
            print(f"  Renamed file: {old_fname!r} -> {new_fname!r}")
            changes.append(('rename', target_path, old_fname, new_fname))
            # Update lookup
            lookup[good_id] = new_path

    # --- Fix 1b: Fix the prereq in busy-beaver-function ---
    bb_id = 'busy-beaver-function'
    if bb_id in lookup:
        bb_path = lookup[bb_id]
        with open(bb_path, 'r', encoding='utf-8') as f:
            content = f.read()

        if bad_id in content:
            new_content = content.replace(bad_id, good_id)
            with open(bb_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"  Fixed prereq in busy-beaver-function: {bad_id!r} -> {good_id!r}")
            print(f"    file: {bb_path}")
            changes.append(('prereq', bb_path, bad_id, good_id))
        else:
            print(f"  busy-beaver-function: prereq already uses ASCII ID")

    # Also fix any OTHER files that reference the old ö ID
    for tid, fpath in list(lookup.items()):
        if tid in (bb_id, bad_id, good_id):
            continue
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        if bad_id in content:
            new_content = content.replace(bad_id, good_id)
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"  Also fixed reference in {tid}: {bad_id!r} -> {good_id!r}")
            changes.append(('other-ref', fpath, bad_id, good_id))

    return changes


def fix_expense_tracking(lookup):
    """Fix collecting-organizing-data-3rd -> collecting-and-organizing-data-3rd."""
    changes = []

    bad_prereq = 'collecting-organizing-data-3rd'
    good_prereq = 'collecting-and-organizing-data-3rd'

    # Verify the good ID exists
    if good_prereq not in lookup:
        print(f"  WARNING: Expected topic {good_prereq!r} not found in lookup!")
        # Try to find closest match
        candidates = [tid for tid in lookup if 'collecting' in tid and 'data' in tid and '3rd' in tid]
        if candidates:
            good_prereq = candidates[0]
            print(f"  Using closest match: {good_prereq!r}")
        else:
            print(f"  No matching topic found. Removing prereq.")
            # We'll handle removal below

    et_id = 'expense-tracking-and-categorization'
    if et_id in lookup:
        et_path = lookup[et_id]
        with open(et_path, 'r', encoding='utf-8') as f:
            content = f.read()

        if bad_prereq in content:
            if good_prereq in lookup:
                new_content = content.replace(bad_prereq, good_prereq)
                action = f'{bad_prereq!r} -> {good_prereq!r}'
            else:
                # Remove the entire prereq entry
                new_content = re.sub(
                    r'-\s*id:\s*' + re.escape(bad_prereq) + r'\n\s*type:\s*\w+\n',
                    '',
                    content,
                )
                action = f'removed {bad_prereq!r} (no match found)'

            with open(et_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"  Fixed prereq in expense-tracking-and-categorization: {action}")
            print(f"    file: {et_path}")
            changes.append(('prereq', et_path, bad_prereq, good_prereq))
        else:
            print(f"  expense-tracking-and-categorization: prereq already correct")

    return changes


def main():
    print("Building topic lookup...\n")
    lookup = build_topic_lookup()
    print(f"Found {len(lookup)} topics.\n")

    print("Fix 1: busy-beaver-function / undecidability-and-gödel")
    changes1 = fix_busy_beaver(lookup)
    print()

    print("Fix 2: expense-tracking-and-categorization / collecting-organizing-data-3rd")
    changes2 = fix_expense_tracking(lookup)
    print()

    total = len(changes1) + len(changes2)
    print(f"Done. {total} changes applied.")


if __name__ == '__main__':
    main()
