---
id: nonlinear-models-interpretation
title: Interpretation and Marginal Effects in Nonlinear Models
domain: economics
course: econometrics
prerequisites:
- id: logit-probit-models
  type: hard
- id: maximum-likelihood-econometrics
  type: hard
tags:
- nonlinear
- interpretation
- marginal-effects
stage: formal-systems
status: draft
---

# Interpretation and Marginal Effects in Nonlinear Models

## Core Idea
In logit, probit, and other nonlinear models, raw coefficients do not represent marginal effects on the outcome. The effect of a unit change in X depends on both the coefficient and the probability/density evaluated at specific covariate values.

## How It's Best Learned
Calculate marginal effects at the mean (MEM) and average marginal effects (AME) for a few key variables. Use plots to show how predicted probabilities change across the range of X.
