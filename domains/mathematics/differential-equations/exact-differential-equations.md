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

## Explainer

You have already worked with integrating factors to solve linear first-order ODEs, and you have seen partial derivatives as a tool for differentiating functions of two variables. Exact differential equations bring these ideas together. The central insight is that some ODEs are secretly just the statement dF = 0 in disguise — they say that some function F(x, y) is constant along solution curves. If you can find F, the solution is F(x, y) = C, and you never need to solve anything explicitly.

The equation M(x, y) dx + N(x, y) dy = 0 is **exact** if the expression M dx + N dy is the total differential of some function F. Recall from partial derivatives that the total differential of F(x, y) is dF = (∂F/∂x) dx + (∂F/∂y) dy. So exactness requires ∂F/∂x = M and ∂F/∂y = N simultaneously. The **exactness condition** ∂M/∂y = ∂N/∂x is then just the equality of mixed partials: ∂²F/∂y∂x = ∂²F/∂x∂y. If the mixed partials are equal (which Clairaut's theorem guarantees for smooth F), the equation is exact. This condition is both necessary and sufficient (on a simply connected domain), so checking ∂M/∂y = ∂N/∂x is the complete test for exactness.

Finding the **potential function** F follows a two-step integration process. Since ∂F/∂x = M, integrate M with respect to x: F(x, y) = ∫M dx + g(y). The unknown function g(y) (not a constant, but a function of y alone) accounts for the "constant of integration" in a multivariable setting. Then differentiate F with respect to y and set it equal to N: ∂F/∂y = (∂/∂y)∫M dx + g'(y) = N. This determines g'(y), which you integrate to find g(y). The solution is then F(x, y) = C implicitly. Note that this process only works when the exactness condition holds — if ∂M/∂y ≠ ∂N/∂x, no such F exists and the method fails cleanly.

When the equation is not exact, an **integrating factor** μ(x, y) can sometimes restore exactness by multiplying through: μM dx + μN dy = 0. Your prerequisite work with integrating factors for linear ODEs is a special case — those integrating factors depended on x alone. The general case is harder: finding μ requires solving its own PDE, which may be intractable. The practical strategy is to check whether (∂M/∂y − ∂N/∂x)/N depends only on x (which gives an integrating factor μ(x)), or whether (∂N/∂x − ∂M/∂y)/M depends only on y (giving μ(y)). If neither simplification works, exact equations may not be the right approach for that particular ODE.
