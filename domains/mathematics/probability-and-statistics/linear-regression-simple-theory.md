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
- id: linear-regression-probability-and-statistics
  type: soft
builds-toward:
- inference-in-linear-regression
- regression-diagnostics
tags:
- linear-regression
stage: formal-systems
status: validated
---
# Simple Linear Regression: Theory and Estimation

## Core Idea
Fit Y=β₀+β₁X+ε by minimizing Σε². Least squares: β₁=Cov(X,Y)/Var(X)=r(s_Y/s_X), β₀=Ȳ−β₁X̄. Under normality, LS is MLE. R²=correlation² is proportion of Y variance explained. Residuals ê_i=y_i−ŷ_i should be random.

## Questions

```yaml
- question: "After fitting a linear regression, you find R² = 0.94. When you plot the residuals against X, they form a clear U-shape — positive at low X, negative in the middle, positive again at high X. What does this indicate?"
  type: multiple-choice
  options:
    - "The model is excellent — R² near 1 confirms the fit is appropriate"
    - "The residuals are supposed to be U-shaped; this is expected behavior"
    - "The relationship between X and Y is likely nonlinear; the linear model is misspecified"
    - "The residuals indicate outliers that should be removed before re-fitting"
  answer: 2
  explanation: "Patterned residuals are a diagnostic signal that the model is misspecified, regardless of how high R² is. A U-shape means the linear model systematically over-predicts in one range and under-predicts in another — a telltale sign that the true relationship is curved, not linear. R² only measures how much variance is explained by the current model; a high R² with patterned residuals means the model captures a strong relationship, but not the right shape. Option A represents the most common mistake: trusting R² without inspecting residuals."

- question: "Two datasets both have correlation r = 0.7 between X and Y. Dataset A has sX = 2 and sY = 6. Dataset B has sX = 4 and sY = 3. Which correctly describes their OLS regression slopes?"
  type: multiple-choice
  options:
    - "Both slopes equal 0.7, because the slope equals the correlation for OLS"
    - "Both slopes are equal, because equal correlations always imply equal slopes"
    - "Dataset A has slope 2.1 and Dataset B has slope 0.525"
    - "The slopes cannot be determined from correlation and standard deviations alone"
  answer: 2
  explanation: "The slope formula is β₁ = r(sY/sX). For Dataset A: 0.7 × (6/2) = 2.1. For Dataset B: 0.7 × (3/4) = 0.525. Two datasets can have identical correlations but very different slopes because the slope rescales correlation into actual measurement units — it tells you how many units Y changes per unit of X, while r is dimensionless. Options A and B reflect the misconception that correlation and slope are the same thing."

- question: "In simple linear regression, R² equals the square of the Pearson correlation coefficient r between X and Y."
  type: true-false
  answer: true
  explanation: "This is a key algebraic identity in simple (one predictor) linear regression: R² = r². It means all the intuition built around correlation transfers directly to R². A correlation of r = 0.8 means R² = 0.64 — the model explains 64% of Y's variance. This equivalence holds for simple regression but does NOT extend to multiple regression, where R² no longer equals any single correlation."

- question: "A regression model with high R² and patterned residuals is well-specified — the patterned residuals are an artifact of the estimation procedure and should not affect interpretation."
  type: true-false
  answer: false
  explanation: "Patterned residuals are one of the clearest diagnostic signals that a model is wrong, regardless of R². If residuals show a systematic curve, fan shape, or clustering, the model is not capturing the true relationship. This means predictions will be biased in predictable ranges, confidence intervals will be invalid, and conclusions about the slope will be unreliable. R² measures variance explained, not model correctness — a model can explain a lot of variance while being fundamentally misspecified."

- question: "Why should you always inspect residual plots after fitting a regression, even when R² is very high?"
  type: short-answer
  answer: "R² only measures the proportion of variance in Y explained by the model — it does not tell you whether the model's functional form is correct. Patterned residuals reveal violations of the model's assumptions: a curved pattern suggests the true relationship is nonlinear; a fan shape (increasing spread) indicates heteroscedasticity; clustered residuals may suggest omitted variables. A high R² confirms that X and Y are strongly related, but patterned residuals show that the linear model is not capturing that relationship correctly. The regression line may still be useful for interpolation near the mean of X, but predictions will be biased elsewhere."
  explanation: "Inspecting residuals is part of model validation, not optional post-hoc analysis. The OLS estimator always finds the best-fitting line — but 'best-fitting line' is not the same as 'correct model.' Only residual diagnostics can reveal whether the line is the right shape for the data."
```

## Explainer

You already know that covariance and correlation measure how two variables move together. Simple linear regression takes that relationship and converts it into a predictive machine: given X, what is our best guess for Y? The model posits a straight line Y = β₀ + β₁X + ε, where ε represents random noise. The question becomes: which line fits best?

**Ordinary least squares (OLS)** answers that by minimizing the sum of squared residuals — the vertical distances between each observed point and the proposed line. Squaring the errors penalizes large misses more than small ones, making the solution unique and analytically tractable. Taking derivatives and setting them to zero yields the formulas: β₁ = Cov(X,Y)/Var(X) and β₀ = Ȳ − β₁X̄. Notice the slope formula: it is covariance (how much X and Y move together) scaled by variance (how spread-out X is). If X and Y are unrelated, Cov = 0, so β₁ = 0 — a flat line that ignores X entirely.

The equivalent form β₁ = r(sY/sX) gives a second interpretation. The correlation r captures the direction and strength of the relationship; the ratio sY/sX rescales it from correlation units into the actual units of Y per unit of X. This is why two datasets can have the same correlation but very different slopes — the slopes also depend on the relative spread of the variables.

**R²** — the coefficient of determination — measures how much of Y's total variation the model explains. It equals r² = 1 − SSRes/SSTotal, ranging from 0 (the line explains nothing beyond the mean) to 1 (perfect fit). Since R² is the square of the correlation, all the intuition you built about correlation directly transfers. After fitting, always inspect the **residuals** ê_i = y_i − ŷ_i. If the model is correctly specified, residuals should look like random noise: no pattern, no fan shape, no curve. Any structure in the residuals signals a problem — the relationship may be nonlinear, or the variance may change with X — and points toward the regression diagnostics you will study next.
