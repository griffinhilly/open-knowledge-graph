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

## Explainer

You already know from stationarity that a well-behaved time series has statistical properties that don't drift over time. An AR model exploits exactly this property: if a series is stationary, its past values contain genuine predictive information about its current value. An **autoregressive model of order p**, written AR(p), formalizes this by regressing yₜ — today's value — on its own p most recent lags: yₜ = c + φ₁yₜ₋₁ + φ₂yₜ₋₂ + ... + φₚyₜ₋ₚ + εₜ. Think of GDP growth, which tends to persist: a strong quarter is more likely to be followed by another strong quarter than by a contraction. The φ coefficients capture exactly that persistence.

The trickiest part of AR modeling is choosing p — how many lags to include. Two diagnostic tools guide this. The **autocorrelation function (ACF)** measures the correlation between yₜ and yₜ₋ₖ for various lags k; it shows total correlation including indirect effects. The **partial autocorrelation function (PACF)** strips out those indirect effects and shows the unique contribution of each lag after controlling for shorter lags. For an AR(p) process, the PACF cuts off sharply after lag p while the ACF decays gradually. This contrast is your diagnostic: if the PACF drops to near zero after lag 2 and the ACF declines slowly, you're likely looking at an AR(2).

For a more formal approach, **information criteria** like AIC (Akaike) and BIC (Bayesian) balance fit against parsimony — BIC penalizes complexity more heavily than AIC. You fit models of various orders and choose the p that minimizes the criterion. The practical advice: start with the PACF plot to get a ballpark, then confirm with AIC/BIC, and prefer lower-order models unless higher-order ones show substantial improvement.

The stability of an AR model depends critically on the φ coefficients. You learned about unit roots when studying stationarity: if φ₁ = 1 in an AR(1), the series has a unit root and is nonstationary — past shocks never die out, and standard inference breaks down. For a stationary AR(p), all roots of the characteristic polynomial must lie outside the unit circle. In practice, this means the φ coefficients must be constrained appropriately. This is why stationarity testing comes before AR modeling — an AR model fitted to a nonstationary series produces spurious, uninterpretable results. Once you confirm stationarity (or difference to achieve it), AR models become powerful forecasting workhorses, forming the AR component of the more general ARIMA framework you'll encounter next.
