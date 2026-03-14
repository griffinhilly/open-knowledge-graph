# Open Knowledge Graph Memory

## Status (Mar 13, 2026)
- **2,628 topics** across **19 domains**, **101 courses**, **7,563+ prerequisite edges**
- 0 dangling prerequisite references, 0 bidirectional mismatch pairs
- 530 builds-toward consistency warnings (down from 1,609 → 571 → 530)
- All topics at status: **validated** (promoted from draft after QA review)
- All courses have 20+ topics
- Phase 6 (Quality Review) **COMPLETE**
- Phase 7 (Visualization) **COMPLETE**

## Phase 7: Visualization (Mar 12–13)
- Updated `visualize_hierarchy.py` to support all 19 domains (was math-only). Added `--all` flag for batch generation + index page. Auto-generates colors from `_domain.yml` configs.
- Built `visualize_radial.py` — radial torus visualization with developmental-stage radial bands and curated domain ordering. Polar force simulation allows organic cross-domain blending. Two iterations: v1 used topological depth (wrong — made psychology look more advanced than math), v2 uses developmental stage (correct).
- Built `generate_topic_pages.py` — generates 2,628 individual HTML detail pages with Core Idea, How It's Best Learned, Common Misconceptions, full prerequisite chain (longest path from root), direct prereqs with hard/soft badges, and direct successors. Dark theme with domain-hue accent colors. Click-to-navigate between pages and back to graph views.
- Domain ordering is curated (not algorithmic) to minimize cross-domain edge distance: math → formal-sciences → philosophy → CS → engineering → physics → chemistry → earth-sciences → biology → health → psychology → social-sciences → economics → practical-life → history → language → literature → arts → music

## QA Review (Mar 12)
- Built `tools/qa_analyze.py` — structural QA tool (hubs, chains, islands, thin courses, shallow content, bidirectional pairs)
- Built `tools/apply_bidirectional_fixes.py` — resolved 39 bidirectional builds-toward pairs (36 directional, 3 dropped both)
- Added 24 new topics across 9 thin courses (practical-life-skills ×16, arts ×7, microbiology ×1)
- Expanded `noun-phrases` topic body from 46 to 120+ words
- Spot-checked longest prerequisite chains across all 19 domains — all pedagogically sound
- Hub review: top 5 hubs (ratios, mean-median-mode, mathematical-induction, percent-concept, partial-derivatives) confirmed reasonable
- Promoted all 2,628 topics from draft → validated

## Reconciliation (Mar 11)
- Built `tools/reconcile_analyze.py` to categorize all 1,599 mismatches into 5 tiers
- Built `tools/reconcile.py` with dialectic-reviewed decisions per tier:
  - **Tier 1 (Dangling refs)**: 35 merged to existing IDs, 12 removed, 31 new topics created
  - **Tier 2 (Cycles)**: 13 cycle-creating edges removed; DAG-as-simplification note added to `meta/schema.md`
  - **Tier 3 (Transitive)**: 411 skipped (already reachable via intermediate chain)
  - **Tier 4 (Same-course)**: 942 added as soft prereqs (bidirectional filter applied)
  - **Tier 5 (Cross-course)**: 124 math-sequential added as soft prereqs, 4 lateral dismissed
- Reconciliation log at `tools/reconcile_log.json`

## Decisions
- **Format**: Markdown + YAML frontmatter (one file per topic). Human-readable AND machine-parseable.
- **ID uniqueness**: Global across all domains.
- **License**: CC BY-SA 4.0 for content, MIT for tools
- **DAG as pedagogical simplification**: Real knowledge has cycles; the DAG represents a teaching sequence, not not a claim about knowledge structure. Documented in `meta/schema.md`.
- **Reconciliation approach**: Bidirectional per-case evaluation with dialectic review. Transitive edges skipped, same-course defaults to add, cross-course evaluated individually.
- **Generation approach**: Per-course agent invocations, not per-domain. ~20-35 topics per call is the sweet spot.
- **Cross-domain linking**: Automated review pass after all courses built. Adds `soft` prereqs by default.
- **Bidirectional pair resolution**: For same-course pairs, choose pedagogical direction (which comes first); for true peers, drop both builds-toward links.
- **Radial layout**: Developmental stage determines radius (not topological depth). Domain ordering is curated for edge proximity, not algorithmic.
- **Visualization navigation**: Topic detail pages link back to radial graph and domain index. Graph nodes click through to topic detail pages.
