---
id: finite-distributed-lag-models
title: Finite Distributed Lag Models
domain: economics
course: econometrics
prerequisites:
- id: time-series-basics-econometrics
  type: hard
- id: multiple-regression-model
  type: hard
- id: multicollinearity
  type: soft
- id: serial-correlation
  type: soft
builds-toward:
- lagged-dependent-variable-regression
tags:
- time series regression
- distributed lag
- impact propensity
- long-run propensity
- lag distribution
- dynamic effects
stage: formal-systems
status: validated
---

# Finite Distributed Lag Models

## Core Idea
A finite distributed lag (FDL) model lets a variable z affect y with a delay by including current and past values of z as regressors: y_t = α₀ + δ₀z_t + δ₁z_{t−1} + ... + δ_q z_{t−q} + u_t. The coefficient δ₀ is the impact propensity, the immediate effect of a one-unit rise in z. The sequence δ₀, δ₁, ..., δ_q is the lag distribution, tracing the effect of a temporary change over time. The sum δ₀ + δ₁ + ... + δ_q is the long-run propensity (LRP), the eventual effect of a permanent one-unit increase in z.

## How It's Best Learned
Take a two-lag model with given coefficients and trace by hand what happens to y after z rises by one unit for a single period and after it rises by one unit permanently. Plot both paths. The temporary path shows the lag distribution; the permanent path climbs to the LRP. Then show how to estimate the LRP and its standard error directly by rewriting the regression.

## Common Misconceptions
- The coefficient on the current value of z measures the full effect of z on y. (It is only the impact effect; with lags, the effect of a permanent change builds up to the sum of all lag coefficients.)
- Insignificant individual lag coefficients mean the lags do not matter. (Lags of z are usually highly correlated, so individual coefficients are imprecise even when the LRP is estimated precisely and is significant.)
- A temporary and a permanent change in z have the same long-run effect. (A temporary change has no effect after q periods, while a permanent change raises y by the LRP.)

## Questions

```yaml
- question: "In the model y_t = 2 + 0.5z_t + 0.3z_{t−1} + 0.1z_{t−2} + u_t, z rises by one unit in period 0 and returns to its old level in period 1. By how much does y differ from its old level in period 2?"
  type: multiple-choice
  options: ["0.5", "0.3", "0.1", "0.9"]
  answer: 2
  explanation: "A temporary change affects y_t through the lag that corresponds to period 0. In period 2, the period-0 rise enters through z_{t−2}, whose coefficient is 0.1. By period 3, y is back at its old level."
- question: "In the same model, what is the long-run propensity?"
  type: multiple-choice
  options: ["0.5", "0.8", "0.9", "2.9"]
  answer: 2
  explanation: "The LRP is δ₀ + δ₁ + δ₂ = 0.5 + 0.3 + 0.1 = 0.9. It is the change in y, after two periods, from a permanent one-unit increase in z."
- question: "It is possible for each lag coefficient in an FDL model to be individually insignificant while the long-run propensity is significant."
  type: true-false
  answer: true
  explanation: "Current and lagged z are often highly correlated, which inflates the standard errors of individual δ's. Their sum can still be estimated precisely, because the regression can tell the combined effect apart even when it cannot apportion it among the lags."
- question: "Describe how to obtain the standard error of the LRP θ = δ₀ + δ₁ + δ₂ directly from a single OLS regression."
  type: short-answer
  answer: "Substitute δ₀ = θ − δ₁ − δ₂ into the model. It becomes y_t = α₀ + θz_t + δ₁(z_{t−1} − z_t) + δ₂(z_{t−2} − z_t) + u_t. Regress y_t on z_t, (z_{t−1} − z_t), and (z_{t−2} − z_t); the coefficient on z_t is θ̂ and its reported standard error is the standard error of the LRP."
  explanation: "This reparameterization is a general trick for getting the standard error of a linear combination of coefficients without computing covariances by hand."
```

## Explainer
In cross-section regression, x affects y at the same moment. Over time, effects often take a while. A rise in the minimum wage may change employment over several quarters. A tax change may affect births with a delay of a year or more, since decisions about having children respond slowly. A **finite distributed lag model** captures this by including several past values of the explanatory variable.

With two lags the model is y_t = α₀ + δ₀z_t + δ₁z_{t−1} + δ₂z_{t−2} + u_t. To read the coefficients, run two thought experiments.

First, a **temporary** change. Suppose z is constant at c, rises to c + 1 in period 0, and returns to c in period 1. In period 0, y rises by δ₀. In period 1, the bump in z appears as z_{t−1}, so y is δ₁ above its old level. In period 2, it appears as z_{t−2}, so y is δ₂ above. From period 3 on, y is back to normal. The sequence δ₀, δ₁, δ₂, plotted against the lag, is the **lag distribution**. δ₀ is called the **impact propensity**.

Second, a **permanent** change. Suppose z rises from c to c + 1 in period 0 and stays there. In period 0, y rises by δ₀. In period 1 both z_t and z_{t−1} are higher, so y is δ₀ + δ₁ above its old level. From period 2 on, y is δ₀ + δ₁ + δ₂ above. That sum is the **long-run propensity**, often the number policy makers care most about.

Estimation uses OLS, and the usual time-series assumptions apply. One practical issue is multicollinearity. Consecutive values of z tend to move together, so the regression has trouble separating δ₀ from δ₁ from δ₂, and individual standard errors are large. The sum is often estimated well anyway. To get its standard error, define θ = δ₀ + δ₁ + δ₂ and substitute δ₀ = θ − δ₁ − δ₂. The model becomes y_t = α₀ + θz_t + δ₁(z_{t−1} − z_t) + δ₂(z_{t−2} − z_t) + u_t, and the coefficient on z_t estimates θ with its own standard error.

Choosing the number of lags involves a tradeoff. More lags capture slow effects but use up degrees of freedom and add collinearity. F-tests on the last lags and information criteria help. Models that also include lagged y are a natural next step.
