---
id: maximum-likelihood-econometrics
title: Maximum Likelihood Estimation
domain: economics
course: econometrics
prerequisites:
- id: ols-assumptions
  type: hard
- id: normal-distribution-intro
  type: hard
- id: sampling-distributions
  type: hard
- id: partial-derivatives
  type: soft
- id: probability-axioms
  type: soft
- id: optimization-problems
  type: soft
- id: natural-logarithm-and-e
  type: soft
builds-toward:
- logit-probit-models
tags:
- MLE
- likelihood
- log-likelihood
- consistency
- asymptotic
stage: formal-systems
status: validated
---

# Maximum Likelihood Estimation

## Core Idea
Maximum likelihood estimation (MLE) finds the parameter values that make the observed data most probable under a specified distributional model. The log-likelihood function ℓ(θ) = Σᵢ log f(yᵢ; θ) is maximized with respect to θ, typically requiring numerical optimization. MLE estimators are consistent and asymptotically efficient (achieving the Cramér-Rao lower bound) under correct model specification. Under normality, OLS and MLE are equivalent for linear regression. When the distributional form is wrong, MLE can be inconsistent — quasi-MLE is a robust alternative that still provides consistent estimates for certain parameters like means.

## How It's Best Learned
Derive the MLE estimator for the mean of a normal distribution by hand — this makes the logic of maximizing the likelihood concrete before applying it to more complex models like logit.

## Common Misconceptions
- MLE requires a correctly specified distributional assumption; when in doubt, OLS with robust standard errors is safer for linear models.
- The MLE is not always the most intuitive estimator — in small samples it can be biased (e.g., the MLE for the normal variance divides by n, not n−1).
