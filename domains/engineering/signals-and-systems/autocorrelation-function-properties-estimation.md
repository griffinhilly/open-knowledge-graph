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

## Explainer

From your study of random signals and power spectral density, you know that a random signal cannot be described sample by sample — instead you characterize it statistically. The **autocorrelation function** R_x(τ) = E[x(t)x(t+τ)] asks a deceptively simple question: how much does a signal resemble a time-shifted copy of itself? At lag τ = 0, a signal is perfectly correlated with itself, so R_x(0) = E[x²(t)] = the signal's average power — the maximum possible value. At large lags, if the signal is stationary and ergodic, R_x(τ) → 0 because distant samples become uncorrelated. The shape of R_x(τ) between these extremes encodes the signal's temporal structure.

Three fundamental properties follow from the definition and are worth internalizing geometrically. First, **R_x(0) ≥ |R_x(τ)|** for all τ — the zero-lag value is always the global maximum. Second, the ACF is **even**: R_x(τ) = R_x(−τ), because flipping the sign of the lag just reverses which sample leads and which follows, and the product is the same. Third, the ACF of a **periodic signal** is itself periodic at the same period — a sinusoid's ACF is a cosine, not a decaying function. This makes the ACF a detector of hidden periodicity: even if a periodic signal is buried in broadband noise, the ACF will show a persistent oscillation at the signal's period while the noise contribution decays toward zero. The link to your PSD prerequisite: by the Wiener-Khinchin theorem, the power spectral density S_x(f) is exactly the Fourier transform of R_x(τ). ACF and PSD are a Fourier pair — two views of the same information.

Estimating R_x(τ) from a finite data record introduces practical complications. The **biased estimator** R̂_x(τ) = (1/N) Σ x(n)x(n+τ), summing over all available sample pairs and dividing by N (the total record length rather than the number of pairs), is biased — it underestimates the true ACF at large lags — but has lower variance and always produces a valid (positive semi-definite) spectrum when Fourier-transformed. The **unbiased estimator** divides by N−|τ| (the actual number of pairs available at each lag), which removes the bias but inflates variance at large lags, where few pairs exist, sometimes producing nonsensical negative spectral estimates. The rule of thumb: use the biased estimator in practice; restrict interpretation to lags much shorter than the record length (τ_max ≤ N/10 is common).

The **ACF of white noise** is an impulse at τ = 0 and zero everywhere else — white noise is uncorrelated sample to sample by definition. Any departure from an impulsive ACF signals structure in the data: a slowly decaying ACF suggests long-range correlation (an AR process with poles near the unit circle), while an ACF that drops to zero abruptly after M lags signals a moving-average process of order M. This diagnostic reading of ACF shape is the practical skill this topic builds — it is the foundation for model order selection in AR/MA/ARMA parametric modeling and for detecting whether a signal has been filtered, correlated, or corrupted in time-structured ways.
