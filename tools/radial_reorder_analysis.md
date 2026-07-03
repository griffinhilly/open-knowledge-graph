# Radial Domain Reorder Analysis

**Date**: 2026-03-29
**Status**: Analysis only (no code changes)

## 1. How Domain Ordering Works

The radial layout in `tools/visualize_radial.py` uses a simple Python list:

```python
DOMAIN_ORDER = [
    "mathematics",                    # 0
    "formal-sciences-and-logic",      # 1
    "philosophy",                     # 2
    "computer-science",               # 3
    "engineering",                    # 4
    "physics",                        # 5
    "earth-and-space-sciences",       # 6
    "chemistry",                      # 7
    "biology",                        # 8
    "health-and-human-development",   # 9
    "psychology",                     # 10
    "social-sciences",                # 11
    "economics",                      # 12
    "practical-life-skills",          # 13
    "history",                        # 14
    "language-and-communication",     # 15
    "literature",                     # 16
    "arts-and-aesthetics",            # 17
    "music",                          # 18  (wraps to mathematics)
]
```

Angular sectors are **proportional to topic count**, so larger domains get wider wedges. A 1.2-degree gap separates each sector. The ordering is circular (music wraps back to mathematics).

Branch X-positions (`COURSE_BRANCH_X` in `visualize_domain_map.py`) define left-right sub-placement within each sector. Branch flips are auto-computed per domain to minimize cross-domain edge lengths within a 3-domain angular window.

### Files that would need updating

| File | What changes |
|------|-------------|
| `tools/visualize_radial.py` | `DOMAIN_ORDER` list (line 56) |
| `tools/visualize_hierarchy.py` | Independent `DOMAIN_ORDER` list (line 73, different ordering) |
| `tools/generate_quiz_page.py` | JS `DOMAIN_ORDER` array (line 678) |
| `tools/diagnose_radial_order.py` | Imports `DOMAIN_ORDER` from `visualize_radial.py` (no change needed) |
| `tools/diagnose_positioning.py` | Imports `DOMAIN_ORDER` from `visualize_radial.py` (no change needed) |
| `tools/trace_topic.py` | Imports `DOMAIN_ORDER` from `visualize_radial.py` (no change needed) |

Note: `visualize_hierarchy.py` has its own independent DOMAIN_ORDER that is already different from the radial one. It uses a different layout (grid, not radial), so changes there are optional.

## 2. Stage Distributions

| Domain | pre-formal | concrete-ops | abstract-reas | formal-sys | advanced | expert | Total |
|--------|-----------|-------------|--------------|-----------|---------|--------|-------|
| **practical-life-skills** | 0 | 94 (20%) | 262 (55%) | 118 (25%) | **0** | **0** | 474 |
| **health-and-human-dev** | 15 (3%) | 36 (6%) | 16 (3%) | 256 (44%) | 215 (37%) | 42 (7%) | 580 |
| **economics** | 0 | 4 (1%) | 10 (2%) | 302 (48%) | 180 (29%) | 129 (21%) | 625 |
| **history** | 0 | 0 | 19 (3%) | 480 (80%) | 80 (13%) | 23 (4%) | 602 |
| **psychology** | 0 | 0 | 0 | 437 (66%) | 125 (19%) | 98 (15%) | 660 |
| **social-sciences** | 0 | 4 (1%) | 64 (13%) | 261 (54%) | 132 (27%) | 25 (5%) | 486 |

Key observation: Practical Life Skills is the **only domain with zero topics beyond formal-systems**. Its entire content lives in the inner 3 radial bands (concrete-operations through formal-systems). Health, by contrast, has 44% at formal-systems, 37% advanced, and 7% expert --- filling the outer rings.

## 3. Cross-Domain Edge Analysis

### Current adjacency pairs (edge weights)

| Pair | Cross-domain edges |
|------|--------------------|
| math -- formal-sciences | 252 |
| formal-sciences -- philosophy | 150 |
| philosophy -- CS | 6 |
| CS -- engineering | **0** |
| engineering -- physics | 135 |
| physics -- earth-space | 182 |
| earth-space -- chemistry | 98 |
| chemistry -- biology | 176 |
| biology -- health | **399** |
| health -- psychology | 13 |
| psychology -- social-sciences | **0** |
| social-sciences -- economics | 7 |
| **economics -- practical-life** | **0** |
| **practical-life -- history** | **0** |
| **history -- language** | **0** |
| language -- literature | 217 |
| literature -- arts | 11 |
| arts -- music | **0** |
| music -- math (wrap) | 172 |

Six adjacency pairs have zero cross-domain edges. Three of these involve practical-life-skills or history.

### Each domain's cross-domain edge profile

**Practical Life Skills** (249 total cross-domain edges):
- mathematics: 248 (99.6%)
- language-and-communication: 1

Practical-life-skills is an extreme outlier: virtually all its cross-domain edges point to mathematics (financial literacy depends on arithmetic/algebra). It has **zero edges** to any of its current neighbors (economics, history) and zero edges to health.

**Economics** (286 total):
- mathematics: 277 (97%)
- social-sciences: 7
- health: 2

Also overwhelmingly math-dependent.

**History** (5 total):
- literature: 4
- arts: 1

Very few cross-domain edges at all. History is largely self-contained.

**Health** (442 total):
- biology: 399 (90%)
- chemistry: 26
- psychology: 13
- economics: 2
- mathematics: 2

Health's dominant connection is to biology (its current left neighbor). The right-side neighbor matters much less.

## 4. Ordering Cost Analysis

Using a weighted cost metric: sum of (edge_count x angular_distance) across all cross-domain pairs.

**Current ordering cost: 13,588**

### Brute-force search (all 720 permutations of the 6-domain middle segment)

Holding the STEM core (math through biology) and humanities tail (language through music) fixed, permuting {health, psychology, social-sciences, economics, practical-life, history}:

| Rank | Ordering (middle segment) | Cost | vs. Current |
|------|--------------------------|------|-------------|
| **1** | health, psych, **history**, social, practical, economics | **12,836** | **-5.5%** |
| 2 | health, psych, **history**, practical, social, economics | 12,852 | -5.4% |
| 3 | health, psych, **history**, social, economics, practical | 12,855 | -5.4% |
| 4 | health, psych, **history**, practical, economics, social | 12,901 | -5.1% |
| 5 | health, psych, **history**, economics, social, practical | 12,904 | -5.0% |
| ... | ... | ... | ... |
| Current | health, psych, social, economics, practical, history | 13,588 | baseline |
| Worst | economics, practical, social, history, psych, health | 17,329 | +27.5% |

**Every single top-10 ordering starts with health-psychology and has history in position 3** (right after psychology). This is because psychology has no direct cross-domain edges to social-sciences (0 edges), while history also has very few, so the cost function is indifferent between them --- but pushing economics and practical-life further from math (toward the tail end) is expensive.

### Orderings satisfying the user's constraints (practical adj. health AND economics adj. history)

| Rank | Ordering | Cost | vs. Current |
|------|----------|------|-------------|
| Best constrained | psych, health, practical, **history, economics**, social | 13,365 | -1.6% |
| 2nd constrained | **health, practical**, psych, **history, economics**, social | 13,513 | -0.6% |
| 3rd constrained | psych, **health, practical**, social, **history, economics** | 13,544 | -0.3% |

The best constrained ordering (13,365) is better than current (13,588) but **worse than the unconstrained optimum (12,836)** by 529 units. The constraint of placing practical-life adjacent to health costs ~4% of possible improvement because practical-life has zero edges to health.

### Simple swap: practical-life and economics

| Ordering | Cost | vs. Current |
|----------|------|-------------|
| ... social, **practical**, **economics**, history ... | 13,569 | -0.1% |

Minimal difference --- both domains have zero edges to their neighbors in either configuration.

## 5. Proposed Orderings

### Option A: Optimal by cost (recommended)

```
math, formal-sci, philosophy, CS, engineering, physics, earth-space, chemistry, biology,
health, psychology, history, social-sciences, practical-life, economics,
language, literature, arts, music
```

**Cost: 12,836 (-5.5%)**

Rationale: This is the global optimum for the 6-domain middle segment. It works because:
- Health stays next to biology (399 edges --- the strongest cross-domain pair in this region)
- Psychology stays next to health (13 edges)
- History moves inward, closer to language/literature (its only cross-domain connections: 4 to literature)
- Economics and practical-life end up closer to music/math side of the wrap, which matters because both have dominant math connections (277 and 248 edges respectively)

Tradeoffs:
- History between psychology and social-sciences may feel thematically odd (psychology-history adjacency)
- Practical-life and economics are now adjacent to each other and to the humanities tail, which is thematically reasonable
- The thematic narrative is: STEM core -> life sciences -> behavioral sciences -> historical/social sciences -> applied/practical -> humanities -> arts

### Option B: User's constraint satisfied (practical adj. health, economics adj. history)

Best version: `psych, health, practical, history, economics, social`

```
math, formal-sci, philosophy, CS, engineering, physics, earth-space, chemistry, biology,
psychology, health, practical-life, history, economics, social-sciences,
language, literature, arts, music
```

**Cost: 13,365 (-1.6%)**

Rationale: Satisfies both user constraints. Psychology moves before health (biology-psychology has 197 edges, making bio-psych-health a strong sequence). Practical-life sits between health and history. Economics sits between history and social-sciences.

Tradeoffs:
- Moves psychology away from social-sciences (currently separated by just 1 domain; now separated by 4)
- Practical-life next to health is **not justified by edge data** (0 cross-domain edges between them), purely a visual/thematic grouping
- Economics next to history is also **not justified by edge data** (0 edges), but is thematically stronger than the current practical-life-history pair
- Still 4% worse than the unconstrained optimum

### Option C: Minimal change (swap practical-life and economics only)

```
math, formal-sci, philosophy, CS, engineering, physics, earth-space, chemistry, biology,
health, psychology, social-sciences, practical-life, economics,
history, language, literature, arts, music
```

**Cost: 13,569 (-0.1%)**

Rationale: Smallest possible change. Puts economics next to history (user request #3). No meaningful cost change because both domains have 0 edges to all their neighbors in this region.

Tradeoffs:
- Does not address the practical-life/health adjacency request
- Practical-life remains far from health (separated by psychology and social-sciences)
- Negligible quantitative improvement

## 6. The "Visual Sector Merging" Question

> Should practical-life and health merge into one visual sector?

**No.** They should remain separate domains.

Reasons:
1. **Zero cross-domain edges** between them. They share no prerequisite relationships.
2. **Completely different content**: practical-life is home maintenance, cooking, financial literacy, digital literacy. Health is anatomy, physiology, epidemiology, public health, child development.
3. **Different stage profiles**: practical-life is exclusively pre-expert content (max: formal-systems). Health spans the full range including advanced and expert.
4. **The adjacency would be purely cosmetic** --- the empty outer rings of practical-life would visually "borrow" from health's populated outer rings, but this creates a false impression of topical connection.

A better approach to the "empty outer rings" visual problem: practical-life genuinely lacks advanced/expert content. That gap is real data, not a visualization artifact. If the visual bothers you, it could be addressed by:
- Eventually adding advanced/expert topics to practical-life (e.g., advanced financial planning, project management, systems thinking for home design)
- Reducing the visual prominence of empty bands (dimming or collapsing empty radial zones)

## 7. Recommendation

**Option A** (global optimum) is the strongest choice by the numbers. The 5.5% cost reduction is the largest achievable improvement to this segment of the ordering without touching the STEM core or humanities tail.

However, if the thematic narrative matters more than edge-length optimization (psychology-history adjacency in Option A is admittedly weird), then **Option B** is a reasonable compromise at -1.6%.

The key insight from the data: **the social/humanities zone (positions 9-14) is an "edge desert"** --- most of these domains connect overwhelmingly to mathematics, not to each other. This means rearranging them has modest quantitative impact. The ordering decision here is more about **thematic coherence** and **visual aesthetics** than edge-crossing minimization.

### Files to modify (2 primary, 1 optional)

1. `tools/visualize_radial.py` --- `DOMAIN_ORDER` list (line 56)
2. `tools/generate_quiz_page.py` --- JS `DOMAIN_ORDER` array (line 678)
3. `tools/visualize_hierarchy.py` --- independent `DOMAIN_ORDER` (line 73, optional, different layout)

Branch flips (`compute_branch_flips`) will auto-recompute. `COURSE_BRANCH_X` positions are per-course and domain-independent, so they need no changes. `DOMAIN_HUES` is keyed by domain name, not position, so it also needs no changes.
