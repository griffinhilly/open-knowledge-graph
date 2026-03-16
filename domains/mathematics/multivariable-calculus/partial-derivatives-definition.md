---
id: partial-derivatives-definition
title: Partial Derivatives and Partial Differential Operators
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: partial-derivatives
  type: hard
builds-toward:
- higher-order-partials-mixed
- chain-rule-multivariable
tags:
- partial-derivatives
- operators
- derivatives
stage: formal-systems
status: draft
---

# Partial Derivatives and Partial Differential Operators

## Core Idea
The partial derivative ∂f/∂x is the rate of change of f with respect to x, holding y constant. Geometrically, it's the slope of the surface f(x, y) in the x-direction. Higher partial derivatives exist: ∂²f/∂x², ∂²f/∂x∂y, etc.

## Explainer

You've already encountered partial derivatives in their basic form — holding one variable fixed and differentiating with respect to the other. This topic formalizes that intuition and introduces the operator notation that makes multivariable calculus readable. The **partial derivative** ∂f/∂x at a point (a, b) is the ordinary derivative of the single-variable function g(x) = f(x, b) at x = a: you literally freeze y = b and differentiate as if f were a one-variable function of x alone. Every technique from single-variable differentiation applies unchanged to this frozen slice.

Geometrically, the surface z = f(x, y) can be cut by vertical planes. The plane y = b slices the surface along a curve; ∂f/∂x gives the slope of that curve in the x-direction. The plane x = a slices a different curve; ∂f/∂y gives its slope in the y-direction. Together, these two slopes describe how the surface tilts along the coordinate axes, but they do not yet capture all directions — that is the role of the **gradient** ∇f = ⟨∂f/∂x, ∂f/∂y⟩, which packages both partials into a single object pointing in the direction of steepest ascent.

Higher-order partial derivatives extend the idea by differentiating again. ∂²f/∂x² measures concavity in the x-direction; the **mixed partial** ∂²f/∂x∂y differentiates first with respect to y, then with respect to x. **Clairaut's theorem** says these mixed partials are equal (∂²f/∂x∂y = ∂²f/∂y∂x) whenever both are continuous — a symmetry that simplifies many calculations. Higher combinations of partial operators appear in important expressions: the **Laplacian** Δf = ∂²f/∂x² + ∂²f/∂y² governs heat flow, electrostatics, and wave propagation.

One important subtlety: the existence of ∂f/∂x and ∂f/∂y at a point does *not* guarantee that f is differentiable there in the full multivariable sense. Full differentiability requires that the linear approximation holds in all directions simultaneously, not just along coordinate axes. A function can have both partial derivatives at a point and still fail to be continuous there. Keeping this distinction clear prevents errors when you later need to invoke the chain rule or total derivative in more complex settings.
