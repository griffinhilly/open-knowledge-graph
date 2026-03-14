---
id: time-domain-response-second-order
title: Second-Order System Time Response
domain: engineering
course: control-systems
prerequisites:
- id: time-domain-response-first-order
  type: hard
- id: second-order-transient-circuits
  type: soft
- id: simple-harmonic-motion
  type: soft
builds-toward:
- steady-state-error-analysis
- routh-hurwitz-criterion
- pid-control
tags:
- damping-ratio
- natural-frequency
- percent-overshoot
- settling-time
- second-order
stage: advanced
status: validated
---

# Second-Order System Time Response

## Core Idea
A standard second-order system has the transfer function G(s) = ωₙ²/(s² + 2ζωₙs + ωₙ²), characterized by natural frequency ωₙ and damping ratio ζ. The damping ratio determines qualitative behavior: underdamped (ζ < 1) produces oscillatory overshoot, critically damped (ζ = 1) gives the fastest non-overshooting response, and overdamped (ζ > 1) gives a sluggish monotone response. Key performance metrics — percent overshoot (%OS = e^{−πζ/√(1−ζ²)}×100), rise time, peak time Tₚ = π/ωd, and settling time Ts ≈ 4/(ζωₙ) — are analytically derivable from ζ and ωₙ. Most control design specifications are stated in terms of these metrics.

## How It's Best Learned
Plot step responses for ζ = 0.1, 0.5, 0.707, 1.0, and 2.0 to internalize how damping affects behavior. Derive the overshoot formula and settling time approximation so they become second nature — these are the most frequently used formulas in control design.

## Common Misconceptions
- Critically damped (ζ = 1) is not always the best choice — ζ ≈ 0.7 often gives a better tradeoff between speed and overshoot in practice.
- The overshoot and settling time formulas apply to the ideal second-order prototype; additional poles or zeros change these predictions significantly.
- Natural frequency ωₙ is not the oscillation frequency of the step response; the damped natural frequency ωd = ωₙ√(1−ζ²) is the actual oscillation rate.
