---
id: cyclotron-motion-and-frequency
title: Cyclotron Motion and Frequency
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: lorentz-force-on-moving-charge
  type: hard
- id: circular-motion-kinematics
  type: hard
builds-toward:
- synchrotron-radiation
tags:
- magnetism
- circular motion
- charged particles
stage: formal-systems
status: draft
---

# Cyclotron Motion and Frequency

## Core Idea
A charged particle moving perpendicular to a uniform magnetic field undergoes circular motion with radius r = mv/(qB) and frequency f_c = qB/(2πm). The cyclotron frequency is independent of velocity and radius. This principle underlies cyclotron accelerators and is fundamental to plasma physics.

## How It's Best Learned
Derive the radius and frequency from Newton's second law for circular motion under Lorentz force. Trace trajectories of particles entering at different angles and speeds.

## Common Misconceptions
- Cyclotron frequency depends on velocity (it depends only on q, m, and B).
- Particles spiral outward in uniform fields (they move in circles at constant radius if v ⊥ B).
- Gyroradius is related to wavelength in the same way as in other contexts (it is not).

## Explainer

Start from the two things you already know: the **Lorentz force** on a moving charge in a magnetic field, F = qv × B, is always perpendicular to the velocity; and from circular motion kinematics, a perpendicular force causes circular motion, requiring a centripetal force F = mv²/r directed inward. Cyclotron motion is simply what happens when these two facts collide. A charged particle moving perpendicular to a uniform magnetic field experiences a constant-magnitude force always pointed toward the center of its circular path — the magnetic force *is* the centripetal force.

Setting qvB = mv²/r and solving for the **gyroradius**: r = mv/(qB). Faster particles make larger circles; heavier particles make larger circles; stronger fields or larger charges make smaller circles. This formula is completely intuitive — radius grows with momentum and shrinks with the field's ability to bend the trajectory. Now compute the period: the particle must travel the circumference 2πr at speed v, so T = 2πr/v = 2πm/(qB). Notice that v cancels entirely. The **cyclotron frequency** f_c = qB/(2πm) depends only on the charge-to-mass ratio and field strength — not on the particle's speed.

This velocity-independence is the key insight. A slow proton and a fast proton in the same field trace circles of different sizes, but complete their orbits in exactly the same time. This is why cyclotron accelerators work: you can apply an alternating electric field at a fixed frequency and it stays in sync with the orbiting particles even as they gain energy and spiral outward. The timing never drifts because the orbital period is constant — a feature that makes the cyclotron elegantly self-synchronizing up to relativistic speeds (where the mass effectively increases and the synchrony breaks, requiring the synchrotron's variable-frequency correction).

In plasma physics, the same result defines the **Larmor radius** (gyroradius) and the **gyrofrequency** — quantities that appear throughout the description of plasma confinement, magnetic mirrors, and aurora formation. Any time charged particles travel through a magnetic field — from particle detectors to the Van Allen belts to the interior of tokamaks — the cyclotron motion framework is the first tool you reach for. The derivation is simple, the result is exact (in the non-relativistic limit), and its implications extend across an enormous range of physics.
