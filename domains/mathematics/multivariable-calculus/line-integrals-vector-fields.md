---
id: line-integrals-vector-fields
title: Line Integrals of Vector Fields
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: line-integrals-scalar
  type: hard
- id: vector-fields
  type: hard
- id: dot-product
  type: hard
builds-toward:
- conservative-fields
- fundamental-theorem-line-integrals
- greens-theorem
tags:
- line-integral
- work
- vector-field
- circulation
stage: formal-systems
status: draft
---

# Line Integrals of Vector Fields

## Core Idea
The line integral of a vector field F along a curve C is ∫_C F · dr = ∫_a^b F(r(t)) · r′(t) dt. It measures the total work done by force field F on a particle moving along C, or the circulation of a fluid velocity field along the curve. Unlike scalar line integrals, vector field line integrals are orientation-dependent: reversing the direction of C negates the integral. The notation ∫_C P dx + Q dy is equivalent to ∫_C F · dr when F = ⟨P, Q⟩.

## How It's Best Learned
Start with the physical interpretation of work: W = F · d is force dot displacement. The line integral generalizes this to a force that varies along the path. Compute simple examples (straight lines, circular arcs) and verify the sign matches physical intuition — moving against a force field gives negative work.

## Common Misconceptions
- ∫_C F · dr depends on the orientation of C: ∫_{−C} F · dr = −∫_C F · dr.
- The integral ∫_C F · dr is not generally independent of the path from start to finish — path independence is the special property of conservative fields.
- F(r(t)) in the formula means evaluate F at the point r(t), substituting x = x(t), y = y(t), z = z(t).
