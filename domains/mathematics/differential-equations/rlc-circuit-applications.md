---
id: rlc-circuit-applications
title: RLC Circuit Applications and Electromagnetic Oscillations
domain: mathematics
course: differential-equations
prerequisites:
- id: resonance-and-damping
  type: hard
builds-toward:
- laplace-transform-definition
tags:
- applications
- circuits
- rlc
stage: formal-systems
status: draft
---

# RLC Circuit Applications and Electromagnetic Oscillations

## Core Idea
An RLC circuit with resistance R, inductance L, and capacitance C satisfies L(d²q/dt²) + R(dq/dt) + q/C = V(t), mathematically identical to the spring-mass equation. Inductance acts like mass, resistance like damping, and the reciprocal capacitance like spring stiffness. The same resonance, damping, and oscillation phenomena occur, connecting electrical engineering to mechanical vibrations.

## Explainer

The central insight here is that the differential equation governing an RLC circuit is **structurally identical** to the spring-mass-damper equation from your study of resonance and damping. The charge q on the capacitor satisfies L·q'' + R·q' + q/C = V(t), while the spring-mass equation is mx'' + bx' + kx = F(t). The correspondence is direct: inductance L plays the role of mass m (both resist changes in motion or current), resistance R plays the role of damping b (both dissipate energy), and 1/C plays the role of spring stiffness k (both provide a restoring force proportional to displacement or charge). Every phenomenon you understand from mechanical oscillations — resonance, overdamping, critical damping, steady-state response — has an exact electrical analog.

The homogeneous equation L·q'' + R·q' + q/C = 0 describes the **natural response**: what the circuit does after a sudden disturbance with no ongoing driving voltage. The characteristic equation Lλ² + Rλ + 1/C = 0 has roots λ = (−R ± sqrt(R² − 4L/C)) / 2L. When R² < 4L/C, the discriminant is negative, the roots are complex, and the solution is an oscillating sinusoid decaying at rate R/2L — the **underdamped** case, analogous to a pendulum in a thin fluid. When R² > 4L/C, the roots are real and negative — the **overdamped** case — and charge simply decays exponentially without oscillating. At R² = 4L/C exactly, the circuit is **critically damped**, decaying as fast as possible without oscillating.

The **resonant frequency** ω₀ = 1/sqrt(LC) is where the circuit oscillates most naturally in the absence of damping. When a sinusoidal driving voltage V(t) = V₀ cos(ωt) is applied, the steady-state amplitude is largest when ω ≈ ω₀. This is why tuning a radio works: adjusting the capacitor C changes ω₀ until it matches the broadcast frequency of a desired station, producing a large-amplitude response to that signal while others remain small. The sharpness of the resonance peak — how selective the circuit is — is governed by the **quality factor** Q = (1/R)·sqrt(L/C), exactly as in mechanical resonance.

The **Laplace transform**, which you will study next, provides the most powerful framework for analyzing these circuits. Rather than solving the differential equation directly, the Laplace transform converts differentiation into multiplication by s, turning the ODE into an algebraic equation in the complex frequency domain. The circuit's **transfer function** H(s) = 1/(Ls² + Rs + 1/C) captures all input-output behavior, and the circuit's response to any driving signal can be found by multiplying in the s-domain and inverting the transform — without solving differential equations by hand each time.
