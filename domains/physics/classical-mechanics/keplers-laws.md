---
id: keplers-laws
title: Kepler's Laws of Planetary Motion
domain: physics
course: classical-mechanics
prerequisites:
- id: orbital-mechanics
  type: hard
- id: conservation-of-angular-momentum
  type: soft
- id: conic-sections-ellipses
  type: soft
- id: polar-coordinates
  type: soft
tags:
- Kepler
- planetary-motion
- elliptical-orbit
- orbital-period
stage: formal-systems
status: validated
---

# Kepler's Laws of Planetary Motion

## Core Idea
Kepler's three empirical laws describe planetary orbits: (1) Planets move in ellipses with the Sun at one focus. (2) A line from the Sun to a planet sweeps equal areas in equal times (consequence of angular momentum conservation). (3) The square of the orbital period is proportional to the cube of the semi-major axis: T² ∝ a³ (specifically T² = 4π²a³/GM). Newton derived all three from his law of universal gravitation, showing they are not independent empirical facts but consequences of deeper physics.

## How It's Best Learned
Derive Kepler's third law for circular orbits from Newton's law of gravitation and centripetal force. Then generalize to ellipses by replacing r with the semi-major axis a. Use Kepler's second law to explain why planets move fastest at perihelion.

## Common Misconceptions
- Thinking planetary orbits are perfect circles: they are ellipses, though many planets have low eccentricity that makes them nearly circular.
- Confusing Kepler's third law: it is T² ∝ a³, not T ∝ a or T² ∝ a².
- Believing Kepler's laws only apply to planets: they apply to any two-body gravitational system (moons, comets, binary stars).

## Explainer

From your work on orbital mechanics, you know that a satellite in a circular orbit maintains constant speed because gravity provides exactly the centripetal force needed. Kepler's laws generalize this: real orbits are not circles but **ellipses**, and the geometry of the ellipse encodes everything about how speed and position vary over the orbit.

An ellipse has two foci. The **First Law** states that the Sun sits at one focus — not the center — of each planet's elliptical orbit. This means the planet's distance from the Sun varies continuously. The closest point is called **perihelion**; the farthest is **aphelion**. For most planets the eccentricity is small (Earth's is about 0.017), so the orbit looks nearly circular, but the Sun is still slightly off-center. For comets, eccentricity can be close to 1, producing very elongated orbits that sweep far from the Sun.

The **Second Law** — equal areas in equal times — is a direct consequence of conservation of angular momentum, which you already know. As a planet approaches perihelion, it speeds up; as it recedes toward aphelion, it slows. The reason is the same as for a spinning ice skater pulling her arms in: as radius decreases, angular velocity must increase to conserve L = mrv. Near perihelion, the planet is moving fastest; near aphelion, slowest. The swept-area law is an elegant geometric expression of this: to cover equal areas in equal times, the planet must move along the arc faster when close to the focus and slower when far.

The **Third Law**, T² = 4π²a³/GM, is the most quantitatively powerful. To derive it for a circular orbit: set gravitational force equal to centripetal force, GMm/r² = mv²/r, and substitute v = 2πr/T. Solving gives T² = 4π²r³/GM, which is already the right form with r = a for circular orbits. For ellipses, the same result holds with the semi-major axis *a* replacing *r*, a result that requires calculus to prove in full generality. The practical power is enormous: if you know the orbital period of any body in the solar system, you can immediately determine the semi-major axis of its orbit, and vice versa. This is how the distances of the planets were first calculated — using timing from telescope observations before spacecraft were ever possible.
