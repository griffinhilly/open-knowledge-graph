---
id: arima-models-forecasting
title: ARIMA Models and Time Series Forecasting
domain: economics
course: econometrics
prerequisites:
- id: autoregressive-ar-models
  type: hard
- id: sequences-convergence
  type: soft
builds-toward:
- vector-autoregression-models
tags:
- time-series
- arima
- forecasting
stage: formal-systems
status: draft
---

# ARIMA Models and Time Series Forecasting

## Core Idea
ARIMA(p,d,q) models combine autoregressive (p), integrated (d orders of differencing), and moving average (q) components to handle nonstationary series. These parsimonious models often outperform complex alternatives in short-term forecasting. Selection relies on AIC/BIC; diagnostic checks verify residuals are white noise.

## How It's Best Learned
Fit ARIMA models to economic time series (unemployment, inflation) and compare one-step-ahead forecast accuracy across specifications.

## Common Misconceptions
ARIMA requires stationarity in the differenced series, but differencing too many times (over-differencing) can introduce spurious dynamics.

## Explainer

ARIMA(p,d,q) stands for Autoregressive Integrated Moving Average. From your prerequisite on AR models, you already know how the autoregressive part works: current values are a weighted sum of p past values plus noise. The "I" component is new: it handles non-stationarity by **differencing**. If a series like monthly employment trends persistently upward, its level is non-stationary — the mean keeps shifting. Taking the first difference (change in employment) may produce a stationary series. Taking d differences removes deterministic and stochastic trends, transforming the series into something that AR and MA components can model.

The **moving average (MA)** component is the complement to AR. Where AR says "the current value depends on past values of the series," MA says "the current value depends on past forecast errors (shocks)." An MA(1) model says today's value equals a constant plus the current shock plus a fraction of yesterday's shock. Economically, this captures situations where a random event — say, a one-time supply disruption — has a fading effect on subsequent periods. AR captures persistent autocorrelation in levels; MA captures the decay of shocks. Together they cover two distinct memory mechanisms.

**Model identification** uses the autocorrelation function (ACF) and partial autocorrelation function (PACF) as diagnostic tools. A pure AR(p) process has PACF that cuts off sharply after lag p. A pure MA(q) process has ACF that cuts off after lag q. Mixed ARMA processes show gradual decay in both. In practice, you fit multiple ARMA(p,q) specifications to the differenced series and select using information criteria: AIC rewards fit but penalizes complexity less harshly than BIC, so BIC tends toward more parsimonious models. This identification-estimation-checking cycle is the Box-Jenkins methodology.

Once you select a model, **diagnostic checking** confirms adequacy. Residuals from a well-specified ARIMA model should be white noise — serially uncorrelated, with no remaining autocorrelation. The Ljung-Box test checks this formally. If residuals still show autocorrelation, you need more AR or MA terms. If variance grows over time, GARCH extensions may be needed. The goal is residuals that look like independent draws from the same distribution — any remaining structure is an exploitable pattern the model missed.

Forecasting with ARIMA is mechanical once the model is fit: plug in known lagged values for point forecasts and propagate uncertainty for prediction intervals. A key characteristic is that ARIMA forecasts **revert toward the mean** quickly for stationary series — after several periods, the forecast converges to the unconditional mean. This is appropriate for mean-reverting processes but limits the model's usefulness for series with structural breaks or genuine long-run trends. The model's practical strength is parsimony and reliable short-horizon performance; its limitation is that it treats the historical pattern as a complete guide to the future.
