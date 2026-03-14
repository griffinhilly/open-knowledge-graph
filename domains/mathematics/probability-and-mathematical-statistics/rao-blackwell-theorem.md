---
id: rao-blackwell-theorem
title: The Rao-Blackwell Theorem
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: conditional-expectation
  type: hard
- id: sufficient-statistics
  type: soft
builds-toward:
- umvue
tags:
- rao-blackwell
- sufficient-statistics
- variance-reduction
stage: abstract-reasoning
status: draft
---

# The Rao-Blackwell Theorem

## Core Idea
If T̂ is an unbiased estimator of g(θ) and S is sufficient, then T̃ = E[T̂|S] is unbiased with Var(T̃) ≤ Var(T̂). Conditioning on a sufficient statistic reduces variance without increasing bias. This provides a systematic method for improving unbiased estimators.
