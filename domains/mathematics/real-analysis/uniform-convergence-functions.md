---
id: uniform-convergence-functions
title: Uniform Convergence
domain: mathematics
course: real-analysis
prerequisites:
- id: pointwise-convergence-functions
  type: hard
builds-toward:
- uniform-convergence-preserves-continuity
- weierstrass-m-test
- interchange-limit-integral
- interchange-limit-derivative
tags:
- uniform-convergence
- function-sequences
- strengthened
stage: advanced
status: draft
---

# Uniform Convergence

## Core Idea
A sequence of functions (fₙ) converges uniformly to f on a set S if for every ε > 0, there exists N (independent of x) such that for all x ∈ S, n > N implies |fₙ(x) - f(x)| < ε. Uniform convergence is stronger than pointwise and guarantees that limits can be exchanged with derivatives and integrals. It is fundamental to analysis on function spaces.
