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
status: validated
---

# Chromatic Polynomial and Counting Proper Colorings

## Core Idea
The chromatic polynomial P(G, k) counts the number of proper k-colorings of graph G. It can be computed using deletion-contraction: P(G,k) = P(G-e,k) - P(G/e,k), where G-e removes edge e and G/e contracts it. The chromatic number is the smallest k where P(G,k) > 0.

## Questions

```yaml
- question: "What is the chromatic polynomial P(K₄, k) for the complete graph on 4 vertices?"
  type: multiple-choice
  options:
    - "k⁴"
    - "k(k−1)(k−2)(k−3)"
    - "k(k−1)³"
    - "4k(k−1)"
  answer: 1
  explanation: "In K₄, every vertex must differ from every other vertex. The first vertex gets k choices, the second k−1, the third k−2, and the fourth k−3 — giving the falling factorial k(k−1)(k−2)(k−3). Option A (k⁴) is the count without any adjacency constraints — it ignores the edges entirely. The falling factorial formula generalizes to all complete graphs: P(Kₙ, k) = k(k−1)(k−2)···(k−n+1)."

- question: "While computing P(G, 3) via deletion-contraction on edge e, you find P(G − e, 3) = 24 and P(G/e, 3) = 9. What is P(G, 3)?"
  type: multiple-choice
  options:
    - "33"
    - "15"
    - "216"
    - "8"
  answer: 1
  explanation: "The deletion-contraction formula is P(G, k) = P(G − e, k) − P(G/e, k). So P(G, 3) = 24 − 9 = 15. The common error is to add rather than subtract. The subtraction makes sense because P(G − e, k) counts all proper colorings of the graph without the edge — including those where the two endpoints of e happen to share a color. P(G/e, k) counts exactly those colorings (after merging the endpoints). Subtracting removes them, leaving only colorings where the endpoints differ, which are precisely the proper colorings of G."

- question: "The chromatic number χ(G) equals the smallest positive integer k for which P(G, k) > 0."
  type: true-false
  answer: true
  explanation: "This is a key structural fact: P(G, k) = 0 for k = 0, 1, ..., χ(G) − 1, because you cannot properly color G with fewer than χ(G) colors. At k = χ(G), at least one proper coloring exists, so P(G, χ(G)) > 0. This means the chromatic number is readable from the polynomial as its smallest positive integer root — a remarkable connection between the combinatorial minimum coloring problem and an algebraic object."

- question: "The degree of the chromatic polynomial P(G, k) equals the number of edges in graph G."
  type: true-false
  answer: false
  explanation: "The degree of P(G, k) equals the number of *vertices*, not edges. For a graph on n vertices, P(G, k) is always a degree-n polynomial with leading coefficient 1. The number of edges affects the specific coefficients (and their signs, which alternate), but not the degree. A tree on 5 vertices and a cycle on 5 vertices have the same degree polynomial — degree 5 — despite having different edge counts."

- question: "Explain the logic behind the deletion-contraction formula P(G, k) = P(G − e, k) − P(G/e, k). Why do we subtract rather than add?"
  type: short-answer
  answer: "P(G − e, k) counts all proper k-colorings of G without the constraint imposed by edge e — including colorings where the two endpoints of e share the same color. These colorings-with-shared-color correspond exactly to proper colorings of the contracted graph G/e (where the two endpoints are merged into one vertex). Subtracting P(G/e, k) removes exactly those invalid colorings, leaving only colorings where the endpoints get different colors — the proper colorings of G."
  explanation: "The argument is an inclusion-exclusion over whether the two endpoints of e receive the same or different colors. If different: that's a proper coloring of G, counted by P(G, k). If the same: you can treat them as one vertex, giving a proper coloring of G/e. Together these two disjoint cases cover all proper colorings of G − e, giving P(G − e, k) = P(G, k) + P(G/e, k), which rearranges to the deletion-contraction formula."
```

## Explainer

You already know from graph coloring that the **chromatic number** χ(G) is the minimum number of colors needed to properly color a graph. The chromatic polynomial takes this idea further: instead of just asking "what is the minimum?", it asks "for a given k, in exactly how many ways can we properly color G?" The answer, P(G, k), turns out to be a polynomial in k — a remarkable fact that connects discrete graph structure to algebraic objects.

The key computational tool is **deletion-contraction**. Pick any edge e = {u, v}. There are two cases for any proper k-coloring: either u and v get different colors (which is exactly a proper coloring of the graph G − e with the extra constraint that u ≠ v), or they could share a color (which corresponds to a proper coloring of the contracted graph G/e, where u and v are merged into one vertex). The formula P(G, k) = P(G − e, k) − P(G/e, k) captures this: total colorings of G-without-the-edge-constraint, minus the colorings where u and v happen to be the same color. You subtract because those colorings violate the edge constraint.

To build intuition, consider a tree on n vertices. No cycles means you can color it greedily: the root gets k choices, and each subsequent vertex just needs to avoid its one parent, giving k − 1 choices. So P(Tree_n, k) = k(k−1)^(n−1). For a complete graph Kₙ, every vertex must differ from every other, giving P(Kₙ, k) = k(k−1)(k−2)···(k−n+1) — falling factorial. These two extremes bracket the general case: sparse graphs have more colorings, dense graphs fewer.

The chromatic polynomial encodes χ(G) as its **smallest positive integer root**: P(G, k) = 0 for k = 0, 1, ..., χ(G) − 1, and P(G, χ(G)) > 0. This means you can read off the chromatic number by finding where the polynomial first becomes positive. The degree of P(G, k) equals the number of vertices, the leading coefficient is 1, and the signs of coefficients alternate — these algebraic signatures reflect structural properties of the graph. Deletion-contraction eventually bottoms out at empty graphs (P(∅, k) = 1) and single edges (P(K₂, k) = k(k−1)), giving a complete recursive recipe for computing P(G, k) for any graph.
