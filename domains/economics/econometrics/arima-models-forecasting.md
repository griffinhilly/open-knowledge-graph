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
