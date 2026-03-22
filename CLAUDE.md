# Open Knowledge Graph

Open-source, machine-readable knowledge graphs mapping prerequisite relationships between topics across every domain of human knowledge.

## Project Structure
- `domains/` — 19 domains, 13,518 topics, 149 courses
- `tools/` — Python tooling (validate.py, visualize_hierarchy.py, visualize_radial.py, generate_topic_pages.py, stats.py, reconcile.py, generate_assessment.py, generate_assessment_page.py, generate_assessment_questions.py, generate_quiz_page.py, diagnose_positioning.py, diagnose_radial_order.py, trace_topic.py)
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
- **13,518 topics** across **19 domains**, **149 courses**, **29,609 prerequisite edges**
- **~13,260 topics** have Explainer sections; **~13,224 topics** have Questions (98%)
- GitHub Pages live at `griffinhilly.github.io/open-knowledge-graph/`
- GitHub Actions CI: validates graph + deploys visualizations on every push
- New topics at `status: draft` pending review; original 2,628 at `status: validated`
- **Phase 9A (Fluency Model) DONE**: `lib/fluency.js` with Bayesian updates, prerequisite propagation, two color modes. Fluency toggle on all graph views + topic pages.
- **Phase 9B (Quiz Engine) DONE**: `output/quiz.html` — interactive trivia quiz with MC/TF questions, fluency integration, warmup + exploration phases. Phase 9C (Deep Dive + Results) is next.

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
