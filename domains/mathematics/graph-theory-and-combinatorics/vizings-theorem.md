---
id: vizings-theorem
title: Vizing's Theorem
domain: mathematics
course: graph-theory-and-combinatorics
prerequisites:
- id: edge-coloring
  type: hard
tags:
- graph-theory
- edge-coloring
stage: formal-systems
status: draft
---

# Vizing's Theorem

## Core Idea
Vizing's Theorem states that the chromatic index of any simple graph is either Δ or Δ+1, where Δ is maximum degree. Graphs achieving Δ are Class 1; those needing Δ+1 are Class 2. Despite this tight characterization, determining class membership is NP-hard in general.

## How It's Best Learned
Examine Class 1 graphs (bipartite graphs are always Class 1) and Class 2 graphs (odd cycles, complete odd cliques) to see patterns in edge structure.

## Common Misconceptions
Not all graphs are Class 1; many require Δ+1 colors despite the tight bound. Determining class membership is computationally hard.

## Explainer

From edge coloring, you know that the **chromatic index** χ'(G) is the minimum number of colors needed to color the edges of G so that no two edges sharing a vertex receive the same color. The trivial lower bound is immediate: if a vertex has degree Δ (the maximum degree in the graph), all Δ edges at that vertex must receive different colors, so χ'(G) ≥ Δ. The question is how much higher than Δ we might need to go.

**Vizing's Theorem** gives a striking answer: never more than Δ + 1. For any simple graph with maximum degree Δ, the chromatic index is either exactly Δ or exactly Δ + 1 — nothing else is possible. This pins χ'(G) to one of just two values, a remarkably tight classification given that Δ alone tells you almost nothing about the graph's global structure. Graphs achieving χ'(G) = Δ are called **Class 1**; those requiring χ'(G) = Δ + 1 are called **Class 2**. Every simple graph falls into exactly one class.

The Class 1/Class 2 distinction has satisfying examples on both sides. **Bipartite graphs are always Class 1** — this follows from König's edge-coloring theorem, which shows that Δ colors always suffice for bipartite graphs. Complete graphs on an even number of vertices (K_{2n}) are also Class 1, since their edges decompose into exactly Δ perfect matchings. On the Class 2 side, **odd cycles** need 3 colors for maximum degree 2, since the odd cycle forces color conflicts. Complete graphs on an odd number of vertices (K_{2n+1}) are also Class 2, because the odd vertex count prevents a clean Δ-coloring.

The frustrating twist is that despite knowing χ'(G) is Δ or Δ+1, determining which one applies is computationally hard — deciding whether a graph is Class 1 is **NP-complete** in general. This mirrors the situation with Hamiltonian cycles: the theorem gives a beautifully precise characterization, but computing which case applies is intractable in the worst case. In scheduling applications, where edges represent tasks sharing a resource and colors represent time slots, Vizing's theorem provides the key practical guarantee: you will never need more than Δ + 1 time slots, regardless of graph structure. That upper bound is what makes the theorem immediately useful even before you know whether your specific graph is Class 1 or Class 2.
