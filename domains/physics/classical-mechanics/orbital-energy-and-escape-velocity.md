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
status: validated
---

# Orbital Energy and Escape Velocity

## Core Idea
A bound circular orbit at radius r has total energy E = −G M m / (2r), entirely determined by the semi-major axis. Escape velocity v_esc = √(2 G M / R) is the minimum speed at Earth's surface to reach infinity with v = 0 (E = 0). For any object, the relationship between E, v, and r determines orbit type: elliptical (E < 0), parabolic (E = 0), or hyperbolic (E > 0).

## Questions

```yaml
- question: "A spacecraft is launched from Earth at exactly escape velocity, then its engines cut off. Ignoring atmospheric drag, which trajectory will it follow?"
  type: multiple-choice
  options:
    - "It falls back to Earth — gravity always pulls objects back eventually"
    - "It enters a stable circular orbit at a very high altitude"
    - "It follows a parabolic trajectory and arrives at infinite distance with zero velocity"
    - "It follows a hyperbolic trajectory and retains kinetic energy at infinite distance"
  answer: 2
  explanation: "Escape velocity is defined as the minimum speed for which the total mechanical energy E = 0. With E = 0, the trajectory is a parabola, and as r → ∞ the kinetic energy approaches zero (all energy was 'used' against gravity). Option A is wrong because E = 0 is exactly the threshold of escape. Option D (hyperbola) requires E > 0, meaning the launch speed exceeded escape velocity. The parabolic trajectory is the knife-edge case — any slightly less speed produces a bound elliptical orbit."

- question: "For a satellite in a circular orbit at radius r, how does its kinetic energy relate to its gravitational potential energy?"
  type: multiple-choice
  options:
    - "KE = |PE| — kinetic and potential energy are equal in magnitude"
    - "KE = ½|PE| — kinetic energy is half the magnitude of the potential energy"
    - "KE = 2|PE| — kinetic energy is twice the potential energy"
    - "KE = |PE| / r — the relationship depends on orbital radius"
  answer: 1
  explanation: "From the circular orbit condition GMm/r² = mv²/r, we get v² = GM/r, so KE = ½mv² = GMm/(2r). Since PE = −GMm/r, we have KE = −PE/2, or KE = ½|PE|. This is the virial theorem for gravitational systems. It also means total energy E = KE + PE = GMm/(2r) − GMm/r = −GMm/(2r) = −KE, so the total energy is always negative (bound) and equals negative of the kinetic energy."

- question: "A comet observed to follow a hyperbolic trajectory through the inner solar system has positive total mechanical energy."
  type: true-false
  answer: true
  explanation: "Orbit type is completely determined by the sign of total energy E = KE + PE. E < 0: bound elliptical orbit. E = 0: parabolic trajectory (barely escapes). E > 0: hyperbolic trajectory — the object has more than enough energy to escape and retains kinetic energy at infinite distance. A comet on a hyperbolic path is an unbound visitor making one pass through the solar system; it was never gravitationally captured. This also applies to interstellar objects like 'Oumuamua."

- question: "An object launched from Earth's surface at escape velocity must be aimed straight up; launching at an angle requires a higher initial speed to escape."
  type: true-false
  answer: false
  explanation: "Gravity is a conservative force, so the work done by gravity depends only on the initial and final positions (radii), not on the path taken. For any trajectory that starts at radius R with speed v_esc = √(2GM/R), the total energy is exactly E = 0, regardless of launch direction. The object will escape no matter what angle it is launched at, as long as the speed equals v_esc. (In practice, atmosphere and terrain matter, but in idealized point-mass mechanics, direction is irrelevant to escape.)"

- question: "Explain why all elliptical orbits with the same semi-major axis have the same orbital period, even if their shapes (eccentricities) are very different."
  type: short-answer
  answer: "The total mechanical energy of an elliptical orbit is E = −GMm/(2a), where a is the semi-major axis. Since energy depends only on a, two orbits with the same a have the same energy regardless of eccentricity. Kepler's third law (T² ∝ a³) follows from this energy relationship combined with angular momentum. A circular orbit and a highly elongated ellipse with the same a have the same period because they have the same total energy — the elongated ellipse moves slowly at apogee and very fast at perigee, averaging out to the same orbital period."
  explanation: "This is one of the most surprising results in orbital mechanics. The 'size' of the orbit (semi-major axis) alone determines both the energy and the period — not the shape. A nearly radial orbit (very high eccentricity) and a nearly circular orbit (eccentricity ≈ 0) with the same a are energetically equivalent and have the same period. This follows because E = −GMm/(2a) is the exact energy for any conic section orbit."
```

## Explainer

You already know that gravitational potential energy takes the form **U = −GMm/r**, where the potential energy is zero at infinite separation and becomes increasingly negative as objects approach. You also know conservation of energy: in any closed system with only conservative forces, the total mechanical energy E = KE + PE remains constant. Orbital mechanics is the application of these two ideas to motion in gravitational fields — and the total energy turns out to classify everything about the orbit.

Start with a simple circular orbit at radius r. For a circular orbit, the gravitational force provides exactly the centripetal acceleration: GMm/r² = mv²/r, giving v² = GM/r and hence kinetic energy KE = GMm/(2r). The potential energy is U = −GMm/r. Total energy: E = KE + U = GMm/(2r) − GMm/r = **−GMm/(2r)**. Notice two things. First, the total energy is negative — the object is **bound** to the central body, just as we say a ball at the bottom of a well has negative potential energy relative to ground level. Second, the kinetic energy is exactly −½ times the potential energy (E = ½U): this is the **virial theorem** for gravitational systems, and it holds for all bound orbits on average, not just circular ones.

Escape velocity follows immediately from conservation of energy. If you launch an object with just enough speed to reach infinity (where both KE and PE are zero), the total energy of the trajectory must equal zero. Setting E = 0: ½mv² − GMm/R = 0, so **v_esc = √(2GM/R)**. At Earth's surface, this gives ≈ 11.2 km/s. This is the minimum launch speed *in the absence of atmosphere* for a projectile — not a rocket, which can fire continuously. The direction doesn't matter for escape velocity because gravity is a conservative force; only the speed at launch determines whether the object escapes, and it doesn't need to follow any particular path.

The total energy determines orbit *type* as well as orbit *size*. If E < 0, the object cannot escape — it's bound — and the orbit is an ellipse (circular orbits are the special case where the ellipse has zero eccentricity). If E = 0, the object barely escapes, arriving at infinity with zero velocity, and the trajectory is a **parabola**. If E > 0, the object escapes with kinetic energy to spare and follows a **hyperbola** — this is the trajectory of a comet making a one-time pass through the solar system, or a spacecraft executing a gravitational slingshot. In each case, the semi-major axis a is determined by E alone: **E = −GMm/(2a)** for bound orbits, which is why all ellipses with the same semi-major axis have the same period (Kepler's third law) regardless of their eccentricity.
