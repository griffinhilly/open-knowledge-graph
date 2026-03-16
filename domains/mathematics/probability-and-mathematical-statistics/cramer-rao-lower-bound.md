---
id: cramer-rao-lower-bound
title: Cramer-Rao Lower Bound
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: fisher-information
  type: hard
- id: variance-higher-moments-rigorous
  type: hard
builds-toward:
- umvue
- asymptotic-normality-mle
tags:
- cramer-rao
- lower-bounds
- estimation
stage: advanced
status: draft
---

# Cramer-Rao Lower Bound

## Core Idea
For any unbiased estimator T of θ, Var(T) ≥ 1/I(θ). The bound is tight: equality holds iff T is the uniformly minimum variance unbiased estimator (UMVUE). The CRLB shows that Fisher information lower-bounds estimator precision. MLEs are asymptotically efficient, achieving the CRLB in the limit.
