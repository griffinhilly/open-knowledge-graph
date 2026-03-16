---
id: greens-theorem
title: Green's Theorem
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: line-integrals-vector-fields
  type: hard
- id: double-integrals-cartesian
  type: hard
builds-toward:
- stokes-theorem
- divergence-theorem
tags:
- greens-theorem
- circulation
stage: formal-systems
status: draft
---

# Green's Theorem

## Core Idea
Green's theorem: ∮_C (P dx + Q dy) = ∬_D (Q_x - P_y) dA. This relates line integrals around a closed curve to a double integral of curl over the region, converting circulation to an area integral.

## Explainer

From line integrals over vector fields and double integrals, you have two seemingly unrelated tools. Line integrals measure cumulative effect along a path — work done by a force, circulation of a fluid. Double integrals sum quantities spread over a 2D region. **Green's theorem** bridges them: it says the circulation of a vector field around a closed curve equals the double integral of a local rotation quantity over the enclosed region. This is one of the deepest results in multivariable calculus, and its key intuition is that **boundary behavior is determined by interior behavior**.

To see why, think of the region D partitioned into many tiny squares. Around each tiny square, the line integral of the field measures the local circulation. When you tile adjacent squares together, the shared interior edges cancel — the contribution along an edge from one square runs in the opposite direction from the neighboring square. What survives is only the outer boundary: the entire interior cancels, leaving the circulation around the full perimeter C. So summing local circulation over all tiny cells gives exactly the boundary circulation. The double integral captures this summation, and the quantity being summed is the **2D curl** Q_x − P_y — the local rotation rate of the vector field at each point.

The quantity Q_x − P_y has a concrete meaning. If F = (P, Q) is a vector field representing fluid velocity, then Q_x − P_y measures how much the field rotates (curls) at a given point: Q_x measures how Q increases in the x-direction, and P_y measures how P increases in the y-direction. Their difference captures net rotation. A field with Q_x − P_y = 0 everywhere has no local rotation; it is called **irrotational** or **conservative**, and the line integral around any closed loop in the region is zero. Green's theorem makes this precise: ∮_C F·dr = ∬_D (curl F) dA, and if curl F = 0 everywhere, the right side is 0.

Green's theorem is a 2D special case of a family of theorems — all sharing the same deep structure: an integral over a region equals an integral over its boundary. The 3D versions are Stokes' theorem (relating surface integrals of curl to boundary line integrals) and the Divergence theorem (relating volume integrals of divergence to surface integrals). Learning to recognize this structure — "integrate something over the interior ↔ integrate something related on the boundary" — is the key to all the major theorems of vector calculus.
