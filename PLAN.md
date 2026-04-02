# Open Knowledge Graph Plan

## Current State

**14,362 topics** across 19 domains, **235 courses** (6 new). Radial graph shows 18 domains (practical-life-skills excluded).

**Last session (Apr 1, 2026) — Quality review + dangling prereqs + Phase 10 question audit:**
- *Quality review*: 55 new topics spot-checked — all structurally clean, content excellent (10/10 courses sampled).
- *Dangling prereqs RESOLVED*: 482 → 0. Built `fix_dangling_prereqs.py`: 325 IDs remapped, 153 refs removed, 11 cycles fixed.
- *Phase 10 (Question Quality Audit)*: 240 question fixes total.
  - 10A: 181 `can rarely→cannot`, 21 `if and primarily if→if and only if`, 35 garbled idioms, 3 sentence-initial `Primarily→Only`. Heuristic analysis of remaining 2,550 hedged questions shows ~1-3% true error rate (not 17% initially estimated).
  - 10B: No meta-pedagogical issues in user-facing pools.
  - 10C: No stage-content mismatches — all 1,009 pre-formal/concrete topics audited, questions are age-appropriate.
  - 10D: No compound-question issues found.
  - 10E: Quiz staleness warning added to pre-push hook.
- *Tooling*: Built `fix_dangling_prereqs.py`, `audit_hedged_tf.py`.
- *P2 topic generation*: +320 topics across 6 new courses + extensions to 15 existing courses. 14 Haiku agents total (9 initial + 5 fix/regen). 25 YAML errors, 5 duplicates, 1 cycle fixed post-generation.
  - New courses: applied-ethics, history-of-science, economic-social-history, robotics-and-autonomous-systems, music-technology, contemporary-art-new-media
  - Extended: ML-theory, quantum-computing, cryptography, information-theory, formal-methods, advanced-algorithms, control-systems, signals-and-systems, materials-science, philosophy-of-science, continental-philosophy, early-language-foundations, advanced-linguistics

**Known issues:**
- **New P2 topics need Q+E quality review** — Haiku-generated content may have shallow explainers or generic questions. Spot-check recommended.
- **New P2 topics may have dangling prereqs** — agents referenced topics that don't exist. Run `map_dangling_prereqs.py` to assess.
- **~2,550 T/F questions** with `primarily`/`typically`/`generally` hedges — ~1-3% may be arguably true. Low priority.
- **~966 near-duplicate pairs** — mostly false positives. Low priority.
- Quiz/assessment data stale after P2 additions (pre-push hook will warn)
- _domain.yml course stages may need reconciliation for new courses
- Index page + quiz not yet mobile-optimized
- Radial mouse/touch handler duplication

**Next steps:**
1. **Music-history restaging** — 63 topics at abstract-reasoning should be formal-systems (their prereqs are formal-systems theory topics). Course-level stage fixed; individual topics need restaging pass.
2. **Phase 9D** (remaining): domain toggle on radial, progress bars, guided learning paths
3. Write announcement post

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
- [x] Finalize README with coverage table update (13,518 topics)
- [x] Create issue templates for topic additions and corrections
- [x] Add Questions + Explainer schema (meta/schema.md, CONTRIBUTING.md)
- [x] Build adaptive placement assessment (generate_assessment.py + generate_assessment_page.py)
- [x] Fix developmental stage misassignments (746 topics across 8 domains)
- [x] Fix prerequisite cycles and format normalization (518 files)
- [x] Fix inflated cross-domain prerequisites (biology, chemistry, 6 other domains)
- [x] Overnight Q+E generation for 1,000 hub topics (COMPLETE, 1,006 total)
- [x] Fix graph-theory-and-combinatorics + probability-and-mathematical-statistics stages
- [x] Topic page domain breadcrumb as clickable link
- [x] Fix radial graph positioning (rotation bug, angular spring-back, prereq ordering force)
- [x] Click-to-preview panel with locked edge highlights on all graph views
- [x] Search bar (Ctrl+F) on all graph views
- [x] Course breadcrumb links on topic pages
- [x] culture-concept data fix (stage + edge corrections)
- [x] Render Questions + Explainer sections on topic detail pages
  - Explainers render on topic pages; Questions on separate interactive pages with scoring
- [x] Explainer generation for all 13,489 topics (30-worker Sonnet swarm, Mar 16)
- [x] Clickable tag pages (20,531 pages) with tag index
- [x] Graph search matches tags and courses (not just title/ID)
- [x] Mobile touch support (pinch-to-zoom, pan, tap-to-select, touch-action:none)
- [x] Pre-commit hook fixed to whitelist domains/ directory
- [x] Removed duplicate Mean, Median, and Mode topic (college-level)
- [x] Confirm mobile touch fix working; remove debug overlay from hierarchy views
  - Root cause: JS temporal dead zone error (`hoveredNode` declared after `draw()` call)
  - Also fixed: pinch-to-zoom anchoring, duplicate mousemove handlers, course name casing
  - Also fixed: radial graph mobile header overlap, legend too large on mobile
  - Added close button to info panel on all graph views
- [x] Add Applied Rationality course under Philosophy (30 topics, 6 topic groups)
  - Placement validated via 3-agent dialectic (Philosophy 8/10 vs Psychology 5/10 vs Formal Sciences 3/10)
- [x] Finalize domain ordering on radial graph
  - 8-agent dialectic: Modified Arc wins. Swapped Earth & Space ↔ Chemistry for natural science adjacency.
  - Narrative: formal foundations → physical sciences → life sciences → mind → society → humanities
- [x] Questions generation for ~13,505 topics (Q5 swarm + retry pass Mar 21, 99.9% coverage)
- [x] Full-coverage validation audit (50 Haiku + 4 Sonnet + Opus dialectic referee)
  - 11,035 draft topics validated. 97.5% pass rate (98.7% after false positive filtering)
  - 6,200+ files fixed: stage inversions, bidirectional pairs, orphans/islands, shallow content, TODO placeholders
  - Dialectic-reviewed: geology prereqs, music staging, anatomy prereq direction
- [x] Stage inversion cascade fix (5,979 promotions across 8 passes)
  - Eliminated radial ordering violations caused by stage misassignment
- [x] Stage assignment audit + fix: 181 mis-staged topics fixed across 14 courses
  - 107 high-confidence (Mar 21): theory-of-computation (32), cell-biology (26), research-methods-psychology (23), oceanography (17), thermodynamics (4), 1st-grade math (5)
  - 61 high-confidence (Mar 22): microeconomics (14), historical-methods (11), political-philosophy (9), logic-and-critical-thinking (6), public-speaking (7), ancient-civilizations (9), music-theory-fundamentals (5)
  - 13 dialectic-decided (Mar 22): 1-1-1 Opus dialectic reviewed 32 borderline topics → 13 restaged, 20 kept as on-ramps
- [x] Missing explainers filled: 130 topics across math (45), music (41), philosophy (43), physics (1) — Opus 4.6 generation
  - All 13,518 topics now have both Questions and Explainer sections (100% coverage)
- [x] Promote all topics to validated (11,508 promoted Mar 23)
- [x] CS programming-fundamentals dedup: 116 → 50 topics (66 duplicates merged, 168 refs updated)
- [x] Add assessment + quiz + domain map generation to GitHub Actions workflow (Mar 25)
- [x] Pre-push hook: cycle detection + CI script tracking (`hooks/pre-push`, ~7s)
- [x] Navigation swap: all links → domain maps, hierarchy pages removed from CI
- [x] Domain map course anchor support (`#course-id` pans/zooms to course)
- [x] Radial branch integration: COURSE_BRANCH_X positions + auto-detected flips (3-domain angular window)
- [x] Leaf connector: 1,069 connections across 5 domains (39.8% → 34.4% leaves)
- [x] Dedup: 18 duplicate pairs merged (13,429 → 13,411 topics)
- [x] Replace regex YAML with PyYAML in `visualize_domain_map.py`
- [ ] Write announcement post

## Phase 8.5: K-12 STEM Expansion — DONE (Mar 22, 2026)
Add introductory courses (pre-formal through abstract-reasoning) to 7 STEM domains that currently have no content below formal-systems. ~500 new topics across ~16 new courses.

### Session 1: Physics + Chemistry — DONE (Mar 22, 2026)
- [x] Physical Science (40 topics, concrete-operations)
- [x] Conceptual Physics (40 topics, abstract-reasoning)
- [x] Properties of Matter (36 topics, concrete-operations)
- [x] Introductory Chemistry (35 topics, abstract-reasoning)

### Session 2: Biology + Earth & Space — DONE (Mar 22, 2026)
- [x] Living Things (40 topics, pre-formal/concrete)
- [x] Life Science (40 topics, concrete/abstract)
- [x] Earth & Weather (37 topics, pre-formal/concrete)
- [x] Earth Science (35 topics, concrete/abstract)

### Session 3: Health + Engineering + Formal Sciences — DONE (Mar 22, 2026)
- [x] My Body (30 topics, pre-formal/concrete)
- [x] Health Foundations (30 topics, concrete/abstract)
- [x] Design & Build (30 topics, concrete-operations)
- [x] Engineering Principles (30 topics, abstract-reasoning)
- [x] Patterns & Logic (25 topics, concrete-operations)
- [x] Reasoning & Proof (25 topics, abstract-reasoning)

**Total: 473 new topics across 14 new courses, 7 domains. 13,991 topics at completion (later reduced to 13,925 by CS dedup).**

### Post-expansion
- [x] Cross-domain prerequisite audit (43 dangling refs fixed, 8 stage violations softened)
- [x] Regenerate visualizations (13,925 topic pages, 19 hierarchy views, radial graph, quiz)
- [ ] Push + deploy to GitHub Pages

## Phase 9: Learning Platform — PLANNED (Mar 19, 2026)
Transform OKG from a static knowledge map into an interactive learning tool. Inspired by Math Academy's adaptive learning model. Nine features across four implementation phases.

### Phase 9A: Fluency Model + Visual Integration — DONE (Mar 19, 2026)
- [x] Define fluency data model: continuous 0-100 per topic, Bayesian log-odds updates
- [x] Implement localStorage schema (`okg-fluency`, `okg-fluency-meta`, `okg-goals`, `okg-adjustments`)
- [x] Implement prerequisite propagation (backward: 0.85^hops decay, forward: ceiling on successors)
  - Forward cap only uses direct evidence (not backward-inferred scores) to avoid circular reasoning
- [x] Add fluency toggle on topic pages (manually mark known)
- [x] Modify graph views to color nodes by fluency
  - Radial + cross-domain hierarchy: domain-hue mode (saturation/lightness by mastery)
  - Per-domain hierarchy: universal mastery gradient (gray→red→amber→green)
  - Frontier topics get gold borders on all views
- [ ] Better visual differentiation: hub topic labels at moderate zoom, directional edge rendering (DEFERRED)

### Phase 9B: Assessment Engine — Phases 1 & 2 — DONE (Mar 21, 2026)
- [x] Build `generate_assessment_questions.py` — extract question bank, prioritize by hub connectivity
  - 13,224 topics with questions, 63,837 total. Quiz pool: 228 warmup + 506 exploration (MC/TF only)
- [x] Assessment welcome screen (low-stakes framing: "trivia game, not exam")
- [x] Phase 1 Warm-Up: cross-domain MC/TF rotation, round-robin across 19 domains
  - Warmup uses lowest available stages per domain (pre-formal/concrete where available, abstract fallback)
- [x] Phase 2 Exploration: per-domain adaptive questioning, all stages, user picks domain
  - "Something different", "Skip domain", "I'm done" controls
- [x] Silent response time tracking (fast/slow modulates evidence weight via fluency.js)
- [x] Asymmetric update rule (wrong answers at 0.7× penalty — uses fluency.js engine)
- [x] "Skip this domain" to dismiss uninterested domains
- [x] Quiz page: `output/quiz.html` (851 KB self-contained, embedded fluency.js + data)
- [x] Index page updated with quiz link

### Phase 9C: Assessment Phase 3 + Results — DONE (Mar 25, 2026)
- [x] Phase 3 Deep Dive: user-selected domains, formal→advanced→expert, short-answer self-graded
  - 483 questions across 19 domains, textarea for user answers before reveal
  - Self-grading: Got it (1.0) / Partially (0.5) / Missed it (0.0)
- [x] Results screen: mini radial canvas (162 course-level nodes, fluency-colored)
- [x] Domain summary cards with course-level fluency breakdowns (collapsible)
- [x] Manual adjustment sliders (per-course, -30 to +30, persisted to localStorage)
- [x] Frontier highlighting weighted by explored/deep-dived domains (1.5x/2.0x boost)
- [x] Fluency model fixes: backward propagation depth 6→12, forced floors for stages 2+ below demonstrated, conservative cross-domain inference, exploration starts at demonstrated tier

### Phase 9D: Landing Page + Polish
- [ ] Redesign index page: "Explore the Map" vs "Personalize Your Map"
- [ ] "Show Domains" toggle on radial graph (collapse dots to labeled domain nodes)
- [ ] Course-level progress bars on hierarchy views and index page
- [ ] Guided learning paths (topological sort of uncompleted topics, goal-directed pathfinding)
- [ ] "Why this topic?" tooltips (downstream fan-out, goal dependencies)
- [x] Export/import progress as JSON (cross-device transfer) — Apr 1, 2026
- [x] Redesign index page: hero CTAs, domain grid with hue accents, practical-life-skills separated — Apr 1, 2026
- [x] Link "Personalize Your Map" to quiz instead of self-rating assessment — Apr 1, 2026
- [ ] Shareable profile URLs (stretch — start with JSON export)

## Phase 10: Question Quality Audit — DONE

Systematic audit of the ~65K question bank. Five issue patterns investigated, 240 fixes applied.

### 10A: T/F Hedging Audit — DONE
- [x] Build audit script (`audit_hedged_tf.py`): 2,770 T/F false questions flagged with hedging language
- [x] Fix `can rarely` pattern: 181 questions reverted to `cannot`
- [x] Fix garbled idioms: 21 `if and primarily if → if and only if`, 35 `primarily one/works/applies/etc. → only`, 3 sentence-initial `Primarily → Only`
- [x] Heuristic evaluation of remaining ~2,550 hedged questions: ~1-3% true error rate (25-75 questions), not the 17% initially estimated. Low priority — the hedged versions are "arguable," not clearly wrong.

### 10B: Meta-Pedagogical Questions — DONE (no issues)
- [x] Audited warmup pool (228), exploration pool, and all pre-formal/concrete topics
- [x] Zero meta-pedagogical questions found in user-facing pools

### 10C: Stage-Content Mismatch — DONE (no issues)
- [x] Audited all 1,009 pre-formal/concrete-operations topics (keyword + title + quiz pool review)
- [x] All questions are age-appropriate. Mar 30 restaging pass resolved the bulk of issues.
- [x] Reviewed 28 pre-formal + 90 concrete warmup questions — all appropriate for declared stage

### 10D: Double Questions — DONE (no issues)
- [x] Audited 79 potential compound questions — all legitimate scenario-based formats

### 10E: Stale Quiz Data Prevention — DONE
- [x] Added staleness check to `hooks/pre-push`: warns when topic files are newer than `assessment-questions.json`
