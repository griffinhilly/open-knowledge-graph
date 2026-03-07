# Open Knowledge Graph

Open-source, machine-readable knowledge graphs mapping prerequisite relationships between topics across every domain of human knowledge.

## Project Structure
- `domains/mathematics/` — 372 topics across 9 courses (4th grade through Calculus 2)
- `tools/` — Python tooling (validate.py, visualize.py, stats.py)
- `meta/` — Schema definition, developmental stages, course list
- `CONTRIBUTING.md` — How to add topics and contribute

## Schema
Each topic is a Markdown file with YAML frontmatter. See `meta/schema.md` for the full spec.
- Required fields: id, title, domain, course, prerequisites
- Prerequisite types: hard (must know first) or soft (helpful but not required)
- Body sections: Core Idea (required), How It's Best Learned, Common Misconceptions

## Tooling
- `python tools/validate.py` — Schema + graph validation (catches broken refs, cycles, duplicates)
- `python tools/visualize.py` — Renders graph as HTML (pyvis) or PNG (matplotlib)
- `python tools/stats.py` — Coverage statistics
- Requires: Python 3.10+, pyyaml. Optional: networkx, matplotlib, pyvis.

## Conventions
- File name = topic ID + .md (lowercase, hyphenated)
- IDs are globally unique across all domains
- Topics belong to the course where they are first formally introduced
- Prerequisites point backward; builds-toward points forward (informational)
- The prerequisite graph is the source of truth for sequencing

## Current Status
- Mathematics: 372 topics, 732 edges, 9 courses (4th grade through Calc 2)
- 5 courses not yet started: linear-algebra, multivariable-calculus, methods-of-proof, probability-and-statistics, discrete-math
- 16 dangling prerequisite references (ID mismatches between agents — need normalization)
- All topics at status: draft

## Related Projects
- `~/knowledge-architecture/` — Prose-based concept sequences (predecessor project)
- `~/canons/` — Reading list analysis projects
