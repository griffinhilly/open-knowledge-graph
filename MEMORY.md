# Open Knowledge Graph Memory

## Status (Apr 12, 2026)
- **15,290 topics** across **19 domains**, **261 courses** (16 literature courses)
- **6 developmental stages**: pre-formal, concrete-operations, abstract-reasoning, formal-systems, advanced, expert
- **Radial graph shows 18 domains** (practical-life-skills excluded — kept on index/domain maps)
- GitHub Pages: `griffinhilly.github.io/open-knowledge-graph/`
- Phase 10 DONE. Phase 10.5 (Literature Expansion) DONE. Phase 11 (Early-Childhood) DONE. **Phase 9D effectively DONE.**
- **Phase 12A DONE** (Apr 12, 2026): virality-first onboarding shipped in 4 cuts. All 9 plan steps delivered. Net +267 LoC (plan target −50/+150; over-budget on refine + next-step card DOM overhead, within "gut-check not abort" threshold). Next actionable: Phase 12B (Sprout + pedagogy-typing + per-edge strength).
- **Domain maps are primary navigation** — hierarchy views removed from CI and all links
- **CI pipeline**: validate → index → radial → topic pages → domain maps → assessment → quiz
- **Pre-push hook**: `hooks/pre-push` — cycle detection + CI script tracking + quiz staleness warning + question YAML error checks (~17s). Setup: `git config core.hooksPath hooks`
- **Learning paths (Apr 9)**: Goal starring on topic pages, `computePathToGoal`/`computeLearningPath` in fluency.js (BFS + topo-sort), "Your Learning Path" on index (lazy-loads `js/graph.js` 3.5MB only when goals exist), "Why this topic?" context (index: goal targets + fan-out; topic pages: static downstream count).
- **Literature dedup (Apr 9)**: 14 pairs merged from 30 candidates. 16 false positives (legitimate prereq chains). One dedup cycle fixed (code-poetry-aesthetic ↔ generative-poetry-algorithms-text). 7 stripped Questions sections regenerated.
- **Cross-domain prereq audit DONE** (Apr 5): 67 connections from Phase 11 + 7 gap-filling bridges. Total: 74 cross-course connections.

## 6-Stage Schema (Mar 22, 2026)
- **Added "expert" stage** for graduate/research content (2,662 topics)
- **Broadened formal-systems** to include standard undergraduate curriculum (not just mathematical proof)
- **Stage criteria**: stage = where content is typically first encountered, not difficulty ceiling
- **Audit pipeline**: Haiku swarm (10 agents) → Opus referees (3 agents) for debatable cases
- Key referee decisions:
  - CS programming fundamentals: kept at abstract-reasoning (programming taught to middle schoolers)
  - Computability & complexity: split 47/51 (standard ToC → formal-systems, advanced complexity stays)
  - Physics QM: Griffiths ch1-3 stays formal-systems, Bell's theorem → advanced

## K-12 STEM Expansion (Mar 22, 2026)
- **473 new topics** across 14 courses in 7 domains
- Physics: Physical Science (40) + Conceptual Physics (40)
- Chemistry: Properties of Matter (36) + Introductory Chemistry (35)
- Biology: Living Things (40) + Life Science (40)
- Earth & Space: Earth & Weather (37) + Earth Science (35)
- Health: My Body (30) + Health Foundations (30)
- Engineering: Design & Build (30) + Engineering Principles (30)
- Formal Sciences: Patterns & Logic (25) + Reasoning & Proof (25)

## Shared Parser (Apr 5, 2026)
- **`tools/parse_topic.py`** — canonical topic file parsing module. 4 functions: `parse_topic()`, `parse_frontmatter()`, `parse_sections()`, `extract_questions()`.
- All 8 CI-pipeline tools refactored to use it (validate, generate_topic_pages, generate_assessment, generate_assessment_questions, generate_domain_questions, visualize_domain_map, visualize_hierarchy, visualize_radial). Net -3 lines.
- Imports work from repo root because Python adds the script's directory (`tools/`) to `sys.path[0]`.
- Commit `38b8f6423`, pushed to master. CI deployment in progress.

## Phase 12A Shipped (Apr 12, 2026)

All 9 plan steps across 4 cuts. Key implementation notes that future cuts / 12B/12C should not re-derive:

- **`showFluency` toggle retained** as pure-map escape hatch (Griffin's explicit call). Alpha gradient + frontier bonus run only when fluency is on. Cold-start floor is applied on top of `propagate()`'s output inside `refreshFluency()`, not contaminating the Bayesian evidence store.
- **Symmetric stage decay** (`max(0, 1 − 0.4 × |s − u|)`) shipped per plan — produces a "band of visibility" that sweeps up with the slider. Asymmetric variant (full credit for prior stages) parked as a live usability question; revisit when real usage tells us which feels right.
- **`getEffectiveScore` split**: floor is display-only. `getScore` / Bayesian updates / propagation unchanged. A "don't know this" click calls `setScore(id, 0)`; the floor will re-raise it if the declared stage implies it should be known, which is correct for display semantics.
- **Deep-dive flow kept intact** as opt-in second entry from the quiz welcome chooser. Griffin wanted extensive single-domain testing preserved. Only warmup + exploration deleted. Welcome screen is a 2-option chooser: "Quick test (24Q seed)" vs "Deep dive".
- **Seed question-bank bug found + fixed at runtime**: MC options in `assessment-questions.json` have ~95% B+C position bias (audited: B=64%, C=30% across both warmup and exploration pools; literature/economics/engineering/formal-sciences/physics are at 100% B+C). `renderQuestionCard` now shuffles MC options per render and re-indexes `q.answer`. One-time data fix is a separate follow-up, not shipped in 12A.
- **Topic dedup in `buildSeedQueue`**: each topic contributes at most one question to a seed (first encountered). Fixed the "two Boltzmann questions in five" bug Griffin hit in testing.
- **Retention card scoring**: `prereq_avg × log(1 + out_degree) × goal_proximity_bonus`. Out-degree is successor count (how many topics depend on this one = centrality). Goal proximity bonus is 2.0 if topic is on any starred goal's learning path, else 1.0.
- **Refine-your-map slider writes to `okg-domain-prior`**, not `okg-adjustments` (plan was imprecise — adjustments are course-level, domain prior is the cold-start multiplier from Cut 1). 5 positions map to multipliers {0.2, 0.6, 1.0, 1.4, 1.8}.
- **`preset=sprout` URL param** is live as a stub: forces `setUserStage(0)` and clears the dismiss flag. Sprout shell itself (TTS, emoji buttons, parent PIN) is Phase 12B.
- **Seed completion flag** `okg-seed-completed=1` set inside `renderResults()` only if user answered ≥1 question. Gates the retention corner card on the radial alongside "has ≥1 starred goal".

## Phase 12A Follow-ups (not blocking 12B)

- **MC position-bias data fix**: rewrite `assessment-questions.json` with pre-shuffled options so the bias is gone at source. Runtime shuffle in `renderQuestionCard` is the load-bearing shield for now.
- **Course-level picker inside Deep Dive**: currently domain-only; Griffin mentioned wanting "domain/course" granularity.
- **Stage-inversion edge spot-check**: 2,325 edges have prereq staged more advanced than successor. The alpha gradient formula produces locally-inverted signals at those pairs. Low priority unless a visual glitch surfaces.
- **Asymmetric stage decay vs symmetric**: user-experience question, parked until real use.
- **Lightweight seed adaptivity**: rolling-window nudge after N questions if >75% or <25% correct. Deferred to Phase 12C per Griffin's call.

## Phase 12 Dialectic Rulings (Apr 11, 2026)

Non-default decisions from the 3-round multi-agent dialectic (Psychometrics / Math Academy / UX / Skeptic → Opus referee). Record so future sessions don't re-derive:

- **Graph-as-product wins over lesson-feed-as-product.** 3-of-4 lens convergence + Griffin's explicit virality framing. OKG's wedge over Math Academy is breadth + self-direction, not sequenced mastery. Rejection of lesson-feed applies to Personas B/C only — Sprout (12B) is a partial lesson-feed concession for Persona A, and that's OK as long as the conceptual boundary stays clean.
- **No new per-topic attributes.** Rejected: `general_knowledge_tier`, `lesson_minutes`, `diagnostic_value`. Rationale: 15,290 topics × new attributes = rot liabilities when topics get renamed/merged/restaged. Alternative: 19-row domain-level slider UI fed into cold-start prior. Cost 0 annotations.
- **Per-edge `strength` (hard/soft) is the ONE new annotation** that survived scrutiny. Per-edge (20-40K edges), not per-topic. Generated via one-time Haiku labeling pass with 200-edge sample QA first. Fixes the "all prereqs treated equally" data-quality bug masquerading as a model bug.
- **Pedagogy-typing at domain level** (`assessable` vs `reflective`) — referee called it the best idea in the dialectic not in the original brief. Reflective domains (literature, philosophy, art history, most of history, music appreciation) get mark-as-read + optional text field, NOT quizzes. Fixes "90% mastery on The Sublime in Wordsworth" absurdity. ~20 min of Griffin classification time on 19 `_domain.yml` files.
- **24Q seed is opt-in, not gated.** Virality preserves over calibration precision. First-time visitors see the radial immediately, then a dismissable stage slider card. Deeper calibration (19-row slider, 24Q seed) lives behind buttons for engaged users.
- **FSRS rejected as retention mechanism.** Replaced by stale-topics query (>3 weeks since touch AND fluency ∈ [50,85]). Pure localStorage timestamp query, no scheduling engine. If long-term retention becomes the bottleneck, revisit — but not as Phase 12.
- **Rasch model is Phase 12C conditional only.** Stage heuristic (`domain_prior × stage_decay`) does the work in 12A. Rasch with θ∈ℝ^8 only if stage heuristic proves off by >1 stage in >20% of sampled users.
- **One component tree with conditional Sprout branch**, NOT three shell codebases. Three persona "presets" are thin preset bundles parameterizing one render path. Sprout is one `if (preset === 'sprout') return <SproutCard/>` conditional.

## Decisions
- **Format**: Markdown + YAML frontmatter (one file per topic)
- **License**: CC BY-SA 4.0 for content, MIT for tools
- **GitHub Pages**: Preferred deployment; generated HTML stays out of git
- **Status**: All topics now `validated` as of Mar 23
- **Domain ordering**: Math → Formal Sciences → Philosophy → CS → Engineering → Physics → Earth & Space → Chemistry → Biology → Health → Psychology → Social Sciences → Economics → Practical Life → History → Language → Literature → Arts → Music
- **Validation approach**: Haiku for volume, Sonnet for review, Opus for decisions
- **Stage audit principle**: stage based on actual file content, not whether simpler version exists for younger learners
- **localStorage keys**: `okg-fluency`, `okg-fluency-conf`, `okg-fluency-meta`, `okg-goals`, `okg-adjustments`

## Stage Audit (Apr 1, 2026)
- **835 topics restaged**: 784 auto-promoted (hard-prereq cascade, 7 iterations), 30 content-reviewed (13 Sonnet agents), 6 high-fan-out over-staged topics fixed + 15 downstream cascade.
- **Auto-promote tool**: `tools/auto_promote_stages.py` — iteratively promotes topics below their hard prereqs. Run with `--apply`.
- **Course-stage audit**: Integrated into `validate.py` (full mode). Warns on courses staged below median cross-course prereq.
- **Standalone audit**: `tools/audit_course_stages.py` — finds misstaged courses with `--fix` option.

## Domain Map Architecture (Mar 24, 2026)
- **Tier layout**: Courses grouped by developmental stage → tiers. Within-tier overlap ~50%, between-tier ~25%.
- **Branch X-positions**: Manual left-right axis per domain (e.g., math: discrete←→analysis). Stored in `COURSE_BRANCH_X` dict. Non-math mappings are AI-proposed, need human review.
- **Sizing**: `area ∝ degree`, out-degree weighted 2x. DEGREE_CEILING=25 for consistent sizing across views.
- **Row splitting**: 3x depth multiplier, recursive splitting (3 passes, cap 20 topics/row).
- **Centroid-anchored placement**: Each layer anchors on connected-neighbor centroid, then 10 rounds of 40% neighbor drift.
- **Cross-course depth floor** (Apr 1): `compute_course_depths` uses domain-wide depth as floor for within-course depth, SCALED to the course's own depth range. Prevents height inflation while fixing cross-course prereq ordering.
- **Radial integration DONE** (Mar 25): `visualize_radial.py` imports `COURSE_BRANCH_X` from domain map. Auto-detects `BRANCH_FLIP` per domain using cross-domain edge lengths within 3-domain angular window. Plan doc: `tools/radial-branch-alignment.md`.
- **Leaf connector tool**: `tools/connect_leaves.py` — tag/title overlap scoring, cycle-safe apply, duplicate detection. Used for 5 domains so far.
- **Dedup tool**: `tools/dedup_pairs.py` — delete weaker file + redirect references. Caveat: broad text replacement can corrupt IDs/tags if delete_id is substring of keep_id (fixed in code but verify after runs).

## Cross-Domain Stage Calibration (Mar 29, 2026) — DONE

**1,446 topics restaged** across 17 domains via 14-agent evaluation swarm. Validation passed (0 errors, 0 new cycles).

**Root cause was blanket course-level staging**: topics inherited course stage from `_domain.yml` without individual evaluation. At least 9 courses had 100% of topics at one stage.

**Key changes:**
- Chemistry: 0→21 expert (DFT, post-HF, 2D NMR, computational chem)
- Computer Science: 0→52 expert (transformers, BFT, polynomial hierarchy, dependent types)
- Mathematics: 59→113 expert (Galois theory, p-adics, martingales, spectral graph theory + 83 formal-systems→advanced)
- Physics: 190→215 expert (scattering theory, path integrals, relativistic QM)
- Health: 273→42 expert (was massively inflated; 215→advanced, 16→formal-systems)
- Engineering: 194→58 expert (128→advanced, 8→formal-systems)
- Psychology: 220→98 expert (clinical disorder overviews demoted)
- Literature: 146→46 expert, History: 93→23 expert
- Social Sciences: 174 topics promoted from formal-systems/abstract-reasoning to advanced
- Grand totals: 2,951 advanced (+1,210), 1,268 expert (-1,094)

**_domain.yml**: Only math/measure-theory-and-functional-analysis changed (advanced→expert). Automated reconciliation of other _domain.yml files was reverted — minimum-stage logic was wrong for mixed-stage courses. _domain.yml course stages may need manual review in a future session.

**Remaining work (deferred):**
- Step 3: Generate missing expert topics (~60 topic areas identified across all domains). Major gaps: inorganic chemistry (entirely absent), quantum computing, cryptography, ML theory, algebraic topology, differential geometry, general relativity, QFT.
- _domain.yml course-stage reconciliation needs a smarter approach (modal stage, not minimum)
- Philosophy-of-science has ~10-12 duplicate topic pairs (separate from staging)

## Gotchas
- **Python f-string + JS templates**: `\'` inside f-string produces `'` not `\'`. Use `"'" +` concatenation instead.
- **Inline JSON size limit**: Browsers choke on 700KB+ single-line `<script>` data. Use `indent=1` for multi-line or external `.js` file.
- **Click-vs-drag in canvas views**: If two `mousemove` handlers share `dragStartX/Y`, track original position separately (`mouseDownX/Y`) for displacement detection.
- **Dedup agents introduce cycles**: Batch find-and-replace during dedup can create mutual prerequisite references. Always run cycle detection after dedup swarms. Also: broad text replace can corrupt IDs when delete_id is substring of keep_id (e.g., `prose-poetry` → `prose-poetry-hybrid-form` corrupted the keep file's own ID).
- **Dangling cross-domain refs**: 394 total across all domains (pre-existing, not from dedup). Mostly course names used as prereq IDs (`probability-and-statistics`, `macroeconomics`) instead of actual topic IDs. Doesn't affect domain maps (within-domain only).
- **Validation (Mar 26)**: 13,153 topics, 0 self-refs, 0 within-domain cycles. Graph is structurally clean after math dedup (91) + non-math dedup (149) = 240 pairs merged.
- **Dedup self-ref pattern**: When keep_file has builds-toward pointing to delete_id, the redirect creates a self-ref. The dedup script skips delete_file but not keep_file. Always run self-ref cleanup after dedup.
- **Dedup cycle pattern**: Soft prereqs added by `connect_leaves.py` can point backwards pedagogically. When dedup merges nodes, these create cycles. Fix: remove the backwards soft prereq.
- **T/F mechanical rewrite caveat**: Regex-based `always→typically` etc. can make false statements arguably true. Spot-check needed, especially `only→primarily`, `entirely→mostly`, `cannot→can rarely`. Also: "every"→"most" breaks plural agreement ("most day" instead of "most days") — fixed 23 instances via `tools/fix_grammar_rewrites.py`. Future batch rewrites should include grammar validation.
- **Canvas mouse/touch handler divergence**: When adding touch support, every mouse handler needs a touch equivalent. The radial touchend was missing domain label navigation that mouseup had. Consider refactoring to shared interaction functions.
- **Radial semantic zoom**: Course labels computed dynamically from visible nodes only — precomputed centroids break when courses span large radial distances (centroid is in the middle, zooming into one end loses the label). Must use viewport-filtered approach.
- **Radial viewport bounds**: Must divide by `camScale * viewScale`, not just `camScale`. viewScale = `Math.min(W,H) / 1200`.
- **Git worktrees**: Work well for parallel OKG development. Branches touched different file sets (tools/ vs domains/) so merges were clean. Remove worktrees before deleting branches. Kill HTTP servers before removing worktree directories.
- **Killing bash scripts doesn't kill `claude --print` children**: The orchestrator spawns `claude --print` as a subprocess. Killing the parent bash script (via `taskkill`) leaves the claude process running. This caused double-generation when a sequential batch was "killed" but its child completed. Use process groups or kill the claude PID directly.
- **Haiku MC option format bug**: Haiku agents frequently write MC options as `{0: "text"}` dicts instead of plain strings in YAML. Run a validation pass after any Haiku Q+E generation to catch these before pushing.
- **Haiku context limits for Q+E**: Haiku agents hit context limits at ~30-40 file edits and either stop or write placeholder content. Split courses into ≤30-file batches for Q+E agents.
- **Quiz state machine lives in `generate_quiz_page.py`, not `fluency.js`**: The 3-phase warmup/exploration/deep-dive orchestrator is embedded JS inside the Python generator (~250 lines). When reasoning about fluency engine LoC, don't conflate — `fluency.js` holds the Bayesian/propagation core, the Python generator holds the quiz orchestration.
- **Stage inversion edges interact with any stage-distance rendering**: 2,325 edges (~8%) have prereq staged more advanced than successor. Any new render logic using `stage_distance` (e.g., Phase 12 opacity field) will produce inverted local signals around those pairs. Spot-check on known-bad edges before shipping. Inversion list is derivable from `stats.py` output.
