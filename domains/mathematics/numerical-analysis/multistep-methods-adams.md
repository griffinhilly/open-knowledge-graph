---
id: multistep-methods-adams
title: 'Multistep Methods: Adams-Bashforth and Adams-Moulton'
domain: mathematics
course: numerical-analysis
prerequisites:
- id: runge-kutta-methods
  type: hard
builds-toward:
- stiff-equations
tags:
- multistep
- adams
- ode
stage: formal-systems
status: validated
---

# Multistep Methods: Adams-Bashforth and Adams-Moulton

## Core Idea
Multistep methods use information from several previous steps to compute y_{n+1}. Adams-Bashforth (explicit) uses past y and f values; Adams-Moulton (implicit) includes f(t_{n+1}, y_{n+1}). Multistep methods are efficient when solution history is available but require startup (using a single-step method for the first few steps) and careful error monitoring.

## Questions

```yaml
- question: "Why do Adams multistep methods require a 'startup procedure' using a single-step method like RK4?"
  type: multiple-choice
  options:
    - "Adams-Bashforth is implicit and needs initial guesses at every step before it can begin"
    - "A k-step Adams method needs k prior solution values, but at t₀ only y₀ is available — a single-step method generates y₁, ..., yₖ₋₁ first"
    - "Single-step methods are more stable and must validate the initial data before multistep methods can proceed"
    - "The Adams formula is only numerically valid after the transient behavior of the ODE has died out"
  answer: 1
  explanation: "The Adams-Bashforth k-step formula requires the function values f(tₙ,yₙ), f(tₙ₋₁,yₙ₋₁), ..., back k steps. At t₀ you only have y₀, so there is nothing in the history. A single-step method (typically RK4) must be run for the first k−1 steps to populate the history before the Adams formula can be applied. This startup cost is a fixed overhead that pays off on long integrations."

- question: "A student argues that since Adams-Moulton is more accurate than Adams-Bashforth at the same order, you should simply use Adams-Moulton alone. What is the strongest counterargument?"
  type: multiple-choice
  options:
    - "Adams-Moulton is less numerically stable than Adams-Bashforth for most ODEs"
    - "Adams-Moulton is implicit — it requires solving for yₙ₊₁ at each step; using Adams-Bashforth to predict yₙ₊₁ first (predictor-corrector) achieves nearly the same accuracy with only explicit function evaluations"
    - "Adams-Bashforth is always more accurate for smooth solutions"
    - "Adams-Moulton cannot be applied to initial value problems, only to boundary value problems"
  answer: 1
  explanation: "Adams-Moulton includes f(tₙ₊₁, yₙ₊₁) in its formula, making it implicit — yₙ₊₁ appears on both sides. Solving this at each step requires a root-finding iteration (expensive). The predictor-corrector strategy uses Adams-Bashforth to predict yₙ₊₁, evaluates f there, and plugs that value into the Adams-Moulton corrector formula — giving implicit-level accuracy while requiring only one or two explicit function evaluations per step."

- question: "A multistep Adams method is more efficient than RK4 for long smooth integrations because it reuses previously computed derivative values rather than computing new intermediate stages."
  type: true-false
  answer: true
  explanation: "Classical RK4 requires 4 new function evaluations per step, every step, without reusing any prior information. Adams methods in predictor-corrector mode typically need 1-2 evaluations per step by reusing function values already stored from prior steps. For long integrations where the per-step savings multiply over thousands of steps, this efficiency advantage is substantial."

- question: "Adams multistep methods are well-suited for problems that require frequent, large changes in step size during integration."
  type: true-false
  answer: false
  explanation: "Changing step size in a multistep method is problematic: all stored past function values were computed at the old step size and cannot simply be reused at a new step size without reformulation. Step-size adaptation typically requires restarting the multistep formula, negating the efficiency gained. Single-step methods like RK4 handle variable step sizes naturally. Adams methods shine on long, smooth integrations at a fixed or slowly varying step size."

- question: "What is the fundamental tradeoff that motivates Adams multistep methods over single-step Runge-Kutta methods, and when does that tradeoff favor multistep methods?"
  type: short-answer
  answer: "Single-step methods compute new intermediate stages at every step and discard all accumulated history, requiring 4+ function evaluations per step. Multistep methods amortize this cost by storing past values of f(t, y) and reusing them in the next-step formula, reducing per-step evaluations to 1-2. The cost: startup (a single-step method must generate the first k values) and difficulty with variable step sizes. The tradeoff favors multistep methods for long, smooth integrations at a fixed step size — where the per-step savings compound — and disfavors them for stiff or highly variable problems requiring frequent adaptation."
  explanation: "This efficiency gain is the entire reason to use multistep methods. Once the startup phase is complete and the solution is smooth, a predictor-corrector Adams pair achieves the same accuracy per step as RK4 at roughly half the function evaluation cost. On an integration spanning 100,000 steps, that difference matters enormously."
```

## Explainer

The Runge-Kutta methods you already know are **single-step** methods: each step from tₙ to tₙ₊₁ uses only information at tₙ (and possibly intermediate stages within that interval). They are self-starting and robust, but they throw away all the history they accumulate. Once you have computed y₁, y₂, ..., yₙ, why not use those past values to make a smarter prediction for yₙ₊₁? That is the motivating idea behind multistep methods.

The Adams family derives its formulas by fitting a polynomial through several past values of f(t, y) — the derivative function — and integrating that polynomial over [tₙ, tₙ₊₁]. **Adams-Bashforth** methods use only past function evaluations (explicit): the 2-step formula is yₙ₊₁ = yₙ + h(3f(tₙ,yₙ) − f(tₙ₋₁,yₙ₋₁))/2. No root-finding is required. **Adams-Moulton** methods include f at the new point tₙ₊₁ as well (implicit), which improves accuracy: the 2-step formula is yₙ₊₁ = yₙ + h(5f(tₙ₊₁,yₙ₊₁) + 8f(tₙ,yₙ) − f(tₙ₋₁,yₙ₋₁))/12. The tradeoff is that an implicit equation must be solved at each step, typically using a corrector iteration.

The standard approach combines them in a **predictor-corrector** pair: use Adams-Bashforth to predict yₙ₊₁, evaluate f there, then plug that into Adams-Moulton to correct. This gives the accuracy of an implicit method while using only explicit function evaluations — one or two evaluations per step. Compare this to a classical 4th-order Runge-Kutta, which requires four evaluations per step. Once the multistep method is running, it is typically more efficient per unit accuracy.

The catch is **startup**: a k-step Adams method needs k prior solution values before it can begin. At t = t₀ you only have y₀, so you must use a single-step method (usually RK4) to generate y₁, ..., yₖ₋₁ first. Changing step size is also more involved — unlike single-step methods, you cannot freely vary h without affecting all the past function values in the formula. These bookkeeping requirements mean Adams methods shine for long smooth integrations at a fixed step size, where the per-step efficiency gain accumulates, and are less suited to problems requiring frequent step-size adaptation or restarts.
