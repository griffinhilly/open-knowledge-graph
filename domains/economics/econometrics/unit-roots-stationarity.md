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
