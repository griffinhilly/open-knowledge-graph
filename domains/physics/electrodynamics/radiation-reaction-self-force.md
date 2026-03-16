---
id: radiation-reaction-self-force
title: Radiation Reaction Force
domain: physics
course: electrodynamics
prerequisites:
- id: radiation-from-accelerated-charges
  type: hard
- id: larmor-formula
  type: hard
builds-toward:
- classical-electron-radius
- radiation-damping-radiation-reaction
tags:
- radiation-reaction
- self-force
- abraham-lorentz
- runaway-solutions
stage: advanced
status: draft
---

# Radiation Reaction Force

## Core Idea
A radiating charge experiences a self-force due to its own radiated field. The Abraham-Lorentz force F = (q²/6πε₀c³)a̍ opposes acceleration and causes energy loss. This leads to runaway solutions in classical theory, limiting applicability to cases where the radiation damping is perturbative.

## Explainer

From the Larmor formula and your study of radiation from accelerated charges, you know that an accelerating charge radiates electromagnetic energy at rate P = q²a²/(6πε₀c³). But where does this energy come from? It must come from the kinetic energy of the charge — the charge must be slowing down, or require extra force to maintain acceleration, due to the energy it is radiating away. This means the charge's own radiation field exerts a force back on the charge itself: the **radiation reaction force** or **self-force**. Capturing this force is one of the deepest and most troublesome problems in classical electrodynamics.

The result is the **Abraham-Lorentz force**: F_rad = (q²/6πε₀c³) ȧ, where ȧ = dā/dt is the **jerk** — the time derivative of acceleration. Notice the unusual structure: this force depends not on position, velocity, or even acceleration, but on the *rate of change* of acceleration. This makes physical sense dimensionally — we need a force that drains power P = F·v proportional to a², and working backwards from the Larmor formula to find a force F such that F·v = −P leads directly to this expression involving ȧ. The coefficient q²/(6πε₀c³) = (2/3)(r_e/c) involves the **classical electron radius** r_e = q²/(4πε₀m_ec²), a characteristic length scale that marks where classical electrodynamics breaks down.

The trouble with this force is that it generates pathological solutions. The equation of motion m·a = F_external + F_rad becomes a third-order ODE in position (since ȧ = d³r/dt³). Third-order ODEs require three initial conditions, and specifying the initial position and velocity is not enough — you must also specify the initial acceleration. This over-specification leads to **runaway solutions**: even with no external force, a free particle can spontaneously accelerate exponentially, with radiation reaction providing positive feedback rather than damping. This is unphysical and signals a fundamental breakdown of the classical point-charge model at very short distance scales (below r_e ≈ 2.8 × 10⁻¹⁵ m for electrons, where quantum effects dominate).

In practice, the Abraham-Lorentz force is only used perturbatively. When the radiation damping is small compared to the applied force (the radiation power is much less than the applied force times the velocity), the runaway instability is suppressed and the equation gives sensible results. For example, an oscillating charge loses energy to radiation, and the damping can be treated as a small correction to the oscillation. This perturbative approach underlies the classical theory of spectral line widths and the damping of antenna radiation. The full resolution of the self-force problem requires quantum electrodynamics, where mass renormalization absorbs the divergent self-energy and the Abraham-Lorentz pathology disappears — a key motivation for the development of quantum field theory.
