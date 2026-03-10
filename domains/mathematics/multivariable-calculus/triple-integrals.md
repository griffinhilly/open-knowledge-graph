---
id: triple-integrals
title: Triple Integrals in Cartesian Coordinates
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: iterated-integrals
  type: hard
- id: functions-of-several-variables
  type: hard
builds-toward:
- triple-integrals-cylindrical-spherical
- jacobian-change-of-variables
tags:
- triple-integral
- volume
- mass
- iterated-integral
stage: formal-systems
status: draft
---

# Triple Integrals in Cartesian Coordinates

## Core Idea
A triple integral ∭_E f(x, y, z) dV integrates a function over a three-dimensional solid region E. When f = 1, the triple integral gives the volume of E; when f is a density function, it gives total mass. Triple integrals are computed as iterated integrals — three nested ordinary integrals — with limits that describe the 3D region. There are six possible orders of integration (xyz, xzy, yxz, yzx, zxy, zyx), and the choice affects the difficulty of setting up limits.

## How It's Best Learned
Start with box regions where all limits are constants, then move to more complex regions. Sketching the 3D solid is essential but challenging; use cross-sections to determine integration limits systematically. Students should practice determining the limits for at least two different integration orders for the same region.

## Common Misconceptions
- Setting up limits for 3D regions is significantly harder than for 2D — the outermost variable must have constant limits, and each inner variable's limits may depend on all outer variables.
- Triple integrals of density functions give mass, not volume; ∭ dV = volume only when the integrand is 1.
- The choice of integration order does not change the value but can dramatically change the difficulty of computation.
