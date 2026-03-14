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
