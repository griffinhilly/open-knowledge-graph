# Visualization Design

## Hierarchy View (`visualize_hierarchy.py`)

Per-domain canvas graphs. Top-to-bottom flow (basics at top, advanced at bottom), course-band Y-axis, dark background (#1a1a2e). All 19 domains supported via `--all`. Hover: blue edges = prerequisites, orange = successors. Click nodes to open topic detail pages. Nav links to index and radial view.

## Radial View (`visualize_radial.py`)

Full cross-domain torus visualization. Developmental-stage radial bands (pre-formal at center → advanced at edge). Curated domain ordering with polar force simulation for organic boundaries. Hover highlights prerequisite (blue) / dependent (orange) edges. Click nodes → topic pages. Click outer ring → domain hierarchy.

**Domain ordering** (curated for edge proximity):
math → formal-sciences → philosophy → CS → engineering → physics → chemistry → earth-sciences → biology → health → psychology → social-sciences → economics → practical-life → history → language → literature → arts → music

## Topic Detail Pages (`generate_topic_pages.py`)

Individual HTML pages with Core Idea, How It's Best Learned, Common Misconceptions, full prerequisite chain, direct prereqs (hard/soft badges), and successors. Dark theme with domain-hue accent colors.

## Index Page

Domain card grid linking to per-domain hierarchy views, radial graph, and full hierarchy graph. Contains both "View Radial Graph" (primary) and "View Hierarchy Graph" links.

## GitHub Pages Deployment

Auto-deployed via `.github/workflows/deploy-pages.yml` on push to master. Generated HTML stays out of git (gitignored). Live at `openknowledgegraph.com`.

## Visualization History (Mar 12–14)

- **Hierarchy views**: Flipped Y-axis (basics at top). Added blue/orange edge colors on hover. Added nav links ("All Domains", "Radial Graph") at top center.
- **Radial view**: Added domain-click navigation (click outer ring → domain hierarchy page). Pointer cursor on hover.
- **Index page**: Added both radial and hierarchy graph links.
- Phase 7 (Mar 12–13): Built `visualize_radial.py`, `generate_topic_pages.py`. Updated `visualize_hierarchy.py` to support all 19 domains with `--all` flag.

## Domain Map Architecture (Mar 24, 2026 — moved from MEMORY.md Jun 12)

- **Tier layout**: Courses grouped by developmental stage → tiers. Within-tier overlap ~50%, between-tier ~25%.
- **Branch X-positions**: Manual left-right axis per domain (e.g., math: discrete←→analysis). Stored in `COURSE_BRANCH_X` dict. Non-math mappings are AI-proposed, need human review.
- **Sizing**: `area ∝ degree`, out-degree weighted 2x. DEGREE_CEILING=25 for consistent sizing across views.
- **Row splitting**: 3x depth multiplier, recursive splitting (3 passes, cap 20 topics/row).
- **Centroid-anchored placement**: Each layer anchors on connected-neighbor centroid, then 10 rounds of 40% neighbor drift.
- **Cross-course depth floor** (Apr 1): `compute_course_depths` uses domain-wide depth as floor for within-course depth, SCALED to the course's own depth range. Prevents height inflation while fixing cross-course prereq ordering.
- **Radial integration** (Mar 25): `visualize_radial.py` imports `COURSE_BRANCH_X` from domain map. Auto-detects `BRANCH_FLIP` per domain using cross-domain edge lengths within 3-domain angular window. Plan doc: `tools/radial-branch-alignment.md`.
- **Leaf connector tool**: `tools/connect_leaves.py` — tag/title overlap scoring, cycle-safe apply, duplicate detection.
- **Dedup tool**: `tools/dedup_pairs.py` — delete weaker file + redirect references (see MEMORY.md Gotchas for dedup hazards).
