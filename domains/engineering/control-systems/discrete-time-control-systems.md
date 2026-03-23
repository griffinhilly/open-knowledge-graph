---
id: discrete-time-control-systems
title: Discrete-Time Control Systems
domain: engineering
course: control-systems
prerequisites:
- id: digital-control-intro
  type: hard
- id: laplace-transform-control
  type: soft
tags:
- z-transform
- zero-order-hold
- pulse-transfer-function
- z-domain-stability
- discretization
- sampling-theorem
stage: expert
status: draft
---

# Discrete-Time Control Systems

## Core Idea
Discrete-time control systems operate on sampled signals x[k] = x(kT) and are analyzed using the z-transform, where the transfer function H(z) = Y(z)/U(z) describes the input-output relationship in the z-domain. The zero-order hold (ZOH) models the digital-to-analog conversion that holds each computed control value constant between samples, and the ZOH-equivalent pulse transfer function G(z) = (1 − z⁻¹)·Z{G(s)/s} captures both the continuous plant dynamics and the hold effect. Stability in the z-domain requires all closed-loop poles to lie strictly inside the unit circle |z| = 1, analogous to the left half-plane requirement in the s-domain. The mapping z = e^{sT} relates s-plane and z-plane pole locations: the imaginary axis in the s-plane maps to the unit circle, the left half-plane maps to the interior of the unit circle, and the negative real s-axis maps to the interval (0, 1) on the real z-axis. Jury's stability criterion or the bilinear transformation w = (z − 1)/(z + 1) followed by Routh-Hurwitz can assess z-domain stability without computing roots explicitly. Discrete-time root locus and Bode plot techniques mirror their continuous-time counterparts but use the unit circle and the z = e^{jωT} frequency mapping respectively, with the critical frequency being the Nyquist frequency ω_s/2 = π/T.

## How It's Best Learned
Discretize a well-understood continuous-time system (e.g., a second-order plant with known pole locations) using the ZOH method at several sampling rates. Plot the z-plane pole locations alongside the original s-plane poles and verify the z = e^{sT} mapping. Design a discrete PID controller directly in the z-domain using root locus on the pulse transfer function, then simulate the closed-loop step response and compare with the continuous-time design to observe intersample ripple and latency effects.

## Common Misconceptions
- The z-transform is not simply the Laplace transform with z substituted for s — the z-transform is defined for sequences x[k], not continuous signals, and the relationship z = e^{sT} means the z-plane wraps the s-plane vertically with period jω_s, causing aliasing of high-frequency dynamics.
- A continuous-time system with poles on the negative real axis does not map to z-plane poles on the negative real z-axis — it maps to the positive real interval (0, 1), while negative real z-axis poles correspond to oscillatory s-plane modes at half the sampling frequency.
- Increasing the sampling rate does not always improve discrete-time controller performance — excessively fast sampling can amplify quantization noise, increase computational load, and approach the numerical precision limits of the controller hardware without meaningful performance benefit beyond a certain point.

## Questions

```yaml
- question: "A continuous-time plant has a stable pole at s = −5. A designer samples this system with period T = 0.1 s and claims the corresponding z-domain pole must be at z = −0.5 on the negative real axis. Is this correct?"
  type: multiple-choice
  options:
    - "Yes, because negative real s-plane poles map directly to the negative real z-axis"
    - "No, the pole maps to z = e^{−5 × 0.1} = e^{−0.5} ≈ 0.607, which lies on the positive real axis inside the unit circle"
    - "No, the pole maps to the unit circle at z = e^{j5} because negative s-values correspond to oscillatory modes"
    - "Yes, because the bilinear transform maps negative real s-values to negative real z-values"
  answer: 1
  explanation: "The mapping between the s-plane and z-plane is z = e^{sT}. For s = −5 and T = 0.1, z = e^{−0.5} ≈ 0.607 — a positive real number well inside the unit circle, confirming stability. Negative real s-axis poles always map to positive real z values in (0, 1) because the exponent e^{negative real} is real and positive. Negative real z-axis poles (z ∈ (−1, 0)) correspond to s-plane poles near ±jπ/T — oscillatory modes near the Nyquist frequency, not stable real poles. The common misconception of 'negative maps to negative' ignores the exponential relationship."

- question: "Why is the zero-order hold (ZOH) included when computing the discrete-time equivalent of a continuous-time plant?"
  type: multiple-choice
  options:
    - "To add differentiation that compensates for the derivative-like effect of the analog-to-digital converter"
    - "To model the digital-to-analog conversion that holds each computed control value constant until the next sample instant"
    - "To cancel Nyquist-frequency aliasing introduced by the sampler at the system input"
    - "To convert the z-domain transfer function back into an equivalent continuous-time transfer function for analysis"
  answer: 1
  explanation: "After the digital controller computes a control value at sample k, a digital-to-analog converter must produce a physical voltage or current that actuates the plant. The ZOH holds this value constant until the next sample at k+1. This holding behavior introduces dynamics: the ZOH adds a lag of T/2 to the effective plant and affects the frequency response. The ZOH-equivalent pulse transfer function G(z) = (1 − z^{−1})·Z{G(s)/s} captures both the continuous plant dynamics and the holding effect in a single discrete-time model."

- question: "A discrete-time closed-loop system with all poles strictly inside the unit circle (|z| < 1) is guaranteed to be stable."
  type: true-false
  answer: true
  explanation: "Stability in the z-domain is directly analogous to the left half-plane criterion in the s-domain. The mapping z = e^{sT} transforms the imaginary axis (σ = 0) to the unit circle and the stable left half-plane (σ < 0) to the interior of the unit circle. Any pole with |z| < 1 corresponds to a mode that decays geometrically — z^k → 0 as k → ∞. A pole at |z| > 1 corresponds to exponential growth and instability. The unit circle is the exact boundary between stable and unstable discrete-time behavior."

- question: "Sampling a continuous-time control system at a higher rate always improves closed-loop controller performance."
  type: true-false
  answer: false
  explanation: "This is a common misconception. While too slow a sampling rate causes aliasing, intersample errors, and degraded phase margin (the ZOH lag T/2 worsens with large T), excessively fast sampling introduces its own problems: quantization noise is amplified because the control effort changes very little between samples yet the quantization error remains the same; computational latency becomes a larger fraction of the sampling period; and fixed-point arithmetic precision limits become relevant. Beyond roughly 10–20× the closed-loop bandwidth, further rate increases typically provide no meaningful performance improvement and may degrade it."

- question: "Explain why the z-transform is not simply the Laplace transform with z substituted for s, and what relationship actually connects the two domains."
  type: short-answer
  answer: "The Laplace transform is defined on continuous-time signals x(t); the z-transform is defined on discrete sequences x[k]. They are mathematically separate tools. The connection is the mapping z = e^{sT}: when you sample a continuous signal every T seconds and take the z-transform of the resulting sequence, the result relates to the Laplace transform of the original signal through this exponential. The mapping wraps the s-plane's vertical structure periodically onto the z-plane — the imaginary axis maps to the unit circle, the left half-plane maps to the interior of the unit circle. Simply substituting z for s gives wrong pole locations and invalidates stability analysis."
  explanation: "Understanding z = e^{sT} as the fundamental relationship prevents numerous errors: why negative real s-poles map to positive real z values, why the stability boundary changes from an axis to a circle, why frequency aliasing occurs (the mapping from Ω to ω is not one-to-one), and why the bilinear transform w = (z−1)/(z+1) is a valid approximation to e^{sT}−1 for small sT. All discrete-time analysis follows from this single exponential relationship."
```

## Explainer

You know from continuous-time control that a system's behavior in the s-domain is characterized by its transfer function G(s) = Y(s)/U(s), and that stability requires all closed-loop poles to lie in the left half of the s-plane (LHP). When a digital computer implements a controller, it reads sensor data at discrete moments — every T seconds — computes a control output, and holds that output constant until the next sample. This **sampling and holding** process fundamentally changes the mathematical framework: continuous signals become sequences x[k] = x(kT), and the Laplace transform gives way to the **z-transform**.

The z-transform is defined on discrete sequences: X(z) = Σ x[k] z^{-k}. The complex variable z is related to s by z = e^{sT}, which is the key mapping between the two domains. Every vertical line Re(s) = σ in the s-plane maps to a circle of radius e^{σT} in the z-plane. The imaginary axis (σ = 0) maps to the **unit circle** |z| = 1. The left half-plane (σ < 0, stable continuous-time poles) maps to the **interior** of the unit circle. The LHP stability criterion becomes: all closed-loop z-domain poles must lie strictly inside the unit circle. A pole at z = 0.8 corresponds to stable, decaying behavior; a pole at |z| = 1.1 corresponds to instability.

To obtain the discrete-time model of a continuous plant plus zero-order hold, you use the **ZOH-equivalent pulse transfer function**: G(z) = (1 − z^{-1}) · Z{G(s)/s}. The term (1 − z^{-1}) captures the ZOH, which holds the control input constant between samples. G(s)/s represents the continuous plant preceded by an integrator, because the ZOH introduces an integration-like effect on the held signal. The z-transform of that combined system, discretized at rate T, gives the discrete-time transfer function relating z-domain input U(z) to output Y(z). Once you have G(z), all the root-locus and frequency-response techniques from continuous-time design carry over — but applied to the z-plane, with the unit circle replacing the imaginary axis as the stability boundary.

Stability checking without computing roots explicitly uses either **Jury's criterion** — a tabular test analogous to Routh-Hurwitz — or the **bilinear transformation** w = (z − 1)/(z + 1), which maps the unit disk onto the LHP. After applying this substitution to the characteristic polynomial, you recover a polynomial in w and apply Routh-Hurwitz directly. The choice of sampling period T profoundly affects the design: too large and dynamics are aliased or poorly approximated (the ZOH hold introduces a lag of T/2, degrading phase margin); too small and quantization noise and computational limitations dominate. A common rule of thumb is to sample at 10–20 times the closed-loop bandwidth, but the appropriate rate depends on the specific plant dynamics and noise environment.
