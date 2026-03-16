---
id: radiation-reaction-force
title: Radiation Reaction Force (Abraham-Lorentz Force)
domain: physics
course: electrodynamics
prerequisites:
- id: larmor-formula
  type: hard
- id: classical-mechanics
  type: soft
builds-toward:
- synchrotron-radiation
tags:
- radiation-reaction
- abraham-lorentz
stage: abstract-reasoning
status: draft
---

# Radiation Reaction Force (Abraham-Lorentz Force)

## Core Idea
A radiating charge experiences recoil force (radiation reaction) opposing acceleration: F_rad = (q²ȧ)/(6πε₀c³). This self-force arises from the charge's own electromagnetic field. The Abraham-Lorentz equation of motion includes this force and shows energy loss proportional to the square of acceleration.

## Explainer

The Larmor formula tells you that an accelerating charge radiates power P = q²a²/(6πε₀c³). This radiated energy must come from somewhere — energy is conserved. If the charge loses kinetic energy to radiation, some force must be doing negative work on it. That force is the **radiation reaction force** (also called the Abraham-Lorentz force or self-force). Its existence is not an assumption but a logical necessity: whatever external field is accelerating the charge cannot simultaneously drain its kinetic energy into radiation. The radiation reaction force is the mechanism by which the field "pays back" the charge for the energy it emits.

Deriving this force by integrating the charge's own electromagnetic field over itself yields the **Abraham-Lorentz formula**: F_rad = (μ₀q²/6πc) · da⃗/dt = (q²/6πε₀c³) · ȧ⃗, where ȧ = da/dt is the **jerk** — the time derivative of acceleration. The full equation of motion is then m ȧ⃗ = F_external + F_rad. The dependence on *jerk* rather than velocity or acceleration is immediately strange from a classical mechanics standpoint: Newton's laws involve up to second derivatives of position, but this introduces a third. This changes the mathematical character of the equation completely, requiring not just initial position and velocity, but also initial acceleration to specify the solution.

The Abraham-Lorentz equation has alarming pathologies. First, **runaway solutions**: even with no external force, the equation admits solutions where acceleration grows exponentially — the particle accelerates itself into infinity. Second, **pre-acceleration**: to avoid runaway solutions, one must impose a boundary condition that forces the particle to "know" about an applied force before it arrives — causality appears to be violated at the scale of the classical electron radius r_e = q²/(4πε₀mc²) ≈ 2.8 × 10⁻¹⁵ m. Both pathologies signal that classical electrodynamics is pushing beyond its domain of validity at scales where quantum mechanics matters.

The deeper lesson is that a point charge in classical electrodynamics is fundamentally problematic: its own field diverges at its location, and the self-energy is infinite. The radiation reaction force is one manifestation of this self-energy problem. Quantum electrodynamics handles it through renormalization — absorbing infinite self-energy terms into the measured mass and charge — but the problem of a fully consistent, finite description of a classical radiating point charge remains conceptually unresolved. The Abraham-Lorentz force is therefore both a practical tool (it correctly predicts average energy loss in, e.g., synchrotron radiation) and a warning about the limits of the classical theory.
