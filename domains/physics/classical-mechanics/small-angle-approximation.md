---
id: small-angle-approximation
title: Small Angle Approximation in Mechanics
domain: physics
course: classical-mechanics
prerequisites:
- id: physical-pendulum-dynamics
  type: hard
- id: simple-harmonic-motion
  type: soft
tags:
- approximations
- oscillations
- linearization
stage: formal-systems
status: draft
---

# Small Angle Approximation in Mechanics

## Core Idea
For small angles θ, sin(θ) ≈ θ and cos(θ) ≈ 1 convert nonlinear equations into linear ones. This approximation is essential for treating oscillating systems as simple harmonic, enabling analytical solutions.

## Explainer

From your study of the physical pendulum, you arrived at the equation of motion by applying Newton's second law for rotation: the restoring torque is τ = -mg·L·sin(θ), giving d²θ/dt² = -(g/L)·sin(θ). This is a **nonlinear** differential equation — the presence of sin(θ) rather than θ makes it analytically intractable for large amplitudes. No closed-form solution exists. The small-angle approximation is the key that transforms this equation into one you already know how to solve.

The approximation rests on the **Taylor expansion** of sin(θ) around θ = 0 (with θ in radians): sin(θ) = θ − θ³/6 + θ⁵/120 − ⋯. For small θ, each successive term is far smaller than the previous one. At θ = 0.1 rad (about 5.7°), the first dropped term θ³/6 ≈ 0.000167 — less than 0.2% of θ itself. We simply discard all terms beyond first order, leaving **sin(θ) ≈ θ**. Similarly, cos(θ) = 1 − θ²/2 + ⋯, so **cos(θ) ≈ 1** for small θ. The entire approximation depends on working in radians, where the small-angle series has this clean form — in degrees, none of this works.

Substituting sin(θ) ≈ θ into the pendulum equation gives d²θ/dt² = −(g/L)·θ. This is precisely the **simple harmonic oscillator** equation d²x/dt² = −ω²x, with ω = √(g/L). The solution is θ(t) = A·cos(ωt + φ), a sinusoidal oscillation with period T = 2π/ω = 2π√(L/g). Two things follow immediately. First, the pendulum oscillates sinusoidally for small amplitudes — which you already knew from SHM. Second, and crucially, the period is **independent of amplitude** A. This is isochrony: a pendulum swinging through a 5° arc and one swinging through a 10° arc have the same period (approximately). This is why pendulum clocks work — as the clock winds down and the swing becomes smaller, the period barely changes, keeping accurate time.

The approximation's domain of validity is roughly θ < 15° (about 0.26 rad), where the error in sin(θ) ≈ θ stays below 1%. Beyond this, the period begins to depend on amplitude and corrections are needed. More broadly, the small-angle technique is an instance of **linearization** — replacing a nonlinear function with its linear approximation near an equilibrium point. This pattern recurs throughout physics: paraxial optics replaces sin(θ) ≈ θ to analyze lens systems; perturbation theory in quantum mechanics treats small Hamiltonians linearly; sound waves in a fluid are analyzed by linearizing the nonlinear fluid equations around equilibrium. Whenever you encounter a nonlinear system, the first question is always: is there a regime where nonlinearity is small, so I can linearize and get analytic results? The small-angle approximation is the simplest and most transparent example of this fundamental physical strategy.
