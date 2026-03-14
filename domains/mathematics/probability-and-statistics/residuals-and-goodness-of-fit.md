---
id: residuals-and-goodness-of-fit
title: Residuals and Goodness of Fit (R²)
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: linear-regression
  type: hard
tags:
- residuals
- R-squared
- goodness-of-fit
- residual-plots
- model-diagnostics
stage: formal-systems
status: validated
---

# Residuals and Goodness of Fit (R²)

## Core Idea
A residual is the difference between an observed y value and the predicted value ŷ from the regression line: eᵢ = yᵢ − ŷᵢ. Residual plots (residuals vs. fitted values or vs. predictor) reveal whether the linear model is appropriate — random scatter around zero indicates a good fit, while patterns suggest the model is misspecified. The coefficient of determination R² = r² gives the proportion of variability in y explained by the linear model, ranging from 0 (no explanatory power) to 1 (perfect linear fit).

## How It's Best Learned
Generate residual plots from regression output in software and practice recognizing patterns: funnel shapes indicate non-constant variance, curved patterns indicate nonlinearity. Connect R² to correlation: if r = 0.8, then R² = 0.64 — 64% of variation in y is explained by x.

## Common Misconceptions
- Thinking R² = 0.7 means 70% of data points are on or near the regression line.
- Treating a high R² as definitive proof the model is appropriate — always check residual plots.
- Confusing R² for simple regression (= r²) with adjusted R² from multiple regression.
