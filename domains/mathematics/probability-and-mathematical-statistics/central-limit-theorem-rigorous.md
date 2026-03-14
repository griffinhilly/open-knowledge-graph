---
id: central-limit-theorem-rigorous
title: Central Limit Theorem (Rigorous via Characteristic Functions)
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: characteristic-functions
  type: hard
- id: convergence-in-distribution
  type: hard
- id: normal-distribution-intro
  type: soft
builds-toward:
- asymptotic-normality-of-mle
- confidence-intervals-rigorous
tags:
- clt
- limit-theorems
- normal-approximation
stage: abstract-reasoning
status: draft
---

# Central Limit Theorem (Rigorous via Characteristic Functions)

## Core Idea
If X_1, X_2, ... are i.i.d. with E[X_i] = μ and Var(X_i) = σ², then √n(X̄_n - μ)/σ converges in distribution to N(0,1). The rigorous proof uses the continuity theorem: characteristic functions of the normalized sum converge pointwise to the standard normal's. The CLT holds for arbitrary distributions (finite variance) and is the foundation of statistical inference.
