# Open Knowledge Graph - Index

## Root Files
- `CLAUDE.md` — AI instructions
- `README.md` — Project description for humans
- `INDEX.md` — This file
- `MEMORY.md` — Working notes
- `PLAN.md` — Roadmap
- `CONTRIBUTING.md` — Contributor guide
- `LICENSE` — CC BY-SA 4.0 (content) + MIT (code)
- `.gitignore`

## Domains (19 domains, 13,518 topics, 149 courses)

Each domain has `_domain.yml` + course subdirectories containing topic `.md` files.

| Domain | Path | Topics | Courses |
|--------|------|--------|---------|
| Mathematics | `domains/mathematics/` | 1,920 | 28 |
| Computer Science | `domains/computer-science/` | 1,059 | 11 |
| Biology | `domains/biology/` | 924 | 9 |
| Physics | `domains/physics/` | 856 | 8 |
| Engineering | `domains/engineering/` | 722 | 7 |
| Economics | `domains/economics/` | 721 | 7 |
| Philosophy | `domains/philosophy/` | 736 | 9 |
| Psychology | `domains/psychology/` | 679 | 8 |
| Earth & Space Sciences | `domains/earth-and-space-sciences/` | 640 | 7 |
| Music | `domains/music/` | 607 | 6 |
| History | `domains/history/` | 605 | 6 |
| Social Sciences | `domains/social-sciences/` | 577 | 7 |
| Language & Communication | `domains/language-and-communication/` | 537 | 6 |
| Health & Human Development | `domains/health-and-human-development/` | 530 | 6 |
| Chemistry | `domains/chemistry/` | 527 | 4 |
| Literature | `domains/literature/` | 495 | 6 |
| Practical Life Skills | `domains/practical-life-skills/` | 482 | 4 |
| Formal Sciences & Logic | `domains/formal-sciences-and-logic/` | 458 | 5 |
| Arts & Aesthetics | `domains/arts-and-aesthetics/` | 444 | 5 |

## Tools
- `tools/validate.py` — Schema + graph validation
- `tools/visualize_hierarchy.py` — Per-domain hierarchical canvas layout (supports `--all` for batch generation + index page)
- `tools/visualize_radial.py` — Radial cross-domain torus visualization (developmental-stage radial bands)
- `tools/generate_topic_pages.py` — Individual topic detail page generator
- `tools/visualize.py` — Alternative force-directed rendering (pyvis/matplotlib)
- `tools/stats.py` — Coverage statistics
- `tools/qa_analyze.py` — Structural QA analysis (hubs, chains, islands, thin courses, shallow content)
- `tools/apply_bidirectional_fixes.py` — Bidirectional builds-toward pair resolver (39 pairs, completed)
- `tools/reconcile.py` — Builds-toward reconciliation (adds missing prereqs, handles merges/removals)
- `tools/reconcile_analyze.py` — Mismatch analysis and categorization (outputs reconcile_analysis.json)
- `tools/reconcile_analysis.json` — Analysis data (1,599 mismatches categorized)
- `tools/reconcile_log.json` — Change log from reconciliation run
- `tools/generate_assessment.py` — Selects probe topics + builds frontier chains → `output/assessment-data.json`
- `tools/generate_assessment_page.py` — Generates adaptive placement assessment UI → `output/assessment.html`
- `tools/diagnose_positioning.py` — Finds topics displaced from their domain sector (angular drift analysis)
- `tools/diagnose_radial_order.py` — Finds prerequisite edges violating radial ordering (prereq more advanced than successor)
- `tools/trace_topic.py` — Traces positioning math for a specific topic (debug tool)
- `tools/generate_rationality_course.py` — Generates all 30 Applied Rationality topic files under philosophy
- `tools/overnight/` — Autonomous generation orchestrator
  - `orchestrator.py` — Main runner (invokes `claude --print` per course)
  - `subjects.py` — Subject queue definitions (all 19 domains, 117 courses)
  - `generator.py` — JSON-to-Markdown file converter + crosslink editor
  - `build_parallel_manifests.py` — Generates N-worker shard manifests for explainer/question generation
  - `build_content_manifests.py` — Single-worker manifest builder (superseded by parallel version)
  - `run-parallel.sh` — Launches N parallel overnight workers
  - `check_progress.py` — Aggregates progress across all shard checkpoints
  - `output/` — Agent JSON outputs and raw text (gitignored)
  - `progress.json` — Execution state for resume capability
  - `run.log` — Execution log

## Output (generated, gitignored)
- `output/index.html` — Domain card grid (links to per-domain hierarchies and radial graph)
- `output/radial-graph.html` — Full cross-domain radial torus visualization
- `output/*-hierarchy.html` — 19 per-domain hierarchy views
- `output/assessment.html` — Adaptive placement assessment (3-round, ~5 minutes)
- `output/assessment-data.json` — Probe topics and frontier chains for assessment
- `output/topics/` — 13,518 individual topic detail pages (Core Idea, explainer, prerequisite chains, successors)
- `output/topics/*-questions.html` — Interactive question pages (1,006 topics with Q+E)
- `output/topics/tags/` — 20,531 tag pages + tag index

## Meta
- `meta/schema.md` — YAML frontmatter schema definition
- `meta/developmental-stages.md` — Stage definitions (pre-formal through advanced)
- `meta/course-list.md` — Course directory listing

## Other
- `legacy/` — Legacy JS libraries (vis.js, tom-select, bindings)
