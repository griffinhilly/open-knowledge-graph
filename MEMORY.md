# Open Knowledge Graph Memory

## Status (Mar 25, 2026)
- **13,429 topics** across **19 domains**, **197 courses** (34 courses registered this session)
- **6 developmental stages**: pre-formal, concrete-operations, abstract-reasoning, formal-systems, advanced, expert
- **All topics at `status: validated`**, **100% Q+E coverage**
- GitHub Pages: `griffinhilly.github.io/open-knowledge-graph/`
- Phase 9A COMPLETE, Phase 9B BUILT, Phase 8.5 (K-12 STEM) COMPLETE
- **Domain map v2 DONE**: All 19 domains portrait orientation. Course maps via `--course`.
- **Data quality pass DONE**: 447 deduped, 586 restaged, 85 refs fixed across 6 domains (CS, Physics, Biology, Earth & Space, Economics, Social Sciences)

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
- **Status**: All topics now `validated` as of Mar 23
- **Domain ordering**: Math → Formal Sciences → Philosophy → CS → Engineering → Physics → Earth & Space → Chemistry → Biology → Health → Psychology → Social Sciences → Economics → Practical Life → History → Language → Literature → Arts → Music
- **Validation approach**: Haiku for volume, Sonnet for review, Opus for decisions
- **Stage audit principle**: stage based on actual file content, not whether simpler version exists for younger learners
- **localStorage keys**: `okg-fluency`, `okg-fluency-conf`, `okg-fluency-meta`, `okg-goals`, `okg-adjustments`

## Domain Map Architecture (Mar 24, 2026)
- **Tier layout**: Courses grouped by developmental stage → tiers. Within-tier overlap ~50%, between-tier ~25%.
- **Branch X-positions**: Manual left-right axis per domain (e.g., math: discrete←→analysis). Stored in `COURSE_BRANCH_X` dict. Non-math mappings are AI-proposed, need human review.
- **Sizing**: `area ∝ degree`, out-degree weighted 2x. DEGREE_CEILING=25 for consistent sizing across views.
- **Row splitting**: 3x depth multiplier, recursive splitting (3 passes, cap 20 topics/row).
- **Centroid-anchored placement**: Each layer anchors on connected-neighbor centroid, then 10 rounds of 40% neighbor drift.
- **Radial integration plan**: Written in `tools/radial-branch-alignment.md`. Auto-detect branch flip from cross-domain edge lengths. Each domain's left-right axis should face its more-related angular neighbor.
- **Next**: Radial integration, leaf-connector swarm, replace regex YAML with PyYAML.

## Gotchas
- **Python f-string + JS templates**: `\'` inside f-string produces `'` not `\'`. Use `"'" +` concatenation instead.
- **Inline JSON size limit**: Browsers choke on 700KB+ single-line `<script>` data. Use `indent=1` for multi-line or external `.js` file.
- **Click-vs-drag in canvas views**: If two `mousemove` handlers share `dragStartX/Y`, track original position separately (`mouseDownX/Y`) for displacement detection.
- ~~**CI workflow gap**~~: FIXED (Mar 25). `deploy-pages.yml` now includes: validate → hierarchy → radial → topic pages → domain maps → assessment → quiz.
- **Dedup agents introduce cycles**: Batch find-and-replace during dedup can create mutual prerequisite references. Always run cycle detection after dedup swarms (Kahn's algorithm).
- **Dangling cross-domain refs**: 394 total across all domains (pre-existing, not from dedup). Mostly course names used as prereq IDs (`probability-and-statistics`, `macroeconomics`) instead of actual topic IDs. Doesn't affect domain maps (within-domain only).
- **Validation (Mar 25)**: 13,429 topics, 0 self-refs, 0 within-domain cycles, 394 cross-domain dangling refs (pre-existing). Graph is structurally clean after dedup.
- **_domain.yml indentation varies**: Math uses 2-space, physics uses 0-space for course entries. Regex parser needed `\s*` instead of fixed indent.
