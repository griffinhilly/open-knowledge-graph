# Open Knowledge Graph Memory

## Status (Mar 21, 2026)
- **13,518 topics** across **19 domains**, **149 courses**, **29,609 prerequisite edges**
- **~13,260 topics** have Explainer sections (overnight Sonnet swarm, Mar 16)
- **~11,100 topics** have Questions sections (82% coverage — 1,006 from hub Q+E run + ~10,100 from Q5 swarm Mar 21)
- **20,531 tag pages** generated; tags are clickable on topic pages
- GitHub Pages: `griffinhilly.github.io/open-knowledge-graph/`
- **All graph views fully interactive** on desktop and mobile (Mar 18 fix)
- **Phase 9A COMPLETE**: Fluency model implemented and wired into all views
- **Domain ordering finalized**: formal foundations → physical sciences → life sciences → social sciences → humanities

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
- **Questions schema**: YAML-in-code-block inside `## Questions`. 3 questions per topic (MC, T/F, short-answer)
- **Explainer schema**: Freeform markdown in `## Explainer`. 3-5 paragraphs teaching the concept
- **Tag pages**: Separate HTML pages per tag, grouped by domain. Tag names slugified for filenames
- **Questions on separate pages**: `{topic-id}-questions.html` with interactive scoring
- **Pre-commit hook**: `domains/` and `output/` paths whitelisted
- **localStorage key contract**: `okg-fluency`, `okg-fluency-meta`, `okg-goals`, `okg-adjustments`
- **Domain ordering**: Math → Formal Sciences → Philosophy → CS → Engineering → Physics → Earth & Space → Chemistry → Biology → Health → Psychology → Social Sciences → Economics → Practical Life → History → Language → Literature → Arts → Music
- **Applied Rationality placement**: Philosophy (3-agent dialectic)
- **Validation approach**: Haiku for volume, Sonnet for review, Opus for decisions. Dialectic 1-1-1 for manual cases. Content quality is high; structural fixes are bulk-scriptable.
