---
id: polynomial-regression-econometrics
title: Polynomial Regression and Nonlinear Functional Forms
domain: economics
course: econometrics
prerequisites:
- id: multiple-regression-model
  type: hard
- id: coefficient-interpretation-regression
  type: hard
builds-toward:
- nonlinear-models-interpretation
- specification-tests-econometrics
tags:
- regression
- nonlinear
- functional-forms
stage: formal-systems
status: draft
---

# Polynomial Regression and Nonlinear Functional Forms

## Core Idea
Polynomial terms (x², x³) extend linear regression to capture nonlinear relationships where the slope changes across values of the regressor. This allows U-shaped, inverted-U, or more complex patterns without requiring a fully nonlinear model.

## How It's Best Learned
Fit polynomials of increasing degree and compare using scatter plots and statistical tests. Use domain knowledge and data visualization to choose the degree rather than maximizing R².

## Common Misconceptions
Higher-degree polynomials always fit the data better in-sample but often overfit and perform poorly out-of-sample. Interpretation of raw coefficients becomes difficult; focus on marginal effects or predicted values instead.

## Explainer

You know from multiple regression that OLS fits the best linear approximation to a relationship between variables. But "linear" in OLS means linear in the parameters — not necessarily linear in the variables themselves. When you add x², x³, or other transformations of x as new regressors, the model remains linear in the coefficients and OLS estimation proceeds exactly as before. What changes is the shape of the fitted relationship in the original (x, y) space. This is the key insight behind **polynomial regression**: you extend the reach of OLS to capture curves, humps, and U-shapes without abandoning the linear regression toolkit.

The simplest case is a quadratic model: y = β₀ + β₁x + β₂x² + ε. If β₂ > 0, the fitted curve is U-shaped; if β₂ < 0, it's an inverted U. A classic example is the relationship between age and earnings — earnings rise with experience but eventually plateau or decline. A linear regression would miss this inverted-U pattern entirely, while a quadratic captures it well. The coefficients β₁ and β₂ cannot be interpreted in isolation; what matters is the **marginal effect**, ∂y/∂x = β₁ + 2β₂x, which varies with x. To report the effect of a one-unit change in x, you must evaluate this derivative at a specific value — typically the mean of x.

Choosing the degree of the polynomial requires balancing fit against **overfitting**. Every additional power of x you add will reduce in-sample residuals and increase R². This is mechanical — a polynomial of degree n-1 can perfectly fit n data points. But a high-degree polynomial will chase noise, fitting wiggles in the data that are not genuine features of the underlying relationship. The curve will look unreasonable and predict poorly out of sample. Useful approaches: use scatter plots and domain knowledge to motivate the degree first; test whether additional terms are statistically significant; evaluate out-of-sample prediction via cross-validation or a held-out test set.

A practical caution concerns **extrapolation**. Polynomial curves can behave wildly outside the range of the data — a cubic that fits well between x = 1 and x = 10 may produce bizarre predictions at x = 20. This makes polynomial regression particularly unreliable for forecasting beyond the observed range, in contrast to theory-based nonlinear models. Within their range and at an appropriate degree, however, polynomials are a flexible and practical tool for capturing nonlinearity while retaining the interpretability and estimation simplicity of OLS. The next steps — nonlinear models and specification tests — will give you more formal frameworks for diagnosing whether a polynomial approximation is adequate.
