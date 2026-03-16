---
id: harmonic-functions-complex-analysis
title: Harmonic Functions
domain: mathematics
course: complex-analysis
prerequisites:
- id: cauchy-riemann-equations
  type: hard
builds-toward:
- harmonic-conjugates
tags:
- harmonic-functions
- laplace-equation
- pde
stage: advanced
status: draft
---

# Harmonic Functions

## Core Idea
A real-valued function u(x,y) is harmonic if ∇²u = ∂²u/∂x² + ∂²u/∂y² = 0. The real and imaginary parts of any holomorphic function are harmonic. Conversely, on simply connected domains, any harmonic function is the real part of some holomorphic function. Harmonic functions model steady-state heat and electrostatic potential.

## Explainer

Your prerequisite — the **Cauchy-Riemann equations** — says that a holomorphic function f(z) = u(x,y) + iv(x,y) must satisfy u_x = v_y and u_y = −v_x. This pair of constraints, combined with the assumption that the second partial derivatives are continuous, forces something remarkable about u and v individually. Differentiate the first equation with respect to x: u_xx = v_yx. Differentiate the second with respect to y: u_yy = −v_xy. Since mixed partials are equal (v_xy = v_yx), adding gives u_xx + u_yy = 0. The real part u automatically satisfies the **Laplace equation** ∇²u = 0. The same argument applied to v shows v is harmonic too.

A **harmonic function** is a real-valued function u(x,y) satisfying ∇²u = ∂²u/∂x² + ∂²u/∂y² = 0. The Laplace equation is the condition that a function has no local extrema in its interior — its value at any point equals the average of its values on any circle centered at that point. This **mean value property** is the geometric heart of harmonicity: harmonic functions are "balanced," never spiking or dipping in the interior of their domain. As a consequence, harmonic functions cannot have local maxima or minima in the interior — they achieve their extreme values only on the boundary (the **maximum principle**).

The connection runs both ways. Any holomorphic function yields a pair of harmonic functions (u and v). But on a **simply connected** domain (one with no holes), the converse holds: any harmonic function u is the real part of some holomorphic function f = u + iv, where v is called the **harmonic conjugate** of u. The harmonic conjugate is found by integrating the Cauchy-Riemann equations: v_x = −u_y and v_y = u_x. The simple connectedness is essential — on a domain with holes (like an annulus), harmonic functions may fail to have a single-valued conjugate globally.

The physical meaning anchors the abstraction. Harmonic functions describe **steady-state phenomena**: temperature distribution in a conducting plate after it has equilibrated, electrostatic potential in a region with no free charges, or fluid velocity potential in irrotational flow. In each case, "steady state" means no net flux accumulating at any interior point — exactly what ∇²u = 0 says analytically. This is why complex analysis, despite being pure mathematics, is an extraordinarily powerful tool for solving two-dimensional physics problems: every holomorphic function simultaneously solves two physical steady-state problems via its real and imaginary parts.
