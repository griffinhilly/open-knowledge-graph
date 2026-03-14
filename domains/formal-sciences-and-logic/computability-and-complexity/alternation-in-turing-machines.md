---
id: alternation-in-turing-machines
title: Alternating Turing Machines and Complexity
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: nondeterministic-turing-machines
  type: hard
- id: pspace-and-complexity-hierarchy
  type: hard
builds-toward:
- circuit-complexity-and-bounds
tags:
- alternation
- ATIME
- ASPACE
- quantifiers
stage: advanced
status: draft
---

# Alternating Turing Machines and Complexity

## Core Idea
An alternating Turing machine combines existential (∃) and universal (∀) states, branching the computation tree along both dimensions. Computation accepts if the game tree evaluates to true (existential wins; universal loses). ATIME and ASPACE characterize the polynomial hierarchy: Σₖ(DTIME(n^k)) = ATIME(n^k) with k-1 alternations. ATMs provide a game-theoretic lens on complexity.
