---
id: weak-law-of-large-numbers
title: Weak Law of Large Numbers
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: convergence-in-probability
  type: hard
- id: independence-sigma-algebras
  type: hard
- id: chebyshev-bounds
  type: soft
builds-toward:
- strong-law-of-large-numbers
- central-limit-theorem-rigorous
tags:
- law-of-large-numbers
- limit-theorems
- probability
stage: formal-systems
status: draft
---

# Weak Law of Large Numbers

## Core Idea
If {Xₙ} are i.i.d. random variables with finite mean μ, then Sₙ/n = (X₁ + ... + Xₙ)/n converges in probability to μ. The key assumption is finite variance (or more generally, applying Chebyshev's inequality). The weak LLN guarantees that sample means stabilize around the true mean, justifying empirical estimation.
