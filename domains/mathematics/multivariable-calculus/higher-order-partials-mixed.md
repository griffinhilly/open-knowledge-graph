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

## Questions

```yaml
- question: "For f(x,y), what does the notation ∂²f/∂y∂x mean — that is, in what order are the differentiations performed?"
  type: multiple-choice
  options:
    - "Differentiate with respect to y first, then with respect to x"
    - "Differentiate with respect to x first, then with respect to y"
    - "Take the second derivative with respect to both x and y simultaneously"
    - "Differentiate twice with respect to x, then twice with respect to y"
  answer: 1
  explanation: "Notation reads right-to-left: ∂²f/∂y∂x means ∂/∂y(∂f/∂x) — first differentiate with respect to x (the rightmost variable), then differentiate the resulting function with respect to y. This is the most common notational confusion with mixed partials. The expression ∂²f/∂x∂y (reversed) differentiates with respect to y first, then x."

- question: "A student computes ∂²f/∂x∂y and ∂²f/∂y∂x for a function f and gets different answers. A classmate says: 'You must have made an error — those are always equal.' Who is right?"
  type: multiple-choice
  options:
    - "The classmate — Clairaut's theorem guarantees equality for any function that has partial derivatives"
    - "The student — mixed partials always differ because the order of differentiation changes the result"
    - "The classmate might be wrong — equality is guaranteed only when both mixed partials exist and are continuous near the point"
    - "The student — the two expressions measure fundamentally different geometric quantities and need not agree"
  answer: 2
  explanation: "Clairaut's theorem requires that both mixed partials exist and are *continuous* near the point — it does not apply unconditionally. There exist pathological functions (such as f(x,y) = xy(x²−y²)/(x²+y²) at the origin) where both mixed partials exist at a point but disagree, because the continuity condition fails. For smooth functions encountered in most calculus settings, the condition holds and equality is guaranteed, but the classmate's 'always' is false."

- question: "The mixed partial derivative ∂²f/∂y∂x at a point measures how the rate of change of f in the x-direction varies as you move in the y-direction."
  type: true-false
  answer: true
  explanation: "Think of ∂f/∂x as the 'x-slope function' that varies across the domain. The mixed partial ∂²f/∂y∂x asks how this x-slope changes as y increases. If ∂²f/∂y∂x > 0, moving in the +y direction makes the function steeper in the x-direction. This 'interaction' interpretation is important for the Hessian: the off-diagonal entries capture how the partial slopes interact across variables, which determines whether a critical point is a saddle point or an extremum."

- question: "Clairaut's theorem guarantees that mixed partial derivatives commute for any function that has partial derivatives at a point — no additional conditions are required."
  type: true-false
  answer: false
  explanation: "The theorem requires continuity of the mixed partials in a neighborhood of the point, not just their existence at the point. The classic counterexample is f(x,y) = xy(x²−y²)/(x²+y²) for (x,y) ≠ (0,0) and f(0,0)=0: both f_xy(0,0) and f_yx(0,0) exist but equal +1 and −1 respectively, violating equality — and indeed the mixed partials are not continuous at the origin. For smooth (C² or better) functions, the continuity condition is automatic and commutativity holds."

- question: "What does it mean geometrically or conceptually when a mixed partial ∂²f/∂y∂x is large and positive at a point? What does this tell you about the function's behavior near that point?"
  type: short-answer
  answer: "A large positive ∂²f/∂y∂x means that the slope of f in the x-direction increases rapidly as y increases. In other words, moving in the +y direction makes the function much steeper in the x-direction. This indicates strong interaction between the two variables: the effect of changing x on f depends significantly on the current value of y. Functions with large mixed partials have surfaces that twist sharply — a 'saddle-like' coupling between the axes."
  explanation: "This interaction interpretation is why mixed partials appear in the Hessian matrix's off-diagonal entries and why the Hessian determinant (f_xx · f_yy − f_xy²) captures the trade-off between the pure second derivatives and the cross-coupling. When the mixed partial is zero, the two variables act independently near that point (the function is locally separable). When large, changes in one variable amplify sensitivity to the other."
```

## Explainer

You already know how to compute a partial derivative: fix all variables except one and differentiate with respect to that one variable. A **higher-order partial derivative** simply repeats this process. The second partial ∂²f/∂x² means differentiate with respect to x twice. The **mixed partial** ∂²f/∂y∂x means differentiate with respect to x first, then with respect to y. Notation reads right-to-left: differentiate the rightmost variable first.

To build intuition, think of ∂f/∂x as a new function — the "x-slope function" that tells you how steeply f rises in the x-direction at each point. The mixed partial ∂²f/∂y∂x asks: how does that x-slope *change* as you move in the y-direction? If ∂²f/∂y∂x > 0 at a point, it means that moving in the +y direction makes the x-slope steeper. Alternatively, ∂²f/∂x∂y asks how the y-slope changes as you move in x. These are questions about the *interaction* between the two variables — does being larger in one direction affect how sensitive the function is to the other direction?

**Clairaut's theorem** is the central result: if both mixed partials ∂²f/∂x∂y and ∂²f/∂y∂x exist and are **continuous** near a point, then they are equal there. For virtually all functions encountered in calculus, this continuity condition holds, so in practice you can differentiate in either order and get the same answer. The theorem is not trivially true — there exist pathological functions where the mixed partials exist but disagree — but those functions fail the continuity hypothesis. For smooth functions, order of differentiation is irrelevant.

The **Hessian matrix** is where higher-order partials become a tool. For f(x, y), the Hessian is the 2×2 matrix of second partials: [[∂²f/∂x², ∂²f/∂x∂y], [∂²f/∂y∂x, ∂²f/∂y²]]. By Clairaut's theorem, the Hessian is symmetric whenever the mixed partials are continuous. The second derivative test for critical points relies entirely on the Hessian — specifically on its determinant and leading entry — so computing higher-order partials accurately is the prerequisite skill for classifying local minima, maxima, and saddle points in multivariable calculus.
