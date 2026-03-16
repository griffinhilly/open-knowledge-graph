---
id: natural-frequency-damping-second-order
title: Natural Frequency and Damping Ratio
domain: engineering
course: control-systems
prerequisites:
- id: characteristic-equation-and-stability
  type: hard
- id: second-order-system-response-analysis
  type: hard
builds-toward:
- time-domain-performance-specifications
- root-locus-pole-placement
tags:
- natural-frequency
- damping
- second-order
- parameters
stage: advanced
status: draft
---

# Natural Frequency and Damping Ratio

## Core Idea
A second-order system is completely characterized by natural frequency ωₙ (undamped oscillation rate) and damping ratio ζ (energy dissipation). Standard form H(s) = ωₙ²/(s² + 2ζωₙs + ωₙ²) yields poles at -ζωₙ ± jωₙ√(1-ζ²). These parameters directly relate to time-domain metrics: overshoot depends on ζ, rise time on ωₙ, and settling time on ζωₙ.

## Explainer

From your work on the characteristic equation, you know that closed-loop poles determine stability and the shape of transient response. For a second-order system — the most common prototype in control design — two parameters capture *all* the information about how the system responds: **natural frequency ωₙ** and **damping ratio ζ**. These are not just abstract mathematical quantities; they correspond directly to physical intuitions about speed and oscillation that engineers use to specify performance requirements.

The **undamped natural frequency ωₙ** is the frequency at which the system would oscillate if there were no damping at all (ζ = 0). Think of a mass-spring system with no friction — it oscillates forever at ωₙ = √(k/m). In control systems, ωₙ sets the *speed* of the system's response: higher ωₙ means faster response. When you want a system that reacts quickly to commands — a fast robot arm or a tight position servo — you want high ωₙ. The standard form denominator s² + 2ζωₙs + ωₙ² makes this explicit: ωₙ² appears as the constant term, so ωₙ = √(constant term) by inspection.

The **damping ratio ζ** controls the shape of the response — specifically, how much the system overshoots its target before settling. At ζ = 0, the system oscillates indefinitely with no decay. At ζ = 1 (critically damped), it reaches the target as fast as possible without overshooting. For 0 < ζ < 1 (underdamped), the system overshoots and oscillates, with smaller ζ producing more oscillation. The **percent overshoot** is determined solely by ζ: %OS = exp(−πζ/√(1−ζ²)) × 100. A damping ratio of 0.707 gives about 4.3% overshoot and is a common design target because it balances speed against overshoot. The poles of the standard-form transfer function sit at s = −ζωₙ ± jωₙ√(1−ζ²): the real part −ζωₙ governs the decay rate (and thus settling time), and the imaginary part ωₙ√(1−ζ²) is the **damped natural frequency ω_d** at which oscillations occur.

The geometric picture in the complex plane is powerful. The poles lie on a circle of radius ωₙ centered at the origin. The angle from the negative real axis to the pole is θ = cos⁻¹(ζ) — so damping ratio is literally the cosine of the pole angle. A pole exactly on the negative real axis (θ = 0°) has ζ = 1 (critically damped). A pole at 45° from the negative real axis has ζ = cos(45°) ≈ 0.707. A pole near the imaginary axis has small ζ and oscillates heavily. This geometric relationship is the bridge between the characteristic equation's roots and time-domain performance specifications — you can look at a pole location in the s-plane and immediately read off the approximate overshoot, damped frequency, and settling time without solving the ODE.
