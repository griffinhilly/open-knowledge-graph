---
id: randomized-complexity-classes
title: Randomized Algorithms and Probabilistic Complexity Classes
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: probabilistic-computation
  type: hard
- id: bpp-randomized-complexity
  type: hard
builds-toward:
- approximation-hardness-results
tags:
- randomized-algorithms
- BPP
- RP
- ZPP
stage: advanced
status: draft
---

# Randomized Algorithms and Probabilistic Complexity Classes

## Core Idea
Randomized Turing machines accept strings with bounded probability. RP (random polynomial time) languages can be verified with one-sided error; BPP (bounded-error probabilistic polynomial time) allows two-sided error. Surprisingly, BPP ⊆ PSPACE and likely BPP = P, suggesting randomness does not provide a fundamental advantage for polynomial-time computation, though random algorithms are practically powerful.
