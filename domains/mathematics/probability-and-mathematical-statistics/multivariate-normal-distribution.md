---
id: multivariate-normal-distribution
title: Multivariate Normal Distribution
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: central-limit-theorem-rigorous
  type: soft
- id: distribution-and-density-functions
  type: hard
- id: matrix-operations
  type: soft
builds-toward:
- asymptotic-normality-of-mle
tags:
- multivariate
- normal-distribution
- gaussian
stage: abstract-reasoning
status: draft
---

# Multivariate Normal Distribution

## Core Idea
A random vector X ∈ ℝ^k follows N(μ, Σ) if every linear combination is univariate normal. The density is f(x) = (2π)^{-k/2}|Σ|^{-1/2} exp(-½(x-μ)'Σ^{-1}(x-μ)). Marginals and conditionals are normal. The multivariate CLT yields multivariate normality of limiting distributions.
