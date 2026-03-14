---
id: chromatic-number-bounds
title: 'Chromatic Number: Bounds and Algorithms'
domain: mathematics
course: graph-theory-and-combinatorics
prerequisites:
- id: graph-coloring
  type: hard
builds-toward:
- brooks-theorem
- chromatic-polynomial
tags:
- graph-theory
- coloring
- bounds
stage: abstract-reasoning
status: draft
---

# Chromatic Number: Bounds and Algorithms

## Core Idea
The chromatic number is the minimum colors needed so no adjacent vertices share a color. Upper bounds come from greedy algorithms (at most Δ+1, where Δ is max degree) and from relaxations; lower bounds come from clique size and spectral properties. Exact computation is NP-hard, making bounds and special cases practically important.
