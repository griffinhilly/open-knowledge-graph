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
- relationships-between-modes-of-convergence
tags:
- convergence
- lp-spaces
- norms
stage: abstract-reasoning
status: draft
---

# Convergence in L^p

## Core Idea
Random variables X_n converge in L^p to X if E[|X_n - X|^p] → 0, with norm ||X||_p = (E[|X|^p])^{1/p}. L^2 convergence (mean square convergence) is particularly important and implies convergence in probability. These spaces form complete normed vector spaces (Banach spaces).
