---
id: runges-phenomenon
title: Runge's Phenomenon
domain: mathematics
course: numerical-analysis
prerequisites:
- id: interpolation-error-analysis
  type: hard
builds-toward:
- chebyshev-nodes
- cubic-spline-interpolation
tags:
- runges-phenomenon
- oscillation
- interpolation
stage: abstract-reasoning
status: draft
---

# Runge's Phenomenon

## Core Idea
For certain smooth functions like f(x) = 1/(1+x²), polynomial interpolation on equally-spaced nodes exhibits wild oscillations that grow unboundedly as the number of nodes increases. This Runge phenomenon demonstrates that increasing polynomial degree with equally-spaced nodes is not a reliable path to better approximation. The root cause is the large node product |∏(x - x_i)| near the interval endpoints.
