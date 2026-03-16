---
id: brooks-theorem
title: Brooks' Theorem
domain: mathematics
course: graph-theory-and-combinatorics
prerequisites:
- id: chromatic-number-bounds
  type: hard
tags:
- graph-theory
- coloring
stage: formal-systems
status: draft
---

# Brooks' Theorem

## Core Idea
Brooks' Theorem states that any connected graph with maximum degree Δ has chromatic number at most Δ, except for complete graphs and odd cycles (which need Δ+1). This result elegantly shows that maximum degree is nearly always sufficient for coloring, vastly improving the trivial Δ+1 bound.

## How It's Best Learned
First examine the exceptions (Kₙ and odd cycles) to understand why they require Δ+1 colors. Then trace through greedy colorings on larger graphs to see how the proof's degree arguments work.

## Common Misconceptions
Brooks' theorem says AT MOST Δ colors suffice (not exactly Δ), and the exceptions are specific. Cliques Kₙ need n colors (which equals degree n-1 plus one).
