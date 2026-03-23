---
id: first-order-system-transient-response
title: 'First-Order System Response: Time Constant and Behavior'
domain: engineering
course: control-systems
prerequisites:
- id: response-specifications-performance-metrics
  type: hard
builds-toward:
- second-order-system-damping-ratio
tags:
- first-order
- time-constant
- exponential-response
stage: expert
status: validated
---

# First-Order System Response: Time Constant and Behavior

## Core Idea
First-order systems have one pole; step response is y(t) = 1 - e^(-t/τ) where τ is time constant. At t = τ, response reaches 63%. At t = 4τ (settling time), response is within 2% of final value. Frequency response has corner frequency at ω = 1/τ. Time constant directly controls response speed.

## Questions

```yaml
- question: "A first-order RC circuit has τ = 10 ms. An engineer wants to reduce the settling time (to within 2% of final value) by a factor of 4. Which change accomplishes this?"
  type: multiple-choice
  options:
    - "Apply a larger step input voltage — more voltage drives the capacitor to charge faster"
    - "Reduce the time constant to τ = 2.5 ms, for example by reducing resistance or capacitance"
    - "Double the resistance while keeping capacitance the same"
    - "Apply a sinusoidal input at the corner frequency to accelerate the transient"
  answer: 1
  explanation: "Settling time is approximately 4τ. To cut settling time by a factor of 4, you need to cut τ by a factor of 4 — from 10 ms to 2.5 ms. The time constant τ = RC, so reducing R or C (or both) achieves this. Applying a larger input voltage does not change the settling time — it changes the final value but the system still takes 4τ to reach 98% of that value. The shape of the exponential approach (and thus τ) is a property of the system, not the input magnitude."

- question: "A control engineer examines the step response of a closed-loop system and observes clear overshoot — the output rises above the commanded setpoint before settling. What can she conclude about the system's order?"
  type: multiple-choice
  options:
    - "Nothing definitive — first-order systems can overshoot if the input step is large enough or the gain is too high"
    - "The system must be at least second-order, since a first-order system cannot overshoot"
    - "The system is first-order with an unusually large time constant and a high-gain controller"
    - "The system has a right-half-plane zero, which causes overshoot regardless of system order"
  answer: 1
  explanation: "A first-order system governed by y(t) = 1 − e^(−t/τ) approaches its final value monotonically — it can never exceed it. This is a mathematical fact: the exponential term is always positive, so the output always falls short of 1, approaching from below. Overshoot requires a system with at least two energy-storage elements (two poles) — enough complexity to produce oscillatory behavior. The moment you observe overshoot, you know the system has at least two poles. This is a powerful diagnostic: overshooting responses are never first-order."

- question: "A first-order system with time constant τ = 5 s has a bandwidth (corner frequency) of 0.2 rad/s, meaning sinusoidal inputs above this frequency are attenuated at −20 dB/decade."
  type: true-false
  answer: true
  explanation: "The transfer function of a first-order system is H(s) = 1/(τs + 1), which has its pole at s = −1/τ. The corner frequency (−3 dB bandwidth) is ω_c = 1/τ = 1/5 = 0.2 rad/s. Below this frequency, the system passes inputs with near-unity gain. Above it, the magnitude rolls off at −20 dB/decade. A system with τ = 5 s is a slow system: it faithfully tracks inputs that change on timescales longer than about 5 seconds but heavily attenuates faster variations."

- question: "After 2 time constants (t = 2τ), a first-order step response has completed approximately 95% of its total change and can be considered essentially settled."
  type: true-false
  answer: false
  explanation: "At t = 2τ, the response is 1 − e^(−2) ≈ 0.865, meaning about 86.5% complete — not 95%. The 95% threshold is reached at approximately t = 3τ (since 1 − e^(−3) ≈ 0.950). The conventional 2% settling criterion is reached at t ≈ 4τ (since 1 − e^(−4) ≈ 0.982). The common confusion is between the 63% mark at τ, the 95% mark at 3τ, and the 98% settling at 4τ. Misidentifying the settling time leads to significant control design errors — a system that looks settled at 2τ still has 13.5% of its transient remaining."

- question: "Explain why the time constant τ appears in both the step response formula and the frequency-domain bandwidth, and what this tells you about the relationship between response speed and bandwidth in a first-order system."
  type: short-answer
  answer: "Both come from the same underlying transfer function H(s) = 1/(τs + 1). In the time domain, the inverse Laplace transform gives y(t) = 1 − e^(−t/τ), so τ sets the timescale of the exponential decay. In the frequency domain, the magnitude |H(jω)| falls to 1/√2 (−3 dB) at ω = 1/τ, defining the bandwidth. They are two representations of the same parameter. A small τ means fast exponential rise AND large bandwidth — the system responds quickly to steps AND passes high-frequency inputs. A large τ means slow rise AND narrow bandwidth. Speed and bandwidth are not independent choices; they are two faces of the same coin."
  explanation: "This duality is a fundamental property of linear time-invariant systems: the step response and the frequency response are Fourier-transform pairs. Fast systems (small τ) have high bandwidth because they can faithfully track rapidly changing inputs; slow systems (large τ) behave as low-pass filters, smoothing out rapid variations. In design, increasing bandwidth (to get faster response) always comes at a cost — typically sensitivity to high-frequency noise. This tradeoff between speed and noise rejection runs throughout control systems design."
```

## Explainer

You've already studied performance metrics like rise time, settling time, and overshoot, which describe how well a system responds to inputs. First-order systems are the simplest class that make these concepts concrete and calculable: one energy-storage element, one pole, one differential equation. Mastering the first-order step response gives you the template that all more complex transient analysis builds on.

A **first-order system** is governed by a differential equation of the form τ·ẏ + y = u, where u is the input, y is the output, and τ is the **time constant**. When a unit step input is applied (u jumps from 0 to 1 at t = 0), the output is y(t) = 1 − e^(−t/τ). This exponential approach to the final value is the signature of first-order dynamics. Physically, it appears everywhere: the charging voltage on an RC circuit (τ = RC), the temperature of a body cooling toward ambient (τ = thermal mass / thermal conductance), the velocity of an object subject to viscous drag (τ = mass / damping coefficient). The same mathematical shape — an exponential rise — describes all of them.

The **time constant τ** is the system's single most important parameter. At t = τ, the output has reached 1 − e^(−1) ≈ 0.632, or about 63% of its final value. This is not an arbitrary threshold — it follows directly from the exponential formula and provides a convenient rule of thumb: one time constant gets you 63% of the way there, two time constants get you 86%, three get you 95%, and four get you 98%. The **settling time** is approximately 4τ (the time to reach and stay within 2% of the final value). Rise time (10% to 90%) is approximately 2.2τ. Crucially, a first-order system has **no overshoot** — it approaches its final value monotonically from below for a positive step. If a system shows overshoot, it is at least second-order.

In the **frequency domain**, the time constant determines the **bandwidth**: the system's transfer function is H(s) = 1 / (τs + 1), which has a pole at s = −1/τ. The Bode magnitude plot is flat at 0 dB below the **corner frequency** ω_c = 1/τ and rolls off at −20 dB/decade above it. This means a fast system (small τ, large ω_c) responds accurately to high-frequency inputs, while a slow system (large τ, small ω_c) acts as a low-pass filter, attenuating rapid changes. The connection between time domain (step response governed by τ) and frequency domain (bandwidth 1/τ) is not a coincidence — it is a fundamental property of linear systems, and recognizing this duality will be essential as you move to second-order systems and more complex transfer functions.


