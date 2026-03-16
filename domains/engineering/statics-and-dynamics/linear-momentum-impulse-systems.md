---
id: linear-momentum-impulse-systems
title: Linear Momentum and Impulse in Systems
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: particle-dynamics-accelerated-motion
  type: hard
- id: impulse-momentum-particles
  type: soft
builds-toward:
- collision-energy-analysis
tags:
- momentum
- impulse
- conservation
- impact
- force-time
- collisions
stage: formal-systems
status: draft
---

# Linear Momentum and Impulse in Systems

## Core Idea
Linear momentum p = mv is conserved when external forces are zero, and changes by impulse (force integrated over time): Δp = ∫F dt. This principle is especially useful for collision analysis, explosions, and impact problems where forces are large but contact time is short, making impulse-momentum methods more practical than detailed force-acceleration analysis.

## Explainer

From your work on particle dynamics, you know that F = ma describes how a single particle responds to a net force. Momentum reformulates this as p = mv, and Newton's second law becomes F = dp/dt — force is the rate of change of momentum. This reframing is subtle but powerful: it generalizes naturally from a single particle to a system of particles, and it opens a different path to solving problems where you do not know the internal forces.

The key idea for a system is to separate internal forces (which particles in the system exert on each other) from external forces (which come from outside the system). Internal forces always occur in Newton's-third-law pairs: if particle A pushes particle B with force F, then B pushes A with −F. When you sum up all forces across the entire system, internal forces cancel in pairs. What remains is the **net external force**. This gives the system momentum principle: F_ext = dP/dt, where P = Σm_i*v_i is the total linear momentum of the system. If the net external force is zero, P is constant — **conservation of linear momentum**.

The **impulse-momentum theorem** follows directly: ∫F dt = ΔP, where the left side is the **impulse** J, a force integrated over time. This form is most useful during collisions and impacts, where the contact forces are extremely large, the contact duration Δt is extremely short, but the product F·Δt (the impulse) is finite and measurable. In these situations, you cannot integrate F(t) directly because you do not know the detailed force-time profile inside the contact. But if you can measure initial and final velocities, you know ΔP and therefore J without needing that detail. Explosions work the same way: the internal blast forces are immense and brief, but if external impulse is negligible over that short interval, momentum is conserved across the event.

A useful analogy: impulse is to momentum what work is to kinetic energy. Work (∫F·dx) tells you how much a force changes the energy of a particle as it moves through space. Impulse (∫F dt) tells you how much a force changes the momentum of a particle as time passes. Both are integrals of force, but over different independent variables, and each connects to a different conserved quantity. When you have a collision problem, momentum methods are natural; when you have a path-dependent problem, energy methods may be cleaner. Choosing between work-energy and impulse-momentum is a skill that develops with practice — look for what is conserved (or what can be calculated) with the given information, and choose the framework that eliminates the unknowns you cannot measure.
