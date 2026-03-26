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
stage: formal-systems
status: validated
---

# Chromatic Polynomials and Deletion-Contraction

## Core Idea
The chromatic polynomial P(G, k) counts the number of proper k-colorings of a graph G. It satisfies the deletion-contraction recurrence P(G, k) = P(G-e, k) - P(G/e, k), which recursively reduces to base cases. Chromatic polynomials encode structural information and can be analyzed algebraically to determine graph properties.

## How It's Best Learned
Compute chromatic polynomials for small graphs (paths, cycles, stars) by hand using deletion-contraction, verifying by direct enumeration.

## Common Misconceptions
The chromatic polynomial is NOT the same as the number of proper colorings for a fixed G; rather, it's a polynomial in k that gives the count for any number of colors k.

## Questions

```yaml
- question: "You compute P(G, k) = k(k−1)(k−2) for a graph G. A classmate says: 'So G has k(k−1)(k−2) proper colorings.' What is wrong with this statement?"
  type: multiple-choice
  options:
    - "Nothing — the statement is correct as written"
    - "The number of proper colorings depends on the specific value of k chosen; k(k−1)(k−2) is a formula giving a different count for each k, not a single fixed number"
    - "P(G, k) counts improper colorings, not proper ones"
    - "The chromatic polynomial only applies when k equals the chromatic number"
  answer: 1
  explanation: "This is the central misconception the topic warns against. P(G, k) is a polynomial — a function of k, not a fixed number. For k = 3, G has 3·2·1 = 6 proper colorings; for k = 4, it has 4·3·2 = 24; for k = 2, it has 2·1·0 = 0. Saying 'G has k(k−1)(k−2) proper colorings' is like saying 'the function f(x) = x² has x² outputs' — it is not wrong exactly, but it misses that k is a variable whose value you must supply. The polynomial encodes the count for every k simultaneously."

- question: "In the deletion-contraction formula P(G, k) = P(G−e, k) − P(G/e, k), what exactly does subtracting P(G/e, k) accomplish?"
  type: multiple-choice
  options:
    - "It removes colorings where the two endpoints of edge e have different colors"
    - "It removes colorings of G−e where the two endpoints of e happen to receive the same color — colorings that would be improper in G since e requires them to differ"
    - "It accounts for the fact that G/e has one fewer vertex than G−e"
    - "It eliminates disconnected components from the count"
  answer: 1
  explanation: "The logic: P(G−e, k) counts all proper colorings of the graph without edge e, which includes cases where the endpoints u and v get the same color. Those colorings are invalid in G (since e requires u and v to differ). Colorings of G−e where u and v are the same color are exactly the colorings of G/e — merging same-colored vertices changes nothing about validity. So P(G−e, k) − P(G/e, k) = colorings of G−e that give u and v different colors = proper colorings of G. The subtraction isolates exactly the valid colorings."

- question: "For any graph G with n vertices, the chromatic polynomial P(G, k) has degree exactly n and leading coefficient 1."
  type: true-false
  answer: true
  explanation: "This is a structural property of chromatic polynomials. The degree equals the number of vertices because the most 'free' a coloring can be is all n vertices choosing independently from k colors (the edgeless graph gives kⁿ). Every edge constraint reduces the polynomial by one degree of freedom, but the degree itself stays n while the lower-order coefficients change. The leading coefficient is always 1, which can be seen from the fact that every graph on n vertices reduces via deletion-contraction to base cases whose leading terms all combine to give a leading coefficient of 1."

- question: "Two non-isomorphic graphs should have different chromatic polynomials — if P(G, k) = P(H, k) for most k, then G and H are isomorphic."
  type: true-false
  answer: false
  explanation: "This is false: two non-isomorphic graphs can coincidentally share the same chromatic polynomial. The chromatic polynomial encodes a great deal of structural information (degree, chromatic number, number of edges, bridges), but it does not uniquely determine the graph. Pairs of non-isomorphic graphs with identical chromatic polynomials are known and serve as examples that the polynomial is powerful but not a complete graph invariant. Graphs with different chromatic polynomials are definitely not isomorphic, but the converse does not hold."

- question: "Explain in your own words why the deletion-contraction formula P(G, k) = P(G−e, k) − P(G/e, k) correctly counts proper colorings of G. What does each term represent, and why does the subtraction give the right answer?"
  type: short-answer
  answer: "P(G−e, k) counts proper colorings of the graph without edge e — these are all colorings where every other adjacency constraint is satisfied, but the two endpoints u and v of e are free to be the same color or different. P(G/e, k) counts colorings of the contracted graph where u and v have been merged into a single vertex — these are exactly the colorings of G−e in which u and v received the same color (since merging same-colored vertices is equivalent). Subtracting removes these invalid cases, leaving only colorings where u and v are different colors — which are precisely the proper colorings of G, where the edge e requires them to differ."
  explanation: "The deletion-contraction argument is a combinatorial partition: take all colorings satisfying all constraints except e, then subtract those that violate e (same-color endpoints). The contracted graph is the clever device for counting that subset cleanly. The recursive application to base cases (edgeless graphs and complete graphs) makes the computation tractable."
```

## Explainer

From graph coloring, you know the **chromatic number** χ(G) — the minimum number of colors needed so that no two adjacent vertices share a color. The chromatic polynomial asks a richer question: not just what the minimum is, but how many ways can we properly color the graph using exactly k colors? The answer, written **P(G, k)**, turns out to be a polynomial in k. Plug in k = 3 and you get the number of proper 3-colorings. Plug in k = χ(G) − 1 and you should get zero (fewer colors than the minimum means no valid coloring exists).

The tool for computing P(G, k) is the **deletion-contraction recurrence**. Pick any edge e connecting vertices u and v. Consider two modified graphs: G − e (delete the edge, allowing u and v to be the same color or different) and G/e (contract the edge, merging u and v into a single vertex, so they must be the same color in any coloring of G). The recurrence is P(G, k) = P(G − e, k) − P(G/e, k). The logic: colorings of G − e where u and v happen to get the same color are exactly the colorings of G/e (since merging same-colored vertices changes nothing). Subtracting removes those "accidentally same-color" cases from G − e, leaving exactly the proper colorings of G.

Apply deletion-contraction repeatedly until you reach base cases. A graph with no edges on n vertices has P(G, k) = kⁿ — every vertex can independently take any of k colors. A complete graph Kₙ has P(Kₙ, k) = k(k−1)(k−2)···(k−n+1), the **falling factorial**, because each new vertex must avoid all previously used colors. For a path on n vertices, P(Pₙ, k) = k(k−1)ⁿ⁻¹. For a cycle Cₙ, it is (k−1)ⁿ + (−1)ⁿ(k−1) — a result that deletion-contraction gives cleanly.

The algebraic structure of P(G, k) encodes graph properties. The degree of the polynomial equals n (the number of vertices). The leading coefficient is always 1. The roots of the polynomial are never positive integers greater than χ(G) − 1 (by definition, since those give zero colorings). If G has a bridge (an edge whose removal disconnects the graph), the chromatic polynomial factors. These structural signatures make the chromatic polynomial a powerful tool for classifying graphs: two graphs with different chromatic polynomials are definitely not isomorphic, though two non-isomorphic graphs can coincidentally share the same polynomial.
