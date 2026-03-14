---
id: parameterized-complexity-fpt
title: Parameterized Complexity and Fixed-Parameter Tractability
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: np-completeness-theorem
  type: hard
- id: approximation-algorithms
  type: soft
tags:
- parameterized-complexity
- fpt
- kernelization
- w-hierarchy
stage: advanced
status: draft
---

# Parameterized Complexity and Fixed-Parameter Tractability

## Core Idea
Parameterized complexity classifies problems not just by input size n but by a secondary parameter k. A problem is fixed-parameter tractable (FPT) if solvable in time f(k)·poly(n) for some function f. Many NP-hard problems (like vertex cover with parameter size k) are FPT, offering a refined view of tractability beyond P versus NP.
