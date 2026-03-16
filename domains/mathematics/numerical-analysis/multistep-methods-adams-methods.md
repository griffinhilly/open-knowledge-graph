---
id: multistep-methods-adams-methods
title: Multistep Methods (Adams-Bashforth/Moulton)
domain: mathematics
course: numerical-analysis
prerequisites:
- id: runge-kutta-methods-for-odes
  type: hard
builds-toward:
- stiff-differential-equations
tags:
- multistep-methods
- adams-bashforth
- adams-moulton
stage: advanced
status: draft
---

# Multistep Methods (Adams-Bashforth/Moulton)

## Core Idea
Multistep methods use information from previous steps to advance the solution by integrating a polynomial interpolant of f through recent points. Adams-Bashforth methods are explicit; Adams-Moulton methods are implicit. These methods are efficient when f evaluation is expensive, using function values already computed from previous steps.

## Explainer

From Runge-Kutta methods, you learned to advance an ODE solution y' = f(t, y) by evaluating f at several carefully chosen intermediate points within a single step, combining them to achieve high-order accuracy. Each RK step is self-contained: it uses only the current point and discards everything computed internally once the step is done. Multistep methods take a different philosophy — they **remember previous steps** and use those stored values instead of computing new intermediate evaluations. If you have already computed f at t_{n-1}, t_{n-2}, and t_{n-3}, why not reuse that information for the current step?

The idea is to fit a polynomial through the recent function values f(t_{n-1}, y_{n-1}), f(t_{n-2}, y_{n-2}), ... and then integrate that polynomial over [t_{n-1}, t_n] to advance the solution. The interpolating polynomial is constructed using **Newton's backward difference formula**, and its integral gives the update formula explicitly. For the **Adams-Bashforth** k-step method, all the data used lies strictly before the current step endpoint — the method is explicit and requires no iteration. The 4-step Adams-Bashforth method achieves 4th-order accuracy using only one new f evaluation per step, compared to four evaluations per step for 4th-order Runge-Kutta.

**Adams-Moulton** methods are the implicit counterpart: they include the unknown value f(t_n, y_n) in the interpolating polynomial, yielding a higher-order method at the same step count but requiring a nonlinear solve at each step. In practice, this solve is avoided by using an Adams-Bashforth step as a **predictor** and an Adams-Moulton step as a **corrector** — the predictor-corrector approach. The corrector uses the predicted y_n to evaluate f(t_n, y_n), then inserts that value into the Adams-Moulton formula to get a corrected (more accurate) y_n, all without iteration.

The startup cost is a fundamental limitation of multistep methods: to take a k-step method's first step, you need k prior values, but you only have the initial condition y₀. The standard remedy is to use a one-step method (like Runge-Kutta) for the first k−1 steps to generate the required history, then switch to the multistep method. This makes implementation more complex than pure RK methods. The payoff is efficiency: for problems where f is expensive to evaluate and the solution is smooth enough to warrant high-order methods, Adams methods reduce the number of f evaluations substantially compared to equivalent-order Runge-Kutta schemes.
