# Open Knowledge Graph Memory

## Status (Mar 22, 2026)
- **13,991 topics** across **19 domains**, **163 courses** (14 new K-12 courses)
- **6 developmental stages**: pre-formal (204), concrete-operations (813), abstract-reasoning (1,266), formal-systems (7,206), advanced (1,840), expert (2,662)
- **100% Q+E coverage**: All topics have Questions + Explainer sections
- GitHub Pages: `griffinhilly.github.io/open-knowledge-graph/`
- Phase 9A COMPLETE, Phase 9B BUILT, Phase 8.5 (K-12 STEM) COMPLETE

## 6-Stage Schema (Mar 22, 2026)
- **Added "expert" stage** for graduate/research content (2,662 topics)
- **Broadened formal-systems** to include standard undergraduate curriculum (not just mathematical proof)
- **Stage criteria**: stage = where content is typically first encountered, not difficulty ceiling
- **Audit pipeline**: Haiku swarm (10 agents) → Opus referees (3 agents) for debatable cases
- Key referee decisions:
  - CS programming fundamentals: kept at abstract-reasoning (programming taught to middle schoolers)
  - Computability & complexity: split 47/51 (standard ToC → formal-systems, advanced complexity stays)
  - Physics QM: Griffiths ch1-3 stays formal-systems, Bell's theorem → advanced

## K-12 STEM Expansion (Mar 22, 2026)
- **473 new topics** across 14 courses in 7 domains
- Physics: Physical Science (40) + Conceptual Physics (40)
- Chemistry: Properties of Matter (36) + Introductory Chemistry (35)
- Biology: Living Things (40) + Life Science (40)
- Earth & Space: Earth & Weather (37) + Earth Science (35)
- Health: My Body (30) + Health Foundations (30)
- Engineering: Design & Build (30) + Engineering Principles (30)
- Formal Sciences: Patterns & Logic (25) + Reasoning & Proof (25)

## Decisions
- **Format**: Markdown + YAML frontmatter (one file per topic)
- **License**: CC BY-SA 4.0 for content, MIT for tools
- **GitHub Pages**: Preferred deployment; generated HTML stays out of git
- **Status**: `draft` until reviewed; original 2,628 at `validated`
- **Domain ordering**: Math → Formal Sciences → Philosophy → CS → Engineering → Physics → Earth & Space → Chemistry → Biology → Health → Psychology → Social Sciences → Economics → Practical Life → History → Language → Literature → Arts → Music
- **Validation approach**: Haiku for volume, Sonnet for review, Opus for decisions
- **Stage audit principle**: stage based on actual file content, not whether simpler version exists for younger learners
- **localStorage keys**: `okg-fluency`, `okg-fluency-conf`, `okg-fluency-meta`, `okg-goals`, `okg-adjustments`
