---
id: exact-differential-equations
title: Exact Differential Equations
domain: mathematics
course: differential-equations
prerequisites:
- id: integrating-factor-method
  type: hard
- id: partial-derivatives
  type: soft
builds-toward:
- existence-uniqueness-ode
tags:
- exact-equations
- first-order
- partial-derivatives
stage: formal-systems
status: draft
---

# Exact Differential Equations

## Core Idea
An exact differential equation M(x,y)dx + N(x,y)dy = 0 satisfies ∂M/∂y = ∂N/∂x, indicating it comes from a potential function F(x,y) where dF = M dx + N dy. The solution is implicitly F(x,y) = C, found by integrating M with respect to x. For non-exact equations, an integrating factor can restore exactness.

## Questions

```yaml
- question: "The equation M(x,y)dx + N(x,y)dy = 0 is exact, with ∂M/∂y = ∂N/∂x. What form does its general solution take?"
  type: multiple-choice
  options:
    - "y = f(x) + C, found by integrating M with respect to x and solving for y"
    - "F(x, y) = C, where F is a potential function satisfying ∂F/∂x = M and ∂F/∂y = N"
    - "The solution is a parametric curve (x(t), y(t)) traced by the vector field (M, N)"
    - "x = g(y) + C, found by integrating N with respect to y and solving for x"
  answer: 1
  explanation: "Exactness means M dx + N dy is the total differential dF of some function F(x,y). So the equation is really just dF = 0 — saying that F is constant along solution curves. The general solution is therefore F(x,y) = C, an implicit equation defining level curves of F. Option A confuses the method of recovery with the form of the solution; options C and D reflect misunderstandings of what the exactness condition means geometrically."

- question: "When solving an exact equation, you integrate M with respect to x to get F(x, y) = ∫M dx + g(y). A student treats g(y) as an arbitrary constant rather than an unknown function. What goes wrong?"
  type: multiple-choice
  options:
    - "Nothing goes wrong — the constant of integration in a multivariable setting is always a pure constant"
    - "The solution will satisfy ∂F/∂x = M but will generally fail to satisfy ∂F/∂y = N, making F incorrect"
    - "The student will find too many solutions because g(y) introduces extra degrees of freedom"
    - "The integration step itself is invalid unless g(y) is confirmed to be constant by the exactness condition"
  answer: 1
  explanation: "When integrating M with respect to x in a two-variable setting, the 'constant' of integration can depend on y — any function g(y) has zero partial derivative with respect to x and therefore vanishes from ∂F/∂x. Treating g(y) as a pure constant loses this dependence, so the resulting F will satisfy ∂F/∂x = M but will fail ∂F/∂y = N in all but degenerate cases. The entire point of the second step — differentiating F with respect to y and setting it equal to N — is to determine what g(y) must be to satisfy both conditions simultaneously."

- question: "The exactness condition ∂M/∂y = ∂N/∂x is both necessary and sufficient for the equation M dx + N dy = 0 to have a potential function, provided the domain is simply connected."
  type: true-false
  answer: true
  explanation: "Necessity follows from the equality of mixed partials: if F exists with ∂F/∂x = M and ∂F/∂y = N, then ∂M/∂y = ∂²F/∂y∂x = ∂²F/∂x∂y = ∂N/∂x (by Clairaut's theorem for smooth F). Sufficiency on a simply connected domain follows from the fact that there are no 'holes' through which a path integral of M dx + N dy could be path-dependent. The simply connected condition is essential — on a domain with holes (like the punctured plane), ∂M/∂y = ∂N/∂x is necessary but not sufficient."

- question: "If ∂M/∂y ≠ ∂N/∂x, the equation M dx + N dy = 0 cannot be solved exactly but can always be made exact by multiplying through by an appropriate integrating factor."
  type: true-false
  answer: false
  explanation: "While an integrating factor μ(x,y) can sometimes restore exactness, finding one in general requires solving its own partial differential equation, which may be intractable. The practical special cases — where (∂M/∂y − ∂N/∂x)/N depends only on x, or (∂N/∂x − ∂M/∂y)/M depends only on y — cover many textbook problems but are not universally applicable. If neither simplification works, the exact equation framework may simply not be the right tool for that ODE."

- question: "Why must the unknown term g(y) in the step F(x, y) = ∫M dx + g(y) be an arbitrary function of y rather than a simple constant?"
  type: short-answer
  answer: "When integrating with respect to x, any function that depends only on y has zero partial derivative with respect to x and therefore vanishes from ∂F/∂x. A pure constant is just the special case where this y-dependent term happens to be constant, but in general the exact equation requires that ∂F/∂y = N, which places a specific constraint on how F must vary with y. The function g(y) is determined (up to a true constant) by differentiating ∫M dx + g(y) with respect to y, setting it equal to N, and integrating the result."
  explanation: "This step is the multivariable analogue of 'constant of integration' in single-variable calculus, but more subtle: instead of a number, the 'constant' with respect to x-integration can be any function of y. Recognizing this is the conceptual core of the method — it is what makes the two-step process work and why it produces a family of solutions F(x,y) = C rather than a single curve."
```

## Explainer

You have already worked with integrating factors to solve linear first-order ODEs, and you have seen partial derivatives as a tool for differentiating functions of two variables. Exact differential equations bring these ideas together. The central insight is that some ODEs are secretly just the statement dF = 0 in disguise — they say that some function F(x, y) is constant along solution curves. If you can find F, the solution is F(x, y) = C, and you never need to solve anything explicitly.

The equation M(x, y) dx + N(x, y) dy = 0 is **exact** if the expression M dx + N dy is the total differential of some function F. Recall from partial derivatives that the total differential of F(x, y) is dF = (∂F/∂x) dx + (∂F/∂y) dy. So exactness requires ∂F/∂x = M and ∂F/∂y = N simultaneously. The **exactness condition** ∂M/∂y = ∂N/∂x is then just the equality of mixed partials: ∂²F/∂y∂x = ∂²F/∂x∂y. If the mixed partials are equal (which Clairaut's theorem guarantees for smooth F), the equation is exact. This condition is both necessary and sufficient (on a simply connected domain), so checking ∂M/∂y = ∂N/∂x is the complete test for exactness.

Finding the **potential function** F follows a two-step integration process. Since ∂F/∂x = M, integrate M with respect to x: F(x, y) = ∫M dx + g(y). The unknown function g(y) (not a constant, but a function of y alone) accounts for the "constant of integration" in a multivariable setting. Then differentiate F with respect to y and set it equal to N: ∂F/∂y = (∂/∂y)∫M dx + g'(y) = N. This determines g'(y), which you integrate to find g(y). The solution is then F(x, y) = C implicitly. Note that this process only works when the exactness condition holds — if ∂M/∂y ≠ ∂N/∂x, no such F exists and the method fails cleanly.

When the equation is not exact, an **integrating factor** μ(x, y) can sometimes restore exactness by multiplying through: μM dx + μN dy = 0. Your prerequisite work with integrating factors for linear ODEs is a special case — those integrating factors depended on x alone. The general case is harder: finding μ requires solving its own PDE, which may be intractable. The practical strategy is to check whether (∂M/∂y − ∂N/∂x)/N depends only on x (which gives an integrating factor μ(x)), or whether (∂N/∂x − ∂M/∂y)/M depends only on y (giving μ(y)). If neither simplification works, exact equations may not be the right approach for that particular ODE.
