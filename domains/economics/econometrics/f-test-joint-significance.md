---
id: f-test-joint-significance
title: F-Test and Joint Significance
domain: economics
course: econometrics
prerequisites:
- id: hypothesis-testing-regression
  type: hard
- id: anova-one-way
  type: soft
builds-toward:
- r-squared-and-model-fit
- multiple-regression-model
tags:
- F-test
- joint-significance
- model-testing
stage: formal-systems
status: draft
---

# F-Test and Joint Significance

## Core Idea
The F-test evaluates whether a set of coefficients is jointly statistically significant, testing the null hypothesis that all slope coefficients equal zero simultaneously. The overall F-statistic compares the explained variance in the restricted model (intercept only) to the full model; individual t-tests cannot perform this joint test without inflating Type I error. F-tests also apply to linear restrictions — for instance, testing whether two coefficients are equal. The F-statistic follows an F-distribution with (q, n−k−1) degrees of freedom, where q is the number of restrictions being tested.

## Common Misconceptions
- Individually insignificant coefficients can be jointly significant — this matters when regressors are correlated.
- The overall F-test rejecting the null does not mean every individual variable matters, only that the model as a whole has predictive content.
