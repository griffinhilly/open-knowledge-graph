---
id: edge-coloring-vizings-theorem
title: Edge Coloring and Vizing's Theorem
domain: mathematics
course: graph-theory-and-combinatorics
prerequisites:
- id: chromatic-polynomial
  type: soft
builds-toward:
- list-coloring
tags:
- edge-coloring
- vizings-theorem
- chromatic-index
stage: formal-systems
status: draft
---

# Edge Coloring and Vizing's Theorem

## Core Idea
The chromatic index χ'(G) is the minimum colors needed for a proper edge coloring. Vizing's theorem states χ'(G) ∈ {Δ(G), Δ(G)+1}, classifying graphs as Class 1 or Class 2. Determining which class a graph belongs to is NP-complete in general.

## How It's Best Learned
Compute edge colorings for small graphs and verify that the chromatic index is either Δ or Δ+1. Try to find patterns distinguishing Class 1 from Class 2 graphs.

## Common Misconceptions
- Thinking edge coloring relates to vertex coloring in a straightforward way; the two are different optimization problems.
- Assuming all graphs are easily classifiable as Class 1 or Class 2 (classification is hard in general).

## Explainer

**Edge coloring** assigns colors to the edges of a graph so that no two edges sharing a vertex get the same color. This models scheduling problems: if vertices are jobs and edges are time slots during which two jobs share a resource, an edge coloring finds a valid schedule. The minimum number of colors needed is called the **chromatic index**, written χ'(G) (to distinguish it from the vertex chromatic number χ(G) from your work on the chromatic polynomial).

What is the obvious lower bound for χ'(G)? Every edge incident to a high-degree vertex must get a distinct color, so you need at least Δ(G) colors, where Δ(G) is the **maximum degree** — the maximum number of edges meeting at any single vertex. The remarkable fact that Vizing proved in 1964 is that you never need more than Δ(G) + 1 colors: χ'(G) ∈ {Δ(G), Δ(G)+1}. This is a tight two-outcome theorem — graphs are partitioned into **Class 1** (chromatic index exactly Δ) and **Class 2** (chromatic index Δ + 1). Every graph lands in one of only two possibilities, with no room in between.

Bipartite graphs are always Class 1 — König's theorem guarantees this. Complete graphs Kₙ illustrate the two cases: K₄ has Δ = 3 and χ' = 3 (Class 1), while K₃ has Δ = 2 and χ' = 3 (Class 2). The Petersen graph, a well-known cubic graph with Δ = 3, is Class 2 with χ' = 4 and resists many simpler edge colorings. These examples suggest that Class 2 graphs are somehow "more constrained" — they have structural bottlenecks preventing the optimal Δ-coloring — but characterizing exactly which graphs are Class 2 has resisted a simple closed-form answer.

The difficulty is computational: deciding whether a graph is Class 1 is NP-complete in general, even though the answer is constrained to just two values. This is a recurring theme in graph theory — problems that seem to have limited output space are often computationally hard. The contrast with vertex coloring is instructive: vertex coloring has no tight universal bound like Vizing's theorem, while edge coloring does, yet edge coloring is just as computationally hard. Vizing's theorem is valuable precisely because it converts an unbounded question ("how many colors?") into a yes/no classification question ("are Δ colors enough?"), which in turn focuses research on identifying structural properties that determine class membership.
