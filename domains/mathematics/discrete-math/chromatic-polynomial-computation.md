---
id: chromatic-polynomial-computation
title: Chromatic Polynomial and Counting Proper Colorings
domain: mathematics
course: discrete-math
prerequisites:
- id: graph-coloring-chromatic
  type: hard
tags:
- graph-theory
- chromatic-polynomial
stage: formal-systems
status: draft
---

# Chromatic Polynomial and Counting Proper Colorings

## Core Idea
The chromatic polynomial P(G, k) counts the number of proper k-colorings of graph G. It can be computed using deletion-contraction: P(G,k) = P(G-e,k) - P(G/e,k), where G-e removes edge e and G/e contracts it. The chromatic number is the smallest k where P(G,k) > 0.

## Explainer

You already know from graph coloring that the **chromatic number** χ(G) is the minimum number of colors needed to properly color a graph. The chromatic polynomial takes this idea further: instead of just asking "what is the minimum?", it asks "for a given k, in exactly how many ways can we properly color G?" The answer, P(G, k), turns out to be a polynomial in k — a remarkable fact that connects discrete graph structure to algebraic objects.

The key computational tool is **deletion-contraction**. Pick any edge e = {u, v}. There are two cases for any proper k-coloring: either u and v get different colors (which is exactly a proper coloring of the graph G − e with the extra constraint that u ≠ v), or they could share a color (which corresponds to a proper coloring of the contracted graph G/e, where u and v are merged into one vertex). The formula P(G, k) = P(G − e, k) − P(G/e, k) captures this: total colorings of G-without-the-edge-constraint, minus the colorings where u and v happen to be the same color. You subtract because those colorings violate the edge constraint.

To build intuition, consider a tree on n vertices. No cycles means you can color it greedily: the root gets k choices, and each subsequent vertex just needs to avoid its one parent, giving k − 1 choices. So P(Tree_n, k) = k(k−1)^(n−1). For a complete graph Kₙ, every vertex must differ from every other, giving P(Kₙ, k) = k(k−1)(k−2)···(k−n+1) — falling factorial. These two extremes bracket the general case: sparse graphs have more colorings, dense graphs fewer.

The chromatic polynomial encodes χ(G) as its **smallest positive integer root**: P(G, k) = 0 for k = 0, 1, ..., χ(G) − 1, and P(G, χ(G)) > 0. This means you can read off the chromatic number by finding where the polynomial first becomes positive. The degree of P(G, k) equals the number of vertices, the leading coefficient is 1, and the signs of coefficients alternate — these algebraic signatures reflect structural properties of the graph. Deletion-contraction eventually bottoms out at empty graphs (P(∅, k) = 1) and single edges (P(K₂, k) = k(k−1)), giving a complete recursive recipe for computing P(G, k) for any graph.
