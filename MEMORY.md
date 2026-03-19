# Open Knowledge Graph Memory

## Status (Mar 19, 2026)
- **13,518 topics** across **19 domains**, **149 courses**, **29,609 prerequisite edges**
- **~13,260 topics** have Explainer sections (overnight Sonnet swarm, Mar 16)
- **1,006 topics** have Questions sections (hub topics from earlier Q+E run)
- **20,531 tag pages** generated; tags are clickable on topic pages
- GitHub Pages: `griffinhilly.github.io/open-knowledge-graph/`
- Project moved to `C:\Users\griff\Projects\griffin\open-knowledge-graph\`
- **All graph views fully interactive** on desktop and mobile (Mar 18 fix)
- **Phase 9 planned**: Learning platform overhaul (fluency model, assessment redesign, semantic zoom, learning paths)
- **Applied Rationality** course added under Philosophy (30 topics, Mar 19)
- **Domain ordering finalized**: swapped Earth & Space ↔ Chemistry. Narrative: formal foundations → physical sciences → life sciences → social sciences → humanities

## Hierarchy Graph TDZ Bug (Mar 18)
- Both per-domain and full hierarchy templates had `let hoveredNode` declared AFTER the initial `draw()` call, but `draw()` references `hoveredNode` in highlight logic. This temporal dead zone error silently crashed the script, preventing ALL event handlers from registering. The graph rendered via the CSS background but was completely non-interactive.
- **Diagnostic**: `node --check` found no syntax errors; had to run the JS with a DOM mock (`new Function(js)()`) to catch the runtime `ReferenceError`.
- **Fix**: Move `let hoveredNode = null` before `draw()`.
- Also fixed: duplicate mousemove handlers (dragMoved never set), pinch-to-zoom drift (missing anchor math), course name `.title()` capitalizing digits ("1St" → "1st").

## Overnight Content Generation (Mar 15-16)
- **Explainer swarm**: 30 Sonnet workers, batch_size=10, parallel shards. Completed ~13,260/13,489.
- **Shard 22 checkpoint corruption**: 0-byte file caused worker crash. Reset manually.
- **Questions generation**: manifests ready (`questions-shard-*.json`), prioritized by hub connectivity + younger developmental stages. Waiting for token limit reset (Saturday Mar 21). Launch: `bash tools/overnight/run-parallel.sh questions`

## Phase 9 Assessment Redesign (Mar 19, 2026)
- **Fluency model**: Continuous 0-100 score per topic (not tri-state). Bayesian updating on log-odds scale — sigmoid naturally emerges. Stored in localStorage as integer percentages, only non-zero topics stored.
- **Prerequisite propagation**: Backward (mastery of successor implies ~0.85^hops fluency on prerequisites) and forward (low fluency on prerequisite caps successors). ~100 well-chosen questions can inform ~1000+ topic fluencies.
- **Assessment uses actual questions** (MC, T/F) from question bank — NOT self-report familiarity like current assessment. Eliminates anxiety about misrepresenting knowledge.
- **Silent response time tracking**: Fast correct = strong evidence, slow correct = moderate, fast wrong = likely misclick (low penalty), slow wrong = genuine gap. Never shown to user.
- **Asymmetric updates**: Wrong answers penalized at 0.7× relative to correct answers. Structurally harder to lose fluency than gain it. Makes assessment feel generous.
- **Three phases**: (1) Warm-up: pre-formal→concrete, rapid-fire, cross-domain rotation, MC/TF only. (2) Exploration: abstract→formal, adaptive per domain, "something different" escape hatch. (3) Deep Dive: optional, user-selected domains, rigorous, short-answer included.
- **"Complete assessment" available at every point** — shows best estimate of personalized graph + frontiers.
- **Post-assessment**: User sees fluency-colored radial graph, domain summary cards with course-level breakdowns, manual adjustment sliders for perceived mismatches.
- **"Skip this domain"** button to dismiss uninterested domains entirely (dimmed, excluded from frontier).
- **Landing experience**: Radial graph as-is (beautiful, expansive) → "Explore the Map" or "Personalize Your Map" → assessment. "Show Domains" toggle reduces dot graph to labeled domain nodes.
- **Math Academy inspiration**: % fluency per topic, frontier = topics with high prerequisite fluency but low own fluency, visual green wave of mastery propagating through graph.
- **Implementation phases**: A (fluency model + localStorage + graph coloring) → B (assessment phases 1-2) → C (assessment phase 3 + results) → D (landing page + domain toggle + progress bars + polish).

## Decisions
- **Format**: Markdown + YAML frontmatter (one file per topic)
- **License**: CC BY-SA 4.0 for content, MIT for tools
- **GitHub Pages**: Preferred deployment method; generated HTML stays out of git
- **New topic status**: `draft` until reviewed; original topics remain `validated`
- **Questions schema**: YAML-in-code-block inside `## Questions`. 3 questions per topic (MC, T/F, short-answer)
- **Explainer schema**: Freeform markdown in `## Explainer`. 3-5 paragraphs teaching the concept
- **Tag pages**: Separate HTML pages per tag, grouped by domain. Tag names slugified for filenames
- **Questions on separate pages**: `{topic-id}-questions.html` with interactive scoring, not cluttering topic page
- **Pre-commit hook**: `domains/` and `output/` paths whitelisted — biology "secretion" topics are not secrets
- **localStorage key contract**: `okg-fluency` (topic→score map), `okg-fluency-meta` (assessment metadata), `okg-goals` (starred target topics), `okg-adjustments` (manual course-level overrides)
- **Domain ordering** (clockwise on radial graph): Math → Formal Sciences → Philosophy → CS → Engineering → Physics → Earth & Space → Chemistry → Biology → Health → Psychology → Social Sciences → Economics → Practical Life → History → Language → Literature → Arts → Music. Decided via 8-agent dialectic (Mar 19). Only change from original: Earth & Space ↔ Chemistry swap. Gains Bio↔Chem (180 edges) and Earth↔Physics (190 edges) adjacency.
- **Applied Rationality placement**: Philosophy (not Psychology or Formal Sciences). Decided via 3-agent dialectic: normative character of content is the deciding factor (scored 8/10 Philosophy vs 5/10 Psychology vs 3/10 Formal Sciences).
