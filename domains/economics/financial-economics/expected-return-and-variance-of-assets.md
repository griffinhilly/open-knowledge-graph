---
id: expected-return-and-variance-of-assets
title: Expected Return and Variance of Financial Assets
domain: economics
course: financial-economics
prerequisites:
- id: risk-and-return-tradeoff
  type: hard
- id: variance-of-random-variables
  type: hard
- id: normal-distribution-intro
  type: soft
- id: expected-value
  type: soft
builds-toward:
- portfolio-diversification
- mean-variance-optimization
tags:
- expected-return
- variance
- covariance
- asset-returns
- statistics
stage: formal-systems
status: draft
---

# Expected Return and Variance of Financial Assets

## Core Idea
The expected return of an asset is the probability-weighted average of its possible returns: E[r] = Σ pᵢrᵢ. Variance measures dispersion around the mean: σ² = Σ pᵢ(rᵢ − E[r])². For a portfolio of two assets with weights w₁ and w₂, portfolio variance is σ²_p = w₁²σ₁² + w₂²σ₂² + 2w₁w₂Cov(r₁,r₂). This covariance term is the key insight behind diversification: assets that do not move perfectly together reduce portfolio risk below the weighted average of individual risks. The magnitude of this reduction depends entirely on the correlation between the two assets.

## How It's Best Learned
Calculate expected return and variance from a probability distribution, then repeat using historical return data to see how the statistical formulas apply empirically. Compute two-asset portfolio variance at correlations of −1, 0, and +1 to see the full range of what diversification can achieve.

## Common Misconceptions
- Omitting the covariance term from portfolio variance is the most common calculation error and entirely misses the point of diversification.
- Assuming returns are normally distributed is convenient but wrong — financial returns exhibit fat tails and negative skewness that the normal distribution systematically underestimates.
