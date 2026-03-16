---
id: radiation-reaction-and-self-force
title: Radiation Reaction and Self-Force
domain: physics
course: electrodynamics
prerequisites:
- id: larmor-formula
  type: hard
- id: radiation-accelerating-charges
  type: hard
builds-toward:
- synchrotron-radiation
tags:
- radiation-reaction
- abraham-lorentz
- self-force
stage: advanced
status: draft
---

# Radiation Reaction and Self-Force

## Core Idea
The radiation reaction force (or Abraham-Lorentz force) accounts for the momentum lost when a charged particle radiates, modifying its equation of motion. This non-relativistic force is F_rad = (q²/6πε₀c³)da/dt (proportional to the time derivative of acceleration). The relativistic generalization reveals subtle issues like pre-acceleration and indicates the breakdown of classical electrodynamics at extremely short timescales, hinting at the need for quantum mechanics.

## Explainer

From the Larmor formula you know that an accelerating charge radiates power P = q²a²/(6πε₀c³). That energy has to come from somewhere. If an external force is pushing the charge and causing the acceleration, then part of the work done by that force must go into radiation rather than into the kinetic energy of the particle. This deficit appears as a recoil-like effect on the particle — the **radiation reaction force**, also called the **Abraham-Lorentz force**.

To derive it, consider energy conservation: the total power delivered by all forces must equal the rate of change of kinetic energy plus the radiated power. Working through the math — integrating by parts to express the Larmor power in terms of the charge's trajectory — yields the Abraham-Lorentz force F_rad = (μ₀q²/6πc)·ȧ, where ȧ = da/dt is the **jerk** (time derivative of acceleration). This is startling: the self-force depends not on acceleration but on the rate of change of acceleration. In Newtonian mechanics, force causes acceleration; here we have a force that depends on how acceleration is changing.

This dependence on jerk leads to deeply troubling consequences. The equation of motion m·a = F_ext + F_rad, when written explicitly, is a third-order differential equation in position (position → velocity → acceleration → jerk). Third-order equations require three initial conditions, not two. One family of solutions shows **runaway acceleration**: a free particle with no external force spontaneously accelerates exponentially, which is unphysical. Another family shows **pre-acceleration**: a particle begins to accelerate slightly before the external force is applied, violating causality. Both pathologies indicate that classical point-charge electrodynamics is internally inconsistent at very short timescales — specifically at the classical electron radius r_e = q²/(4πε₀mc²) ≈ 2.8 × 10⁻¹⁵ m, where the self-energy of the electron equals its rest mass energy.

The resolution requires quantum electrodynamics (QED). In QED, the classical divergences are regularized by the discrete photon nature of radiation and by renormalization, which absorbs infinite self-energy into the definition of the measured mass. Practically, for most applications where accelerations change slowly compared to the timescale r_e/c ≈ 10⁻²³ s, the Abraham-Lorentz force is a small perturbative correction and can be used safely. The lesson of radiation reaction is profound: classical electrodynamics applied to point particles is not a closed, self-consistent theory — it already contains the seeds of its own replacement by quantum field theory.
