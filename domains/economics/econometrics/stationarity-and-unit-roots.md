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
builds-toward:
- serial-correlation
tags:
- stationarity
- unit-root
- ADF-test
- I(1)
- random-walk
stage: formal-systems
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
