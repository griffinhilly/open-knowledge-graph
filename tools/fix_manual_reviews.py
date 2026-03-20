"""
Fix script for manual review topics identified by dialectic review.

Group 1: Remove/replace pedagogically wrong geophysics prereqs from 13 geology topics
Group 2: Fix stages for 3 music topics (electronic-composition-fundamentals,
         harmonic-accompaniment-fundamentals, melody-composition-basics)
Group 3: Fix inverted prereq direction in 2 anatomy topics
         (brain-anatomy-and-functional-organization, cell-structure-organelles-and-function)
"""

import os
import re
import sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMAINS = os.path.join(BASE, "domains")

def read_file(path):
    with open(path, encoding="utf-8") as f:
        return f.read()

def write_file(path, content):
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)

def remove_prereq(content, prereq_id):
    """Remove a prerequisite entry (- id: X\\n  type: Y) from YAML frontmatter."""
    # Match the prereq block: "- id: prereq_id\n  type: hard/soft\n"
    pattern = re.compile(
        r"- id: " + re.escape(prereq_id) + r"\n\s+type: (?:hard|soft)\n",
        re.MULTILINE
    )
    new_content = pattern.sub("", content)
    if new_content == content:
        print(f"  WARNING: Could not find prereq '{prereq_id}' to remove")
        return content, False
    return new_content, True

def add_prereq(content, prereq_id, prereq_type="soft"):
    """Add a prerequisite entry after the last existing prereq."""
    # Find the prerequisites section and add after the last entry
    pattern = re.compile(
        r"(prerequisites:\n(?:- id: .+\n\s+type: (?:hard|soft)\n)+)"
    )
    match = pattern.search(content)
    if match:
        old_block = match.group(1)
        new_entry = f"- id: {prereq_id}\n  type: {prereq_type}\n"
        new_block = old_block + new_entry
        return content.replace(old_block, new_block), True
    else:
        print(f"  WARNING: Could not find prerequisites section to add '{prereq_id}'")
        return content, False

def change_stage(content, new_stage):
    """Change the stage field in YAML frontmatter."""
    pattern = re.compile(r"^stage: .+$", re.MULTILINE)
    new_content = pattern.sub(f"stage: {new_stage}", content)
    if new_content == content:
        print(f"  WARNING: Could not find stage field to change")
        return content, False
    return new_content, True

def move_prereq_to_builds_toward(content, prereq_id):
    """Move a prerequisite ID from prerequisites to builds-toward."""
    # First remove from prerequisites
    new_content, removed = remove_prereq(content, prereq_id)
    if not removed:
        return content, False

    # Then add to builds-toward
    bt_pattern = re.compile(r"^builds-toward:\n((?:- .+\n)*)", re.MULTILINE)
    bt_match = bt_pattern.search(new_content)
    if bt_match:
        old_bt = bt_match.group(0)
        new_bt = old_bt.rstrip("\n") + "\n- " + prereq_id + "\n"
        new_content = new_content.replace(old_bt, new_bt)
    else:
        # No builds-toward section exists; add one before tags
        tags_pattern = re.compile(r"^tags:", re.MULTILINE)
        tags_match = tags_pattern.search(new_content)
        if tags_match:
            insert_pos = tags_match.start()
            bt_section = f"builds-toward:\n- {prereq_id}\n"
            new_content = new_content[:insert_pos] + bt_section + new_content[insert_pos:]
        else:
            print(f"  WARNING: Could not find builds-toward or tags section")
            return content, False

    return new_content, True

def get_old_stage(content):
    m = re.search(r"^stage: (.+)$", content, re.MULTILINE)
    return m.group(1).strip() if m else "unknown"


# ===========================================================================
# GROUP 1: Geology - Remove/replace geophysics prereqs
# ===========================================================================

GEOLOGY_DIR = os.path.join(DOMAINS, "earth-and-space-sciences", "geology")

# Each entry: (topic_file, prereq_to_remove, replacement_prereq_or_None, replacement_type)
GEOLOGY_FIXES = [
    ("ductile-brittle-transition-deformation.md",
     "rock-rheology-elastic-plastic-deformation",
     None, None),
    # stress-strain-rock-deformation already a prereq via earthquakes-and-seismology chain

    ("earthquake-mechanisms-stress-release.md",
     "coulomb-stress-transfer",
     None, None),

    ("fold-fault-formation-stress-analysis.md",
     "stress-tensor-inversion-from-earthquakes",
     None, None),
    # stress-strain-rock-deformation already exists as same-course prereq

    ("groundwater-flow-hydrogeology-porosity-permeability.md",
     "fluid-flow-porous-media",
     None, None),

    ("paleomagnetic-reversal-magnetostratigraphy.md",
     "geomagnetic-reversal-chronology",
     None, None),

    ("plate-boundary-types-kinematics.md",
     "focal-mechanisms-and-stress-tensors",
     None, None),

    ("plate-tectonics.md",
     "mantle-convection-and-dynamics",
     None, None),

    ("plate-tectonics-continental-drift-evidence.md",
     "paleomagnetic-poles-and-plate-reconstruction",
     None, None),

    ("radiometric-dating-isotope-systems-geochronology.md",
     "radioactive-heat-production",
     None, None),

    ("rift-extension-crustal-thinning.md",
     "mantle-convection-and-dynamics",
     None, None),

    ("seismic-wave-velocity-attenuation.md",
     "elastic-wave-propagation-in-solids",
     None, None),

    ("seismic-waves-p-s-surface.md",
     "elastic-wave-propagation-in-solids",
     None, None),

    ("stress-strain-rock-deformation.md",
     "stress-tensor-inversion-from-earthquakes",
     None, None),
]

# ===========================================================================
# GROUP 2: Music - Stage corrections
# ===========================================================================

MUSIC_STAGE_FIXES = [
    (os.path.join(DOMAINS, "music", "composition", "electronic-composition-fundamentals.md"),
     "advanced"),
    (os.path.join(DOMAINS, "music", "composition", "harmonic-accompaniment-fundamentals.md"),
     "abstract-reasoning"),
    (os.path.join(DOMAINS, "music", "composition", "melody-composition-basics.md"),
     "abstract-reasoning"),
]

# ===========================================================================
# GROUP 3: Anatomy - Move prereqs to builds-toward
# ===========================================================================

ANATOMY_DIR = os.path.join(DOMAINS, "health-and-human-development", "anatomy-and-physiology")

# (topic_file, list_of_prereqs_to_move_to_builds_toward)
ANATOMY_FIXES = [
    ("brain-anatomy-and-functional-organization.md",
     ["basal-ganglia", "cerebellum", "amygdala-emotion", "hippocampus-memory"]),
    ("cell-structure-organelles-and-function.md",
     ["mitochondria-structure-and-function", "mitochondrion-energy-production"]),
]


def main():
    changes = []
    errors = []

    # --- GROUP 1: Geology prereq removal ---
    print("=" * 70)
    print("GROUP 1: Geology - Removing pedagogically wrong geophysics prerequisites")
    print("=" * 70)

    for filename, prereq_to_remove, replacement, rep_type in GEOLOGY_FIXES:
        filepath = os.path.join(GEOLOGY_DIR, filename)
        if not os.path.exists(filepath):
            errors.append(f"File not found: {filepath}")
            continue

        content = read_file(filepath)
        topic_id = filename.replace(".md", "")
        print(f"\n--- {topic_id} ---")

        # Remove the bad prereq
        new_content, removed = remove_prereq(content, prereq_to_remove)
        if removed:
            print(f"  REMOVED prereq: {prereq_to_remove}")
            changes.append({
                "topic": topic_id,
                "group": "geology",
                "action": "remove_prereq",
                "removed": prereq_to_remove,
            })
        else:
            errors.append(f"Could not remove {prereq_to_remove} from {topic_id}")

        # Add replacement if specified
        if replacement and removed:
            new_content, added = add_prereq(new_content, replacement, rep_type or "soft")
            if added:
                print(f"  ADDED prereq: {replacement} (type: {rep_type or 'soft'})")
                changes[-1]["replacement"] = replacement
            else:
                errors.append(f"Could not add replacement {replacement} to {topic_id}")

        if new_content != content:
            write_file(filepath, new_content)

    # --- GROUP 2: Music stage corrections ---
    print("\n" + "=" * 70)
    print("GROUP 2: Music - Stage corrections")
    print("=" * 70)

    for filepath, new_stage in MUSIC_STAGE_FIXES:
        if not os.path.exists(filepath):
            errors.append(f"File not found: {filepath}")
            continue

        content = read_file(filepath)
        topic_id = os.path.basename(filepath).replace(".md", "")
        old_stage = get_old_stage(content)
        print(f"\n--- {topic_id} ---")

        if old_stage == new_stage:
            print(f"  SKIP: Already at {new_stage}")
            continue

        new_content, changed = change_stage(content, new_stage)
        if changed:
            print(f"  CHANGED stage: {old_stage} -> {new_stage}")
            changes.append({
                "topic": topic_id,
                "group": "music",
                "action": "change_stage",
                "old_stage": old_stage,
                "new_stage": new_stage,
            })
            write_file(filepath, new_content)
        else:
            errors.append(f"Could not change stage for {topic_id}")

    # --- GROUP 3: Anatomy prereq direction fixes ---
    print("\n" + "=" * 70)
    print("GROUP 3: Anatomy - Moving inverted prereqs to builds-toward")
    print("=" * 70)

    for filename, prereqs_to_move in ANATOMY_FIXES:
        filepath = os.path.join(ANATOMY_DIR, filename)
        if not os.path.exists(filepath):
            errors.append(f"File not found: {filepath}")
            continue

        content = read_file(filepath)
        topic_id = filename.replace(".md", "")
        print(f"\n--- {topic_id} ---")

        for prereq_id in prereqs_to_move:
            content, moved = move_prereq_to_builds_toward(content, prereq_id)
            if moved:
                print(f"  MOVED to builds-toward: {prereq_id}")
                changes.append({
                    "topic": topic_id,
                    "group": "anatomy",
                    "action": "move_to_builds_toward",
                    "prereq": prereq_id,
                })
            else:
                errors.append(f"Could not move {prereq_id} in {topic_id}")

        write_file(filepath, content)

    # --- Summary ---
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"Total changes applied: {len(changes)}")
    print(f"  Geology prereq removals: {sum(1 for c in changes if c['group'] == 'geology')}")
    print(f"  Music stage changes: {sum(1 for c in changes if c['group'] == 'music')}")
    print(f"  Anatomy prereq moves: {sum(1 for c in changes if c['group'] == 'anatomy')}")
    if errors:
        print(f"\nErrors ({len(errors)}):")
        for e in errors:
            print(f"  - {e}")

    return changes, errors


if __name__ == "__main__":
    changes, errors = main()
    sys.exit(1 if errors else 0)
