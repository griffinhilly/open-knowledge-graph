---
id: prediction-intervals-regression
title: Prediction Intervals and Out-of-Sample Forecasting
domain: economics
course: econometrics
prerequisites:
- id: confidence-intervals-regression
  type: hard
- id: multiple-regression-model
  type: soft
builds-toward:
- arima-models-forecasting
tags:
- forecasting
- prediction
- uncertainty
stage: advanced
status: draft
---

# Prediction Intervals and Out-of-Sample Forecasting

## Core Idea
Prediction intervals account for both uncertainty in parameter estimates and irreducible error variance, making them wider than confidence intervals for mean predictions. Choosing between prediction and confidence intervals depends on the task: use confidence intervals to estimate mean effects, prediction intervals to forecast individual outcomes.

## Explainer

From your work on confidence intervals in regression, you know how to quantify uncertainty about estimated coefficients and about the expected value of Y at a given X. A confidence interval for the mean of Y at X = x* answers the question: "What is the average outcome for all units with this value of X?" But there is a different and often more practically relevant question: "What outcome should I expect for this specific new unit?" That is the question a prediction interval answers — and the distinction matters enormously for applied work.

Here is why a **prediction interval** must be wider than a confidence interval for the mean. When you ask about the mean of Y at a given X, uncertainty comes only from imprecision in your estimated regression line — you have estimated β with some error. As sample size grows, this uncertainty shrinks toward zero. But when you ask about a *specific new observation*, there is an additional, irreducible source of uncertainty: the error term ε for that new unit. That new unit will not fall exactly on the regression line even if you knew the line perfectly. The variance of a new prediction is therefore Var(ŷ_new) = σ²[1 + X_new′(X′X)⁻¹X_new], the "1" representing the irreducible error variance that never disappears no matter how large your sample. The confidence interval omits the "1" term. This structural difference means prediction intervals do not shrink to zero as n → ∞ — they converge to ±1.96σ around the true mean, where σ is the residual standard error.

A practical implication is that prediction intervals widen as X_new moves away from the center of your data. This follows from the (X_new′(X′X)⁻¹X_new) term, which is smallest near the mean of X and grows as you extrapolate. Predicting the salary of someone with 20 years of experience when most of your data covers 0–10 years yields an interval so wide it may be useless. This is the statistical signature of **extrapolation risk**: even if your model is correctly specified within the observed range, predictions far outside it carry large formal uncertainty — and unknown model misspecification risk on top of that.

**Out-of-sample forecasting** brings a further complication: model selection bias. When you fit a model on training data and evaluate its predictive accuracy on a held-out test set, the test error is an honest estimate of future prediction error; in-sample R² and residual variance estimates are not. Overfitted models look precise in-sample but produce wide prediction intervals out-of-sample — or, worse, generate point forecasts that perform poorly in ways the in-sample fit masked. The discipline of holding out a test set, or using cross-validation, forces you to confront prediction interval width honestly. A model that minimizes in-sample residual variance is not the same as a model that minimizes out-of-sample forecast error, and understanding this gap is the foundation of modern forecasting methodology.
