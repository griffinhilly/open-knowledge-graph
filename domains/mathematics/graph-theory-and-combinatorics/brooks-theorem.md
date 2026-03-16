---
id: brooks-theorem
title: Brooks' Theorem
domain: mathematics
course: graph-theory-and-combinatorics
prerequisites:
- id: chromatic-number-bounds
  type: hard
tags:
- graph-theory
- coloring
stage: formal-systems
status: draft
---

# Brooks' Theorem

## Core Idea
Brooks' Theorem states that any connected graph with maximum degree Δ has chromatic number at most Δ, except for complete graphs and odd cycles (which need Δ+1). This result elegantly shows that maximum degree is nearly always sufficient for coloring, vastly improving the trivial Δ+1 bound.

## How It's Best Learned
First examine the exceptions (Kₙ and odd cycles) to understand why they require Δ+1 colors. Then trace through greedy colorings on larger graphs to see how the proof's degree arguments work.

## Common Misconceptions
Brooks' theorem says AT MOST Δ colors suffice (not exactly Δ), and the exceptions are specific. Cliques Kₙ need n colors (which equals degree n-1 plus one).

## Explainer

From chromatic number bounds, you know the trivial upper bound: any graph with maximum degree Δ can be colored with Δ+1 colors, because a greedy algorithm can always find an available color for each vertex (it has at most Δ neighbors, so at least one of Δ+1 colors is unused). **Brooks' Theorem** tightens this bound dramatically, showing that Δ colors almost always suffice — the "+1" is only ever necessary for two specific families of graphs.

The two exceptions are the ones you'd predict from extremes. A **complete graph** Kₙ has every pair of vertices connected, so every vertex is adjacent to every other; you need a different color for each vertex, giving χ(Kₙ) = n = Δ+1. An **odd cycle** C_{2k+1} needs 3 colors despite having maximum degree 2 — you can 2-color any even cycle (alternate colors around the ring), but an odd cycle forces a third color when you wrap around and the start and end conflict. For every other connected graph, Δ colors are enough.

The proof idea is constructive. If the graph is not Kₙ or an odd cycle, you can find a clever vertex ordering that lets greedy coloring succeed within Δ colors. The key structural observation: in any graph that's neither a complete graph nor an odd cycle, there exists a vertex ordering where, when you color greedily in that order, every vertex has at most Δ−1 already-colored neighbors when you reach it — so one of the Δ colors is always free. The proof constructs this ordering using the structure of spanning trees rooted at a vertex of degree less than Δ (which must exist if the graph isn't Kₙ).

In practice, Brooks' Theorem tells you the **worst-case coloring cost** for most graphs: if you see a graph with Δ = 4, you can guarantee a proper 4-coloring exists unless it's K₅ or an odd cycle. This is especially useful in applications like register allocation (where a register-interference graph must be colored), scheduling (time slots = colors, conflicts = edges), and frequency assignment. The bound is tight — many Δ-regular graphs require exactly Δ colors — but it's never tighter than that outside the two exception families.
