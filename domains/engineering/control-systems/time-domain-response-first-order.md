---
id: time-domain-response-first-order
title: First-Order System Time Response
domain: engineering
course: control-systems
prerequisites:
- id: transfer-functions-control
  type: hard
- id: first-order-transient-circuits
  type: soft
builds-toward:
- time-domain-response-second-order
- steady-state-error-analysis
tags:
- time-constant
- step-response
- first-order
- transient
- bandwidth
stage: advanced
status: validated
---

# First-Order System Time Response

## Core Idea
A first-order system has a transfer function G(s) = K/(τs + 1), where K is the DC gain and τ is the time constant. The step response rises exponentially as y(t) = K(1 − e^{−t/τ}), reaching 63.2% of its final value at t = τ and settling within 2% at t ≈ 4τ. First-order systems never overshoot — they approach the final value monotonically. The time constant τ characterizes both the speed of response and the system's bandwidth (ω₋₃dB = 1/τ rad/s), providing a direct link between time-domain and frequency-domain behavior.

## How It's Best Learned
Measure and fit τ from step response data on RC circuits or thermal systems, then verify by computing the Bode bandwidth. Simulate step responses with varying K and τ to build physical intuition before moving to higher-order systems.

## Common Misconceptions
- The time constant τ is not the settling time; the 2% settling time is approximately 4τ.
- A first-order system with an added zero is still first-order but can exhibit an initial positive spike or an initial undershoot depending on the zero location.
- Faster response (smaller τ) requires larger bandwidth, which amplifies measurement noise — speed always trades off against noise sensitivity.

## Explainer

The first-order system is the simplest dynamical system — one energy storage element, one time constant, no oscillations. You already know transfer functions map inputs to outputs in the Laplace domain. When you apply a unit step input to G(s) = K/(τs + 1), the output in the time domain is y(t) = K(1 − e^{−t/τ}). This exponential rise follows directly from the system's internal feedback structure: the rate of change is proportional to how far the output still has to go. That is exactly what produces the decaying-error shape. The system is always "trying to catch up" to the target, and as it gets closer, it slows down.

The **time constant** τ is the single most important parameter. At t = τ, the output has reached 63.2% of its final value — this number is 1 − e^{−1} ≈ 0.632. At 2τ you are at 86%; at 4τ you are at 98%. Engineers use the **2% settling time** ≈ 4τ as the practical definition of when the transient is over. The system never literally reaches the final value (it approaches asymptotically), but 4τ is close enough for all practical purposes. Knowing τ from a step test immediately tells you how quickly the system responds and what bandwidth you will need to track time-varying inputs.

The time constant also links time-domain behavior to frequency-domain behavior. The **bandwidth** — the frequency at which output power drops to half its DC value — equals ω_{−3dB} = 1/τ exactly. Faster systems (smaller τ) have wider bandwidth, meaning they faithfully track higher-frequency input changes. But that wider bandwidth also passes more high-frequency noise through the system. A thermostat with a one-second time constant tracks fast temperature fluctuations precisely but is jittery; one with a ten-second time constant is smooth but sluggish. This speed-versus-noise tradeoff recurs in every real control and signal processing design — first-order systems make it explicit and quantitative.

One thing first-order systems never do is **overshoot**. With a single pole at s = −1/τ, the step response is purely real-exponential and rises monotonically. You can add a **zero** to a first-order system (by differentiating the input, for example), which may create an initial spike or undershoot depending on the zero location, but the underlying pole structure remains first-order and the response eventually settles without oscillation. This clean baseline — one pole, monotonic approach, settling at 4τ, bandwidth at 1/τ — is what you will use as a reference when second-order systems begin to overshoot and ring. The richer behavior there comes entirely from the second pole.
