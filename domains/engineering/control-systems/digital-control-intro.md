---
id: digital-control-intro
title: Introduction to Digital Control Systems
domain: engineering
course: control-systems
prerequisites:
- id: transfer-functions-control
  type: hard
- id: laplace-transform-control
  type: soft
- id: pid-control
  type: soft
tags:
- digital-control
- z-transform
- sampled-data
- discretization
- sampling-rate
stage: advanced
status: validated
---

# Introduction to Digital Control Systems

## Core Idea
Digital control systems process continuous physical signals using discrete-time computations, requiring analog-to-digital conversion (sampling) and digital-to-analog conversion (typically via zero-order hold reconstruction). The z-transform Z{x[k]} = Σ x[k]z^{−k} plays the role of the Laplace transform for discrete-time systems, and stability requires all poles of the discrete-time transfer function H(z) to lie inside the unit circle |z| < 1. Continuous-time controllers are discretized using methods including forward Euler (s ≈ (z−1)/T), backward Euler (s ≈ (z−1)/Tz), or Tustin's bilinear method (s ≈ (2/T)(z−1)/(z+1)). Practical sampling rates are typically 5–20 times the closed-loop bandwidth to avoid performance degradation from inter-sample behavior.

## How It's Best Learned
Discretize a continuous PID controller using Tustin's method and compare the step response of continuous and discrete implementations at several sampling rates to directly observe how aliasing and delay degrade performance below the Nyquist limit.

## Common Misconceptions
- A stable continuous-time controller does not automatically remain stable after discretization — poles that were in the left half s-plane may map outside the unit circle if the sampling period is too large.
- The z-domain and s-domain are related by z = e^{sT}, but this mapping is transcendental; the bilinear approximation introduces frequency warping that must be precompensated for accurate frequency-domain design.
- Digital control is not simply analog control implemented in software — computation delay (one sample latency), quantization error, and finite word length all introduce dynamics absent in continuous-time analysis.

## Explainer

You've studied transfer functions and the Laplace transform as tools for analyzing continuous-time systems, and you may have designed a PID controller that works beautifully in continuous time. Now suppose you want to implement that controller in a microcontroller — you can't integrate or differentiate continuously, you can only read a sensor value, compute a number, and write an output, all at discrete time steps. This is the essential challenge of digital control: replacing a continuous-time system with a sampled-data approximation that preserves stability and performance.

The **sampling process** is the first step. An analog-to-digital converter (ADC) reads the physical signal at intervals of T seconds, producing a sequence of numbers x[0], x[1], x[2], .... The Nyquist-Shannon theorem (from signal processing) says you must sample at least twice the highest frequency in the signal to avoid **aliasing** — where high-frequency components masquerade as lower-frequency ones. In control, the rule of thumb is stricter: sample 5–20 times per closed-loop bandwidth period, because the control algorithm must also react to disturbances and model errors between samples. A controller with 10 Hz closed-loop bandwidth typically needs 50–200 Hz sampling. After the controller computes an output, a **zero-order hold (ZOH)** holds that output constant until the next sample — a staircase approximation to the continuous command signal.

The **z-transform** is the discrete-time analog of the Laplace transform. Just as the Laplace transform converts a continuous-time differential equation into an algebraic equation in s, the z-transform converts a discrete-time difference equation into an algebraic equation in z. The z variable represents a one-sample delay: z⁻¹ means "the value from the previous time step." Stability in the z-domain uses the unit circle as its boundary the same way the imaginary axis serves as the stability boundary in the s-domain: poles inside |z| < 1 are stable, poles outside are unstable. The exact mapping between the two domains is z = e^{sT} — a stable s-domain pole at s = -a maps to z = e^{-aT}, which lies inside the unit circle for positive a. But as T grows larger, this mapping distorts more severely, and poles that were comfortably stable in continuous time can wander near or outside the unit circle.

**Discretizing a controller** is the practical skill that ties this together. Suppose you have a PID controller C(s) designed for the continuous-time plant. The **Tustin bilinear method** approximates s ≈ (2/T)(z-1)/(z+1), substituting this expression everywhere s appears in C(s) to get a z-domain transfer function C(z). This is equivalent to using the trapezoidal rule to approximate integration — it's more accurate than forward or backward Euler and preserves stability better. However, Tustin introduces **frequency warping**: the discrete-time frequency response is a warped version of the continuous-time response, with higher frequencies compressed. If your controller has a critical frequency — a notch filter or a resonance peak — you must **pre-warp** that frequency before applying Tustin to ensure it appears at the right place after discretization. This is the detail that separates a digital implementation that works from one that performs subtly differently than the continuous design, especially at frequencies approaching half the sampling rate.
