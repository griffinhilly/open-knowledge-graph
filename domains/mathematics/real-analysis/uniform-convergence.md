---
id: uniform-convergence
title: Uniform Convergence
domain: mathematics
course: real-analysis
prerequisites:
- id: pointwise-convergence-function-sequences
  type: hard
builds-toward:
- uniform-convergence-preserves-continuity
- interchange-limit-integral
- weierstrass-m-test
tags:
- uniform-convergence
- function-sequences
- limits
stage: advanced
status: draft
---

# Uniform Convergence

## Core Idea
A sequence (fₙ) converges uniformly to f on S if for every ε > 0, there exists N (depending only on ε, not on x) such that for all n > N and all x in S, |fₙ(x) − f(x)| < ε. Uniform convergence is stronger than pointwise and preserves many properties: limits of continuous functions are continuous, we can interchange limit and integral, etc.
