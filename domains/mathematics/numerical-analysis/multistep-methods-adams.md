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
status: draft
---

# Multistep Methods: Adams-Bashforth and Adams-Moulton

## Core Idea
Multistep methods use information from several previous steps to compute y_{n+1}. Adams-Bashforth (explicit) uses past y and f values; Adams-Moulton (implicit) includes f(t_{n+1}, y_{n+1}). Multistep methods are efficient when solution history is available but require startup (using a single-step method for the first few steps) and careful error monitoring.

## Explainer

The Runge-Kutta methods you already know are **single-step** methods: each step from tₙ to tₙ₊₁ uses only information at tₙ (and possibly intermediate stages within that interval). They are self-starting and robust, but they throw away all the history they accumulate. Once you have computed y₁, y₂, ..., yₙ, why not use those past values to make a smarter prediction for yₙ₊₁? That is the motivating idea behind multistep methods.

The Adams family derives its formulas by fitting a polynomial through several past values of f(t, y) — the derivative function — and integrating that polynomial over [tₙ, tₙ₊₁]. **Adams-Bashforth** methods use only past function evaluations (explicit): the 2-step formula is yₙ₊₁ = yₙ + h(3f(tₙ,yₙ) − f(tₙ₋₁,yₙ₋₁))/2. No root-finding is required. **Adams-Moulton** methods include f at the new point tₙ₊₁ as well (implicit), which improves accuracy: the 2-step formula is yₙ₊₁ = yₙ + h(5f(tₙ₊₁,yₙ₊₁) + 8f(tₙ,yₙ) − f(tₙ₋₁,yₙ₋₁))/12. The tradeoff is that an implicit equation must be solved at each step, typically using a corrector iteration.

The standard approach combines them in a **predictor-corrector** pair: use Adams-Bashforth to predict yₙ₊₁, evaluate f there, then plug that into Adams-Moulton to correct. This gives the accuracy of an implicit method while using only explicit function evaluations — one or two evaluations per step. Compare this to a classical 4th-order Runge-Kutta, which requires four evaluations per step. Once the multistep method is running, it is typically more efficient per unit accuracy.

The catch is **startup**: a k-step Adams method needs k prior solution values before it can begin. At t = t₀ you only have y₀, so you must use a single-step method (usually RK4) to generate y₁, ..., yₖ₋₁ first. Changing step size is also more involved — unlike single-step methods, you cannot freely vary h without affecting all the past function values in the formula. These bookkeeping requirements mean Adams methods shine for long smooth integrations at a fixed step size, where the per-step efficiency gain accumulates, and are less suited to problems requiring frequent step-size adaptation or restarts.
