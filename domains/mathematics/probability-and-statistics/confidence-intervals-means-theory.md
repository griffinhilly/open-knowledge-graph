---
id: confidence-intervals-means-theory
title: Confidence Intervals for Population Means
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: standard-normal-z-scores-theory
  type: hard
- id: distribution-of-sample-mean-theory
  type: hard
builds-toward:
- hypothesis-testing-fundamentals
tags:
- confidence-interval
stage: formal-systems
status: draft
---

# Confidence Intervals for Population Means

## Core Idea
A 100(1−α)% CI for μ: X̄±z_{α/2}(σ/√n) when σ known, or X̄±t_{n-1,α/2}(s/√n) when unknown. Interpretation: 100(1−α)% of repeated CIs contain μ, NOT P(μ in CI)=1−α (μ is fixed, CI is random). t-distribution used because s estimates σ.
