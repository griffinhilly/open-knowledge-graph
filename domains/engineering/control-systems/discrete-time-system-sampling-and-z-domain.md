---
id: discrete-time-system-sampling-and-z-domain
title: 'Discrete-Time Systems: Sampling and z-Domain Analysis'
domain: engineering
course: control-systems
prerequisites:
- id: digital-control-intro
  type: hard
- id: transfer-functions-control
  type: hard
builds-toward:
- practical-control-system-implementation
tags:
- sampling
- z-transform
- discrete-time
- aliasing
- sampler-hold
stage: advanced
status: draft
---

# Discrete-Time Systems: Sampling and z-Domain Analysis

## Core Idea
Sampling continuous signals at rate Ts produces discrete-time signals; the z-transform is the discrete analog of the Laplace transform with z = esTs. Nyquist sampling theorem requires Ts ≤ π/ωmax to avoid aliasing. Discrete-time systems are analyzed using z-domain pole-zero maps analogous to continuous s-domain analysis.

## Questions

```yaml
- question: "A control engineer samples a sensor at 500 Hz. An electric motor vibrates at 400 Hz, producing noise. In the sampled data, this noise appears at 100 Hz. The engineer applies a digital filter to remove the 100 Hz component. Why does this fail to eliminate the motor vibration?"
  type: multiple-choice
  options:
    - "Digital filters cannot attenuate frequencies above the Nyquist limit"
    - "Aliasing has already folded the 400 Hz signal onto 100 Hz; the two are indistinguishable in the sampled data, so filtering 100 Hz also removes genuine low-frequency signals"
    - "The z-transform maps 400 Hz to 100 Hz in the digital domain, and the filter must target 400 Hz directly"
    - "Sampling at 500 Hz is too slow to represent 400 Hz signals at all, so the noise does not appear in the data"
  answer: 1
  explanation: "This is aliasing: a 400 Hz signal sampled at 500 Hz folds to 500 − 400 = 100 Hz. Once aliasing occurs, the 400 Hz component and any genuine 100 Hz content are mathematically identical in the sampled sequence — no downstream digital processing can separate them. The correct remedy is an anti-aliasing filter applied to the analog signal before the ADC, attenuating everything above the Nyquist frequency (250 Hz in this case) before sampling begins. Filtering after the fact cannot undo the information loss."

- question: "In z-domain analysis, the stability condition for a discrete-time system requires that:"
  type: multiple-choice
  options:
    - "All poles lie in the left half of the z-plane (Re(z) < 0)"
    - "All poles lie inside the unit circle (|z| < 1)"
    - "All poles lie on the imaginary axis of the z-plane"
    - "All poles lie outside the unit circle (|z| > 1) to ensure sufficient gain"
  answer: 1
  explanation: "The mapping z = e^(sTs) transforms the stability boundary from the imaginary axis (Re(s) = 0) in the s-plane to the unit circle (|z| = 1) in the z-plane. The left half s-plane (stable region, Re(s) < 0) maps to the interior of the unit circle. So a discrete-time system is stable if and only if all its poles satisfy |z| < 1. This is the z-domain analog of the continuous-time rule — the geometry changes but the logic is identical."

- question: "Anti-aliasing filters must be applied to the analog signal before the analog-to-digital converter, not applied digitally after sampling, because aliasing creates frequency content indistinguishable from genuine low-frequency signals."
  type: true-false
  answer: true
  explanation: "Aliasing is a fundamental and irreversible consequence of sampling. Once a high-frequency signal has been sampled below the Nyquist rate, its alias overlaps with lower frequencies in the digital domain. There is no way to distinguish the aliased content from genuine content at that frequency — the information is permanently confounded. Anti-aliasing filters must act on the continuous-time signal before it is discretized."

- question: "If a signal has been aliased during sampling, increasing the sampling rate of subsequent processing can recover the original high-frequency content."
  type: true-false
  answer: false
  explanation: "Aliasing is irreversible. Once a signal is sampled below its Nyquist rate, high-frequency components are folded into lower frequencies and the distinction is permanently lost. Resampling the already-aliased digital sequence at a higher rate simply interpolates the corrupted data — it cannot reconstruct information that was never captured. Recovery requires going back to the original analog signal and resampling it at a sufficient rate with an anti-aliasing filter in place."

- question: "Explain why aliasing is described as a fundamental consequence of sampling rather than a numerical error, and what this implies about when anti-aliasing filters must be applied."
  type: short-answer
  answer: "Aliasing arises from the mathematics of periodic sampling itself, not from any computational imprecision. When a continuous signal is sampled at rate fs, the spectrum of the sampled sequence is a sum of shifted copies of the original spectrum, repeated at every multiple of fs. If the original signal contains energy above fs/2, those spectral copies overlap and add together — frequencies above Nyquist are permanently confused with frequencies below it. No amount of computational care or post-processing can undo this because the information distinguishing the two was never captured. Anti-aliasing filters must therefore attenuate all signal content above the Nyquist frequency before the analog-to-digital conversion occurs."
  explanation: "This is why the Nyquist theorem is a hard constraint rather than a guideline. It is not that sampling above Nyquist is 'safer' — it is that sampling below Nyquist is mathematically guaranteed to produce aliasing regardless of how carefully the digital processing is done. Engineers place analog lowpass filters before ADCs for precisely this reason: the only point at which aliasing can be prevented is before it happens."
```

## Explainer

Your understanding of continuous transfer functions established that a system's behavior is characterized by where its poles and zeros sit in the complex s-plane, with the imaginary axis as the stability boundary. Digital control forces a translation: microcontrollers read sensors and update actuators at discrete time steps, not continuously. A sensor sampled every T_s seconds produces a sequence of numbers y[0], y[1], y[2], ... rather than a continuous signal y(t). The **z-transform** is the mathematical tool built for exactly this setting, playing the same role for discrete-time sequences that the Laplace transform plays for continuous-time functions.

The connection between the two domains is the substitution **z = e^(sT_s)**. To understand what this mapping does geometrically: the left half of the s-plane (stable continuous poles, where Re(s) < 0) maps to the interior of the unit circle in the z-plane (|z| < 1). The imaginary axis (s = jω, the stability boundary) maps to the unit circle itself (|z| = 1). So the stability test changes from "are all poles in the left half-plane?" to "are all poles inside the unit circle?" — a new geometry, but the same logic. A discrete-time transfer function H(z) = Y(z)/U(z) is analyzed with identical tools: factor, find poles and zeros, check stability, compute frequency response by evaluating along the unit circle (z = e^(jωT_s)).

**Sampling** introduces a constraint with no continuous-time analog: the **Nyquist theorem**. When you sample a signal at rate f_s = 1/T_s, you can only faithfully represent frequencies up to f_s/2 (the Nyquist frequency). Any signal component above this frequency folds back into the spectrum — it appears as a lower frequency signal indistinguishable from a genuine low-frequency component. This **aliasing** is not a numerical artifact; it is a fundamental consequence of the sampling process. A 1100 Hz tone sampled at 1000 Hz is indistinguishable from a 100 Hz tone in the sampled data. In control systems, aliasing from sensor noise or vibration can destabilize a controller that was designed assuming clean measurements, which is why anti-aliasing filters are placed before analog-to-digital converters.

Choosing the sampling rate T_s involves a practical tradeoff. Faster sampling (smaller T_s) reduces aliasing risk and makes the discrete controller approximate a continuous one more closely, but demands faster computation and generates more data. A common rule of thumb is to sample 10–20 times faster than the closed-loop bandwidth, ensuring that the discretization introduces negligible phase lag in the frequency range where the control loop operates. Too slow, and the digital controller introduces phase lag that degrades stability margins or causes instability — the zero-order hold (ZOH), which holds each sample value constant until the next sample, adds an effective time delay of T_s/2 that reduces phase margin. Understanding this z-domain framework equips you to design and analyze controllers that will actually run on real digital hardware, which is the implementation context that follows directly from these foundations.
