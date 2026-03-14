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
