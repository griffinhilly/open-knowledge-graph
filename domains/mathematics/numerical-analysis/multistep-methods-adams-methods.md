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
stage: formal-systems
status: validated
---

# Multistep Methods (Adams-Bashforth/Moulton)

## Core Idea
Multistep methods use information from previous steps to advance the solution by integrating a polynomial interpolant of f through recent points. Adams-Bashforth methods are explicit; Adams-Moulton methods are implicit. These methods are efficient when f evaluation is expensive, using function values already computed from previous steps.

## Questions

```yaml
- question: "A 4th-order Runge-Kutta method requires 4 evaluations of f per step. A 4-step Adams-Bashforth method achieves the same order with only 1 new evaluation per step. What accounts for this difference?"
  type: multiple-choice
  options:
    - "Adams-Bashforth uses a lower-order polynomial interpolant, so it does less computational work per step"
    - "Adams-Bashforth reuses function values already computed at the previous four steps instead of computing new intermediate evaluations"
    - "Adams-Bashforth is an implicit method, so it solves a linear system rather than evaluating f"
    - "Adams-Bashforth takes larger step sizes, so fewer steps are required overall"
  answer: 1
  explanation: "The key insight of multistep methods is memory reuse: because function values f(t_{n-1}, y_{n-1}), f(t_{n-2}, y_{n-2}), etc. were already computed in previous steps, they can be used to build a polynomial interpolant for the current step without any new evaluations. Runge-Kutta methods discard all intermediate evaluations once a step is done; Adams-Bashforth methods exploit the fact that prior f values are still available. This is efficient when f is expensive — the cost of evaluating f is paid once and reused across multiple steps."

- question: "You want to apply a 4-step Adams-Bashforth method to an ODE starting from a single initial condition y₀. What must you do before the multistep method can take its first step?"
  type: multiple-choice
  options:
    - "Run the Adams-Moulton corrector to generate the required starting values"
    - "Use a one-step method (such as Runge-Kutta) to generate y₁, y₂, and y₃"
    - "Reduce the method to a 1-step Adams-Bashforth and gradually increase the number of steps"
    - "Nothing — a 4-step method can start from any single initial value by setting missing prior values to zero"
  answer: 1
  explanation: "A k-step Adams-Bashforth method requires k previous function values to interpolate through. At the very start, only y₀ is known — the history needed for k steps doesn't exist yet. The standard solution is to use a self-starting one-step method like Runge-Kutta to compute y₁ through y_{k-1} at the cost of full RK evaluations per step, then switch to the multistep method once sufficient history exists. This startup cost is a fundamental limitation that makes multistep methods more complex to implement than pure RK methods."

- question: "Adams-Moulton methods are more accurate per step than Adams-Bashforth methods with the same number of previous steps."
  type: true-false
  answer: true
  explanation: "This is true. Adams-Moulton methods include the unknown endpoint value f(t_n, y_n) in the interpolating polynomial, which gives them one higher order of accuracy than the corresponding Adams-Bashforth method using the same number of prior points. A k-step Adams-Moulton method achieves order k+1, while a k-step Adams-Bashforth achieves order k. The tradeoff is that Adams-Moulton methods are implicit — they require y_n on the right-hand side of their own update formula, necessitating a nonlinear solve or a predictor-corrector approach. The higher accuracy is why Adams-Moulton is used as the corrector in predictor-corrector schemes."

- question: "Multistep methods are always preferable to Runge-Kutta methods because they require fewer function evaluations per step."
  type: true-false
  answer: false
  explanation: "This is false. Multistep methods have real advantages when f is expensive and the solution is smooth, but they carry significant disadvantages: they require a startup phase using a one-step method, they are harder to implement, and they can struggle with stiff differential equations where implicit methods are essential. Runge-Kutta methods are self-starting, easier to implement, and naturally adaptive with step-size control. The right choice depends on the problem — if f is cheap or the solution has discontinuities or rapid transients, RK methods may be preferable. 'Fewer evaluations per step' is only an advantage if each step is valid, which requires smooth solutions and a fixed step size."

- question: "Why must multistep methods be bootstrapped with a one-step method, and what fundamental property of multistep methods creates this requirement?"
  type: short-answer
  answer: "Multistep methods generate the current step's solution by interpolating a polynomial through recent function values from the last k steps and integrating it. At the very start of the problem, only the initial condition y₀ is known — the prior step values needed for k > 1 don't exist. Since multistep methods cannot start themselves, a self-starting one-step method (typically Runge-Kutta) must generate the first k−1 solution values before the multistep method can engage. This startup cost is inherent to the multistep design philosophy: the efficiency gain (one f evaluation per step instead of k) only materializes after the history is built."
  explanation: "The startup problem arises directly from the memory-reuse philosophy. The very feature that makes multistep methods efficient — using old f values — requires that old f values exist. Runge-Kutta methods have no such dependency; each step is self-contained. This makes the implementation of multistep methods more involved: you effectively run two different algorithms on the same problem, switching from RK to Adams after sufficient history accumulates. The practical consequence is that adaptive step-size control is also harder — changing the step size invalidates the stored history, requiring either re-interpolation or a fresh startup."
```

## Explainer

From Runge-Kutta methods, you learned to advance an ODE solution y' = f(t, y) by evaluating f at several carefully chosen intermediate points within a single step, combining them to achieve high-order accuracy. Each RK step is self-contained: it uses only the current point and discards everything computed internally once the step is done. Multistep methods take a different philosophy — they **remember previous steps** and use those stored values instead of computing new intermediate evaluations. If you have already computed f at t_{n-1}, t_{n-2}, and t_{n-3}, why not reuse that information for the current step?

The idea is to fit a polynomial through the recent function values f(t_{n-1}, y_{n-1}), f(t_{n-2}, y_{n-2}), ... and then integrate that polynomial over [t_{n-1}, t_n] to advance the solution. The interpolating polynomial is constructed using **Newton's backward difference formula**, and its integral gives the update formula explicitly. For the **Adams-Bashforth** k-step method, all the data used lies strictly before the current step endpoint — the method is explicit and requires no iteration. The 4-step Adams-Bashforth method achieves 4th-order accuracy using only one new f evaluation per step, compared to four evaluations per step for 4th-order Runge-Kutta.

**Adams-Moulton** methods are the implicit counterpart: they include the unknown value f(t_n, y_n) in the interpolating polynomial, yielding a higher-order method at the same step count but requiring a nonlinear solve at each step. In practice, this solve is avoided by using an Adams-Bashforth step as a **predictor** and an Adams-Moulton step as a **corrector** — the predictor-corrector approach. The corrector uses the predicted y_n to evaluate f(t_n, y_n), then inserts that value into the Adams-Moulton formula to get a corrected (more accurate) y_n, all without iteration.

The startup cost is a fundamental limitation of multistep methods: to take a k-step method's first step, you need k prior values, but you only have the initial condition y₀. The standard remedy is to use a one-step method (like Runge-Kutta) for the first k−1 steps to generate the required history, then switch to the multistep method. This makes implementation more complex than pure RK methods. The payoff is efficiency: for problems where f is expensive to evaluate and the solution is smooth enough to warrant high-order methods, Adams methods reduce the number of f evaluations substantially compared to equivalent-order Runge-Kutta schemes.
