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
