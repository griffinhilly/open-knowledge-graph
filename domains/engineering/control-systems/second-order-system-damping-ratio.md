---
id: second-order-system-damping-ratio
title: 'Second-Order System Response: Damping Ratio and Natural Frequency'
domain: engineering
course: control-systems
prerequisites:
- id: first-order-system-transient-response
  type: hard
- id: second-order-systems-resonance
  type: soft
builds-toward:
- compensation-design-tradeoffs-cascadefeedback
tags:
- second-order
- damping-ratio
- natural-frequency
- underdamped
- overdamped
stage: advanced
status: draft
---

# Second-Order System Response: Damping Ratio and Natural Frequency

## Core Idea
Second-order systems are characterized by natural frequency ωₙ and damping ratio ζ. Overdamped (ζ>1): slow, no overshoot; critically damped (ζ=1): fastest without overshoot; underdamped (ζ<1): fast but with overshoot and oscillation. Overshoot M_p ≈ e^(-πζ/√(1-ζ²)); settling time T_s ≈ 4/(ζωₙ).

## Explainer

From your study of first-order systems, you know that a single energy storage element (an RC circuit, a thermal mass, a motor with inertia but no spring) produces a step response that rises exponentially toward its final value with a single **time constant** τ. There is no overshoot — the response is purely monotonic, and the only design parameter is how fast or slow it settles. A **second-order system** adds another energy storage element, which allows the two elements to exchange energy back and forth. This exchange is what produces oscillation, and the interplay between energy exchange and dissipation creates the rich family of responses characterized by **natural frequency ωₙ** and **damping ratio ζ**.

Think of a spring-mass-damper system as the mechanical archetype. The spring stores potential energy; the mass stores kinetic energy; they constantly trade energy back and forth. Without a damper (ζ = 0), the mass oscillates forever at exactly ωₙ — the **natural frequency**. Add a damper (friction) and some energy is removed each cycle. The damping ratio ζ measures how much energy is dissipated per cycle relative to the energy stored. When ζ < 1 (**underdamped**), the system oscillates but the oscillations shrink each cycle, eventually settling to the final value. When ζ = 1 (**critically damped**), dissipation is just strong enough to prevent oscillation — the fastest possible settling without any overshoot. When ζ > 1 (**overdamped**), dissipation dominates; no oscillation occurs, but settling is slower than the critically damped case because the two real poles are widely separated and the slower one limits the response.

The **pole locations** in the complex plane make this vivid. The two poles are at s = −ζωₙ ± jωₙ√(1−ζ²). For underdamped systems (ζ < 1), the poles are complex conjugates: the real part −ζωₙ sets the exponential decay envelope, and the imaginary part ωₙ√(1−ζ²) — called the **damped natural frequency ωd** — sets the oscillation frequency. Moving the poles straight left (increasing ζωₙ) speeds up settling. Moving the poles upward (decreasing ζ toward zero) increases oscillation frequency but also increases overshoot. The poles sit on a circle of radius ωₙ: increasing ωₙ scales the whole response faster without changing the shape. The angle from the negative real axis is arccos(ζ): a 45° angle corresponds to ζ ≈ 0.707, often used as a design target for moderate overshoot (~4.3%) with reasonable speed.

The **performance specifications** connect directly to ζ and ωₙ. Percent overshoot depends only on ζ: M_p ≈ e^(−πζ/√(1−ζ²)) × 100%. A target overshoot of 5% → ζ ≈ 0.69; 20% → ζ ≈ 0.46. Settling time (±2% of final value) is approximately 4/(ζωₙ). So for a given overshoot target (which fixes ζ), you can meet any settling time requirement by choosing ωₙ = 4/(ζ·T_s). This clean separation — ζ controls shape, ωₙ controls speed — is the fundamental design insight. When you design a controller to meet transient specifications, you are essentially choosing a target location in the complex plane (a target ζ and ωₙ) and then designing the controller to place the dominant closed-loop poles there.
