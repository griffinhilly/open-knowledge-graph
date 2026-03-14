---
id: interpolation-error-analysis
title: Interpolation Error Analysis
domain: mathematics
course: numerical-analysis
prerequisites:
- id: newton-divided-differences
  type: hard
- id: taylor-series
  type: hard
builds-toward:
- runges-phenomenon
- chebyshev-nodes
tags:
- error-analysis
- interpolation
- bounds
stage: abstract-reasoning
status: draft
---

# Interpolation Error Analysis

## Core Idea
If P(x) interpolates f at n+1 points, the error E(x) = f(x) - P(x) satisfies |E(x)| ≤ (max |f^{(n+1)}|)/(n+1)! |∏(x - x_i)|. This bound reveals that error depends on the (n+1)-th derivative of f and the magnitude of the node product. For smooth functions with well-chosen nodes, interpolation error can be very small; poor node placement causes large errors.
