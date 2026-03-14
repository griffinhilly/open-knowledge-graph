---
id: multiple-regression-intro
title: Introduction to Multiple Linear Regression
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: linear-regression
  type: hard
tags:
- regression
- multiple-regression
- multivariate
stage: formal-systems
status: draft
---

# Introduction to Multiple Linear Regression

## Core Idea
Multiple linear regression extends simple regression to many predictors: E[Y|X₁,...,Xₚ] = β₀ + β₁X₁ + ... + βₚXₚ. Coefficients represent partial effects (adjusted for other predictors). Model selection and multicollinearity are key concerns.

## How It's Best Learned
Fit multiple regression models with software. Compare nested models using F-tests. Examine variance inflation factors (VIF) for multicollinearity. Interpret partial slopes as adjusted effects. Use visualization and residual diagnostics.

## Common Misconceptions
Interpreting regression coefficients causally without experimentation. Ignoring multicollinearity and its effects on interpretability. Believing all significant predictors should be included. Overfitting with too many predictors.
