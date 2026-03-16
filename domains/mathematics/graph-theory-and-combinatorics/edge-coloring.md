---
id: edge-coloring
title: Edge Coloring and Chromatic Index
domain: mathematics
course: graph-theory-and-combinatorics
prerequisites:
- id: graph-coloring
  type: hard
builds-toward:
- vizings-theorem
tags:
- graph-theory
- edge-coloring
stage: abstract-reasoning
status: draft
---

# Edge Coloring and Chromatic Index

## Core Idea
Edge coloring assigns colors to edges so no two edges sharing a vertex have the same color. The chromatic index is the minimum colors needed. Edge coloring has practical applications in scheduling and frequency assignment, and relates closely to finding matchings.

## Explainer

From vertex coloring, you learned to assign colors to vertices so that no two adjacent vertices share a color. **Edge coloring** flips the question: assign colors to *edges* so that no two edges sharing a *vertex* share a color. Two edges are in conflict when they meet at a vertex, and a valid edge coloring eliminates all conflicts. The minimum number of colors needed for a valid edge coloring is called the **chromatic index**, written χ'(G).

Why does this matter? Notice that all edges of the same color form a **matching** — a set of edges with no shared endpoints. So an edge coloring is exactly a partition of all edges into matchings, and the chromatic index is the fewest matchings needed to cover all edges. This connection to matchings is what makes edge coloring both deep and useful. A concrete scheduling example: suppose you have a round-robin tournament where every pair of teams must play once, and each team plays at most one game per time slot. Each time slot corresponds to a matching (games played simultaneously), and the chromatic index tells you the minimum number of slots needed. For n teams (the complete graph Kₙ), this turns out to be n−1 if n is even and n if n is odd.

A fundamental observation: every vertex has degree Δ (using Δ for the maximum degree), and all edges at that vertex need different colors, so χ'(G) ≥ Δ. You might hope χ'(G) = Δ always, but it isn't quite that clean. **Vizing's theorem** — the central result of edge coloring — says the truth is very close: χ'(G) is either Δ or Δ+1. Graphs achieving χ'(G) = Δ are called **Class 1**; those requiring Δ+1 colors are **Class 2**. Bipartite graphs are always Class 1 (a theorem of König), but determining whether an arbitrary graph is Class 1 or Class 2 is NP-complete. This makes Vizing's theorem particularly striking: the answer lies in a range of just two values, but pinning down which one is computationally hard.

The practical intuition for why one extra color can be necessary: imagine a vertex with very high degree. All its incident edges need distinct colors, saturating Δ colors just at that one vertex. If the rest of the graph's edge-matching structure doesn't align cleanly with that vertex's demands, one additional color becomes unavoidable. Vizing's proof shows this can always be resolved with at most one extra, which is a remarkably tight bound — a testament to the hidden structure in how edges and vertices interact.
