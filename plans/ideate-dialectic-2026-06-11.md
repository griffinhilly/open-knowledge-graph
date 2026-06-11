# Ideate Dialectic — Initial-View Engagement + Usage Pathways (Jun 11, 2026)

**Process**: `/dialectic-review --ideate`, 5 generators (lenses: first-visit UX, virality mechanics, learning science, open-data ecosystem, wildcard) → 2 challengers → 3 synthesizers, all Opus. Seeded by `plans/initial-view-and-usage-ideas-2026-06-10.md` (the "ranked plan", items A1–A8 / B1–B6) with instructions to go beyond it. Constraints held fixed: no backend/accounts, no TikTok, SEO sprint + stage-card reversal already shipped, parent-acquisition out of scope.

**Volume**: 25 ideas generated → 21 after dedup → 2 STRONG/STRONG survivors + 1 disputed high-ceiling + ~6 conditional → 3 synthesizers converged on a small BUILD tier + sequencing that preserves the existing plan's spine.

## Cross-cutting constraints (both challengers, all synthesizers adopted)

1. **Base-rate filter is the master discriminator**: distribution artifacts (things that travel — lists, links, search results, calendar files) escape the "6 months of features → zero users" trap; pure features don't. Rank accordingly.
2. **Edge quality gates headline claims**: any artifact putting a computed path/distance/count in a headline needs its slice edge-audited first (8% of edges violate stage ordering; 2,325 edges). BUT the audit is bounded, not a crisis — Cut-6 QA flip rate was 0.7%, and a top-50 slice audit is ~an hour of agent work.
3. **localStorage can't aggregate**: every social/crowd/tally/duel mechanic silently degrades to single-player on a static site. Several generated ideas designed for a backend that doesn't exist.
4. **Self-report stays display-only** (Phase 12A `getEffectiveScore` discipline) — declared-knowledge inputs must never write to the Bayesian fluency store.
5. **Consolidate, don't add on-ramps**: 21 ideas collapsed into ~5 engines; funnel sprawl is a named failure mode for a solo builder.

## BUILD tier (3/3 synthesizer convergence)

1. **Keystone leaderboard** — "The 50 most powerful things to learn," ranked by transitive-successor count (data already computed). Static page + og:image. The cheapest distribution artifact on the board; roadmap.sh-shaped; candidate Show HN asset by itself. First step: edge-audit the top ~80 candidates, decide hub-bias handling explicitly (raw-with-stated-methodology vs per-domain cap — state the methodology on the page either way).
2. **ONE path engine, several surfaces** — consolidates ideas #1 (bridge-path query) + #7 (six-degrees gallery) + #21-lite (single-player puzzle) with the plan's A2 (search-first) + A3 (ancestry reveal) + B4 (shareable subgraphs). Build one BFS/camera/highlight engine. **Hard gate: explicit no-path fallback** (the graph is a forest of DAGs — most arbitrary pairs don't connect; the fallback UX is the feature, not an edge case). Ship order within the cluster: A3 ancestry (always answerable) → A2 search entry → B4 share URLs → curated, edge-audited counterintuitive-pairs gallery.
3. **Comeback Card (.ics)** — calendar event at a next-review date with a deep link back to a review session. The only push channel a static site can own; net-new vs the plan. Caveats: the fluency model is Bayesian, NOT an SRS — interval logic must be built (deliberately dumb expanding intervals, e.g. 3d/1w/3w); copy says "reminder," never "optimal"; scheduling logic must not write into the Bayesian store. Retention-class → build post-launch.
4. **(From the existing plan, reaffirmed)** B3 og:image cards + A6 topic-page cold-landing upgrades ship FIRST (same file/session; every artifact above lands on these pages), B2 "counting → QFT" explorable remains the Show HN launch moment and must not fire before the pages convert.

## Consensus implementation order

1. B3 og:image (hub topics first) + A6 topic-page upgrades — the substrate every share artifact lands on
2. Keystone leaderboard (+ shared precomputed stats table that later share artifacts reuse)
3. Path-engine cluster (A3 → A2 → B4 → curated gallery)
4. B2 explorable → **Show HN launch** (with #10's .ics built just before, so the spike has a return channel)
5. Post-launch, fueled by the first cohort: daily ritual, frontier mirror, reframed share-stat card, Markdown/Obsidian export, B5 dataset + JSON dump + llms.txt
6. Embeddable widget only when someone actually asks to embed

## EXPLORE tier (gating question each)

- **Daily ritual, Variant B "Prerequisite Detective"** (date-seeded Wordle-style) — the one genuine challenger disagreement (dead-without-users vs highest-viral-ceiling). Resolution: build the deterministic solvability/anti-degenerate-day checker first; ship only after the launch produces a cohort. Highest ceiling among no-backend options.
- **"Prerequisites for the news"** evergreen explainer layer (~10–20 concepts: CRISPR, transformers, QE…) — gate: 1-hour corpus-coverage check. Synthesizer 2 wildcard-elevated it: the only idea riding exogenous demand rather than manufacturing interest; possibly the highest-ROI distribution artifact if coverage passes.
- **Ego-number share card** — mechanic good, stat fragile; gate: find the defensible reframe ("N topics across M domains," never "% of human knowledge").
- **Frontier mirror** (pick #20 over #4; both are the same declare→frontier primitive) — gate: strictly display-only inputs; fueled by a hand-curated landmark-topic list (the honest version of "prestige").
- **Exports** — Markdown/Obsidian is near-BUILD plumbing; Anki .apkg is a hidden-complexity trap (SQLite-packed format) needing a separate spike.
- **Static JSON dump + llms.txt + B5 HuggingFace** — cheap plumbing track, one export logic, run opportunistically. No stability promises.

## PARK tier (one line each)

- Binary-search frontier finder — monotonicity is false on a branching DAG; existing adaptive assessment already serves the goal.
- Hosted MCP server — violates the no-backend constraint (llms.txt fragment survives in the plumbing track).
- Public-commitment goal URL — the "public" is illusory (recipient can't see sharer's localStorage); it's B4 relabeled.
- Argument-bait tally — localStorage tally is theater; see wildcard salvage below.
- Two-player duel — blind guessing over a 15k-node graph + no shared state; single-player version is absorbed by the path engine/daily ritual.
- Fork-my-path — "fork" implies a social store that doesn't exist; harvest the "named curriculum" card framing into B4.
- Curiosity-gap teasers — "prestige" signal doesn't exist in the data; landmark list feeds the frontier mirror instead.
- Retrieval-practice landing — bounce-vs-dwell risk on exactly the SEO traffic it's meant to convert; revisit as an A/B inside A6 with real data.
- Misconception cold-open at scale — misconception quality never audited (Phase 10 audited Questions); curated-subset index card + per-page placement survive as A6 riders.
- Scroll-silhouette — lost the frontier-surface contest to the mirror; funnel sprawl.
- Embeddable widget — strongest compounding mechanic but chicken-and-egg; deferred until sharing demand is evidenced.

## Synthesizer wildcards (three different picks — all worth holding)

- **S1**: the *job* of the killed binary-search finder — "stranger gets a personalized 'here's your edge' in 60 seconds" — is the missing front door; deliver it by re-skinning the EXISTING adaptive assessment (Bayesian propagation + max-information-gain question picking), not bisection. Nothing in the BUILD tier currently gives a cold visitor a concrete win in minute one.
- **S2**: the news-prerequisites layer may outrank the keystone leaderboard (exogenous demand vs manufactured interest) — give it the coverage spike before relegating it.
- **S3**: the GitHub-issue funnel killed as "argument-bait" is actually a **data-quality flywheel** — "this prerequisite looks wrong → file an issue" turns disagreeing visitors into the distributed edge-audit workforce that ideas 1–2 depend on. Nearly free; reframe as data integrity, not engagement.

## Disagreements preserved (valuable ambiguity)

- **Daily ritual timing**: challenger split (DOA-at-zero-users vs Wordle-bootstrapped-from-zero); synthesizers unanimously resolved to "explore now, ship post-launch" — but if the Show HN spike lands, this is the first thing to fire while attention is hot.
- **Where the "first 5 minutes win" lives**: S1 says the BUILD tier is all passive/search-driven and lacks an active cold-open win (his wildcard); S2/S3 implicitly accept search + leaderboard as sufficient. Open product question for Griffin.
- **News layer rank**: EXPLORE (S1, S3) vs possible-top-ROI (S2).

## Reconciliation notes

- All sequencing assumes B1 (SEO) shipped Jun 11 — **the gating manual action is Griffin submitting sitemap.xml to Google Search Console** (project-page robots.txt is not read by crawlers).
- Any share artifact printing a topic count must use the reconciled 15,290 (the 16,951 inflation was fixed Jun 11).
