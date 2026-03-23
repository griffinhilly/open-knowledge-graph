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
status: validated
---

# Autoregressive (AR) Models and Order Selection

## Core Idea
An AR(p) model regresses a series on its own p lags: yₜ = c + φ₁yₜ₋₁ + ... + φₚyₜ₋ₚ + εₜ. Order p is chosen using ACF/PACF plots or information criteria; AR models capture temporal dependence and form the basis for ARMA and ARIMA extensions.

## Questions

```yaml
- question: "You examine the ACF and PACF plots of a time series. The PACF has large spikes at lags 1 and 2 but is near zero for lags 3 and beyond. The ACF decays gradually. Which model specification does this suggest?"
  type: multiple-choice
  options:
    - "AR(1), because the first lag is the strongest"
    - "MA(2), because the partial autocorrelations cut off after lag 2"
    - "AR(2), because the PACF cuts off after lag 2 while the ACF decays gradually"
    - "ARMA(2,2), because both the ACF and PACF show some nonzero values"
  answer: 2
  explanation: "The diagnostic signature of an AR(p) process is exactly this pattern: the PACF cuts off sharply after lag p (dropping to near zero), while the ACF decays gradually (often exponentially or in a damped oscillation). An MA(q) process shows the opposite: ACF cuts off, PACF decays. ARMA processes show both gradually decaying. Here, sharp PACF cutoff at lag 2 and gradual ACF decay clearly point to AR(2)."

- question: "A researcher fits an AR(3) model to a monthly time series without first testing for stationarity. The series turns out to have a unit root. What is the most serious consequence?"
  type: multiple-choice
  options:
    - "The model will overfit and select too many lags via AIC"
    - "The estimated φ coefficients will all equal 1 by definition"
    - "The estimates will be spurious and standard inference breaks down — t-statistics and confidence intervals are invalid for nonstationary series"
    - "The model will fail to converge because AR models require finite variance"
  answer: 2
  explanation: "Fitting an AR model to a nonstationary series produces spurious results. The assumption underlying AR modeling — that past values carry genuine predictive information in a stable statistical relationship — requires stationarity. With a unit root, shocks never die out, the variance grows without bound, and the distribution theory behind standard errors and t-tests collapses. This is why stationarity testing (ADF, KPSS) must precede AR model fitting."

- question: "For an AR(p) process, the autocorrelation function (ACF) cuts off sharply to zero after lag p, making the ACF the primary tool for identifying the correct order."
  type: true-false
  answer: false
  explanation: "This describes the MA(q) process, not the AR(p) process. For AR(p), it is the PACF that cuts off sharply after lag p — the ACF decays gradually. The ACF captures total correlation including indirect effects through intermediate lags, so even an AR(1) will have nonzero ACF at lags 2, 3, etc. (via the chain yₜ → yₜ₋₁ → yₜ₋₂). The PACF removes those indirect effects, revealing only the direct lag coefficients."

- question: "An AR model regresses the current value of a time series on its own past values, exploiting the idea that a stationary series can contain predictive information about itself."
  type: true-false
  answer: true
  explanation: "This is the defining structure of autoregressive models. 'Autoregressive' means self-regressing — the series predicts itself using its own history. The stationarity requirement ensures that this predictive relationship is stable over time: the same lag coefficients that held last year still hold this year. Without stationarity, the relationship drifts, and regression on past values produces meaningless results."

- question: "Why does the PACF cut off after lag p for an AR(p) process, while the ACF does not?"
  type: short-answer
  answer: "The ACF at lag k measures total correlation between yₜ and yₜ₋ₖ — including all indirect paths through intermediate lags. In an AR(2), for instance, yₜ is correlated with yₜ₋₃ through the chain yₜ → yₜ₋₁ → yₜ₋₂ → yₜ₋₃, even though yₜ₋₃ has no direct coefficient in the model. The PACF controls for all shorter lags and measures only the direct contribution of each lag. Since an AR(p) has direct coefficients only for lags 1 through p, the PACF drops to zero after lag p — there are no more direct effects to detect."
  explanation: "This is why the PACF is the right diagnostic tool for AR order selection. It strips away the indirect correlations that make the ACF decay gradually, revealing the 'true' lag structure. The symmetry: for MA(q), the ACF cuts off (direct moving-average structure) and the PACF decays; for AR(p), the PACF cuts off and the ACF decays."
```

## Explainer

You already know from stationarity that a well-behaved time series has statistical properties that don't drift over time. An AR model exploits exactly this property: if a series is stationary, its past values contain genuine predictive information about its current value. An **autoregressive model of order p**, written AR(p), formalizes this by regressing yₜ — today's value — on its own p most recent lags: yₜ = c + φ₁yₜ₋₁ + φ₂yₜ₋₂ + ... + φₚyₜ₋ₚ + εₜ. Think of GDP growth, which tends to persist: a strong quarter is more likely to be followed by another strong quarter than by a contraction. The φ coefficients capture exactly that persistence.

The trickiest part of AR modeling is choosing p — how many lags to include. Two diagnostic tools guide this. The **autocorrelation function (ACF)** measures the correlation between yₜ and yₜ₋ₖ for various lags k; it shows total correlation including indirect effects. The **partial autocorrelation function (PACF)** strips out those indirect effects and shows the unique contribution of each lag after controlling for shorter lags. For an AR(p) process, the PACF cuts off sharply after lag p while the ACF decays gradually. This contrast is your diagnostic: if the PACF drops to near zero after lag 2 and the ACF declines slowly, you're likely looking at an AR(2).

For a more formal approach, **information criteria** like AIC (Akaike) and BIC (Bayesian) balance fit against parsimony — BIC penalizes complexity more heavily than AIC. You fit models of various orders and choose the p that minimizes the criterion. The practical advice: start with the PACF plot to get a ballpark, then confirm with AIC/BIC, and prefer lower-order models unless higher-order ones show substantial improvement.

The stability of an AR model depends critically on the φ coefficients. You learned about unit roots when studying stationarity: if φ₁ = 1 in an AR(1), the series has a unit root and is nonstationary — past shocks never die out, and standard inference breaks down. For a stationary AR(p), all roots of the characteristic polynomial must lie outside the unit circle. In practice, this means the φ coefficients must be constrained appropriately. This is why stationarity testing comes before AR modeling — an AR model fitted to a nonstationary series produces spurious, uninterpretable results. Once you confirm stationarity (or difference to achieve it), AR models become powerful forecasting workhorses, forming the AR component of the more general ARIMA framework you'll encounter next.
