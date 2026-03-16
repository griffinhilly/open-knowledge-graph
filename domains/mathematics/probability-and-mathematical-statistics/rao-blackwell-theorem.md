---
id: rao-blackwell-theorem
title: Rao-Blackwell Theorem
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: umvue
  type: soft
- id: conditional-expectation
  type: hard
- id: sufficient-statistics
  type: hard
builds-toward:
- bayesian-point-estimation
tags:
- rao-blackwell
- unbiased-estimation
- statistics
stage: advanced
status: draft
---

# Rao-Blackwell Theorem

## Core Idea
If T is an unbiased estimator of θ and S is a sufficient statistic, then φ = E[T|S] is unbiased for θ and Var(φ) ≤ Var(T). This theorem shows how to improve unbiased estimators by conditioning on sufficient statistics. Combined with completeness, it yields UMVUEs.
