---
id: variance-higher-moments-rigorous
title: Variance and Higher Moments (Rigorous)
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: expectation-measure-theoretic
  type: hard
- id: variance-of-random-variables
  type: soft
builds-toward:
- moment-generating-functions
- characteristic-functions
- convergence-in-lp
tags:
- moments
- variance
- measure-theory
stage: abstract-reasoning
status: draft
---

# Variance and Higher Moments (Rigorous)

## Core Idea
The k-th moment of X is μₖ = E[Xᵏ], which exists if E[|X|ᵏ] < ∞. Variance Var(X) = E[(X - E[X])²] measures spread; higher central moments μₖ = E[(X - E[X])ᵏ] capture skewness (k=3) and kurtosis (k=4). Hölder's inequality and Jensen's inequality are key tools relating moments.
