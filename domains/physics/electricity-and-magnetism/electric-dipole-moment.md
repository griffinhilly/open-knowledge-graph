---
id: electric-dipole-moment
title: Electric Dipoles and Dipole Moment
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: equipotential-surfaces
  type: soft
- id: electric-potential-field
  type: hard
builds-toward:
- dielectric-polarization
tags:
- dipole
- moment
- polarization
stage: formal-systems
status: draft
---

# Electric Dipoles and Dipole Moment

## Core Idea
An electric dipole consists of charges +q and −q separated by distance d, with dipole moment p⃗ = qd⃗. In a uniform external field, a dipole experiences torque τ⃗ = p⃗ × E⃗ and has potential energy U = −p⃗·E⃗. Far from a dipole, the potential falls as V ∝ cos(θ)/r², defining the dipole field pattern.

## Explainer

From your study of electric potential, you know that a single point charge produces a potential V = kq/r that falls as 1/r. An **electric dipole** — a pair of equal and opposite charges +q and −q separated by a small distance d — is the next level of complexity. At large distances, the positive and negative contributions to the potential nearly cancel, but not perfectly: the small offset between the charges creates a residual potential proportional to 1/r². This faster falloff is the defining signature of the dipole.

The **dipole moment** p⃗ = qd⃗ captures both the strength and orientation of the dipole in a single vector: it points from the negative charge to the positive charge, and its magnitude is qd. The far-field potential is V = (1/4πε₀) · (p⃗ · r̂)/r² = (1/4πε₀) · p cos(θ)/r², where θ is measured from the dipole axis. Notice that the potential is maximum along the axis (θ = 0), zero in the perpendicular plane (θ = 90°), and most negative anti-parallel to p⃗. The corresponding electric field lines form the classic two-lobed dipole pattern you have likely seen: field lines emerge from the positive charge, arc around, and terminate on the negative charge.

When a dipole is placed in an **external electric field** E⃗, the two charges experience equal and opposite forces that sum to zero — so there is no net force in a uniform field — but they create a net torque τ⃗ = p⃗ × E⃗ that tends to align p⃗ with E⃗. The potential energy of this alignment is U = −p⃗ · E⃗. When p⃗ is parallel to E⃗, U is at its minimum (most stable); antiparallel gives maximum U (unstable equilibrium). This torque-and-alignment physics governs the behavior of polar molecules in electric fields — a water molecule, for instance, acts as a permanent dipole that orients itself in response to applied fields.

The dipole model is not just a textbook abstraction. It is the first term in the **multipole expansion** of any charge distribution: every localized charge distribution can be described at large distance as a sum of a monopole (net charge), dipole, quadrupole, and so on. If the net charge is zero, the dipole term dominates at large r. This framework connects directly to **dielectric polarization** — your next topic — where dipole moments induced in atoms and molecules by an external field collectively modify how the material responds to electric fields.
