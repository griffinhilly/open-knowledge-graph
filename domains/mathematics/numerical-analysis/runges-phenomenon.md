---
id: runges-phenomenon
title: Runge's Phenomenon
domain: mathematics
course: numerical-analysis
prerequisites:
- id: lagrange-polynomial-interpolation
  type: hard
- id: interpolation-error-analysis
  type: hard
builds-toward:
- chebyshev-nodes-optimal-interpolation
tags:
- runges-phenomenon
- oscillation
- equally-spaced-nodes
stage: advanced
status: draft
---

# Runge's Phenomenon

## Core Idea
Runge's phenomenon demonstrates that increasing the degree of polynomial interpolation with equally-spaced nodes can increase rather than decrease error, particularly near the interval boundaries. The nodal polynomial oscillates wildly with large magnitude away from the central cluster of roots, amplifying even moderate derivatives. This fundamental limitation motivates the use of nonuniform node placement.
