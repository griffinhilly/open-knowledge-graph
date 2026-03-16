---
id: gravitational-potential-energy-extended
title: Gravitational Potential Energy (Extended)
domain: physics
course: classical-mechanics
prerequisites:
- id: potential-energy
  type: hard
- id: newtons-law-of-gravitation
  type: hard
builds-toward:
- orbital-energy-and-escape-velocity
tags:
- gravitation
- potential-energy
- energy
- orbits
stage: formal-systems
status: draft
---

# Gravitational Potential Energy (Extended)

## Core Idea
Gravitational potential energy between two masses is U(r) = −G m₁ m₂ / r (with U = 0 at r = ∞). Unlike the near-Earth approximation U = mgh (linear in height), the true gravitational PE is inversely proportional to distance and negative, indicating an attractive interaction. Total mechanical energy E = KE + U is conserved in gravitational systems, determining whether orbits are bound (E < 0) or unbound (E ≥ 0).

## Explainer

You already know **potential energy** as stored energy associated with position in a force field: the closer you are to Earth's surface, the lower your gravitational PE (taking the surface as reference). And from **Newton's law of gravitation** you know the force law: F = −G m₁ m₂ / r², always attractive, falling off as 1/r². The extended potential energy formula is just what you get when you integrate that force law over all possible separations, using infinity as the natural zero point.

The formula U(r) = −G m₁ m₂ / r has two features that initially surprise students. First, it is always **negative**. This is because gravity is attractive: to pull two masses apart from their natural tendency to fall together, you must add energy. Starting at infinity (U = 0), any finite separation is *below* the natural reference — you're in an energy well. The deeper you are (smaller r), the more negative U is, and the more energy you would need to supply to reach r = ∞. Second, it is inversely proportional to r (not r²): the *force* falls off as 1/r², but integrating that gives a 1/r potential. At twice the distance, the potential energy is halved in magnitude (U doubles toward zero), while the force is reduced to one-quarter.

The near-Earth approximation U = mgh is the limit of this formula for small height h above Earth's surface. If you expand −GMm/(R + h) around h = 0, the first correction is +GMmh/R² = mgh (since g = GM/R²). For h ≪ R, the approximation is excellent; for satellite orbits or interplanetary trajectories, you must use the full 1/r formula. The crossover happens roughly at heights comparable to Earth's radius (~6400 km).

The most powerful consequence is the energy classification of orbits. Total mechanical energy E = ½mv² − GMm/r is conserved (no friction, no thrust). If E < 0, the object is **bound**: it lacks enough kinetic energy to escape to infinity. The orbit is an ellipse (or circle), and the object endlessly returns. If E = 0, the object is on a **parabolic** escape trajectory — just barely able to reach infinity with zero velocity remaining. If E > 0, the orbit is **hyperbolic** — the object escapes with kinetic energy to spare. **Escape velocity** is simply the v that sets E = 0: v_esc = √(2GM/r). For Earth's surface, v_esc ≈ 11.2 km/s. The sign of total energy is the single most important quantity in orbital mechanics.
