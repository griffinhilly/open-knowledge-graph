# Phase 12 Implementation Notes (Apr 12, 2026)

Purpose: full implementation detail, LoC ledgers, and reviewer findings for Phase 12A and Phase 12B Cuts 5-7. Moved out of MEMORY.md (Jun 12, 2026 prune) — read this before resuming any Phase 12 / fluency-engine / Sprout work so decisions aren't re-derived. The two live tripwires (asymmetric-decay fix for Persona C; bulk-labeling QA protocol) are ALSO summarized in MEMORY.md.

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

## Phase 12B Cuts 5-6 Shipped (Apr 12, 2026)

**Cut 5 — pedagogy-typing + reflective cards + stale-topics** (plan steps 5, 6, 7, 11):

- **`pedagogy_type` field** added to all 19 `_domain.yml` files. Classification: **assessable (13)** = math, formal-sciences, CS, engineering, physics, chemistry, biology, earth-and-space, economics, health, psychology, language-and-communication, practical-life-skills. **reflective (6)** = philosophy, social-sciences, history, literature, arts-and-aesthetics, music. Music is a judgment call (theory is assessable, appreciation is reflective — went with domain-level reflective to match plan intent).
- **Reflective topic pages** swap the "Practice Questions" CTA for a "Mark as read" card with an optional "What did you take from this?" textarea. Text persists to new `okg-reflections` localStorage. `markAsRead()` sets score to 100. Quiz-me-anyway escape hatch preserved when questions exist. Assessable topic pages are unchanged.
- **Reflective-domain frontier variant**: `findFrontier` now branches on `pedagogyType`. Reflective topics bypass the prereq check entirely — any untouched reflective topic becomes frontier-eligible with a flat readiness of 80 (below assessable root topics' 100 so assessables still win ties). Before Cut 5, reflective topics were categorically excluded from frontier because of the prereq gate; 4070 reflective topics now appear.
- **Stale-topics frontier signal**: new `okg-fluency-touched` localStorage key tracks per-topic last-touched timestamps. `setScore` and `updateTopic` write timestamps automatically. `findStaleTopics()` returns topics with stored score in `[50, 85]` and `last_touched > 21 days` ago, sorted oldest-first. Radial retention card surfaces stale topics **before** fresh frontier candidates, relabeling "Your next step" → "Review this" and the button "Start this" → "Review".

**Cut 6 — per-edge strength propagation** (plan steps 8, 9, 10):

- **Soft-edge propagation in `fluency.js`**: `BACKWARD_DECAY_HARD=0.85`, `BACKWARD_DECAY_SOFT=0.425`. Backward BFS now tracks per-path decay (a hard-then-soft path multiplies correctly to 0.85 × 0.425 = 0.361, not 0.85² = 0.7225). Forward capping considers HARD prereqs only. `findFrontier` and `isFrontier` compute `avgPrereq` over hard prereqs only — a topic with strong hard prereqs and weak soft prereqs is frontier-eligible (was previously excluded).
- **`prereqId(p)` / `prereqType(p)` helpers** normalize either shape (string or `{id, type}`) so propagate/findFrontier/computePathToGoal/topoSort all work against mixed-shape input. Backward-compat with legacy string-only graphs.
- **Graph shape changed in two places**: `buildFluencyGraph` in `visualize_radial.py` now emits `{id, type}` objects for prereqs/successors. `_build_lightweight_graph` in `generate_quiz_page.py` was rewritten to include soft edges (was filtering them out); same `{id, type}` shape. The quiz's results-screen frontier renderer was updated to match the hard-only avgPrereq semantics.
- **Edge distribution finding** (run during Cut 6 recon): the corpus is already **54% hard / 46% soft** (20,086 hard, 17,159 soft of 37,245 total). NOT the "all-hard" starting state the plan assumed. Soft-edge weighting shipped immediately has real teeth without the Haiku relabeling pass.
- **`tools/label_edge_strength.py`** script written but NOT run. Supports `--sample N`, `--resume`, `--apply`. Docstring includes QA protocol.
- **Sample QA outcome**: 200 topics / 542 edges classified via 4 parallel Haiku research-agents (plan usage, not API budget). **Flip rate 0.7% (4 of 542)** — vastly below the 10% re-run threshold. All 4 flips were `soft → hard`, zero `hard → soft`. Conclusion: the existing manual labels from Phases 6-8 are already high-quality; full relabeling pass was skipped. The 4 surgical flips were applied in the Apr 12 reconciliation commit. Sample data archived in `data/edge-sample-manifest.json` + `data/edge-strength-labels.json`.

**Net LoC (Cuts 5+6 combined)**: ~+370 insertions, −65 deletions across 23 files. File breakdown: lib/fluency.js +127 total (67 cut 5 + 60 cut 6 net), generate_topic_pages.py +144, generate_quiz_page.py ~30 touched, visualize_radial.py ~45 touched, label_edge_strength.py +260 new, 19 domain YAMLs +1 each.

## Phase 12B Cut 7 Shipped (Apr 12, 2026)

Conditional SproutCard shell for Persona A inside `tools/visualize_radial.py`. Commit `d65f8551e`, pushed.

**Dialectic referee rulings** (tradeoff mode, 2A-2C-1R, 6 sub-decisions) — the bundle broke and three defaults flipped:

- **Trigger: AND, not OR.** `preset=sprout AND (no prior fluency OR stage===0)`. OR was semantically confused because the `preset=sprout` stub already calls `setUserStage(0)`, so the OR arm only catches accidentally-stage-0 users — including Griffin-as-Persona-C testing the symmetric-decay bug. AND closes the ambush hole. `initStageSlider`'s old 4-line stub was deleted; detection now lives at the top of the script block.
- **Coloring-book REPLACES the radial in Sprout mode, not a sidebar.** The radial canvas is not rendered at all when `renderSproutShell()` fires. Containment fix for the 4,070 reflective topics Cuts 5–6 added — a sidebar with the radial underneath would let a curious 6-year-old tap into Wordsworth. Bonus: skipping radial render buys back LoC budget.
- **Shared `preset=sprout` URLs render Sprout shell + "See the full map" CTA**, not a straight graph-for-strangers. Honest about what the kid sees, preserves virality via the prominent escape hatch. ~10 LoC middle path.

**Confirmed defaults (not flipped)**:
- Conditional branch inside `visualize_radial.py`, honoring the Phase 12 "one component tree" non-negotiable (not a separate `sprout.html`)
- Emoji-first with `HERO_IMAGE_RETROFIT` TODO at the render site; retrofit gated on first real Persona A tester
- Parent PIN opt-in only (not required on entry or exit); SHA-256 via SubtleCrypto, session-bypass flag after correct verify
- Guardrail honored: `renderSproutShell()` does not touch `draw()`, `showPanel()`, `buildFluencyGraph()`, or the retention card stack

**Key implementation notes**:
- New `SPROUT_DOMAIN_EMOJI` + `load_sprout_topics()` helper in Python reads 322 pre-formal topics across 9 domains (arts, biology, earth-space, health, language, literature, math, music, psychology) and injects `sproutTopics` into the graph_json. Core Idea text trimmed to ~280 chars per topic.
- `detectSproutMode()` runs immediately after `const data = {graph_json};` so the trigger fires before any UI init. Adult-mode surfaces (canvas, stats, nav, controls, search, tooltip, panel, stageCard, refineCard, nextStepCard) are `display: none`'d in Sprout mode.
- 9-wedge coloring-book SVG uses domain hue + mastery fill fraction. One background wedge always rendered, fill wedge only when ≥1 topic in the domain has score ≥70.
- Response buttons map: know=90, kinda=60, dunno=20 → `OKGFluency.setScore(topic.id, score)` → rerender next topic.

**LoC accounting**: +469 insertions, −13 deletions = net +456 in initial pass. Trimmed by 4 low-value features to hit referee's strict 430 budget: all-done placeholder (−8), same-topic avoidance (−3), TTS-mute persistence (−5), PIN success toast (−5), merged two domain metadata maps into one (−6). Final: **+440 / −13 = net +427**, under 430.

**Browser verification via claude-in-chrome**: Sprout renders at stage 0 with real pre-formal topics, 9 wedges + 9 labels in the coloring-book SVG, response buttons persist scores, PIN set and verify work via SubtleCrypto, non-Sprout URL still renders the unmodified 14,816-node radial, mobile layout clean at 567px viewport, zero console errors.

**Deferred eval acknowledged**: Phase 12B success criterion "a real child uses Sprout without adult interpretation" is not evaluable this phase — Addi is 2.5, no Persona A testers exist. Shipping emoji-only is buying speed with unvalidated child-UX quality. The reviewer called this out explicitly; don't let "we shipped emoji in Cut 7" become institutional justification for never retrofitting.

**Meta-irony to remember (session reviewer flagged this)**: Cut 7 itself went through this session without `/plan-task` or `/implement` — it was ad-hoc implementation driven by conversation-level planning. If Cut 7 had been routed through the skill system, the new scope-gate added to `/plan-task` (see workflow-config commit `fa9fb65` and `feedback_scope_gate_deterministic.md`) would have fired on it. The gate works against *other agents* but not against the orchestrator operating in inline-execution mode. This is the same failure pattern 12A's dialectic gate had, one layer down. Flagged as the dominant residual failure mode. **Update Jun 12, 2026: the deterministic fix (pre-push dialectic-trailer hook) is now BUILT — see hooks/pre-push.**

## Phase 12A Reviewer Findings (Apr 12, 2026)

A fresh-context session reviewer caught material issues that were glossed over during execution. Recording here so future sessions don't re-derive them or inherit the misleading framing.

- **Step 3 is additive, not a replace.** PLAN.md marks it with `[~]` and explains. The radial still carries 10 `if (showFluency)` branches and the `showFluency = false` default. The plan specified a single render path with net −60 LoC; actual delivery is additive. Future sessions reading "step 3 shipped" should understand they are building on top of a dual-mode render path, not a single-mode one.
- **Step 8 delete was partial.** Deep-dive flow retained. Plan credited −250 against the budget; real delete is ~−200. PLAN.md updated accordingly. This decision is probably right — the reviewer noted that deep-dive retention is likely the correct call in isolation, the problem is it shipped as a silent plan divergence without a tradeoff-gate question.
- **+267 LoC overshoot root cause**: ~+140 LoC is from the two undelivered deletes above, not CSS bloat. The original "refine+next-step card DOM overhead" framing was misleading — if a future session tries to trim the overshoot by simplifying card CSS, they'll be solving the wrong problem. The real knob is step 3's showFluency branches.
- **Symmetric stage decay warning for Persona C**: `max(0, 1 − 0.4 × |s − u|)` with 6 stages means a grad student at stage 5 gets `floor(pre-formal) = 0` — zero credit for kindergarten content they obviously know. Persona C (fuzzy-recall college grad) is the exact persona this breaks. This shipped with known semantics per plan. **If Griffin as Persona C tests the stage slider and complains that his kindergarten math is dim, the fix is to switch to asymmetric decay** (`max(0, 1 − 0.4 × max(0, topic_stage − user_stage))`), not to debug the fluency engine. Don't lose this diagnosis in a downstream bug hunt.
- **Haiku 0.7% sample flip rate was not trusted; action was taken anyway**: The reviewer noted that 4 of 4 disagreements in the same direction (soft → hard) is a bias signature. A genuine high-agreement result should have disagreements roughly proportional to label prevalence (54/46). **No shared-bias check was run on the agreements** — we looked at where Haiku disagreed, not where Haiku reinforced existing labels that might themselves be wrong. The "full labeling pass skipped" decision was made on incomplete evidence.
- **Improved QA protocol for future labeling passes** (reviewer recommendation):
  1. Eyeball the disagreements (already standard, keep)
  2. **Eyeball 20 random *agreements*** with a separate fresh agent to detect shared bias
  3. **Inter-agent reliability**: re-run the same 50 edges through a different Haiku agent and measure agent-to-agent agreement. If agents agree <90% with each other, their agreement with existing labels is meaningless as a quality signal.
  4. Under a null of random error, flips should be roughly 46% hard→soft / 54% soft→hard. 4/0 is p ≈ 0.08 at N=4 — weak but not dismissible.
- **Dialectic-review gate failed twice. Diagnosis: execution-layer problem, not forgetfulness.** Structural causes: (a) always-loaded context ≠ always-executed; (b) no discrete "cut just closed" event fires a gate check; (c) cost friction is one-directional. **Fix** (reviewer rec): promote from behavioral → deterministic via a pre-push hook requiring a `dialectic-reviewed:` or `dialectic-skipped:<reason>` trailer. **Built Jun 12, 2026 — see hooks/pre-push.**

## 6-Stage Schema referee case decisions (Mar 22, 2026)

- CS programming fundamentals: kept at abstract-reasoning (programming taught to middle schoolers)
- Computability & complexity: split 47/51 (standard ToC → formal-systems, advanced complexity stays)
- Physics QM: Griffiths ch1-3 stays formal-systems, Bell's theorem → advanced
