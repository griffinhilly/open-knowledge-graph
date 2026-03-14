---
id: weak-law-of-large-numbers
title: Weak Law of Large Numbers
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: convergence-in-probability
  type: hard
- id: chebyshev-bounds
  type: soft
builds-toward:
- method-of-moments
- consistency-of-estimators
tags:
- limit-theorems
- lln
- average
stage: abstract-reasoning
status: draft
---

# Weak Law of Large Numbers

## Core Idea
If X_1, X_2, ... are i.i.d. with E[X_i] = μ, then the sample mean (X_1 + ... + X_n)/n converges in probability to μ. This justifies using empirical averages to estimate population means. The proof uses Chebyshev's inequality; it extends to dependent variables under mixing conditions.
