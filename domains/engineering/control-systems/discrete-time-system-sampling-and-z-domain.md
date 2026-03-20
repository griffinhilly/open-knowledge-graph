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

## Explainer

Your understanding of continuous transfer functions established that a system's behavior is characterized by where its poles and zeros sit in the complex s-plane, with the imaginary axis as the stability boundary. Digital control forces a translation: microcontrollers read sensors and update actuators at discrete time steps, not continuously. A sensor sampled every T_s seconds produces a sequence of numbers y[0], y[1], y[2], ... rather than a continuous signal y(t). The **z-transform** is the mathematical tool built for exactly this setting, playing the same role for discrete-time sequences that the Laplace transform plays for continuous-time functions.

The connection between the two domains is the substitution **z = e^(sT_s)**. To understand what this mapping does geometrically: the left half of the s-plane (stable continuous poles, where Re(s) < 0) maps to the interior of the unit circle in the z-plane (|z| < 1). The imaginary axis (s = jω, the stability boundary) maps to the unit circle itself (|z| = 1). So the stability test changes from "are all poles in the left half-plane?" to "are all poles inside the unit circle?" — a new geometry, but the same logic. A discrete-time transfer function H(z) = Y(z)/U(z) is analyzed with identical tools: factor, find poles and zeros, check stability, compute frequency response by evaluating along the unit circle (z = e^(jωT_s)).

**Sampling** introduces a constraint with no continuous-time analog: the **Nyquist theorem**. When you sample a signal at rate f_s = 1/T_s, you can only faithfully represent frequencies up to f_s/2 (the Nyquist frequency). Any signal component above this frequency folds back into the spectrum — it appears as a lower frequency signal indistinguishable from a genuine low-frequency component. This **aliasing** is not a numerical artifact; it is a fundamental consequence of the sampling process. A 1100 Hz tone sampled at 1000 Hz is indistinguishable from a 100 Hz tone in the sampled data. In control systems, aliasing from sensor noise or vibration can destabilize a controller that was designed assuming clean measurements, which is why anti-aliasing filters are placed before analog-to-digital converters.

Choosing the sampling rate T_s involves a practical tradeoff. Faster sampling (smaller T_s) reduces aliasing risk and makes the discrete controller approximate a continuous one more closely, but demands faster computation and generates more data. A common rule of thumb is to sample 10–20 times faster than the closed-loop bandwidth, ensuring that the discretization introduces negligible phase lag in the frequency range where the control loop operates. Too slow, and the digital controller introduces phase lag that degrades stability margins or causes instability — the zero-order hold (ZOH), which holds each sample value constant until the next sample, adds an effective time delay of T_s/2 that reduces phase margin. Understanding this z-domain framework equips you to design and analyze controllers that will actually run on real digital hardware, which is the implementation context that follows directly from these foundations.
