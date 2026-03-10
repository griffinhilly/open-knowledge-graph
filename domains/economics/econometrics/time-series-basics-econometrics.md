---
id: time-series-basics-econometrics
title: 'Time Series Data: Structure and Concepts'
domain: economics
course: econometrics
prerequisites:
- id: econometrics-intro
  type: hard
- id: gdp-and-national-income
  type: soft
- id: business-cycles
  type: soft
builds-toward:
- stationarity-and-unit-roots
- serial-correlation
tags:
- time-series
- autocorrelation
- trend
- seasonality
stage: formal-systems
status: draft
---

# Time Series Data: Structure and Concepts

## Core Idea
Time series data records observations on a single unit at sequential, equally spaced time points — GDP, unemployment, or stock prices over quarters or years. Unlike cross-sectional data, time series observations are ordered and typically autocorrelated: past values predict future values. Standard OLS assumptions break down because errors are serially correlated and many economic variables have stochastic trends. Time series analysis requires specialized tools to account for the time dependence structure, distinguish short-run dynamics from long-run relationships, and handle non-stationary processes.

## How It's Best Learned
Plot GDP and the federal funds rate over several decades, visually identifying trends, recessions (business cycles), and co-movement — this builds intuition before formalizing with AR models and cointegration.

## Common Misconceptions
- A 'spurious regression' can show high R² and significant t-statistics between two trending but unrelated series — non-stationarity inflates test statistics.
- 'Seasonal adjustment' is a data preprocessing step, not a modeling technique; always clarify whether a series is seasonally adjusted before modeling.
