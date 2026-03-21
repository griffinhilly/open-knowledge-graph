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

## Questions

```yaml
- question: "A researcher estimates the model y = β₀ + β₁x + β₂x² + ε and obtains β₁ = 5 and β₂ = −0.3. What is the marginal effect of x on y when x = 10?"
  type: multiple-choice
  options:
    - "5, because β₁ is the coefficient on x"
    - "−0.3, because the quadratic term dominates at large values of x"
    - "5 + 2(−0.3)(10) = 5 − 6 = −1"
    - "5 − 0.3 = 4.7, by summing the two coefficients"
  answer: 2
  explanation: "The marginal effect in a quadratic model is ∂y/∂x = β₁ + 2β₂x, which varies with x. At x = 10: 5 + 2(−0.3)(10) = 5 − 6 = −1. You cannot simply read β₁ as 'the effect of x' — that is only valid in a purely linear model. The quadratic term means the slope changes continuously. Option A is the most common error: reporting β₁ alone as if the quadratic term doesn't exist, which would be correct only at x = 0."

- question: "A researcher adds x², x³, x⁴, and x⁵ to a model and observes that in-sample R² rises with each term. They keep all terms to maximize fit. What is the main problem with this approach?"
  type: multiple-choice
  options:
    - "OLS cannot be applied when more than one polynomial term is present"
    - "Higher-degree polynomials will overfit by chasing noise in the data, producing unreliable out-of-sample predictions and often implausible curve shapes"
    - "R² decreases when additional polynomial terms are added, so this approach is mathematically impossible"
    - "The model violates the linearity assumption of OLS because polynomial terms are nonlinear"
  answer: 1
  explanation: "R² mechanically increases with every term added — a polynomial of degree n−1 can perfectly fit any n data points. But perfect in-sample fit does not mean the model captures the true relationship; it means it has memorized the noise. A high-degree polynomial can produce wild swings between data points and collapse outside the observed range. Option D is the crucial misconception: 'linear' in OLS means linear in the parameters (β), not in x. Adding x² is fine — OLS estimates β₂ just like any other coefficient."

- question: "Polynomial regression is still estimated with OLS because the model remains linear in the parameters, even though it captures nonlinear relationships in x."
  type: true-false
  answer: true
  explanation: "OLS requires the model to be linear in the coefficients β — it places no restriction on the variables. Treating x², x³, etc. as new variables (call them z₁ = x², z₂ = x³) transforms the polynomial model into a standard multiple regression. OLS then estimates β₁, β₂, β₃ exactly as usual. The result is a curved fitted line in the (x, y) space, but the estimation procedure is unchanged."

- question: "A higher-degree polynomial always produces a better model because it increases R² and therefore captures more of the true relationship."
  type: true-false
  answer: false
  explanation: "R² always increases (or stays the same) when you add a predictor — this is a mechanical property of OLS, not evidence of a better model. A higher-degree polynomial may fit the sample very well while fitting poorly on new data. The test of a good model is out-of-sample predictive accuracy, not in-sample R². The appropriate degree should be motivated by theory, scatter-plot inspection, and significance tests — not by maximizing R²."

- question: "Why can't you interpret the coefficient β₁ in isolation in the model y = β₀ + β₁x + β₂x² + ε, and what should you report instead?"
  type: short-answer
  answer: "β₁ alone is not the effect of x on y because the quadratic term means the slope changes with x. The marginal effect is ∂y/∂x = β₁ + 2β₂x, which depends on the value of x. Report the marginal effect evaluated at a meaningful x value (e.g., the sample mean), along with how it varies across the range of x — often shown as a marginal effect plot."
  explanation: "Reporting β₁ as 'the effect of x' implicitly assumes the relationship is linear (β₂ = 0). When a quadratic is included, that is exactly what the model is testing against. The reason you added x² in the first place is to allow the slope to vary — so report that varying slope, not a single number that pretends otherwise. This connects directly to the broader principle that OLS coefficient interpretation depends on the model specification."
```

## Explainer

You know from multiple regression that OLS fits the best linear approximation to a relationship between variables. But "linear" in OLS means linear in the parameters — not necessarily linear in the variables themselves. When you add x², x³, or other transformations of x as new regressors, the model remains linear in the coefficients and OLS estimation proceeds exactly as before. What changes is the shape of the fitted relationship in the original (x, y) space. This is the key insight behind **polynomial regression**: you extend the reach of OLS to capture curves, humps, and U-shapes without abandoning the linear regression toolkit.

The simplest case is a quadratic model: y = β₀ + β₁x + β₂x² + ε. If β₂ > 0, the fitted curve is U-shaped; if β₂ < 0, it's an inverted U. A classic example is the relationship between age and earnings — earnings rise with experience but eventually plateau or decline. A linear regression would miss this inverted-U pattern entirely, while a quadratic captures it well. The coefficients β₁ and β₂ cannot be interpreted in isolation; what matters is the **marginal effect**, ∂y/∂x = β₁ + 2β₂x, which varies with x. To report the effect of a one-unit change in x, you must evaluate this derivative at a specific value — typically the mean of x.

Choosing the degree of the polynomial requires balancing fit against **overfitting**. Every additional power of x you add will reduce in-sample residuals and increase R². This is mechanical — a polynomial of degree n-1 can perfectly fit n data points. But a high-degree polynomial will chase noise, fitting wiggles in the data that are not genuine features of the underlying relationship. The curve will look unreasonable and predict poorly out of sample. Useful approaches: use scatter plots and domain knowledge to motivate the degree first; test whether additional terms are statistically significant; evaluate out-of-sample prediction via cross-validation or a held-out test set.

A practical caution concerns **extrapolation**. Polynomial curves can behave wildly outside the range of the data — a cubic that fits well between x = 1 and x = 10 may produce bizarre predictions at x = 20. This makes polynomial regression particularly unreliable for forecasting beyond the observed range, in contrast to theory-based nonlinear models. Within their range and at an appropriate degree, however, polynomials are a flexible and practical tool for capturing nonlinearity while retaining the interpretability and estimation simplicity of OLS. The next steps — nonlinear models and specification tests — will give you more formal frameworks for diagnosing whether a polynomial approximation is adequate.
