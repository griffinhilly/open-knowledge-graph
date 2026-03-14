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

## Domains (19 domains, 3,080+ topics, 101 courses)

Each domain has `_domain.yml` + course subdirectories containing topic `.md` files.

| Domain | Path | Topics | Courses |
|--------|------|--------|---------|
| Mathematics | `domains/mathematics/` | 661 | 18 |
| Philosophy | `domains/philosophy/` | 210 | 6 |
| Language & Communication | `domains/language-and-communication/` | 189 | 4 |
| Engineering | `domains/engineering/` | 188 | 5 |
| Computer Science | `domains/computer-science/` | 170 | 6 |
| Physics | `domains/physics/` | 163 | 5 |
| Chemistry | `domains/chemistry/` | 162+ | 4 |
| Practical Life Skills | `domains/practical-life-skills/` | 160 | 4 |
| Formal Sciences & Logic | `domains/formal-sciences-and-logic/` | 144+ | 4 |
| Biology | `domains/biology/` | 134 | 5 |
| History | `domains/history/` | 127 | 5 |
| Economics | `domains/economics/` | 120 | 4 |
| Psychology | `domains/psychology/` | 111 | 5 |
| Literature | `domains/literature/` | 105 | 5 |
| Music | `domains/music/` | 102 | 5 |
| Earth & Space Sciences | `domains/earth-and-space-sciences/` | 89 | 4 |
| Health & Human Development | `domains/health-and-human-development/` | 85 | 4 |
| Social Sciences | `domains/social-sciences/` | 80 | 4 |
| Arts & Aesthetics | `domains/arts-and-aesthetics/` | 80 | 4 |

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
- `tools/overnight/` — Autonomous generation orchestrator
  - `orchestrator.py` — Main runner (invokes `claude --print` per course)
  - `subjects.py` — Subject queue definitions (all 19 domains, 117 courses)
  - `generator.py` — JSON-to-Markdown file converter + crosslink editor
  - `output/` — Agent JSON outputs and raw text (gitignored)
  - `progress.json` — Execution state for resume capability
  - `run.log` — Execution log

## Output (generated, gitignored)
- `output/index.html` — Domain card grid (links to per-domain hierarchies and radial graph)
- `output/radial-graph.html` — Full cross-domain radial torus visualization
- `output/*-hierarchy.html` — 19 per-domain hierarchy views
- `output/topics/` — 2,628 individual topic detail pages (Core Idea, prerequisite chains, successors)

## Meta
- `meta/schema.md` — YAML frontmatter schema definition
- `meta/developmental-stages.md` — Stage definitions (pre-formal through advanced)
- `meta/course-list.md` — Course directory listing

## Other
- `legacy/` — Legacy JS libraries (vis.js, tom-select, bindings)
