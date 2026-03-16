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
- id: differential-equations-intro-separable
  type: hard
- id: second-order-linear-homogeneous-odes
  type: hard
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
status: validated
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

## Explainer

You know from first-order transient circuits that an RC or RL circuit responds to a sudden change with a single exponential decay — one time constant, one initial condition, one characteristic root. Adding a second energy-storage element (a capacitor and an inductor together in an RLC circuit) introduces a second degree of freedom. The circuit now has "memory" in two variables simultaneously — energy stored in the electric field of the capacitor and energy stored in the magnetic field of the inductor. The mathematical description becomes a second-order ODE, and its solutions are qualitatively richer than a simple exponential.

Applying KVL around a series RLC loop after a switch opens or closes gives a second-order differential equation in, say, the capacitor voltage v_C. After pulling out the standard form, you identify two parameters: the **undamped natural frequency** ω₀ = 1/√(LC) and the **damping coefficient** α = R/(2L). The ratio ζ = α/ω₀ is the **damping ratio**. To solve, you write the **characteristic equation** s² + 2αs + ω₀² = 0 and find its roots s = −α ± √(α² − ω₀²). The nature of these roots determines the qualitative behavior — and the three cases correspond to three physically distinct phenomena.

When ζ > 1 (**overdamped**), α > ω₀, the discriminant is positive, and you get two distinct real negative roots s₁ and s₂. The solution is a sum of two decaying exponentials: v_C(t) = A₁ e^(s₁t) + A₂ e^(s₂t). The circuit returns to equilibrium monotonically — no oscillation, but more slowly than a critically damped system. When ζ = 1 (**critically damped**), the two roots are equal (s = −α), and the solution takes the special form (A₁ + A₂t) e^(−αt). This is the fastest possible return to equilibrium without oscillation — the engineering sweet spot for applications requiring speed without overshoot, like certain door closers or servo drives. When ζ < 1 (**underdamped**), the roots are complex conjugates s = −α ± jω_d where the **damped natural frequency** ω_d = √(ω₀² − α²). The solution is a decaying sinusoid: e^(−αt) (B₁ cos(ω_d t) + B₂ sin(ω_d t)). The circuit oscillates, with amplitude shrinking exponentially. The oscillation frequency is ω_d, which is always slightly less than ω₀ because damping slows the oscillation.

The two initial conditions — v_C(0⁺) and dv_C/dt(0⁺) — are required to find A₁, A₂ (or B₁, B₂). The first comes from the capacitor voltage continuity rule (v_C cannot jump). The second requires you to apply KVL or KCL at t = 0⁺ to find the initial inductor current, then use the capacitor's defining relation i_C = C dv_C/dt to get the derivative. This two-step initial condition procedure is the most common source of errors in second-order transient analysis.
