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
stage: formal-systems
status: draft
---

# Stiff Differential Equations

## Core Idea
A system dy/dt = f(t,y) is stiff if it contains vastly different time scales—some components decay rapidly while others change slowly. The stiffness ratio is proportional to the ratio of largest to smallest eigenvalue magnitudes of the Jacobian. Explicit methods must use tiny steps for stability, making implicit methods (which are A-stable) necessary for practical stiff ODE solving.

## Questions

```yaml
- question: "You are solving a stiff ODE system with an explicit Adams-Bashforth method. The solution you care about changes smoothly over hours, yet the solver requires microsecond time steps. What is the primary cause?"
  type: multiple-choice
  options:
    - "The solution is not smooth enough for an Adams-Bashforth method to handle accurately"
    - "Rapidly-decaying components impose a stability constraint that forces tiny steps, even though those components carry no useful information at this stage"
    - "Adams-Bashforth is not accurate enough; switching to a higher-order explicit method will fix the step-size problem"
    - "The step size is too small — you should increase it to improve speed without consequence"
  answer: 1
  explanation: "This is the defining symptom of stiffness: the accuracy requirement (steps of minutes or hours) is completely decoupled from the stability requirement (steps of microseconds). The fast-decaying transients have eigenvalues with large magnitude, and explicit methods must satisfy h|λ_max| ≤ C (a constant determined by the stability region) to avoid blow-up — even after those transients have essentially vanished. A higher-order explicit method does not solve this, because the stability region problem persists regardless of order."

- question: "What property of implicit methods makes them the preferred choice for stiff ODEs?"
  type: multiple-choice
  options:
    - "They are more accurate than explicit methods for smooth solutions"
    - "They evaluate f at previous time steps, which smooths out rapid oscillations"
    - "They are A-stable — stable for all h when Re(λ) < 0 — so step size can be chosen based on accuracy alone, not stability"
    - "They automatically detect stiffness and switch to an explicit scheme when the solution becomes smooth"
  answer: 2
  explanation: "A-stability means the method's stability region contains the entire left half of the complex plane. For any eigenvalue with Re(λ) < 0 (a decaying mode), the method is stable regardless of step size. This decouples stability from accuracy: you can take large steps to follow the slow dynamics you care about, without worrying that the fast-decaying modes will cause numerical blow-up. The implicit cost is that each step requires solving a (possibly nonlinear) system, but this is worthwhile compared to taking millions of tiny explicit steps."

- question: "In a stiff ODE system, the step size required for stability is typically much smaller than the step size required for accuracy."
  type: true-false
  answer: true
  explanation: "This is the precise definition of stiffness: stability and accuracy constraints are badly mismatched. The fast eigenvalues (large |λ|) force explicit methods to take steps proportional to 1/|λ_max| for stability, even when the smooth dynamics you want to capture would allow steps orders of magnitude larger. This mismatch is what makes stiff problems computationally expensive for explicit methods."

- question: "A stiff ODE system is one where the solution itself changes very rapidly everywhere, requiring small time steps for accuracy."
  type: true-false
  answer: false
  explanation: "Stiffness is not about the solution being rapidly varying — it is about the *stability constraint* being far more stringent than the *accuracy constraint*. A stiff system often has a slowly-varying solution you care about (which needs large steps for efficiency) alongside rapidly-decaying transients that force tiny steps for stability in explicit methods. After the transients have died out, accuracy alone would allow large steps, but stability still does not — that is the hallmark of stiffness."

- question: "Explain why explicit methods struggle with stiff ODEs and what property of implicit methods resolves this problem."
  type: short-answer
  answer: "Explicit methods have finite stability regions: to remain stable, the step h must satisfy h|λ| ≤ C for every eigenvalue λ. Large eigenvalues (fast modes) force h to be tiny, even when those modes no longer meaningfully affect the solution. Implicit methods evaluate f at the new time level, and the resulting algebra makes the stability region cover the entire left half-plane (A-stability). This means any decaying mode is stable for any h, so step size can be chosen purely for accuracy."
  explanation: "The resolution is not magic — implicit methods require solving a nonlinear system per step, which is expensive. But for stiff problems, this cost is far less than the cost of taking millions of tiny explicit steps. The solver can now stride across the slow dynamics efficiently, with step sizes dictated by accuracy alone."
```

## Explainer

From Adams methods and other multistep schemes, you learned that step size h is constrained both by accuracy (you want h small enough to capture the solution's features) and by **stability** (taking h too large causes the numerical solution to blow up spuriously). For most ODEs, these two constraints are compatible: the step size required for accuracy is similar to the step size required for stability. Stiff equations break this compatibility in a dramatic way.

Imagine a chemical reaction network where some species decay with a half-life of microseconds while others persist for hours. The solution you *care about* changes on the scale of hours, so accuracy only requires time steps of, say, minutes. But the rapidly-decaying transients impose a stability requirement: explicit methods like Adams-Bashforth must take steps tiny enough to track those microsecond decays — even after those species have essentially vanished and no longer affect the solution. The fast components force tiny steps even though they carry no useful information. This is stiffness: **the stability requirement is far more stringent than the accuracy requirement**.

Mathematically, stiffness is measured through the **Jacobian** ∂f/∂y of the right-hand side. The eigenvalues λᵢ of this Jacobian determine the characteristic time scales of the system — each eigenvalue contributes a mode that evolves like e^(λᵢt). The **stiffness ratio** is roughly max|Re(λᵢ)|/min|Re(λᵢ)|; ratios of 10⁶ or larger are not uncommon in practical problems (circuit simulation, chemical kinetics, mechanical systems with contact). For an explicit method with stability region |1 + hλ| ≤ 1, the large eigenvalues force h|λ_max| to stay within the stability region — meaning h must be smaller than 1/|λ_max|, which is tiny.

The solution is **implicit methods**, where the update equation involves f evaluated at the new time level yₙ₊₁, not just old values. This requires solving a (possibly nonlinear) system at each step, but the payoff is **A-stability**: the method is stable for *all* h when Re(λ) < 0, regardless of how large |λ| is. The workhorse is the **backward Euler method** yₙ₊₁ = yₙ + h·f(tₙ₊₁, yₙ₊₁) and its higher-order relatives like the **trapezoidal rule** and **BDF (backward differentiation formula)** methods. MATLAB's `ode15s` and similar solvers detect stiffness automatically and switch to an implicit integrator, choosing step sizes based solely on accuracy — because stability is no longer the binding constraint. Recognizing stiffness transforms an apparently intractable problem into a straightforward one, once you choose the right method.
