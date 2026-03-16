---
id: higher-order-partials
title: Higher-Order Partial Derivatives
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: partial-derivatives
  type: hard
- id: higher-order-derivatives
  type: soft
builds-toward:
- clairaut-theorem
- hessian-matrix-second-derivative-test
tags:
- second-derivatives
- mixed-partials
- notation
stage: formal-systems
status: draft
---

# Higher-Order Partial Derivatives

## Core Idea
Higher-order partials are partial derivatives of partial derivatives: ∂²f/∂x², ∂²f/∂y², and mixed partials ∂²f/∂x∂y. Notation ∂²f/∂x∂y means first differentiate with respect to y, then x.

## Explainer

You already know that the partial derivative ∂f/∂x treats all variables other than x as constants and differentiates with respect to x alone. The resulting expression ∂f/∂x is itself a function of the same variables — which means you can differentiate it again. **Higher-order partial derivatives** are just iterated applications of this operation. The second partial ∂²f/∂x² differentiates with respect to x twice; physically, it measures how the rate of change in the x-direction itself changes as you move in the x-direction.

The richer case is the **mixed partial** ∂²f/∂x∂y, where you differentiate with respect to two different variables in succession. The notation is read right-to-left: ∂²f/∂x∂y means "first differentiate with respect to y, then differentiate the result with respect to x." Think of it as composition of operators: ∂/∂x applied to (∂f/∂y). Alternatively, the subscript notation f_xy means differentiate first in x, then in y — this one reads left-to-right, so be careful which convention a text is using. For the function f(x, y) = x²y³, computing f_xy: first f_x = 2xy³, then (f_x)_y = 6xy². Computing f_yx: first f_y = 3x²y², then (f_y)_x = 6xy². Same answer — this equality of mixed partials is not a coincidence.

For "well-behaved" functions (specifically when the mixed partials are continuous near a point), the order of differentiation doesn't matter: ∂²f/∂x∂y = ∂²f/∂y∂x. This is **Clairaut's theorem**, which you will prove next. Intuitively, it says that the change in slope from simultaneously wiggling x and y doesn't depend on which wiggle you think of as "first." The theorem requires continuity of the mixed partials — there exist pathological examples where the equality fails — but for all smooth functions encountered in practice, mixed partials commute freely.

Higher-order partials become essential in optimization and in understanding the local shape of a function near a critical point. The four second partials f_xx, f_xy, f_yx, and f_yy are assembled into the **Hessian matrix**, which plays the role that the second derivative plays in single-variable calculus. Just as f″(a) > 0 signals a local minimum in one dimension, the Hessian's eigenvalues (or equivalently its determinant and trace) tell you whether a critical point of a multivariable function is a local min, local max, or saddle point — which is why you need this topic before tackling the second derivative test.
