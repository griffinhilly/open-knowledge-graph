---
id: orbital-energy-and-escape-velocity
title: Orbital Energy and Escape Velocity
domain: physics
course: classical-mechanics
prerequisites:
- id: gravitational-potential-energy-extended
  type: hard
- id: conservation-of-energy
  type: hard
builds-toward:
- orbital-elements-and-trajectories
tags:
- gravitation
- orbits
- energy
- escape-velocity
stage: formal-systems
status: draft
---

# Orbital Energy and Escape Velocity

## Core Idea
A bound circular orbit at radius r has total energy E = −G M m / (2r), entirely determined by the semi-major axis. Escape velocity v_esc = √(2 G M / R) is the minimum speed at Earth's surface to reach infinity with v = 0 (E = 0). For any object, the relationship between E, v, and r determines orbit type: elliptical (E < 0), parabolic (E = 0), or hyperbolic (E > 0).

## Explainer

You already know that gravitational potential energy takes the form **U = −GMm/r**, where the potential energy is zero at infinite separation and becomes increasingly negative as objects approach. You also know conservation of energy: in any closed system with only conservative forces, the total mechanical energy E = KE + PE remains constant. Orbital mechanics is the application of these two ideas to motion in gravitational fields — and the total energy turns out to classify everything about the orbit.

Start with a simple circular orbit at radius r. For a circular orbit, the gravitational force provides exactly the centripetal acceleration: GMm/r² = mv²/r, giving v² = GM/r and hence kinetic energy KE = GMm/(2r). The potential energy is U = −GMm/r. Total energy: E = KE + U = GMm/(2r) − GMm/r = **−GMm/(2r)**. Notice two things. First, the total energy is negative — the object is **bound** to the central body, just as we say a ball at the bottom of a well has negative potential energy relative to ground level. Second, the kinetic energy is exactly −½ times the potential energy (E = ½U): this is the **virial theorem** for gravitational systems, and it holds for all bound orbits on average, not just circular ones.

Escape velocity follows immediately from conservation of energy. If you launch an object with just enough speed to reach infinity (where both KE and PE are zero), the total energy of the trajectory must equal zero. Setting E = 0: ½mv² − GMm/R = 0, so **v_esc = √(2GM/R)**. At Earth's surface, this gives ≈ 11.2 km/s. This is the minimum launch speed *in the absence of atmosphere* for a projectile — not a rocket, which can fire continuously. The direction doesn't matter for escape velocity because gravity is a conservative force; only the speed at launch determines whether the object escapes, and it doesn't need to follow any particular path.

The total energy determines orbit *type* as well as orbit *size*. If E < 0, the object cannot escape — it's bound — and the orbit is an ellipse (circular orbits are the special case where the ellipse has zero eccentricity). If E = 0, the object barely escapes, arriving at infinity with zero velocity, and the trajectory is a **parabola**. If E > 0, the object escapes with kinetic energy to spare and follows a **hyperbola** — this is the trajectory of a comet making a one-time pass through the solar system, or a spacecraft executing a gravitational slingshot. In each case, the semi-major axis a is determined by E alone: **E = −GMm/(2a)** for bound orbits, which is why all ellipses with the same semi-major axis have the same period (Kepler's third law) regardless of their eccentricity.
