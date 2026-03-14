# Open Knowledge Graph

Open-source, machine-readable knowledge graphs mapping prerequisite relationships between topics across every domain of human knowledge.

## Project Structure
- `domains/` — 19 domains, 3,080+ topics, 101 courses
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
- `python tools/visualize_hierarchy.py` — Per-domain hierarchical canvas layout (course-band Y-axis, top-to-bottom). Use `--domain mathematics`, `--course algebra-1`, or `--all` to batch-generate all 19 domains + index page. Navigation links to index and radial view.
- `python tools/visualize_radial.py` — **Radial torus visualization**. Developmental-stage radial bands, curated domain ordering, polar force simulation. Generates `output/radial-graph.html`.
- `python tools/generate_topic_pages.py` — Generates individual topic detail pages in `output/topics/`. Each page has Core Idea, prerequisite chains, successors, and navigation.
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
- **Hierarchy view** (`visualize_hierarchy.py`): Per-domain canvas graphs. Top-to-bottom flow (basics at top, advanced at bottom), course-band Y-axis, dark background (#1a1a2e). All 19 domains supported via `--all`. Hover: blue edges = prerequisites, orange = successors. Click nodes to open topic detail pages. Nav links to index and radial view.
- **Radial view** (`visualize_radial.py`): Full cross-domain torus visualization. Developmental-stage radial bands (pre-formal at center → advanced at edge). Curated domain ordering with polar force simulation for organic boundaries. Hover highlights prerequisite (blue) / dependent (orange) edges. Click nodes → topic pages. Click outer ring → domain hierarchy.
- **Topic detail pages** (`generate_topic_pages.py`): Individual HTML pages with Core Idea, How It's Best Learned, Common Misconceptions, full prerequisite chain, direct prereqs (hard/soft badges), and successors. Dark theme with domain-hue accent colors.
- **Index page**: Domain card grid linking to per-domain hierarchy views, radial graph, and full hierarchy graph.
- **GitHub Pages**: Auto-deployed via `.github/workflows/deploy-pages.yml` on push to master. Live at `griffinhilly.github.io/open-knowledge-graph/`.

## Current Status
- **3,080+ topics** across **19 domains**, **101 courses**, **8,400+ prerequisite edges**
- Topic granularity expansion in progress (Phases 1-2 complete, Phase 3 in progress)
- Expanded domains: practical-life-skills (80→160), language-and-communication (89→189), engineering (115→188), philosophy (124→210), formal-sciences-and-logic (81→144+), chemistry (112→162+)
- GitHub Pages live at `griffinhilly.github.io/open-knowledge-graph/`
- GitHub Actions CI: validates graph + deploys visualizations on every push
- New topics at `status: draft` pending review; original 2,628 at `status: validated`

## Related Projects
- `~/knowledge-architecture/` — Prose-based concept sequences (predecessor project)
- `~/canons/` — Reading list analysis projects
