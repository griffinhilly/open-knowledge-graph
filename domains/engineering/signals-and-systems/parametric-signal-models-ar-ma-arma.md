---
id: parametric-signal-models-ar-ma-arma
title: 'Parametric Signal Models: AR, MA, and ARMA'
domain: engineering
course: signals-and-systems
prerequisites:
- id: autocorrelation-function-properties-estimation
  type: hard
builds-toward:
- system-identification-basics
- digital-spectral-analysis-nonparametric
tags:
- parametric-models
- AR
- MA
- ARMA
- signal-modeling
stage: concrete-application
status: draft
---

# Parametric Signal Models: AR, MA, and ARMA

## Core Idea
Parametric models represent signals as outputs of linear systems driven by white noise. Autoregressive (AR) models use feedback (poles only); moving-average (MA) models use feedforward (zeros only); ARMA uses both. These models are more parsimonious than non-parametric methods for sufficiently regular signals, enabling spectral estimation with fewer parameters. Model order selection and parameter estimation are critical for accuracy.

## How It's Best Learned
Generate autoregressive signal using known AR coefficients. Estimate AR model order and coefficients from the data using Yule-Walker method. Verify estimated parameters match generation parameters.

## Common Misconceptions
- Thinking AR, MA, ARMA are different types of signals (they're models that can represent similar signals).
- Confusing model order with model quality (higher order doesn't guarantee better fit).
- Not recognizing stability constraints for AR models (poles must be inside unit circle).
