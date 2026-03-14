---
id: polynomial-regression-econometrics
title: Polynomial Regression and Nonlinear Functional Forms
domain: economics
course: econometrics
prerequisites:
- id: multiple-regression-model
  type: hard
- id: coefficient-interpretation-regression
  type: hard
builds-toward:
- nonlinear-models-interpretation
- specification-tests-econometrics
tags:
- regression
- nonlinear
- functional-forms
stage: formal-systems
status: draft
---

# Polynomial Regression and Nonlinear Functional Forms

## Core Idea
Polynomial terms (x², x³) extend linear regression to capture nonlinear relationships where the slope changes across values of the regressor. This allows U-shaped, inverted-U, or more complex patterns without requiring a fully nonlinear model.

## How It's Best Learned
Fit polynomials of increasing degree and compare using scatter plots and statistical tests. Use domain knowledge and data visualization to choose the degree rather than maximizing R².

## Common Misconceptions
Higher-degree polynomials always fit the data better in-sample but often overfit and perform poorly out-of-sample. Interpretation of raw coefficients becomes difficult; focus on marginal effects or predicted values instead.
