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

## Questions

```yaml
- question: "A satellite orbits Earth with total mechanical energy E = KE + PE = −5 × 10⁹ J. Which statement correctly describes this orbit?"
  type: multiple-choice
  options:
    - "The satellite has negative kinetic energy and will slow to a stop"
    - "The satellite is in a bound orbit and cannot escape to infinity without an energy input"
    - "The satellite will escape Earth's gravity because its KE exceeds its PE"
    - "Total energy cannot be negative — the calculation contains an error"
  answer: 1
  explanation: "E < 0 means the satellite is bound. KE is always positive (½mv² ≥ 0), so the negative total energy comes entirely from U = −GMm/r being large and negative. For the satellite to reach r = ∞ (where U = 0), it would need KE = E − U = E < 0 at infinity, which is impossible. The orbit is therefore elliptical or circular, and the satellite cannot escape without an external energy input."

- question: "As a spacecraft moves from distance r to distance 2r from Earth's center, what happens to its gravitational potential energy?"
  type: multiple-choice
  options:
    - "U becomes more negative — moving farther out increases the gravitational well depth"
    - "U stays the same — gravitational PE is constant at orbital distances"
    - "U becomes less negative, moving from −GMm/r toward zero — the spacecraft climbs out of the gravity well"
    - "U changes sign from negative to positive once the spacecraft passes a threshold distance"
  answer: 2
  explanation: "U(r) = −GMm/r. At 2r, U = −GMm/(2r), which is half as negative — closer to zero. Moving away from Earth means climbing out of the gravitational potential well; U increases (becomes less negative), approaching 0 as r → ∞. U is always negative for gravity and never becomes positive — U = 0 is the reference at infinity, not a sign-change threshold."

- question: "Gravitational potential energy U(r) = −GMm/r is always negative because gravity is attractive, meaning two masses always release energy when brought from infinite separation to any finite distance."
  type: true-false
  answer: true
  explanation: "Setting U = 0 at r = ∞ (the natural zero for an inverse-square force), any finite separation requires that energy was released as the masses fell together under attraction. Equivalently, you must add energy to pull them back apart to infinity. Being 'in' a gravitational well means U < 0, and the magnitude of U tells you how much energy must be supplied to escape. This is why gravitationally bound systems (planets, stars, galaxies) all have negative total energy."

- question: "The near-Earth approximation U = mgh fails at high altitudes because gravity reverses direction above a certain distance from Earth's surface."
  type: true-false
  answer: false
  explanation: "Gravity does not reverse direction — it always points toward Earth's center at all distances. The approximation U = mgh fails at large h because it assumes g is constant (the linear approximation), but the true formula g(r) = GM/r² decreases significantly as r increases. The crossover occurs at heights comparable to Earth's radius (~6400 km). The direction of gravity is irrelevant to this failure — only the magnitude variation matters."

- question: "Explain why the sign of total mechanical energy E = KE + U determines whether a gravitational orbit is bound or unbound."
  type: short-answer
  answer: "In a gravitational system, KE ≥ 0 always, and U = −GMm/r → 0 as r → ∞. If E < 0, reaching r = ∞ would require KE = E − 0 = E < 0, which is impossible — so the object can never reach infinity and is trapped in a bound (elliptical or circular) orbit. If E ≥ 0, the object can reach infinity with KE = E ≥ 0 remaining and escapes. E = 0 is the boundary: the object barely reaches infinity with zero remaining velocity, defining escape velocity v_esc = √(2GM/r)."
  explanation: "This energy classification is the single most important tool in orbital mechanics. The bound/unbound distinction determines whether a comet returns, whether a spacecraft can reach another planet, and whether a galaxy is gravitationally stable. The key insight is that U approaches zero from below as r increases, so the sign of E tells you whether the object has 'enough' energy to climb out of the potential well entirely."
```

## Explainer

You already know **potential energy** as stored energy associated with position in a force field: the closer you are to Earth's surface, the lower your gravitational PE (taking the surface as reference). And from **Newton's law of gravitation** you know the force law: F = −G m₁ m₂ / r², always attractive, falling off as 1/r². The extended potential energy formula is just what you get when you integrate that force law over all possible separations, using infinity as the natural zero point.

The formula U(r) = −G m₁ m₂ / r has two features that initially surprise students. First, it is always **negative**. This is because gravity is attractive: to pull two masses apart from their natural tendency to fall together, you must add energy. Starting at infinity (U = 0), any finite separation is *below* the natural reference — you're in an energy well. The deeper you are (smaller r), the more negative U is, and the more energy you would need to supply to reach r = ∞. Second, it is inversely proportional to r (not r²): the *force* falls off as 1/r², but integrating that gives a 1/r potential. At twice the distance, the potential energy is halved in magnitude (U doubles toward zero), while the force is reduced to one-quarter.

The near-Earth approximation U = mgh is the limit of this formula for small height h above Earth's surface. If you expand −GMm/(R + h) around h = 0, the first correction is +GMmh/R² = mgh (since g = GM/R²). For h ≪ R, the approximation is excellent; for satellite orbits or interplanetary trajectories, you must use the full 1/r formula. The crossover happens roughly at heights comparable to Earth's radius (~6400 km).

The most powerful consequence is the energy classification of orbits. Total mechanical energy E = ½mv² − GMm/r is conserved (no friction, no thrust). If E < 0, the object is **bound**: it lacks enough kinetic energy to escape to infinity. The orbit is an ellipse (or circle), and the object endlessly returns. If E = 0, the object is on a **parabolic** escape trajectory — just barely able to reach infinity with zero velocity remaining. If E > 0, the orbit is **hyperbolic** — the object escapes with kinetic energy to spare. **Escape velocity** is simply the v that sets E = 0: v_esc = √(2GM/r). For Earth's surface, v_esc ≈ 11.2 km/s. The sign of total energy is the single most important quantity in orbital mechanics.
