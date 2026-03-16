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
builds-toward:
- stability-of-circular-orbits
tags:
- orbits
- gravitation
- trajectories
- orbital-mechanics
stage: formal-systems
status: draft
---

# Orbital Elements and Trajectories

## Core Idea
Orbital shape is uniquely determined by total energy E and angular momentum L. Low energy (E < 0) and high L yield elliptical orbits with semi-major axis a = −G M m / (2 E) and eccentricity e = √[1 + 2 E L² / (μ (G M)²)]. The orbit is closed (periodic) for E < 0, parabolic for E = 0, and hyperbolic for E > 0. Each orbit is conic section about the central mass.

## Explainer

You come to this topic knowing that orbital energy and angular momentum are conserved quantities in gravitational motion, and that conic sections — ellipses, parabolas, hyperbolas — are the curves obtained by slicing a cone at different angles. The deep result here is that these two pieces of mathematics are the same thing: the conserved quantities E and L uniquely determine which conic section a gravitational orbit traces. Shape and energy are not independent — they are locked together by Newton's law of gravity.

Think first about what **energy** and **angular momentum** each control. Total energy E = K + U determines whether the orbit is bound. For a gravitational potential U = −GMm/r, E is negative when the particle is gravitationally bound (cannot escape to infinity), zero at the precise boundary of escape, and positive when the particle has more than enough energy to escape. This directly maps to orbit type: E < 0 gives an **ellipse** (closed, periodic — the planet returns), E = 0 gives a **parabola** (exactly escapes, the minimum-energy trajectory to infinity), E > 0 gives a **hyperbola** (overshoots escape velocity, passes through and continues to infinity). Every comet or spacecraft flyby tracing a hyperbolic path through the solar system is on a positive-energy orbit.

**Angular momentum** L controls the *shape* within a given energy class. For fixed E < 0, larger L means a more circular ellipse (low eccentricity), while smaller L means a more elongated, needle-like ellipse (high eccentricity). The limiting case L → 0 at fixed negative energy is a radial free-fall — a degenerate "orbit" that plunges straight through the center. The **eccentricity** formula e = √[1 + 2EL²/(μ(GM)²)] makes this precise: when L is large relative to the binding energy, the second term inside the square root is small and e ≈ 0 (circular); as L decreases, e approaches 1 (parabolic boundary) and beyond (hyperbolic).

The practical vocabulary of orbital mechanics — **semi-major axis** a, eccentricity e, periapsis and apoapsis distances — maps directly onto E and L via these formulas. For an elliptical orbit, a = −GMm/(2E) tells you the orbit's size from its energy alone, independent of shape. This is why two objects on the same ellipse but at different positions have the same total energy — they trade kinetic and potential as they move, but the sum stays constant and the semi-major axis stays fixed. Knowing E and L, you know everything about the orbit's geometry. This is the power of conservation laws: they reduce a continuous dynamical trajectory to two numbers.
