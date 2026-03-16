---
id: random-signals-autocorrelation-psd
title: Random Signals, Autocorrelation, and Power Spectral Density
domain: engineering
course: signals-and-systems
prerequisites:
- id: signal-properties-periodicity-energy-power
  type: hard
- id: parseval-theorem-energy-analysis
  type: hard
tags:
- random-signals
- noise
- stochastic
- power-spectral-density
stage: advanced
status: draft
---

# Random Signals, Autocorrelation, and Power Spectral Density

## Core Idea
Random signals (noise, stochastic processes) are characterized by their autocorrelation R(τ) = E[x(t)x(t+τ)] and power spectral density S(f) = FT{R(τ)}. White noise has flat PSD; colored noise has frequency-dependent power. These tools enable analysis of systems driven by noise and filtering of noisy signals.

## Explainer

Deterministic signals can be described exactly by a formula — you know what the signal will be at every future time. Random signals cannot. Thermal noise in a resistor, acoustic vibrations in a room, and radio interference are all unpredictable sample-by-sample, yet they have stable *statistical structure* that repeats on average. The challenge is to characterize that structure without knowing the actual waveform.

The key tool is the **autocorrelation function** R(τ) = E[x(t)x(t+τ)]. It answers: how similar is the signal to a time-shifted version of itself, on average? When the lag τ = 0, you get the signal's average power: R(0) = E[x²]. As τ increases, a signal with slow fluctuations stays correlated over long lags, while pure noise decorrelates instantly. Intuitively, R(τ) tells you the "memory" of the signal — how long it takes for the signal's current value to stop predicting its future values. From your prerequisite on signal power, you already know that power matters more than instantaneous amplitude for most engineering problems; autocorrelation formalizes this by tracking how power is distributed across time delays.

The **power spectral density** S(f) brings this into the frequency domain via the Wiener-Khinchin theorem: S(f) = FT{R(τ)}. This is the random-signal analog of the relationship you saw in Parseval's theorem — total power can be computed either in the time domain (integrating R(0)) or in the frequency domain (integrating S(f) across all frequencies). The PSD tells you *where in frequency* the signal's power lives. **White noise** is the idealized extreme: S(f) = constant across all frequencies, meaning equal power at every frequency. This implies R(τ) = δ(τ) — the signal is completely uncorrelated with itself at any nonzero lag. In practice, white noise is an approximation; real noise is bandlimited and has some residual correlation.

**Colored noise** has frequency-dependent PSD — more power at some frequencies than others. Pink noise (1/f noise) concentrates power at low frequencies; blue noise concentrates it at high frequencies. When a random signal passes through a linear system (filter), the output PSD is S_out(f) = |H(f)|² · S_in(f), where H(f) is the system's frequency response. This is the stochastic analog of the deterministic convolution you already know. It means you can design a filter to suppress noise in certain frequency bands while preserving signal, and you can predict exactly what the output noise statistics will be — even though you cannot predict the actual output waveform. This connection between frequency-domain tools and statistical characterization is what makes PSD analysis so powerful in signal processing, communications, and control systems.
