---
id: differentials
title: Differentials
domain: mathematics
course: calculus-1
prerequisites:
  - id: linear-approximation
    type: hard
  - id: derivative-notation
    type: hard
builds-toward:
  - u-substitution
tags: [derivatives, differentials, approximation]
stage: formal-systems
status: validated
---

# Differentials

## Core Idea
If y = f(x), the differential dy = f'(x) dx represents the change in y along the tangent line for a small change dx in x. While the actual change in y is Delta_y = f(x + dx) - f(x), the differential dy approximates it: dy is approximately equal to Delta_y when dx is small. Differentials formalize the Leibniz notation and are used in error estimation, integration by substitution, and differential equations.

## How It's Best Learned
Compare Delta_y (actual change along the curve) with dy (change along the tangent line) graphically and numerically. Practice computing differentials: if y = x^3, then dy = 3x^2 dx. Apply to error propagation: if a measurement has error dx, estimate the error in a computed quantity.

## Common Misconceptions
- Confusing dy with Delta_y (dy is the linear approximation to the actual change).
- Treating dx as zero (it is small but nonzero).
- Not understanding the relationship between differentials and the chain rule / u-substitution.

## Explainer

You already know how to use the tangent line to approximate a function near a point — that's linear approximation. Differentials give that idea a precise algebraic form. If y = f(x), then **dx** is any small (but nonzero) change in x, and **dy** is defined as f′(x) dx: the corresponding change along the tangent line. The actual change in the function value is Δy = f(x + dx) − f(x), which follows the curve. The differential dy follows the tangent line instead, and when dx is small, dy ≈ Δy.

To compute a differential in practice, differentiate as normal and then attach dx. If y = x³, then dy = 3x² dx. If y = sin(x), then dy = cos(x) dx. The dx is not decorative — it is a variable in its own right, representing an increment in x. You can think of the familiar derivative notation dy/dx as a literal ratio of two differentials: the ratio of how much y changes (along the tangent) to how much x changes.

This reframing makes **u-substitution** in integration make sense. When you write u = x² and then compute du = 2x dx, you are computing a differential. The substitution replaces not just u but the entire dx-expression, capturing how the substitution changes the variable of integration. Without differentials, this step would seem like a notational trick; with them, it is a coherent change of variables.

Differentials also formalize **error propagation**. If you measure x with a small error dx, then the induced error in y = f(x) is approximately dy = f′(x) dx. For example, if you measure the radius of a sphere as r = 5 cm with an error of ±0.1 cm, the error in the volume V = (4/3)πr³ is approximately dV = 4πr² dr = 4π(25)(0.1) ≈ 31.4 cm³. This is linear approximation in applied form, and it is why scientists routinely use differentials to estimate measurement uncertainty.
