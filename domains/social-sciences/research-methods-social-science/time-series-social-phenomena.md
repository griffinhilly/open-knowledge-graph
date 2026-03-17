---
id: time-series-social-phenomena
title: Time Series Analysis of Social Phenomena
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: linear-regression-social-science
  type: hard
- id: sequences-and-series-review
  type: hard
- id: functions-domain-codomain-range
  type: soft
- id: differential-equations-intro
  type: soft
tags:
- time-series
- autocorrelation
- stationarity
- policy-evaluation
stage: advanced
status: draft
---

# Time Series Analysis of Social Phenomena

## Core Idea
Extends regression methods to analyze temporal social data with autocorrelation. Covers autoregressive models, moving averages, testing for stationarity, and interrupted time series designs for evaluating policy interventions. Addresses challenges of serial correlation in social data.

## How It's Best Learned
Analyze aggregate time series data (crime, unemployment, attitudes), test for stationarity and autocorrelation, estimate ARIMA models, design interrupted time series to evaluate policy.

## Common Misconceptions
- More time points always enable better inference
- Autocorrelation is a problem rather than a feature
- Interrupted time series requires random assignment

## Explainer

In your prerequisite work with regression, each observation was treated as independent — the error terms were assumed uncorrelated across cases. With social time series data, this assumption breaks down immediately. Crime rates, unemployment, public opinion, and institutional budgets all exhibit **autocorrelation**: this year's value is correlated with last year's because underlying conditions persist over time. Treating autocorrelated data as independent observations leads to artificially small standard errors, false confidence, and spurious findings. Time series methods are the toolkit for handling data where observations are ordered in time and each observation is not independent of its neighbors.

The foundational diagnostic is **stationarity** — whether the statistical properties of a series (mean, variance, autocorrelation structure) are stable over time, or whether the series is drifting or growing. A non-stationary series has a mean or variance that changes over time, making it impossible to model reliably. The classic test is the **Augmented Dickey-Fuller test**, which checks whether a series has a unit root (a sign of non-stationarity). Many social variables — unemployment levels, GDP, population — are non-stationary in levels but become stationary after differencing (working with period-to-period changes rather than raw levels). This is why macroeconomic models often work with growth rates rather than levels. Your background in sequences gives you the core intuition: a stationary series behaves like a bounded sequence, while a non-stationary series can drift without bound.

**ARIMA models** (Autoregressive Integrated Moving Average) are the workhorse of time series analysis. The autoregressive (AR) component models the current value as a linear function of past values: this month's unemployment partly depends on last month's. The moving average (MA) component models the current value as a function of past *error terms*: random shocks propagate forward through time. The "I" stands for integration — how many times you need to difference the series to achieve stationarity. An ARIMA(2,1,1) model has two autoregressive terms, is differenced once, and has one moving average term. Your background in differential equations makes the underlying logic intuitive: ARIMA is a discrete-time dynamic model of how a series evolves, analogous to a first-order difference equation with stochastic inputs.

**Interrupted time series (ITS)** designs apply time series logic to causal inference about policy interventions. The idea: collect many pre-intervention observations to model the counterfactual trend (what would have happened without the policy), then compare post-intervention observations to that projected trend. A law banning cell phone use while driving would show up as an abrupt change in accident rates (a level change) or a changed trajectory (a slope change) after implementation. ITS is one of the strongest quasi-experimental designs for policy evaluation because it doesn't require random assignment — it uses time itself to construct the counterfactual. The key threat to validity is concurrent history effects: other events may have changed at the same moment as the intervention, making it hard to attribute the change to the policy alone. Multiple replications across jurisdictions and times provide the strongest ITS evidence.
