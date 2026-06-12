# Open Knowledge Graph Plan

## Current State

**15,290 topics** across 19 domains, **261 courses**. Radial graph shows 18 domains (practical-life-skills excluded).

**Last session (Apr 9, 2026):**
- *Phase 9D effectively DONE*: Removed domain toggle from radial. Built guided learning paths (goal starring UI, path engine in fluency.js, learning path section on index with lazy-loaded graph.js, "Why this topic?" context on index + topic pages).
- *Cleanup debt resolved*: 14 literature duplicate pairs merged (30 reviewed, 16 false positives). 7 missing Questions sections regenerated. Dedup cycle fixed. Shareable profile URLs deferred (JSON export covers it).
- Fixed pre-existing bug: `STAGE_ORDER` in fluency.js was missing 'expert' stage.

**Known issues:**
- **~2,550 T/F questions** with hedging language — ~1-3% arguable. Low priority.
- **Upstream over-staging**: Chemistry agent flagged physics/chemistry foundation topics. Targeted pass recommended.
- Index page + quiz not yet mobile-optimized
- Radial mouse/touch handler duplication
- Topic page "Why this topic?" shows static downstream count only (no goal-aware context — would need graph.js on topic pages)

**Last session (Apr 12, 2026):**
- **Phase 12A shipped in 4 cuts** — all 9 steps. Net +267 LoC. Surfaces: cold-start prior, alpha-gradient opacity field, stage slider DOM overlay, 24Q stratified seed, refine-your-map domain slider, next-step retention card, inline know/don't-know panel buttons, index CTA + `preset=sprout` stub.
- **Phase 12B Cuts 5+6 shipped** — pedagogy-typing on 19 `_domain.yml` files (13 assessable / 6 reflective), reflective card variant on topic pages, reflective-domain frontier variant in `findFrontier`, stale-topics signal, soft-edge propagation (`BACKWARD_DECAY_SOFT=0.425`), per-path decay in `propagate()`. See MEMORY.md.
- **Phase 12B Cut 7 shipped** (commit `d65f8551e`, pushed) — Sprout shell for Persona A. Net +427 LoC. See MEMORY.md.

**Last session (Jun 10-11, 2026) — initial-view audit + SEO sprint + DOMAIN:**
- **openknowledgegraph.com is FULLY LIVE (Jun 12)**: HTTPS enforced (cert auto-renews), Cloudflare proxy ON + SSL Full (strict), email spoofing locked down (SPF -all, DMARC reject, null MX), old github.io URLs 301. Search Console domain property verified + sitemap submitted (expect "Processing data" lag 24-48h — normal, don't debug). Cert gotcha hit and solved: GH Pages cert provisioning is one-shot — fired while DNS was still Cloudflare-proxied and stuck at null; `pages/health` API diagnosed, remove/re-add domain forced a fresh cycle. Note: .org was already taken; one-letter neighbor openknowledgegraphs.com (plural, semantic-web catalog) exists — accepted risk.
- **Cold-visit audit** (headless-Chrome screenshots + code-side surface map + comparable-product research): full findings and ranked ideas at `plans/initial-view-and-usage-ideas-2026-06-10.md`. Headline: all ~15k topic pages were invisible to search (no meta/sitemap/structured data); graph-as-hero is a documented failure mode (Khan retired theirs); search-first + ancestry-reveal is the highest-leverage intuitiveness idea.
- **SEO sprint SHIPPED**: meta description + canonical + Open Graph on all page types (shared `seo_meta_tags`/`meta_description` helpers in `parse_topic.py`); JSON-LD `LearningResource` per topic page (`educationalLevel`, `teaches`, `competencyRequired` = hard prereqs); new `tools/generate_sitemap.py` → sitemap.xml (15,312 URLs; tag/question pages excluded by design) + robots.txt; CI step added. **Activation step: submit sitemap via Google Search Console** (robots.txt at a project-page subpath is not read by crawlers).
- **Stage-card auto-show reversed** (see Phase 12A Step 2 note).
- **Index count inflation fixed**: hero said 16,951 — `load_graph`'s phantom "external" nodes were being summed into domain stats. Now counts real nodes only (15,290). Domain-card counts also corrected.
- Also fixed: `STAGE_LABELS` in `generate_topic_pages.py` was missing `expert` (same bug class as fluency.js `STAGE_ORDER`); topic + questions pages had no viewport meta tag.
- **Ideate dialectic RUN (Jun 11, 5-2-3 Opus)**: full verdict at `plans/ideate-dialectic-2026-06-11.md`. BUILD consensus: (1) B3 og:image + A6 topic-page upgrades first, (2) NEW: keystone leaderboard ("50 most powerful things to learn", edge-audit top-80 first), (3) ONE path engine consolidating A2/A3/B4 + bridge-path/six-degrees (hard gate: no-path fallback), (4) B2 explorable → Show HN launch, (5) NEW: .ics Comeback Card post-launch. Killed: binary-search frontier, hosted MCP, vote tallies, two-player duel (localStorage can't aggregate). **Gating manual action: Griffin submits output/sitemap.xml to Google Search Console** — project-page robots.txt is not read by crawlers, so without submission the SEO sprint stays dormant.

**Last session (Apr 25, 2026) — STRATEGIC PIVOT, no code:**
- Griffin had been deferring OKG ~2 weeks; flagged the parent-acquisition intuition gap. Triggered `/dialectic-review --ideate` (5 lenses × 2 challengers × 3 synthesizers, all Opus xhigh) → 33 ideas → 15 clusters → top 5 ranking.
- **Griffin's K-reframe correction**: dialectic dismissed the "gifted accelerator track" with a 5%-TAM frame; Griffin pushed back — actual demographic is 20-30% of intentional parents who feel their kid is held back by school pace. Folded into Tradeoff #2 as a 4th option mid-stream.
- Two `/dialectic-review --tradeoff` rounds (T1: content-vs-product; T2: opening wedge among 4). Both referees converged on a hybrid sequence; both independently rejected "calibration" framing in favor of *topology verification*.
- **Final integrated plan** at `plans/parent-acquisition-ideation.md` (~5000 words): B-first build (worksheet OCR, math 2-5, narrow to Beast/Eureka/enVision/Singapore — Beast as bridge curriculum), K-reframed *positioning* (heatmap output reframed as "prereq chain blocking ceiling expression"), days-60-90 layer K-radial on warm B users, TikTok deferred, Mrs. Johnson eliminated.
- **Concrete 2-day pre-build move**: 3 manual worksheet diagnoses → Twitter threads in K-reframed framing → measure ≥30 likes + ≥3 "where can I get this" replies as gate, OR trigger `/dialectic-review --premortem` on the wedge itself.
- **Session reviewer flagged 3 unaddressed weaknesses**: (1) Twitter-standing assumption is doing more work than admitted (Griffin orbits the cluster but hasn't posted as OKG-content); (2) recruitment problem (Addi 2.5, no school-age kids in immediate network) waved away — synthetic worksheets/cold-DMs each their own project; (3) Week-4 kill gate assumes Griffin will execute against his own work, exactly the failure pattern from Phase 12A and Bottom Billion exhaustive-path. Reviewer rec: externalize the kill gate (Madi check-in, calendar-triggered `/dialectic-review --premortem` on May 23).
- **Griffin paused at decision-time**: wants to sit with it before committing.

**Next steps — DISTRIBUTION TRACK (post Jun 11 dialectic; the active track):**
0. **FIRST, two session-reviewer mandates (Jun 12) before any BUILD item:** (a) **Strategy-fork decision for Griffin**: the distribution track now competes with the paused Apr 25 parent-acquisition wedge for the project's center of gravity — these are different products; decide which is being built (or explicitly run both with priorities) rather than letting adjacent work decide by default. (b) **Analytics snippet** (Cloudflare Web Analytics or GoatCounter) — GATES the entire dialectic sequence, since every "ship then measure" item is unexecutable without a measurement layer. One script tag in the generators, ~10 min.
1. **B3 og:image cards (hub topics first) + A6 topic-page cold-landing upgrades** — same file/session (`generate_topic_pages.py` + a render step); the substrate every shared link lands on. NCP native-HTML/CSS pipeline transfers.
2. **Keystone leaderboard** — "50 most powerful things to learn." HARD GATE before publishing: edge-audit the top ~80 candidates + decide hub-bias methodology explicitly (state it on the page). Don't skip the gate because the page looks trivially shippable.
3. **Path engine cluster** — ONE engine for A3 ancestry reveal → A2 search-first → B4 shareable subgraphs → curated six-degrees gallery. HARD GATE: explicit no-path fallback UX before any two-topic surface ships.
4. **B2 "counting → QFT" explorable → Show HN launch.** Do not launch before 1-3 are live.
5. **Comeback Card (.ics)** post-launch.
- **Pre-launch checklist (cheap, must precede Show HN)**: write README.md (repo has none!); add analytics (Cloudflare Web Analytics or GoatCounter — zero-backend; without it the dialectic's "gate features on evidence" sequencing has nothing to read); bump CI actions for the ~Jun 16 Node-24 cutover.
- **Housekeeping**: Griffin confirm sitemap shows "Success" in Search Console (~Jun 13); remove dead `STAGE_CARD_DISMISSED_KEY` write; clear untracked root cruft (old batch scripts, dedup_stderr.txt, stale `.claude/worktrees/radial-zoom-sizing/`).
- **Scheduled cloud routines (manage at claude.ai/code/routines)**: Node-24 deploy check (one-time, Jun 17); SEO pulse (one-time, Jun 26); **dormancy pulse (monthly, 1st @ 9am CT — nudges with PLAN item-0 verbatim if repo >21 days quiet; self-expires in-prompt after Sep 15, 2026, then Griffin disables it in the UI)**.
- Full dialectic verdict + EXPLORE/PARK tiers: `plans/ideate-dialectic-2026-06-11.md`.

**Next steps — PARENT-ACQUISITION TRACK (unchanged since Apr 25, still PAUSED at decision-time):**
1. **Run the 2-day Twitter test BEFORE any OCR code.** This is the gate: 3 manual worksheet diagnoses (synthetic from AoPS/Beast public samples is acceptable for v0) → Twitter threads → measure organic reception in Griffin's existing edu-acceleration cluster orbit. ≥30 likes + ≥3 "where can I get this" replies = signal to build. <10 likes = trigger `/dialectic-review --premortem` on the parent-acquisition wedge.
2. **Externalize the Week-4 kill gate** — calendar-trigger or Madi check-in for May 23. Not Griffin's own discipline (per reviewer; Phase 12A flagged this exact failure pattern).
3. **Cost the recruitment problem explicitly** — synthetic-vs-real worksheet sourcing decision before Day 1.
4. **Resume only on signal**: build OCR (math 2-5, Beast/Eureka/enVision/Singapore curricula) only after the Twitter test passes.
5. **Deferred (not blocking 90-day plan)**: Phase 12A/B follow-ups (MC bias data fix, course-level Deep Dive picker, stage-inversion edge spot-check), announcement post for Phase 12, Phase 9D stretch, hero-image retrofit.

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
- [ ] Finalize README — **FALSE LEDGER ENTRY caught Jun 12, 2026: this was marked [x] but no README.md exists anywhere in the repo.** Must be rewritten before any launch moment (the repo is a landing page for HN/researchers).
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
- [x] Removed "Domains" toggle from radial graph (low utility, took mobile real estate) — Apr 6, 2026
- [ ] Course-level progress bars on hierarchy views and index page
- [x] Guided learning paths — goal starring, path engine (BFS + topo-sort), learning path on index, lazy-loaded graph.js — Apr 9, 2026
- [x] "Why this topic?" — index path shows goal targets + fan-out; topic pages show transitive downstream count — Apr 9, 2026
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

## Phase 11: Early-Childhood Expansion — DONE (Apr 4, 2026)

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

## Phase 12: Three-Persona Redesign — IN PROGRESS

Virality-first learning platform redesign. Serves three personas (young child + parent, high school student, fuzzy-recall college graduate) on one engine, straddles the virality-vs-utility tension (graph is the hook, learning plans are the retention), and aims net-subtractive where possible.

**Full plan**: [plans/phase-12-three-persona-redesign.md](plans/phase-12-three-persona-redesign.md)

**Designed via 3-round multi-agent dialectic** (adaptive psychometrics / Math Academy pedagogy / UX progressive disclosure / anti-complexity skeptic → Opus referee).

### Phase 12A — PARTIALLY SHIPPED (Apr 12, 2026)

7 of 9 plan steps fully shipped; 2 shipped with known divergences from the plan. See MEMORY.md "Phase 12A Shipped" and "Phase 12A Reviewer Findings" for implementation decisions and what is still outstanding.

- [x] Step 1: Cold-start prior formula in fluency.js (`computeFloor`, `getUserStage`, `getDomainPrior`)
- [x] Step 2: Stage slider DOM overlay with first-visit auto-show + dismiss persistence
  - **REVERSED Jun 11, 2026 (Griffin's call)**: first-visit auto-show removed — the card covered the map center before a new visitor saw anything (confirmed by cold-visit screenshot audit). Level button is now the only entry point. Dismiss-flag write in `hideStageCard` is dead code pending removal.
- [~] **Step 3: Alpha-gradient opacity field ADDITIVE, not a replace.** The plan specified "Single render path: opacity = f(…). Replaces the dual color-mode code" with a net −60 LoC delete. What actually shipped: the alpha gradient was added inside the existing `if (showFluency)` branch, and `showFluency` plus its ~10 branches were retained as a pure-map escape hatch (Griffin's explicit call). The −60 delete did not happen. The new opacity code is an overlay on top of the existing dual-mode path, not a replacement for it. **Outstanding**: either delete the `showFluency` branches and make the opacity field the single render path (as the plan intended), or formally amend the plan to "additive" and reconcile the LoC ledger.
- [x] Step 4: "Your next step" retention corner card
- [x] Step 5: Inline "I know / don't know this" buttons on topic panel
- [x] Step 6: 19-row "Refine your map" domain slider writing to `okg-domain-prior`
- [x] Step 7: 24Q stratified seed replaces warmup+exploration phases (opt-in via welcome chooser)
- [~] **Step 8: 3-phase scaffolding delete was PARTIAL.** Plan said "delete the warmup→exploration→deep-dive state machine"; actual delete removed only warmup and exploration. Deep-dive flow retained as an opt-in second entry from the welcome chooser (Griffin's explicit call to preserve extensive single-domain testing). The −250 LoC credit booked against the budget is partially fictional — real delete was closer to −200. **Outstanding**: either finish deleting deep-dive, or formally amend the plan to recognize deep-dive as a retained opt-in feature.
- [x] Step 9: Index CTA cleanup + `preset=sprout` stub link

**Net LoC: +267 across 4 files** (plan target −50/+150). The two step divergences above account for approximately **+140 LoC of the overshoot** (step 3's undelivered −60 + step 8's partial delete). The remaining ~+80 LoC of overshoot is refine + next-step card DOM/CSS coming in heavier than estimated. This correction is material — the original framing attributed the entire overshoot to CSS bloat, which would suggest trimming CSS as the fix. The actual fix is reconciling the undelivered deletes.

### Phase 12B — IN PROGRESS

**Cuts 5-6 DONE (Apr 12, 2026)** — engine work, no new UI shell:
- [x] Step 5: `pedagogy_type` added to all 19 `_domain.yml` files
- [x] Step 6: Reflective card variant (Mark-as-read + optional reflection text) on topic pages
- [x] Step 7: Reflective-domain frontier variant in `findFrontier`
- [x] Step 11: Stale-topics frontier signal (21-day, score-in-[50,85] band)
- [x] Step 8: `tools/label_edge_strength.py` written (not run)
- [x] Step 9: 200-topic / 542-edge sample QA via parallel Haiku agents (plan usage) — 0.7% flip rate, full pass skipped
- [x] Step 10: Soft-edge propagation (`BACKWARD_DECAY_SOFT=0.425`, forward cap hard-only, avgPrereq hard-only)

**Cut 7 SHIPPED (Apr 12, 2026)** — Sprout shell. Dialectic-reviewed before coding (2A-2C-1R tradeoff mode, 6 sub-decisions). Bundle broke; flipped three defaults from the initial approach: AND trigger instead of OR, coloring-book replaces radial instead of sidebar, shared URL renders Sprout + "See full map" CTA instead of falling through to graph. All code lives in `tools/visualize_radial.py` (conditional branch honoring the Phase 12 one-component-tree ruling).
- [x] Step 2: SproutCard conditional render branch — full-screen topic, emoji-first, Web Speech API TTS, three emoji response buttons, 9-wedge coloring-book SVG replacing the radial, browser-verified at 567px and 1420px
- [x] Step 3: Parent PIN opt-in via SubtleCrypto SHA-256, session-bypass after correct verify
- [x] Step 4: Coloring-book SVG progress visualization (9 pre-formal domains, fills per topic mastery)
- [x] Trigger: `preset=sprout AND (no prior fluency OR stage===0)` — Persona C grad-student ambush fixed
- [x] Old `preset=sprout` stub removed from `initStageSlider`; detection now lives at the top of the script block
- [ ] Step 1: Hero image audit (Griffin, ~20 min) — **deferred to post-ship retrofit**

**Deferred eval**: Phase 12B Cut 7 ships Sprout without Persona A validation. No real child testers exist in 12B (Addi is 2.5). Hero-image retrofit and the "real child uses without adult interpretation" success criterion are gated on the first actual Persona A tester. Do not let "we shipped emoji in Cut 7" become institutional justification for never retrofitting — the dialectic referee explicitly flagged this tradeoff as the key unvalidated cost of Cut 7. `HERO_IMAGE_RETROFIT` TODO markers live at the emoji render site in `visualize_radial.py` and in `SPROUT_DOMAIN_EMOJI`.

### Phase 12C — CONDITIONAL
- **Rasch upgrade** (1-3 weeks, conditional): only if stage heuristic proves off by >1 stage in >20% of sampled users. Rasch with θ ∈ ℝ^8, Fisher-info adaptive seed, reflective-domain exclusion

**Non-goals**: lesson-feed-as-primary-surface, FSRS, 2PL IRT, new per-topic attributes, persona-router page, demographic onboarding questions, separate shell codebases.
