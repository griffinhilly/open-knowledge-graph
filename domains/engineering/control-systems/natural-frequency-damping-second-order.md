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
- id: second-order-system-damping-ratio
  type: soft
builds-toward:
- time-domain-performance-specifications
- root-locus-pole-placement
tags:
- natural-frequency
- damping
- second-order
- parameters
stage: advanced
status: validated
---
# Natural Frequency and Damping Ratio

## Core Idea
A second-order system is completely characterized by natural frequency ωₙ (undamped oscillation rate) and damping ratio ζ (energy dissipation). Standard form H(s) = ωₙ²/(s² + 2ζωₙs + ωₙ²) yields poles at -ζωₙ ± jωₙ√(1-ζ²). These parameters directly relate to time-domain metrics: overshoot depends on ζ, rise time on ωₙ, and settling time on ζωₙ.

## Questions

```yaml
- question: "A second-order control system has ωₙ = 4 rad/s and ζ = 0.3. A designer wants to approximately halve the settling time without changing the percent overshoot. What adjustment achieves this?"
  type: multiple-choice
  options:
    - "Double ζ to 0.6 while keeping ωₙ = 4 rad/s"
    - "Double ωₙ to 8 rad/s while keeping ζ = 0.3"
    - "Halve ζ to 0.15 while keeping ωₙ = 4 rad/s"
    - "Halve both ωₙ to 2 rad/s and ζ to 0.15"
  answer: 1
  explanation: "Settling time is approximately 4/(ζωₙ) — the decay time constant is τ = 1/(ζωₙ). To halve settling time, you need to double the decay rate ζωₙ. Keeping ζ constant and doubling ωₙ doubles the product ζωₙ, halving settling time. Since percent overshoot depends only on ζ (not ωₙ), overshoot is unchanged. Option A would also speed settling but changes the overshoot by altering ζ. This highlights that ωₙ and ζ can be tuned somewhat independently."

- question: "The closed-loop poles of a second-order system are located at s = −2 ± j2. What are the natural frequency ωₙ and damping ratio ζ?"
  type: multiple-choice
  options:
    - "ωₙ = 2√2 rad/s, ζ = cos(45°) ≈ 0.707"
    - "ωₙ = 2 rad/s, ζ = 0.5"
    - "ωₙ = 4 rad/s, ζ = 0.707"
    - "ωₙ = 2 rad/s, ζ = 1"
  answer: 0
  explanation: "The poles lie at distance ωₙ from the origin: ωₙ = √(2² + 2²) = √8 = 2√2 ≈ 2.83 rad/s. The angle from the negative real axis is θ = arctan(2/2) = 45°, and ζ = cos(45°) ≈ 0.707. This geometric reading — ωₙ is the pole's distance from the origin, ζ is the cosine of its angle from the negative real axis — is the key s-plane insight that lets you infer time-domain performance directly from the pole plot."

- question: "For a standard second-order system, increasing the natural frequency ωₙ while holding the damping ratio ζ constant will increase the percent overshoot."
  type: true-false
  answer: false
  explanation: "Percent overshoot is determined solely by ζ: %OS = exp(−πζ/√(1−ζ²)) × 100. The natural frequency ωₙ controls the speed of the response (rise time, settling time) but does not affect the overshoot. Changing ωₙ moves the poles radially in the s-plane — closer to or farther from the origin — without changing the angle, so ζ = cos(θ) is unchanged and overshoot is unchanged."

- question: "In the complex s-plane, the poles of a standard second-order transfer function lie on a circle of radius ωₙ centered at the origin, and the damping ratio equals the cosine of the angle the pole makes with the negative real axis."
  type: true-false
  answer: true
  explanation: "The poles are at s = −ζωₙ ± jωₙ√(1−ζ²). Their distance from the origin is √((ζωₙ)² + (ωₙ√(1−ζ²))²) = ωₙ√(ζ²+1−ζ²) = ωₙ. The angle from the negative real axis satisfies cos(θ) = ζωₙ/ωₙ = ζ. This geometric picture is why root-locus design is powerful: you can read ωₙ and ζ — and therefore all time-domain specs — directly from where the poles sit in the s-plane."

- question: "Explain the geometric interpretation of ωₙ and ζ in the s-plane, and describe how a control engineer can read approximate time-domain performance from a pole location without solving the differential equation."
  type: short-answer
  answer: "Poles of a standard second-order system lie on a circle of radius ωₙ centered at the origin. The angle θ from the negative real axis satisfies ζ = cos(θ). From these two geometric quantities, all key time-domain metrics follow: settling time ≈ 4/(ζωₙ) = 4/(real part magnitude); damped oscillation frequency ω_d = ωₙ√(1−ζ²) = imaginary part; percent overshoot = exp(−πζ/√(1−ζ²)) × 100, a function of ζ alone. A pole further from the origin (larger ωₙ) responds faster; a pole closer to the negative real axis (smaller angle, larger ζ) overshoots less."
  explanation: "This geometric view is the foundation of root-locus design: the designer specifies desired time-domain performance, converts it to a target region in the s-plane (e.g., a sector defined by minimum ζ and a vertical line defined by minimum decay rate), and then uses gain or compensator design to place poles in that region. The power of the ωₙ–ζ parameterization is that it makes the mapping between frequency-domain pole locations and time-domain behavior transparent and intuitive."
```

## Explainer

From your work on the characteristic equation, you know that closed-loop poles determine stability and the shape of transient response. For a second-order system — the most common prototype in control design — two parameters capture *all* the information about how the system responds: **natural frequency ωₙ** and **damping ratio ζ**. These are not just abstract mathematical quantities; they correspond directly to physical intuitions about speed and oscillation that engineers use to specify performance requirements.

The **undamped natural frequency ωₙ** is the frequency at which the system would oscillate if there were no damping at all (ζ = 0). Think of a mass-spring system with no friction — it oscillates forever at ωₙ = √(k/m). In control systems, ωₙ sets the *speed* of the system's response: higher ωₙ means faster response. When you want a system that reacts quickly to commands — a fast robot arm or a tight position servo — you want high ωₙ. The standard form denominator s² + 2ζωₙs + ωₙ² makes this explicit: ωₙ² appears as the constant term, so ωₙ = √(constant term) by inspection.

The **damping ratio ζ** controls the shape of the response — specifically, how much the system overshoots its target before settling. At ζ = 0, the system oscillates indefinitely with no decay. At ζ = 1 (critically damped), it reaches the target as fast as possible without overshooting. For 0 < ζ < 1 (underdamped), the system overshoots and oscillates, with smaller ζ producing more oscillation. The **percent overshoot** is determined solely by ζ: %OS = exp(−πζ/√(1−ζ²)) × 100. A damping ratio of 0.707 gives about 4.3% overshoot and is a common design target because it balances speed against overshoot. The poles of the standard-form transfer function sit at s = −ζωₙ ± jωₙ√(1−ζ²): the real part −ζωₙ governs the decay rate (and thus settling time), and the imaginary part ωₙ√(1−ζ²) is the **damped natural frequency ω_d** at which oscillations occur.

The geometric picture in the complex plane is powerful. The poles lie on a circle of radius ωₙ centered at the origin. The angle from the negative real axis to the pole is θ = cos⁻¹(ζ) — so damping ratio is literally the cosine of the pole angle. A pole exactly on the negative real axis (θ = 0°) has ζ = 1 (critically damped). A pole at 45° from the negative real axis has ζ = cos(45°) ≈ 0.707. A pole near the imaginary axis has small ζ and oscillates heavily. This geometric relationship is the bridge between the characteristic equation's roots and time-domain performance specifications — you can look at a pole location in the s-plane and immediately read off the approximate overshoot, damped frequency, and settling time without solving the ODE.
