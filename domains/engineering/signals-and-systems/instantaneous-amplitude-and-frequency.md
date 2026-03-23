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
stage: expert
status: validated
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

## Questions

```yaml
- question: "A researcher computes the analytic signal of a broadband audio recording containing simultaneous bass, midrange, and treble tones, then plots the instantaneous frequency over time. She observes the curve occasionally dropping to negative values. The most likely explanation is:"
  type: multiple-choice
  options:
    - "The signal contains frequencies below DC, producing aliasing in the Hilbert transform"
    - "The narrowband assumption is violated; instantaneous frequency of a multi-component signal becomes a meaningless weighted average"
    - "There is a phase discontinuity caused by a digital clipping artifact in the recording"
    - "The Hilbert transform has been applied to a non-periodic signal, violating a required assumption"
  answer: 1
  explanation: "Negative instantaneous frequency is the clearest sign that the narrowband assumption is violated. For a broadband signal with many simultaneous frequency components, the phase of the analytic signal reflects the interference of all components; its derivative is a weighted average that can easily fall below zero. Instantaneous frequency only has physical meaning when the signal is locally narrowband — dominated by a single frequency at each moment. For broadband audio, Fourier analysis or STFT methods are the appropriate tools."

- question: "For a chirp signal x(t) = cos(2π(f₀ + αt)t), the instantaneous frequency computed from the analytic signal is:"
  type: multiple-choice
  options:
    - "The constant f₀, which is the dominant carrier around which the frequency sweeps"
    - "A linearly increasing function f_i(t) = f₀ + 2αt, tracking the sweep in real time"
    - "The bandwidth of the chirp, which grows as the frequency sweep progresses"
    - "The time-averaged value of f₀ + αt over the signal duration"
  answer: 1
  explanation: "The instantaneous phase is φ(t) = 2π(f₀t + αt²), which is quadratic in time. Instantaneous frequency is f_i(t) = (1/2π)·dφ/dt = f₀ + 2αt — a linearly increasing function that precisely tracks the frequency at each moment. This is the key advantage over Fourier analysis: the Fourier spectrum of a chirp is smeared across a band of frequencies, while instantaneous frequency gives a clean, time-resolved frequency trajectory. For FM communications, radar, and sonar, this time-varying frequency track carries the actual information."

- question: "Instantaneous frequency and spectral (Fourier) frequency describe the same property of a signal at different time resolutions."
  type: true-false
  answer: false
  explanation: "They are fundamentally different quantities. Spectral frequency describes the distribution of energy across frequencies over a time window (or the entire signal). Instantaneous frequency is the derivative of instantaneous phase at a single moment in time — it is a time-domain quantity, not a frequency-domain one. For a stationary sinusoid they agree numerically, but for non-stationary signals they can be completely different. Instantaneous frequency gives a time-varying 'frequency track'; the Fourier spectrum gives a static aggregate. They are not just different resolutions of the same thing."

- question: "The instantaneous amplitude of a real signal x(t) equals the square root of the sum of x²(t) and the square of its Hilbert transform."
  type: true-false
  answer: true
  explanation: "By definition, the analytic signal is z(t) = x(t) + j·x̂(t), where x̂(t) is the Hilbert transform of x(t). Written in polar form z(t) = A(t)·e^(jφ(t)), the instantaneous amplitude is A(t) = |z(t)| = √(x²(t) + x̂²(t)). This envelope is always non-negative and traces the smooth curve that connects the signal's peaks — it captures the slow-varying amplitude modulation riding on top of the fast carrier oscillation, which is why it underlies AM radio demodulation."

- question: "Why is instantaneous frequency only physically meaningful for narrowband signals, and what goes wrong when it is applied to a broadband signal?"
  type: short-answer
  answer: "Instantaneous frequency is defined as f_i(t) = (1/2π)·dφ/dt, the rate of change of the analytic signal's phase. For a narrowband signal dominated by a single frequency at each moment, this derivative cleanly tracks that frequency over time. For a broadband signal with multiple simultaneous frequency components, the analytic signal's phase reflects the superposition of all components; its derivative yields a weighted average of the component frequencies. This average can take values outside the actual range of frequencies present — including negative values — producing a result with no physical interpretation."
  explanation: "The narrowband assumption is the critical prerequisite for meaningful instantaneous frequency. When it holds (FM signals, EEG oscillations, bat chirps), the instantaneous frequency gives a precise, time-resolved frequency trajectory that Fourier analysis cannot provide. When it is violated, the concept breaks down entirely. Recognizing this boundary — and choosing appropriate time-frequency tools (STFT, wavelets) when signals are locally but not globally narrowband — is the practical takeaway."
```

## Explainer

From your study of the Hilbert transform and analytic signals, you know that for any real signal x(t), its **analytic signal** is z(t) = x(t) + j·x̂(t), where x̂(t) is the Hilbert transform of x(t). The analytic signal is complex-valued and has a one-sided spectrum (energy only at positive frequencies). Writing z(t) in polar form: z(t) = A(t)·e^(jφ(t)), the two scalar functions A(t) and φ(t) reveal everything about how the signal varies in amplitude and frequency over time.

**Instantaneous amplitude** A(t) = |z(t)| = √(x²(t) + x̂²(t)) is the **envelope** of the signal — it traces the smooth curve connecting the peaks. For an amplitude-modulated (AM) signal x(t) = [1 + m·cos(2πf_m t)]·cos(2πf_c t), the instantaneous amplitude is exactly the modulating envelope 1 + m·cos(2πf_m t) (after low-pass filtering the demodulated result). Think of it as the slowly-varying "amplitude track" that rides on top of the fast carrier oscillation. This is why envelope detection is the basis of AM radio demodulation.

**Instantaneous phase** φ(t) = arctan(x̂(t)/x(t)) = ∠z(t) tracks the continuously evolving phase angle of the signal. **Instantaneous frequency** is then defined as f_i(t) = (1/2π)·dφ/dt — the rate of change of phase. For a pure sinusoid cos(2πf₀t + φ₀), the phase is linear in time so the instantaneous frequency is the constant f₀, exactly as expected. For a **chirp signal** cos(2π(f₀ + αt)t), the phase is quadratic, and the instantaneous frequency rises linearly: f_i(t) = f₀ + 2αt. This is why instantaneous frequency is so valuable for analyzing **frequency-modulated (FM) signals** and non-stationary signals whose frequency content changes over time — it gives you a time-varying frequency track, not just a static spectrum.

The critical constraint is the **narrowband assumption**: instantaneous frequency is only physically interpretable when the signal is narrowband around a single dominant frequency at each instant. For a broadband signal containing many frequency components simultaneously (like a chord of music), the analytic signal's instantaneous frequency is a weighted average that may not correspond to any actual frequency present in the signal, and can even be negative — a clear sign that the narrowband assumption is violated. When the assumption holds (as in FM communications, biomedical signals like EEG, seismic chirps, or bat echolocation pulses), instantaneous frequency extraction gives you a precise, time-resolved frequency trajectory that a Fourier spectrum — which smears time information — fundamentally cannot provide. This is the entry point to time-frequency analysis methods like the short-time Fourier transform and wavelet transform, which extend these ideas to signals that are locally narrowband but globally broadband.
