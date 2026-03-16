---
id: parametric-curves-calculus
title: Calculus of Parametric Curves
domain: mathematics
course: calculus-2
prerequisites:
  - id: parametric-equations-intro
    type: hard
  - id: chain-rule
    type: hard
builds-toward:
  - arc-length-parametric
tags: [parametric, derivatives, calculus]
stage: formal-systems
status: validated
---

# Calculus of Parametric Curves

## Core Idea
For parametric curves x = f(t), y = g(t), the slope of the tangent line is dy/dx = (dy/dt)/(dx/dt), applying the chain rule. The second derivative d^2y/dx^2 = (d/dt[dy/dx])/(dx/dt). These formulas let you find tangent lines, identify horizontal and vertical tangents, determine concavity, and locate extrema for parametrically defined curves without eliminating the parameter.

## How It's Best Learned
Derive dy/dx from the chain rule. Practice finding tangent lines to parametric curves (e.g., the cycloid). Identify horizontal tangents (dy/dt = 0) and vertical tangents (dx/dt = 0). Compute the second derivative for concavity analysis.

## Common Misconceptions
- Computing dy/dx as g(t)/f(t) instead of g'(t)/f'(t).
- Confusing horizontal tangent (dy/dt = 0) with vertical tangent (dx/dt = 0).
- Incorrectly computing the second derivative (it is not d^2y/dt^2 divided by d^2x/dt^2).

## Explainer

In standard calculus, y is a function of x, so dy/dx is computed directly. For a **parametric curve**, both x and y depend on a third variable t (time, angle, or a parameter). You have two rates: dx/dt (how fast x changes as t varies) and dy/dt (how fast y changes as t varies). To find the slope dy/dx — how y changes with respect to x along the curve — you apply the **chain rule**: dy/dx = (dy/dt) / (dx/dt). Think of it as a unit conversion: dy/dt has units of (y per t) and dx/dt has units of (x per t), so dividing cancels the t and gives (y per x) as desired.

The geometry of the tangent line follows naturally. A **horizontal tangent** requires dy/dx = 0, which happens when dy/dt = 0 (and dx/dt ≠ 0) — the curve is momentarily moving horizontally. A **vertical tangent** requires dy/dx to be undefined, which happens when dx/dt = 0 (and dy/dt ≠ 0) — the curve is momentarily moving vertically. When both derivatives are zero at the same t, the curve has a **singular point** requiring more careful analysis. These conditions tell you where the curve changes direction without eliminating the parameter.

The **second derivative** d²y/dx² measures concavity along the curve. It is not d²y/dt² divided by d²x/dt² — that would be the ratio of two second derivatives in t, which carries no geometric meaning. Instead, you treat d(dy/dx)/dt as a new "dy/dt" and divide by dx/dt: d²y/dx² = [d/dt(dy/dx)] / (dx/dt). The logic is the same chain rule applied again, but now to the quantity dy/dx rather than to y. Once you have the second derivative, concavity analysis proceeds exactly as in standard calculus — positive means concave up, negative means concave down.

A powerful payoff: many important curves (the cycloid, the ellipse, the astroid) have no clean Cartesian equation y = f(x) but are cleanly expressible parametrically. The calculus of parametric curves lets you find tangent lines, extrema, and concavity for all of them. Later, the same machinery extends to arc length and surface area integrals in parametric form, and it is the conceptual foundation for calculus on curves in polar coordinates and in space.
