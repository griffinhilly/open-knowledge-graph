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
status: validated
---

# Partial Derivatives and Partial Differential Operators

## Core Idea
The partial derivative ∂f/∂x is the rate of change of f with respect to x, holding y constant. Geometrically, it's the slope of the surface f(x, y) in the x-direction. Higher partial derivatives exist: ∂²f/∂x², ∂²f/∂x∂y, etc.

## Questions

```yaml
- question: "A function f(x, y) has both partial derivatives ∂f/∂x and ∂f/∂y defined at the origin. A student concludes that f must be differentiable there and applies the chain rule to a composition involving f. What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "Nothing — if both partial derivatives exist, the function is automatically differentiable"
    - "The partial derivatives must also be continuous at the origin for differentiability to follow"
    - "Differentiability requires the gradient ∇f to equal zero at the point"
    - "Partial derivatives can only be used with the chain rule if f has three or more variables"
  answer: 1
  explanation: "Existence of partial derivatives is weaker than full differentiability. A function can have both ∂f/∂x and ∂f/∂y at a point and still fail to be continuous there — let alone differentiable. Full differentiability (the linear approximation holding in all directions) requires the partial derivatives to exist *and* be continuous in a neighborhood of the point (sufficient condition). Option A is the classic error: confusing the partial-derivative existence condition with full multivariable differentiability."

- question: "For f(x, y) = x²y³ + sin(y), what is ∂f/∂x?"
  type: multiple-choice
  options:
    - "2xy³ + cos(y)"
    - "2xy³"
    - "x²·3y² + cos(y)"
    - "2x·3y² + cos(y)"
  answer: 1
  explanation: "To compute ∂f/∂x, treat y as a constant and differentiate with respect to x. The term x²y³ differentiates to 2xy³ (y³ is just a constant factor). The term sin(y) contains no x, so its partial derivative with respect to x is zero — it vanishes entirely. Option A is wrong because cos(y) would only appear if we were differentiating sin(y) with respect to y."

- question: "Geometrically, the partial derivative ∂f/∂x at a point (a, b) gives the slope of the curve formed by the intersection of the surface z = f(x, y) with the plane y = b."
  type: true-false
  answer: true
  explanation: "This is exactly the geometric meaning of ∂f/∂x. Freezing y = b slices the surface with a vertical plane parallel to the xz-plane; the result is a curve in that plane. The partial derivative ∂f/∂x at (a, b) is the slope (tangent slope) of that curve at x = a. Analogously, ∂f/∂y gives the slope of the curve formed by the plane x = a."

- question: "If both partial derivatives ∂f/∂x and ∂f/∂y exist at a point, the function f must be continuous at that point."
  type: true-false
  answer: false
  explanation: "This is a common and important false belief. A standard counterexample is f(x, y) = xy/(x² + y²) for (x,y) ≠ (0,0) and f(0,0) = 0. Both partial derivatives exist at the origin (each is 0), but the function is not continuous there — approaching along y = x gives a different limit than approaching along y = 0. Partial derivatives only measure behavior along coordinate axes; they can exist even when the function misbehaves in other directions."

- question: "What is Clairaut's theorem, and what condition makes it applicable?"
  type: short-answer
  answer: "Clairaut's theorem states that the mixed partial derivatives ∂²f/∂x∂y and ∂²f/∂y∂x are equal — the order of differentiation does not matter. The condition is that both mixed partials must be continuous at the point in question."
  explanation: "Without the continuity condition, the mixed partials can differ. Clairaut's theorem is extremely useful in practice because it halves the work when computing multiple mixed partials — you can choose whichever order is algebraically easier. It also underlies many results in multivariable calculus where swapping differentiation order is needed (e.g., in the derivation of the gradient and in checking integrability conditions for differential equations)."
```

## Explainer

You've already encountered partial derivatives in their basic form — holding one variable fixed and differentiating with respect to the other. This topic formalizes that intuition and introduces the operator notation that makes multivariable calculus readable. The **partial derivative** ∂f/∂x at a point (a, b) is the ordinary derivative of the single-variable function g(x) = f(x, b) at x = a: you literally freeze y = b and differentiate as if f were a one-variable function of x alone. Every technique from single-variable differentiation applies unchanged to this frozen slice.

Geometrically, the surface z = f(x, y) can be cut by vertical planes. The plane y = b slices the surface along a curve; ∂f/∂x gives the slope of that curve in the x-direction. The plane x = a slices a different curve; ∂f/∂y gives its slope in the y-direction. Together, these two slopes describe how the surface tilts along the coordinate axes, but they do not yet capture all directions — that is the role of the **gradient** ∇f = ⟨∂f/∂x, ∂f/∂y⟩, which packages both partials into a single object pointing in the direction of steepest ascent.

Higher-order partial derivatives extend the idea by differentiating again. ∂²f/∂x² measures concavity in the x-direction; the **mixed partial** ∂²f/∂x∂y differentiates first with respect to y, then with respect to x. **Clairaut's theorem** says these mixed partials are equal (∂²f/∂x∂y = ∂²f/∂y∂x) whenever both are continuous — a symmetry that simplifies many calculations. Higher combinations of partial operators appear in important expressions: the **Laplacian** Δf = ∂²f/∂x² + ∂²f/∂y² governs heat flow, electrostatics, and wave propagation.

One important subtlety: the existence of ∂f/∂x and ∂f/∂y at a point does *not* guarantee that f is differentiable there in the full multivariable sense. Full differentiability requires that the linear approximation holds in all directions simultaneously, not just along coordinate axes. A function can have both partial derivatives at a point and still fail to be continuous there. Keeping this distinction clear prevents errors when you later need to invoke the chain rule or total derivative in more complex settings.
