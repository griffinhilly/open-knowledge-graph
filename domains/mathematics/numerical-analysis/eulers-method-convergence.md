---
id: eulers-method-convergence
title: 'Euler''s Method: Error Analysis'
domain: mathematics
course: numerical-analysis
prerequisites:
- id: eulers-method
  type: hard
- id: taylor-series
  type: hard
builds-toward:
- runge-kutta-methods
tags:
- euler-method
- ode
- error-analysis
stage: abstract-reasoning
status: draft
---

# Euler's Method: Error Analysis

## Core Idea
Euler's method y_{n+1} = y_n + hf(t_n, y_n) has local truncation error O(h²) at each step and global error O(h) over a fixed time interval. The method converges as h → 0 under standard Lipschitz conditions, but slowly—halving h halves the error. Understanding error behavior guides practical choices of step size and informs when faster methods are needed.

## Explainer

Euler's method steps forward in time by replacing the exact solution curve with a straight-line tangent approximation: at each point (t_n, y_n), it travels along the tangent for a distance h. Your prerequisite, Taylor series, lets you quantify precisely how much is lost in each such step. Expand the exact solution y(t_{n+1}) around t_n: y(t_{n+1}) = y(t_n) + h·y'(t_n) + (h²/2)·y''(t_n) + ···. Since y'(t_n) = f(t_n, y(t_n)), the Euler update y_{n+1} = y_n + h·f keeps the first two terms and discards everything from h² onward. The **local truncation error** — the error made in one step, assuming the previous value is exact — is therefore proportional to h², typically written O(h²).

But errors accumulate over time. Over a fixed interval [0, T], the number of steps is T/h. Each step introduces an O(h²) error, and these errors can compound: each new step is taken from a slightly wrong position, creating an error in the next step. A careful analysis shows the errors do not simply add — the **global error** at the endpoint is O(h), not O(h²). Intuitively: the sum of (T/h) terms each of size O(h²) is O(h), and this first-order accumulation dominates. Halving h halves the global error — a first-order method. By contrast, a fourth-order method like Runge-Kutta has global error O(h^4), so halving h gives a 16× improvement. Euler's method is the baseline that all better methods are measured against.

The convergence proof — that global error → 0 as h → 0 — requires one technical condition: the **Lipschitz condition** on f. This says |f(t, y₁) - f(t, y₂)| ≤ L|y₁ - y₂| for all t and all y₁, y₂, where L is a fixed constant. The Lipschitz condition bounds how fast nearby solution curves can diverge. When L is large (a stiff problem), errors amplify rapidly and small h is required to achieve any accuracy. When L is small, errors stay controlled and moderate h suffices. Understanding this gives you a practical tool: if a problem requires very small h to stabilize, suspect stiffness and consider an implicit method rather than brute-forcing Euler with tiny steps.
