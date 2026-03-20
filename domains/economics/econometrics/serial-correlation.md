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
stage: advanced
status: validated
---
# Serial Correlation (Autocorrelation) in Regression

## Core Idea
Serial correlation (autocorrelation) in regression errors means Cov(u_t, u_s) ≠ 0 for t ≠ s, violating the Gauss-Markov assumption. Like heteroskedasticity, it does not bias coefficient estimates but makes standard OLS standard errors invalid — typically understating them, leading to overconfidence in results. The Durbin-Watson statistic tests for first-order autocorrelation (AR(1) errors). The standard remedy is heteroskedasticity-and-autocorrelation consistent (HAC) standard errors (Newey-West), which are valid for both heteroskedasticity and serial correlation of unknown form. Alternatively, explicitly modeling the error structure with GLS or FGLS corrects both efficiency and inference.

## Common Misconceptions
- Serial correlation in errors is distinct from including lagged y as a regressor — the latter can create different (but related) biases.
- Newey-West standard errors require choosing a bandwidth (number of lags); the choice matters and should be reported.

## Explainer

From your work on OLS assumptions, you know that the Gauss-Markov theorem requires errors to be uncorrelated across observations. For cross-sectional data — a sample of individuals or firms from a single point in time — this is often plausible. For time-series data, it is almost always violated. Economic variables evolve continuously; today's output depends on yesterday's output, today's inflation reflects last quarter's inflation expectations, and today's forecast error is related to yesterday's. When this persistence shows up in the residuals of a regression, it is called **serial correlation** or **autocorrelation**.

Visually, you can detect serial correlation by plotting residuals against time. If you see waves — long runs of positive residuals followed by long runs of negative ones, or an oscillating pattern — the residuals are not random scatter around zero but carry information about the next residual. The simplest formal model is the **AR(1) error**: u_t = ρu_{t-1} + ε_t, where ε_t is white noise. The parameter ρ measures how much of the last period's error persists. The **Durbin-Watson statistic** tests for this pattern: DW ≈ 2(1 − ρ̂), so DW near 2 indicates no autocorrelation, DW near 0 indicates strong positive autocorrelation, and DW near 4 indicates strong negative autocorrelation.

Like heteroskedasticity — your related prerequisite — serial correlation does not bias OLS coefficient estimates. The OLS estimator is still unbiased and consistent: it correctly estimates the conditional mean relationship. The damage is to standard errors. OLS treats each observation as providing independent information about the regression relationship. But correlated errors mean consecutive observations carry redundant information — the effective sample size for inference is smaller than the nominal sample size. OLS standard errors understate the true uncertainty, inflating t-statistics and making results appear more statistically significant than they are. This is a serious problem for inference, even though point estimates are fine.

The standard remedy is **HAC (heteroskedasticity-and-autocorrelation consistent) standard errors**, commonly called **Newey-West standard errors**. Instead of assuming errors are uncorrelated, Newey-West estimates the long-run variance of the OLS estimator by summing weighted autocovariances of the residuals up to a chosen lag bandwidth. The bandwidth controls how much autocorrelation structure is estimated — more lags accommodate slower-decaying autocorrelation but require more data for stable estimation. Newey-West standard errors are robust to both heteroskedasticity and serial correlation simultaneously, making them the default choice in time-series regressions when the error structure is unknown.

If you are willing to specify the full error structure, **GLS (generalized least squares)** provides a more efficient alternative. In GLS for AR(1) errors, the regression is transformed by quasi-differencing: y_t − ρy_{t-1} = β(x_t − ρx_{t-1}) + ε_t, which produces uncorrelated errors ε_t. In practice, ρ is unknown and must be estimated first — this is **feasible GLS (FGLS)**. GLS is more efficient than using OLS with HAC standard errors (it actually uses the error structure to improve estimation), but it is less robust: if the AR(1) specification is wrong, GLS can perform poorly. The general recommendation is to use Newey-West for robustness unless you have strong theoretical reasons to specify a particular error structure.
