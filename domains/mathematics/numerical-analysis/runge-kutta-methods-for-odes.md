---
id: runge-kutta-methods-for-odes
title: Runge-Kutta Methods for ODEs
domain: mathematics
course: numerical-analysis
prerequisites:
- id: euler-method-error-analysis
  type: hard
- id: order-of-convergence
  type: hard
builds-toward:
- multistep-methods-adams-methods
- stiff-differential-equations
tags:
- runge-kutta
- ode-solver
- higher-order-method
stage: advanced
status: draft
---

# Runge-Kutta Methods for ODEs

## Core Idea
Runge-Kutta methods evaluate f at intermediate stages within each step, using these evaluations to approximate the solution more accurately. The classical 4th-order RK4 uses four stages and achieves O(h⁴) global error. RK methods are explicit, have a finite stability region, and balance accuracy with computational efficiency, making them widely used in practice.

## Explainer

You've studied Euler's method and its error analysis: Euler steps forward using the slope f(x_n, y_n) at the current point, producing O(h) local truncation error per step and O(h) global error overall — a first-order method. The source of that error is using a single, potentially unrepresentative slope over the entire interval [x_n, x_n + h]. The slope at the left endpoint may be a poor predictor of the average slope across the step. Runge-Kutta methods address this directly by sampling f at multiple points within each step and computing a weighted average slope that better captures the true behavior of the solution.

The classical **RK4** uses four slope evaluations: k_1 = hf(x_n, y_n) is the slope at the left endpoint; k_2 = hf(x_n + h/2, y_n + k_1/2) is the slope at the midpoint using an Euler half-step as a predictor; k_3 = hf(x_n + h/2, y_n + k_2/2) is a corrected midpoint slope; and k_4 = hf(x_n + h, y_n + k_3) is the slope at the right endpoint. The update is y_{n+1} = y_n + (k_1 + 2k_2 + 2k_3 + k_4)/6. The midpoint slopes k_2 and k_3 receive double weight because they carry more information about the step's interior behavior. This scheme achieves O(h^4) local error and O(h^4) global error — four orders of accuracy from four function evaluations.

From your study of order of convergence, you know that higher order produces dramatically better accuracy at the same step size. Halving h in a first-order method halves the error; halving h in RK4 reduces the error by a factor of 16. In practice, RK4 can take much larger steps than Euler for equivalent accuracy, resulting in far fewer total evaluations. This makes RK4 the standard workhorse for non-stiff ODEs — it balances accuracy, cost, and simplicity.

The limitation is the **stability region**: explicit methods can go unstable if h is too large relative to the ODE's decay rate. For y' = λy with λ < 0, RK4 requires |λ|h ≤ 2.8 approximately. If λ is very large in magnitude — meaning the ODE has very fast dynamics, called **stiff** equations — stability forces tiny step sizes regardless of accuracy needs. This is why stiff problems require implicit methods like backward Euler or implicit Runge-Kutta variants, where the stability region covers the entire left half-plane. The Runge-Kutta framework is also highly extensible: **Butcher tableaux** provide a systematic notation for designing methods of arbitrary order, and **embedded pairs** like RK45 (Dormand-Prince) run two methods of different orders simultaneously to estimate local error and adapt the step size automatically, making modern ODE solvers both accurate and adaptive.
