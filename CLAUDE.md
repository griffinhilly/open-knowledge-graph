# Open Knowledge Graph

Open-source, machine-readable knowledge graphs mapping prerequisite relationships between topics across every domain of human knowledge.

## Project Structure
- `domains/` — 19 domains, 13,489 topics, 148 courses
- `tools/` — Python tooling (validate.py, visualize_hierarchy.py, visualize.py, stats.py, reconcile.py, generate_assessment.py, generate_assessment_page.py)
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
- **13,489 topics** across **19 domains**, **148 courses**, **29,596 prerequisite edges**
- **1,006 topics** have Questions + Explainer sections
- GitHub Pages live at `griffinhilly.github.io/open-knowledge-graph/`
- GitHub Actions CI: validates graph + deploys visualizations on every push
- New topics at `status: draft` pending review; original 2,628 at `status: validated`

## Related Projects
- `~/knowledge-architecture/` — Prose-based concept sequences (predecessor project)
- `~/canons/` — Reading list analysis projects

## Situational Guides
- When running any tool (validation, visualization, generation, reconciliation) → read `guides/tools-reference.md`
- When modifying visualizations or adding a new viz → read `guides/visualization.md`
