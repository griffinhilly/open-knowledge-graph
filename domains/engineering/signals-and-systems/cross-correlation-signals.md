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
stage: advanced
status: draft
---

# Cross-Correlation and Time Delay Estimation

## Core Idea
Cross-correlation Rxy(τ) = ∫ x(t)·y(t+τ) dt measures similarity between two signals as a function of delay τ. The peak indicates the time lag that best aligns the signals, enabling time-delay estimation for target location and synchronization. Normalized cross-correlation removes amplitude effects. In noise, matched filtering and phase-based methods improve robustness.

## Explainer

From your study of autocorrelation and power spectral density, you know that the autocorrelation function Rxx(τ) = ∫ x(t)·x(t+τ) dt measures how similar a signal is to a shifted version of itself. It peaks at τ = 0 because a signal always matches itself perfectly with zero lag, and it decays as the shift grows. **Cross-correlation** extends this idea to *two different signals*: instead of comparing x to itself, you compare x to y, sliding one past the other and measuring their overlap at each lag. The result is a function of delay that tells you how similar the signals are as a function of time offset.

The value of cross-correlation becomes clear through a concrete example. Suppose a sonar system emits a sound pulse x(t) and receives an echo y(t) = x(t − τ₀) + noise, where τ₀ is the round-trip travel time to a target. The received signal looks like a delayed, noisy version of the transmitted signal. Computing Rxy(τ) = ∫ x(t)·y(t+τ) dt and finding where it peaks gives you the value of τ that best aligns x with y — which is precisely τ₀, the delay. Multiplying the delay by the wave speed gives target range. This is the operating principle of radar, sonar, ultrasonic flow meters, and GPS: they all estimate time delays by cross-correlating a reference signal with a received version of it.

The **normalized cross-correlation** divides by the product of the signal energies: ρxy(τ) = Rxy(τ) / √(Rxx(0) · Ryy(0)). This bounds the result between −1 and +1, removing dependence on signal amplitude. A peak near +1 at some lag means the two signals are nearly identical up to that time shift; near −1 means they are inverted copies; near 0 means they are uncorrelated. The normalized form is especially useful in pattern matching — finding a known template within a longer signal — because it responds only to the *shape* similarity, not the amplitude.

In practice, cross-correlation is computed efficiently via the Fourier transform: the cross-spectral density Sxy(f) = X*(f) · Y(f) is the Fourier transform of Rxy(τ), so computing Rxy requires only a forward FFT, a complex multiplication, and an inverse FFT. When noise is present, the **generalized cross-correlation** method applies weighting in the frequency domain to emphasize frequencies with high signal-to-noise ratio before inverse-transforming to find the delay peak. This connects cross-correlation to the broader framework of spectral estimation and coherence that you will encounter in subsequent topics — coherence between two signals is essentially the normalized cross-power spectrum, revealing at which frequencies two signals are linearly related.
