# Open Knowledge Graph

Open-source, machine-readable knowledge graphs mapping prerequisite relationships between topics across every domain of human knowledge.

## Project Structure
- `domains/` — 19 domains, 15,304 topics, 261 courses
- `tools/` — Python tooling (validate.py, visualize_hierarchy.py, visualize_radial.py, visualize_domain_map.py, generate_topic_pages.py, generate_quiz_page.py, generate_assessment.py, generate_assessment_page.py, generate_assessment_questions.py, connect_leaves.py, dedup_pairs.py, find_near_duplicates.py, reconcile_domain_stages.py, spot_check_new_topics.py, map_dangling_prereqs.py, stats.py, reconcile.py)
- `hooks/` — Git hooks (pre-push: cycle detection + CI script check). Setup: `git config core.hooksPath hooks`
- `tools/overnight/` — Autonomous generation orchestrator (used to build the initial graph and Q+E content)
- `meta/` — Schema definition, developmental stages, course list
- `output/` — Generated HTML visualizations (gitignored)
- `CONTRIBUTING.md` — How to add topics and contribute

## Schema
Each topic is a Markdown file with YAML frontmatter. See `meta/schema.md` for the full spec.
- Required fields: id, title, domain, course, prerequisites
- Prerequisite types: hard (must know first) or soft (helpful but not required)
- Body sections: Core Idea (required), How It's Best Learned, Common Misconceptions, Questions (optional), Explainer (optional)

## Tooling

Tool commands: see `guides/tools-reference.md`

## Conventions
- File name = topic ID + .md (lowercase, hyphenated)
- IDs are globally unique across all domains
- Topics belong to the course where they are first formally introduced
- Prerequisites point backward; builds-toward points forward (informational)
- The prerequisite graph is the source of truth for sequencing
- Each domain has a `_domain.yml` with domain metadata and course list

## Visualization Design

Visualization design: see `guides/visualization.md`

## Current Status
- **15,304 topics** across **19 domains**, **261 courses**
- **6 developmental stages**: pre-formal, concrete-operations, abstract-reasoning, formal-systems, advanced, expert
- **All topics at `status: validated`**
- GitHub Pages live at `griffinhilly.github.io/open-knowledge-graph/`
- GitHub Actions CI: validates → generates index + radial + topic pages + domain maps + assessment + quiz → deploys to Pages
- **Phases 1-9C DONE**, **Phase 10 (Question Quality Audit) DONE**, **Phase 11 (Early-Childhood) DONE**
- **P2 topic expansion DONE** (Apr 1): +320 topics, 6 new courses (applied-ethics, history-of-science, economic-social-history, robotics-and-autonomous-systems, music-technology, contemporary-art-new-media), 15 courses extended
- **Phase 11 DONE** (Apr 4): +358 topics, 12 new early-childhood courses across 7 domains (Music 3, Literature 2, Psychology 3, History 1, Philosophy 1, Social Sciences 1, Arts 1)

## Related Projects
- `~/knowledge-architecture/` — Prose-based concept sequences (predecessor project)
- `~/canons/` — Reading list analysis projects

## Radial Visualization Tuning

The radial layout (`visualize_radial.py`) has several tunable parameters in the force simulation:
- **Angular spring-back** (0.02): pulls topics toward their domain sector center. Higher = more rigid domains, lower = more organic blending.
- **Cross-domain edge attraction** (0.008) vs same-domain (0.003): cross-domain edges pull 2.67x harder.
- **Radial jitter** (5% of band width): keeps depth ordering intact while adding organic feel.
- **Prerequisite ordering force** (0.006): soft force pushing prerequisites inward, successors outward when they overlap radially.
- 2,325 edges (8%) still violate radial ordering (prereq staged more advanced than successor). ~676 have 2+ stage gap. Triage by severity for data fixes.

## Learning Platform Architecture (Phase 9)
- **Fluency model**: Continuous 0-100 per topic, Bayesian log-odds updates, prerequisite propagation
- **localStorage keys**: `okg-fluency` (scores), `okg-fluency-meta` (metadata), `okg-goals` (starred topics), `okg-adjustments` (manual overrides)
- **Assessment**: 3-phase adaptive (warm-up → exploration → deep dive), uses actual question bank, silent response time tracking
- **Graph coloring**: Fluency-based node colors override domain colors when progress data exists; frontier topics get distinctive borders

## Situational Guides
- When running any tool (validation, visualization, generation, reconciliation) → read `guides/tools-reference.md`
- When modifying visualizations or adding a new viz → read `guides/visualization.md`
