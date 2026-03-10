---
id: ols-assumptions
title: Classical OLS Assumptions (Gauss-Markov)
domain: economics
course: econometrics
prerequisites:
- id: bivariate-regression
  type: hard
- id: expected-value
  type: hard
- id: random-variables-intro
  type: hard
- id: variance-of-random-variables
  type: soft
builds-toward:
- multiple-regression-model
- heteroskedasticity
- serial-correlation
- omitted-variable-bias
tags:
- Gauss-Markov
- BLUE
- assumptions
- unbiasedness
stage: formal-systems
status: draft
---

# Classical OLS Assumptions (Gauss-Markov)

## Core Idea
The Gauss-Markov theorem states that OLS is the Best Linear Unbiased Estimator (BLUE) when six classical assumptions hold: linearity in parameters, random sampling, no perfect multicollinearity, zero conditional mean of errors (E[u|x]=0), homoskedasticity, and no serial correlation. The most critical assumption is E[u|x]=0, which requires that all determinants of y omitted from the model are uncorrelated with x. When this assumption fails — due to omitted variables, measurement error, or simultaneity — OLS estimates are biased and inconsistent. The remaining assumptions govern efficiency rather than unbiasedness.

## How It's Best Learned
Work through examples of each assumption violation — simulate data with heteroskedastic errors, then see how OLS still estimates coefficients correctly (unbiased) but standard errors are wrong. This separates biasedness from inefficiency.

## Common Misconceptions
- Violating homoskedasticity biases standard errors, not coefficients — a common confusion.
- The 'linearity' assumption applies to parameters (β), not to the functional form of x; including x² is still 'linear in parameters'.
