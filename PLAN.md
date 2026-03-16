# Open Knowledge Graph Plan

## Phase 1: Foundation — DONE
- [x] Schema design (meta/schema.md)
- [x] Repository structure
- [x] Validation tooling (tools/validate.py)
- [x] Visualization tooling (tools/visualize.py, visualize_hierarchy.py)
- [x] Statistics tooling (tools/stats.py)
- [x] Contributor guide (CONTRIBUTING.md)
- [x] License (CC BY-SA 4.0 + MIT)

## Phase 2: Math Seed — DONE
- [x] 4th grade: 36 topics
- [x] 5th grade: 33 topics
- [x] Prealgebra: 45 topics
- [x] Algebra 1: 41 topics
- [x] Geometry: 53 topics
- [x] Algebra 2: 48 topics
- [x] Precalculus: 38 topics
- [x] Calculus 1: 42 topics
- [x] Calculus 2: 37 topics
- Total: 372 topics, 732 prerequisite edges

## Phase 3: Validate and Polish — DONE
- [x] Fix 16 dangling prerequisite references (ID normalization)
- [x] Generate visualization and verify graph structure
- [x] Initial commit and git setup

## Phase 4: Expand Math Coverage — DONE
- [x] Kindergarten: 25 topics
- [x] 1st Grade: 28 topics
- [x] 2nd Grade: 30 topics
- [x] 3rd Grade: 33 topics
- [x] Linear Algebra: 35 topics
- [x] Multivariable Calculus: 35 topics
- [x] Methods of Proof: 25 topics
- [x] Probability & Statistics: 35 topics
- [x] Discrete Math: 30 topics
- Math total: 649 topics across 18 courses

## Phase 5: All Domains — DONE
- [x] Physics: 161 topics, 5 courses
- [x] Computer Science: 170 topics, 6 courses
- [x] Formal Sciences & Logic: 81 topics, 4 courses
- [x] Chemistry: 112 topics, 4 courses
- [x] Biology: 133 topics, 5 courses
- [x] Earth & Space Sciences: 89 topics, 4 courses
- [x] Economics: 120 topics, 4 courses
- [x] Psychology: 111 topics, 5 courses
- [x] Engineering: 113 topics, 5 courses
- [x] Health & Human Development: 82 topics, 4 courses
- [x] History: 126 topics, 5 courses
- [x] Philosophy: 124 topics, 6 courses
- [x] Social Sciences: 80 topics, 4 courses
- [x] Language & Communication: 83 topics, 4 courses
- [x] Literature: 101 topics, 5 courses
- [x] Music: 102 topics, 5 courses
- [x] Arts & Aesthetics: 72 topics, 4 courses
- [x] Practical Life Skills: 64 topics, 4 courses
- [x] Cross-domain prerequisite linking (15 domains reviewed)
- [x] Dangling reference cleanup (27 → 0)
- Grand total: 2,573 topics, 6,511 edges, 19 domains (pre-reconciliation)

## Phase 6: Quality Review — DONE
- [x] Spot-check prerequisite chains per domain for correctness
  - Longest chains reviewed across all 19 domains (21–147 steps). All pedagogically sound.
- [x] Expert review of highest-connected topics (hubs)
  - Top 5 hubs reviewed (ratios, mean-median-mode, mathematical-induction, percent-concept, partial-derivatives). All confirmed reasonable.
- [x] Identify and fill coverage gaps (thin courses)
  - 24 new topics added across 9 courses. All courses now have 20+ topics.
- [x] Resolve builds-toward consistency warnings (1,609 → 571 → 530)
  - Dialectic-reviewed reconciliation: 31 topics created, 35 IDs merged, 13 cycles removed, 942 same-course + 124 cross-course prereqs added, 411 transitive edges skipped
  - DAG-as-simplification note added to meta/schema.md
- [x] Review bidirectional pairs (75 → 39 → 0)
  - 39 pairs resolved via apply_bidirectional_fixes.py (36 directional, 3 dropped both)
- [x] Shallow content fixed (noun-phrases expanded)
- [x] Move reviewed topics from draft → validated status
  - All 2,628 topics promoted to validated
- [x] Built QA tooling: tools/qa_analyze.py (structural analysis), tools/apply_bidirectional_fixes.py

## Phase 7: Visualization Update — DONE
- [x] Update visualize_hierarchy.py to support multi-domain rendering
  - Auto-generates colors from `_domain.yml` configs, added `--all` flag for batch generation
- [x] Generate per-domain hierarchy visualizations
  - All 19 domains + index page generated via `--all`
- [x] Build full cross-domain graph visualization
  - `visualize_radial.py`: developmental-stage radial bands, curated domain ordering, polar force simulation
  - Two iterations: v1 used topological depth (incorrect), v2 uses developmental stage (correct)
- [x] Build individual topic detail pages
  - `generate_topic_pages.py`: 2,628 pages with Core Idea, prerequisite chains, successors, navigation
- [x] Click-to-navigate between graph views and topic detail pages

## Phase 7.5: Topic Granularity Expansion — DONE
Expanding non-math domains from ~20 topics/course toward ~35-40 topics/course.

### Phase 7.5a: Practical Life Skills + Language & Communication — DONE
- [x] Practical Life Skills: 80 → 160 topics (+80)
  - Financial Literacy +20, Cooking & Nutrition +20, Home Maintenance +20, Digital Literacy +20
- [x] Language & Communication: 89 → 189 topics (+100)
  - Grammar & Syntax +25, Linguistics +25, Public Speaking +25, Rhetoric & Composition +25

### Phase 7.5b: Engineering + Philosophy — DONE
- [x] Engineering: 115 → 188 topics (+73)
  - Statics & Dynamics +15, Materials Science +15, Fluid Mechanics +14, Circuits & Electronics +15, Control Systems +14
- [x] Philosophy: 124 → 210 topics (+86)
  - Logic +14, Epistemology +14, Metaphysics +14, Ethics +15, Political Philosophy +14, Philosophy of Mind +15

### Phase 7.5c: Formal Sciences + Chemistry — DONE
- [x] Formal Sciences & Logic: 81 → 148 topics (+67)
  - Propositional & Predicate Logic +15, Set Theory +17, Computability & Complexity +17, Category Theory +18
- [x] Chemistry: 112 → 181 topics (+69)
  - General Chemistry +19, Organic Chemistry +18, Physical Chemistry +14, Analytical Chemistry +18

**Total expansion: 2,628 → 3,100+ topics (+475)**

### Visualization Improvements (Mar 14)
- [x] Hierarchy view: flipped Y-axis (basics at top), blue/orange edge colors on hover
- [x] Radial view: domain-click navigation (outer ring → domain hierarchy)
- [x] Index page: links to both radial and hierarchy full-graph views
- [x] Domain hierarchy pages: nav links to index and radial view

### Infrastructure (Mar 14)
- [x] GitHub repo created: griffinhilly/open-knowledge-graph (public)
- [x] GitHub Pages: auto-deployed via Actions on push
- [x] GitHub Actions CI: validates + generates visualizations

## Phase 8: Community Launch — IN PROGRESS
- [x] Push to GitHub as public repo
- [x] Set up GitHub Actions for CI validation
- [x] Finalize README with coverage table update (13,489 topics)
- [x] Create issue templates for topic additions and corrections
- [x] Add Questions + Explainer schema (meta/schema.md, CONTRIBUTING.md)
- [x] Build adaptive placement assessment (generate_assessment.py + generate_assessment_page.py)
- [x] Fix developmental stage misassignments (746 topics across 8 domains)
- [x] Fix prerequisite cycles and format normalization (518 files)
- [x] Fix inflated cross-domain prerequisites (biology, chemistry, 6 other domains)
- [x] Overnight Q+E generation for 1,000 hub topics (~935 complete)
- [ ] Fix remaining radial graph positioning issues (hub topics misplaced)
- [ ] Add assessment generation to GitHub Actions workflow
- [ ] Add topic page links (domain/course as clickable navigation)
- [ ] Promote new draft topics to validated after review
- [ ] Write announcement post
- [ ] Populate Q+E across remaining topics (contributor-driven + more overnight runs)
