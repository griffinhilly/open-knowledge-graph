# Initial-View Engagement + Usage Pathways — Ideation (Jun 10, 2026)

**Purpose**: Griffin asked for product improvements and usage-building pathways, with particular interest in making the initial view intuitive and engaging. This session ran a three-part audit (live-site cold-visit screenshots via headless Chrome, code-side map of all first-visit surfaces, web research on comparable knowledge-map products) and synthesized ranked ideas.

**Method**: 2 background agents (code explorer + web researcher) + headless-Chrome screenshots of live site (index/radial/quiz/sprout/topic, desktop + 390px mobile). ~10 min wall-clock.

**Relationship to the Apr 25 parent-acquisition plan**: this does NOT re-open that decision. The wedge plan targets parents via worksheet OCR and is paused on the 2-day Twitter test. Everything below targets general learners via *distribution* and *initial-view conversion* — compatible and orthogonal. Honest framing per MEMORY.md's base-rate finding ("feature-shipping has produced zero parent users"): Bucket B (distribution) creates traffic; Bucket A (initial view) converts traffic. Sequence accordingly — distribution first.

---

## Audit findings (facts, not opinions)

### Live-site cold-visit observations
1. **The wow asset is hidden.** Index is a clean text-card page; the radial map — the single most impressive thing the project owns — is behind a click. Hero = title + count + two equal CTAs.
2. **Radial cold-open is a modal ambush.** "Make this yours" stage card auto-shows on first visit and covers the center of the map. The first thing a new visitor is asked to do is configure, before they've seen anything. (Duolingo/Brilliant pattern is the opposite: value first, commitment later.)
3. **The map at rest zoom is unlabeled colored dust.** Domain labels only render at zoom ≥1.05; at default zoom the first view is beautiful but illegible. Stats box says "14,816 topics" while index hero says "16,951" (radial excludes practical-life-skills etc. — but a careful visitor sees an inconsistency).
4. **Search is the answer to graph paralysis and it's hidden** at bottom-center behind Ctrl+F discoverability.
5. **Mobile radial still has the header overlap** (controls row collides with title box at 390px); stage-card buttons clip off-screen.
6. **Sprout is genuinely warm** but at 390px the topic title and third response button ("Dunno") clip off the right edge.
7. **Quiz welcome is flat**: "Knowledge Trivia — pick how you want to play." No preview of the payoff (the personalized colored map), which is the actual reason to take it. 9.4 MB page load.
8. **Topic pages are content-rich but orphaned**: landing from a search engine, there's no "what is this site" context, no visual of where the topic sits in the graph, raw `a^2 + b^2 = c^2` (no math rendering). Buried gem: "Unlocks 6,206 downstream topics" — that's a hook line rendered as a gray caption.

### Code-side facts (Explore agent)
- **SEO is zero.** No meta descriptions, no og: tags, no canonical, no JSON-LD, no sitemap.xml, no robots.txt — across all ~17k pages. Titles exist. The radial is canvas (uncrawlable); topic pages are crawlable but undiscovered.
- Payloads: radial-graph.html 8.7 MB, quiz.html 9.4 MB, index 502 KB, js/graph.js 3.4 MB lazy.
- Topic pages: ~50–150 KB each, genuinely unique content (Core Idea, misconceptions, explainer, questions, prereq structure).

### Research findings (web agent)
- **Graph-as-hero is a documented failure mode**: Khan Academy retired its knowledge map (linear converted better for the median learner; Sal says it returns "with generative AI"); Obsidian's graph view = "more fun to look at than navigate"; Metacademy/learn-anything stagnated as "a library with no front desk."
- **What converts**: a concrete win in the first 5 minutes (Math Academy diagnostic-first; Brilliant puzzle-first); "you are here" anchor before full-scope exposure (OpenSyllabus search-first; Quanta's 3-node guided start); scroll-as-narrative for big reveals (neal.fun "The Deep Sea"); deferred commitment (Duolingo registers AFTER first lesson).
- **Post-2024 Google**: scaled template pages get deindexed; *rich-dataset differentiation* pages (unique structured data per page) rank. OKG's topic pages are the good kind — if they get metadata + sitemap.
- **roadmap.sh model**: 700k monthly users by being the link people paste when answering "what should I learn to become X." Requires linkable sub-graphs.
- **HN front page**: 10–40k uniques in 24h; needs a "wow" single-page entry, not "here's my graph."
- **schema.org LearningResource** has native fields for exactly what OKG has: `teaches`, `educationalLevel`, `competencyRequired` (prerequisites!).
- **FineWeb-Edu / HuggingFace**: structured CC-licensed educational data is exactly what training pipelines and researchers seek; dataset publication = second discovery surface.

---

## Bucket B — Usage pathways (distribution; do these first)

Ranked by effort-to-impact. These sidestep the "features produced zero users" base rate because they are not features.

### B1. SEO foundation sprint ⭐ top pick
One session, deterministic generator changes, zero product risk, compounds while the project is paused:
- Per-page `<meta name="description">` = first sentence of Core Idea (data already exists)
- `og:title` / `og:description` / `og:type` / canonical on all pages
- `sitemap.xml` generation in CI (~17k URLs) + `robots.txt`
- JSON-LD `LearningResource` per topic page: `teaches`, `educationalLevel` (stage), `competencyRequired` (hard prereqs), `isPartOf` (course) — the schema is a near-1:1 match for OKG's data model
- Target query class: "what do I need to know before learning X" / "prerequisites for X" — long-tail, low competition, exactly what these pages answer
- Effort: ~1 session. All in `generate_topic_pages.py` + a new sitemap step in CI.

### B2. "From counting to quantum field theory" explorable → the Show HN
One scroll-narrative page that walks the longest prerequisite chain in the graph (PLAN.md records chains up to 147 steps) — The Deep Sea pattern applied to knowledge. Scroll = ascend through the stages from kindergarten counting to QFT, with the radial lighting up the path as you go. This single page is the HN/Reddit submission — not the graph. The graph is where visitors land afterward.
- Effort: ~1–2 sessions; reuses graph data + radial render code.
- This is also the announcement post Phase 8 still owes.

### B3. Per-topic og:image social cards
Auto-generate share cards: topic title + mini prereq-chain graphic + "unlocks N topics" stat. Every pasted link becomes an ad. NCP's native-HTML/CSS-charts pipeline (headless Chrome render at build time) transfers directly.
- Effort: ~1 session for template + CI step; render time for 17k cards is the constraint — start with the ~1,000 hub topics.

### B4. Shareable subgraph URLs (roadmap.sh model)
`?focus=<topic-id>` on the radial: renders that topic's ancestry subtree highlighted, camera framed on it, clean URL to paste. Teachers/bloggers link "the statistics map." This is the embed/widget play in its cheapest form.
- Effort: ~1 session (camera + highlight logic mostly exists in search/panel code).

### B5. HuggingFace dataset publication
Export topics + edges + stages + questions as a structured dataset (CC BY-SA already). Dataset card frames it as the open prerequisite-structure corpus. Researchers cite, link back.
- Effort: half a session (export script + card).

### B6. Wikipedia external links (slow burn)
Only where genuinely additive; editors reject promo. Maybe 20–50 high-fit articles. Do after B1 (pages need to look credible when editors check).

## Bucket A — Initial view (conversion; cheap, do alongside)

### A1. Put the map on the index page
The course-level mini radial already exists (quiz results screen renders 162 course nodes on a canvas). Reuse it as a live hero behind/above the fold — full radial one click deeper. Index stops being a text page and becomes the map.
- Effort: ~half a session; code exists.

### A2. Search-first entry ("you are here" anchor)
Hero search box on index + radial: "What do you want to understand?" → fly-to topic + light its full prerequisite chain. Converts the hairball into an answer machine. This is the single highest-leverage intuitiveness change; OpenSyllabus pattern.
- Effort: ~1 session (search + camera exist; chain-highlight is A3).

### A3. One-click ancestry reveal
Clicking a node dims everything except its full prerequisite ancestry — the "what it takes to understand X" moment as a visual story instead of a side-panel list. Screenshot-able = shareable. Pairs with B4.
- Effort: ~half a session (BFS exists in fluency.js; render-side dimming is new).

### A4. De-ambush the radial cold-open
Stage card should not block the map center on first visit. Options: slim bottom-bar nudge, corner card, or show after first interaction (zoom/click). Value first, calibration second.
- Effort: small. Note: this partially re-opens 12A Step 2's "first-visit auto-show" — flag to Griffin rather than silently reverse (it was a deliberate 12A decision).

### A5. Domain labels at rest zoom
Legend or always-on labels so the first view isn't unlabeled dust.

### A6. Topic-page cold-landing upgrades
"Unlocks N topics" as a hero stat; small inline chain strip (prereqs → topic → successors); "See this on the map" button (→ B4 URL); one-line site context for search-engine arrivals. KaTeX or Unicode cleanup for `a^2` runs.
- Effort: ~1 session in `generate_topic_pages.py`; regenerates everything for free in CI.

### A7. Mobile fixes
Radial header overlap (known issue, confirmed live), stage-card clipping, Sprout title/third-button clipping at 390px.

### A8. Quiz welcome sells the payoff
Show a blurred/colored preview map: "24 questions → your map lights up like this." The payoff is visual; show it.

---

## Suggested sequencing

1. **B1 SEO sprint** (one session, compounds passively, zero risk)
2. **A6 + B3 together** (topic pages become both landing pages and share cards — same file, same session)
3. **A2 + A3 + B4** (search-first + ancestry reveal + shareable subgraphs — one coherent "answer machine" upgrade to the radial)
4. **B2 explorable** → Show HN launch moment (after the above so arrivals convert)
5. **A1, A4, A5, A7, A8** opportunistically alongside

Items NOT proposed: anything requiring accounts/backend (out of architecture), TikTok (Apr 25 finding stands), more content expansion (corpus isn't the constraint — distribution is).

## Data inconsistencies noticed (housekeeping)
- COMP files say 15,290 topics; live index says 16,951; radial says 14,816 (PLS exclusion explains part). COMP files appear stale relative to the deployed site — reconcile next /wrapup.
