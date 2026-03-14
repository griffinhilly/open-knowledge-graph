---
id: parameterized-complexity-fundamentals
title: Parameterized Complexity and Fixed-Parameter Tractability
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: np-completeness-formal
  type: hard
- id: polynomial-time-reductions
  type: soft
builds-toward:
- kolmogorov-complexity-properties
tags:
- parameterized-complexity
- FPT
- kernelization
stage: advanced
status: draft
---

# Parameterized Complexity and Fixed-Parameter Tractability

## Core Idea
Parameterized complexity treats problem instances as pairs (x, k) where k is a parameter (e.g., solution size). An NP-hard problem can be fixed-parameter tractable (FPT) if solvable in time f(k) · poly(|x|), making it practical for small parameters despite NP-hardness. This framework explains why many intractable problems become tractable on restricted inputs and guides algorithm design.
