---
id: vector-autoregression-var
title: Vector Autoregression (VAR) Models
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: time-series-cross-section
  type: hard
- id: causal-inference-observational-data
  type: soft
- id: eigenvalues-eigenvectors
  type: hard
- id: matrix-operations
  type: hard
- id: systems-of-first-order-linear-odes
  type: soft
- id: eigenvalues-and-eigenvectors
  type: soft
builds-toward:
- structural-var-models
- impulse-response-analysis
tags:
- time-series
- multivariate
- dynamics
- causal
stage: advanced
status: draft
---

# Vector Autoregression (VAR) Models

## Core Idea
Vector autoregression models capture dynamic interdependencies among multiple time series. Each variable is regressed on its own past values and the past values of all other variables. VARs reveal which variables Granger-cause others, and impulse-response functions show how a shock to one variable propagates through the system. VARs are used to study feedback loops in economic systems, policy dynamics, and social processes.

## Explainer

From your time series prerequisites, you know how to model a single variable — say, GDP growth — using its own past values via an autoregressive (AR) model. But social and economic systems rarely evolve in isolation. GDP growth, unemployment, and inflation interact dynamically: a rise in unemployment may suppress inflation, which may prompt a policy rate cut, which may stimulate growth, which reduces unemployment. A **Vector Autoregression (VAR)** model handles this by running a system of AR equations simultaneously — one for each variable — where every variable in the system can depend on its own lags and the lags of every other variable.

The matrix representation connects directly to your linear algebra prerequisites. If you have k variables and p lags, the VAR(p) model is written as **y_t = A_1 y_{t-1} + A_2 y_{t-2} + ... + A_p y_{t-p} + ε_t**, where **y_t** is a k×1 vector of observations and each **A_i** is a k×k coefficient matrix. The eigenvalues of the companion matrix determine stability — for the system to be stationary (not explosive), all eigenvalues must lie inside the unit circle. This is exactly the stability analysis from your dynamical systems background applied to empirical data.

**Granger causality** is one of the key tools VAR provides. Variable X Granger-causes Y if past values of X help predict Y beyond what Y's own past already predicts — tested by whether the coefficients on lagged X in the Y equation are jointly significant. This is a statistical definition of predictive precedence, not philosophical causality, but it is a principled way to detect directional temporal relationships in observational data. From your causal inference prerequisites, you know this is not the same as establishing structural causation — Granger causality can be confounded by omitted variables.

**Impulse response functions (IRFs)** translate VAR coefficients into something interpretable: they trace how a one-unit shock to one variable ripples through the system over time. If you hit GDP with an unexpected positive shock, the IRF shows the predicted trajectory of GDP, unemployment, and inflation over the next several periods. The shape of these paths — does unemployment respond quickly or slowly? does the effect persist or decay? — is typically what researchers report. Because all variables affect all others, the shocks must be **orthogonalized** (usually via Cholesky decomposition) to separate their effects, which requires ordering decisions that encode causal assumptions. This is where the transition to structural VAR models begins.
