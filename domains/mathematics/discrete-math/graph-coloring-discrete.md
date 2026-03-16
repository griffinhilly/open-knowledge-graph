---
id: graph-coloring-discrete
title: Graph Coloring and Chromatic Numbers
domain: mathematics
course: discrete-math
prerequisites:
- id: graph-coloring
  type: hard
builds-toward:
- bipartite-graphs-matching
tags:
- coloring
- chromatic-number
- greedy-coloring
- bounds
stage: formal-systems
status: draft
---

# Graph Coloring and Chromatic Numbers

## Core Idea
A proper graph coloring assigns colors to vertices so adjacent vertices have different colors. The chromatic number χ(G) is the minimum colors needed. Computing χ(G) is NP-hard in general, but bounds exist: χ(G) ≤ Δ(G) + 1, where Δ is max degree.

## How It's Best Learned
Find the chromatic number of small graphs by hand. Implement a greedy coloring algorithm. Understand special cases: bipartite graphs have χ = 2; complete graphs have χ = n; cycles of odd length have χ = 3.

## Common Misconceptions
The four-color theorem applies to planar graphs, not all graphs. χ(G) = 2 iff G is bipartite (no odd cycles). Greedy coloring doesn't always find the optimal number.

## Explainer

Building on your understanding of graph coloring, the **chromatic number** χ(G) answers the optimization question: what is the *minimum* number of colors needed for a proper coloring? Think of the classic scheduling problem — you want to assign time slots for university exams so that no two courses sharing a student are scheduled at the same time. Each course is a vertex; a shared student creates an edge. Colors are time slots. A proper coloring corresponds to a valid schedule, and χ(G) is the fewest time slots you need.

The upper bound χ(G) ≤ Δ(G) + 1 (where Δ is the maximum vertex degree) comes from a simple greedy algorithm: process vertices in any order, and assign each vertex the smallest color not used by any of its neighbors. At the moment you color a vertex with at most Δ neighbors, at most Δ colors are already excluded, so the (Δ+1)th color is always available. This guarantees the bound, but greedy often does better — and the bound isn't always tight.

Special graph families reveal what χ(G) actually measures. A **complete graph** Kₙ has every pair of vertices adjacent, so all n vertices must get different colors: χ(Kₙ) = n. A **bipartite graph** can be 2-colored — label one partition class with color 1 and the other with color 2 — and χ(G) = 2 characterizes exactly the bipartite graphs (those with no odd cycles). An odd cycle like C₅ (a pentagon) needs 3 colors: you can alternate 2 colors around most of the cycle, but the last vertex ends up adjacent to vertices of both colors, forcing a third.

The bad news for algorithms: computing χ(G) exactly for an arbitrary graph is NP-hard. No polynomial-time algorithm is known. This is why graph coloring appears in so many "hard optimization" contexts — the scheduling, register allocation, and frequency assignment problems it models are genuinely difficult. In practice, one bounds χ(G) between the size of the largest **clique** (complete subgraph) below and Δ+1 above, and applies heuristics in between.
