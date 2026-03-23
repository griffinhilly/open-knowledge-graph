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
status: validated
---

# Higher-Order Partial Derivatives

## Core Idea
Higher-order partials are partial derivatives of partial derivatives: ∂²f/∂x², ∂²f/∂y², and mixed partials ∂²f/∂x∂y. Notation ∂²f/∂x∂y means first differentiate with respect to y, then x.

## Questions

```yaml
- question: "For f(x, y) = x³y², what operation does the notation ∂²f/∂x∂y instruct you to perform?"
  type: multiple-choice
  options:
    - "Differentiate with respect to x first, then with respect to y"
    - "Differentiate with respect to y first, then with respect to x"
    - "Differentiate with respect to both x and y simultaneously"
    - "Take the second derivative with respect to x and multiply by the second derivative with respect to y"
  answer: 1
  explanation: "The Leibniz notation ∂²f/∂x∂y is read right-to-left: the variable closest to f (on the right) is differentiated first. So ∂²f/∂x∂y means: first differentiate f with respect to y, then differentiate the result with respect to x. The subscript notation reverses this: f_xy means differentiate x first, then y (left-to-right). So f_xy and ∂²f/∂y∂x represent the same operation. Mixing up these conventions is one of the most common errors with higher-order partials."

- question: "A student computes f_x = 4x³y for f(x,y) = x⁴y. To find the mixed partial f_xy, she should next differentiate with respect to:"
  type: multiple-choice
  options:
    - "x again, giving 12x²y"
    - "y, giving 4x³"
    - "both x and y, taking the product of the results"
    - "x, then negate the result to account for the mixed direction"
  answer: 1
  explanation: "f_xy means differentiate x first, then y. She has already completed the first step (f_x = 4x³y). The second step is to differentiate with respect to y, treating x as a constant: ∂(4x³y)/∂y = 4x³. This equals f_yx by Clairaut's theorem — verifiable by computing f_y = x⁴, then ∂(x⁴)/∂x = 4x³. ✓"

- question: "If the mixed partials ∂²f/∂x∂y and ∂²f/∂y∂x are both continuous near a point, they must be equal there."
  type: true-false
  answer: true
  explanation: "True — this is Clairaut's theorem. Under the condition that mixed partials are continuous near a point, differentiation order doesn't matter. This is not automatic for all functions — pathological examples exist where the equality fails at points of discontinuity — but for all smooth functions (polynomial, trigonometric, exponential) encountered in practice, mixed partials commute freely."

- question: "The subscript notation f_xy and the Leibniz notation ∂²f/∂x∂y instruct you to differentiate with respect to x first."
  type: true-false
  answer: false
  explanation: "False — the two notations use opposite reading conventions. In subscript notation f_xy, you differentiate with respect to x first, then y (left-to-right). In Leibniz notation ∂²f/∂x∂y, you differentiate with respect to y first, then x (right-to-left). So f_xy corresponds to ∂²f/∂y∂x in Leibniz notation. Confusing these conventions is one of the most common errors with higher-order partials."

- question: "Why does the order of differentiation not matter for mixed partials of smooth functions, and when would you need to check whether this equality holds?"
  type: short-answer
  answer: "For smooth functions, Clairaut's theorem guarantees ∂²f/∂x∂y = ∂²f/∂y∂x because the mixed partial measures an interaction — how the rate of change in one direction varies as you move in another — and for well-behaved functions this interaction is symmetric. You need to check whether equality holds when the mixed partials might be discontinuous: at corners, cusps, or points defined piecewise where the function or its derivatives may not be smooth."
  explanation: "The theorem's hypothesis (continuity of mixed partials) is automatically satisfied by all elementary functions everywhere they are defined. Checking becomes necessary only for functions constructed piecewise or near singular points. In practice, verifying continuity of mixed partials is required only in pathological examples designed to violate Clairaut's theorem."
```

## Explainer

You already know that the partial derivative ∂f/∂x treats all variables other than x as constants and differentiates with respect to x alone. The resulting expression ∂f/∂x is itself a function of the same variables — which means you can differentiate it again. **Higher-order partial derivatives** are just iterated applications of this operation. The second partial ∂²f/∂x² differentiates with respect to x twice; physically, it measures how the rate of change in the x-direction itself changes as you move in the x-direction.

The richer case is the **mixed partial** ∂²f/∂x∂y, where you differentiate with respect to two different variables in succession. The notation is read right-to-left: ∂²f/∂x∂y means "first differentiate with respect to y, then differentiate the result with respect to x." Think of it as composition of operators: ∂/∂x applied to (∂f/∂y). Alternatively, the subscript notation f_xy means differentiate first in x, then in y — this one reads left-to-right, so be careful which convention a text is using. For the function f(x, y) = x²y³, computing f_xy: first f_x = 2xy³, then (f_x)_y = 6xy². Computing f_yx: first f_y = 3x²y², then (f_y)_x = 6xy². Same answer — this equality of mixed partials is not a coincidence.

For "well-behaved" functions (specifically when the mixed partials are continuous near a point), the order of differentiation doesn't matter: ∂²f/∂x∂y = ∂²f/∂y∂x. This is **Clairaut's theorem**, which you will prove next. Intuitively, it says that the change in slope from simultaneously wiggling x and y doesn't depend on which wiggle you think of as "first." The theorem requires continuity of the mixed partials — there exist pathological examples where the equality fails — but for all smooth functions encountered in practice, mixed partials commute freely.

Higher-order partials become essential in optimization and in understanding the local shape of a function near a critical point. The four second partials f_xx, f_xy, f_yx, and f_yy are assembled into the **Hessian matrix**, which plays the role that the second derivative plays in single-variable calculus. Just as f″(a) > 0 signals a local minimum in one dimension, the Hessian's eigenvalues (or equivalently its determinant and trace) tell you whether a critical point of a multivariable function is a local min, local max, or saddle point — which is why you need this topic before tackling the second derivative test.
