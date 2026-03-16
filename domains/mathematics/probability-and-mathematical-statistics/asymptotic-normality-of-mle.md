---
id: asymptotic-normality-of-mle
title: Asymptotic Normality of the MLE
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: maximum-likelihood-estimation-theory
  type: hard
- id: central-limit-theorem-rigorous
  type: hard
- id: fisher-information
  type: soft
builds-toward:
- confidence-intervals-rigorous
tags:
- mle
- asymptotics
- normal-approximation
stage: advanced
status: draft
---

# Asymptotic Normality of the MLE

## Core Idea
Under regularity conditions, √n(θ̂_n - θ) converges in distribution to N(0, I(θ)^{-1}), so θ̂_n ≈ N(θ, I(θ)^{-1}/n) for large n. The convergence rate is √n and the asymptotic variance achieves the Cramér-Rao lower bound (asymptotic efficiency). This enables construction of confidence intervals and hypothesis tests.
