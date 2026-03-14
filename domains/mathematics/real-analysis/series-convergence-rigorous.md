---
id: series-convergence-rigorous
title: Rigorous Series Convergence
domain: mathematics
course: real-analysis
prerequisites:
- id: epsilon-n-convergence
  type: hard
- id: series-convergence-tests
  type: soft
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
A series ∑aₙ converges to S if its sequence of partial sums Sₙ = a₁ + ... + aₙ converges to S in the ε-N sense. Series are limits of sequences of partial sums, so all tools for sequences (monotone convergence, Cauchy criterion) apply. A series converges if and only if its partial sums form a Cauchy sequence.
