---
id: time-complexity-classes
title: 'Time Complexity Classes: P and EXPTIME'
domain: computer-science
course: theory-of-computation
prerequisites:
- id: turing-machines
  type: hard
- id: time-space-complexity
  type: soft
- id: big-o-notation
  type: soft
builds-toward:
- nondeterministic-complexity
- space-complexity-classes
tags:
- P
- EXPTIME
- complexity
- polynomial-time
- time-complexity
stage: advanced
status: draft
---

# Time Complexity Classes: P and EXPTIME

## Core Idea
The class P consists of all decision problems solvable by a deterministic TM in polynomial time O(nᵏ) for some constant k. P captures problems that are 'efficiently solvable' and includes sorting, shortest paths, primality testing, and linear programming. EXPTIME contains problems solvable in exponential time 2^poly(n); it strictly contains P. Basing complexity on TM running time formalizes the intuitive notion of tractability. The polynomial-time model is robust across reasonable machine models — polynomial in one is polynomial in another.

## How It's Best Learned
Classify known algorithms into P: sorting is O(n log n) ⊆ P, BFS/DFS is O(V+E) ⊆ P. Then encounter problems (chess, exponential-search problems) known to require exponential time. This calibrates the P boundary.

## Common Misconceptions
- Thinking P means 'fast' in practice — O(n¹⁰⁰) is in P but completely impractical.
- Confusing EXPTIME with 'undecidable' — EXPTIME problems are decidable, just slow.
