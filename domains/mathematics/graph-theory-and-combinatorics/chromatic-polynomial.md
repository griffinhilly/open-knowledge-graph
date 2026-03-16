---
id: chromatic-polynomial
title: Chromatic Polynomials and Deletion-Contraction
domain: mathematics
course: graph-theory-and-combinatorics
prerequisites:
- id: graph-coloring
  type: hard
tags:
- graph-theory
- coloring
- polynomials
stage: advanced
status: draft
---

# Chromatic Polynomials and Deletion-Contraction

## Core Idea
The chromatic polynomial P(G, k) counts the number of proper k-colorings of a graph G. It satisfies the deletion-contraction recurrence P(G, k) = P(G-e, k) - P(G/e, k), which recursively reduces to base cases. Chromatic polynomials encode structural information and can be analyzed algebraically to determine graph properties.

## How It's Best Learned
Compute chromatic polynomials for small graphs (paths, cycles, stars) by hand using deletion-contraction, verifying by direct enumeration.

## Common Misconceptions
The chromatic polynomial is NOT the same as the number of proper colorings for a fixed G; rather, it's a polynomial in k that gives the count for any number of colors k.

## Explainer

From graph coloring, you know the **chromatic number** χ(G) — the minimum number of colors needed so that no two adjacent vertices share a color. The chromatic polynomial asks a richer question: not just what the minimum is, but how many ways can we properly color the graph using exactly k colors? The answer, written **P(G, k)**, turns out to be a polynomial in k. Plug in k = 3 and you get the number of proper 3-colorings. Plug in k = χ(G) − 1 and you should get zero (fewer colors than the minimum means no valid coloring exists).

The tool for computing P(G, k) is the **deletion-contraction recurrence**. Pick any edge e connecting vertices u and v. Consider two modified graphs: G − e (delete the edge, allowing u and v to be the same color or different) and G/e (contract the edge, merging u and v into a single vertex, so they must be the same color in any coloring of G). The recurrence is P(G, k) = P(G − e, k) − P(G/e, k). The logic: colorings of G − e where u and v happen to get the same color are exactly the colorings of G/e (since merging same-colored vertices changes nothing). Subtracting removes those "accidentally same-color" cases from G − e, leaving exactly the proper colorings of G.

Apply deletion-contraction repeatedly until you reach base cases. A graph with no edges on n vertices has P(G, k) = kⁿ — every vertex can independently take any of k colors. A complete graph Kₙ has P(Kₙ, k) = k(k−1)(k−2)···(k−n+1), the **falling factorial**, because each new vertex must avoid all previously used colors. For a path on n vertices, P(Pₙ, k) = k(k−1)ⁿ⁻¹. For a cycle Cₙ, it is (k−1)ⁿ + (−1)ⁿ(k−1) — a result that deletion-contraction gives cleanly.

The algebraic structure of P(G, k) encodes graph properties. The degree of the polynomial equals n (the number of vertices). The leading coefficient is always 1. The roots of the polynomial are never positive integers greater than χ(G) − 1 (by definition, since those give zero colorings). If G has a bridge (an edge whose removal disconnects the graph), the chromatic polynomial factors. These structural signatures make the chromatic polynomial a powerful tool for classifying graphs: two graphs with different chromatic polynomials are definitely not isomorphic, though two non-isomorphic graphs can coincidentally share the same polynomial.
