---
id: conservation-of-energy-mechanical-systems
title: Conservation of Mechanical Energy in Systems
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: work-energy-theorem-rigorous
  type: hard
- id: potential-energy-conservative-forces
  type: hard
- id: energy-conservation-applications
  type: hard
builds-toward:
- lagrangian-mechanics-overview
tags:
- energy
- conservation-laws
- mechanical-systems
stage: formal-systems
status: draft
---

# Conservation of Mechanical Energy in Systems

## Core Idea
When only conservative forces act on a mechanical system, total mechanical energy E = T + V (kinetic plus potential) remains constant. This scalar conservation law is often more useful than Newton's laws for solving complex problems, particularly when motion is constrained and constraint forces are unknown or irrelevant to the energy analysis.

## Explainer

From your work with the work-energy theorem and potential energy, you already know that a conservative force is one where the work it does depends only on start and end position, not on the path taken — gravity and springs are the canonical examples. The energy conservation law in mechanics is the direct consequence: if every force doing work on a system is conservative, then whatever kinetic energy is lost as an object slows down must be stored as potential energy, and vice versa. The sum E = T + V never changes. This is not a new physical principle; it is a special case of the work-energy theorem when all work comes from conservative forces.

The power of this scalar law becomes clearest when you compare it to Newton's second law approach. Newton's laws give you vector equations — often three coupled differential equations — and to use them you must track every force including constraint forces like normal forces and tension. In many problems, those constraint forces do no work (they act perpendicular to motion), so you do not care what they are, yet you still have to carry them through Newton's equations. Energy conservation skips all of that. You write the energy at one instant equal to the energy at another instant: T₁ + V₁ = T₂ + V₂. The constraint forces never appear. A bead constrained to slide on a frictionless wire, a pendulum swinging on a massless rod, a ball rolling down a curved surface — all of these yield to a single scalar equation that Newton's approach would make far more laborious.

The critical word is **conservative**: this law fails the moment friction, air resistance, or any non-conservative force does work on the system. When those forces are present, energy is lost from the mechanical system (converted to heat), and T + V is no longer constant. In that case, you must return to the work-energy theorem and account for the work done by non-conservative forces: T₁ + V₁ + W_{nc} = T₂ + V₂. Conservation of mechanical energy is the zero-non-conservative-work special case of this more general statement.

Building toward Lagrangian mechanics, which is your next topic, it helps to see conservation of energy as the first hint of a deeper truth: the equations of motion for a mechanical system can be derived entirely from its energy, without ever writing force vectors. The **Lagrangian** L = T − V encodes all the dynamics, and the Euler-Lagrange equations extract them. Conservation of mechanical energy is the gateway to that more powerful formulation — and the physical intuition is the same: describe a system by how its energies trade off, and the motion follows.
