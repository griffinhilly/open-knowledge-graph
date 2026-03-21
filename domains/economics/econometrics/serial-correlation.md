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

## Questions

```yaml
- question: "A researcher runs a time-series regression and finds that residuals display long runs of positive values followed by long runs of negative values. What is the primary statistical consequence?"
  type: multiple-choice
  options:
    - "The OLS coefficient estimates are biased — they systematically over- or underestimate the true relationship"
    - "The coefficient estimates remain unbiased and consistent, but OLS standard errors understate true uncertainty, inflating t-statistics and making results appear more significant than they are"
    - "The regression cannot be estimated at all because the Gauss-Markov theorem is violated"
    - "Only the intercept estimate is affected; slope coefficients are unaffected by serial correlation in errors"
  answer: 1
  explanation: "Serial correlation violates the Gauss-Markov assumption of uncorrelated errors but does NOT bias OLS coefficient estimates — they remain unbiased and consistent. The damage is to inference. When consecutive errors are positively correlated, observations carry redundant information: the effective sample size for estimating uncertainty is smaller than the nominal sample size. OLS treats all observations as independent and therefore underestimates the true variance of the estimator. The resulting standard errors are too small, t-statistics too large, and confidence intervals too narrow — systematic overconfidence in results."

- question: "A researcher reports a Durbin-Watson statistic of 0.4 for their time-series regression. What does this indicate, and what is the appropriate remedy?"
  type: multiple-choice
  options:
    - "DW ≈ 0.4 indicates strong negative autocorrelation; the remedy is to add more lags to the model"
    - "DW ≈ 0.4 indicates strong positive autocorrelation (since DW ≈ 2(1-ρ), so ρ ≈ 0.8); the remedy is HAC (Newey-West) standard errors or GLS with AR(1) error structure"
    - "DW ≈ 0.4 is in the inconclusive region; no action is needed until it falls below 0"
    - "DW ≈ 0.4 is close enough to zero to indicate heteroskedasticity rather than autocorrelation"
  answer: 1
  explanation: "The Durbin-Watson statistic is approximately DW ≈ 2(1 − ρ̂), where ρ̂ is the first-order autocorrelation of residuals. DW near 2 means ρ ≈ 0 (no autocorrelation); DW near 0 means ρ ≈ 1 (strong positive autocorrelation); DW near 4 means ρ ≈ −1 (strong negative autocorrelation). DW = 0.4 implies ρ̂ ≈ 0.8 — strong positive serial correlation. The standard remedy is Newey-West HAC standard errors, which are valid for autocorrelation of unknown form and provide correct inference without requiring a specific error model."

- question: "Serial correlation in regression errors typically causes OLS standard errors to understate true uncertainty, leading to inflated t-statistics."
  type: true-false
  answer: true
  explanation: "Positive serial correlation means consecutive errors carry similar signs — the observations are not as informationally independent as OLS assumes. OLS standard errors are derived under the assumption that each observation adds independent information, so they systematically underestimate the true variance of the coefficient estimator when observations are actually correlated. The result is t-statistics that are too large, p-values too small, and confidence intervals too narrow. This is why time-series regressions reported with default OLS standard errors and no robustness correction should be viewed skeptically."

- question: "When serial correlation is detected in regression residuals, the OLS coefficient estimates are biased and should be recalculated using GLS."
  type: true-false
  answer: false
  explanation: "This is the central misconception about serial correlation. Unlike omitted variable bias or endogeneity, serial correlation in errors does NOT bias OLS coefficient estimates — they remain unbiased and consistent. The problem is entirely in the standard errors (and therefore inference). GLS corrects efficiency and standard errors, not the point estimates. The recommendation to use GLS or Newey-West is about getting valid p-values and confidence intervals, not about fixing biased slopes. Practitioners who re-estimate slopes due to serial correlation are solving the wrong problem."

- question: "Why does serial correlation in regression errors cause standard errors to be understated, even though the coefficient estimates themselves are unbiased?"
  type: short-answer
  answer: "OLS standard errors are calculated under the assumption that each observation provides independent information about the regression relationship. Serial correlation means consecutive observations are not independent — they carry overlapping information because each error is partially predictable from the previous one. The effective sample size for estimating the uncertainty of the coefficients is smaller than the nominal sample size N. OLS doesn't know this and uses N as if all observations were independent, producing standard errors that are too small. The coefficient estimates are still correct in expectation — each observation still correctly identifies the average relationship — but the uncertainty around those estimates is underreported."
  explanation: "An analogy: asking 100 people for the time when 90 of them synchronized their watches gives you much less independent information than asking 100 fully independent people. OLS treats the 100 correlated observations as fully independent and reports a small standard error, when in fact you have the effective information of far fewer independent observations. Newey-West corrects for this by explicitly estimating the long-run variance, accounting for the autocorrelation structure."
```

## Explainer

From your work on OLS assumptions, you know that the Gauss-Markov theorem requires errors to be uncorrelated across observations. For cross-sectional data — a sample of individuals or firms from a single point in time — this is often plausible. For time-series data, it is almost always violated. Economic variables evolve continuously; today's output depends on yesterday's output, today's inflation reflects last quarter's inflation expectations, and today's forecast error is related to yesterday's. When this persistence shows up in the residuals of a regression, it is called **serial correlation** or **autocorrelation**.

Visually, you can detect serial correlation by plotting residuals against time. If you see waves — long runs of positive residuals followed by long runs of negative ones, or an oscillating pattern — the residuals are not random scatter around zero but carry information about the next residual. The simplest formal model is the **AR(1) error**: u_t = ρu_{t-1} + ε_t, where ε_t is white noise. The parameter ρ measures how much of the last period's error persists. The **Durbin-Watson statistic** tests for this pattern: DW ≈ 2(1 − ρ̂), so DW near 2 indicates no autocorrelation, DW near 0 indicates strong positive autocorrelation, and DW near 4 indicates strong negative autocorrelation.

Like heteroskedasticity — your related prerequisite — serial correlation does not bias OLS coefficient estimates. The OLS estimator is still unbiased and consistent: it correctly estimates the conditional mean relationship. The damage is to standard errors. OLS treats each observation as providing independent information about the regression relationship. But correlated errors mean consecutive observations carry redundant information — the effective sample size for inference is smaller than the nominal sample size. OLS standard errors understate the true uncertainty, inflating t-statistics and making results appear more statistically significant than they are. This is a serious problem for inference, even though point estimates are fine.

The standard remedy is **HAC (heteroskedasticity-and-autocorrelation consistent) standard errors**, commonly called **Newey-West standard errors**. Instead of assuming errors are uncorrelated, Newey-West estimates the long-run variance of the OLS estimator by summing weighted autocovariances of the residuals up to a chosen lag bandwidth. The bandwidth controls how much autocorrelation structure is estimated — more lags accommodate slower-decaying autocorrelation but require more data for stable estimation. Newey-West standard errors are robust to both heteroskedasticity and serial correlation simultaneously, making them the default choice in time-series regressions when the error structure is unknown.

If you are willing to specify the full error structure, **GLS (generalized least squares)** provides a more efficient alternative. In GLS for AR(1) errors, the regression is transformed by quasi-differencing: y_t − ρy_{t-1} = β(x_t − ρx_{t-1}) + ε_t, which produces uncorrelated errors ε_t. In practice, ρ is unknown and must be estimated first — this is **feasible GLS (FGLS)**. GLS is more efficient than using OLS with HAC standard errors (it actually uses the error structure to improve estimation), but it is less robust: if the AR(1) specification is wrong, GLS can perform poorly. The general recommendation is to use Newey-West for robustness unless you have strong theoretical reasons to specify a particular error structure.
