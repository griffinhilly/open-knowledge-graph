# Open Knowledge Graph Memory

## Status (Mar 14, 2026)
- **3,080+ topics** across **19 domains**, **101 courses**, **8,400+ prerequisite edges**
- GitHub repo: `griffinhilly/open-knowledge-graph` (public)
- GitHub Pages: `griffinhilly.github.io/open-knowledge-graph/` (auto-deployed via Actions)
- Original 2,628 topics at status: **validated**; ~452 new expansion topics at status: **draft**

## Topic Granularity Expansion (Mar 13-14)
Three-phase expansion to increase topic granularity across non-math domains:

| Phase | Domains | Before | After | Status |
|-------|---------|--------|-------|--------|
| 1 | practical-life-skills, language-and-communication | 169 | 349 | DONE |
| 2 | engineering, philosophy | 239 | 398 | DONE |
| 3 | formal-sciences-and-logic, chemistry | 193 | 306+ | IN PROGRESS |

**Expansion approach**: Research agent analyzes domain granularity (topics/course, edges/topic, content breadth) → proposes decompositions + gap-filling → implementation agents generate 15-25 topics per course in parallel.

**Domains NOT expanded** (already well-structured): physics, computer-science, mathematics, history, social-sciences.

## Visualization Updates (Mar 13-14)
- **Hierarchy views**: Flipped Y-axis (basics at top, advanced at bottom). Added blue/orange edge colors on hover (blue = prerequisite, orange = successor). Added nav links ("All Domains", "Radial Graph") at top center.
- **Radial view**: Added domain-click navigation (click outer ring → domain hierarchy page). Pointer cursor on hover.
- **Index page**: Added both "View Radial Graph" (primary) and "View Hierarchy Graph" links.
- **GitHub Pages**: `.github/workflows/deploy-pages.yml` auto-generates all visualizations and deploys on push.

## Phase 7: Visualization (Mar 12–13)
- Updated `visualize_hierarchy.py` to support all 19 domains. Added `--all` flag for batch generation + index page.
- Built `visualize_radial.py` — radial torus with developmental-stage radial bands and curated domain ordering.
- Built `generate_topic_pages.py` — generates individual HTML detail pages.
- Domain ordering is curated for edge proximity: math → formal-sciences → philosophy → CS → engineering → physics → chemistry → earth-sciences → biology → health → psychology → social-sciences → economics → practical-life → history → language → literature → arts → music

## QA Review (Mar 12)
- Built `tools/qa_analyze.py` — structural QA tool
- Built `tools/apply_bidirectional_fixes.py` — resolved 39 bidirectional pairs
- Added 24 new topics across 9 thin courses
- Promoted all 2,628 topics from draft → validated

## Decisions
- **Format**: Markdown + YAML frontmatter (one file per topic)
- **ID uniqueness**: Global across all domains
- **License**: CC BY-SA 4.0 for content, MIT for tools
- **DAG as pedagogical simplification**: Documented in `meta/schema.md`
- **Hierarchy Y-axis**: Basics at top, advanced at bottom (top-to-bottom reading order)
- **Radial layout**: Developmental stage determines radius. Domain ordering curated.
- **GitHub Pages**: Preferred deployment method; generated HTML stays out of git
- **Expansion strategy**: Research → plan → parallel generation agents → validate → commit
- **New topic status**: `draft` until reviewed; original topics remain `validated`
