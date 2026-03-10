---
id: logit-probit-models
title: Logit and Probit Models for Binary Outcomes
domain: economics
course: econometrics
prerequisites:
- id: multiple-regression-model
  type: hard
- id: maximum-likelihood-econometrics
  type: hard
- id: normal-distribution-intro
  type: soft
- id: continuous-random-variables
  type: soft
tags:
- logit
- probit
- binary-outcome
- MLE
- marginal-effects
stage: formal-systems
status: draft
---

# Logit and Probit Models for Binary Outcomes

## Core Idea
When the dependent variable is binary (y ∈ {0,1}), the linear probability model (OLS on a dummy) can predict probabilities outside [0,1] and has heteroskedastic errors by construction. Logit and probit models instead model P(y=1|x) = F(x'β) where F is the logistic function (logit) or the standard normal CDF (probit), ensuring predicted probabilities lie in (0,1). Both are estimated by maximum likelihood, not OLS. Coefficients are not directly interpretable as marginal effects; marginal effects (dP/dx evaluated at the mean or averaged over the sample) are reported instead. Logit and probit produce similar results in practice; the choice is usually conventional.

## How It's Best Learned
Estimate a labor force participation model (binary) using LPM, logit, and probit on the same data. Compare predicted probabilities near 0 and 1 to see where LPM fails. Compute average marginal effects for the logit model.

## Common Misconceptions
- Logit coefficients are log-odds ratios, not probability changes — always compute and report marginal effects.
- Pseudo-R² statistics (McFadden, Nagelkerke) are not comparable to OLS R² and should not be interpreted as 'fraction of variance explained'.
