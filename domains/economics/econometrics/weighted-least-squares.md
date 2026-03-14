---
id: weighted-least-squares
title: Weighted Least Squares (WLS)
domain: economics
course: econometrics
prerequisites:
- id: heteroskedasticity
  type: hard
- id: generalized-least-squares
  type: hard
tags:
- wls
- heteroskedasticity
- weights
stage: formal-systems
status: draft
---

# Weighted Least Squares (WLS)

## Core Idea
WLS applies inverse-variance weights to observations to correct for heteroskedasticity. High-variance observations receive lower weight, improving efficiency when the variance structure is known or can be estimated.

## How It's Best Learned
Estimate the variance function from residuals, then use predicted variances as weights in a second-stage regression. Compare WLS standard errors to OLS standard errors to verify the efficiency gain.
