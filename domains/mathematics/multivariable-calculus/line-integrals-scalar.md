---
id: line-integrals-scalar
title: Line Integrals of Scalar Functions
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: arc-length-parametric
  type: hard
builds-toward:
- line-integrals-vector-fields
tags:
- line-integral
- arc-length
stage: formal-systems
status: validated
---

# Line Integrals of Scalar Functions

## Core Idea
The line integral ∫_C f ds integrates a scalar function along a curve, weighted by arc length. Parametrically: ∫_C f ds = ∫_a^b f(r(t)) ||r'(t)|| dt. This generalizes single-variable integration to curves.

## Questions

```yaml
- question: "A wire is shaped like a curve C with linear density f(x, y). You parametrize C two different ways: one traversal takes 2 seconds, another takes 6 seconds over the same path. What is the relationship between the two values of ∫_C f ds?"
  type: multiple-choice
  options:
    - "The slower traversal gives a larger value because more time elapses per unit length"
    - "They are equal — the |r'(t)| factor converts parameter speed to actual arc length, making the result independent of parametrization"
    - "The faster traversal gives a larger value because the speed term |r'(t)| is larger"
    - "They differ unless the parametrization is linear in t"
  answer: 1
  explanation: "The |r'(t)| factor is precisely what makes the scalar line integral parametrization-independent. A faster traversal has a larger |r'(t)|, but the dt interval is correspondingly compressed — the product |r'(t)| dt always equals the actual arc-length element ds. The integral measures mass (or total accumulated quantity) along the curve as a geometric object, not as a function of how you choose to traverse it."

- question: "You compute ∫_C f ds along a curve C from point A to point B. A classmate computes the same integral from B to A (reversing the direction). How do the two results compare?"
  type: multiple-choice
  options:
    - "The classmate's result is the negative of yours, because the direction of integration reversed"
    - "The classmate's result equals yours — scalar line integrals are orientation-independent"
    - "The classmate's result equals yours only if f is a constant function"
    - "The classmate's result is twice yours, because the path is traversed in the other direction"
  answer: 1
  explanation: "Unlike vector-field line integrals (where reversing direction negates the result because the dot product with r'(t) flips sign), scalar line integrals use |r'(t)| — the absolute value of the derivative — which is always positive regardless of direction. Both f and ds are unaffected by orientation, so ∫_C f ds is the same in either direction. This is the key structural difference between scalar and vector line integrals."

- question: "The scalar line integral ∫_C f ds gives the same numerical value regardless of which parametrization you choose for the curve C."
  type: true-false
  answer: true
  explanation: "This is a fundamental property of scalar line integrals. The |r'(t)| factor in the formula ∫_a^b f(r(t)) |r'(t)| dt acts as a 'speed correction' that converts changes in the parameter t into actual arc length. No matter how fast or slow you traverse the curve — as long as you traverse the same path — the product f(r(t)) · |r'(t)| dt accumulates the same total quantity along the curve."

- question: "The scalar line integral ∫_C f ds changes sign when the direction of traversal along C is reversed, just as a definite integral ∫_a^b f(x) dx changes sign when the limits are swapped."
  type: true-false
  answer: false
  explanation: "This is a common confusion between scalar and vector line integrals. In a single-variable integral, swapping limits introduces a negative sign. But in a scalar line integral, the arc-length element ds = |r'(t)| dt is always positive — reversing direction does NOT flip the sign. The correct analogy for sign-sensitive integrals is the vector line integral ∫_C F · dr, where reversing orientation negates the result because r'(t) (not |r'(t)|) appears in the formula."

- question: "Why must the |r'(t)| factor be included in the scalar line integral formula ∫_a^b f(r(t)) |r'(t)| dt, rather than just integrating f(r(t)) dt directly?"
  type: short-answer
  answer: "The parameter t is not arc length — it is an arbitrary label for positions on the curve. The factor |r'(t)| converts dt (a change in parameter) into ds (an actual infinitesimal length along the curve). Without it, you would be summing f values weighted by parameter increments, which depends on how fast you traverse the curve and gives different answers for different parametrizations. Including |r'(t)| ensures you are integrating f per unit of actual geometric length — giving a result that depends only on the curve as a set of points, not on the arbitrary choice of parameter."
  explanation: "Think of it physically: if f is mass per unit length of a wire, the mass of a tiny piece is f · (length of piece). The length of the piece is |r'(t)| dt, not dt itself. A fast parametrization compresses dt but has large |r'(t)|; a slow one expands dt but has small |r'(t)|. The product is always the same infinitesimal arc length. Omitting |r'(t)| would make the 'mass' calculation depend on traversal speed — a physically meaningless artifact."
```

## Explainer

From arc length, you know that the length of a curve C parametrized by r(t) for t ∈ [a, b] is ∫ₐᵇ |r'(t)| dt. This integral accumulates the infinitesimal arc-length element ds = |r'(t)| dt along the path. A **scalar line integral** ∫_C f ds does the same accumulation, but instead of adding up ds alone, it weights each piece of arc length by the value of the scalar function f at that point. Intuitively: if f(x, y, z) represents the linear density (mass per unit length) of a wire shaped like the curve C, then ∫_C f ds gives the total mass of the wire.

The parametric formula makes this concrete. Substitute the curve: f is evaluated at each point r(t) on the path, giving f(r(t)), and each infinitesimal bit of arc length is |r'(t)| dt. The integral becomes ∫ₐᵇ f(r(t)) |r'(t)| dt — an ordinary single-variable integral in t. The |r'(t)| factor is essential: it converts from "distance in parameter t" to "actual distance along the curve," which is what makes the result independent of how you choose to parametrize C. If you travel the same wire faster or slower, the mass doesn't change.

This independence from parametrization is a key feature. Unlike vector-field line integrals (which you'll study next and which do depend on the direction of traversal), scalar line integrals are purely geometric: ∫_C f ds depends on the curve as a set of points and on the function f, but not on the direction of travel or the speed of parametrization. Reversing the direction of C leaves ∫_C f ds unchanged, because both f and ds are unaffected by orientation.

The step from arc length to scalar line integrals is the conceptual bridge to all line integrals. Once you accept the idea of "sum up a quantity per unit length along a curve," the scalar line integral is natural. The vector-field line integral ∫_C F · dr comes next, but its formula ∫ₐᵇ F(r(t)) · r'(t) dt has a different character — the dot product with r'(t) (rather than |r'(t)|) incorporates both direction and magnitude, which is why vector line integrals measure work done and do depend on orientation.
