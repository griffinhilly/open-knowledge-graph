# Open Knowledge Graph Memory

## Status (Mar 14, 2026)
- **13,489 topics** across **19 domains**, **148 courses**, **13,314 prerequisite edges**
- GitHub repo: `griffinhilly/open-knowledge-graph` (public)
- GitHub Pages: `griffinhilly.github.io/open-knowledge-graph/` (auto-deployed via Actions)
- Original 2,628 topics at status: **validated**; ~10,861 expansion topics at status: **draft**

## Topic Expansion (Mar 13-14)
Overnight autonomous runner expanded topics from ~2,628 to 13,489 across all 19 domains (148 courses).
169/170 tasks completed successfully. Cross-domain prerequisite links added for all domains.

## Decisions
- **Format**: Markdown + YAML frontmatter (one file per topic)
- **License**: CC BY-SA 4.0 for content, MIT for tools
- **GitHub Pages**: Preferred deployment method; generated HTML stays out of git
- **Expansion strategy**: Research → plan → parallel generation agents → validate → commit
- **New topic status**: `draft` until reviewed; original topics remain `validated`
