# Domain Audit Results — March 25, 2026

Audits of the 6 domains with wide knowledge maps (W:H > 3.0).
Results will inform data quality improvements.

## Status
- [x] Economics — COMPLETE
- [x] Earth & Space — COMPLETE
- [x] Biology — COMPLETE
- [ ] Social Sciences — PENDING
- [ ] Computer Science — PENDING
- [ ] Physics — PENDING

## Cross-Cutting Findings

### 1. Missing courses from _domain.yml (FIXED)
All 6 domains had courses on disk not registered in _domain.yml.
Total: 34 courses, 2,973 topics (21% of graph). Fixed this session.

### 2. Massive duplication (NOT YET FIXED)
Every audited domain has significant topic duplication:
- Economics: ~190 duplicates (26% of domain)
- Earth & Space: ~50-70 duplicates
- Biology: ~30 duplicate pairs

### 3. Stage misassignment (NOT YET FIXED)
Topics staged incorrectly (too high or too low):
- Economics: ~50 topics need re-staging (many at formal-systems should be concrete/abstract)
- Biology: 99 stage violations (topics staged below their prereqs)
- Earth & Space: Missing the `advanced` stage entirely (jumps formal→expert)

### 4. Missing prerequisite edges (NOT YET FIXED)
Shallow within-course chains are the primary cause of wide layouts:
- Economics: 42% of topics are leaves (nothing depends on them)
- Earth & Space: 41% leaves
- Biology: similar pattern

## Per-Domain Summaries

### Economics
- **Dedup**: ~190 topics removable (721→530). Worst: development-economics (85→50), advanced-micro (100→60)
- **New course**: `principles-of-economics` (concrete-operations/abstract-reasoning) — pull intro topics from micro/macro
- **Re-stage**: ~10 topics to concrete-ops, ~10 to abstract-reasoning, ~30 dev-econ from expert→advanced
- **Missing topics**: Labor economics, public finance, industrial organization, economic history, environmental economics

### Earth & Space
- **Dedup**: ~50-70 topics removable (712→645). Cross-course duplicates especially in climate/ocean
- **Re-stage**: ~60-80 topics to fill missing `advanced` stage (currently jumps formal→expert)
- **Missing topics**: Natural hazards, remote sensing, GIS, mass extinctions, tsunamis, atmospheric chemistry
- **Course structure**: 9 courses (after fix) are sufficient, no splits needed

### Biology
- **Dedup**: ~30 pairs (1004→974). Cross-course overlap in genetics/cell-bio and ecology/evo-bio
- **Re-stage**: 99 stage violations. ~15 biochem topics advanced→formal, ~13 evo-bio advanced→formal, ~10 neuro expert→advanced
- **Missing topics**: Stem cells, CRISPR, DNA structure, embryology, biomes, microbiome, prions
- **Course structure**: 11 courses (after fix) sufficient. Consider splitting life-science into foundations + advanced

## Next Steps
1. Deduplication swarm (CS-style dedup pipeline for each domain)
2. Stage re-assignment audit
3. Missing prerequisite edge additions
4. Missing topic generation
