---
id: compactness-hausdorff-spaces
title: Compactness in Hausdorff Spaces
domain: mathematics
course: topology
prerequisites:
- id: compact-spaces-open-covers
  type: hard
- id: hausdorff-spaces
  type: hard
builds-toward:
- tychonoff-theorem
- topological-manifolds-introduction
tags:
- compactness
- hausdorff
- closed-sets
stage: advanced
status: draft
---

# Compactness in Hausdorff Spaces

## Core Idea
In Hausdorff spaces, compact subsets are closed and finite products of compact spaces are compact (though infinite products require Tychonoff's theorem). These results show that compactness and closure interact beautifully in Hausdorff spaces, making them ideal for analysis.

## Explainer

You already know two things: compactness (every open cover has a finite subcover) and the Hausdorff property (distinct points can be separated by disjoint open sets). These two properties interact to give each other more power than either has alone. The central result is: **compact subsets of Hausdorff spaces are closed**. This is not obvious — in a general topological space, compact sets need not be closed. But the Hausdorff condition provides exactly the separation needed to separate a compact set from any external point.

The proof idea is instructive. Given a compact subset K and a point x ∉ K, the Hausdorff property lets you separate x from *each* point of K with disjoint open sets. Compactness then reduces this infinite family of separations to a *finite* one, and from that finite collection you can build a single open neighborhood of x disjoint from K. This is the pattern you will see repeatedly in topology: compactness converts infinitely many local conditions into finitely many, which can then be combined explicitly.

An important corollary follows: a continuous bijection from a compact space onto a Hausdorff space is a **homeomorphism** — its inverse is automatically continuous. This is striking because, in general, the inverse of a continuous bijection need not be continuous. Compactness ensures the image of a closed set is closed (closed subsets of compacts are compact, and compact subsets of Hausdorff spaces are closed), which is exactly what's needed for the inverse to be continuous.

Finite products of compact spaces are compact under either the box or product topology (in the finite case, these agree). But for infinite products, the product topology is essential — this is what Tychonoff's theorem handles. The key takeaway about Hausdorff spaces is that they provide a controlled environment: compactness no longer needs extra qualifications to behave as geometric intuition demands. In ℝⁿ, compact sets are exactly the closed and bounded ones (Heine-Borel), and that theorem lives entirely within the Hausdorff-compact framework you're now studying.
