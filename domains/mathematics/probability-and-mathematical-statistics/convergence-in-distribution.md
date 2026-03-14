---
id: convergence-in-distribution
title: Convergence in Distribution
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: distribution-functions-densities-rigorous
  type: hard
- id: characteristic-functions
  type: soft
builds-toward:
- relationships-modes-convergence
- central-limit-theorem-rigorous
tags:
- convergence
- distribution
- limit-theorems
stage: abstract-reasoning
status: draft
---

# Convergence in Distribution

## Core Idea
Xₙ converges to X in distribution if lim_{n→∞} Fₙ(x) = F(x) at continuity points of F, or equivalently lim_{n→∞} φₙ(t) = φ(t) for all t. This is the weakest form of convergence—Xₙ and X need not be defined on the same probability space. Characteristic function convergence provides the most convenient criterion.
