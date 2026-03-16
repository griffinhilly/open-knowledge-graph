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

## Explainer

From your study of first-order systems, you know that a single time constant τ fully describes how fast a system approaches its final value — the response is always a decaying exponential, never oscillatory. A second-order system introduces a new possibility: the system can overshoot its target and ring back and forth before settling. This happens because a second-order system has energy storage in two different elements (think of a mass with both spring and dashpot), and those elements can exchange energy with each other. The two parameters that replace τ are the **natural frequency** ωₙ and the **damping ratio** ζ.

The natural frequency ωₙ sets the intrinsic speed of the system — how fast it would oscillate if there were no damping at all (ζ = 0). Think of it as the frequency of an undamped spring-mass system from your simple harmonic motion prerequisite. The damping ratio ζ measures how aggressively the system dissipates energy relative to that natural oscillation. When ζ = 0, the system oscillates forever. When ζ = 1 (**critically damped**), dissipation exactly prevents any overshoot. When ζ > 1 (**overdamped**), the system is sluggish — imagine a door closer in thick oil. The most practically useful regime is **underdamped** (0 < ζ < 1), where the system overshoots but settles quickly. The actual oscillation frequency you observe in the step response is the **damped natural frequency** ωd = ωₙ√(1−ζ²), which is always lower than ωₙ because damping slows the oscillations.

The performance metrics follow directly from ζ and ωₙ. **Percent overshoot** depends only on ζ: %OS = e^(−πζ/√(1−ζ²)) × 100. This is a pure function of ζ — if you want less than 5% overshoot, you need ζ > 0.69. **Peak time** Tₚ = π/ωd tells you when the first overshoot peak occurs — it decreases as ωd increases, meaning a faster (higher ωₙ) or less-damped system peaks sooner. **Settling time** Ts ≈ 4/(ζωₙ) depends on both parameters: to settle faster, you need either more damping or a higher natural frequency. This is the essential design tradeoff — ζ controls the overshoot; ωₙ scales the overall speed.

The value ζ ≈ 0.707 (= 1/√2) deserves special attention. It is not critically damped, but it achieves a near-optimal compromise: the step response is fast, the overshoot is only about 4.3%, and the settling is clean. Many practical specifications target this region. In the s-plane, increasing ωₙ moves the closed-loop poles radially outward (faster), while increasing ζ rotates them toward the negative real axis (less oscillatory). When you move to designing controllers like PID, every gain adjustment is really an attempt to place those poles at the right combination of ωₙ and ζ — so internalizing the relationship between pole location and these time-domain metrics is foundational to everything that follows.
