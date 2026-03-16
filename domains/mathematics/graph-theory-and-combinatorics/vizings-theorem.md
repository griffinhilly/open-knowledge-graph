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
