---
id: space-curves
title: Space Curves and Tangent Vectors
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: vector-valued-functions-intro
  type: hard
- id: arc-length-parametric
  type: hard
builds-toward:
- parametric-surfaces
- stokes-theorem
tags:
- curves
- tangent
- geometry
stage: formal-systems
status: draft
---

# Space Curves and Tangent Vectors

## Core Idea
A space curve r(t) has tangent vector r'(t), which indicates direction of motion. Arc length parameterization uses s(t) as the parameter and gives unit tangent T(s) = dr/ds. Curvature κ measures how quickly the curve changes direction.

## Explainer

You already know that a **vector-valued function** r(t) = (x(t), y(t), z(t)) traces a path through three-dimensional space as t varies. The parameter t is often time, and r(t) records the position of a moving particle. The derivative r'(t) = (x'(t), y'(t), z'(t)) is the **tangent vector** — it points in the direction of motion and its magnitude ‖r'(t)‖ is the speed. This is a direct generalization of the single-variable derivative: just as f'(a) gives the slope of a curve in the plane, r'(t₀) gives the direction of motion along a space curve at the moment t₀.

The challenge with a parameter like t is that it is arbitrary. Two parametrizations of the same geometric curve — say, one traversed slowly and one quickly — produce different tangent vectors ‖r'(t)‖ (different speeds) even though they trace the same shape. To remove this parameter-dependence and focus purely on the geometry of the curve, we use **arc length parameterization**. The arc length s(t) = ∫₀ᵗ ‖r'(u)‖ du measures how far you have traveled along the curve. Reparametrizing by s gives a curve r(s) that always moves at unit speed: ‖dr/ds‖ = 1. The unit tangent **T**(s) = dr/ds now depends only on where you are on the curve, not on how fast you got there.

**Curvature** κ measures how sharply the curve bends. In arc length terms, κ = ‖dT/ds‖ — it is the rate at which the unit tangent vector changes direction as you walk along the curve at unit speed. A straight line has κ = 0 (the tangent never rotates). A circle of radius R has constant curvature κ = 1/R (tighter circles bend more sharply). An arbitrary space curve has varying curvature that characterizes its local geometry at each point. High curvature means the curve is turning quickly; low curvature means it is nearly straight.

Together, the tangent vector and curvature begin building what is called the **Frenet-Serret frame** — a moving coordinate system that travels with the curve and reveals its intrinsic geometry. Beyond curvature, a space curve (unlike a plane curve) can also twist out of a plane, measured by a quantity called torsion. These local geometric quantities — direction, bending, and twisting — completely characterize a space curve up to rigid motion. This geometric perspective connects back to arc length from your prerequisites and forward to the study of surfaces and Stokes' theorem, where curves appear as the boundaries of surfaces.
