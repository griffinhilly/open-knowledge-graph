---
id: stiff-equations
title: Stiff Differential Equations
domain: mathematics
course: numerical-analysis
prerequisites:
- id: multistep-methods-adams
  type: hard
builds-toward:
- stability-regions-ode
tags:
- stiff-equations
- ode
- eigenvalues
stage: abstract-reasoning
status: draft
---

# Stiff Differential Equations

## Core Idea
A system dy/dt = f(t,y) is stiff if it contains vastly different time scales—some components decay rapidly while others change slowly. The stiffness ratio is proportional to the ratio of largest to smallest eigenvalue magnitudes of the Jacobian. Explicit methods must use tiny steps for stability, making implicit methods (which are A-stable) necessary for practical stiff ODE solving.

## Explainer

From Adams methods and other multistep schemes, you learned that step size h is constrained both by accuracy (you want h small enough to capture the solution's features) and by **stability** (taking h too large causes the numerical solution to blow up spuriously). For most ODEs, these two constraints are compatible: the step size required for accuracy is similar to the step size required for stability. Stiff equations break this compatibility in a dramatic way.

Imagine a chemical reaction network where some species decay with a half-life of microseconds while others persist for hours. The solution you *care about* changes on the scale of hours, so accuracy only requires time steps of, say, minutes. But the rapidly-decaying transients impose a stability requirement: explicit methods like Adams-Bashforth must take steps tiny enough to track those microsecond decays — even after those species have essentially vanished and no longer affect the solution. The fast components force tiny steps even though they carry no useful information. This is stiffness: **the stability requirement is far more stringent than the accuracy requirement**.

Mathematically, stiffness is measured through the **Jacobian** ∂f/∂y of the right-hand side. The eigenvalues λᵢ of this Jacobian determine the characteristic time scales of the system — each eigenvalue contributes a mode that evolves like e^(λᵢt). The **stiffness ratio** is roughly max|Re(λᵢ)|/min|Re(λᵢ)|; ratios of 10⁶ or larger are not uncommon in practical problems (circuit simulation, chemical kinetics, mechanical systems with contact). For an explicit method with stability region |1 + hλ| ≤ 1, the large eigenvalues force h|λ_max| to stay within the stability region — meaning h must be smaller than 1/|λ_max|, which is tiny.

The solution is **implicit methods**, where the update equation involves f evaluated at the new time level yₙ₊₁, not just old values. This requires solving a (possibly nonlinear) system at each step, but the payoff is **A-stability**: the method is stable for *all* h when Re(λ) < 0, regardless of how large |λ| is. The workhorse is the **backward Euler method** yₙ₊₁ = yₙ + h·f(tₙ₊₁, yₙ₊₁) and its higher-order relatives like the **trapezoidal rule** and **BDF (backward differentiation formula)** methods. MATLAB's `ode15s` and similar solvers detect stiffness automatically and switch to an implicit integrator, choosing step sizes based solely on accuracy — because stability is no longer the binding constraint. Recognizing stiffness transforms an apparently intractable problem into a straightforward one, once you choose the right method.
