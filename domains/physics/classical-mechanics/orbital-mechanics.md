---
id: orbital-mechanics
title: 'Orbital Mechanics: Circular and Elliptical Orbits'
domain: physics
course: classical-mechanics
prerequisites:
- id: newtons-law-of-gravitation
  type: hard
- id: circular-motion-dynamics
  type: hard
- id: conservation-of-energy
  type: soft
builds-toward:
- keplers-laws
tags:
- orbits
- circular-orbit
- gravitational-force
- orbital-velocity
stage: formal-systems
status: draft
---

# Orbital Mechanics: Circular and Elliptical Orbits

## Core Idea
A satellite in a circular orbit is in free fall: gravity provides exactly the centripetal force needed to maintain circular motion. Setting GMm/r² = mv²/r gives orbital speed v = √(GM/r) and period T = 2π r^(3/2) / √(GM). The total mechanical energy of a circular orbit is E = −GMm/(2r): negative, indicating a bound orbit. Elliptical orbits are more general and governed by the same gravitational law with energy E = −GMm/(2a), where a is the semi-major axis.

## How It's Best Learned
Derive orbital speed and period for circular orbits, then extend to geostationary orbit calculations (find the orbital radius where T = 24 hours). Compare the energy of a circular orbit at different radii to understand why lower orbits move faster.

## Common Misconceptions
- Thinking astronauts in orbit are weightless because there is no gravity: they are in free fall, accelerating toward Earth at the same rate as their spacecraft, producing the sensation of weightlessness.
- Believing that firing rocket engines always speeds up a spacecraft: it depends on the burn direction relative to the velocity vector.
