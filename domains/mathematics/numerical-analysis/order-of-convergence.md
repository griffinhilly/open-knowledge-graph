---
id: order-of-convergence
title: Order of Convergence
domain: mathematics
course: numerical-analysis
prerequisites:
- id: bisection-method
  type: hard
- id: newton-method-convergence
  type: hard
tags:
- convergence
- error-reduction
- rates
stage: formal-systems
status: draft
---

# Order of Convergence

## Core Idea
The order of convergence describes how fast iteration errors decrease. Linear convergence (order 1) reduces error by a constant factor each step; quadratic (order 2) roughly squares the error each step. Higher orders reach tolerance in fewer iterations, but convergence order only holds asymptotically near the solution—far away, even superlinear methods may behave slowly.

## How It's Best Learned
Compare error reduction for bisection, Newton, and secant methods on the same problem, plotting error vs. iteration on a log scale to see the different slopes.

## Common Misconceptions
- Confusing order of convergence with speed; a method with lower order but fewer function evaluations per step may be faster overall.
- Assuming quadratic convergence from the first iteration; convergence order applies only in the final iterations when close to the solution.

## Explainer

From studying bisection and Newton's method, you have seen that iterative methods get closer to a solution step by step — but they don't all close the gap at the same rate. The **order of convergence** gives a precise language for this. Let e_n = |x_n − x*| be the error at step n. A method has **order p** if |e_{n+1}| / |e_n|^p → C for some constant C > 0 called the **asymptotic error constant**. The exponent p is what determines how dramatically the error shrinks with each step.

**Linear convergence** (order 1, C < 1) means each step reduces error by the same fraction: e_{n+1} ≈ C · e_n. Bisection is the prototype — each step halves the interval, so C = 0.5. Starting with e_0 = 1, after 10 steps you have e_{10} ≈ 10^{−3}. You gain roughly log₁₀(1/C) correct decimal digits per step, which is constant. On a log-scale error plot, linear convergence appears as a straight line with slope equal to the convergence factor.

**Quadratic convergence** (order 2) is qualitatively different. If e_n ≈ 10^{−4}, then e_{n+1} ≈ C · (10^{−4})² = C · 10^{−8}: the number of correct decimal digits roughly doubles with every step. Newton's method achieves this near a simple root where f′(x*) ≠ 0 — the reason it is the default choice for smooth root-finding. The secant method achieves superlinear order ≈ 1.618 (the golden ratio), faster than linear but slower than quadratic. A few iterations of quadratic convergence accomplish what thousands of iterations of linear convergence would require once you're close enough to the solution.

Two important caveats flow directly from your prerequisite methods. First, convergence order is an **asymptotic** statement — it describes behavior only when x_n is already close to x*. Far from the solution, even Newton's method can diverge or cycle. Second, order is not the same as efficiency. Newton's method requires both f and f′ per step; if evaluating f′ is expensive, a lower-order method requiring only f evaluations may deliver more accuracy per unit of computational cost. The right metric is accuracy per function evaluation, not accuracy per iteration — a distinction that matters greatly in expensive simulations or optimization problems.
