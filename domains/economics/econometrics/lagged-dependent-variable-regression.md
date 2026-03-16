---
id: lagged-dependent-variable-regression
title: Lagged Dependent Variable Regression
domain: economics
course: econometrics
prerequisites:
- id: multiple-regression-model
  type: hard
- id: time-series-basics-econometrics
  type: hard
- id: sequences-and-series-review
  type: soft
builds-toward:
- dynamic-panel-arellano-bond-estimator
tags:
- dynamic-models
- time-series
- lagged-variables
stage: formal-systems
status: draft
---

# Lagged Dependent Variable Regression

## Core Idea
The model Yₜ = β₀ + β₁Yₜ₋₁ + β₂Xₜ + uₜ includes lagged Y; β₁ measures persistence and dynamic adjustment. OLS remains consistent if uₜ is serially uncorrelated and exogenous, but standard errors require adjustment for the correlation between Yₜ₋₁ and subsequent errors.

## Explainer

Your multiple regression model assumes that the regressors explain current outcomes, and that past values of the outcome have no independent explanatory power once those regressors are included. For a great many economic processes, this is unrealistic. GDP this quarter is partly predicted by GDP last quarter, independently of any other variable you might include. Inflation today partly reflects inflation yesterday. Unemployment persists. The **lagged dependent variable** model formalizes this insight: Yₜ₋₁ appears as an explicit regressor, so the model can distinguish how much of today's value reflects yesterday's value (inertia) versus the effect of current inputs.

The coefficient β₁ on the lagged dependent variable has a clean interpretation: it measures **persistence**, the fraction of a deviation from steady state that carries forward one period. If β₁ = 0.8, a one-unit shock to Y today fades to 0.8 units next period, 0.64 the period after, and so on — a geometric decay you may recognize from sequences. When 0 < β₁ < 1, the process is stationary and mean-reverting. The dynamic effect of X on Y also becomes richer: a one-unit increase in X today raises Y immediately by β₂, but also raises Yₜ₊₁ by β₁β₂ (via the lagged term), and Yₜ₊₂ by β₁²β₂, continuing indefinitely. The total **long-run effect** of X on Y is β₂ / (1 − β₁), substantially larger than the immediate impact when β₁ is close to 1.

From your time series basics you know that the relationship between Yₜ and Yₜ₋₁ creates a structural constraint on the error term. OLS on this model requires that uₜ be serially uncorrelated — if errors are themselves autocorrelated, then Yₜ₋₁ will be correlated with uₜ through the chain Yₜ₋₁ → uₜ₋₁ → uₜ, violating the exogeneity condition and biasing estimates. This is why you cannot simply import a cross-sectional regression mindset into dynamic time series. Testing residuals for serial correlation (Durbin-Watson or Breusch-Godfrey) is not optional — it is the diagnostic that validates your model. If autocorrelation is present, the solution is either to add more lags or to specify the error structure explicitly, not to ignore it.
