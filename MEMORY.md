# Open Knowledge Graph Memory

## Status (Mar 21, 2026)
- **13,518 topics** across **19 domains**, **149 courses**, **29,609 prerequisite edges**
- **~13,260 topics** have Explainer sections (overnight Sonnet swarm, Mar 16)
- **~13,505 topics** have Questions sections (99.9% coverage — Q5 swarm + retry pass Mar 21)
- **20,531 tag pages** generated; tags are clickable on topic pages
- GitHub Pages: `griffinhilly.github.io/open-knowledge-graph/`
- **All graph views fully interactive** on desktop and mobile (Mar 18 fix)
- **Phase 9A COMPLETE**: Fluency model implemented and wired into all views
- **Phase 9B BUILT**: Quiz engine with adaptive tier warmup, exploration, post-assessment inference, confidence tracking
- **Domain ordering finalized**: formal foundations → physical sciences → life sciences → social sciences → humanities

## Stage Assignment Audit (Mar 21, 2026)
- **~274 potentially mis-staged topics** across 23 of 149 courses (~2%)
- Pattern: university-level courses have some topics stuck at abstract-reasoning or below
- **High-confidence fixes needed (~120 topics, 6 courses)**:
  - `computer-science/theory-of-computation`: 32 topics (abstract-reasoning → advanced)
  - `biology/cell-biology`: 26 topics (22 abstract + 4 concrete → formal/advanced)
  - `psychology/research-methods-psychology`: 23 topics (abstract → formal/advanced)
  - `earth-and-space-sciences/oceanography`: 17 topics (abstract → advanced)
  - `physics/thermodynamics`: 4 topics (concrete → formal) — ideal-gas-law already fixed
  - `mathematics/1st-grade`: 5 topics (abstract → concrete/pre-formal)
- **Medium-confidence (~60 topics)**: microeconomics, historical-methods, political-philosophy
- **Debatable (~90 topics)**: logic, public-speaking, ancient-civilizations, music fundamentals
- 11 physics topics already fixed this session (10 electrodynamics + 1 thermodynamics)
- Root cause: Sonnet swarm's systematic weakness is stage assignment for topics whose concepts appear at multiple education levels

## Phase 9B Design Decisions (Mar 21, 2026)
- **Adaptive tier warmup**: 3 questions per stage × 5 tiers, always escalates (never stops on easy misses). Domain-specific trivia at low tiers shouldn't block seeing harder questions.
- **Post-assessment inference model**: Overall "academic tier" estimated from highest stage demonstrated in 2+ domains. General-ed domains get universal floors; specialized domains (music, arts, engineering, philosophy, formal-sciences) only infer from direct evidence.
- **Confidence per topic**: 0-1 scale. First direct answer = 0.45 (inference can override), two answers = 0.70 (locked). Inferred topics get 0.1-0.5 confidence.
- **localStorage key**: `okg-fluency-conf` added alongside existing `okg-fluency`
- **Quiz is self-contained**: fluency.js + question data + topic index all embedded in quiz.html (~1.4 MB)
- **Griffin feedback**: MC questions test test-taking ability as much as knowledge. Short-answer (Phase 9C) will give more accurate readings. Assessment should estimate "brain tier" quickly, not grind through domain-specific trivia.

## Full-Coverage Validation Audit (Mar 19, 2026)
- **50 Haiku agents** validated all 11,035 draft topics across 50 batches
- **4 Sonnet agents** filtered false positives and identified systematic patterns
- **Opus referee** ran 1-1-1 dialectic reviews for 48 manual-review cases (geology prereqs, music staging, anatomy prereq direction)
- **Result**: 97.5% raw pass rate → 98.7% after false positive filtering. Zero factual errors — all issues were structural (stage labels, prereq direction)
- **Fixes applied**: 5,979 stage inversions (cascading), 198 bidirectional pairs, 129 orphan/island connections, 25 shallow topics expanded, 6 TODO placeholders filled, 13 geology prereqs removed, 3 music topics restaged, 2 anatomy prereqs inverted, 1 non-ASCII ID normalized, 1 dangling prereq fixed
- **Overnight generation quality insight**: Sonnet's content accuracy is excellent; the systematic weakness is stage assignment (abstract-reasoning vs formal-systems vs advanced) and cross-domain prerequisite ID matching

## Decisions
- **Format**: Markdown + YAML frontmatter (one file per topic)
- **License**: CC BY-SA 4.0 for content, MIT for tools
- **GitHub Pages**: Preferred deployment method; generated HTML stays out of git
- **New topic status**: `draft` until reviewed; original topics remain `validated`
- **Questions schema**: YAML-in-code-block inside `## Questions`. 3-5 questions per topic (MC, T/F, short-answer)
- **Explainer schema**: Freeform markdown in `## Explainer`. 3-5 paragraphs teaching the concept
- **Tag pages**: Separate HTML pages per tag, grouped by domain. Tag names slugified for filenames
- **Questions on separate pages**: `{topic-id}-questions.html` with interactive scoring
- **Pre-commit hook**: `domains/` and `output/` paths whitelisted
- **localStorage key contract**: `okg-fluency`, `okg-fluency-conf`, `okg-fluency-meta`, `okg-goals`, `okg-adjustments`
- **Domain ordering**: Math → Formal Sciences → Philosophy → CS → Engineering → Physics → Earth & Space → Chemistry → Biology → Health → Psychology → Social Sciences → Economics → Practical Life → History → Language → Literature → Arts → Music
- **Applied Rationality placement**: Philosophy (3-agent dialectic)
- **Validation approach**: Haiku for volume, Sonnet for review, Opus for decisions. Dialectic 1-1-1 for manual cases. Content quality is high; structural fixes are bulk-scriptable.
