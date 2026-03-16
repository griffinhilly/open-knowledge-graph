---
id: first-order-system-response-analysis
title: First-Order System Response Analysis
domain: engineering
course: control-systems
prerequisites:
- id: transfer-functions-control
  type: hard
- id: laplace-transform-control
  type: hard
builds-toward:
- rise-time-settling-time-overshoot
- sinusoidal-response-magnitude-phase-angle
tags:
- transient-response
- time-constant
- exponential
- step-response
stage: abstract-reasoning
status: draft
---

# First-Order System Response Analysis

## Core Idea
First-order systems, characterized by a single pole in the transfer function, respond exponentially to inputs with a time constant τ that controls the rate of approach to steady state. The step response rises as 1 − e^(−t/τ), reaching 63% of final value at t = τ.

## Explainer

You've studied transfer functions as the Laplace-domain ratio of output to input, and you know that a transfer function's poles — the values of s where the denominator is zero — determine the system's natural behavior. A **first-order system** has exactly one pole, giving a transfer function of the form G(s) = K/(τs + 1), where K is the DC gain and τ is the **time constant**. The single pole sits at s = −1/τ in the left half-plane (for a stable system). Everything about how this system responds to any input follows from these two parameters.

To understand why the response is exponential, return to the time-domain differential equation. A first-order system satisfies τ·(dy/dt) + y = K·u(t), where y is the output and u is the input. When u steps from 0 to 1 at t = 0, the solution is y(t) = K(1 − e^(−t/τ)). The output starts at zero, rises asymptotically toward the final value K, and the rate of rise is governed entirely by τ. At t = τ, you've covered 1 − e^(−1) ≈ 63% of the total distance. At t = 2τ, about 86%. At t = 5τ, the response is within 1% of steady state — the engineering convention is that the system has "settled" after five time constants. This 63%-at-one-tau rule is worth committing to memory: it's the clock tick of first-order dynamics.

The time constant has a physical interpretation that transfers across all first-order systems, regardless of domain. An RC electrical circuit has τ = RC: a 1 kΩ resistor with a 1 µF capacitor charges to 63% of supply voltage in 1 ms. A thermal system (room heating) has τ = thermal mass / thermal conductance. A fluid tank draining through an orifice has τ = volume / flow coefficient. In all cases, τ is the ratio of energy storage to energy dissipation — larger storage or smaller dissipation means slower response. When you see a Laplace-domain pole at s = −1/τ, you can immediately read off the physical timescale of the response.

In the frequency domain, the **Bode plot** of G(jω) = K/(jωτ + 1) shows a flat response at K for ω << 1/τ and a −20 dB/decade roll-off for ω >> 1/τ. The **break frequency** is ω_b = 1/τ — the frequency where the response has fallen to K/√2 (about 70.7% of DC gain, or −3 dB). This is the bandwidth of the first-order system: signals slower than 1/τ pass through with near-full gain; signals faster than 1/τ are attenuated. The connection between time-constant and bandwidth — τ = 1/ω_b — lets you move fluidly between the time-domain picture (how fast does it settle?) and the frequency-domain picture (what signals does it pass?). First-order analysis is the foundation on which second-order and higher-order system analysis is built: more complex systems are often characterized as collections of first-order modes, each contributing its own exponential to the total response.


