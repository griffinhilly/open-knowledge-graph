---
id: serial-correlation
title: Serial Correlation (Autocorrelation) in Regression
domain: economics
course: econometrics
prerequisites:
- id: time-series-basics-econometrics
  type: hard
- id: ols-assumptions
  type: hard
- id: heteroskedasticity
  type: soft
- id: stationarity-and-unit-roots
  type: soft
tags:
- serial-correlation
- autocorrelation
- Durbin-Watson
- HAC
- AR-errors
stage: formal-systems
status: validated
---
# Serial Correlation (Autocorrelation) in Regression

## Core Idea
Serial correlation (autocorrelation) in regression errors means Cov(u_t, u_s) ≠ 0 for t ≠ s, violating the Gauss-Markov assumption. Like heteroskedasticity, it does not bias coefficient estimates but makes standard OLS standard errors invalid — typically understating them, leading to overconfidence in results. The Durbin-Watson statistic tests for first-order autocorrelation (AR(1) errors). The standard remedy is heteroskedasticity-and-autocorrelation consistent (HAC) standard errors (Newey-West), which are valid for both heteroskedasticity and serial correlation of unknown form. Alternatively, explicitly modeling the error structure with GLS or FGLS corrects both efficiency and inference.

## Common Misconceptions
- Serial correlation in errors is distinct from including lagged y as a regressor — the latter can create different (but related) biases.
- Newey-West standard errors require choosing a bandwidth (number of lags); the choice matters and should be reported.
