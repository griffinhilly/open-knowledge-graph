---
id: savitch-theorem-and-implications
title: Savitch Theorem and Time-Space Tradeoffs
domain: computer-science
course: theory-of-computation
prerequisites:
- id: space-complexity-definitions
  type: hard
tags:
- savitch-theorem
- pspace
- npspace
- simulation
- tradeoff
- quadratic
stage: advanced
status: draft
---

# Savitch Theorem and Time-Space Tradeoffs

## Core Idea
Savitch's theorem proves PSPACE = NPSPACE: nondeterministic polynomial space equals deterministic polynomial space. Simulation requires squaring space (O(s²) for space s) but succeeds because space reusability bounds recursion depth. This contrasts sharply with time, where NP vs P remains open. Savitch highlights how time and space behave fundamentally differently in computational complexity.
