---
id: cramer-rao-lower-bound
title: The Cramér-Rao Lower Bound
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: fisher-information
  type: hard
- id: expectation-measure-theoretic
  type: soft
builds-toward:
- umvue
- consistency-of-estimators
tags:
- cramer-rao
- bounds
- variance
stage: abstract-reasoning
status: draft
---

# The Cramér-Rao Lower Bound

## Core Idea
For an unbiased estimator T̂ of θ, Var(T̂) ≥ 1/I(θ) where I(θ) is Fisher information. This universal bound reveals the fundamental limit on estimation precision. Estimators achieving the bound have variance 1/I(θ) and are asymptotically efficient (UMVUEs).
