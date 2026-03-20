---
id: gaussian-and-colored-noise-characterization
title: Gaussian and Colored Noise Characterization
domain: engineering
course: signals-and-systems
prerequisites:
- id: random-signals-autocorrelation-psd
  type: hard
builds-toward:
- signal-detection-and-hypothesis-testing
- quantization-error-and-noise-analysis
tags:
- noise
- gaussian
- colored-noise
- characterization
stage: advanced
status: draft
---

# Gaussian and Colored Noise Characterization

## Core Idea
White noise has flat power spectral density and zero autocorrelation except at lag zero; colored (shaped) noise has frequency-dependent spectral content determined by its autocorrelation function. Gaussian noise has Gaussian amplitude distribution and is fully characterized by mean and variance. Non-Gaussian noise (e.g., uniform, laplacian) has different amplitude statistics. Understanding noise type is essential for signal detection, estimation, and filter design.

## How It's Best Learned
Generate white and colored noise (filter white noise with lowpass). Compare their autocorrelation functions and power spectral densities. Fit parametric models (AR) to colored noise.

## Common Misconceptions
- Thinking white noise means quiet (it means flat spectrum).
- Confusing Gaussian amplitude distribution with white spectrum.
- Assuming all practical noise is white or Gaussian.

## Explainer

From your prerequisite on random signals, autocorrelation, and PSD, you know that a random signal is characterized not by its specific sample values but by its statistical properties. Two of the most important properties are completely independent and are often incorrectly conflated: the **spectral shape** (how power is distributed across frequency) and the **amplitude distribution** (what values the signal takes). Understanding each separately is essential for choosing detection algorithms, designing matched filters, and validating measurement systems.

**Spectral character** is described by the power spectral density. A signal is called **white noise** when its PSD is flat across all frequencies — equal power per unit bandwidth at every frequency. The name is an analogy to white light, which contains all colors equally. White noise has zero autocorrelation for any nonzero lag (samples at different times are uncorrelated), and its autocorrelation function is a scaled impulse: R(τ) = σ²δ(τ). In practice, truly white noise cannot exist — it would require infinite total power — but bandlimited white noise (flat PSD over a finite bandwidth) is a useful approximation for thermal noise, quantization noise, and ADC dither. **Colored noise** has a frequency-dependent PSD; it is white noise that has been shaped by passing through a filter. Pink noise has PSD ∝ 1/f (equal power per octave), appearing in biological systems and electronic components. Brown (or red) noise has PSD ∝ 1/f², characteristic of random walks and integrated white noise. Blue noise emphasizes high frequencies. The color metaphor is informal but widely used in engineering and physics.

**Amplitude distribution** is an entirely separate property. **Gaussian noise** has amplitude values drawn from a normal distribution, fully characterized by its mean (usually zero) and variance σ². The Gaussian distribution is the central limit theorem in action: many independent random sources summed together produce Gaussian statistics, regardless of each source's individual distribution. This is why thermal noise (arising from the random motion of many electrons) is Gaussian in amplitude. But spectral character and amplitude distribution are independent: you can have Gaussian white noise (flat PSD, Gaussian amplitudes), Gaussian pink noise (1/f PSD, Gaussian amplitudes), or non-Gaussian white noise (flat PSD, non-Gaussian amplitudes). **Non-Gaussian noise** arises in many practical contexts: shot noise has a Poisson distribution at low counts; impulsive noise from electrical switching has heavy-tailed (Laplacian or alpha-stable) distributions; clipping produces truncated distributions.

The practical consequences are significant. Gaussian white noise is mathematically the most tractable: optimal linear filters (Wiener filter, Kalman filter) are derived assuming Gaussian white or colored noise, and in this case the optimal detector is the matched filter. When noise is non-Gaussian, linear filtering may no longer be optimal, and robust or nonlinear estimators may dramatically outperform. Similarly, characterizing noise as colored when it is actually white (or vice versa) misspecifies the noise model and degrades filter performance. The standard workflow for characterizing unknown noise is: (1) measure or simulate a long noise record, (2) estimate its PSD (via the Welch method) to determine spectral character, (3) fit a parametric spectral model (AR or ARMA) if needed, and (4) test the amplitude distribution against Gaussian using Q-Q plots or the Kolmogorov-Smirnov test. Both characterizations together give you everything you need to design an optimal signal processing system.
