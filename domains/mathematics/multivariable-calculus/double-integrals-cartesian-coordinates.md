---
id: double-integrals-cartesian-coordinates
title: Double Integrals over Rectangular Regions
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: multivariable-functions-intro-domain
  type: hard
- id: double-integrals-cartesian
  type: hard
builds-toward:
- double-integrals-general-regions
tags:
- double-integrals
- integration
- cartesian
stage: formal-systems
status: draft
---

# Double Integrals over Rectangular Regions

## Core Idea
For a rectangle R = [a, b] × [c, d], the double integral ∬_R f(x, y) dA equals the iterated integral ∫_a^b ∫_c^d f(x, y) dy dx. By Fubini's theorem, the order of integration can be switched if f is continuous. The integral represents signed volume under the surface.

## Explainer

From your study of multivariable functions, you know that a function f(x, y) assigns a height to each point (x, y) in the plane, producing a surface in three dimensions. The **double integral** ∬_R f(x, y) dA asks: what is the signed volume of the solid region between the surface z = f(x, y) and the xy-plane, over the region R? Just as the single-variable integral sums up infinitely many thin rectangular strips (each of width dx and height f(x)), the double integral sums up infinitely many thin rectangular columns (each of base area dA = dx dy and height f(x, y)).

For a rectangular region R = [a, b] × [c, d], the calculation proceeds by **iterated integration**. Fix x for a moment and integrate f(x, y) with respect to y from c to d — this gives the area of a cross-sectional "slice" of the solid at that x-value, A(x) = ∫_c^d f(x, y) dy. Now sweep x from a to b, integrating A(x): ∫_a^b A(x) dx = ∫_a^b [ ∫_c^d f(x, y) dy ] dx. The outer integral adds up all the cross-sectional areas, giving the total volume. This "slice and sweep" thinking is the same as the washer/shell methods from single-variable calculus — integrate a cross-section, then integrate those cross-sections.

**Fubini's theorem** guarantees that for continuous f (and more generally for integrable f), the order of integration can be reversed: ∫_a^b ∫_c^d f(x, y) dy dx = ∫_c^d ∫_a^b f(x, y) dx dy. Both orders give the same number because they are both computing the same volume; they just slice it in perpendicular directions. Choosing the better order can make a computation dramatically easier — sometimes one order leads to an elementary antiderivative and the other does not.

The machinery here is used constantly: integrals over non-rectangular regions (your next topic) require adjusting the limits of the inner integral as a function of the outer variable, but the iterated-integral structure remains. Double integrals also compute mass (when f is density), expected values in probability, and areas (when f = 1). The key skill to develop is correctly setting up the limits — draw the region, decide which variable is "outer" (fixed while the inner integral runs), and read the inner limits as functions of the outer variable from the boundary of the region.
