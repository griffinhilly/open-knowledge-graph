---
id: double-integrals-cartesian
title: Double Integrals in Cartesian Coordinates
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: definite-integral-definition
  type: hard
- id: riemann-sums
  type: hard
- id: functions-of-several-variables
  type: hard
builds-toward:
- iterated-integrals
- double-integrals-polar
- jacobian-change-of-variables
- greens-theorem
tags:
- double-integral
- volume
- Riemann-sum
- integration
stage: formal-systems
status: validated
---

# Double Integrals in Cartesian Coordinates

## Core Idea
The double integral ∬_R f(x, y) dA is defined as the limit of double Riemann sums over a region R in ℝ². When f ≥ 0, it equals the volume of the solid bounded above by the surface z = f(x, y) and below by R. Double integrals also measure signed volume, average value, mass (when f is a density function), and surface area. The definition parallels the single-variable integral but requires partitioning a 2D region into small rectangles of area ΔA = ΔxΔy.

## How It's Best Learned
Begin by interpreting the double integral as volume — students who can visualize solids will have strong intuition. Then introduce double Riemann sums as direct analogues of single-variable Riemann sums. The shift from computing to setting up integrals is the major skill to develop, and this requires careful attention to region description.

## Common Misconceptions
- The order of integration matters for the limits, not for the value: switching order requires re-describing the region in the new order.
- Double integrals over non-rectangular regions require careful attention to variable limits.
- The integrand f(x,y) = 1 gives the area of R, not 1 — this is because dA already encodes area.
