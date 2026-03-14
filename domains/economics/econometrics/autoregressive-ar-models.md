---
id: autoregressive-ar-models
title: Autoregressive (AR) Models and Order Selection
domain: economics
course: econometrics
prerequisites:
- id: unit-roots-stationarity
  type: hard
builds-toward:
- arima-models-forecasting
tags:
- time-series
- ar-models
- stationary
stage: formal-systems
status: draft
---

# Autoregressive (AR) Models and Order Selection

## Core Idea
An AR(p) model regresses a series on its own p lags: yₜ = c + φ₁yₜ₋₁ + ... + φₚyₜ₋ₚ + εₜ. Order p is chosen using ACF/PACF plots or information criteria; AR models capture temporal dependence and form the basis for ARMA and ARIMA extensions.
