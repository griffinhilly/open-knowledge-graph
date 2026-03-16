---
id: stiff-differential-equations
title: Stiff Differential Equations and Stability Regions
domain: mathematics
course: numerical-analysis
prerequisites:
- id: runge-kutta-methods-for-odes
  type: hard
tags:
- stiff-equations
- stability-region
- implicit-methods
stage: advanced
status: draft
---

# Stiff Differential Equations and Stability Regions

## Core Idea
Stiff ODEs have widely separated eigenvalues; fast modes force explicit methods to use tiny steps for stability, though slow modes change slowly. Implicit methods have larger stability regions, allowing larger steps. Stiffness is problem-dependent and characterized by the ratio of largest to smallest eigenvalue magnitudes times the integration interval length.

## Explainer

You already know Runge-Kutta methods: given y' = f(t, y), you estimate the next value by sampling f at several points within a step and taking a weighted average. The step size h controls the tradeoff between accuracy and computational cost. For most problems, a larger h means larger (but acceptable) error, and you can choose h to balance those concerns. **Stiff equations** break this tradeoff: they force you to use extremely small step sizes not because the solution changes rapidly, but because of stability requirements.

The key idea is that stiff equations have multiple timescales that differ drastically in speed. A classic example is the system y' = −1000y + z, z' = y − z. One component decays on timescale ~1/1000, while the other decays on timescale ~1. The "fast" component settles almost instantly to a quasi-steady state, but an explicit method like RK4 doesn't know this — it just sees the eigenvalue −1000 and demands h < 2/1000 = 0.002 for stability. If you're integrating the slow component over t ∈ [0, 1], you need at least 500 steps just to maintain stability, even though the solution of interest barely changes over that interval.

The **stability region** of a numerical method formalizes this constraint. Apply the method to the test equation y' = λy (where λ is a complex number with Re(λ) < 0). The stability region is the set of values hλ in the complex plane for which the numerical solution doesn't blow up. For explicit Euler, the stability region is a small disk around hλ = −1. For RK4, it's larger but still bounded. **Implicit methods** — like backward Euler or implicit Runge-Kutta schemes — can have stability regions that cover the entire left half-plane. This property is called **A-stability**, and it means the method remains stable for any h when the underlying problem is stable, regardless of how large |λ| is.

The tradeoff is that implicit methods require solving a (possibly nonlinear) system of equations at each step — typically via Newton's method — whereas explicit methods just evaluate f. For non-stiff problems this extra work is wasteful. For stiff problems it enables step sizes thousands of times larger than any explicit method could take. The practical test for stiffness is behavioral: if an explicit ODE solver takes far more steps than the solution's smoothness seems to require, your system is probably stiff and should be handed to an implicit solver such as SciPy's `solve_ivp` with `method='Radau'` or MATLAB's `ode15s`.
