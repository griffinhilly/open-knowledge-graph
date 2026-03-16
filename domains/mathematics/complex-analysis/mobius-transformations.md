---
id: mobius-transformations
title: Möbius Transformations
domain: mathematics
course: complex-analysis
prerequisites:
- id: conformal-mappings
  type: hard
tags:
- mobius-transformations
- linear-fractional
- conformal
stage: advanced
status: draft
---

# Möbius Transformations

## Core Idea
A Möbius transformation is f(z) = (az + b)/(cz + d) where ad - bc ≠ 0. These are conformal maps of the extended complex plane (including ∞) and form a group under composition. They map circles and lines to circles and lines, making them useful for transforming domains in conformal mapping problems.

## Explainer

You've already studied conformal mappings — angle-preserving maps of the complex plane that translate, rotate, scale, and transform domains to make boundary value problems solvable. Möbius transformations are the most important class of conformal maps, combining several elementary operations into a single elegant formula that acts on the entire extended complex plane.

A **Möbius transformation** (also called a **linear fractional transformation**) is any map f(z) = (az + b)/(cz + d) where a, b, c, d ∈ ℂ and **ad - bc ≠ 0**. The condition ad - bc ≠ 0 (the determinant of the matrix [[a,b],[c,d]] is nonzero) ensures the map isn't degenerate — if ad = bc, the transformation collapses to a constant. Every Möbius transformation is a composition of three elementary operations you already know: a translation (z ↦ z + b/a), a scaling and rotation (z ↦ az), and an **inversion** (z ↦ 1/z). The inversion is the new ingredient that plain linear maps can't provide — it maps points near the origin to points far away, and vice versa.

The key geometric property: **Möbius transformations map circles and lines to circles and lines**. Here, "line" is treated as a circle through the point at infinity in the extended complex plane ℂ ∪ {∞}. A Möbius transformation sends z = -d/c to ∞ (the pole) and sends ∞ to a/c. This is why they're defined on the **Riemann sphere** — they become bijections of that compact space. The image of a circle under a Möbius transformation is another circle or possibly a line, and critically, angles between curves are preserved (conformality is maintained).

The power of Möbius transformations in applications comes from the **three-point rule**: given any two triples of distinct points (z₁, z₂, z₃) and (w₁, w₂, w₃) in ℂ ∪ {∞}, there is exactly one Möbius transformation sending z_i ↦ w_i. This means you can construct the specific map that transforms a given domain (say, a disk) to a standard domain (say, the upper half-plane) by specifying where three boundary points go. Since Möbius transformations form a **group** under composition, you can chain them: first map disk to disk (centering it), then map disk to half-plane, and the composition is another Möbius transformation — no approximation, exact and conformal.
