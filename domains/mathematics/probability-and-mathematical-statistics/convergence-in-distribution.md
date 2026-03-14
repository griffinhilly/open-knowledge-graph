---
id: convergence-in-distribution
title: Convergence in Distribution (Weak Convergence)
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: characteristic-functions
  type: hard
- id: distribution-and-density-functions
  type: soft
builds-toward:
- central-limit-theorem-rigorous
- relationships-between-modes-of-convergence
tags:
- convergence
- distribution
- weak-convergence
stage: abstract-reasoning
status: draft
---

# Convergence in Distribution (Weak Convergence)

## Core Idea
Random variables X_n converge in distribution to X if CDFs F_n(x) → F(x) at continuity points of F. Equivalently, characteristic functions φ_n(t) → φ(t) for all t. The limiting X need not exist on the same probability space as the X_n.
