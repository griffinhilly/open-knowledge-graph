# Open Knowledge Graph Memory

## Status (Mar 15, 2026)
- **13,489 topics** across **19 domains**, **148 courses**, **29,596 prerequisite edges**
- GitHub repo: `griffinhilly/open-knowledge-graph` (public)
- GitHub Pages: `griffinhilly.github.io/open-knowledge-graph/` (auto-deployed via Actions)
- Original 2,628 topics at status: **validated**; ~10,861 expansion topics at status: **draft**
- **1,006 topics** have Questions + Explainer sections (overnight Q+E run COMPLETE)

## Quality Fixes (Mar 15)
- **Stage fixes**: 841 draft topics had wrong developmental stages (blanket assignments from overnight expansion). Fixed via hub analysis + propagation across music, arts, language, practical-life-skills, diff-eq, complex/real analysis, graph-theory-and-combinatorics, probability-and-mathematical-statistics.
- **Cycle fixes**: 27+ prerequisite cycles broken, format normalized (518 files from crashed session recovered)
- **Inflated prerequisite depth**: Systemic issue where cross-domain prerequisites chain through courses not actually required. Fixed biology (max depth 58→16), chemistry (removed physical-chem prereqs from gen-chem), and 6 other domains. ~133 files changed total.
- **Remaining issue**: Many hub topics still visually misplaced on radial graph. The force simulation allows angular drift toward cross-domain connections, which is desired behavior (domain blurring) but combined with remaining inflated prereqs causes some topics to appear far from their domain. Needs fresh approach next session — possibly per-topic investigation of worst offenders rather than bulk fixes.

## Overnight Q+E Run (Mar 14-15) — COMPLETE
- Manifest: `tools/overnight/qe-manifest.json` (1,000 hub topics by connectivity)
- Result: 1,000/1,000 completed, 0 failed. 1,006 total with Q+E (including 6 hand-crafted examples).
- Quality spot-checked on supply-and-demand, time-complexity-classes — both excellent

## Decisions
- **Format**: Markdown + YAML frontmatter (one file per topic)
- **License**: CC BY-SA 4.0 for content, MIT for tools
- **GitHub Pages**: Preferred deployment method; generated HTML stays out of git
- **Expansion strategy**: Research → plan → parallel generation agents → validate → commit
- **New topic status**: `draft` until reviewed; original topics remain `validated`
- **Questions schema**: YAML-in-code-block inside `## Questions` section. 3 questions per topic (MC, T/F, short-answer). Validated by validate.py as warnings.
- **Explainer schema**: Freeform markdown in `## Explainer` section. 3-5 paragraphs that teach the concept.
- **Radial viz domain blurring**: Keep cross-domain angular drift — topics should migrate toward domains they serve. Don't pin to sector. Fix misplacement via better prerequisite accuracy instead.

## Courses Flagged for Stage Review
All flagged courses have been fixed.
