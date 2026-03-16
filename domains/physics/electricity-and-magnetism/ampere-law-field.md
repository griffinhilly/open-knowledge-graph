---
id: ampere-law-field
title: Ampere's Law and Magnetic Field Symmetry
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: biot-savart-field
  type: soft
- id: curl-and-divergence
  type: hard
- id: line-integrals-vector-fields
  type: hard
builds-toward:
- magnetic-field-solenoid
tags:
- ampere-law
- symmetry
- circulation
stage: formal-systems
status: draft
---

# Ampere's Law and Magnetic Field Symmetry

## Core Idea
Ampere's law states ∮ B⃗·d⃗ℓ = μ₀I_enc. For high-symmetry current distributions, choosing an Amperian loop aligned with that symmetry makes the circulation integral trivial. For a solenoid: B = μ₀nI inside, 0 outside. For a toroid: B = μ₀NI/(2πr) inside, 0 outside. Ampere's law is a direct consequence of the Biot-Savart law.

## Explainer

Ampère's law is the magnetic analog of Gauss's law: instead of asking how much flux threads a closed surface, it asks how much **circulation** a magnetic field has around a closed loop. Mathematically, ∮ B⃗·d⃗ℓ = μ₀I_enc — the line integral of B around any closed path equals μ₀ times the current passing through the surface bounded by that path. You already know line integrals from your vector calculus prerequisites; here, the integrand is the component of B tangent to the chosen loop. The law holds for any loop you can draw, but it only becomes computationally useful when symmetry makes B constant in magnitude and everywhere parallel (or perpendicular) to the loop.

The strategy mirrors what you learned with Gauss's law. First, identify the symmetry of the current distribution. A long straight wire has cylindrical symmetry: B must circle the wire in rings, with the same magnitude at every point on a circle of radius r centered on the wire. Choose a circular Amperian loop of radius r in the plane perpendicular to the wire. Because B is tangent to this circle everywhere and has constant magnitude, the integral becomes B × (2πr) = μ₀I_enc, giving B = μ₀I/(2πr) — the same result the Biot-Savart law gives, but arrived at in a single algebraic step once symmetry is invoked.

The solenoid is the canonical second example. An ideal solenoid is a tightly wound helical coil; by symmetry, B must be axial (along the solenoid's axis) inside and negligible outside. Choose a rectangular Amperian loop with one long side inside the solenoid and the other outside. The outside side contributes zero (B ≈ 0 there), and the two short sides are perpendicular to B and contribute zero. Only the inside segment matters: B × L = μ₀ × (nL) × I, where n is the number of turns per unit length and nL is the number of turns threading the rectangle. The result is B = μ₀nI — a uniform field inside, independent of position. This is why solenoids are used to create controlled, uniform magnetic fields.

**The Amperian loop** is a purely mathematical construct — you choose it to exploit symmetry, just as you chose Gaussian surfaces. The requirement is that B be either constant and parallel to d⃗ℓ (so it factors out of the integral) or perpendicular to d⃗ℓ (so its contribution is zero) on each segment of the loop. If no such loop exists, Ampère's law is still true but gives you an equation you cannot easily solve — in those cases you fall back to Biot-Savart. The deeper point, which your curl-and-divergence prerequisite illuminates, is that Ampère's law in differential form reads ∇ × B = μ₀J: the curl of B equals the current density. This connects the macroscopic circulation integral to the local swirling behavior of the field, and it is one of Maxwell's four fundamental equations.
