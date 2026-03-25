---
id: orbital-elements-and-trajectories
title: Orbital Elements and Trajectories
domain: physics
course: classical-mechanics
prerequisites:
- id: orbital-energy-and-escape-velocity
  type: hard
- id: angular-momentum
  type: hard
- id: conic-sections-ellipses
  type: hard
- id: reduced-mass-problem
  type: soft
- id: phase-space-trajectories
  type: soft
builds-toward:
- stability-of-circular-orbits
tags:
- orbits
- gravitation
- trajectories
- orbital-mechanics
stage: formal-systems
status: validated
---
# Orbital Elements and Trajectories

## Core Idea
Orbital shape is uniquely determined by total energy E and angular momentum L. Low energy (E < 0) and high L yield elliptical orbits with semi-major axis a = −G M m / (2 E) and eccentricity e = √[1 + 2 E L² / (μ (G M)²)]. The orbit is closed (periodic) for E < 0, parabolic for E = 0, and hyperbolic for E > 0. Each orbit is conic section about the central mass.

## Questions

```yaml
- question: "Two spacecraft leave Earth on trajectories with the same total energy E < 0 but different angular momenta L₁ > L₂. Which correctly describes their orbits?"
  type: multiple-choice
  options:
    - "Both orbits are the same size and shape because energy alone determines the orbit"
    - "Both are ellipses with the same semi-major axis, but the higher-L orbit has lower eccentricity (more circular)"
    - "The higher-L orbit is larger because angular momentum determines orbital size"
    - "The higher-L orbit is hyperbolic because more angular momentum means more kinetic energy"
  answer: 1
  explanation: "Semi-major axis is determined by energy alone: a = −GMm/(2E). So both orbits have the same semi-major axis and the same period. But angular momentum controls shape (eccentricity): e = √[1 + 2EL²/(μ(GM)²)]. Higher L yields lower e — a more circular ellipse. Lower L yields higher e — a more elongated, needle-like ellipse. This is the key insight: E sets the orbit's size; L sets its shape."

- question: "A comet is observed on a trajectory that will just barely allow it to escape the solar system and reach infinite distance with zero remaining velocity. What type of orbit is it on?"
  type: multiple-choice
  options:
    - "A hyperbolic orbit, because any escape trajectory must have excess velocity"
    - "A circular orbit, because circular orbits have the minimum energy to remain bound"
    - "A parabolic orbit, because E = 0 corresponds to exactly escaping with zero final velocity"
    - "An elliptical orbit with very high eccentricity approaching 1"
  answer: 2
  explanation: "When E = 0, the object has just enough kinetic energy to reach infinity — it escapes the gravitational well but arrives with zero velocity remaining. This is the precise boundary between bound (E < 0, elliptical) and unbound (E > 0, hyperbolic) motion, and it corresponds to a parabolic orbit. A hyperbolic orbit has E > 0 and arrives at infinity with nonzero velocity. An ellipse with e approaching 1 is extremely elongated but still bound (E < 0); it never reaches infinity."

- question: "Two objects in the same elliptical orbit but at different positions (one near periapsis, one near apoapsis) have different total energies because their kinetic and potential energies differ at each location."
  type: true-false
  answer: false
  explanation: "Total mechanical energy E = K + U is conserved. As an object moves from apoapsis (slowest, farthest, most negative potential energy contribution) to periapsis (fastest, closest), it gains kinetic energy while its potential energy becomes less negative — the sum stays constant. Both objects have the same total energy E because they are on the same orbit. The semi-major axis a = −GMm/(2E) depends only on E, confirming that all points on the same ellipse share the same total energy."

- question: "For a fixed negative total energy, increasing an object's angular momentum makes its orbit more elongated (higher eccentricity)."
  type: true-false
  answer: false
  explanation: "The eccentricity formula e = √[1 + 2EL²/(μ(GM)²)] shows that for fixed E < 0 (negative), the term 2EL²/... becomes more negative as L increases, making the expression inside the square root closer to zero — meaning e approaches 0, a more circular orbit. The limiting case L → 0 gives a radial free-fall (e → 1, degenerate ellipse); maximum L gives a circular orbit (e = 0). Higher angular momentum means more 'sideways' motion, which rounds out the orbit."

- question: "Why do just two conserved quantities — total energy E and angular momentum L — completely determine the shape and size of a gravitational orbit?"
  type: short-answer
  answer: "In a two-body gravitational system, energy E = K + U determines whether the orbit is bound (E < 0 → ellipse), marginally bound (E = 0 → parabola), or unbound (E > 0 → hyperbola), and sets the semi-major axis a = −GMm/(2E) for ellipses. Angular momentum L controls how the available energy is distributed between radial and tangential motion, setting the eccentricity e = √[1 + 2EL²/(μ(GM)²)] — how circular versus elongated the orbit is. Together, a and e completely specify the conic section. The gravitational force law (inverse-square) is what makes this exact determination possible; it is a special property of 1/r² forces."
  explanation: "Conservation laws reduce a problem with infinite degrees of freedom (the full trajectory as a function of time) to two numbers that capture the geometry. This is the power of symmetry: the spherical symmetry of gravity conserves angular momentum; the time-invariance of gravity conserves energy. Any orbit consistent with those two conserved values must be a specific conic section — no other trajectory is possible under Newtonian gravity."
```

## Explainer

You come to this topic knowing that orbital energy and angular momentum are conserved quantities in gravitational motion, and that conic sections — ellipses, parabolas, hyperbolas — are the curves obtained by slicing a cone at different angles. The deep result here is that these two pieces of mathematics are the same thing: the conserved quantities E and L uniquely determine which conic section a gravitational orbit traces. Shape and energy are not independent — they are locked together by Newton's law of gravity.

Think first about what **energy** and **angular momentum** each control. Total energy E = K + U determines whether the orbit is bound. For a gravitational potential U = −GMm/r, E is negative when the particle is gravitationally bound (cannot escape to infinity), zero at the precise boundary of escape, and positive when the particle has more than enough energy to escape. This directly maps to orbit type: E < 0 gives an **ellipse** (closed, periodic — the planet returns), E = 0 gives a **parabola** (exactly escapes, the minimum-energy trajectory to infinity), E > 0 gives a **hyperbola** (overshoots escape velocity, passes through and continues to infinity). Every comet or spacecraft flyby tracing a hyperbolic path through the solar system is on a positive-energy orbit.

**Angular momentum** L controls the *shape* within a given energy class. For fixed E < 0, larger L means a more circular ellipse (low eccentricity), while smaller L means a more elongated, needle-like ellipse (high eccentricity). The limiting case L → 0 at fixed negative energy is a radial free-fall — a degenerate "orbit" that plunges straight through the center. The **eccentricity** formula e = √[1 + 2EL²/(μ(GM)²)] makes this precise: when L is large relative to the binding energy, the second term inside the square root is small and e ≈ 0 (circular); as L decreases, e approaches 1 (parabolic boundary) and beyond (hyperbolic).

The practical vocabulary of orbital mechanics — **semi-major axis** a, eccentricity e, periapsis and apoapsis distances — maps directly onto E and L via these formulas. For an elliptical orbit, a = −GMm/(2E) tells you the orbit's size from its energy alone, independent of shape. This is why two objects on the same ellipse but at different positions have the same total energy — they trade kinetic and potential as they move, but the sum stays constant and the semi-major axis stays fixed. Knowing E and L, you know everything about the orbit's geometry. This is the power of conservation laws: they reduce a continuous dynamical trajectory to two numbers.
