# Open Knowledge Graph Plan

## Current State

**14,946 topics** across 19 domains, **249 courses** (14 literature courses). Radial graph shows 18 domains (practical-life-skills excluded).

**Last session (Apr 3, 2026):**
- *Literature domain expansion*: 6 → 14 courses, 483 → 1,067 topics (+584). 8 new courses: Stories & Narrative, Mythology/Folklore/Oral Traditions (abstract-reasoning), Literary Movements & Periods, Genre Fiction, Creative Nonfiction, World Literature, Children's & YA Literature (formal-systems), Digital & Experimental Literature (advanced). All with Q+E.
- *Quiz balancing fix*: `generate_assessment_questions.py` now round-robins across courses within each stage tier.
- Literature quiz bias resolved — drama no longer dominates abstract-reasoning questions.

**Known issues:**
- **~14 near-duplicate pairs** in new literature courses (from double-generation). Low priority — different content, not true duplicates.
- **~2,550 T/F questions** with hedging language — ~1-3% arguable. Low priority.
- **Upstream over-staging**: Chemistry agent flagged physics/chemistry foundation topics. Targeted pass recommended.
- Index page + quiz not yet mobile-optimized
- Radial mouse/touch handler duplication
- **CI deployment failure** (Apr 3) — investigating

**Next steps:**
1. **Phase 11: Early-Childhood Expansion** — see below
2. **Fix CI deployment failure**
3. **Phase 9D** (remaining): domain toggle on radial, progress bars, guided learning paths
4. Write announcement post

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

## Phase 10.5: Literature Domain Expansion — DONE (Apr 3, 2026)

Expanded literature from 6 courses / 483 topics to 14 courses / 1,067 topics.

- [x] Stories & Narrative (52 topics, abstract-reasoning) — literary analysis on-ramp
- [x] Mythology, Folklore & Oral Traditions (43 topics, abstract-reasoning)
- [x] Literary Movements & Periods (94 topics, formal-systems) — Romanticism through Postmodernism
- [x] Genre Fiction (88 topics, formal-systems) — SF, fantasy, horror, mystery, romance
- [x] Creative Nonfiction (86 topics, formal-systems) — essay, memoir, journalism
- [x] World Literature (92 topics, formal-systems) — non-Western literary traditions
- [x] Children's & YA Literature (70 topics, formal-systems)
- [x] Digital & Experimental Literature (59 topics, advanced)
- [x] All topics have Questions (5 per topic) + Explainer sections
- [x] Quiz pool rebalanced with course round-robin selection
- [x] Validation passing, pushed to GitHub Pages

## Phase 11: Early-Childhood Expansion — PLANNED (Apr 3, 2026)

Build robust pre-formal and concrete-operations content so the OKG has genuine on-ramps for young learners across domains. Goal: a child starting the quiz at age 5-10 should find engaging, age-appropriate content in most domains.

### Design Principles
- **Don't force it.** Some domains legitimately start later. Economics for 5-year-olds is Practical Life Skills, not economics.
- **Deep where it matters.** Domains kids naturally engage with (music, stories, emotions, art) deserve thorough coverage, not token courses.
- **Match how kids learn.** Pre-formal = sensory, experiential, no notation. Concrete-operations = hands-on with models and simple systems.

### Current early-stage coverage
- **Strong (leave alone):** Mathematics (K-5th, 6 courses), Language & Communication (2 courses), Health (2 courses), Practical Life Skills (93 concrete topics)
- **Adequate (leave alone):** Biology, Chemistry, Earth & Space, Engineering, Formal Sciences, Physics (all have K-12 STEM expansion courses from Phase 8.5)
- **Gap — no content below formal-systems:** Computer Science, History, Literature, Music, Philosophy, Psychology

### Tier 1: Deep investment (~9-12 new courses, ~300-400 topics)

Domains where early-childhood content is genuinely rich and foundational.

#### Music (biggest gap — 0 early content)
Music is one of the first things children engage with. Singing, clapping, moving to rhythm start before age 2.

| Course | Stage | ~Topics | Content |
|--------|-------|---------|---------|
| Musical Play & Listening | pre-formal | 30-35 | Loud/quiet, fast/slow, high/low pitch, singing along, moving to music, instruments by family (shake/blow/hit/strum), musical games, call-and-response, lullabies, sound vs silence |
| Rhythm & Song | concrete-operations | 30-35 | Steady beat, simple patterns, clapping rhythms, note duration (long/short), simple songs and rounds, dynamics, tempo, basic notation (icons), instrument exploration, genres kids encounter |
| Listening & Musical Elements | abstract-reasoning | 30-35 | Melody recognition, major/minor mood, verse/chorus form, basic harmony, timbre, composing simple pieces, reading simple notation, musical cultures around the world |

#### Literature (currently starts at abstract-reasoning)
A 5-year-old's relationship with books is fundamentally different from a middle schooler's literary analysis.

| Course | Stage | ~Topics | Content |
|--------|-------|---------|---------|
| First Stories & Read-Alouds | pre-formal | 25-30 | Being read to, picture books, cover/title/author, beginning/middle/end at simplest level, characters we love, retelling a story, favorite books, wordless picture books, nursery rhymes, repetition and patterns in stories |
| Reading & Understanding Stories | concrete-operations | 30-35 | Main character vs supporting, problem and solution, sequence of events, making predictions, asking questions about stories, fiction vs nonfiction, comparing two stories, author and illustrator roles, chapter books, reading independently |

#### Psychology / Social-Emotional Learning (0 content below formal-systems)
Children do social-emotional learning from age 2 — naming feelings, empathy, self-regulation. This is a core early-childhood domain.

| Course | Stage | ~Topics | Content |
|--------|-------|---------|---------|
| Feelings & Self-Awareness | pre-formal | 25-30 | Naming basic emotions (happy, sad, angry, scared, surprised), body signals for emotions, it's OK to feel feelings, calming down strategies, expressing needs with words, comfort objects, routines and safety |
| Understanding Self & Others | concrete-operations | 30-35 | Empathy, perspective-taking basics, friendship skills, sharing and turn-taking, dealing with conflict, feelings vocabulary expansion (frustrated, embarrassed, proud, jealous), family feelings, grief and loss at a simple level, self-esteem |
| Growing Up & Getting Along | abstract-reasoning | 30-35 | Identity and self-concept, peer pressure, emotional regulation strategies, understanding bullying, growth mindset, resilience, communication skills, cultural identity, managing anxiety, healthy relationships |

### Tier 2: Lighter touch (~5-7 new courses, ~150-200 topics)

Domains with legitimate but less deep early-childhood content.

#### History
| Course | Stage | ~Topics | Content |
|--------|-------|---------|---------|
| Then & Now | concrete-operations | 25-30 | Long ago vs today, family history and stories, holidays and traditions, timelines (yesterday/today/tomorrow), community history, how things change over time, historical figures kids encounter, maps of "where I live" |

#### Philosophy
| Course | Stage | ~Topics | Content |
|--------|-------|---------|---------|
| Wondering & Thinking | concrete-operations | 25-30 | "Why?" questions, fairness and rules, right and wrong, what makes a good friend, is it ever OK to lie?, thought experiments for kids, "what would happen if...?", different points of view, imagination vs reality |

#### Social Sciences
| Course | Stage | ~Topics | Content |
|--------|-------|---------|---------|
| My Community & World | concrete-operations | 25-30 | Family structures, neighborhoods, community helpers, maps and directions, needs vs wants, rules and why we have them, cultural celebrations, near and far places, belonging to groups |

#### Arts & Aesthetics (has 4 pre-formal topics — expand to a full course)
| Course | Stage | ~Topics | Content |
|--------|-------|---------|---------|
| Creative Play & Expression | pre-formal | 25-30 | Drawing and scribbling, colors and shapes, cutting and pasting, clay and playdough, finger painting, patterns in art, looking at art and talking about it, art materials exploration, dance and movement, pretend play |

### Scope Summary
- **Tier 1:** ~9 courses, ~290 topics (Music 3, Literature 2, Psychology 3, + possible additional abstract-reasoning for Music)
- **Tier 2:** ~4-5 courses, ~125 topics (History, Philosophy, Social Sciences, Arts)
- **Total:** ~13-14 new courses, ~400-420 new topics
- **Execution:** Same pipeline as literature expansion — Haiku generation + parallel agents for Q+E, ~2 sessions

### Not expanding (and why)
- **Computer Science:** Logic/patterns for kids is already in Formal Sciences (Patterns & Logic). "Coding for kids" is really abstract-reasoning, not pre-formal/concrete.
- **Economics:** Money and trading basics are in Practical Life Skills. No need to duplicate.
- **Chemistry/Physics/Biology/Earth Science:** Already have concrete-operations courses from Phase 8.5.
- **Engineering:** Already has Design & Build (concrete-operations).
