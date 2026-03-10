---
id: np-completeness
title: NP-Completeness
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: np-and-polynomial-time
  type: hard
- id: polynomial-time-reductions
  type: hard
- id: big-o-notation
  type: soft
builds-toward:
- cook-levin-theorem
- pspace-and-complexity-hierarchy
tags:
- complexity
- NP-complete
- hardness
- intractability
stage: advanced
status: draft
---

# NP-Completeness

## Core Idea
A problem is NP-complete if it is in NP and every problem in NP reduces to it in polynomial time — it is simultaneously the hardest class of problems in NP. If any NP-complete problem has a polynomial-time algorithm, then P = NP and all NP problems become tractable. Hundreds of natural problems from combinatorics, graph theory, logic, and optimization are NP-complete. The NP-completeness framework, introduced by Cook and Karp in the early 1970s, provides rigorous grounds for arguing a problem is computationally intractable.

## How It's Best Learned
Build a mental map of NP-complete problems and their reduction relationships: SAT → 3-SAT → 3-Coloring → Clique → Independent Set → Vertex Cover. Understanding these reductions both proves completeness and reveals deep structural connections between seemingly unrelated problems.

## Common Misconceptions
- NP-completeness does not prove a problem is unsolvable — it says the problem is likely intractable assuming P ≠ NP, but exponential exact algorithms, approximation schemes, and special-case analyses remain viable.
- Membership in NP-complete means the problem is *at most* exponential, not that it requires exponential time.
