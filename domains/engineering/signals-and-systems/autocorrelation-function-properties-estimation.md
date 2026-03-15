---
id: autocorrelation-function-properties-estimation
title: Autocorrelation Function Properties and Estimation
domain: engineering
course: signals-and-systems
prerequisites:
- id: random-signals-autocorrelation-psd
  type: hard
builds-toward:
- parametric-signal-models-ar-ma-arma
- signal-detection-and-hypothesis-testing
tags:
- correlation
- autocorrelation
- estimation
- properties
stage: formal-systems
status: draft
---

# Autocorrelation Function Properties and Estimation

## Core Idea
The autocorrelation function (ACF) measures signal self-similarity at different time lags, revealing periodicity, trend, and stationarity. The ACF is maximum at lag zero, even (symmetric), and bounded by signal energy. For finite observations, biased and unbiased ACF estimators trade bias for variance. The ACF of white noise is an impulse at lag zero; colored noise shows non-zero lags. ACF is the Fourier transform of power spectral density.

## How It's Best Learned
Compute ACF of sinusoid, random noise, and autoregressive signal. Observe lag structure and relate to expected properties. Compare biased vs unbiased estimators on short records.

## Common Misconceptions
- Thinking ACF can exceed unity in magnitude.
- Confusing autocorrelation with cross-correlation computation.
- Not recognizing that autocorrelation is real and even for real signals.
