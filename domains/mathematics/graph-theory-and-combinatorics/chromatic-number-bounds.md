---
id: chromatic-number-bounds
title: 'Chromatic Number: Bounds and Algorithms'
domain: mathematics
course: graph-theory-and-combinatorics
prerequisites:
- id: graph-coloring
  type: hard
builds-toward:
- brooks-theorem
- chromatic-polynomial
tags:
- graph-theory
- coloring
- bounds
stage: formal-systems
status: draft
---

# Chromatic Number: Bounds and Algorithms

## Core Idea
The chromatic number is the minimum colors needed so no adjacent vertices share a color. Upper bounds come from greedy algorithms (at most Δ+1, where Δ is max degree) and from relaxations; lower bounds come from clique size and spectral properties. Exact computation is NP-hard, making bounds and special cases practically important.

## Explainer

From graph coloring, you know that the **chromatic number** χ(G) is the minimum number of colors needed to properly color a graph — no two adjacent vertices share a color. The hard truth is that computing χ(G) exactly for arbitrary graphs is NP-hard, meaning no efficient general algorithm is known. In practice, we rely on bounds that can be computed efficiently, and on structural results that pin down χ(G) for special graph families.

The simplest upper bound comes from the **greedy coloring algorithm**: process vertices in any order, and assign each vertex the smallest color not already used by its neighbors. A vertex with degree d has at most d neighbors, so the greedy algorithm never needs more than d + 1 colors. Since the maximum degree Δ(G) is the worst case, this gives χ(G) ≤ Δ(G) + 1. This bound is tight: the complete graph Kₙ and odd cycles both achieve Δ + 1. Brooks' theorem (your next topic) tightens this: except for complete graphs and odd cycles, χ(G) ≤ Δ(G).

The simplest lower bound comes from **cliques**. A clique is a set of vertices all pairwise adjacent; every pair of clique vertices needs a different color. So χ(G) ≥ ω(G), where ω(G) is the clique number (size of the largest clique). Unfortunately, the clique bound can be quite weak: there exist graphs with no triangles (ω = 2) but arbitrarily large chromatic number, showing that local structure alone doesn't determine χ. **Spectral bounds** — using eigenvalues of the adjacency or Laplacian matrix — often give tighter lower bounds for specific graphs, but require linear algebra machinery beyond the greedy argument.

Understanding bounds matters practically because many real-world problems reduce to graph coloring: scheduling tasks with conflicts (vertices are tasks, edges are conflicts), register allocation in compilers, and frequency assignment in wireless networks. In all these settings, you need to know the chromatic number or a good approximation. The upper bound tells you a feasible solution exists with at most Δ + 1 resources; the lower bound tells you you cannot do better than ω resources. When the two bounds meet, you have found χ(G) exactly — without solving an NP-hard problem directly.
