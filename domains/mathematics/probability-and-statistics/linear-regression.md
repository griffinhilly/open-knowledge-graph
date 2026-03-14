---
id: linear-regression
title: Simple Linear Regression
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: correlation-coefficient
  type: hard
- id: slope-concept
  type: soft
- id: writing-linear-equations
  type: soft
builds-toward:
- residuals-and-goodness-of-fit
tags:
- linear-regression
- least-squares
- slope
- intercept
- prediction
stage: formal-systems
status: validated
---
# Simple Linear Regression

## Core Idea
Simple linear regression fits a line ŷ = b₀ + b₁x to data by minimizing the sum of squared residuals (least squares). The slope b₁ = r · (sᵧ/sₓ) and intercept b₀ = ȳ − b₁x̄ are uniquely determined by the data. The regression line always passes through (x̄, ȳ). The slope represents the predicted change in y per one-unit increase in x, and predictions should only be made within the observed range of x (avoiding extrapolation).

## How It's Best Learned
Use real datasets: predict college GPA from SAT scores, or fuel efficiency from car weight. Have students interpret slope in context ('for each additional 100 lbs, fuel efficiency decreases by 0.5 mpg'). Explicitly warn against extrapolation with vivid examples of absurd predictions outside the data range.

## Common Misconceptions
- Switching predictor and response variables changes the regression line — y on x ≠ x on y.
- Interpreting the y-intercept as meaningful when x = 0 is outside the data range.
- Using regression for prediction when the relationship is clearly nonlinear.
