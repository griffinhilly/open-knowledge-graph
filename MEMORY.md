# Open Knowledge Graph Memory

## Status (Mar 15, 2026)
- **13,489 topics** across **19 domains**, **148 courses**, **29,596 prerequisite edges**
- GitHub repo: `griffinhilly/open-knowledge-graph` (public)
- GitHub Pages: `griffinhilly.github.io/open-knowledge-graph/` (auto-deployed via Actions)
- Original 2,628 topics at status: **validated**; ~10,861 expansion topics at status: **draft**
- **1,006 topics** have Questions + Explainer sections (overnight Q+E run COMPLETE)

## Radial Positioning Fixes (Mar 15, session 2)
- **Rotation bug found and fixed**: edge attraction had asymmetric y-force (`ps["y"] -= fy` instead of `+= fy`) causing systematic angular displacement in wrong direction. This was the primary cause of topics appearing in wrong domains.
- **Angular spring-back added** (0.02 strength): gentle pull toward domain sector center. Reduced displaced topics from 4,503 to ~2,400 at this strength. Higher values (0.12) made domains too rigid.
- **Prereq radial ordering force added**: soft force pushing prerequisites inward, successors outward when they overlap. Helps enforce visual "inner=foundational, outer=advanced" expectation.
- **Radial jitter reduced** from 18% to 5% of band width to preserve depth ordering within bands.
- **Dialectic review result**: both data fixes AND algorithm fixes needed. Data fixes for genuine stage misassignments; algorithm fixes for structural same-band ordering. Don't split topics yet.
- **culture-concept data fix applied**: moved from concrete-operations to abstract-reasoning; softened prereq edges for ethnocentrism, ritual-and-ceremony, material-culture.
- **2,325 edges (8%) still violate radial ordering** — prereq at more advanced stage than successor. 676 have 2+ stage gap. Next step: triage top violations by severity.

## Quality Fixes (Mar 15, session 1)
- **Stage fixes**: 841 draft topics had wrong developmental stages (blanket assignments from overnight expansion). Fixed via hub analysis + propagation across music, arts, language, practical-life-skills, diff-eq, complex/real analysis, graph-theory-and-combinatorics, probability-and-mathematical-statistics.
- **Cycle fixes**: 27+ prerequisite cycles broken, format normalized (518 files from crashed session recovered)
- **Inflated prerequisite depth**: Systemic issue where cross-domain prerequisites chain through courses not actually required. Fixed biology (max depth 58->16), chemistry (removed physical-chem prereqs from gen-chem), and 6 other domains. ~133 files changed total.

## Overnight Q+E Run (Mar 14-15) — COMPLETE
- Manifest: `tools/overnight/qe-manifest.json` (1,000 hub topics by connectivity)
- Result: 1,000/1,000 completed, 0 failed. 1,006 total with Q+E (including 6 hand-crafted examples).
- Quality spot-checked on supply-and-demand, time-complexity-classes — both excellent

## UI Improvements (Mar 15, session 2)
- **Click-to-preview panel**: clicking a node in radial or hierarchy views shows panel with prereqs/successors (hard/soft badges). Clicking items navigates to that node. Topic title links to detail page.
- **Locked edge highlights**: clicking a node locks the blue (prereq) / orange (successor) edge highlights on screen. Escape or click empty space to clear.
- **Search**: Ctrl+F search bar on all graph views. Multi-match highlights nodes with yellow rings. Single match auto-selects and shows panel.
- **Course breadcrumb links**: topic pages now link to course (not just domain) in breadcrumb.
- **Q+E sections NOT yet rendered** on topic pages — data exists in markdown but generate_topic_pages.py doesn't output them.

## Decisions
- **Format**: Markdown + YAML frontmatter (one file per topic)
- **License**: CC BY-SA 4.0 for content, MIT for tools
- **GitHub Pages**: Preferred deployment method; generated HTML stays out of git
- **Expansion strategy**: Research -> plan -> parallel generation agents -> validate -> commit
- **New topic status**: `draft` until reviewed; original topics remain `validated`
- **Questions schema**: YAML-in-code-block inside `## Questions` section. 3 questions per topic (MC, T/F, short-answer). Validated by validate.py as warnings.
- **Explainer schema**: Freeform markdown in `## Explainer` section. 3-5 paragraphs that teach the concept.
- **Radial viz domain blurring**: Keep cross-domain angular drift (0.02 spring-back) — topics should migrate toward domains they serve. Don't pin rigidly to sector.
- **Topic splitting**: NOT recommended as general policy. Reserve for cases where data+algorithm fixes fail to resolve a specific topic's positioning.

## Courses Flagged for Stage Review
All flagged courses have been fixed.
