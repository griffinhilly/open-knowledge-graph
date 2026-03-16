---
id: mixed-partials-clairaut
title: Mixed Partial Derivatives and Clairaut's Theorem
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: higher-order-partial-derivatives
  type: hard
builds-toward:
- critical-points-multivariable
- second-partials-test
tags:
- partials
- symmetry
stage: formal-systems
status: draft
---

# Mixed Partial Derivatives and Clairaut's Theorem

## Core Idea
Mixed partial derivatives are equal when they are continuous: ∂²f/∂x∂y = ∂²f/∂y∂x, by Clairaut's theorem. This equality simplifies computation and reflects symmetry in the function's behavior.

## Explainer

You already know how to compute higher-order partial derivatives: differentiate once with respect to one variable, then differentiate the result with respect to another. A **mixed partial derivative** ∂²f/∂x∂y means: first differentiate with respect to y (the rightmost variable in denominator notation), then differentiate with respect to x. The question is: does the order matter? Could ∂²f/∂x∂y differ from ∂²f/∂y∂x?

In general, for badly-behaved functions, the answer is yes — the mixed partials can differ. But for almost every function you encounter in practice, they are equal, and **Clairaut's theorem** (also called the symmetry of second derivatives or Schwarz's theorem) makes this precise: if both mixed partials ∂²f/∂x∂y and ∂²f/∂y∂x are continuous at a point, then they are equal at that point. Continuity of the mixed partials is the key condition — it is sufficient, though not necessary.

The intuition is that if f is smooth, then at the infinitesimal level, "how the x-slope changes in the y-direction" and "how the y-slope changes in the x-direction" both measure the same feature of the function's curvature. Think of a surface z = f(x, y): ∂²f/∂y∂x asks how the tilt in the x-direction changes as you move in the y-direction, while ∂²f/∂x∂y asks how the tilt in the y-direction changes as you move in the x-direction. For a smooth surface, both measure the same "twisting" of the surface, so they must agree.

The practical consequence is significant: for smooth functions, you can differentiate in whichever order is computationally convenient. This matters when computing the **Hessian matrix** H(f), whose (i, j) entry is ∂²f/∂xᵢ∂xⱼ. Clairaut's theorem guarantees that H is a **symmetric matrix** (H = Hᵀ) whenever the second partials are continuous — which gives the Hessian all the nice spectral properties of symmetric matrices, including real eigenvalues. This symmetry is directly used in the second partials test for classifying critical points as local maxima, minima, or saddle points, which is the next topic in your path.
