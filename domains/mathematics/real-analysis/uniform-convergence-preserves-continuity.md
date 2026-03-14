---
id: uniform-convergence-preserves-continuity
title: Uniform Convergence Preserves Continuity
domain: mathematics
course: real-analysis
prerequisites:
- id: uniform-convergence-functions
  type: hard
- id: epsilon-delta-continuity
  type: hard
builds-toward:
- interchange-limit-integral
- weierstrass-approximation-theorem
tags:
- uniform-convergence
- continuity
- preservation
stage: abstract-reasoning
status: draft
---

# Uniform Convergence Preserves Continuity

## Core Idea
If (fₙ) converges uniformly to f and each fₙ is continuous, then f is continuous. This is the key theorem justifying when lim can be exchanged with continuity and derivatives. Pointwise convergence does not guarantee this: fₙ(x) = xⁿ on [0,1] is pointwise but not uniformly convergent to the discontinuous step function.
