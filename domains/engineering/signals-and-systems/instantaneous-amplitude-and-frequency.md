---
id: instantaneous-amplitude-and-frequency
title: Instantaneous Amplitude and Frequency Estimation
domain: engineering
course: signals-and-systems
prerequisites:
- id: hilbert-transform-analytic-signals
  type: hard
builds-toward:
- short-time-fourier-transform
- wavelet-transform-analysis
tags:
- instantaneous-frequency
- amplitude-modulation
- analytic-signal
stage: abstract-reasoning
status: draft
---

# Instantaneous Amplitude and Frequency Estimation

## Core Idea
The analytic signal (obtained via Hilbert transform) has instantaneous amplitude and phase defined in complex form. Instantaneous frequency is the derivative of instantaneous phase with respect to time, enabling detection of frequency modulation. For narrowband signals around a carrier, instantaneous frequency estimates the frequency deviation. Applications include FM demodulation, chirp detection, and time-frequency analysis of non-stationary signals.

## How It's Best Learned
Construct analytic signal of FM-modulated sinusoid using Hilbert transform. Extract instantaneous frequency by differentiating phase; verify it matches the modulation function.

## Common Misconceptions
- Thinking instantaneous frequency is always meaningful (only for narrowband signals with well-defined "frequency").
- Confusing instantaneous frequency with spectral frequency content.
- Not recognizing that instantaneous phase is discontinuous at zero-crossings in real signals.

## Explainer

From your study of the Hilbert transform and analytic signals, you know that for any real signal x(t), its **analytic signal** is z(t) = x(t) + j·x̂(t), where x̂(t) is the Hilbert transform of x(t). The analytic signal is complex-valued and has a one-sided spectrum (energy only at positive frequencies). Writing z(t) in polar form: z(t) = A(t)·e^(jφ(t)), the two scalar functions A(t) and φ(t) reveal everything about how the signal varies in amplitude and frequency over time.

**Instantaneous amplitude** A(t) = |z(t)| = √(x²(t) + x̂²(t)) is the **envelope** of the signal — it traces the smooth curve connecting the peaks. For an amplitude-modulated (AM) signal x(t) = [1 + m·cos(2πf_m t)]·cos(2πf_c t), the instantaneous amplitude is exactly the modulating envelope 1 + m·cos(2πf_m t) (after low-pass filtering the demodulated result). Think of it as the slowly-varying "amplitude track" that rides on top of the fast carrier oscillation. This is why envelope detection is the basis of AM radio demodulation.

**Instantaneous phase** φ(t) = arctan(x̂(t)/x(t)) = ∠z(t) tracks the continuously evolving phase angle of the signal. **Instantaneous frequency** is then defined as f_i(t) = (1/2π)·dφ/dt — the rate of change of phase. For a pure sinusoid cos(2πf₀t + φ₀), the phase is linear in time so the instantaneous frequency is the constant f₀, exactly as expected. For a **chirp signal** cos(2π(f₀ + αt)t), the phase is quadratic, and the instantaneous frequency rises linearly: f_i(t) = f₀ + 2αt. This is why instantaneous frequency is so valuable for analyzing **frequency-modulated (FM) signals** and non-stationary signals whose frequency content changes over time — it gives you a time-varying frequency track, not just a static spectrum.

The critical constraint is the **narrowband assumption**: instantaneous frequency is only physically interpretable when the signal is narrowband around a single dominant frequency at each instant. For a broadband signal containing many frequency components simultaneously (like a chord of music), the analytic signal's instantaneous frequency is a weighted average that may not correspond to any actual frequency present in the signal, and can even be negative — a clear sign that the narrowband assumption is violated. When the assumption holds (as in FM communications, biomedical signals like EEG, seismic chirps, or bat echolocation pulses), instantaneous frequency extraction gives you a precise, time-resolved frequency trajectory that a Fourier spectrum — which smears time information — fundamentally cannot provide. This is the entry point to time-frequency analysis methods like the short-time Fourier transform and wavelet transform, which extend these ideas to signals that are locally narrowband but globally broadband.
