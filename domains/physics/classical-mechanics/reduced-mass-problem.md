---
id: reduced-mass-problem
title: Reduced Mass Problem
domain: physics
course: classical-mechanics
prerequisites:
- id: center-of-mass-motion
  type: hard
tags:
- two-body
- gravitation
- reduced-mass
- orbital-mechanics
stage: formal-systems
status: draft
---

# Reduced Mass Problem

## Core Idea
In a two-body gravitational system (e.g., Earth–Sun or binary stars), the center of mass moves with constant velocity, and the relative motion reduces to a single-body problem: a reduced mass μ = m₁ m₂ / (m₁ + m₂) orbits a fixed potential with mass M = m₁ + m₂. When one mass dominates (m₁ >> m₂), the reduced mass μ ≈ m₂, and the lighter body orbits the heavier one.

## Explainer

From your study of center-of-mass motion, you know that in an isolated system the center of mass (CM) moves at constant velocity — or equivalently, in the CM frame it is at rest. The key insight of the reduced-mass approach is to use this fact to split any two-body problem into two completely separate, simpler problems: one trivial (the CM drifts uniformly), and one non-trivial but effectively a one-body problem (the relative motion).

The mathematical setup works as follows. Define the CM position R = (m₁r₁ + m₂r₂)/(m₁ + m₂) and the **relative coordinate** r = r₁ − r₂. The total momentum P = (m₁ + m₂)Ṙ is conserved, so the CM moves uniformly — done. For the relative coordinate, Newton's second law gives: **μr̈ = F(r)**, where F(r) is the mutual force between the bodies (gravitational, spring, etc.) and μ = m₁m₂/(m₁ + m₂) is the **reduced mass**. This single equation, involving only the relative separation r, is formally identical to the one-body problem of a particle of mass μ moving in the force field F(r). All the results you know from single-particle orbital mechanics — Kepler's laws, energy conservation, angular momentum conservation, the effective potential — apply directly to this equivalent problem.

To build intuition for the reduced mass formula, note its behavior at the extremes. When the two masses are equal (m₁ = m₂ = m), μ = m/2: the reduced mass is half the individual mass, reflecting that both bodies orbit their common center. When one mass dominates (say m₁ ≫ m₂, like the Sun and Earth), μ ≈ m₂: the reduced mass is approximately the lighter body's mass. This is why treating the Earth as orbiting a fixed Sun is an excellent approximation — the Sun barely moves. The correction is tiny but real: the Sun does wobble slightly, and for binary star systems of comparable masses, both stars orbit the common CM at distances inversely proportional to their masses.

A concrete example cements the method. For the Earth–Sun system: m_E ≈ 6 × 10²⁴ kg, m_S ≈ 2 × 10³⁰ kg. The reduced mass is μ = m_E m_S/(m_E + m_S) ≈ m_E × (1 − m_E/m_S) ≈ m_E, with a correction of only one part in 300,000. For a **binary star** with m₁ = m₂ = m, the reduced mass is m/2, both stars orbit the CM at radius R₁ = R₂ = r/2, and each contributes equally to the system's kinetic energy. The reduced-mass framework is the gateway to treating all two-body central-force problems — including atomic physics, where it is used to account for the finite mass of the nucleus in the hydrogen atom energy levels.
