---
id: rigorous-series-convergence
title: Rigorous Series Convergence
domain: mathematics
course: real-analysis
prerequisites:
- id: series-convergence-tests
  type: hard
- id: epsilon-n-convergence
  type: hard
builds-toward:
- absolute-convergence-rearrangement
- uniform-convergence-power-series
tags:
- series
- convergence
- partial-sums
stage: abstract-reasoning
status: draft
---

# Rigorous Series Convergence

## Core Idea
A series ∑ aₙ converges to S if the sequence of partial sums Sₙ = a₁ + a₂ + ... + aₙ converges to S using epsilon-N. A series converges if and only if it is Cauchy: for every ε > 0, there exists N such that for all n > m ≥ N, |Sₙ − Sₘ| < ε. This provides a rigorous foundation for all convergence tests.
