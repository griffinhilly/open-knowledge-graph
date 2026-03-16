---
id: multivariate-normal-distribution
title: Multivariate Normal Distribution
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: joint-distributions-marginals-rigorous
  type: hard
- id: characteristic-functions
  type: soft
- id: linear-transformations
  type: soft
builds-toward:
- central-limit-theorem-rigorous
- bayesian-inference-foundations
tags:
- multivariate-normal
- distributions
- statistics
stage: formal-systems
status: draft
---

# Multivariate Normal Distribution

## Core Idea
A random vector X ~ N(μ, Σ) has characteristic function φ(t) = exp(it'μ - ½t'Σt). The MVN is closed under linear transformations and marginals. A joint distribution is MVN if every linear combination of components is univariate normal. The MVN is fundamental in statistical inference because the sample mean vector is MVN for large samples.
