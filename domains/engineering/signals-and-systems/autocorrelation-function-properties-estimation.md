---
id: autocorrelation-function-properties-estimation
title: Autocorrelation Function Properties and Estimation
domain: engineering
course: signals-and-systems
prerequisites:
- id: random-signals-autocorrelation-psd
  type: hard
- id: cross-correlation-applications-estimation
  type: soft
builds-toward:
- parametric-signal-models-ar-ma-arma
- signal-detection-and-hypothesis-testing
tags:
- correlation
- autocorrelation
- estimation
- properties
stage: expert
status: validated
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

## Questions

```yaml
- question: "You compute the ACF of a signal and observe that it decays slowly, remaining significantly nonzero for lags up to several seconds. What does this pattern indicate?"
  type: multiple-choice
  options:
    - "The signal is white noise, since white noise has a broad ACF spread across many lags"
    - "The signal has long-range temporal correlation — samples separated by seconds are still statistically related"
    - "The ACF computation has an error; a correct ACF always decays to zero within a few samples"
    - "The signal is periodic with a period equal to the lag at which the ACF first crosses zero"
  answer: 1
  explanation: "A slowly decaying ACF indicates long-range dependence — the signal has memory, and distant samples are still correlated. This is the signature of an AR process with poles near the unit circle. White noise has an impulsive ACF (maximum at lag zero, zero everywhere else) because its samples are uncorrelated by definition. A periodic signal would show an oscillating ACF, not a monotone decay."

- question: "For a finite data record, why is the biased ACF estimator (dividing by N regardless of lag) generally preferred over the unbiased estimator (dividing by N − |τ|)?"
  type: multiple-choice
  options:
    - "The biased estimator is mathematically unbiased at all lags, making it more accurate"
    - "The biased estimator always produces a valid positive semi-definite result, preventing nonsensical negative power spectral estimates"
    - "The unbiased estimator underestimates the ACF at all lags, making it systematically wrong"
    - "The biased estimator requires less computation because it avoids counting available pairs"
  answer: 1
  explanation: "The biased estimator (dividing by N) guarantees positive semi-definiteness — a mathematical requirement for any valid autocorrelation function. When Fourier-transformed to obtain a PSD, it always yields non-negative spectral values. The unbiased estimator (dividing by N−|τ|) corrects bias but inflates variance at large lags where few sample pairs exist, sometimes violating positive semi-definiteness and producing negative PSD values — a physically impossible result. Trading some bias for a valid estimate is the practical engineering choice."

- question: "The autocorrelation function R_x(τ) of any real, stationary signal satisfies R_x(τ) = R_x(−τ) — it is an even (symmetric) function of lag."
  type: true-false
  answer: true
  explanation: "Even symmetry follows directly from the definition: R_x(τ) = E[x(t)x(t+τ)]. Replacing τ with −τ gives R_x(−τ) = E[x(t)x(t−τ)], which by stationarity equals E[x(t+τ)x(t)] = R_x(τ). The expectation of a product doesn't depend on which sample leads. Geometrically, the ACF is symmetric about lag zero, so you only need to compute and interpret it for non-negative lags."

- question: "White noise has a flat (constant) autocorrelation function, reflecting that all lags contribute equally to its power."
  type: true-false
  answer: false
  explanation: "White noise has an impulsive ACF — R_x(0) equals average power, and R_x(τ) = 0 for all τ ≠ 0. White noise samples are uncorrelated by definition: knowing the value at one time gives no information about any other. A flat ACF would imply constant nonzero correlation at all lags. The confusion may arise from white noise's flat power spectral density — but the ACF (the Fourier transform of the PSD) of a flat spectrum is an impulse, not a flat function."

- question: "What does it mean that the ACF of a periodic signal is itself periodic, and why is this property practically useful?"
  type: short-answer
  answer: "If a signal x(t) has period T, then x(t) and x(t+T) are identical, so their product averages to R_x(0) — the ACF repeats at lags that are multiples of T. The ACF is therefore periodic with the same period T. This is useful because even when a periodic signal is buried in broadband noise, the noise's ACF decays to zero while the signal's periodic oscillation persists in the combined ACF, revealing the hidden period."
  explanation: "This turns the ACF into a periodicity detector robust to additive noise. In radar, sonar, or vibration analysis, you may need to detect a periodic component (engine rotation, target echo) in a noisy environment. Direct spectral analysis may show a peak buried in the noise floor, but the ACF will show a persistent oscillation at the signal's period while the noise contribution decays away. This is one of the key practical motivations for computing the ACF rather than working directly with the raw signal."
```

## Explainer

From your study of random signals and power spectral density, you know that a random signal cannot be described sample by sample — instead you characterize it statistically. The **autocorrelation function** R_x(τ) = E[x(t)x(t+τ)] asks a deceptively simple question: how much does a signal resemble a time-shifted copy of itself? At lag τ = 0, a signal is perfectly correlated with itself, so R_x(0) = E[x²(t)] = the signal's average power — the maximum possible value. At large lags, if the signal is stationary and ergodic, R_x(τ) → 0 because distant samples become uncorrelated. The shape of R_x(τ) between these extremes encodes the signal's temporal structure.

Three fundamental properties follow from the definition and are worth internalizing geometrically. First, **R_x(0) ≥ |R_x(τ)|** for all τ — the zero-lag value is always the global maximum. Second, the ACF is **even**: R_x(τ) = R_x(−τ), because flipping the sign of the lag just reverses which sample leads and which follows, and the product is the same. Third, the ACF of a **periodic signal** is itself periodic at the same period — a sinusoid's ACF is a cosine, not a decaying function. This makes the ACF a detector of hidden periodicity: even if a periodic signal is buried in broadband noise, the ACF will show a persistent oscillation at the signal's period while the noise contribution decays toward zero. The link to your PSD prerequisite: by the Wiener-Khinchin theorem, the power spectral density S_x(f) is exactly the Fourier transform of R_x(τ). ACF and PSD are a Fourier pair — two views of the same information.

Estimating R_x(τ) from a finite data record introduces practical complications. The **biased estimator** R̂_x(τ) = (1/N) Σ x(n)x(n+τ), summing over all available sample pairs and dividing by N (the total record length rather than the number of pairs), is biased — it underestimates the true ACF at large lags — but has lower variance and always produces a valid (positive semi-definite) spectrum when Fourier-transformed. The **unbiased estimator** divides by N−|τ| (the actual number of pairs available at each lag), which removes the bias but inflates variance at large lags, where few pairs exist, sometimes producing nonsensical negative spectral estimates. The rule of thumb: use the biased estimator in practice; restrict interpretation to lags much shorter than the record length (τ_max ≤ N/10 is common).

The **ACF of white noise** is an impulse at τ = 0 and zero everywhere else — white noise is uncorrelated sample to sample by definition. Any departure from an impulsive ACF signals structure in the data: a slowly decaying ACF suggests long-range correlation (an AR process with poles near the unit circle), while an ACF that drops to zero abruptly after M lags signals a moving-average process of order M. This diagnostic reading of ACF shape is the practical skill this topic builds — it is the foundation for model order selection in AR/MA/ARMA parametric modeling and for detecting whether a signal has been filtered, correlated, or corrupted in time-structured ways.
