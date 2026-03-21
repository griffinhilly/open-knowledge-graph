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

## Questions

```yaml
- question: "A graph G has maximum degree Δ(G) = 6. The greedy coloring algorithm processes vertices in some order. Which statement is guaranteed to be true?"
  type: multiple-choice
  options:
    - "The greedy algorithm will always use exactly 7 colors"
    - "The chromatic number χ(G) is exactly 6"
    - "The greedy algorithm uses at most 7 colors, but χ(G) may be much smaller"
    - "No proper coloring of G can use fewer than 6 colors"
  answer: 2
  explanation: "The greedy upper bound χ(G) ≤ Δ(G) + 1 = 7 tells us the greedy algorithm never needs more than 7 colors, but it says nothing about the minimum. The true chromatic number could be 2, 3, or any value up to 7. The greedy algorithm's performance also depends on vertex ordering — a different ordering might use fewer colors. The bound is a guarantee of feasibility, not a computation of the minimum."

- question: "A graph G is triangle-free (contains no 3-clique). What can we conclude about χ(G)?"
  type: multiple-choice
  options:
    - "χ(G) = 2, because triangle-free graphs are bipartite"
    - "χ(G) ≤ 2, because ω(G) = 1 gives a tight lower bound"
    - "χ(G) ≥ 2, but χ(G) could be arbitrarily large despite ω(G) = 2"
    - "χ(G) ≤ Δ(G) by Brooks' theorem, since G is not a complete graph"
  answer: 2
  explanation: "Triangle-free means ω(G) ≤ 2 (no 3-clique), giving the lower bound χ(G) ≥ 2 only. But there exist triangle-free graphs with arbitrarily large chromatic number — the clique bound is weak here. Triangle-free does not mean bipartite; odd cycles of length ≥ 5 are triangle-free but need 3 colors. This is a core insight: local structure (cliques) does not determine global coloring complexity."

- question: "For any graph G, the chromatic number χ(G) is always at least as large as the clique number ω(G)."
  type: true-false
  answer: true
  explanation: "Every pair of vertices in a clique is adjacent, so each vertex in a k-clique needs a distinct color. If G contains a clique of size ω(G), then at least ω(G) colors are required for that clique alone. This lower bound χ(G) ≥ ω(G) always holds. It is useful when tight, but can be very loose: graphs exist with ω(G) = 2 (no triangles) but χ(G) arbitrarily large."

- question: "If a graph G has clique number ω(G) = 5, then its chromatic number must be exactly 5."
  type: true-false
  answer: false
  explanation: "ω(G) = 5 gives the lower bound χ(G) ≥ 5, but the chromatic number could be 6, 10, or any larger value. The clique number is a lower bound, not an exact value. Perfect graphs are a special class where χ(G) = ω(G) always holds, but this is a deep result (the perfect graph theorem), not a general fact. For arbitrary graphs, χ can far exceed ω."

- question: "Why is the clique lower bound χ(G) ≥ ω(G) sometimes a very weak lower bound, and what does this reveal about the chromatic number?"
  type: short-answer
  answer: "The clique bound only captures local structure — how densely connected small subsets of vertices are. But chromatic number is a global property depending on how the entire graph is structured. There exist graphs (e.g., Mycielski graphs) with no triangles at all (ω = 2) but chromatic number as high as you want. These graphs have complex global structure that forces many colors even though no two adjacent vertices share more than one neighbor. This reveals that χ cannot be determined from local clique information alone."
  explanation: "This gap between ω and χ is precisely why computing χ is NP-hard in general. Local certificates (cliques) give cheap lower bounds, but global chromatic number requires understanding the whole graph's structure — which resists efficient computation."
```

## Explainer

From graph coloring, you know that the **chromatic number** χ(G) is the minimum number of colors needed to properly color a graph — no two adjacent vertices share a color. The hard truth is that computing χ(G) exactly for arbitrary graphs is NP-hard, meaning no efficient general algorithm is known. In practice, we rely on bounds that can be computed efficiently, and on structural results that pin down χ(G) for special graph families.

The simplest upper bound comes from the **greedy coloring algorithm**: process vertices in any order, and assign each vertex the smallest color not already used by its neighbors. A vertex with degree d has at most d neighbors, so the greedy algorithm never needs more than d + 1 colors. Since the maximum degree Δ(G) is the worst case, this gives χ(G) ≤ Δ(G) + 1. This bound is tight: the complete graph Kₙ and odd cycles both achieve Δ + 1. Brooks' theorem (your next topic) tightens this: except for complete graphs and odd cycles, χ(G) ≤ Δ(G).

The simplest lower bound comes from **cliques**. A clique is a set of vertices all pairwise adjacent; every pair of clique vertices needs a different color. So χ(G) ≥ ω(G), where ω(G) is the clique number (size of the largest clique). Unfortunately, the clique bound can be quite weak: there exist graphs with no triangles (ω = 2) but arbitrarily large chromatic number, showing that local structure alone doesn't determine χ. **Spectral bounds** — using eigenvalues of the adjacency or Laplacian matrix — often give tighter lower bounds for specific graphs, but require linear algebra machinery beyond the greedy argument.

Understanding bounds matters practically because many real-world problems reduce to graph coloring: scheduling tasks with conflicts (vertices are tasks, edges are conflicts), register allocation in compilers, and frequency assignment in wireless networks. In all these settings, you need to know the chromatic number or a good approximation. The upper bound tells you a feasible solution exists with at most Δ + 1 resources; the lower bound tells you you cannot do better than ω resources. When the two bounds meet, you have found χ(G) exactly — without solving an NP-hard problem directly.
