---
id: time-dilation-clock-rates
title: Time Dilation and Moving Clocks
domain: physics
course: modern-physics
prerequisites:
- id: time-dilation
  type: hard
builds-toward:
- mass-energy-equivalence-relativity
tags:
- special-relativity
- time
- clocks
stage: advanced
status: draft
---

# Time Dilation and Moving Clocks

## Core Idea
Moving clocks run slow compared to stationary clocks by a factor of γ = 1/√(1 − v²/c²)—the Lorentz factor. This effect is symmetric: each observer sees the other's clock running slow. Time dilation is not an illusion but a fundamental feature of spacetime; proper time measured along an object's worldline is invariant across frames.

## Explainer

From your prerequisite study of time dilation, you know that time runs at different rates for observers in relative motion. Now we go deeper: what does this mean for actual clocks, how do we calculate it precisely, and how do we resolve the apparent paradox that both observers see the other's clock running slow?

The **Lorentz factor** γ = 1/√(1 − v²/c²) is the central quantity. Notice its behavior: when v ≪ c, the factor under the square root is nearly 1, so γ ≈ 1 and clocks agree — recovering everyday experience. As v approaches c, the denominator approaches zero and γ grows without bound. A clock moving at 0.6c runs at γ = 1/√(0.64) = 1.25, meaning it ticks only 80% as fast as a stationary clock. At 0.99c, γ ≈ 7.1 — the moving clock runs more than seven times slower. GPS satellites must account for this effect to maintain centimeter-level positioning accuracy.

The symmetry of time dilation is the part that trips people up. If Alice's rocket moves past Bob at 0.6c, Bob sees Alice's clock running slow. But from Alice's frame, Bob is moving at 0.6c in the opposite direction — so Alice sees Bob's clock running slow. Both are correct. This is not a contradiction; it reflects that simultaneity is frame-dependent. The two observers are not comparing the same pair of events when they say "my clock reads T₁ while your clock reads T₂."

The resolution comes through **proper time**: the time measured by a clock that travels with the object being timed. Proper time τ along a worldline is invariant — every observer agrees on how much proper time a moving clock accumulates between two events on its worldline. The formula is τ = t/γ, where t is the coordinate time in the "stationary" frame. Proper time is shorter than coordinate time because the moving clock is traversing a path through spacetime, and spacetime geometry makes paths through time shorter when more spatial distance is covered. This is the deeper statement: time dilation is not a mechanical effect on clocks but a geometric fact about the structure of spacetime itself.
