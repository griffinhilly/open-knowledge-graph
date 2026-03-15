---
id: heteroskedasticity
title: Heteroskedasticity
domain: economics
course: econometrics
prerequisites:
- id: ols-assumptions
  type: hard
- id: variance-of-random-variables
  type: hard
- id: residuals-and-goodness-of-fit
  type: soft
- id: probability-axioms
  type: soft
builds-toward:
- robust-standard-errors
tags:
- heteroskedasticity
- variance
- Breusch-Pagan
- White-test
stage: formal-systems
status: validated
---

# Heteroskedasticity

## Core Idea
Heteroskedasticity means the variance of the regression error u is not constant across observations: Var(u|x) ≠ σ². This violates the Gauss-Markov homoskedasticity assumption, so OLS remains unbiased but is no longer efficient, and reported standard errors are incorrect (usually too small), making inference invalid. It is common in cross-sectional economic data — for instance, expenditure variance typically rises with income. The Breusch-Pagan and White tests formally detect heteroskedasticity. The practical remedy is heteroskedasticity-robust standard errors, which produce valid inference without changing the coefficient estimates.

## How It's Best Learned
Plot residuals against fitted values — a fan-shaped pattern indicates heteroskedasticity. Compare conventional and robust standard errors on real data to see how inference changes.

## Common Misconceptions
- Heteroskedasticity does not bias β̂, only its standard errors — so point estimates may still be meaningful.
- Weighted least squares (WLS) is optimal under known heteroskedasticity structure, but robust standard errors are preferred when the form is unknown.
