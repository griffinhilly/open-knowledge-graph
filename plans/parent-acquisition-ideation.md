# OKG Parent-Acquisition Ideation — Final Synthesis

*Multi-agent dialectic, /dialectic-review --ideate --agents 5 --model opus, 2026-04-25*

**Process.** 5 generators (edtech-founder, anxious-parent, learning-scientist, virality, K-12-teacher) → 33 distinct ideas → 2 challengers (feasibility/value, distribution/30s-bar) → 3 synthesizers (independent) → this merged synthesis.

**Goal.** Parent hears about OKG → lands → 30 seconds → "this is the perfect tool for my children." Holds across preK-2 / 3-5 / 6-8 / 9-12, secondarily college. One engineer (Griffin), no marketing budget. Standalone web app, backend services, freemium all on the table.

---

## Headline

The dialectic produced 15 idea clusters. **All three synthesizers independently converged on the same handful of winners — with one big argument about whether the answer is even in the cluster list at all.** The convergence and the argument are both load-bearing.

Two synthesizers (S2, S3) put their #1 slot on **a missing category that the generators didn't propose**: a TikTok-native worksheet-diagnosis content engine, with worksheet-OCR (cluster B) as the landing page that converts the views. The third (S1) keeps the content engine subordinate to the product but agrees worksheet-OCR is the entry surface, not the diagnostic.

The argument worth running before any code: **content-engine-as-primary vs. product-features-as-primary.** That tradeoff decides the next 90 days.

---

## High-Confidence Convergence

All three synthesizers ranked these in their top 5 (or top 5+1). These are the ideas where independent post-challenger analysis agrees.

### Tier-1 BUILD (3 of 3 synthesizers)

1. **B — Worksheet / Test OCR → Upstream-Brick X-Ray.** Photograph the homework or returned test → vision API → OKG walks 2-3 prereq hops upstream → output is a single shareable artifact: "the broken brick is *equivalent fractions*, not *long division*." All three synthesizers ranked B in their top 2. The disagreement is sequencing (standalone v1 vs sequel to A) — see §Disagreements.

2. **D-narrowed — Mrs. Johnson's Page.** The only D-variant worth building. Teacher pastes their unit's topics into a 90-second authoring flow → gets a shareable URL → sends to 25 parents in the class newsletter. Each landing parent sees the prereq spine for *their kid's actual class*, with a per-topic readiness check. Distribution-built-in: one teacher = 25 parents, no school-district sales motion. All three synthesizers had this in top 5; C2 also identified it as the only D worth pursuing.

3. **N-defanged — IEP/504 Companion.** All three synthesizers overruled Challenger 1 here and sided with Challenger 2: this is "the most underrated idea in the brief." IEP communities (CHADD, Understood.org, r/Autism_Parenting, r/specialed) are mobilized, share aggressively, and have no graph-based tool. C1's FERPA/litigation concern is real but solved by **scoping the product to "explain the prereqs of the goal," never "advocate for goal changes"**, plus local-only / never-store-IEP processing. The community moat + content-policy moat are exactly the kind of defensibility a one-engineer no-budget project needs.

### Tier-1 BUILD (2 of 3 synthesizers)

4. **A — Diagnostic Heatmap with Fictional-Kid Demo Landing.** The 24Q diagnostic + Bayesian engine + radial fluency viz already exist. The 30-second bar fails when A is gated behind 5-8 minutes of kid-cooperation; it clears the bar when the *landing page itself* is a pre-rendered x-ray of "Maya, 4th grade" — visible in 8 seconds, no signup. S1 places A as #2 product-spine; S3 demotes A to "the visualization layer that makes #1, #2, and #3 legible — A is the brand asset, not the product surface." S2 collapses A into B entirely (B is the diagnostic, not a sequel to one). All three agree A's calibration-crisis (C1's headline concern) is real and binding.

5. **The TikTok / Reels Content Engine** *(formally cluster "missing-category #1," not in the original 15)*. 60-90s videos: parent-submitted worksheet → host points at the wrong answer → upstream-walk to the actual broken brick → CTA "drop your kid's worksheet, link in bio." Link goes to B. **The content IS the marketing AND the demo.** S2 and S3 rank this #1; S1 keeps it subordinate but still calls it "marketing infrastructure that should be built after #1 ships." Real disagreement on rank-#1 status — see §Disagreements.

### Tier-1 BUILD — K-reframed (post-synthesis correction, Griffin 2026-04-25)

The dialectic ran K with the "gifted-track / 5% TAM" frame inherited from Beast Academy / AoPS — both challengers used that frame to demote it. **That frame was wrong.** The actual demographic is much wider: **parents who believe their kid can do harder, more rigorous work and feel limited by their school from even trying.** That spans:

- Ambitious-mainstream parents whose kid is on-grade-level but underchallenged
- Microschool-curious / homeschool-adjacent parents
- Parents whose kid tested into G&T but the program is weak / unavailable
- Pandemic-acceleration parents (kids who advanced rapidly during pods)
- The "their kid is reading at 4" / "doing arithmetic in head" tribe

This is closer to **20-30% of intentional parents**, not 5%. And critically, it has *strong organic distribution* — these parents share aggressively because they want validation that their instinct (*my kid is held back*) is correct.

**The product reframe:** the radial graph itself becomes the value prop, not a backend. "See your kid's actual ceiling across all 19 domains, not just the 1 your school grades them on." Cross-domain breadth is OKG's wedge against AoPS's math-only depth and Synthesis's small-cohort framing. **K-reframed is now Tradeoff #2 option 4.**

### Tier-2 BUILD (1 of 3, but flavor preserved)

6. **G — Summer Slide Insurance** (S1's pick): time-boxed June campaign, "Mathnasium charges $300/mo for this; we're free and better-targeted." Calendar-driven distribution event. Skip if not launching April-May.

7. **F — Daily Practice / Spaced Review** as silent retention only. All three synthesizers degrade F from acquisition surface to retention surface. Don't market F. Don't put F on a landing page. F runs silently after a #1-#3 moment.

### #6 — Weird-But-Worth-Thinking-About

**The Audio-First Car-Ride Product** (C2's missing-category #2, S2 + S3 both flagged). 12-minute drive-time podcast: today's prereq walk for [grade] [domain]. Parent and kid listen together. No app install (RSS + Spotify/Apple). The 15-minute morning school commute is the most under-monetized parent-attention block in the world; OKG's graph is the only IP that can systematically generate this content. Park for month 6, pursue if #1-#3 land.

---

## High-Confidence SKIP

All three synthesizers ranked these out:

- **C — Family Dashboard + Weekly Digest.** Retention infrastructure mislabeled as acquisition. Phase 4 at the earliest.
- **E-standalone — Parent Re-Education.** ChatGPT eats this. Build the *graph-aware* slice (the Socratic-coaching script + Common-Core method translator) only as a feature inside #1-#3, never standalone.
- **H — Conference / Educator Translation.** Niche, twice-yearly, narrow trigger window. Build as a single seasonal blog post + free tool 2 weeks before October/March, not as product.
- ~~**K — Gifted Accelerator Track.** Year-2 second product line. Defer.~~ **REVISED — see "K-reframed" below.**
- **L-standalone — "Am I A Bad Parent" Reassurance LLM.** Hallucination-screenshot risk; ChatGPT replicates for free; no share loop. **But** see honest caveat #3 — there's a real product question hiding inside L that the dialectic didn't reach.
- **M — Mastery Gate / Transfer Test / Confidence Layer.** Pedagogically excellent, parent-invisible. Backend only. Knewton's grave is the warning.
- **O-standalone — Method Translator.** Politically charged Common-Core minefield as standalone; survives only as a feature inside #1 or #3, or as TikTok-content content (which is #1's content pipeline anyway).

### Skipped with internal disagreement

- **I — Sprout-as-Trojan-Horse.** S1 + S3 with Challenger 1: skip as funnel ("Sprout buries the cross-domain wedge that doesn't activate until 3rd grade"). S2 with Challenger 2: ship standalone with the wedge visible to the parent from minute one. **Final position (2 of 3): keep Sprout alive as a side-product, don't make it the parent-acquisition front door.** The 3rd-grade-and-up parent is the primary persona for OKG's graph value; preK-2 is real but secondary, and the visual frame ("coloring book") doesn't translate upward.

- **J — Knowledge Wordle / shareable artifacts.** S1: marketing infrastructure, not product. S2: skip outright (Wordle's viral coefficient has collapsed since 2018). S3: redirect — the right shape is **the diagnostic heatmap screenshot from #4 used as the shareable artifact inside #1**, not a Wordle clone. **Final position (3 of 3 against the Wordle format itself, 3 of 3 for "shareability is real but the heatmap is the artifact"):** kill the Wordle/quiz/streak-card subprojects. Invest the equivalent engineering hours in making the heatmap screenshot from #4 ravishing as a standalone image, with built-in share affordances.

---

## Disagreements Worth Surfacing

### Disagreement #1: Is the answer in the cluster list at all?

- **S1 view:** The product spine A→B→F is right; calibrate ~200 anchor topics with real kid data; ship A+G as a June campaign with B as sequel. Content marketing is downstream of a working product.
- **S2/S3 view:** The dialectic itself is too feature-focused. With no marketing budget, **content marketing IS the marketing.** The right v1 is the TikTok worksheet-diagnosis engine + B as the landing. Calibration happens *through* the content pipeline (every video calibrates one more topic).

This is the load-bearing tradeoff. **Recommend: this gets a focused `/dialectic-review --tradeoff` before the next 90 days are committed.** Pick wrong and the project loses Q2-Q3.

### Disagreement #2: Sprout (I)

- **2 of 3 against Sprout-as-funnel** (S1, S3 + Challenger 1).
- **1 of 3 for Sprout-standalone** (S2 + Challenger 2: "the existing Sprout shell + the 15,290-topic graph beneath it is genuinely unique — highest leverage on existing asset").
- **Final position:** Sprout stays alive as Persona-A side-product, does not get the parent-acquisition critical path. If S2 is right that there's a real Instagram-parent-content motion in Sprout, treat it as a *separate* B-channel with its own brand voice — don't pollute the diagnostic-graph value prop with it.

### Disagreement #3: B sequencing

- **C1 + S1:** B as sequel to A. OCR-as-evidence-for-existing-claim, not OCR-as-magic-trick. Lower accuracy bar because the claim is already on the table.
- **C2 + S2 + S3:** B is the standalone wedge. The 30-second bar clears with the parent's existing artifact (the worksheet in their hand). A's calibration-crisis argues *for* B-first — B can ship narrow (math grades 1-5), generates labeled data, calibrates A in the background.
- **Final position (2 of 3 + both challengers split):** **B-first, narrow scope.** Math grades 2-5 only, printed worksheets only, "this is what I read; correct me" confirmation step before diagnosis. Use the data B generates to calibrate A's 200-topic anchor spine.

### Disagreement #4: N (IEP)

- **C1:** Skip on FERPA + exhaustion + litigation grounds.
- **C2 + all 3 synthesizers:** Build it defanged. Most underrated idea in the brief. C1's risk model is calibrated for a VC-backed startup; for one engineer with no funding, the asymmetric upside of an organized share community outweighs the legal scoping work.
- **Final position:** Build N defanged. Local-only processing, never store the IEP, scope hard to "explain the prereqs of the goal" with no advocacy. $1-2k lawyer consult once. The community-moat thesis gets validated in 5 conversations before any code.

---

## Top 5 Final Ranking (merged)

| # | Idea | 30s impact | Leverage | Days-inv | Defensibility | Top-5 votes |
|---|------|---|---|---|---|---|
| 1 | **B — Worksheet OCR (math 2-5, narrow)** | 9 | 9 | 6 | 6 | 3/3 |
| 2 | **D-narrowed — Mrs. Johnson's Page** | 8 | 9 | 8 | 6 | 3/3 |
| 3 | **N-defanged — IEP/504 Companion** | 8 | 7 | 5 | 9 | 3/3 |
| 4 | **A — Diagnostic with fictional-kid landing** | 8 | 10 | 5 | 8 | 2/3 |
| 5 | **TikTok content engine + B as conversion page** | 9 | 6 | 4 | 8 | 2/3 (#1 votes from 2 of 3) |
| 6* | **Audio-first car-ride product** (weird-but-worth) | — | — | — | — | flavor preserved |

*Score key: 1-10 each. 30s = parent says "perfect" in 30s. Leverage = 80% off-shelf primitives. Days-inv = 10 if ≤7d, 1 if >60d. Defensibility = 10 if uncopyable for 12+ months.*

---

## Concrete First Steps (≤2 days each)

For each top-5 idea, the dialectic produced a "first step" that is **a distribution-validation test, not a build step.** Don't skip these.

1. **B:** Manually diagnose 10 real worksheets from Griffin's parent-friend network. Send back x-rays via DM. Measure: do parents share the x-ray screenshot unprompted? If no, the artifact is wrong; iterate before building OCR.

2. **D-narrowed:** Email 5 teachers (Madi's network, Addi's preK feeders) offering to *manually* build their week's class page free for 4 weeks. Concierge first; tool second. Measure: parent click-through from the teacher email.

3. **N-defanged:** Don't build. Post in 3 IEP communities (r/specialed, CHADD FB group, Understood.org forum): "I'm building a thing that explains the prereqs of an IEP goal — what would actually help?" If response is thin, the community-moat thesis is wrong.

4. **A:** Build the fictional-kid landing as a static Figma artifact. Post on X with "this is what OKG will show you about your kid in 6 minutes — DM me to be in the calibration cohort." Measure share rate on the static.

5. **TikTok engine:** Record 5 manual worksheet-diagnosis videos. Post one. **If Griffin can't do this on camera convincingly, the entire OKG distribution thesis is in trouble and we need to know that before another build phase.** If the format is right but Griffin isn't the on-camera persona, hire a credentialed teacher on Upwork ($2-5k for first 30 videos).

---

## Recommended `/dialectic-review --tradeoff` Targets

Two tradeoffs are worth full multi-agent stress-testing before the next 90-day commit:

1. **Content-engine-as-primary-marketing vs. product-features-as-primary-marketing.** This is the load-bearing decision. S2/S3 say content engine wins; S1 says product spine wins. The two paths look completely different at the 90-day mark — different hires, different first ships, different metrics. Worth running.

2. **Lead with B (worksheet OCR) vs. lead with the TikTok engine that points at B vs. lead with D-narrowed (Mrs. Johnson's Page).** All three are top-tier distribution-built-in plays, but they have different audience capture mechanics (TikTok = cold-traffic-funnel, B = warm-search-traffic, D-narrowed = teacher-distribution). One engineer can only run one with focus. Pick wrong and lose Q2.

---

## Honest Caveats

### Caveat #1: The calibration crisis is real and binding.

C1's strongest point. The 15,290-topic Bayesian engine has the *structure* of psychometric inference without the *response data* needed to make it sound. Per-topic difficulty estimates require ~30-100 real-kid responses each. **Shipping any diagnostic feature without ~200 anchor-topic calibration on real kids = the diagnoses will sometimes be confidently wrong, parents will catch it, and the "perfect tool" reaction inverts to "this thing got my kid wrong."** That's the Knewton/AltSchool failure pattern.

Two viable mitigation paths, both honest:
- **Pre-calibrate (S1's path):** 4-6 week calibration sprint with 50-150 real kids, narrow scope to grades 2-5 math + reading. Then ship.
- **Ship-and-calibrate (S2/S3's path):** Treat the content pipeline / B's narrow-scope launch as the calibration data source. Hard rule: only ship videos / diagnoses on manually-verified topics. Each shipped artifact calibrates one more node.

These paths are **not equally safe.** Path 2 only works if the discipline of "manually verify before shipping" actually holds — which depends on Griffin's ability to refuse to ship something unverified when there's pressure to fill a content calendar. If that discipline is uncertain, Path 1 is safer.

### Caveat #2: Distribution is the actual problem.

The brief framed this as a 30-second-bar question. C2's parting shot was right: "the 30-second bar only matters for parents who land, and most won't." The dialectic generated 15 product ideas because the brief framed it as a product question. Three of the five top-rank ideas (B, D-narrowed, the TikTok engine) have built-in distribution mechanics. Two (A, N) need to be *carried* by something else — A by being embedded in the others' UIs, N by community-organic share.

If after reading this synthesis the action item that lands is "let me build A and B better" — the synthesis failed.

### Caveat #3: The dialectic missed parent emotional state as primary design surface.

Both challengers scored down L (Reassurance LLM) for hallucination risk and ChatGPT-replicability — correctly. But the *underlying observation* — that a parent of a struggling kid is an *emotional* user before a diagnostic one — went unaddressed. None of the top-5 ideas treats emotional reassurance as the primary value prop with diagnosis as the proof. They all treat diagnosis as the primary value prop with reassurance as a side-effect.

There's a real product question here: **what does OKG look like if the primary value is "you are not a bad parent and here is why" with diagnosis as the proof?** That's a different product than what this dialectic synthesized. Worth a future ideation pass framed entirely on emotional-design — perhaps after the first round of #1-#3 feedback comes in and reveals what parents actually shared and why.

---

## Bottom Line

**Skip 9 of 15** (C, E-standalone, H, I-as-funnel, J-Wordle, K, L-standalone, M, O-standalone).

**Build 5**, with one critical pre-build tradeoff:

- **Tier-1, build now:** B (narrow), D-narrowed (Mrs. Johnson's Page), N-defanged (IEP).
- **Tier-1, conditional on the content-vs-product tradeoff:** the TikTok engine + B-as-landing if content-marketing wins; A + B as product spine if product-features wins.
- **Tier-2, retention only:** F (silently, gated behind acquisition).

**Two-day next move:** Run the manual-validation tests on B, D-narrowed, N-defanged in parallel. The TikTok-engine validation (5 worksheet videos) is the highest-leverage single test because it answers Tradeoff #1 — if the videos clear 10k views unpaid, the content path is real; if they die at <500 views and Griffin isn't the right on-camera persona, hire-a-creator becomes Tradeoff #2.

**The single biggest risk:** building any product feature before the distribution mechanism is proven. The OKG project has been edging toward this failure mode for two phases. The synthesis isn't "build the right product." It's "validate the distribution loop with the cheapest possible artifact, then build the product that the loop already wants."

---

# Tradeoff Reviews — Final Rulings (2026-04-25)

After the synthesis, two `/dialectic-review --tradeoff` rounds were run on the load-bearing decisions. Each was 2-4 advocates × cross-assigned counter-advocates × 1 referee, all Opus xhigh. **The two referees converged on the same shape, with one important reframe both made independently.**

## The Reframe Both Referees Made: Calibration ≠ Topology Verification

The single most devastating landing in either tradeoff: **the word "calibration" was being used to mean two completely different operations**, and both the content-engine advocate and the product-features advocate were trading on the rhetorical bridge.

- *Topology verification* (does this prereq edge exist? does the upstream-walk make pedagogical sense?) — a manual review by an expert teacher walking the graph. ~30 topics in 90 days is honest scope.
- *Item-difficulty calibration* (Rasch / IRT — what is the b-parameter for this question under this kid's θ?) — requires kid-response data on items under known prior-knowledge state. ~30-100 responses per topic. 200 topics × 50 kids ≈ months of recruitment + analysis.

**Any plan promising IRT-grade calibration in 4-6 weeks is overclaiming.** Any plan claiming "30 videos = 30 calibrated topics" is overclaiming in the opposite direction. Both referees independently rejected the calibration framing in favor of topology verification on a narrow surface as the realistic 90-day deliverable.

## Tradeoff #1 Ruling — Content vs Product

**RECOMMENDED:** Neither pure option. The synthesis the counter-advocate proposed: start content motion in week 1, run topology verification (not IRT calibration) in parallel scoped to the 30-50 topics the content surfaces, defer the 50-150 kid recruitment sprint to Q3.

Specific implementation:
- **Week 1-2 — format pilot, no creator hire.** Griffin posts 5-8 videos himself in the lowest-friction format that exists (screen-record radial + voiceover walking a parent-named worry). YouTube Shorts + Reels initially; skip TikTok cold-start until after signal.
- **Topology verification, not calibration**, as the parallel deliverable. Each video forces manual upstream-walk of one topic + 5-15 prereqs. Honest scope: 30 topics with verified topology by week 6.
- **External kill criterion at week 4** (not video 30). Pre-commit in writing now: median <300 views on first 10 videos AND zero email captures AND zero comment-driven topic requests → escalate via `/dialectic-review` before continuing. Addresses the soft-kill failure mode directly given Griffin's documented exhaustive-path pattern.
- **Creator hire deferred to a signal-gate, not a calendar-gate.** Hire only if Griffin's own pilot shows ≥1 video over 2k views or ≥5 organic email captures. Realistic creator pricing $300-800/video is the planning number, not $66-165.
- **OCR (worksheet diagnosis) ships as conversion surface week 3-4.** Math grades 2-5 only, GPT-4V or Mathpix off-shelf. Not a calibrated product — a "paste your kid's worksheet, see the prereq chain it tests" demo.

**RUNNER-UP:** Pure 30-day YouTube SEO experiment (drop the calibration-parallel arm, keep everything else).

**NOT RECOMMENDED:** Option B as articulated — it's content-first delayed 8-12 weeks with no discovery channel at the end, against a 6-month internal base rate of feature-shipping producing zero parents.

**Key tradeoff:** Griffin gives up the psychometric-rigor story. He cannot honestly claim a calibrated diagnostic by Q3. The recommendation forces accepting that distribution-finding precedes calibration-finishing — which inverts the project's six-month posture.

**Strongest losing argument:** B's calibration-as-discipline argument, properly stated. Six months of OKG product-building has been undisciplined feature accretion without forcing-function contact with real kids; a 50-150 kid recruitment sprint *would* be different work because the constraint is external. The recommendation absorbs the legitimate part by keeping topology-verification parallel, while refusing the part that defers the unsolved problem (distribution).

## Tradeoff #2 Ruling — Opening Wedge

**RECOMMENDED:** A two-phase 90-day sequence — **B-first, K-second, TikTok deferred, Mrs. Johnson eliminated.**

- **Days 1-35: B build, framed for K-reframed audience.** Worksheet OCR + upstream-brick diagnosis, scoped to 3-4 dominant curricula (Eureka, enVision, Beast Academy, Singapore — not all 50+). **Critical reframing:** the heatmap output is not "your kid has gaps" (struggling-kid framing) but "here's the prereq chain currently blocking ceiling expression in this domain" (acceleration framing). Same artifact, acceleration-tribe-legible copy. **Beast Academy is the bridge curriculum** — most-photographed worksheet in acceleration-parent households.
- **Days 35-60: Standing-capital build via Twitter, not Reddit.** Griffin already orbits the Garry Tan / Tyler Cowen / "talented young people" cluster. That's standing capital that *already exists* — not r/Gifted standing he'd have to earn cold. 8-12 worksheet-diagnosis case studies on Twitter (anonymized real kid worksheets → upstream brick → 30-second insight). Routes around counter-K's most damaging critique (5-community-rejection scenario) by going where Griffin has standing.
- **Days 60-90: Layer K-reframed radial on top of B-acquired users.** Users who came in via worksheet-diagnosis are warm. Add the 24Q + radial as "now see the full ceiling map across all 19 domains." **The kid-cooperation gap dissolves because the kid already cooperated for the worksheet step.** The radial becomes the retention/expansion surface, not the cold acquisition surface.

**RUNNER-UP:** Pure B-standalone with explicit acceleration-tribe Twitter framing — strip the K-layered radial in days 60-90 if UX is sliding.

**NOT RECOMMENDED:**
- Pure TikTok-engine + B — 2026 cold-start economics break the load-bearing "algorithm is the marketing budget" claim.
- Mrs. Johnson's Page — repels the K-reframed audience Griffin just identified, demotes the cross-domain radial moat to invisible backend, Mystery Science precedent doesn't transfer.
- Pure K-reframed cold — community gatekeeping (5 posts → mostly removed/dead in r/Gifted/Davidson/Hoagies/Beast Academy parent FB), kid-cooperation gap at discovery moment, 4-6 weeks UX before any user contact.

**Key tradeoff:** Griffin gives up the cleanest single-shot version of "moat is the value prop in 30 seconds." K-reframed cold is the only option where OKG's actual structural advantage (cross-domain prereq graph) is what the parent sees first. The hybrid puts the worksheet-heatmap first (less-distinctive artifact) and only reveals the radial after a kid-cooperation step. If radial-as-mobile-artifact turns out to be genuinely magic, the hybrid discovers that more slowly than a pure K launch would.

**Strongest losing argument:** K-reframed's "only option where OKG's actual moat is the visible 30s value prop." True — every other option leads with a less-distinctive artifact. K still loses as opener because it requires three prerequisites Griffin doesn't yet have (parent-facing radial UX, standing in gatekept communities where ICP lives, discovery moment that doesn't require kid-cooperation). The hybrid manufactures all three in 60 days more cheaply than K can earn them cold.

## The Integrated Plan (T1 + T2 merged)

The two rulings collapse into one coherent plan because they emphasize different parts of the same answer:

| Week | Build | Discovery | Calibration |
|------|-------|-----------|-------------|
| 1-2 | Heatmap-share-card prototype + first-pass topology check on ~20 topics | **Griffin posts manual worksheet diagnoses** to his existing Twitter audience (acceleration-tribe orbit). 2-3 case studies/week. No creator hire. | Topology verification on the topics that surface |
| 3-4 | Worksheet OCR (math 2-5, Beast/Eureka/enVision/Singapore) | Twitter cadence continues; first email captures | +30 topics topology-verified |
| 5-6 | OCR conversion-page polished for K-reframed framing ("prereq chain blocking ceiling expression") | **Week 4 kill gate**: median <300 views + zero captures + zero topic requests → escalate via `/dialectic-review`. Pass = continue | |
| 7-8 | Beta cohort of 10-30 acceleration-tribe parents using the heatmap | Twitter case studies → email captures → beta invites | Beta usage feeds OCR-to-topic mapping calibration |
| 9-12 | Layer 24Q + parent-polished radial on top | Existing warm users see the K-reframed radial as expansion | First real per-topic response data from beta cohort |

**Three things explicitly NOT in this plan:** (a) hiring an on-camera creator, (b) building Mrs. Johnson's teacher-side authoring flow, (c) the 4-6 week 50-150-kid recruitment sprint. All three are deferred to post-90-day reassessment, conditional on signal.

## Reversal Conditions (combined)

Revisit the plan if any of these fire:

1. **Week 4 signal-gate hits negative cleanly** (median <300 views + zero captures + zero topic requests on first 10 Twitter case studies). At that point the question isn't "content vs product" — it's whether OKG's parent-facing wedge is wrong entirely. Trigger `/dialectic-review --premortem` on the wedge itself.
2. **Twitter-acceleration-tribe traction fails by day 50** (8-12 case studies → <100 trial completions cumulative). Standing-capital thesis is wrong; fall back to runner-up (pure B + paid micro-experiments) or pause and reassess ICP.
3. **Beast/Eureka/enVision/Singapore OCR scope explodes past 5 weeks.** Either narrow further (Beast Academy only — highest-acceleration-density curriculum) or pivot to K-reframed cold and accept gatekeeping risk.
4. **Creator-hire shortcut materializes** (warm intro to a proven edu-acceleration creator in Griffin's Twitter orbit). TikTok-engine + B re-enters the analysis with the cold-start critique partially defused.
5. **Heatmap shows <2% organic share rate** across 200+ generated outputs. The structural claim of B (heatmap-as-shareable-trigger) is wrong; pivot test to radial-as-status-artifact (different share thesis: status/aspirational signaling, not insight).
6. **Edu-equity viral-negative event hits the radial.** Counter-K's political-risk point materializes; retreat to B-only.
7. **Competitor enters the exact wedge** (grades 2-5 math+reading with prereq-graph diagnosis). Empty-battlefield premise reverses; calibration-moat case strengthens; consider sprint.
8. **Griffin's creator-management bandwidth exceeds 25% of week** without paid hire being justified by signal. Don't let this become his first managerial role by accident.

## What Replaces the Original "Top 5"

The original top-5 ranking is superseded by the sequenced plan above. Of the original ideas:

- **B (worksheet OCR)** survives as the v1 build — but narrowed (4 curricula, math 2-5) and reframed (acceleration-tribe-legible copy)
- **A (diagnostic + radial)** survives as the days-60-90 expansion layer
- **K-reframed (radial-as-ceiling-finder)** survives as the *positioning* and the audience target, not as the cold-launch surface
- **N-defanged (IEP companion)** stays in the post-90-day backlog
- **D-narrowed (Mrs. Johnson)** is eliminated by the audience-mismatch and moat-demotion critiques
- **TikTok content engine** is deferred until 2026 cold-start signal exists or a creator-hire shortcut materializes
- **G (summer slide)** is naturally absorbed into the days-60-90 timing if the sequence holds (mid-May through early-June)
- **F (daily practice)**, C, E, H, J, L, M, O — all stay deferred per original synthesis

## Concrete Two-Day Move

Don't build OCR yet. Do this first:

1. **Pick 3 real worksheets** from Griffin's network (Madi's network, Addi's preK feeders, friends-of-friends with elementary kids — including at least one Beast Academy worksheet if reachable).
2. **Manually trace each missed problem** to its upstream broken-brick using the existing graph.
3. **Write three Twitter threads** in the K-reframed framing ("prereq chain blocking ceiling expression in [domain]"), one per worksheet, with a clean static image of the upstream-walk as the share artifact.
4. **Post one** as a real test, anonymizing the kid.
5. **Measure**: does it land in the acceleration-tribe Twitter orbit Griffin already inhabits? If three threads in two weeks produce ≥30 likes + ≥3 replies asking "where can I get this for my kid," the discovery thesis has signal and the OCR build is the right next step. If they die at <10 likes, the entire OKG-as-consumer-product thesis is in question and a `/dialectic-review --premortem` on the wedge should run before another build phase.

This is the cheapest possible falsification step. Two days of Griffin's time, no engineering, no hires, no commitments. It tests the load-bearing assumption (Twitter-acceleration-tribe is the discovery channel) before any code is written.
