---
id: stationarity-and-unit-roots
title: Stationarity and Unit Roots
domain: economics
course: econometrics
prerequisites:
- id: time-series-basics-econometrics
  type: hard
- id: random-variables-intro
  type: hard
- id: sequences-convergence
  type: soft
- id: differential-equations-intro-separable
  type: soft
- id: probability-theory
  type: hard
- id: limit-superior-and-inferior
  type: soft
builds-toward:
- serial-correlation
tags:
- stationarity
- unit-root
- ADF-test
- I(1)
- random-walk
stage: advanced
status: validated
---

# Stationarity and Unit Roots

## Core Idea
A time series is (weakly) stationary if its mean, variance, and autocovariances do not depend on time. Many economic series — GDP levels, price indices, exchange rates — are non-stationary: they have stochastic trends, drifting means, and growing variance. A random walk y_t = y_{t−1} + ε_t has a 'unit root' and is integrated of order 1 (I(1)); its first difference Δy_t = ε_t is stationary. The Augmented Dickey-Fuller (ADF) test formally tests for unit roots. Regressing one I(1) series on another without cointegration produces spurious results; the standard remedy is to work in differences.

## How It's Best Learned
Apply the ADF test to GDP levels and then to GDP growth rates — levels typically fail the test (unit root not rejected) while growth rates pass. Simulate a random walk and AR(1) with ρ<1 to see the difference visually.

## Common Misconceptions
- Differencing eliminates stochastic trends but also removes all long-run information — cointegration analysis recovers long-run relationships without losing this information.
- A trending series is not necessarily non-stationary; a linear deterministic trend can be removed by detrending, not differencing.

## Questions

```yaml
- question: "A researcher regresses U.S. GDP levels on Danish butter production over 1950–2010, finding R² = 0.94 and a t-statistic of 18 on the slope. What is the most likely explanation?"
  type: multiple-choice
  options:
    - "Butter production genuinely drives U.S. GDP through a food-economy linkage"
    - "The regression is spurious — both series are I(1) and trend upward, and OLS mistakes their shared stochastic trend for a causal relationship"
    - "The result is valid because R² = 0.94 always indicates a meaningful statistical relationship"
    - "The t-statistic of 18 is so extreme that spurious regression can be ruled out by any significance threshold"
  answer: 1
  explanation: "This is the classic spurious regression problem. Both GDP and butter production are I(1) — their levels wander upward due to stochastic trends. OLS interprets their shared upward drift as a relationship, producing high R² and inflated t-statistics. Crucially, standard t-test critical values are invalid for I(1) variables — even a t-statistic of 18 provides no evidence of a true relationship. Testing for stationarity before running regressions is not optional."

- question: "You apply the ADF test to monthly CPI levels and fail to reject the null hypothesis at the 5% level. What is the most accurate conclusion?"
  type: multiple-choice
  options:
    - "The series definitely has a unit root and is non-stationary"
    - "The series is probably stationary, since failing to reject usually means the null is true"
    - "You cannot reject the presence of a unit root, but this does not prove non-stationarity — the test may have insufficient power"
    - "The series should be differenced twice, since failing the ADF test implies it is I(2)"
  answer: 2
  explanation: "The ADF test has a specific directionality: the null hypothesis IS unit root (non-stationarity). Failing to reject means you lack sufficient evidence to conclude stationarity — not that you've proven non-stationarity. ADF tests are known to have low power, especially with short samples or near-unit-root processes (ρ close to but less than 1). The correct conclusion is 'we cannot reject a unit root,' not 'this series has a unit root.' Combine ADF results with economic reasoning and visual inspection."

- question: "A time series following a linear deterministic trend y_t = a + bt + ε_t is non-stationary and is expected to be first-differenced to achieve stationarity."
  type: true-false
  answer: false
  explanation: "A deterministic trend can be removed by detrending — regressing y_t on time t and keeping the residuals — which yields a stationary series. First-differencing also removes the trend, but over-differences a trend-stationary series, introducing a unit root in the MA component and distorting the model. The key distinction: a stochastic trend (unit root) requires differencing; a deterministic trend requires detrending. Treating a deterministic trend as a unit root is a specification error."

- question: "In a random walk y_t = y_{t-1} + ε_t, a positive shock to ε_t permanently raises the level of the series, with no tendency to revert toward a long-run mean."
  type: true-false
  answer: true
  explanation: "This is the defining feature distinguishing I(1) series from stationary ones. In a stationary AR(1) with |ρ| < 1, shocks decay geometrically and the series returns to its mean. In a random walk (ρ = 1), the series simply starts from a new, permanently higher level after a positive shock and wanders from there — there is no mean to return to. Variance grows without bound (Var(y_t) = σ²t), directly violating constant-variance stationarity."

- question: "Explain why regressing two unrelated I(1) series on each other typically produces a high R² and significant t-statistics, even though no true relationship exists."
  type: short-answer
  answer: "Both I(1) series have stochastic trends causing their levels to drift over the sample period. OLS minimizes squared residuals, and the best way to fit one drifting series with another is to find a slope that makes them track each other's long-run drift. The resulting fit appears strong (high R²) not because of causation, but because both series move in similar directions over time. Additionally, standard OLS critical values assume well-behaved (stationary) residuals; residuals from regressing two unrelated I(1) series are themselves non-stationary, so conventional t-test distributions don't apply and t-statistics can be extreme under the null of no relationship."
  explanation: "The diagnostic is to test whether regression residuals are stationary (cointegration, which would indicate a genuine long-run relationship) or non-stationary (spurious). High R² and significant coefficients alone cannot distinguish the two cases — only residual stationarity tests can."
```

## Explainer

Your time series background gives you the tools to model how economic variables evolve over time. The next essential question is whether a series behaves consistently over time — whether its statistical properties are stable or drifting. A series is **weakly stationary** if its mean, variance, and autocovariances are all constant over time. Think of coin flip outcomes: no matter when you start recording, the mean hovers at 0.5 and the variance stays fixed. A stationary series has a stable "center of gravity" it keeps returning to after shocks. Many standard results in time series econometrics — the law of large numbers, the central limit theorem — require stationarity to hold. When stationarity fails, those results break down, and so do many standard regression techniques.

The contrast is a **random walk**: y_t = y_{t−1} + ε_t, where ε_t is white noise. Each period, the series moves by a random shock — and here is the key: the shock is permanent. There is no mean to return to. After a positive shock today, the series simply starts from a higher level and wanders from there. The variance of a random walk grows without bound as time passes (it equals σ²t after t periods), which violates the stationarity requirement of constant variance. This is what it means to be **integrated of order 1**, or **I(1)**: one differencing operation is needed to produce a stationary series. The first difference Δy_t = y_t − y_{t−1} = ε_t is simply white noise — stationary. GDP levels, stock prices, exchange rates, and many price indices behave like random walks (or near-random walks). GDP growth rates, stock returns, and inflation rates tend to be stationary.

The practical danger of non-stationarity is **spurious regression**. If you regress one I(1) series on another unrelated I(1) series — say, U.S. GDP on the population of Iceland — you will typically find a high R² and a statistically significant slope coefficient, even though no true relationship exists. Both series are simply trending over time, and OLS interprets their shared trend as a relationship. Your probability theory and random variables background helps here: you know that the sampling distributions of OLS estimates change fundamentally when variables are I(1), invalidating the usual t- and F-test critical values. This is why checking for stationarity before running regressions is not optional.

The **Augmented Dickey-Fuller (ADF) test** formalizes this check. The null hypothesis is that the series has a unit root (is non-stationary); rejection of the null means stationarity. The ADF regression tests whether the autoregressive coefficient is equal to one by running the transformed regression Δy_t = α + ρ*y_{t−1} + lagged differences + ε_t and testing whether ρ = 0. Note the counterintuitive direction of the test: you need evidence *against* the null (unit root) to conclude stationarity, and failing to reject does not prove the series is non-stationary — it may just mean you have insufficient power. If a series is I(1), the standard remedy is to **work in differences**: first-differencing removes the stochastic trend, produces a stationary series, and restores the validity of standard inference. The tradeoff is that differencing also removes all long-run level information — the cointegration framework, covered next, recovers long-run relationships without discarding them.
