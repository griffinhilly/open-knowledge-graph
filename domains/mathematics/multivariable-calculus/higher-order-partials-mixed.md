---
id: higher-order-partials-mixed
title: Higher-Order Partial Derivatives and Mixed Partials
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: partial-derivatives-definition
  type: hard
builds-toward:
- hessian-matrix-second-test
tags:
- higher-order
- mixed-partials
- clairaut
stage: formal-systems
status: draft
---

# Higher-Order Partial Derivatives and Mixed Partials

## Core Idea
Mixed partial derivatives ∂²f/∂x∂y and ∂²f/∂y∂x measure rate of change in two different variables. Clairaut's theorem states that if mixed partials are continuous, then ∂²f/∂x∂y = ∂²f/∂y∂x (they commute).

## Explainer

You already know how to compute a partial derivative: fix all variables except one and differentiate with respect to that one variable. A **higher-order partial derivative** simply repeats this process. The second partial ∂²f/∂x² means differentiate with respect to x twice. The **mixed partial** ∂²f/∂y∂x means differentiate with respect to x first, then with respect to y. Notation reads right-to-left: differentiate the rightmost variable first.

To build intuition, think of ∂f/∂x as a new function — the "x-slope function" that tells you how steeply f rises in the x-direction at each point. The mixed partial ∂²f/∂y∂x asks: how does that x-slope *change* as you move in the y-direction? If ∂²f/∂y∂x > 0 at a point, it means that moving in the +y direction makes the x-slope steeper. Alternatively, ∂²f/∂x∂y asks how the y-slope changes as you move in x. These are questions about the *interaction* between the two variables — does being larger in one direction affect how sensitive the function is to the other direction?

**Clairaut's theorem** is the central result: if both mixed partials ∂²f/∂x∂y and ∂²f/∂y∂x exist and are **continuous** near a point, then they are equal there. For virtually all functions encountered in calculus, this continuity condition holds, so in practice you can differentiate in either order and get the same answer. The theorem is not trivially true — there exist pathological functions where the mixed partials exist but disagree — but those functions fail the continuity hypothesis. For smooth functions, order of differentiation is irrelevant.

The **Hessian matrix** is where higher-order partials become a tool. For f(x, y), the Hessian is the 2×2 matrix of second partials: [[∂²f/∂x², ∂²f/∂x∂y], [∂²f/∂y∂x, ∂²f/∂y²]]. By Clairaut's theorem, the Hessian is symmetric whenever the mixed partials are continuous. The second derivative test for critical points relies entirely on the Hessian — specifically on its determinant and leading entry — so computing higher-order partials accurately is the prerequisite skill for classifying local minima, maxima, and saddle points in multivariable calculus.
