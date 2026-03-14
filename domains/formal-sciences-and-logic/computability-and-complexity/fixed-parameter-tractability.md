---
id: fixed-parameter-tractability
title: Fixed-Parameter Tractability (FPT)
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: np-completeness-formal
  type: hard
- id: vertex-cover-problem
  type: soft
tags:
- parameterized-complexity
- tractable-hardness
- algorithms
stage: advanced
status: draft
---

# Fixed-Parameter Tractability (FPT)

## Core Idea
Fixed-parameter tractability asks: while a problem is NP-hard in general, can it be solved in time f(k)·n^O(1) where k is a problem parameter (like solution size) and f is an arbitrary computable function? A problem is FPT if such algorithms exist. For instance, vertex cover is FPT parameterized by cover size k, though NP-complete in general. FPT provides a refined complexity landscape beyond classical NP-hardness.
