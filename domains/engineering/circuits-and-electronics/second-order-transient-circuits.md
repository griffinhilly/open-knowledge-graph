---
id: second-order-transient-circuits
title: Second-Order Transient Circuit Response
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: first-order-transient-circuits
  type: hard
- id: lc-and-rlc-circuits
  type: soft
- id: characteristic-polynomial
  type: soft
builds-toward:
- resonance-circuits
tags:
- RLC
- second-order
- overdamped
- underdamped
- critically-damped
- natural-frequency
- damping-ratio
stage: formal-systems
status: draft
---

# Second-Order Transient Circuit Response

## Core Idea
RLC circuits containing both a capacitor and an inductor are described by second-order ODEs. The response is characterized by the undamped natural frequency ω₀ = 1/√(LC) and the damping ratio ζ (or damping coefficient α = R/2L for series RLC). The characteristic equation s² + 2αs + ω₀² = 0 has roots that determine the response type: overdamped (ζ > 1, two distinct real roots, sum of exponentials), critically damped (ζ = 1, repeated root, t·e^(−αt)), or underdamped (ζ < 1, complex roots, decaying sinusoidal oscillation). Initial conditions on both the variable and its first derivative are required.

## How It's Best Learned
Derive the characteristic equation for both series and parallel RLC circuits from KVL and KCL respectively. Sketch qualitative step responses for all three damping cases before computing exact answers. Practice finding the initial derivative from KVL or KCL at t = 0⁺.

## Common Misconceptions
- Forgetting that two initial conditions are needed: the initial value of the variable and the initial value of its derivative.
- Using the series RLC formula for α in a parallel RLC circuit (α = 1/(2RC) for parallel).
- Assuming underdamped means the response oscillates indefinitely — it decays to the forced response determined by sources.
