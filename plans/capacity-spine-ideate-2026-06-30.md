# Capacity Spine — Ideate Dialectic (2026-06-30)

`/dialectic-review --ideate` on "the capacity spine": a floor-to-ceiling layered structure of cognitive
faculties for OKG. Griffin's locked decision: the spine is **layered** — DISTINCT, more-abstract
faculty-sets take over the further out you go (new structure at altitude, not the same 10 re-weighted).
5 generators (cognitive-science / architecture / learner / parent / adoption), 2 challengers, 3
synthesizers, all Opus. Generator outputs merged + deduped below; verdicts appended after.

---

## A. The theoretical model (what the spine IS) — from the cognitive-science vantage

- **A1. Two axes, not one ladder.** Vertical THREADS = each infant capacity redescribed upward into its
  mature form. Horizontal BANDS = genuinely new faculty-sets that switch on at altitude with NO infant
  ancestor. A topic's "shape of understanding" = its loading on the threads, read at the band its stage
  selects. (Answers "distinct vs re-weighting": it's BOTH — threads carry continuity, bands carry the new.)
- **A2. Four bands, not seven sets.** Map the 7 OKG stages onto ~4 Piagetian reorganizations: floor
  (proto+pre-formal, shipped); Band 1 concrete-operational; Band 2 formal-operational/abstract; Band 3
  formal-systems; Band 4 expert/disciplinary (= Band 3 faculties at higher automaticity + epistemic adds).
- **A3. Per-band faculty-sets (named, theory-anchored, testable):**
  - Band 1 (concrete-ops, Piaget): conservation/invariance, reversibility, class-inclusion, transitive
    seriation, decentration, unit-iteration/measurement, perspective-taking.
  - Band 2 (formal-ops; Inhelder & Piaget, Gentner): hypothetico-deductive, control-of-variables,
    combinatorial, proportional/multiplicative, propositional/conditional logic, relational-analogical
    mapping, reification.
  - Band 3 (formal-systems): axiomatic-proof, modeling/formalization, symmetry/invariance-under-transform,
    recursion/self-reference, representational fluency, generalization/parameterization.
  - Band 4 (expert; Chi, Ericsson, King & Kitchener): deep-structure perception, epistemic cognition,
    conditionalized/forward reasoning, generative recombination, cross-domain transfer, metacognitive
    regulation. (Deep-structure perception = the formal def of "shape of understanding" — Band 4 reads the spine itself.)
- **A4. The vertical threads (infant → expert, ~9-10):** objects→conservation→invariance/symmetry;
  space→perspective-taking→structural-systems; number→measurement→proportional→analysis;
  discernment→multi-attribute→relational-analogical mapping→isomorphism; seriation→monotonicity→order/optimization;
  classification→class-inclusion→formal-type-systems; naming→notation-fluency→formal-semantics;
  symbolic-function→reification→recursion→reflective-abstraction; agents→mechanism→control-of-variables→systems-dynamics;
  social→theory-of-mind→epistemic-perspective→intersubjective-justification (this thread powers Band 4 epistemics).
- **A5. Orphan faculties — name where the mapping BREAKS, as a feature.** Proof, hypothesis-testing,
  recursion, and especially PROPORTIONAL/multiplicative reasoning have NO infant ancestor (proportional is a
  *false friend* of number-sense — additive sense doesn't bootstrap ratio; Carey, Meyer & Land threshold
  concepts). Claiming pure continuity won't survive a dev-psych referee; lead with the threads AND the breaks.
- **A6. Representational Redescription (Karmiloff-Smith) as the growth engine.** Bands = explicitness levels
  (do conservation at 7, state at 12, prove at 18, generalize at expert), not difficulty buckets — a
  principled, possibly-derivable mechanism for why bands exist and are ordered.

## B. How it's computed / represented (architecture)

- **B1. Ancestry-flow propagation operator (the engine).** Faculty profile = a single reverse-topological
  sweep over the existing prereq DAG: each seed emits a unit vector; each topic = weighted blend of its
  prereqs' profiles + its own seed edges, L1-normalized to a simplex. Deterministic, reproducible, ~30 lines,
  regenerated in CI like the radial. Add per-hop decay λ^depth as a knob.
- **B2. Pure infant-propagation COLLAPSES (the load-bearing finding).** Diffusing only the 10 floor seeds up
  7 stages converges every node to the same blend — the whole-graph version of the floor's anti-collapse
  problem. So the design MUST split into (a) the operator [B1] + (b) a LAYERED BASIS that adds distinct seeds
  at altitude. This is the architectural proof that Griffin's "distinct set" decision is *necessary*, not optional.
- **B3. Faculty space as a PROJECTION (recommended; keeps DAG pure).** Faculties live OUTSIDE the prereq
  graph as a tiny artifact: per-stage bases + `(capacity→faculty)` and `(faculty_N→faculty_N+1)` transition
  matrices (~hundreds of numbers). Run B1 in the infant basis, then multiply by transition matrices at each
  stage boundary to re-express in that band's own basis. Per-topic profile = a generated field. Zero new
  edges → zero cycle risk, zero open-data edge pollution; retune one matrix → whole spine re-derives.
- **B4. Stratified faculty RAIL as `kind: faculty` nodes (alternative).** Add ~40-60 faculty nodes (new kind,
  reusing the capacity kind-guard) as a sparse stratified DAG alongside topics; topics attach at their own
  altitude. Acyclicity via a stage-monotone lint (a kind:{capacity,faculty} edge may only target a strictly
  lower stage). Makes faculties navigable nodes — at the cost of injecting enabling-edges into public topic
  frontmatter. **B3 vs B4 is the real architecture fork.**
- **B5. On-demand dual-accumulator walk.** Piggyback two tallies on the ancestry walk fluency.js already
  runs: one weighted by edge type = topic DEMAND vector; one weighted by the learner's 0-100 fluency on each
  ancestor = learner STRENGTH vector, same basis, directly subtractable → the strengths/weaknesses map for
  free. Store nothing; always live.
- **B6. Domain × thread prior matrix (~19×~9 ≈ 150 theory-grounded numbers).** Author once (engineering:
  invariance HIGH, social LOW, etc.); auditable seed for B1. The judgment lives in ~150 inspectable cells, not
  15K per-topic guesses.
- **B7. Emergent faculties via factorization (research probe).** Factorize B1's 15K profile matrix per stage
  (NMF/sparse-PCA); recurring latent bundles = candidate higher faculties; human only NAMES the factors.
  Generates B3's basis from the graph's own topology instead of hand-authoring. May be uninterpretable.
- **B8. Model of Hierarchical Complexity as a deterministic altitude metric.** Task-analytic ordering
  (Commons/Fischer) assigns a topic's band from the structure of what it asks, learner-independent; cross-check
  vs the stage field → disagreements surface mis-staged topics (auditable error class; ties to the known 8%
  stage-ordering violations).
- **B9. Keystone-only seeding.** Hand/rule-curate faculty edges for the few-hundred high-centrality keystones
  (centrality already computed), then propagate (B1) to the ~14K rest. Human effort O(keystones), not O(topics).

## C. Learner-facing product

- **C1. Topic X-Ray ("what is this made of?").** Search any topic → its 4-6 faculty decomposition, each traced
  down the spine to its infant origin. Zero data required → the zero-friction entry ramp; teaches the spine by
  example. (Adoption-critical; UTILITY-PLAY.)
- **C2. Friction Forecast.** On a topic page, before studying: "this leans on conservation + spatial-structural
  — your two weakest faculties; the friction isn't the chemistry, it's the spatial part," + ONE faculty-purity
  detour (the cleanest lower topic that exercises the weak faculty in isolation, possibly cross-domain). This
  is exactly Griffin's Heat-Recovery example.
- **C3. Fog-of-War Fingerprint.** The faculty radar redesigned around CONFIDENCE: unmeasured faculties drawn as
  fog (not a lying zero); "3 questions to clear this fog" button; altitude-banded so abstract bands sit in fog
  until you climb there. Honesty becomes the engagement loop.
- **C4. Spinal X-Ray (recolor the radial).** Toggle: color every node by predicted friction for THIS learner
  (demand × profile) → the map becomes a topography of hot ridges/cool valleys CUTTING ACROSS domains; second
  toggle colors by dominant faculty. Reuses existing fluency-recolor infra; most demo-able.
- **C5. Latent-Faculty Diagnostic + Faculty Tracks.** When a learner stumbles on several unrelated topics,
  decompose the failures → "all 4 share proportional reasoning; the wall isn't the subjects, it's one trainable
  faculty." Companion: a cross-domain easy→hard study path for one faculty. (Highest honesty risk — gate hard.)
- **C6. Faculty Fingerprint via flexing-what-you-know.** Build the profile by anchoring on topics you ALREADY
  understand (a mirror of strength), not a weakness quiz; screenshottable "shape of my understanding."

## D. Parent-facing product (floor)

- **D1. Plain-language renames of the 10** (keep academic name as subtitle): Solid Things, Hidden Things;
  Wanting and Trying; A Sense of How Many; Where Things Are; Me, You, and Us; Same or Different; Putting Things
  in Order; Words Stand for Things; Things That Go Together; Pretending and Imagining. (Cheapest highest-leverage
  win; zero liability — titles only.)
- **D2. Ten Wonder Cards.** One flip-card per capacity; front = plain name + softened Core Idea; back = 2-3
  "things you might delight in catching" (Observable Signs) each welded to ONE play idea (Emerges Through).
  Publishes authored-but-unrendered node content; notice→play pairing makes it "fun thing to try," never a
  checklist. Lowest-risk enrichment.
- **D3. "Building Toward."** Tap a capacity → the real forward prereq thread (pretend → first stories → reading
  → narrative…), answering "what is this play building toward?" Only OKG can build it (needs the prereq spine).
  Keep it descriptive of the DOMAIN, never predictive of the CHILD.
- **D4. This Week's Play.** One capacity + play idea, rotating weekly, deterministic from the date (week mod 10)
  → feels personalized while storing NOTHING. Furthest point from the liability cliff.
- **D5. Anti-Checklist sign format (the safety rail).** Signs always a shuffled PARTIAL sample ("a few things
  you might notice"); zero age/ordinal anchoring; phrased as present delight + a play response; "kids vary
  wildly — wonder, don't worry." Attacks checklist STRUCTURE (which the existing word-lint can't see). Codify as
  a §6 spec addendum.

## E. Adoption / shareable artifacts

- **E1. Cradle-to-Frontier Card.** Parent taps what their kid does ("stacks blocks") → the faculty it builds,
  traced up the REAL graph to an impressive adult topic ("the same chain that ends in conservation laws"). The
  punchline is the RECEIPT (a literal ancestor path, not a metaphor) — that defensibility survives a skeptic's
  screenshot. Bounce risk: if the leap reads as horoscope, the real-path proof must load WITH the claim.
- **E2. Seed Map.** The 10 capacities as seeds at the base, the whole OKG graph blooming upward into every
  domain; explorable. Converts the structural achievement into emotional, screenshot-native product. Safe as a
  map of KNOWLEDGE; the cliff appears only if you persist per-CHILD lit-up state.
- **E3. Family Spine (moonshot).** Child + adult on the SAME spine: "your toddler is at the root building
  spatial reasoning; you're 200 topics up the same branch learning fluid dynamics — same faculty, 30 years
  apart." Shareable emotion = connection (rarer/stickier than pride or vanity); uniquely ownable by a
  prereq-graph product. Needs a pre-rendered example before asking the user to build their own.
- **E4. Bounce-traps (universal, weigh in every product decision):** (1) never show the raw 15,285-node graph
  on arrival — it reads as homework; enter through ONE concrete example. (2) Never front-load an assessment —
  even 3 questions is a wall to a tweet-clicker; value precedes every ask. (3) Faculty claims must show the
  "real path" receipt in the same glance, or it collapses into horoscope and the best sharers bounce.
- **Adoption verdict:** parents are the cheaper viral wedge (high share coefficient + pride hook) BUT carry the
  highest trust risk (one "is my kid behind?" misread → backlash); learners are slower but safer. Educators =
  worst spread, best legitimacy. Suggested stranger-facing order: lead with C1/Topic X-Ray (zero-friction
  proof) → E1 Cradle-to-Frontier as the money shot → E3 Family Spine as aspirational hero.

---

## CROSS-CUTTING CONVERGENCES (independent agents agreeing = strong signal)
1. **Derive, don't stamp.** Cog-sci (A/B6/B9), architecture (B1/B3), and learner (B5) independently reject a
   15K blind LLM pass in favor of deterministic propagation up the DAG seeded by a small theory-grounded basis.
2. **Distinct altitude basis is necessary** (B2) — pure infant propagation collapses; this *proves* Griffin's
   "distinct set" decision is forced by the math, not just an aesthetic choice.
3. **Profile axis vs prereq nodes** (B3 vs B4 / A10) is THE architecture fork to decide.
4. **Honesty is the product** — fog-of-war (C3), orphan faculties (A5), "real-path receipt" (E1/E4), demand-not-
   verdict framing all say: the trustworthy version beats the confident-looking one, on both ethics and adoption.
5. **Parent end stays stateless enrichment** — every parent idea (D2-D5, E2) deliberately delivers "for MY kid"
   feeling via stateless means (date-rotation, graph-traversal, self-selected tapping) to avoid the COPPA cliff.
