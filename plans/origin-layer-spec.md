# Origin Layer Spec — typed developmental-capacity floor (Option iv)

**Status:** APPROVED (re-scoped) — Griffin ratified premortem CONDITIONAL GO, 2026-06-26.
**Decision lineage:** `plans/precursor-primitives-probe-2026-06-26.md` (probe + dialectic + premortem).
**One line:** Add 10 developmental precursor *capacities* as a new typed node-kind beneath the 314
pre-formal roots — fixing the disconnected-roots defect and anchoring the path engine — without
rebranding the project or coupling to a parent-tracker product.

**Built (2026-06-26):** 10 capacity nodes + schema plumbing shipped; 80 pre-formal roots wired
(kindergarten + feelings); anti-collapse gate PASS; fluency regression test green; validate clean;
all public surfaces exclude capacities; ~234 roots deferred. Uncommitted at session wrap.

---

## 0. APPROVED SCOPE (re-scoped after premortem — SUPERSEDES conflicting detail below)

Premortem (3-2-1 Opus, 2026-06-26) verdict: **CONDITIONAL GO on a GRAPH-ONLY, single-session pilot.**
The full-spec risk concentrated in Decision D (public pages); reversing D drops nearly all
strategic/SEO/funder risk at zero cost to the structural win (ancestry resolution is fluency-
independent and survives). Griffin ratified all five conditions. Binding scope:

1. **Decision D REVERSED → graph-only.** Capacities stay IN the prerequisite graph + `graph.js`
   (ancestry resolves, dead-ends fixed) but are EXCLUDED from rendered topic pages, the sitemap, and
   JSON-LD `competencyRequired`. No public capacity pages, no `## Observable Signs` published surface,
   no parent-facing SEO. (Kills premortem scenarios 6 / 8 / 9-smell. The `## Observable Signs` body
   section is still authored for future use but not rendered.)
2. **Fluency go/no-go (verified live bug).** A capacity at fluency-100 would trip `fluency.js`
   forward-cap (`FORWARD_CAP_WEIGHT 0.9`, cap cascades `0.9^depth`). Implement "assumed-known" by
   (i) pruning `kind:capacity` from path computation BY KIND (not by seeding score 100) and
   (ii) excluding `kind:capacity` from the `capSource` forward-cap loop (one `continue`). Add a
   regression test "adding a capacity prereq lowers no successor's effective score," and run a
   manual before/after trace on ≥3 deep topics downstream of a wired root. **Any observed cap = STOP.**
3. **Single-session scope.** Plumbing (§2) in full; wire a **20–30-root PILOT** on the cleanest
   clusters (counting / shapes / feelings), NOT all 314. Script-wire the remainder only if it lands
   in-session; do not gate on 314. (Answers premortem #7: a one-session integrity repair of existing
   primary-track assets is defensible; a multi-session content build now is not.)
4. **Four deterministic pre-commit gates:** (a) §4 anti-collapse (≥4 distinct capacity-prereq
   signatures, none >40%) PLUS the assertion "every wired root has ≥1 capacity ≠
   `discernment-same-different`"; (b) a `validate.py` lint over `## Observable Signs` bodies
   rejecting age-cutoff language (`by \d+ months`, `if not`, `delay`, `concern`) and requiring the
   disclaimer; (c) literal-`"validated"` sweep of `tools/` + add a `"reference"` key to
   `dedup_analysis.py` STATUS_PRIORITY; (d) a 20-wiring HUMAN eyeball (sample agreements, not just
   oddities — wiring correctness is the single biggest residual risk; the diversity gate is blind to it).
5. **Dedup/connect hardening:** rename the bare id `classification` → `classification-sorting`; add
   the 11 capacity ids to the dedup/connect ignore sets; one `kind`-guard in `connect_leaves.py`.

**Single biggest residual risk:** wiring correctness is structurally unguarded (only the §4d human
eyeball backstops it — the baseball-sim "aggregate gate passing ≠ per-claim correct" trap). Keeping
the substrate PRIVATE (condition 1) is what makes a wrong edge internal-and-revisable rather than
crawler-published. Document contested placements (e.g., binaries→`naming-symbol-reference`) as
CHOICES, not asserted facts.

## 0.6 WIRING-SCOPE RESOLUTION → A′ (corrected-A). Decided 2026-06-29 via `/dialectic-review --tradeoff`.

The "finishing the floor" pass surfaced that the original "314 roots" was a miscount: only **37** of the
314 pre-formal topics are true graph-roots (zero prereqs); 277 already chain down to them. Tradeoff
dialectic (2 advocates / 2 counter-advocates / 1 referee, all Opus; full record below) on **A** (wire all
314 directly) vs **B** (wire only the 37 true roots, inherit the rest):

- **B falsified:** transitive inheritance disagrees with direct wiring on **62% of non-roots** (138 lose a
  capacity, 98 gain a spurious one) — it yields the *least*-specific set, contradicting §4's "most
  specific" craft; `what-is-soil` dead-ends under B day-one (its only prereq is a higher-stage node).
- **A's only real fault was regex quality, not scope:** the rule matched on the **course name**, blanket-
  stamping e.g. `core-agents`+`classification` (hard) onto all 16 `living-things` topics incl. body-parts/
  senses; plus title homonyms (`fact-families`/`instrument-families`→core-social, `vocabulary-building`→
  core-space, `quiet-time`→grade-seriation, `subitizing`→classification). These false edges sit in PUBLIC
  topic frontmatter (only capacity *nodes* are private; edges from public topics are open data).

**A′ = keep the full direct floor, fix the regex** (Griffin ratified, leans-A′ on both deciding beliefs:
the parent tracker is deferred-not-dead, and redundant-but-correct `kind:capacity`-typed enabling edges
don't degrade the open data). Implemented in `tools/wire_capacities.py`:
1. Per-topic rules match **title + tags only** — never the course name.
2. Curated `COURSE_DEFAULTS` for content-homogeneous courses (feelings→core-social+symbolic-function,
   music→discrimination, stories→symbolic-function) — deliberate, not accidental course-name hits.
3. Homonym guards strip the four documented false positives.
4. `reconcile_prereqs` replaces the add-only inserter (adds AND removes capacity prereqs to match the
   computed target exactly — the de-sticky deletion tool the project lacked).
5. **Connectivity invariant in `validate.py`** (NEW): every pre-formal topic must reach a `kind:capacity`
   node via prereq ancestry — backstops the content-based wiring so a future unmatched true-root is caught
   loudly, not silently dead-ended. Proven sound: 314/314 reach a capacity live, 0/314 if capacities
   ignored.

**A′ result (2026-06-29):** 307 pre-formal topics directly floored, 7 unfloored (all CONNECTED — reach the
floor transitively, zero true-root dead-ends); anti-collapse gate PASS (35 signatures, top 19%, disc-only
6%); validate clean incl. connectivity invariant; fluency regression green. Eyeball surface (full, grouped
by course): `plans/origin-layer-wiring-review.md`. The 7 unfloored: 3 art judgment-calls
(dance/decorating/looking-at-art) + `why-water-is-important` + 3 self-care routines (brushing-teeth/
washing-hands/why-we-drink-water). Supersedes the §0.3 "20–30-root pilot" scope and the §4 "314 roots"
wording. Decision lineage + four agent cases: this session's transcript; durable summary in MEMORY.md.

---

---

## 1. Design principles (what the dialectic locked in)

1. **Decoupled from the tracker.** This spec is a graph-integrity edit only. The parent-facing
   developmental tracker is OUT OF SCOPE — a separate, later, separately-gated decision (where the
   zero-users base rate and COPPA/liability bind). Nothing here commits to it.
2. **Conservative present identity; aspirational North Star.** Public per-page framing stays
   "prerequisite map of what is taught and studied." "A complete map of everything *learnable*,
   grounded in the capacities all learning presupposes" is recorded as the project's **aspirational
   target** (PLAN.md vision), NOT asserted on topic pages or in JSON-LD. (Griffin, 2026-06-26.)
3. **No clean "center" is claimed.** The dialectic established the origin layer is ~5–6 *parallel*
   foundations + a short build-up chain — a narrowing **funnel**, not a single-node pinch. We sell
   the connectedness gain (314 dead roots → a rooted substrate), not a mythical hourglass neck.
4. **"Enabling, not reductive" is honored by node-kind, not a new edge type.** Edges stay `hard`/
   `soft`. The developmental/enabling flavor is *derived*: any edge whose source is `kind: capacity`
   is an enabling edge. Consumers that care can filter on kind. We do NOT claim derived concepts
   reduce to capacities (Carey/bootstrapping caveat).
5. **Differential wiring (anti-collapse).** Each root is wired to its *most specific* capacity
   prerequisites, not just the universal `discrimination`. This is the guard against the referee's
   reversal condition ("if everything just points to discriminate, the layer adds no signal").

---

## 2. Schema changes

### 2.1 New optional field: `kind`
| Field | Type | Default | Values |
|---|---|---|---|
| `kind` | string | `topic` (implicit when omitted) | `topic` \| `capacity` |

All 15,285 existing nodes are implicitly `kind: topic` (omit the field — no mass edit). Only the ~10
new nodes carry `kind: capacity`. Parser is field-agnostic (no code change); add one row to
`meta/schema.md`.

### 2.2 New status value: `reference`
Capacity nodes are not quiz-assessable and must not carry `validated`. Add `reference` to
`VALID_STATUSES` in `validate.py` (1-line change). Update the CLAUDE.md invariant from
"all topics validated" → **"all `kind: topic` nodes validated; `kind: capacity` nodes are
`status: reference`."**

### 2.3 New developmental stage (low-stakes — see Open Decision A)
Add one stage below `pre-formal` to `meta/developmental-stages.md` + `VALID_STAGES`. Recommended
token: `proto-formal` (alternatives: `innate`, `origins`). Stage is display-only here (behavior is
driven by `kind`), so the name is low-risk.

### 2.4 New meta-domain (structural necessity)
`validate.py` requires `domain ∈ domains/` and resolves prereq targets via `domains/**/*.md`, so the
capacity nodes must physically live under `domains/`. Create:
- `domains/developmental-origins/_domain.yml` (a **meta-domain**, flagged hidden)
- `domains/developmental-origins/precursor-capacities/` (one course, holds the ~10 nodes)

**Count integrity:** headline counts ("19 domains, 15,285 topics") report `kind: topic` only. The
origin layer is reported separately ("+10 foundational capacities"). `stats.py`, index generation,
and CLAUDE.md status text must exclude `kind: capacity` from headline domain/topic counts. (CLAUDE.md
data-propagation rule applies — sweep all count references on implementation.)

### 2.5 Capacity-node body template (replaces the topic template)
```markdown
## Core Idea            (required — what the capacity is, plainly)
## Emerges Through      (how it develops; replaces "How It's Best Learned" — NOT instruction)
## Observable Signs     (illustrative developmental markers — see liability boundary §6)
```
NO `## Questions` (not assessable) — so assessment skips them even before the kind-guard.

---

## 3. The ~10 origin nodes

`kind: capacity`, `domain: developmental-origins`, `course: precursor-capacities`,
`status: reference`, `stage: proto-formal` (pending Open Decision A).

### Foundations (`prerequisites: []` — co-equal roots; there is no single root)
| id | title | core idea (1 line) |
|---|---|---|
| `core-objects` | Object Cohesion and Permanence | Things are bounded, solid, move continuously, and persist when hidden. |
| `core-agents` | Agency and Goal-Directed Action | Some things act toward goals — the seed of cause and intention. |
| `core-number` | Approximate Number and Small-Set Tracking | Rough magnitude ("more") + exact tracking of 1–3 things. |
| `core-space` | Spatial Layout and Geometry | Distance, direction, and arrangement of places. |
| `core-social` | Social Beings and In-Group Awareness | People are special agents; self vs. others, familiar vs. stranger. *(Open Decision B — include?)* |
| `discernment-same-different` | Discernment: Same and Different | Isolate one attribute and judge two things same or different. The central operation (renamed from "Discrimination"; fed by objects, number, and symbolic-function under the Jul-1 restructure). |

### Build-up (depend on foundations)
| id | title | prereqs (kind:capacity) | core idea |
|---|---|---|---|
| `grade-seriation` | Grading and Seriation | hard: `discernment-same-different`; soft: `core-number` | Order instances along a gradient (small→big). |
| `naming-symbol-reference` | Naming and Symbol–Referent Mapping | hard: `discernment-same-different`, `grade-seriation` | A word/sign stands for a thing; **binary opposites = naming the two gradient endpoints** (hot/cold). ← where Griffin's "binaries" live. |
| `classification` | Classification and Sorting | hard: `discernment-same-different`; soft: `naming-symbol-reference` | Group many things by a shared attribute. |
| `symbolic-function` | Symbolic Function | hard: `naming-symbol-reference`, `core-objects` | Hold a thing in mind in its absence; unlocks language, pretend, counting. The gateway. |

→ ~11 nodes. Internal structure: 5–6 parallel foundations → discrimination → grade → name → classify,
with symbolic-function as the gateway the 314 roots mostly route through.

---

## 4. Wiring rule: capacity → root (the load-bearing craft)

**Principle:** wire each root to its *most specific* capacity prerequisites. `discrimination` is
near-universal and may attach to most roots, but every root must also carry ≥1 *more specific*
capacity so the layer adds differential signal.

Worked examples (hard edges unless noted):
| root topic | capacity prerequisites |
|---|---|
| `counting-to-five` | `core-number`, `discernment-same-different` |
| `comparing-quantities-more-less-equal` | `grade-seriation`, `core-number`, `discernment-same-different` |
| `sorting-by-one-attribute` | `classification`, `discernment-same-different` |
| `recognizing-basic-2d-shapes` | `core-space`, `discernment-same-different` |
| `positional-words-above-below` | `core-space`, `naming-symbol-reference` |
| `naming-your-feelings` / `feeling-happy` | `core-social`, `symbolic-function`, `discernment-same-different` |
| `first-stories-and-read-alouds` | `symbolic-function`, `naming-symbol-reference` |
| `recognizing-ab-repeating-patterns` | `grade-seriation`, `discernment-same-different` |

**Bulk wiring (latent-vs-deterministic):** derive a *deterministic* mapping from each root's
`course` + `tags` → a default capacity-prereq set (e.g., any `counting` tag ⇒ `core-number`; any
`shape`/`spatial` ⇒ `core-space`; any `emotion`/`feelings` ⇒ `core-social`+`symbolic-function`;
any `pattern`/`compare`/`grade` ⇒ `grade-seriation`). Apply by script, then human-review the
residual. Judgment only where the tag mapping is ambiguous.

**Anti-collapse acceptance check (script):** after wiring, compute the distinct capacity-prereq
*signatures* across the 314 roots. REQUIRE ≥4 distinct signatures and NO single signature covering
>40% of roots. If it collapses (everything = `{discrimination}`), the layer failed its purpose →
fall back to runner-up (iii) separate annotation. This is the go/no-go gate.

---

## 5. Integration checklist (all CHEAP — verified against code by Explore probe)

INCLUDE capacity nodes (graph membership — so ancestry resolves, dead-ends fixed):
- `validate.py` — no change; cycle/dangling checks pass with capacities as valid prereq targets.
- prereq-graph serialization for client path-finding (`graph.js` build in `generate_quiz_page.py`)
  — **keep capacities IN the graph** (override the Explore agent's blanket-exclude suggestion here).

EXCLUDE capacity nodes (output surfaces — one-line `kind != "capacity"` guard each):
- `generate_keystone_page.py` ~L61 — exclude from centrality scoring.
- `generate_topic_pages.py` ~L768 — exclude capacities ENTIRELY (per §0.1 reversal): no rendered
  page AND no `competencyRequired` emission of capacity ids. Skip `kind:capacity` in the page loop.
- `generate_assessment.py` ~L152/180 + `generate_quiz_page.py` ~L130 — exclude from probe/question
  selection (they have no Questions anyway). NOTE: keep capacities IN the `graph.js` serialization
  (path-finding) — exclude only from question selection.
- `generate_sitemap.py` ~L47 — EXCLUDE capacities (per §0.1 reversal: graph-only, not indexed).
- `visualize_radial.py` ~L159, `visualize_domain_map.py` ~L209/238 — exclude from viz (no synthetic
  domain sector needed).
- `stats.py` / index — exclude from headline counts (§2.4).

POLICY (follow-up, not v1): in `fluency.js`, treat `kind: capacity` nodes as **assumed-known**
(default fluency 100) for adult learners, so they fix structure without cluttering grown-up learning
paths — while remaining available to a future tracker. Spec'd here, deferred.

---

## 6. Liability / framing boundary (binding, because the graph is crawler-indexed)

`## Observable Signs` content MUST:
- be illustrative, NOT a checklist with age cutoffs;
- contain NO "if not by age X, concern" / delay-inference language;
- carry the standing disclaimer: *"Developmental markers vary widely; this is an enrichment map, not
  a screening tool. For concerns about a child's development, consult a pediatrician."*
- collect no data (no tracker here → no COPPA surface at the graph layer).

This keeps even the static graph on the enrichment side of the enrichment-vs-diagnostic line.

---

## 7. Explicitly OUT of scope
- The parent-facing developmental tracker (separate decision; base rate + COPPA bind there).
- Any public "everything learnable" rebrand (aspirational North Star only).
- Recursing below the innate endowment (reflexes, prenatal sensory) — the floor stops at the core
  systems by design.

---

## 8. Resolved decisions (Griffin, 2026-06-26)
- **A — stage token:** `proto-formal`. ✓ LOCKED.
- **B — include `core-social`?** YES. ✓ LOCKED — the 11-node count and the 5th foundation stand;
  wires the 28 feelings-and-self-awareness roots.
- **C — capacities in adult learning paths:** ASSUMED-KNOWN (default fluency 100). ✓ LOCKED.
  Promote the §5 `fluency.js` policy from "follow-up" to **v1** (small, and required so capacity
  nodes don't clutter adult paths the moment they enter the graph).
- **D — capacity pages public?** ~~RENDER~~ → **REVERSED to GRAPH-ONLY by premortem (see §0.1).**
  Capacities get NO rendered pages, NO sitemap entry, NO JSON-LD. They stay in `graph.js` only.
  (§2.5 `## Observable Signs` is still authored for future use but not published.)

---

## 9. Implementation sequencing (after approval + premortem)
1. Schema + validate.py + meta-domain scaffold + developmental-stages.md (the plumbing).
2. Author the ~11 capacity nodes (Core Idea + Emerges Through + Observable Signs).
3. Wire capacity↔capacity edges; run cycle check.
4. Bulk-wire roots via the tag mapping; human-review residual.
5. **Run the §4 anti-collapse acceptance check — go/no-go gate.**
6. Add the §5 output-exclusion guards; run full `validate.py` + regenerate; eyeball radial/keystone/
   counts for leakage.
7. Update CLAUDE.md/ORIENT.md/PLAN.md (counts, invariant, North Star note).

**Acceptance:** validate.py clean; headline counts unchanged (still 15,285 / 19 domains); ≥4 distinct
capacity-prereq signatures; no capacity node leaks into keystone/JSON-LD/quiz/sitemap; path engine
ancestry now reaches the origin layer instead of dead-ending at the 314 roots.
