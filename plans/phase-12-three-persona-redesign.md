# Phase 12: Three-Persona Redesign — Virality-First Learning Platform

*Designed via 3-round multi-agent dialectic (Apr 11, 2026). See MEMORY.md for rationale.*

## Goals

Serve three user personas with one engine, while preserving the graph's viral first-impression pull and adding the retention hooks that turn curious visitors into avid users.

- **Persona A** — young child (5-8), parent-guided. Starts from scratch, shouldn't see collegiate+ graph. Wants 1-2 topics per early-childhood domain. Progression fills inner circle as they learn.
- **Persona B** — high school student (14-18). Learning via coursework, wants to excel and filter college subjects. Inner circles mostly assumed-filled via coursework-induced fluency.
- **Persona C** — college graduate with fuzzy coursework recall + broad osmotic knowledge. Pre-collegiate topics assumed known without explicit demonstration. Efficient path to frontier — no 200-question warmup.

## Guiding principles

1. **Graph first, friction last.** The radial is the hook; personalization is opt-in and progressive.
2. **Straddle virality + utility.** Cool graph pulls people in; learning plans keep them.
3. **Aim net-subtractive where possible.** Phase 12A should ideally leave `js/fluency.js` shorter than it started — useful gut-check for whether complexity is accreting. Ambition, not a gate; don't cut features that earn their weight just to hit a LoC target.
4. **No new per-topic annotations.** One new per-edge annotation (`strength`) is the only data-layer addition.
5. **Pedagogy-typing at domain level.** Reflective domains (literature, philosophy, art history, most of history, music appreciation) don't get quizzed — they get marked-as-read.

## Non-goals (explicitly rejected)

- Lesson-feed-as-primary-home-surface (Math Academy model)
- FSRS spaced-repetition engine
- IRT 2PL model
- New per-topic `general_knowledge_tier` attribute
- Hand-tagging ~1,500 "load-bearing" topics
- Demographic onboarding questions (age × education × tier)
- Persona-router page as first-visit experience
- Three separate URL roots / three separate codebases

---

## Phase 12A: Virality-First Onboarding — weekend (2-3 days)

**Goal:** Every claim in the three-persona brief becomes testable in the live product, without adding a friction wall for first-time visitors.

**Principle:** Aim for net LoC ≤ 0 as a sanity check. Meaningfully net-positive without strong justification is a signal to re-examine what's being added.

### Steps

1. **Cold-start prior formula in `js/fluency.js`**
   - Add `floor(topic, user) = domain_prior[topic.domain] × stage_decay(topic.stage, user_stage)`
   - `stage_decay(s, u) = max(0, 1 - 0.4 × |s - u|)`
   - `domain_prior` defaults uniform; updated by the 19-row slider when user engages with it
   - Wires as the prior; existing Bayesian updates run on top
   - **LoC:** +40 / −60 / **net −20**

2. **Stage slider as dismissable card over the radial**
   - Card floats over the graph on first visit: *"Make this yours. Where are you?"*
   - Single slider labeled: early child / late child / middle school / high school / college / graduate
   - One-tap commitment; opacity field updates live; inner circle fills visibly
   - Dismiss X to skip entirely; setting persists to `localStorage`
   - **LoC:** +80 / 0 / **+80**

3. **Opacity field on radial (replaces dual color modes)**
   - Single render path: `opacity = f(stage_distance, fluency, frontier_score)`
   - Replaces the dual color-mode code and current stage-band rendering
   - Parameterized so Sprout preset (Phase 12B) can reuse it with a tighter threshold
   - **LoC:** +90 / −150 / **net −60**

4. **"Your next step" corner card (retention hook)**
   - Uses existing goal-starring + BFS+topo-sort path engine (already shipped in Phase 9D)
   - Persistent small card bottom-right, **appears only after** (a) user completed the opt-in 24Q seed, OR (b) user has ≥1 starred goal. Single quiz answer is NOT enough — we want the card to feel like guidance, not clutter, and that requires the user to have signaled intent first.
   - Surfaces top frontier topic scored by `prereq_avg_fluency × log(1 + in_degree) × goal_proximity_bonus`
   - One-tap "Start this" opens the topic page
   - Dismissable (local per-session); reappears next visit
   - **LoC:** +180-220 (reviewer-corrected — includes CSS, metadata index, show/hide logic)

5. **Inline "I don't actually know this" button on topic cards**
   - One button per topic card; writes correction to existing `okg-adjustments` localStorage
   - No new infrastructure — reuses the adjustment mechanism already built
   - **LoC:** +25 / 0 / **+25**

6. **19-row domain slider as "Refine your map" button (opt-in)**
   - Accessible from a button next to the stage slider (not auto-shown as a modal)
   - 19 rows, 5-position sliders, writes to `okg-adjustments` keyed by domain
   - Labeled "For precision: tell us what you already know"
   - Collapsed/hidden by default
   - **LoC:** +180 / 0 / **+180**

7. **24Q stratified seed demoted to opt-in "Test yourself?" button**
   - The existing seed logic survives but is no longer the onboarding default
   - Button on the same row as stage slider and "Refine your map"
   - Stratification: 19 domains × target(stage) with ±1 variance, sampled by domain weight from stage slider
   - Stopping rule: 24 questions OR per-domain posterior confidence ≥ threshold (reuses existing log-odds infrastructure)
   - **LoC:** +120 / 0 / **+120** (delete happens in step 8, in a different file)

8. **Delete 3-phase warmup/exploration/deep-dive scaffolding**
   - Single-phase seed replaces it; remove the warmup→exploration→deep-dive state machine
   - **File location:** the state machine is JS embedded in `tools/generate_quiz_page.py` (the Python generator), not in `js/fluency.js`. Net-subtractive credit here applies to `generate_quiz_page.py`, not to the fluency engine.
   - Retain the question bank itself (still used by the opt-in seed)
   - **LoC (`generate_quiz_page.py`):** −250

9. **Index page cleanup**
   - Current hero CTAs and "Personalize Your Map" quiz link point to the new onboarding surface
   - "Setting up for a child?" link → routes to `preset=sprout` (preset doesn't exist yet in 12A; link is a stub that lands on the same page with a stage=0 slider position)
   - **LoC:** +60 / −80 / **net −20**

### Phase 12A totals

**Net LoC across both files**: approximately −50 to +150 depending on how "Refine your map" and the retention hook come in. The big delete (−250) hits `generate_quiz_page.py`; most adds hit `js/fluency.js` + new UI files. `fluency.js` alone is likely modestly positive (maybe +100 to +200); the cross-file picture is closer to neutral. Watch the number; don't worship it.

### Phase 12A success criteria

- First-time visitor lands on the radial within 1 second; no gating screen
- Stage-slider tap → visible graph update within 100ms (opacity field recomputes client-side)
- Self (Griffin) can onboard from index to "this graph reflects my actual state" in ≤ 5 minutes
- **Mobile**: stage slider card and corner retention card are both tappable on a phone without overlapping critical touch targets (radial pan/zoom, node tap). Reuses existing touch infrastructure from Phase 8's mobile touch fix. Cross-check CLAUDE.md's `Canvas mouse/touch handler divergence` gotcha before shipping — any new interactive element must have matching mouse + touch handlers.
- `js/fluency.js` line count roughly flat to modestly positive (~+100 to +200 is acceptable; the big delete is in `generate_quiz_page.py`)
- `okg-adjustments` localStorage key has non-zero writes in first week of self-use
- **Persona A gap**: Phase 12A does NOT deliver real Persona A value. A child lands on stage=0 and sees the radial with early-childhood topics highlighted — better than nothing, but the full Sprout experience (TTS, emoji buttons, coloring-book progress, parent PIN) is 12B. Do not claim Persona A success from 12A alone.

---

## Phase 12B: Sprout + Pedagogy-Typing + Per-Edge Strength — week (4-7 days)

**Goal:** Persona A gets a real shell; reflective domains stop forcing quizzes; propagation uses edge semantics.

**Dependencies:** Phase 12A must be live and stable.

### Steps

1. **Hero image audit (Griffin, ~20 min)**
   - Open 5-10 stage-0 and stage-1 topic pages in `output/`
   - Decide: images work / need sourcing pass / emoji-only is fine for Sprout
   - This gates the visual direction of step 2

2. **SproutCard conditional render branch**
   - Triggered when `preset=sprout` OR stage slider set to 0
   - Full-screen single topic; picture-first (hero image or emoji fallback per step 1)
   - TTS via Web Speech API for topic name + core idea
   - Three giant emoji response buttons: know it / kinda / don't know
   - Collegiate+ radial rings `display: none` (not just `opacity: 0`) for Sprout
   - **LoC:** +280 + ~40 CSS

3. **Parent PIN unlock for Sprout settings**
   - 4-digit PIN, localStorage-hashed (SubtleCrypto SHA-256)
   - Gates the stage slider and preset switch — prevents child from wandering into collegiate view
   - **LoC:** +60

4. **Coloring-book progress visualization for Sprout**
   - SVG inner-circle wedges (one per early-childhood domain) fill with color as topics marked known
   - Reuses existing domain color palette
   - **LoC:** +120

5. **Domain-level pedagogy typing**
   - Add `pedagogy_type ∈ {assessable, reflective}` to each of 19 `_domain.yml` files
   - Assessable: math, CS, physics, chem, bio, quant econ, geography-facts, grammar, music theory
   - Reflective: literature, philosophy, art history, most of history, music appreciation
   - ~20 min of Griffin's classification time
   - **LoC (engine):** +30

6. **Reflective card variant (replaces quiz CTA for reflective topics)**
   - Text field: "What did you take from this?" (optional, persists to localStorage)
   - "Mark as read" button → binary `touched=1` → fluency 100
   - Optional "Quiz me anyway" toggle falls through to existing quiz engine for users who want it
   - **LoC:** +110

7. **Reflective-domain frontier variant**
   - Frontier on reflective domains = `topics_touched / topics_in_subdomain` instead of `prereq_avg × mastery`
   - **LoC:** +40

8. **Per-edge `strength` labeling pass**
   - Script: `tools/label_edge_strength.py` — Haiku batch over all prereq edges (~20-40K)
   - Each edge classified as `hard` (must know first) or `soft` (helpful but not required)
   - Estimated cost: $5-15 via Haiku
   - **LoC (script):** +60

9. **Sample QA before full apply**
   - Eyeball a 200-edge random sample from the labeling output
   - If <10% error rate, apply the full labeling to edge data
   - If ≥10% error rate, revise the prompt and re-run on the sample

10. **Soft-edge propagation weighting**
    - Modify backward propagation in `js/fluency.js`: soft edges weighted at 0.5× hard weight (`0.425^hops` instead of `0.85^hops`)
    - **LoC:** +20

11. **Stale-topics frontier signal**
    - Query: topics last-touched > 3 weeks ago with fluency ∈ [50, 85]
    - Surface on Compass/Frontier "review these" ribbon
    - Pure localStorage timestamp query — **not** FSRS
    - **LoC:** +60

### Phase 12B totals

**Net LoC: approximately +800.** Honest weight added, mostly in SproutCard and reflective card variant.

### Phase 12B success criteria

- A real child (Addi at appropriate age, or a friend's kid) uses Sprout without adult interpretation of the UI
- Opening a literature topic in Compass no longer feels like "I'm being quizzed on Wordsworth"
- Per-edge strength reduces "this prereq shouldn't be required" complaints to near-zero on a 20-topic spot-check

---

## Phase 12C: Conditional Rasch Upgrade — 1-3 weeks (conditional)

**Goal:** Upgrade cold-start inference from stage heuristic to Rasch model **only if** Phase 12B data reveals systematic failures.

**Trigger condition:** The stage heuristic is off by >1 stage in >20% of sampled users in specific domains. Measurement is subjective (Griffin's own usage) unless Phase 12A adds lightweight telemetry.

### Steps (only if triggered)

1. **Rasch model with stage-derived difficulties**
   - `θ ∈ ℝ^8` (8 domain clusters, reduced from 19 via domain similarity)
   - Fixed discrimination `a_q ≡ 1`, `b_q = stage_index - 2.5`
   - **LoC:** +250

2. **Fisher-info adaptive within the 24Q seed**
   - Replaces stratified sampling with information-gain-driven question selection
   - Stopping: posterior SE < 0.4 logits OR 24Q cap
   - **LoC:** +50, −50 (replaces stratified sampler)

3. **Reflective-domain exclusion from Rasch**
   - Rasch runs only over assessable domains; reflective domains use binary-touched
   - **LoC:** +20

4. **Revisit load-bearing tagging (only if Fisher analysis demands)**
   - If specific topics consistently dominate info gain, hand-tag those ~50-200 specifically
   - **Not** the ~1,500 originally proposed

### Phase 12C success criteria

- Cold-start fluency predictions within 0.5 stage of demonstrated aptitude on sampled users
- Seed completion rate unchanged or improved (Fisher selection shouldn't feel harder)

---

## Deferred / Not doing

- FSRS spaced-repetition engine *(stale-topics heuristic replaces it)*
- Lesson-feed-as-primary-home-surface *(graph is the hook)*
- 2PL IRT *(Rasch only, and only conditionally)*
- `general_knowledge_tier` per-topic attribute *(19-row slider replaces it)*
- `lesson_minutes`, `diagnostic_value` per-topic attributes *(dropped in R2 dialectic)*
- Persona-router page *(index IS the router)*
- Demographic onboarding questions *(stage slider + domain slider replaces)*
- Confidence UI on topic cards *(out of scope)*
- Three separate URL roots / shell codebases *(one component tree, presets + conditional render)*

## Decisions pending

- **Hero image audit outcome** (Phase 12B step 1) — **DECIDED Apr 12, 2026: emoji-only works.** Griffin's adult read of sample pre-formal topic pages across the 9 domains concluded the text is readable as-is for parent-to-child narration and the per-domain emoji is sufficient visual anchor. No retrofit this cut. **Caveat**: this is an adult read, not a child test. `HERO_IMAGE_RETROFIT` TODO markers stay in `tools/visualize_radial.py`; revisit when the first real Persona A tester surfaces a gap. Do not let this decision harden into institutional justification for never retrofitting (the Cut 7 dialectic referee explicitly flagged this risk).
- **Per-edge labeling sample QA outcome** (Phase 12B step 9)
- **Phase 12C trigger assessment** (subjective vs telemetry-backed)

## Risks

- **Phase 12A net LoC drifts significantly positive** → gut-check signal; re-examine scope but don't auto-abort
- **SproutCard scope creep** → prototype with emoji-only first, images/TTS in 12B.5 if needed
- **19-row slider overwhelms users** → mitigate by defaulting all rows to seed-inferred values and showing 5 at a time with "show all"
- **Edge labeling quality <90%** → fall back to treating all edges as hard; accept status-quo propagation
- **Reflective-domain pushback** ("I wanted a quiz") → "Quiz me anyway" escape hatch on reflective cards
- **Mid-Phase-12A commit crisis** — if you decide lesson-feed-as-product is actually right, stop immediately. Don't try to do both. Plan is coherent only under graph-as-product commitment.
- **Stage-inversion edges interact with opacity field.** 2,325 edges (~8%) have a prereq staged more advanced than its successor (documented in MEMORY.md). The opacity field's `stage_distance` component will produce locally-inverted signals around those node pairs. Not blocking for 12A, but the new render path should be spot-checked on a few known-bad edges (see `stats.py` output for inversion list). If the visual glitch is noticeable, either fix the worst-offender edges first or dampen the stage_distance weight in the opacity formula.
- **Sprout is a partial lesson-feed concession.** The Math Academy agent's "lesson-feed as product" position did not actually lose cleanly — it won for Persona A, where the full-screen single-topic Sprout card is conceptually a lesson feed under another name. The plan is coherent under "graph is product for Personas B and C; Sprout is a sibling experience for Persona A." Don't let this framing rot — if 12B Sprout starts wanting a back-button to the graph, the conceptual boundary is leaking and it needs re-examination.
