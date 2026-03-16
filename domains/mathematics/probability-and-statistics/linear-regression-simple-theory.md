---
id: linear-regression-simple-theory
title: 'Simple Linear Regression: Theory and Estimation'
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: linear-regression-basics
  type: soft
- id: covariance-correlation-theory
  type: hard
builds-toward:
- inference-in-linear-regression
- regression-diagnostics
tags:
- linear-regression
stage: formal-systems
status: draft
---

# Simple Linear Regression: Theory and Estimation

## Core Idea
Fit Y=β₀+β₁X+ε by minimizing Σε². Least squares: β₁=Cov(X,Y)/Var(X)=r(s_Y/s_X), β₀=Ȳ−β₁X̄. Under normality, LS is MLE. R²=correlation² is proportion of Y variance explained. Residuals ê_i=y_i−ŷ_i should be random.

## Explainer

You already know that covariance and correlation measure how two variables move together. Simple linear regression takes that relationship and converts it into a predictive machine: given X, what is our best guess for Y? The model posits a straight line Y = β₀ + β₁X + ε, where ε represents random noise. The question becomes: which line fits best?

**Ordinary least squares (OLS)** answers that by minimizing the sum of squared residuals — the vertical distances between each observed point and the proposed line. Squaring the errors penalizes large misses more than small ones, making the solution unique and analytically tractable. Taking derivatives and setting them to zero yields the formulas: β₁ = Cov(X,Y)/Var(X) and β₀ = Ȳ − β₁X̄. Notice the slope formula: it is covariance (how much X and Y move together) scaled by variance (how spread-out X is). If X and Y are unrelated, Cov = 0, so β₁ = 0 — a flat line that ignores X entirely.

The equivalent form β₁ = r(sY/sX) gives a second interpretation. The correlation r captures the direction and strength of the relationship; the ratio sY/sX rescales it from correlation units into the actual units of Y per unit of X. This is why two datasets can have the same correlation but very different slopes — the slopes also depend on the relative spread of the variables.

**R²** — the coefficient of determination — measures how much of Y's total variation the model explains. It equals r² = 1 − SSRes/SSTotal, ranging from 0 (the line explains nothing beyond the mean) to 1 (perfect fit). Since R² is the square of the correlation, all the intuition you built about correlation directly transfers. After fitting, always inspect the **residuals** ê_i = y_i − ŷ_i. If the model is correctly specified, residuals should look like random noise: no pattern, no fan shape, no curve. Any structure in the residuals signals a problem — the relationship may be nonlinear, or the variance may change with X — and points toward the regression diagnostics you will study next.
