#!/usr/bin/env python3
"""Split restaging data into per-course batch files for swarm agents."""

import json
from pathlib import Path

DATA_PATH = Path(__file__).parent / "restaging_data.json"
BATCH_DIR = Path(__file__).parent / "restaging_batches"
BATCH_DIR.mkdir(exist_ok=True)

with open(DATA_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

# Group courses into agent batches (aim for ~150-250 topics per batch)
batches = {
    "batch_01_math_pure": {
        "courses": [
            ("mathematics", "real-analysis"),
            ("mathematics", "abstract-algebra"),
            ("mathematics", "topology"),
        ],
        "direction": "promote",
    },
    "batch_02_math_applied": {
        "courses": [
            ("mathematics", "complex-analysis"),
            ("mathematics", "number-theory"),
            ("mathematics", "probability-and-mathematical-statistics"),
            ("mathematics", "differential-equations"),
        ],
        "direction": "promote",
    },
    "batch_03_math_discrete": {
        "courses": [
            ("mathematics", "numerical-analysis"),
            ("mathematics", "graph-theory-and-combinatorics"),
        ],
        "direction": "promote",
    },
    "batch_04_cs_theory": {
        "courses": [
            ("computer-science", "theory-of-computation"),
            ("computer-science", "compilers"),
        ],
        "direction": "promote",
    },
    "batch_05_cs_applied": {
        "courses": [
            ("computer-science", "artificial-intelligence"),
            ("computer-science", "distributed-systems"),
        ],
        "direction": "promote",
    },
    "batch_06_chem": {
        "courses": [
            ("chemistry", "physical-chemistry"),
            ("chemistry", "analytical-chemistry"),
        ],
        "direction": "promote",
    },
    "batch_07_physics": {
        "courses": [
            ("physics", "quantum-mechanics"),
            ("physics", "modern-physics"),
        ],
        "direction": "promote",
    },
    "batch_08_health": {
        "courses": [
            ("health-and-human-development", "epidemiology"),
            ("health-and-human-development", "pathophysiology"),
            ("health-and-human-development", "public-health"),
        ],
        "direction": "demote",
    },
    "batch_09_engineering": {
        "courses": [
            ("engineering", "control-systems"),
            ("engineering", "signals-and-systems"),
        ],
        "direction": "demote",
    },
    "batch_10_psych": {
        "courses": [
            ("psychology", "clinical-psychology"),
            ("psychology", "cognitive-neuroscience"),
            ("psychology", "psychometrics"),
        ],
        "direction": "demote",
    },
    "batch_11_literature_history": {
        "courses": [
            ("literature", "critical-theory"),
            ("literature", "comparative-literature"),
            ("history", "historiography"),
        ],
        "direction": "demote",
    },
    "batch_12_humanities": {
        "courses": [
            ("philosophy", "philosophy-of-science"),
            ("arts-and-aesthetics", "aesthetic-theory"),
            ("music", "advanced-music-theory"),
            ("language-and-communication", "advanced-linguistics"),
        ],
        "direction": "demote",
    },
    "batch_13_bio_social": {
        "courses": [
            ("biology", "neuroscience"),
            ("biology", "immunology"),
            ("social-sciences", "sociological-theory"),
            ("social-sciences", "international-relations-theory"),
            ("social-sciences", "research-methods-social-science"),
        ],
        "direction": "both",
    },
    "batch_14_formal_econ": {
        "courses": [
            ("formal-sciences-and-logic", "category-theory"),
            ("formal-sciences-and-logic", "model-theory"),
            ("economics", "development-economics"),
        ],
        "direction": "demote",
    },
}

for batch_name, batch_config in batches.items():
    batch_topics = []
    for domain, course in batch_config["courses"]:
        if domain in data and course in data[domain]:
            course_data = data[domain][course]
            # Slim down: drop filepath for the prompt (agent doesn't need it)
            for t in course_data["topics"]:
                batch_topics.append({
                    "id": t["id"],
                    "title": t["title"],
                    "domain": t["domain"],
                    "course": t["course"],
                    "stage": t["stage"],
                    "prereq_count": t["prereq_count"],
                    "core_idea": t["core_idea"],
                    "filepath": t["filepath"],
                })

    batch_file = BATCH_DIR / f"{batch_name}.json"
    with open(batch_file, "w", encoding="utf-8") as f:
        json.dump({
            "direction": batch_config["direction"],
            "topic_count": len(batch_topics),
            "topics": batch_topics,
        }, f, indent=1, ensure_ascii=False)

    print(f"{batch_name}: {len(batch_topics)} topics")

print(f"\nBatch files written to {BATCH_DIR}")
