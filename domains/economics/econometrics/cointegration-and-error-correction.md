---
id: cointegration-and-error-correction
title: Cointegration and Error Correction Models
domain: economics
course: econometrics
prerequisites:
- id: stationarity-and-unit-roots
  type: hard
- id: unit-roots-stationarity
  type: soft
- id: simple-linear-regression-estimation
  type: soft
- id: vector-autoregression-models
  type: soft
builds-toward: []
tags:
- time series
- cointegration
- error correction model
- Engle-Granger
- spurious regression
- long-run equilibrium
stage: advanced
status: validated
---

# Cointegration and Error Correction Models

## Core Idea
Two series that each have a unit root, I(1), are cointegrated if some linear combination of them, such as y_t − βx_t, is stationary, I(0). Cointegration means the series share a common stochastic trend and do not drift apart in the long run, so a regression of one on the other is meaningful rather than spurious. The Engle-Granger method estimates β by OLS and then tests the residuals for a unit root using special critical values. When series are cointegrated, an error correction model links short-run changes to the previous period's deviation from the long-run relationship.

## How It's Best Learned
Simulate two random walks that share a common trend and two that are independent, and plot each pair along with the residual from regressing one on the other. Students see the residual wander without bound in the spurious case and revert in the cointegrated case. Then estimate an error correction model on the cointegrated pair and interpret the adjustment coefficient as the fraction of last period's gap closed each period.

## Common Misconceptions
- A high R² between two trending series shows they are cointegrated. (Independent random walks often produce high R² and large t-statistics; cointegration must be tested through the stationarity of the residuals.)
- The residuals from the cointegrating regression can be tested with ordinary Dickey-Fuller critical values. (Because β is estimated to make the residuals look as stationary as possible, the test needs Engle-Granger critical values, which are more negative.)
- Differencing both series is always the safe response to unit roots. (If the series are cointegrated, a model only in differences drops the long-run relationship; the error correction term restores it.)

## Questions

```yaml
- question: "Two series y_t and x_t are both I(1). Which finding would indicate they are cointegrated?"
  type: multiple-choice
  options: ["The regression of y on x has R² above 0.9", "The residuals from regressing y_t on x_t are stationary", "Both Δy_t and Δx_t are stationary", "The correlation of the levels exceeds 0.8"]
  answer: 1
  explanation: "Cointegration means a linear combination of the I(1) series is I(0). The residual from the levels regression estimates that combination, so testing it for stationarity is the Engle-Granger test. Stationary first differences hold for any pair of I(1) series, and high R² or correlation often appears even between unrelated random walks, so neither shows cointegration."
- question: "In the error correction model Δy_t = α + γΔx_t + δ(y_{t−1} − βx_{t−1}) + u_t, an estimate δ = −0.25 means about one quarter of last period's deviation from the long-run relationship is corrected in the current period."
  type: true-false
  answer: true
  explanation: "If y was above its long-run level βx last period, the negative δ pulls Δy down this period by 25% of the gap. A negative δ is required for the system to move back toward equilibrium."
- question: "Why does the Engle-Granger residual-based test use different critical values from a standard Dickey-Fuller test?"
  type: multiple-choice
  options: ["Because the residuals are always normally distributed", "Because OLS chooses β to minimize residual variance, which makes the residuals look more stationary than a series that was not estimated", "Because the test is two-sided", "Because the residuals have a deterministic trend"]
  answer: 1
  explanation: "OLS picks the combination of y and x with the smallest residual variance. That fitting biases the test toward finding stationarity, so stricter, more negative critical values are needed to keep the test's size correct."
- question: "Explain why a regression in first differences alone can be misspecified when two series are cointegrated."
  type: short-answer
  answer: "Differencing removes the unit roots but also removes the information that the levels are tied together in the long run. If the series are cointegrated, past deviations from the long-run relationship help predict changes, so the differenced model omits a relevant variable, the lagged error correction term."
  explanation: "The Granger representation theorem states that cointegrated series have an error correction representation, so the error correction term belongs in the model."
```

## Explainer
From your work on unit roots you know that regressing one I(1) series on another can produce a spurious regression: high R² and significant t-statistics even when the series are unrelated. The usual fix is to difference the data. But some pairs of trending series really are tied together. Consumption and income both grow, but consumption does not drift arbitrarily far from income. Short- and long-term interest rates move a lot, but the spread between them tends to return toward a typical level. Cointegration describes this case.

Two I(1) series x_t and y_t are **cointegrated** if there is a number β such that y_t − βx_t is stationary. Each series wanders, but they wander together, because they share a common stochastic trend. The combination y_t − βx_t measures the distance from long-run equilibrium, and that distance keeps returning toward its mean. Clive Granger introduced the idea, and his 1987 paper with Robert Engle set out how to represent, estimate, and test it. Granger's work on cointegration was cited when the two shared the 2003 Nobel Memorial Prize in Economic Sciences.

The **Engle-Granger two-step method** tests for it. First, regress y_t on x_t in levels by OLS and save the residuals. Second, run a Dickey-Fuller-type regression on those residuals. If you reject a unit root, the series are cointegrated. The critical values differ from the usual Dickey-Fuller table. Because OLS chose β to make the residuals as small as possible, they look more stationary than an arbitrary series would, so the test requires stronger evidence. With cointegration, the OLS estimate of β converges to the true value unusually fast, a property called superconsistency.

Once cointegration is established, the **error correction model** describes the short run:

Δy_t = α + γΔx_t + δ(y_{t−1} − βx_{t−1}) + u_t.

Every term in this equation is stationary, so the usual regression tools can be used for γ and δ. The coefficient γ captures the immediate response to a change in x. The coefficient δ, expected to be negative, governs adjustment: if y was above its long-run level last period, y tends to fall now. With δ = −0.25, about a quarter of any gap closes each period. Granger's representation theorem shows that cointegration and an error correction form go together.

For more than two series there can be several cointegrating relationships. Johansen's method tests for their number within a vector autoregression, producing a vector error correction model.
