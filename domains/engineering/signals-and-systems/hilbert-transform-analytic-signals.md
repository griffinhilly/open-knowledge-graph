---
id: hilbert-transform-analytic-signals
title: Hilbert Transform and Analytic Signals
domain: engineering
course: signals-and-systems
prerequisites:
- id: fourier-transform-definition-properties
  type: hard
builds-toward:
- quadrature-modulation-iq-representation
tags:
- hilbert-transform
- analytic-signals
- envelope
- phase
stage: advanced
status: draft
---

# Hilbert Transform and Analytic Signals

## Core Idea
The Hilbert transform H[x(t)] produces output whose spectrum is the original spectrum multiplied by –j·sgn(f). The analytic signal z(t) = x(t) + j·H[x(t)] suppresses negative frequencies, enabling instantaneous amplitude and phase extraction. Phase unwrapping recovers instantaneous frequency as dφ/dt.

## Explainer

The Fourier transform you studied decomposes a real-valued signal into complex exponentials at positive and negative frequencies. For a real signal x(t), the negative-frequency components are always the complex conjugate of the positive-frequency components — they carry no additional information. The spectrum is redundant by exactly a factor of two. The Hilbert transform and the **analytic signal** construction exploit this redundancy: by suppressing the negative-frequency half of the spectrum, you pack exactly the same information into a one-sided spectrum, which enables something powerful — the clean separation of a signal's **instantaneous amplitude** from its **instantaneous phase**.

The Hilbert transform H[x(t)] is defined in the frequency domain as multiplication by −j·sgn(f): positive frequencies are multiplied by −j (a 90° phase lag) and negative frequencies by +j (a 90° phase lead). In the time domain, this corresponds to convolution with 1/(πt). The output x̂(t) = H[x(t)] is a real signal that looks like x(t) with every frequency component shifted 90° in phase — the Hilbert transform of cos(2πft) is sin(2πft), and the Hilbert transform of sin(2πft) is −cos(2πft). The **analytic signal** is then z(t) = x(t) + j·x̂(t). By construction, its Fourier transform Z(f) is zero for f < 0 — the imaginary part exactly cancels the negative-frequency components and doubles the positive-frequency ones.

This one-sided spectrum enables envelope and phase extraction without ambiguity. Writing z(t) = A(t)·e^{jφ(t)}, the instantaneous amplitude (envelope) is A(t) = |z(t)| = √[x(t)² + x̂(t)²], and the instantaneous phase is φ(t) = arctan[x̂(t)/x(t)]. For an AM radio signal x(t) = m(t)·cos(2πf_ct), where m(t) is the message, the analytic signal gives A(t) = m(t) directly — equivalent to an ideal envelope detector. For an FM signal where frequency varies with the message, the **instantaneous frequency** is the time derivative of phase: f_i(t) = (1/2π)·dφ/dt.

Phase is accumulated continuously, but the arctan function wraps at ±π. **Phase unwrapping** adds or subtracts 2π at each discontinuity to reconstruct the smooth, continuously increasing phase that differentiates cleanly to give instantaneous frequency. This combination — analytic signal formation, envelope extraction, and phase unwrapping — is the foundation of modern demodulation algorithms, vibration analysis, and medical signal processing wherever the instantaneous properties of a real signal need to be tracked over time.
