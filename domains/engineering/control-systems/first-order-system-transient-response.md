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
stage: advanced
status: draft
---

# First-Order System Response: Time Constant and Behavior

## Core Idea
First-order systems have one pole; step response is y(t) = 1 - e^(-t/τ) where τ is time constant. At t = τ, response reaches 63%. At t = 4τ (settling time), response is within 2% of final value. Frequency response has corner frequency at ω = 1/τ. Time constant directly controls response speed.

## Explainer

You've already studied performance metrics like rise time, settling time, and overshoot, which describe how well a system responds to inputs. First-order systems are the simplest class that make these concepts concrete and calculable: one energy-storage element, one pole, one differential equation. Mastering the first-order step response gives you the template that all more complex transient analysis builds on.

A **first-order system** is governed by a differential equation of the form τ·ẏ + y = u, where u is the input, y is the output, and τ is the **time constant**. When a unit step input is applied (u jumps from 0 to 1 at t = 0), the output is y(t) = 1 − e^(−t/τ). This exponential approach to the final value is the signature of first-order dynamics. Physically, it appears everywhere: the charging voltage on an RC circuit (τ = RC), the temperature of a body cooling toward ambient (τ = thermal mass / thermal conductance), the velocity of an object subject to viscous drag (τ = mass / damping coefficient). The same mathematical shape — an exponential rise — describes all of them.

The **time constant τ** is the system's single most important parameter. At t = τ, the output has reached 1 − e^(−1) ≈ 0.632, or about 63% of its final value. This is not an arbitrary threshold — it follows directly from the exponential formula and provides a convenient rule of thumb: one time constant gets you 63% of the way there, two time constants get you 86%, three get you 95%, and four get you 98%. The **settling time** is approximately 4τ (the time to reach and stay within 2% of the final value). Rise time (10% to 90%) is approximately 2.2τ. Crucially, a first-order system has **no overshoot** — it approaches its final value monotonically from below for a positive step. If a system shows overshoot, it is at least second-order.

In the **frequency domain**, the time constant determines the **bandwidth**: the system's transfer function is H(s) = 1 / (τs + 1), which has a pole at s = −1/τ. The Bode magnitude plot is flat at 0 dB below the **corner frequency** ω_c = 1/τ and rolls off at −20 dB/decade above it. This means a fast system (small τ, large ω_c) responds accurately to high-frequency inputs, while a slow system (large τ, small ω_c) acts as a low-pass filter, attenuating rapid changes. The connection between time domain (step response governed by τ) and frequency domain (bandwidth 1/τ) is not a coincidence — it is a fundamental property of linear systems, and recognizing this duality will be essential as you move to second-order systems and more complex transfer functions.


