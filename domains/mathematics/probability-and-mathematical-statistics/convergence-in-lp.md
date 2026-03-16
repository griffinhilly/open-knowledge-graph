---
id: convergence-in-lp
title: Convergence in L^p
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: expectation-measure-theoretic
  type: hard
- id: inner-product-spaces
  type: soft
builds-toward:
- relationships-modes-convergence
tags:
- convergence
- lp-spaces
- functional-analysis
stage: formal-systems
status: draft
---

# Convergence in L^p

## Core Idea
Xₙ converges to X in L^p if lim_{n→∞} E[|Xₙ - X|^p] = 0, equivalently ||Xₙ - X||_p → 0 in the L^p norm. L^p spaces form a Banach space of random variables with finite p-th moment. Convergence in L² (mean square convergence) is particularly important because it preserves inner products.
