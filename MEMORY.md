# Open Knowledge Graph Memory

## Status (Apr 4, 2026)
- **15,304 topics** across **19 domains**, **261 courses** (16 literature courses)
- **6 developmental stages**: pre-formal, concrete-operations, abstract-reasoning, formal-systems, advanced, expert
- **Radial graph shows 18 domains** (practical-life-skills excluded — kept on index/domain maps)
- GitHub Pages: `griffinhilly.github.io/open-knowledge-graph/`
- Phase 10 DONE. Phase 10.5 (Literature Expansion) DONE. Phase 11 (Early-Childhood) DONE.
- **Domain maps are primary navigation** — hierarchy views removed from CI and all links
- **CI pipeline**: validate → index → radial → topic pages → domain maps → assessment → quiz
- **Pre-push hook**: `hooks/pre-push` — cycle detection + CI script tracking + quiz staleness warning + question YAML error checks (~17s). Setup: `git config core.hooksPath hooks`
- **Literature expansion (Apr 3)**: 6 → 14 courses, 483 → 1,067 topics. 8 new courses: Stories & Narrative, Mythology/Folklore, Literary Movements, Genre Fiction, Creative Nonfiction, World Literature, Children's/YA, Digital & Experimental. All with Q+E.
- **Quiz balancing**: `generate_assessment_questions.py` round-robins across courses within each stage tier.
- **Validation hardened**: question YAML errors (invalid YAML, non-string options) promoted from warnings to errors. Quick mode now checks them.
- **Early-Childhood expansion (Apr 4)**: +358 topics, 12 new courses across 7 domains. Music (3 courses: Musical Play & Listening, Rhythm & Song, Listening & Musical Elements), Literature (2: First Stories & Read-Alouds, Reading & Understanding Stories), Psychology (3: Feelings & Self-Awareness, Understanding Self & Others, Growing Up & Getting Along), History (Then & Now), Philosophy (Wondering & Thinking), Social Sciences (My Community & World), Arts (Creative Play & Expression). All with Q+E.
- **14 near-duplicate pairs** in literature courses — need dedup pass.
- **~7 topics with stripped Questions sections** across other domains (broken YAML, need regeneration).
- **Cross-domain prereq audit pending** for Phase 11 courses — currently self-contained, no links to existing domain content.

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
