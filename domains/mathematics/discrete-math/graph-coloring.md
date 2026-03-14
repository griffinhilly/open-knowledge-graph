---
id: graph-coloring
title: Graph Coloring and the Chromatic Number
domain: mathematics
course: discrete-math
prerequisites:
- id: graph-connectivity
  type: hard
- id: planar-graphs
  type: soft
- id: bipartite-graphs
  type: soft
- id: pigeonhole-principle
  type: soft
tags:
- graph-coloring
- chromatic-number
- four-color-theorem
- brooks-theorem
stage: formal-systems
status: validated
---

# Graph Coloring and the Chromatic Number

## Core Idea
A proper k-coloring assigns one of k colors to each vertex so that no two adjacent vertices share a color. The chromatic number χ(G) is the minimum k for which a proper coloring exists. Bipartite graphs have χ = 2; complete graphs Kₙ require n colors. The greedy coloring algorithm gives an upper bound of Δ(G)+1, and Brook's theorem tightens this to χ(G) ≤ Δ(G) except for complete graphs and odd cycles. The celebrated four-color theorem states every planar graph satisfies χ ≤ 4.

## How It's Best Learned
Color progressively complex graphs by hand — trees, even cycles, odd cycles, wheel graphs — and determine the chromatic number by finding both a valid coloring (upper bound) and an argument why fewer colors fail (lower bound). Scheduling problems (exam timetabling, register allocation) make the applications tangible.

## Common Misconceptions
- Thinking the chromatic number always equals the size of the largest clique — the clique number is a lower bound but not always achieved (see the Mycielski construction).
- Confusing vertex coloring (chromatic number) with edge coloring (chromatic index), which is a separate problem.
