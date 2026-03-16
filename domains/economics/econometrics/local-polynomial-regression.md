---
id: local-polynomial-regression
title: Local Polynomial Regression and Bandwidth Selection
domain: economics
course: econometrics
prerequisites:
- id: regression-discontinuity
  type: soft
tags:
- local-polynomial
- nonparametric
- bandwidth
stage: formal-systems
status: draft
---

# Local Polynomial Regression and Bandwidth Selection

## Core Idea
Local polynomial regression fits a polynomial within a neighborhood around each point, producing a nonparametric estimate of conditional expectations. Bandwidth (window size) controls smoothness; larger bandwidth reduces variance but increases bias.

## Explainer

From regression discontinuity design, you already know the motivation: near a threshold, you need to estimate what the outcome would have been on each side had no discontinuity existed. You do this by fitting a regression line or curve to the data on each side and extrapolating to the cutoff. But what function should you fit? Ordinary least squares assumes a global linear or polynomial relationship — a strong assumption. Local polynomial regression relaxes this entirely: instead of fitting one function to all the data, it fits a separate polynomial in a **bandwidth** window around each evaluation point, using only observations nearby.

The mechanics work like this. Pick a point x₀ where you want to estimate the conditional expectation E[Y|X = x₀]. Collect all observations within a bandwidth h of x₀. Fit a polynomial (degree 0 = local mean, degree 1 = local linear, degree 2 = local quadratic) to those observations, weighting nearby points more heavily than distant ones using a **kernel function** — typically a triangular or Epanechnikov kernel that assigns zero weight to observations outside the bandwidth. The fitted value at x₀ is your estimate. Slide x₀ across the full range of X and the resulting curve is the local polynomial estimate.

**Bandwidth selection** is the central tuning decision and involves a fundamental **bias-variance tradeoff** you first encountered in statistical modeling. A narrow bandwidth uses only observations very close to x₀, giving a highly local fit with low bias (no need to extrapolate across a wide range) but high variance (few observations, noisy estimate). A wide bandwidth borrows strength from more observations, reducing variance, but forces the local polynomial to approximate the true function over a larger range, introducing bias if the true function curves. Optimal bandwidth minimizes mean squared error, which balances these forces — the standard approach is **cross-validation** or the **plug-in bandwidth selector** that estimates the curvature of the underlying function.

The degree of the polynomial also matters. Local linear regression (degree 1) is the workhorse in econometrics, particularly in RD designs, because it has better boundary behavior than local constant regression: it does not suffer from the same upward bias at the edges of the support. Local quadratic adds another layer of flexibility but at the cost of variance. In RD applications, the key quantity is the difference between the fitted values from the left-side and right-side local polynomial regressions evaluated at the cutoff — this gives the causal effect estimate. The choice of bandwidth and polynomial degree are both robustness checks that credible RD papers report across multiple specifications.
