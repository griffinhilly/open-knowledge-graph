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

## Questions

```yaml
- question: "A continuous-time PID controller has all poles in the left half s-plane and is stable. It is discretized using forward Euler with a large sampling period T. What would you expect?"
  type: multiple-choice
  options:
    - "The discrete controller remains stable — pole locations in the s-plane determine stability absolutely, regardless of discretization method"
    - "The discrete controller may become unstable — large T can map s-plane poles to locations outside the unit circle in the z-plane"
    - "The discrete controller is functionally identical to the continuous one — only the notation changes from s to z"
    - "Stability is unaffected by sampling rate; only the speed of computation changes"
  answer: 1
  explanation: "This is the most critical misconception in digital control. A stable s-domain pole at s = -a maps to z = e^(-aT) under the exact mapping. For small T, e^(-aT) is safely inside the unit circle. But forward Euler uses the approximation s ≈ (z-1)/T, a cruder mapping that distorts the s-plane-to-z-plane relationship. As T increases, the approximation error grows, and poles that were stable in continuous time may map outside the unit circle — making the discrete controller unstable. Choosing an appropriate sampling rate and discretization method is not optional; it is essential to preserving stability."

- question: "Why is Tustin's bilinear method (s ≈ (2/T)(z-1)/(z+1)) generally preferred over forward Euler (s ≈ (z-1)/T) for discretizing continuous-time controllers?"
  type: multiple-choice
  options:
    - "Tustin's method requires fewer arithmetic operations per sample, making it faster to execute on microcontrollers"
    - "Tustin's method corresponds to the trapezoidal integration rule, better preserving stability margins and frequency-domain accuracy"
    - "Tustin's method eliminates the need for anti-aliasing filters before the ADC"
    - "Tustin's method maps the s-plane exactly to the z-plane, introducing no approximation error"
  answer: 1
  explanation: "Forward Euler uses a rectangular (left-endpoint) approximation to integration, which is first-order accurate and can push stable poles outside the unit circle. Tustin's bilinear method uses the trapezoidal rule — second-order accurate — and has the crucial property that the entire left half s-plane maps inside the unit circle, so a stable continuous controller always produces a stable discrete controller (though frequency response may be warped). This stability-preservation property makes Tustin the default choice for controller discretization. The tradeoff is frequency warping, which requires pre-warping of critical frequencies before applying the transformation."

- question: "In a digital control system, stability requires all poles of the discrete-time transfer function H(z) to lie strictly inside the unit circle |z| < 1."
  type: true-false
  answer: true
  explanation: "This is the z-domain analogue of the s-domain stability criterion (all poles in the left half-plane). The mapping between the two domains is z = e^(sT): a stable continuous-time pole at s = -a (left half-plane) maps to z = e^(-aT), which has magnitude e^(-aT) < 1 for positive a — inside the unit circle. Poles on the unit circle (|z| = 1) correspond to marginally stable behavior (undamped oscillation); poles outside are unstable. The unit circle plays exactly the role of the imaginary axis in the s-domain."

- question: "Digital control is simply analog control implemented in software — the same equations, just computed at discrete time steps rather than continuously."
  type: true-false
  answer: false
  explanation: "Digital implementation introduces new dynamics that do not exist in continuous-time analysis. Computation delay (typically one sample latency between measurement and output) adds a pure delay that degrades phase margin. Quantization error from finite ADC/DAC resolution adds a noise-like signal. Finite word length in the processor can cause limit cycling and coefficient rounding errors. The zero-order hold introduces a half-sample delay in the frequency response. None of these appear in the continuous-time model. A controller that works perfectly in continuous-time simulation may perform noticeably differently as a digital implementation, especially at frequencies approaching half the sampling rate."

- question: "Why must the sampling rate in a digital control system be much higher than the closed-loop bandwidth, and what happens to controller performance if sampling is too slow?"
  type: short-answer
  answer: "The sampling rate must be high enough that the controller can react to disturbances and errors within a fraction of the system's response time. The Nyquist criterion requires sampling at least twice the highest signal frequency, but in control this is insufficient — the rule of thumb is 5–20 times the closed-loop bandwidth. If sampling is too slow, several problems emerge: the zero-order hold introduces phase lag that erodes stability margins, the controller cannot respond quickly enough to reject disturbances, inter-sample behavior (what the plant does between samples) becomes significant and uncontrolled, and aliasing can fold high-frequency disturbances into the control bandwidth. The result is degraded tracking performance, reduced disturbance rejection, and potentially instability."
  explanation: "A concrete example: a controller with 10 Hz closed-loop bandwidth needs a 50–200 Hz sampling rate. At 50 Hz, the ZOH introduces about 10 ms of average delay (half a sample period), which adds phase lag of approximately 3.6° per Hz of bandwidth — noticeable but manageable. At 10 Hz sampling (only 1× bandwidth), the phase lag becomes catastrophic and the controller may destabilize. This is why choosing the sampling rate is one of the first design decisions in digital control, not an afterthought."
```

## Explainer

You've studied transfer functions and the Laplace transform as tools for analyzing continuous-time systems, and you may have designed a PID controller that works beautifully in continuous time. Now suppose you want to implement that controller in a microcontroller — you can't integrate or differentiate continuously, you can only read a sensor value, compute a number, and write an output, all at discrete time steps. This is the essential challenge of digital control: replacing a continuous-time system with a sampled-data approximation that preserves stability and performance.

The **sampling process** is the first step. An analog-to-digital converter (ADC) reads the physical signal at intervals of T seconds, producing a sequence of numbers x[0], x[1], x[2], .... The Nyquist-Shannon theorem (from signal processing) says you must sample at least twice the highest frequency in the signal to avoid **aliasing** — where high-frequency components masquerade as lower-frequency ones. In control, the rule of thumb is stricter: sample 5–20 times per closed-loop bandwidth period, because the control algorithm must also react to disturbances and model errors between samples. A controller with 10 Hz closed-loop bandwidth typically needs 50–200 Hz sampling. After the controller computes an output, a **zero-order hold (ZOH)** holds that output constant until the next sample — a staircase approximation to the continuous command signal.

The **z-transform** is the discrete-time analog of the Laplace transform. Just as the Laplace transform converts a continuous-time differential equation into an algebraic equation in s, the z-transform converts a discrete-time difference equation into an algebraic equation in z. The z variable represents a one-sample delay: z⁻¹ means "the value from the previous time step." Stability in the z-domain uses the unit circle as its boundary the same way the imaginary axis serves as the stability boundary in the s-domain: poles inside |z| < 1 are stable, poles outside are unstable. The exact mapping between the two domains is z = e^{sT} — a stable s-domain pole at s = -a maps to z = e^{-aT}, which lies inside the unit circle for positive a. But as T grows larger, this mapping distorts more severely, and poles that were comfortably stable in continuous time can wander near or outside the unit circle.

**Discretizing a controller** is the practical skill that ties this together. Suppose you have a PID controller C(s) designed for the continuous-time plant. The **Tustin bilinear method** approximates s ≈ (2/T)(z-1)/(z+1), substituting this expression everywhere s appears in C(s) to get a z-domain transfer function C(z). This is equivalent to using the trapezoidal rule to approximate integration — it's more accurate than forward or backward Euler and preserves stability better. However, Tustin introduces **frequency warping**: the discrete-time frequency response is a warped version of the continuous-time response, with higher frequencies compressed. If your controller has a critical frequency — a notch filter or a resonance peak — you must **pre-warp** that frequency before applying Tustin to ensure it appears at the right place after discretization. This is the detail that separates a digital implementation that works from one that performs subtly differently than the continuous design, especially at frequencies approaching half the sampling rate.
