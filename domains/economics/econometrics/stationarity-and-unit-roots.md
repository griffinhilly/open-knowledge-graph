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

## Explainer

Your time series background gives you the tools to model how economic variables evolve over time. The next essential question is whether a series behaves consistently over time — whether its statistical properties are stable or drifting. A series is **weakly stationary** if its mean, variance, and autocovariances are all constant over time. Think of coin flip outcomes: no matter when you start recording, the mean hovers at 0.5 and the variance stays fixed. A stationary series has a stable "center of gravity" it keeps returning to after shocks. Many standard results in time series econometrics — the law of large numbers, the central limit theorem — require stationarity to hold. When stationarity fails, those results break down, and so do many standard regression techniques.

The contrast is a **random walk**: y_t = y_{t−1} + ε_t, where ε_t is white noise. Each period, the series moves by a random shock — and here is the key: the shock is permanent. There is no mean to return to. After a positive shock today, the series simply starts from a higher level and wanders from there. The variance of a random walk grows without bound as time passes (it equals σ²t after t periods), which violates the stationarity requirement of constant variance. This is what it means to be **integrated of order 1**, or **I(1)**: one differencing operation is needed to produce a stationary series. The first difference Δy_t = y_t − y_{t−1} = ε_t is simply white noise — stationary. GDP levels, stock prices, exchange rates, and many price indices behave like random walks (or near-random walks). GDP growth rates, stock returns, and inflation rates tend to be stationary.

The practical danger of non-stationarity is **spurious regression**. If you regress one I(1) series on another unrelated I(1) series — say, U.S. GDP on the population of Iceland — you will typically find a high R² and a statistically significant slope coefficient, even though no true relationship exists. Both series are simply trending over time, and OLS interprets their shared trend as a relationship. Your probability theory and random variables background helps here: you know that the sampling distributions of OLS estimates change fundamentally when variables are I(1), invalidating the usual t- and F-test critical values. This is why checking for stationarity before running regressions is not optional.

The **Augmented Dickey-Fuller (ADF) test** formalizes this check. The null hypothesis is that the series has a unit root (is non-stationary); rejection of the null means stationarity. The ADF regression tests whether the autoregressive coefficient is equal to one by running the transformed regression Δy_t = α + ρ*y_{t−1} + lagged differences + ε_t and testing whether ρ = 0. Note the counterintuitive direction of the test: you need evidence *against* the null (unit root) to conclude stationarity, and failing to reject does not prove the series is non-stationary — it may just mean you have insufficient power. If a series is I(1), the standard remedy is to **work in differences**: first-differencing removes the stochastic trend, produces a stationary series, and restores the validity of standard inference. The tradeoff is that differencing also removes all long-run level information — the cointegration framework, covered next, recovers long-run relationships without discarding them.
