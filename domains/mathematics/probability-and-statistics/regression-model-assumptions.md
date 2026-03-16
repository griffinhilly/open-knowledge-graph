---
id: regression-model-assumptions
title: Assumptions in Linear Regression
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: linear-regression
  type: hard
builds-toward:
- regression-diagnostics
- inference-in-linear-regression
tags:
- regression
- assumptions
- diagnostics
stage: formal-systems
status: draft
---

# Assumptions in Linear Regression

## Core Idea
Standard linear regression assumes: linearity (relationship is linear), independence of observations, homoscedasticity (constant error variance), and normality of errors. Violations affect validity of inferential procedures. Residual plots help diagnose violations.

## How It's Best Learned
Create residual plots for various datasets and identify assumption violations. Compare behavior of regression under satisfied vs. violated assumptions. Use transformations to stabilize variance or linearize relationships.

## Common Misconceptions
Assuming regression works automatically without checking assumptions. Thinking normality is most important (independence violations are often more problematic). Fitting regression to inherently nonlinear relationships and ignoring residual patterns.

## Explainer

From your prerequisite on linear regression, you know how to fit a line by minimizing squared residuals and how to read off a coefficient like "for each additional year of education, income increases by $3,200." That fitting procedure always produces a line — it will always give you numbers. But the p-values, confidence intervals, and standard errors you compute alongside those coefficients rest on four assumptions that the data may or may not satisfy. Understanding assumptions is about knowing when those inferential statements are trustworthy, not about when regression "works" mechanically.

The four assumptions are often remembered by the acronym LINE. **Linearity** means the true relationship between the predictors and the outcome is additive and linear — if it curves, your coefficients are biased estimates of a nonlinear truth. **Independence** means each observation's error is unrelated to every other — this is violated in time-series data (where yesterday's error predicts today's), in clustered data (where students within the same school share unmeasured factors), and anywhere that repeated measurements come from the same unit. Independence violations are often the most damaging, yet they leave no trace in a standard residual plot. **Homoscedasticity** means error variance is constant across the range of fitted values — if higher predicted values also have larger residuals (a "fan" pattern), your standard errors are wrong in ways that can either inflate or deflate significance. **Normality of errors** is the mildest assumption: the Central Limit Theorem makes regression estimates approximately normal even when residuals are not, especially for large samples.

The primary diagnostic tool is the **residual plot** — a scatterplot of fitted values (x-axis) against residuals (y-axis). A well-satisfied model produces a cloud of points with no visible pattern: random scatter centered at zero, constant spread, no curves. Curved patterns indicate violated linearity; a fan or funnel shape indicates heteroscedasticity; systematic bands or waves often indicate autocorrelation. A QQ-plot of residuals against theoretical normal quantiles checks the normality assumption: points should fall on a straight diagonal line.

When you find violations, you have options rather than a dead end. A curved residual pattern often calls for a transformation of a predictor (log x, x²) or the outcome (log y for multiplicative relationships). Heteroscedasticity often responds to a log transformation of y, or to using robust standard errors that are valid without the constant-variance assumption. Autocorrelation requires modeling the error structure directly — Durbin-Watson tests detect it, and time-series methods correct for it. Independence violations from clustering are addressed by clustered standard errors or mixed models. The assumptions are not pass-or-fail gates; they are diagnostic signals that tell you what model refinements are needed.

A practical framing: think of the four assumptions as ordered by the severity of their violation. Nonlinearity produces biased coefficients — the fundamental estimates are wrong. Independence violations corrupt standard errors in hard-to-predict directions. Heteroscedasticity inflates or deflates standard errors but leaves coefficients unbiased. Normality violations matter primarily for small samples and are the first to forgive. Every regression analysis should at minimum produce a residual-vs-fitted plot and a QQ-plot before any inference is reported; skipping this step is not efficiency, it is silent model misspecification.
