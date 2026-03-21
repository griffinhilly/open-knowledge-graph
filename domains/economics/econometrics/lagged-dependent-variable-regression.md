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

## Questions

```yaml
- question: "In a lagged dependent variable model with β₁ = 0.7 and β₂ = 0.3, a permanent one-unit increase in X occurs at time t. What is the total long-run effect on Y?"
  type: multiple-choice
  options:
    - "0.3 — only the immediate impact coefficient matters"
    - "0.7 — the persistence coefficient captures all dynamic effects"
    - "1.0 — the long-run effect is β₂/(1 − β₁) = 0.3/0.3"
    - "∞ — the effects accumulate indefinitely and never stop growing"
  answer: 2
  explanation: "The long-run multiplier is β₂/(1 − β₁) = 0.3/(1 − 0.7) = 0.3/0.3 = 1.0. The mechanism: the immediate effect is β₂ = 0.3. Next period, Y is higher by 0.3, which feeds into Yₜ₋₁, adding β₁ × 0.3 = 0.21. The following period adds β₁² × 0.3 = 0.147, and so on. The sum of this geometric series is β₂/(1 − β₁). Option A misses all the dynamic propagation. Option D would require β₁ ≥ 1 (non-stationary process) — with β₁ = 0.7 < 1, the process is stationary and the series converges."

- question: "OLS estimates in a lagged dependent variable model are inconsistent when..."
  type: multiple-choice
  options:
    - "The sample size is small — OLS requires at least 100 observations with lagged variables"
    - "The errors uₜ are serially autocorrelated, because Yₜ₋₁ and uₜ are then correlated through past errors"
    - "The coefficient β₁ is close to 1, making the model nearly nonstationary"
    - "The model includes more than one lag of Y, requiring instrumental variables"
  answer: 1
  explanation: "The consistency of OLS in the lagged dependent variable model requires that Yₜ₋₁ be uncorrelated with the current error uₜ. If errors are serially autocorrelated (e.g., uₜ = ρuₜ₋₁ + εₜ), then uₜ₋₁ enters uₜ, but uₜ₋₁ also determined Yₜ₋₁ (since Yₜ₋₁ = ... + uₜ₋₁). This creates a correlation between the regressor Yₜ₋₁ and the error uₜ — a violation of the exogeneity condition — causing OLS to be biased and inconsistent. Sample size (Option A) affects precision, not consistency. β₁ near 1 (Option C) is a stationarity concern, not a bias concern per se."

- question: "In a lagged dependent variable model, a coefficient β₁ = 0.9 implies that shocks to Y dissipate quickly because 0.9 is less than 1."
  type: true-false
  answer: false
  explanation: "β₁ = 0.9 implies HIGH persistence, not quick dissipation. After a shock, the deviation in Y decays as 0.9^t: after 5 periods it is still 59% of the original size (0.9⁵ ≈ 0.59); after 20 periods it is still 12% (0.9²⁰ ≈ 0.12). The process is stationary only because 0.9 < 1 — it does eventually revert to the mean — but it does so slowly. Quick dissipation would require β₁ close to 0. A coefficient close to 1 is often described as 'near unit root' behavior, where shocks are extremely persistent."

- question: "When residuals from a lagged dependent variable regression show serial autocorrelation, this is a signal that the exogeneity assumption for Yₜ₋₁ may be violated, making OLS estimates biased."
  type: true-false
  answer: true
  explanation: "Serial autocorrelation in the residuals means uₜ is correlated with uₜ₋₁. But Yₜ₋₁ depends on uₜ₋₁ (since Yₜ₋₁ = β₀ + β₁Yₜ₋₂ + β₂Xₜ₋₁ + uₜ₋₁), so Yₜ₋₁ is correlated with uₜ. This violates the OLS exogeneity condition, causing bias. This is why testing for serial correlation (Durbin-Watson, Breusch-Godfrey) is essential in LDV models — it is not just a specification nicety but a direct check on whether OLS is consistent."

- question: "Explain the difference between the short-run and long-run effects of X on Y in a lagged dependent variable model, and derive why the long-run multiplier is β₂/(1 − β₁)."
  type: short-answer
  answer: "The short-run effect is β₂: a one-unit increase in X raises Y immediately by β₂. But Y also feeds back on itself through the lagged term. In the next period, Y is higher by β₂, which via Yₜ₋₁ raises Y again by β₁β₂. The period after that adds β₁²β₂, and so on. The total long-run effect is the sum of this geometric series: β₂(1 + β₁ + β₁² + ...) = β₂ × 1/(1 − β₁) = β₂/(1 − β₁), valid when |β₁| < 1. This multiplier is always larger than the short-run effect β₂ when β₁ > 0, and it can be substantially larger when β₁ is close to 1 — a permanent change in X has outsized cumulative consequences in highly persistent processes."
  explanation: "The long-run vs. short-run distinction is the core practical contribution of the LDV model. A policy that raises X by 1 unit produces an immediate effect of β₂, but the full reckoning takes many periods to play out. A researcher who only reports the contemporaneous coefficient β₂ is dramatically underestimating the impact of a permanent policy change when β₁ is substantial."
```

## Explainer

Your multiple regression model assumes that the regressors explain current outcomes, and that past values of the outcome have no independent explanatory power once those regressors are included. For a great many economic processes, this is unrealistic. GDP this quarter is partly predicted by GDP last quarter, independently of any other variable you might include. Inflation today partly reflects inflation yesterday. Unemployment persists. The **lagged dependent variable** model formalizes this insight: Yₜ₋₁ appears as an explicit regressor, so the model can distinguish how much of today's value reflects yesterday's value (inertia) versus the effect of current inputs.

The coefficient β₁ on the lagged dependent variable has a clean interpretation: it measures **persistence**, the fraction of a deviation from steady state that carries forward one period. If β₁ = 0.8, a one-unit shock to Y today fades to 0.8 units next period, 0.64 the period after, and so on — a geometric decay you may recognize from sequences. When 0 < β₁ < 1, the process is stationary and mean-reverting. The dynamic effect of X on Y also becomes richer: a one-unit increase in X today raises Y immediately by β₂, but also raises Yₜ₊₁ by β₁β₂ (via the lagged term), and Yₜ₊₂ by β₁²β₂, continuing indefinitely. The total **long-run effect** of X on Y is β₂ / (1 − β₁), substantially larger than the immediate impact when β₁ is close to 1.

From your time series basics you know that the relationship between Yₜ and Yₜ₋₁ creates a structural constraint on the error term. OLS on this model requires that uₜ be serially uncorrelated — if errors are themselves autocorrelated, then Yₜ₋₁ will be correlated with uₜ through the chain Yₜ₋₁ → uₜ₋₁ → uₜ, violating the exogeneity condition and biasing estimates. This is why you cannot simply import a cross-sectional regression mindset into dynamic time series. Testing residuals for serial correlation (Durbin-Watson or Breusch-Godfrey) is not optional — it is the diagnostic that validates your model. If autocorrelation is present, the solution is either to add more lags or to specify the error structure explicitly, not to ignore it.
