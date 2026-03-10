---
id: mean-variance-optimization
title: Mean-Variance Optimization (Markowitz Framework)
domain: economics
course: financial-economics
prerequisites:
- id: portfolio-diversification
  type: hard
- id: expected-return-and-variance-of-assets
  type: hard
builds-toward:
- efficient-frontier-portfolio-theory
- capital-asset-pricing-model
tags:
- markowitz
- portfolio-optimization
- covariance-matrix
- modern-portfolio-theory
stage: formal-systems
status: draft
---

# Mean-Variance Optimization (Markowitz Framework)

## Core Idea
Harry Markowitz (1952) formalized portfolio selection as an optimization problem: for any target expected return, find the portfolio weights that minimize variance, subject to weights summing to one. The inputs are expected returns, variances, and all pairwise covariances — summarized in the covariance matrix. Solving this quadratic optimization for all feasible return levels traces out the minimum-variance frontier, and the upper portion — where no portfolio can offer higher expected return for the same variance — is the efficient frontier. This was the first rigorous mathematical treatment of diversification, earning Markowitz a Nobel Prize in Economics in 1990.

## How It's Best Learned
Set up the optimization in matrix form for three assets to see the role of the covariance matrix. Use software (Python/scipy or Excel Solver) to trace the full efficient frontier. Observe how the frontier shifts when correlations change, highlighting the central role of covariance structure.

## Common Misconceptions
- The framework does not identify a unique 'best' portfolio — it gives a frontier; the investor's risk tolerance determines which point on the frontier is optimal.
- The framework is extremely sensitive to expected return inputs — small estimation errors produce large changes in optimal weights, limiting practical reliability.
