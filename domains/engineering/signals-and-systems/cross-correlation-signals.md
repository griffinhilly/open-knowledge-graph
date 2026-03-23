---
id: cross-correlation-signals
title: Cross-Correlation and Time Delay Estimation
domain: engineering
course: signals-and-systems
prerequisites:
- id: random-signals-autocorrelation-psd
  type: hard
builds-toward:
- coherence-and-spectral-density
tags:
- cross-correlation
- time-delay
- similarity
- signals
stage: expert
status: draft
---

# Cross-Correlation and Time Delay Estimation

## Core Idea
Cross-correlation Rxy(τ) = ∫ x(t)·y(t+τ) dt measures similarity between two signals as a function of delay τ. The peak indicates the time lag that best aligns the signals, enabling time-delay estimation for target location and synchronization. Normalized cross-correlation removes amplitude effects. In noise, matched filtering and phase-based methods improve robustness.

## Questions

```yaml
- question: "A radar system transmits pulse x(t) and receives y(t) = x(t − τ₀) + noise, where τ₀ is the unknown round-trip travel time to a target. The cross-correlation Rxy(τ) is computed. How is target range estimated from this result?"
  type: multiple-choice
  options:
    - "By measuring the amplitude of Rxy(τ) at τ = 0, which represents the signal energy remaining after transmission loss over distance."
    - "By finding the lag τ where Rxy(τ) is maximized — this equals the round-trip delay τ₀, and multiplying by wave propagation speed gives range."
    - "By subtracting the noise floor from Rxy(τ) and dividing by the signal bandwidth to extract timing information."
    - "By integrating Rxy(τ) over all lags, since the integral equals the total signal power, which decays with distance."
  answer: 1
  explanation: "Cross-correlation measures similarity between x and a time-shifted version of y. When y is a delayed copy of x (plus noise), Rxy(τ) peaks at the lag τ = τ₀ that best aligns x with the delayed signal — exactly the round-trip delay. The amplitude at τ = 0 gives only autocorrelation of x with the unshifted y, which is irrelevant to delay estimation. Range = (τ₀/2) × wave_speed (dividing by 2 because the delay is round-trip). This is the operating principle of all delay-and-estimate systems: radar, sonar, GPS pseudorange, and ultrasonic flow meters."

- question: "Signal x(t) has amplitude 1 and signal y(t) is identical in shape to x(t) but has amplitude 10 and a 5-second time lag. You compute both the raw cross-correlation Rxy(τ) and the normalized cross-correlation ρxy(τ). Which statement correctly describes what normalization reveals that the raw cross-correlation does not?"
  type: multiple-choice
  options:
    - "Normalization reveals the time lag more precisely by suppressing noise at lags far from the peak."
    - "Normalization confirms that the shape similarity is essentially perfect (ρ ≈ +1 at τ = 5 s) regardless of the amplitude difference — isolating shape similarity from amplitude effects."
    - "Normalization reveals the frequency content of the delay, showing which spectral components are responsible for the lag."
    - "The two are equivalent; normalization only rescales the vertical axis without changing any interpretation."
  answer: 1
  explanation: "The raw Rxy(τ) peak height depends on both signal amplitudes and shape similarity — a high peak could mean either 'very similar shapes' or 'very large amplitudes' or both. Normalization by √(Rxx(0)·Ryy(0)) scales the result to [−1, +1], removing amplitude dependence entirely. A peak of ρ ≈ +1 means the signals are essentially identical in shape up to the given delay, regardless of how large or small either signal is. This is critical for pattern matching: finding a known template in a noisy signal requires responding to shape, not amplitude. Option D is wrong because normalization changes the interpretation of the peak height, even though it does not change the peak location."

- question: "The cross-correlation Rxy(τ) always peaks at τ = 0, just as the autocorrelation Rxx(τ) does."
  type: true-false
  answer: false
  explanation: "The autocorrelation Rxx(τ) peaks at τ = 0 because a signal is always most similar to an unshifted version of itself — any shift reduces overlap. Cross-correlation Rxy(τ) peaks at the lag τ₀ that best aligns signal x with signal y. If y is a delayed version of x (e.g., an echo), the peak is at τ = τ₀, not zero. If x and y have no time delay relationship and are uncorrelated, there may be no sharp peak at all. The cross-correlation peak location is information — it reveals the relative time alignment between two signals, which is exactly what makes it useful for delay estimation."

- question: "Computing cross-correlation efficiently using the FFT requires only a forward transform of each signal, a pointwise complex multiplication of their spectra, and an inverse transform to obtain the correlation in the time domain."
  type: true-false
  answer: true
  explanation: "The cross-correlation theorem states that Rxy(τ) ↔ X*(f)·Y(f), where X*(f) is the complex conjugate of X(f). This means the Fourier transform of the cross-correlation equals the cross-spectrum. So to compute Rxy: (1) FFT x to get X(f), (2) FFT y to get Y(f), (3) multiply X*(f)·Y(f) pointwise, (4) inverse FFT the result. This is O(N log N) rather than O(N²) for direct computation of the correlation integral — a crucial practical speedup for long signals. This same FFT-based approach underlies matched filtering and generalized cross-correlation with frequency-domain weighting."

- question: "Explain in your own words what the normalized cross-correlation ρxy(τ) reveals, and why normalization matters when comparing signals of very different amplitudes."
  type: short-answer
  answer: "The normalized cross-correlation ρxy(τ) = Rxy(τ) / √(Rxx(0)·Ryy(0)) measures the degree of linear similarity between x and y at each time lag, bounded between −1 and +1. A value of +1 at some lag means the signals are essentially identical in shape (one is a scaled version of the other at that delay); −1 means they are inverted copies; 0 means they are uncorrelated. Normalization removes amplitude dependence: a loud signal and a quiet one with identical shape will give ρ ≈ +1 at the correct lag, just as two signals of equal amplitude would. Without normalization, the raw peak height conflates shape similarity with signal energy — you cannot tell whether a large Rxy value means 'similar shapes' or 'large amplitudes' or both. Normalization isolates the shape and delay information, which is what detection and estimation tasks actually need."
  explanation: "Think of normalization as measuring 'how much of signal y can be explained by a shifted, scaled copy of signal x.' A value of +1 says 'perfectly, up to a scalar.' The division by signal energies is the same operation as computing a correlation coefficient in statistics — it standardizes the result to be interpretable as a measure of dependence rather than magnitude."
```

## Explainer

From your study of autocorrelation and power spectral density, you know that the autocorrelation function Rxx(τ) = ∫ x(t)·x(t+τ) dt measures how similar a signal is to a shifted version of itself. It peaks at τ = 0 because a signal always matches itself perfectly with zero lag, and it decays as the shift grows. **Cross-correlation** extends this idea to *two different signals*: instead of comparing x to itself, you compare x to y, sliding one past the other and measuring their overlap at each lag. The result is a function of delay that tells you how similar the signals are as a function of time offset.

The value of cross-correlation becomes clear through a concrete example. Suppose a sonar system emits a sound pulse x(t) and receives an echo y(t) = x(t − τ₀) + noise, where τ₀ is the round-trip travel time to a target. The received signal looks like a delayed, noisy version of the transmitted signal. Computing Rxy(τ) = ∫ x(t)·y(t+τ) dt and finding where it peaks gives you the value of τ that best aligns x with y — which is precisely τ₀, the delay. Multiplying the delay by the wave speed gives target range. This is the operating principle of radar, sonar, ultrasonic flow meters, and GPS: they all estimate time delays by cross-correlating a reference signal with a received version of it.

The **normalized cross-correlation** divides by the product of the signal energies: ρxy(τ) = Rxy(τ) / √(Rxx(0) · Ryy(0)). This bounds the result between −1 and +1, removing dependence on signal amplitude. A peak near +1 at some lag means the two signals are nearly identical up to that time shift; near −1 means they are inverted copies; near 0 means they are uncorrelated. The normalized form is especially useful in pattern matching — finding a known template within a longer signal — because it responds only to the *shape* similarity, not the amplitude.

In practice, cross-correlation is computed efficiently via the Fourier transform: the cross-spectral density Sxy(f) = X*(f) · Y(f) is the Fourier transform of Rxy(τ), so computing Rxy requires only a forward FFT, a complex multiplication, and an inverse FFT. When noise is present, the **generalized cross-correlation** method applies weighting in the frequency domain to emphasize frequencies with high signal-to-noise ratio before inverse-transforming to find the delay peak. This connects cross-correlation to the broader framework of spectral estimation and coherence that you will encounter in subsequent topics — coherence between two signals is essentially the normalized cross-power spectrum, revealing at which frequencies two signals are linearly related.
