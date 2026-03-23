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
stage: expert
status: draft
---

# Hilbert Transform and Analytic Signals

## Core Idea
The Hilbert transform H[x(t)] produces output whose spectrum is the original spectrum multiplied by –j·sgn(f). The analytic signal z(t) = x(t) + j·H[x(t)] suppresses negative frequencies, enabling instantaneous amplitude and phase extraction. Phase unwrapping recovers instantaneous frequency as dφ/dt.

## Questions

```yaml
- question: "The Hilbert transform is applied to x(t) = cos(2πft). What is the result?"
  type: multiple-choice
  options:
    - "cos(2πft + π/4) — the signal is shifted 45° in phase"
    - "sin(2πft) — the signal is shifted 90° in phase"
    - "−cos(2πft) — the signal is phase-inverted (180° shift)"
    - "cos(2πft + π) — the signal is shifted 180° in phase"
  answer: 1
  explanation: "The Hilbert transform applies a 90° phase lag to all positive frequencies (multiplication by −j in the frequency domain). Since cos(2πft) has a positive-frequency component at +f and a negative-frequency component at −f, applying −j to the positive and +j to the negative gives exactly sin(2πft). This is the defining property: H[cos(2πft)] = sin(2πft) and H[sin(2πft)] = −cos(2πft). The Hilbert transform is a wideband 90° phase shifter."

- question: "An engineer wants to extract the envelope m(t) from an AM radar pulse x(t) = m(t)·cos(2πfct). Which operation correctly recovers m(t)?"
  type: multiple-choice
  options:
    - "Take the absolute value of x(t) directly"
    - "Form the analytic signal z(t) = x(t) + j·H[x(t)] and compute |z(t)| = √(x² + H[x]²)"
    - "Apply a bandpass filter centered at fc and take the real part"
    - "Differentiate x(t) with respect to time"
  answer: 1
  explanation: "For x(t) = m(t)·cos(2πfct), the analytic signal is z(t) ≈ m(t)·e^{j2πfct} (when m(t) is bandlimited below fc). Taking the magnitude: |z(t)| = m(t). This is an ideal envelope detector. Option A gives |m(t)·cos(2πfct)|, which retains fast oscillations at 2fc — it does not cleanly separate envelope from carrier. Option C preserves the carrier. Option D gives instantaneous frequency, not envelope."

- question: "The analytic signal z(t) = x(t) + j·H[x(t)] contains twice as much information as the original real signal x(t) because it has both real and imaginary parts."
  type: true-false
  answer: false
  explanation: "The analytic signal contains the same information as x(t). For a real signal, negative-frequency components are always the complex conjugate of positive-frequency components — they carry no additional information. The analytic signal suppresses these redundant negative frequencies. The imaginary part H[x(t)] is fully determined by x(t): knowing x(t) is sufficient to compute x̂(t) via convolution with 1/(πt). No new information is added; the representation is mathematically reorganized to make instantaneous amplitude and phase accessible."

- question: "For an FM signal, the instantaneous frequency can be recovered from the analytic signal by differentiating the instantaneous phase."
  type: true-false
  answer: true
  explanation: "Writing z(t) = A(t)·e^{jφ(t)}, the instantaneous phase is φ(t) = arctan[H[x(t)]/x(t)], and the instantaneous frequency is fi(t) = (1/2π)·dφ/dt. For an FM signal, the message is encoded in frequency variations, so dφ/dt directly recovers the modulating signal. Phase unwrapping — adding or subtracting 2π at ±π discontinuities — is needed to make φ(t) a smooth, continuously increasing function before differentiation."

- question: "Why do negative frequencies in the spectrum of a real-valued signal carry no independent information, and how does the analytic signal exploit this property?"
  type: short-answer
  answer: "For any real-valued signal x(t), the Fourier transform satisfies conjugate symmetry: X(−f) = X*(f). The negative-frequency component is always the complex conjugate of the positive-frequency component, so it is completely determined by positive frequencies and adds no new information. The analytic signal exploits this by zeroing out all negative-frequency components and doubling the positive-frequency ones, producing a one-sided spectrum Z(f) = 2X(f) for f > 0. This creates a unique polar representation z(t) = A(t)e^{jφ(t)} with unambiguous instantaneous amplitude A(t) = |z(t)| and phase φ(t) = arg(z(t)), which would be ill-defined if negative frequencies were retained."
  explanation: "If negative frequencies were kept, the representation A(t)e^{jφ(t)} would not be unique — different combinations of A and φ could produce the same signal. Removing the redundant half creates the mathematical structure needed for clean instantaneous parameter extraction."
```

## Explainer

The Fourier transform you studied decomposes a real-valued signal into complex exponentials at positive and negative frequencies. For a real signal x(t), the negative-frequency components are always the complex conjugate of the positive-frequency components — they carry no additional information. The spectrum is redundant by exactly a factor of two. The Hilbert transform and the **analytic signal** construction exploit this redundancy: by suppressing the negative-frequency half of the spectrum, you pack exactly the same information into a one-sided spectrum, which enables something powerful — the clean separation of a signal's **instantaneous amplitude** from its **instantaneous phase**.

The Hilbert transform H[x(t)] is defined in the frequency domain as multiplication by −j·sgn(f): positive frequencies are multiplied by −j (a 90° phase lag) and negative frequencies by +j (a 90° phase lead). In the time domain, this corresponds to convolution with 1/(πt). The output x̂(t) = H[x(t)] is a real signal that looks like x(t) with every frequency component shifted 90° in phase — the Hilbert transform of cos(2πft) is sin(2πft), and the Hilbert transform of sin(2πft) is −cos(2πft). The **analytic signal** is then z(t) = x(t) + j·x̂(t). By construction, its Fourier transform Z(f) is zero for f < 0 — the imaginary part exactly cancels the negative-frequency components and doubles the positive-frequency ones.

This one-sided spectrum enables envelope and phase extraction without ambiguity. Writing z(t) = A(t)·e^{jφ(t)}, the instantaneous amplitude (envelope) is A(t) = |z(t)| = √[x(t)² + x̂(t)²], and the instantaneous phase is φ(t) = arctan[x̂(t)/x(t)]. For an AM radio signal x(t) = m(t)·cos(2πf_ct), where m(t) is the message, the analytic signal gives A(t) = m(t) directly — equivalent to an ideal envelope detector. For an FM signal where frequency varies with the message, the **instantaneous frequency** is the time derivative of phase: f_i(t) = (1/2π)·dφ/dt.

Phase is accumulated continuously, but the arctan function wraps at ±π. **Phase unwrapping** adds or subtracts 2π at each discontinuity to reconstruct the smooth, continuously increasing phase that differentiates cleanly to give instantaneous frequency. This combination — analytic signal formation, envelope extraction, and phase unwrapping — is the foundation of modern demodulation algorithms, vibration analysis, and medical signal processing wherever the instantaneous properties of a real signal need to be tracked over time.
