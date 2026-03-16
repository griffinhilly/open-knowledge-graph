---
id: unit-roots-stationarity
title: Unit Roots and Testing for Stationarity
domain: economics
course: econometrics
prerequisites:
- id: time-series-basics-econometrics
  type: hard
- id: chow-test-structural-breaks
  type: soft
- id: characteristic-equation-method
  type: hard
- id: complex-numbers-intro
  type: soft
builds-toward:
- autoregressive-ar-models
tags:
- time-series
- unit-roots
- stationarity
stage: formal-systems
status: draft
---

# Unit Roots and Testing for Stationarity

## Core Idea
A time series is stationary if its mean, variance, and autocovariances are time-invariant. A unit root (coefficient on lagged dependent variable equal to 1) induces nonstationarity and persistence. Tests like the Augmented Dickey-Fuller (ADF) and KPSS test detect unit roots; differencing restores stationarity for I(1) series.

## How It's Best Learned
Simulate AR(1) processes with different coefficients (e.g., 0.9 vs 1.0) and observe how unit roots produce very different time path behavior.

## Common Misconceptions
A nearly unit root process (e.g., φ = 0.99) is not the same as a unit root process; small differences have large implications for statistical properties.

## Explainer

Think back to what makes a time series useful for standard inference: you need the statistical properties of the series to be stable over time. If the mean, variance, and autocorrelations all stay the same regardless of when you sample, the series is **stationary**, and the familiar tools of regression and hypothesis testing apply. If those properties drift — the mean trends upward, the variance grows, or the autocovariances depend on where you are in time — the series is **nonstationary**, and standard inference breaks down in subtle and serious ways.

The most important source of nonstationarity in economic data is the **unit root**. Consider the simplest case: an AR(1) process yₜ = φyₜ₋₁ + εₜ. If |φ| < 1, the effect of a shock to y dies away over time — the series reverts toward its mean and is stationary. If φ = 1 exactly, shocks never die away; every εₜ is permanently incorporated into the level of the series. This is a **random walk**: yₜ = yₜ₋₁ + εₜ, the most common unit root process. GDP, stock prices, and interest rates often behave this way — a shock today shifts the entire future path of the series, not just the next few periods. The crucial distinction between φ = 0.99 and φ = 1.0 seems numerically small but is statistically enormous: the first eventually reverts, the second never does.

Running a regression between two unrelated random walk series produces the **spurious regression** problem: you'll find high R² and significant t-statistics even though there is no true relationship. This is why testing for unit roots before modeling is essential. The **Augmented Dickey-Fuller (ADF) test** is the standard tool. It tests the null hypothesis that a unit root is present (φ = 1) against the alternative of stationarity (|φ| < 1). A key quirk: the test statistic does not follow a standard t-distribution under the null, so you must use Dickey-Fuller critical values, which are more negative than standard thresholds. Failing to reject the null means the series likely has a unit root.

The **KPSS test** takes the opposite approach: it tests the null of stationarity against the alternative of a unit root. Using ADF and KPSS together is good practice — if ADF fails to reject and KPSS rejects, both tests point to a unit root. When a series has a unit root, the standard remedy is **differencing**: taking first differences Δyₜ = yₜ - yₜ₋₁ removes one unit root. If a series requires one difference to become stationary, it is called **integrated of order 1**, or I(1); requiring two differences gives I(2), and so on. Once differenced to stationarity, you can apply AR models and standard regression — which is exactly where the next topic, AR models, begins.
