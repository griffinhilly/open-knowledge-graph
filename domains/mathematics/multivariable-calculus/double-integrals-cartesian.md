---
id: double-integrals-cartesian
title: Double Integrals in Cartesian Coordinates
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: iterated-integrals
  type: hard
builds-toward:
- double-integrals-polar
- area-volume-integrals
tags:
- double-integral
- area-volume
stage: formal-systems
status: draft
---

# Double Integrals in Cartesian Coordinates

## Core Idea
The double integral ∬_R f(x,y) dA gives the volume under z = f(x,y) above region R. For non-rectangular regions, bounds depend on neighboring variables: ∫_a^b ∫_{g₁(x)}^{g₂(x)} f(x,y) dy dx.

## Explainer

You already know how to compute **iterated integrals** — integrals computed step by step, one variable at a time. A double integral over a rectangular region is just an iterated integral where the bounds are all constants: ∫_a^b ∫_c^d f(x,y) dy dx means "for each fixed x in [a,b], integrate f(x,y) over y from c to d, then integrate the result over x." Fubini's theorem guarantees that for well-behaved f you can switch the order of integration freely on a rectangle, and the answer is the same either way.

The more interesting case — and the one requiring real care — is integration over **non-rectangular regions**. The region R might be bounded above by a curve y = g₂(x) and below by y = g₁(x), for x running from a to b. For a given x, y only ranges from g₁(x) to g₂(x), not all the way from c to d. So the inner integral's limits become functions of x: ∫_a^b [∫_{g₁(x)}^{g₂(x)} f(x,y) dy] dx. The inner integral (in y) is computed first with x treated as a constant, producing a function of x alone. Then the outer integral finishes the job. Think of slicing the region R into thin vertical strips of width dx; for each strip at position x, you integrate f from the bottom boundary curve up to the top boundary curve.

You can also slice horizontally: fix y and let x run from some left boundary h₁(y) to some right boundary h₂(y), then integrate over y. The choice of orientation depends on which gives simpler limits. A region bounded by y = x and y = x² from x = 0 to x = 1 is easy to describe with vertical slices (x from 0 to 1, y from x² to x) and awkward to describe with horizontal slices. Always sketch the region first, then decide which slicing direction gives cleaner limits.

The geometric meaning reinforces the algebra. If f(x,y) ≥ 0, then ∬_R f(x,y) dA is the volume of the solid above R and below the surface z = f(x,y). When f = 1, ∬_R 1 dA = area of R — the double integral reduces to an area formula. More generally, if f represents a surface density (mass per unit area), then the double integral gives total mass. These physical interpretations are a useful check: if your computed volume is negative or your computed area is enormous, something has gone wrong with the limits.
