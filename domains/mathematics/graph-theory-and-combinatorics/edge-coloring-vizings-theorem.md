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
