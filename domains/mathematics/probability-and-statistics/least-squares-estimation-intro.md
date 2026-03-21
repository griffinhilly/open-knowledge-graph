---
id: least-squares-estimation-intro
title: Least Squares Estimation
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: linear-regression
  type: soft
builds-toward:
- regression-diagnostics
tags:
- estimation
- regression
- least-squares
stage: formal-systems
status: draft
---

# Least Squares Estimation

## Core Idea
Least squares estimation minimizes the sum of squared residuals: Σ(yᵢ - ŷᵢ)². For simple linear regression, this yields slope = r(s_y/s_x) and intercept = ȳ - b·x̄. Least squares is intuitive and optimal under normality.

## How It's Best Learned
Fit linear regression by hand for a small dataset. Visualize residuals and understand what minimizing their squared sum means geometrically. Compare least squares to other fitting methods.

## Common Misconceptions
Thinking least squares requires normal errors (it gives optimal linear fit regardless). Assuming high R² means good predictions. Not recognizing that outliers can heavily influence least squares estimates.

## Questions

```yaml
- question: "A data scientist says: 'We can't use least squares regression here — our residuals clearly aren't normally distributed.' Is this objection valid?"
  type: multiple-choice
  options:
    - "Yes — least squares is only mathematically valid when errors follow a normal distribution"
    - "Yes — without normality, the slope and intercept formulas give different results"
    - "No — least squares gives the minimum sum of squared residuals regardless of the error distribution; normality is only needed for certain inferential guarantees like confidence intervals"
    - "No — least squares is always optimal regardless of the error distribution, so normality never matters"
  answer: 2
  explanation: "This is the central misconception about least squares: many students believe normality is a prerequisite for using it at all. In fact, the least squares criterion (minimize Σ(yᵢ − ŷᵢ)²) is a purely geometric/algebraic optimization that holds for any distribution of errors. Normality is only required for stronger statistical guarantees: specifically, that the estimates are BLUE (Best Linear Unbiased Estimator) in the Gauss-Markov sense, and for constructing exact t-tests and F-tests. The fit itself is valid without normality."

- question: "Why does least squares minimize the sum of *squared* residuals rather than, say, the sum of absolute residuals?"
  type: multiple-choice
  options:
    - "Squaring residuals is required by the central limit theorem"
    - "Squaring ensures all residuals are positive so they don't cancel out"
    - "Squaring yields a smooth, differentiable objective function with a unique closed-form solution, and it penalizes large deviations more heavily than small ones"
    - "Squared residuals correspond exactly to the variance of the errors, which makes the estimator unbiased"
  answer: 2
  explanation: "Squaring residuals does make them positive, but that's not the main reason — absolute values also achieve this. The key advantages of squaring are: (1) the squared-loss function is differentiable everywhere, allowing calculus to yield closed-form solutions for slope and intercept; (2) it penalizes large deviations much more heavily than small ones (the penalty grows quadratically), making it sensitive to outliers. This is both an advantage (it 'notices' big errors) and a drawback (a single outlier can pull the line dramatically). Absolute-value loss (leading to least absolute deviations regression) gives a more robust fit but lacks a closed-form solution."

- question: "A regression model with R² = 0.95 is guaranteed to make accurate predictions for new observations drawn from the same population."
  type: true-false
  answer: false
  explanation: "High R² means the model explains a large proportion of the variance in the *training data*, but this does not guarantee accurate predictions on new data. The model could be overfitting (capturing noise specific to the sample), the new observations might fall outside the range of training data (extrapolation failure), or the relationship might not hold in new contexts. R² is a measure of in-sample fit, not predictive accuracy. Cross-validation or out-of-sample testing is the correct way to assess predictive performance."

- question: "Least squares estimates are particularly sensitive to outliers because the squaring of residuals causes large deviations to contribute disproportionately to the objective function."
  type: true-false
  answer: true
  explanation: "Squaring amplifies large residuals: a residual of 10 contributes 100 to the objective; a residual of 2 contributes only 4. This means the optimizer is driven heavily by a few extreme observations. A single outlier with a large residual can pull the estimated regression line substantially toward it, distorting both slope and intercept. This is a direct consequence of the squared-loss criterion — it is not a bug in the implementation but a mathematical property of the objective being minimized."

- question: "Explain why minimizing squared residuals rather than absolute residuals is a deliberate design choice with real consequences, not just an arbitrary convention."
  type: short-answer
  answer: "Squaring makes the objective differentiable everywhere, enabling closed-form analytical solutions for slope and intercept via calculus (setting derivatives to zero). Absolute value is not differentiable at zero, requiring iterative numerical methods. Squaring also weights large errors more heavily, which is desirable when you want the line to be pulled toward points that would otherwise be badly fit — but also means outliers have outsized influence. The choice between squared and absolute loss is a tradeoff: squared loss is computationally tractable and sensitive to large errors; absolute loss is more robust to outliers but harder to minimize analytically."
  explanation: "Understanding this tradeoff is essential for applied statistics. When data have occasional extreme values (e.g., income data, sensor errors), least absolute deviations (LAD) regression may be preferable. When errors are well-behaved and computational efficiency matters, ordinary least squares is the standard choice. The squared-loss convention is not incidental — it shapes which observations dominate the fit and which properties the estimator has."
```
