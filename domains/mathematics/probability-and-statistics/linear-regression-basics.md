---
id: linear-regression-basics
title: Linear Regression Basics
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: correlation-coefficient
  type: hard
builds-toward:
- residuals-and-goodness-of-fit
tags:
- regression
- least-squares
- prediction
- slope-intercept
stage: formal-systems
status: draft
---

# Linear Regression Basics

## Core Idea
Linear regression fits a line y = a + bx to paired data (xᵢ, yᵢ) by minimizing the sum of squared residuals. The slope b measures the change in y per unit change in x; the intercept a is y when x = 0. The regression line passes through (x̄, ȳ) and its slope is b = r × (s_y/s_x). Linear regression enables prediction and quantifies linear relationships, though predictions outside the data range (extrapolation) are unreliable.

## How It's Best Learned
Fit regression lines to scatterplots. Interpret slope in context. Use regression to make predictions and discuss uncertainty. Compare fitted values to observed values (residuals).

## Common Misconceptions
Thinking regression assumes causation. Using regression for severely nonlinear data. Extrapolating far beyond the data range with confidence. Confusing the fitted value with the data point.
