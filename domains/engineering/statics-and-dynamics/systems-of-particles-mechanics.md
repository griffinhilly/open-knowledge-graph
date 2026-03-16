---
id: systems-of-particles-mechanics
title: 'Systems of Particles: Center of Mass and Internal Forces'
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: center-of-mass-vs-centroid
  type: hard
- id: conservation-of-linear-momentum
  type: hard
builds-toward:
- rigid-body-kinetics-force-acceleration
tags:
- systems
- center-of-mass
- particle-systems
stage: formal-systems
status: draft
---

# Systems of Particles: Center of Mass and Internal Forces

## Core Idea
A system of particles behaves as though all its mass were concentrated at the center of mass, which accelerates according to the net external force (internal forces cancel by Newton's third law). This decomposition separates translational motion from internal dynamics, simplifying analysis of complex multi-body systems including rigid bodies.

## Explainer

You already know that the **center of mass** is the mass-weighted average position of a body, and that **linear momentum** is conserved when no external forces act. The system-of-particles result ties these together into a single principle with broad reach. When multiple particles interact — through springs, contact, tension, or any internal mechanism — the internal forces always come in action-reaction pairs (Newton's third law). Summing over all particles, every internal force has an equal and opposite counterpart within the system, and they cancel exactly. Internal forces cannot change the system's total momentum or accelerate the system's center of mass.

What remains is clean: **ΣF_ext = M · a_cm**, where M is total mass and a_cm is the acceleration of the center of mass. This is Newton's second law applied to the entire system, with internal forces gone. The center of mass moves exactly as though all the system's mass were concentrated there, subject only to external forces. A spinning wrench thrown across a room, a cluster of colliding billiard balls, a rocket expelling exhaust — in every case, the center of mass follows the trajectory dictated by external forces alone, no matter how complicated the internal dynamics.

This separation is what makes rigid body dynamics tractable. A rigid body is a system of infinitely many particles with internal stresses maintaining fixed relative positions. By the particle-system result, translational motion of the center of mass is governed by ΣF_ext = Ma_cm (external forces only), and rotational motion about the center of mass is governed by ΣM_cm = Iα (external torques only). The two equations decouple — you do not need to know the internal stresses to analyze gross translational and rotational motion.

The practical power is clearest in collision analysis. If you take two colliding objects as your system, the collision forces are internal and cancel. During the brief collision interval, external forces (gravity, friction) are small relative to the impulsive collision forces and can often be neglected. In that approximation, total system momentum is conserved — not because forces vanish, but because internal forces cancel and external impulses are negligible. The boundary you draw around the system determines what counts as internal, so choosing the system thoughtfully is the analytical skill at the heart of every multi-body problem.
