# Open Knowledge Graph

Open-source, machine-readable knowledge graphs mapping prerequisite relationships between topics across every domain of human knowledge.

## Project Structure
- `domains/` — 19 domains, 2,628 topics, 101 courses
- `tools/` — Python tooling (validate.py, visualize_hierarchy.py, visualize.py, stats.py, reconcile.py)
- `tools/overnight/` — Autonomous generation orchestrator (used to build the initial graph)
- `meta/` — Schema definition, developmental stages, course list
- `output/` — Generated HTML visualizations (gitignored)
- `CONTRIBUTING.md` — How to add topics and contribute

## Schema
Each topic is a Markdown file with YAML frontmatter. See `meta/schema.md` for the full spec.
- Required fields: id, title, domain, course, prerequisites
- Prerequisite types: hard (must know first) or soft (helpful but not required)
- Body sections: Core Idea (required), How It's Best Learned, Common Misconceptions

## Tooling
- `python tools/validate.py` — Schema + graph validation (catches broken refs, cycles, duplicates)
- `python tools/visualize_hierarchy.py` — Per-domain hierarchical canvas layout (course-band Y-axis, bottom-to-top). Use `--domain mathematics`, `--course algebra-1`, or `--all` to batch-generate all 19 domains + index page.
- `python tools/visualize_radial.py` — **Radial torus visualization**. Developmental-stage radial bands, curated domain ordering, polar force simulation. Generates `output/radial-graph.html`.
- `python tools/generate_topic_pages.py` — Generates 2,628 individual topic detail pages in `output/topics/`. Each page has Core Idea, prerequisite chains, successors, and navigation.
- `python tools/visualize.py` — Force-directed graph rendering (pyvis HTML or matplotlib PNG)
- `python tools/stats.py` — Coverage statistics
- `python tools/qa_analyze.py` — Structural QA analysis (hubs, longest chains, islands, thin courses, shallow content, bidirectional pairs). Supports `--json` and `--domain`.
- `python tools/reconcile.py --dry-run` — Builds-toward reconciliation (preview changes)
- `python tools/reconcile.py --apply` — Apply reconciliation changes
- `python tools/reconcile_analyze.py` — Analyze mismatches for decision-making
- `python tools/overnight/orchestrator.py` — Autonomous bulk generation (invokes `claude --print` per course)
- Requires: Python 3.10+, pyyaml. Optional: networkx, matplotlib, pyvis.

## Conventions
- File name = topic ID + .md (lowercase, hyphenated)
- IDs are globally unique across all domains
- Topics belong to the course where they are first formally introduced
- Prerequisites point backward; builds-toward points forward (informational)
- The prerequisite graph is the source of truth for sequencing
- Each domain has a `_domain.yml` with domain metadata and course list

## Visualization Design
- **Hierarchy view** (`visualize_hierarchy.py`): Per-domain canvas graphs. Bottom-to-top flow, course-band Y-axis, dark background (#1a1a2e). All 19 domains supported via `--all`. Click nodes to open topic detail pages.
- **Radial view** (`visualize_radial.py`): Full cross-domain torus visualization. Developmental-stage radial bands (pre-formal at center → advanced at edge). Curated domain ordering with polar force simulation for organic boundaries. Hover highlights prerequisite (blue) / dependent (orange) edges. Click opens topic detail pages.
- **Topic detail pages** (`generate_topic_pages.py`): 2,628 individual HTML pages with Core Idea, How It's Best Learned, Common Misconceptions, full prerequisite chain, direct prereqs (hard/soft badges), and successors. Dark theme with domain-hue accent colors.
- **Index page**: Domain card grid linking to per-domain hierarchy views and the radial graph.

## Current Status
- **2,628 topics** across **19 domains**, **101 courses** — all at status: **validated**
- 0 dangling prerequisite references, 0 bidirectional mismatch pairs
- 530 builds-toward consistency warnings (down from 1,609)
- All courses have 20+ topics
- Cross-domain prerequisite links established via automated review pass
- Prerequisite graph is a DAG; cycles resolved as pedagogical linearizations (see `meta/schema.md`)
- Phase 6 (Quality Review) complete. Phase 7 (Visualization) complete. Next: Phase 8 (Community Launch)

## Related Projects
- `~/knowledge-architecture/` — Prose-based concept sequences (predecessor project)
- `~/canons/` — Reading list analysis projects
