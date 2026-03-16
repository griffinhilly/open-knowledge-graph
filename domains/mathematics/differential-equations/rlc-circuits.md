---
id: rlc-circuits
title: RLC Circuit Applications of Differential Equations
domain: mathematics
course: differential-equations
prerequisites:
- id: second-order-linear-homogeneous-odes
  type: hard
- id: damping-and-resonance
  type: soft
builds-toward:
- laplace-transform-of-derivatives
tags:
- application
- electrical-circuits
- modeling
stage: formal-systems
status: draft
---

# RLC Circuit Applications of Differential Equations

## Core Idea
In an RLC circuit with resistance R, inductance L, and capacitance C, Kirchhoff's voltage law gives L·i'' + R·i' + i/C = V'(t), analogous to the damped spring-mass equation. Solving this ODE predicts transient currents and steady-state response to AC sources.

## How It's Best Learned
Derive the circuit equation from Kirchhoff's laws: V_R + V_L + V_C = V_applied. Identify analogies with mechanical systems: L↔m, R↔c, 1/C↔k. Solve for underdamped and overdamped responses.

## Common Misconceptions
- Confusing voltage across the capacitor (∫i dt / C) with current; the signs matter. - Forgetting the R·i term or misinterpreting its role as energy dissipation. - Not recognizing the mechanical-electrical duality, missing intuition from one domain to the other.

## Explainer

From **second-order linear homogeneous ODEs**, you know how to solve equations of the form ay'' + by' + cy = 0 and how the nature of the characteristic roots — real and distinct, repeated, or complex conjugate — determines whether solutions decay monotonically, decay with critical damping, or oscillate. The RLC circuit is a direct physical realization of exactly this equation, letting you see those three cases play out in measurable voltages and currents.

Applying **Kirchhoff's voltage law** around a series RLC circuit says the voltage drops must sum to the applied voltage: V_R + V_L + V_C = V(t). The component voltage laws are: V_R = Ri (resistor), V_L = L·di/dt (inductor), V_C = q/C = (1/C)∫i dt (capacitor, where q is charge). Differentiating the whole equation with respect to time to work in terms of current i gives **L·i'' + R·i' + (1/C)·i = V'(t)**. This is a second-order linear ODE for i(t) with constant coefficients — precisely the form you solved abstractly, now grounded in physical components. The characteristic equation is Lλ² + Rλ + 1/C = 0.

The **mechanical-electrical duality** is the key intuition bridge. Compare L·i'' + R·i' + (1/C)·i = 0 with the damped spring-mass equation m·x'' + c·x' + k·x = 0. The correspondence is: inductance L ↔ mass m (both resist changes in their respective "flow"), resistance R ↔ damping constant c (both dissipate energy), and 1/C ↔ spring constant k (both provide a restoring force proportional to accumulated displacement or charge). The three qualitative behaviors map perfectly: an **overdamped** circuit (R² > 4L/C) has two real characteristic roots and current decays exponentially without oscillation — like a heavy mass in thick oil. An **underdamped** circuit (R² < 4L/C) has complex roots and produces **ringing** — oscillations that decay exponentially, like a plucked string. A **critically damped** circuit (R² = 4L/C) decays as fast as possible without oscillating — like a car door that closes quickly but without bouncing.

For a driven circuit with AC voltage V(t) = V₀cos(ωt), the particular solution (the **steady-state response**) has the same frequency ω as the driving voltage but may differ in amplitude and phase. **Resonance** occurs when the driving frequency matches the circuit's natural frequency ω₀ = 1/√(LC) — the same condition as mechanical resonance, for the same mathematical reason. At resonance, the impedance from the inductor and capacitor cancel, leaving only the resistance to limit current, so current amplitude is maximized. This principle underlies radio tuning: adjusting C changes ω₀ until it matches the frequency of a desired station.
