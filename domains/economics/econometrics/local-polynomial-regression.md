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
status: validated
---

# Local Polynomial Regression and Bandwidth Selection

## Core Idea
Local polynomial regression fits a polynomial within a neighborhood around each point, producing a nonparametric estimate of conditional expectations. Bandwidth (window size) controls smoothness; larger bandwidth reduces variance but increases bias.

## Questions

```yaml
- question: "A researcher doubles the bandwidth in a local linear regression. What is the most likely effect on the resulting estimates?"
  type: multiple-choice
  options:
    - "Variance increases and bias decreases, because more data points are used for each estimate"
    - "Variance decreases and bias increases, because the local polynomial must approximate the true function over a wider range"
    - "Both variance and bias decrease, because more data always improves estimation"
    - "The estimates are unaffected, because local polynomial regression automatically adjusts for bandwidth changes"
  answer: 1
  explanation: "This is the fundamental bias-variance tradeoff in local polynomial regression. A larger bandwidth borrows more observations, reducing variance (the estimate is less noisy). But it also forces the local polynomial to approximate the true function over a wider range — if the true function curves, the locally linear fit will be systematically off, introducing bias. Doubling bandwidth doesn't uniformly improve estimates; it trades one error source for another. Optimal bandwidth minimizes total mean squared error, balancing these forces."

- question: "In a regression discontinuity design, why is local linear regression (degree 1) preferred over local constant regression (degree 0) near the cutoff?"
  type: multiple-choice
  options:
    - "Local linear uses more observations, reducing variance at the boundary"
    - "Local constant has worse boundary behavior because it cannot capture the slope of the true function, introducing upward bias at the edges of the support"
    - "Local linear automatically selects the optimal bandwidth, while local constant requires manual tuning"
    - "Local constant regression is biased everywhere, not just at boundaries"
  answer: 1
  explanation: "Local constant regression (fitting a local mean) suffers from boundary bias: at the edge of the data support, observations exist only on one side, so the local mean is pulled toward the interior. Local linear regression fits a slope as well as an intercept, which allows the fit to extrapolate more accurately to the boundary by accounting for the function's direction of travel. In RD designs, the key quantity is the fitted value at the cutoff (a boundary point), making this distinction critical."

- question: "A wider bandwidth in local polynomial regression usually produces a better estimate because it uses more data."
  type: true-false
  answer: false
  explanation: "Using more data is not inherently better when the data farther away contains misleading information for the target estimate. A wider bandwidth forces the local polynomial to approximate the true function over a larger range. If the true conditional expectation function is nonlinear, a wide-bandwidth local linear fit will be systematically biased toward a straight-line approximation. The optimal bandwidth explicitly trades variance reduction against bias increase — there is a bandwidth that minimizes MSE, and going beyond it increases total error even as variance keeps falling."

- question: "Local polynomial regression fits a separate polynomial in a neighborhood around each evaluation point, rather than fitting a single polynomial to the entire dataset."
  type: true-false
  answer: true
  explanation: "This is the defining feature of local polynomial regression and what makes it nonparametric. For each evaluation point x₀, the method collects nearby observations (within bandwidth h), weights them by a kernel function, and fits a polynomial to that local subset. A different polynomial is fit at each x₀, so the resulting curve can flex to match the local shape of the data everywhere. This contrasts with global polynomial regression, which fits a single function to all observations and imposes a rigid global shape."

- question: "Explain the bias-variance tradeoff in bandwidth selection for local polynomial regression. What happens as bandwidth shrinks toward zero, and what happens as it grows very large?"
  type: short-answer
  answer: "As bandwidth shrinks toward zero, each local fit uses only observations very close to the evaluation point — variance explodes (tiny sample, noisy estimate) but bias approaches zero (no need to extrapolate across a wide range). As bandwidth grows very large, the local fit incorporates most of the data — variance falls but bias grows, because the local polynomial must approximate the true function over a wide range where it may curve significantly. Optimal bandwidth sits between these extremes, minimizing mean squared error = bias² + variance."
  explanation: "This tradeoff appears throughout nonparametric statistics and machine learning (e.g., the choice of k in k-nearest neighbors, or the kernel bandwidth in kernel density estimation). The insight is that adding observations near the target reduces noise but adding distant observations introduces approximation error. Cross-validation and plug-in methods find bandwidth by estimating where the bias² + variance curve reaches its minimum."
```

## Explainer

From regression discontinuity design, you already know the motivation: near a threshold, you need to estimate what the outcome would have been on each side had no discontinuity existed. You do this by fitting a regression line or curve to the data on each side and extrapolating to the cutoff. But what function should you fit? Ordinary least squares assumes a global linear or polynomial relationship — a strong assumption. Local polynomial regression relaxes this entirely: instead of fitting one function to all the data, it fits a separate polynomial in a **bandwidth** window around each evaluation point, using only observations nearby.

The mechanics work like this. Pick a point x₀ where you want to estimate the conditional expectation E[Y|X = x₀]. Collect all observations within a bandwidth h of x₀. Fit a polynomial (degree 0 = local mean, degree 1 = local linear, degree 2 = local quadratic) to those observations, weighting nearby points more heavily than distant ones using a **kernel function** — typically a triangular or Epanechnikov kernel that assigns zero weight to observations outside the bandwidth. The fitted value at x₀ is your estimate. Slide x₀ across the full range of X and the resulting curve is the local polynomial estimate.

**Bandwidth selection** is the central tuning decision and involves a fundamental **bias-variance tradeoff** you first encountered in statistical modeling. A narrow bandwidth uses only observations very close to x₀, giving a highly local fit with low bias (no need to extrapolate across a wide range) but high variance (few observations, noisy estimate). A wide bandwidth borrows strength from more observations, reducing variance, but forces the local polynomial to approximate the true function over a larger range, introducing bias if the true function curves. Optimal bandwidth minimizes mean squared error, which balances these forces — the standard approach is **cross-validation** or the **plug-in bandwidth selector** that estimates the curvature of the underlying function.

The degree of the polynomial also matters. Local linear regression (degree 1) is the workhorse in econometrics, particularly in RD designs, because it has better boundary behavior than local constant regression: it does not suffer from the same upward bias at the edges of the support. Local quadratic adds another layer of flexibility but at the cost of variance. In RD applications, the key quantity is the difference between the fitted values from the left-side and right-side local polynomial regressions evaluated at the cutoff — this gives the causal effect estimate. The choice of bandwidth and polynomial degree are both robustness checks that credible RD papers report across multiple specifications.
