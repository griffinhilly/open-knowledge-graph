---
id: magnetic-torque-dipole
title: Torque on Magnetic Dipoles
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: magnetic-force-current-wires
  type: hard
builds-toward:
- inductance-circuits-rl-transients
tags:
- torque
- dipole
- rotation
stage: formal-systems
status: draft
---

# Torque on Magnetic Dipoles

## Core Idea
A current loop with magnetic moment μ = IA (A is area vector) in field B experiences torque τ = μ × B. Torque tends to align the dipole with the field. Potential energy is U = −μ⋅B.

## Explainer

From your study of magnetic forces on current-carrying wires, you know that a wire of length L carrying current I in a field B experiences force F = IL × B. A rectangular current loop in a uniform magnetic field extends this idea: opposite sides carry opposite current directions, so they experience opposite forces. In a uniform field these forces cancel out as net force — the loop doesn't translate. But they don't act on the same line, so they create a **torque** that tends to rotate the loop.

The quantity that characterizes the loop's response to an external magnetic field is the **magnetic dipole moment** μ = IA, where I is the current and A is the area vector (magnitude = loop area, direction given by the right-hand rule relative to the current flow). The torque is τ = μ × B. The cross product means torque is zero when μ is parallel to B (the equilibrium orientation) and maximum when μ is perpendicular to B. The direction of the torque always acts to rotate μ toward alignment with B — just as a compass needle rotates toward north.

The **potential energy** U = −μ⋅B = −μB cos θ completes the picture. When μ is antiparallel to B (θ = 180°), U = +μB — the highest energy state. When μ is parallel to B (θ = 0°), U = −μB — the lowest energy state. A dipole released from any orientation will oscillate about the aligned configuration (or relax to it if there's damping), exactly like a pendulum swinging toward equilibrium. The energy difference between aligned and antialigned states is 2μB, which appears in many physical contexts: this is the energy cost of flipping an atomic magnetic moment in an external field, the basis of magnetic resonance and the Zeeman effect.

The magnetic dipole is the magnetic analog of the electric dipole. Both feel torques (τ = p × E electrically, τ = μ × B magnetically) and both have potential energy minimized when aligned with the field. The difference is that magnetic dipoles arise from circulating currents, not separated charges — but the mathematical structure is identical. This parallel runs deep: it underlies the similarity between electric and magnetic terms in Maxwell's equations and explains why magnetic materials (with atomic current loops) behave so analogously to dielectric materials (with electric dipoles) when placed in external fields.
