---
id: euler-method-error-analysis
title: Euler's Method for ODEs (Error Analysis)
domain: mathematics
course: numerical-analysis
prerequisites:
- id: eulers-method
  type: hard
- id: taylor-series
  type: hard
builds-toward:
- runge-kutta-methods-for-odes
tags:
- euler-method
- ode-solving
- truncation-error
stage: advanced
status: draft
---

# Euler's Method for ODEs (Error Analysis)

## Core Idea
Euler's method y_{n+1} = y_n + h*f(x_n, y_n) has local truncation error O(h²) and global error O(h) by Taylor expansion analysis. The local error at each step accumulates over the integration interval, and the total accumulated error grows linearly with integration length. Understanding this trade-off guides appropriate step size selection.

## Explainer

You know Euler's method from practice: starting at y(x₀) = y₀, you step forward by yₙ₊₁ = yₙ + h·f(xₙ, yₙ), where h is the step size. The method produces numbers that approximate the true solution, but it makes errors at every step and those errors accumulate. To understand how reliable the method is, you need to quantify two distinct quantities: **local truncation error** (the mistake at a single step) and **global error** (the total accumulated mistake at the end of the integration interval).

The local truncation error comes directly from Taylor series. The true solution satisfies y(xₙ₊₁) = y(xₙ) + h·y'(xₙ) + (h²/2)·y''(xₙ) + O(h³). Euler's method keeps only the first two terms: yₙ₊₁ = yₙ + h·f(xₙ, yₙ) = yₙ + h·y'(xₙ). The discrepancy at one step is therefore (h²/2)·y''(xₙ) + O(h³), which is O(h²). This is the local truncation error. The "2" in the exponent gives Euler's method its classification as a **first-order method** — the global error is O(h¹), one power lower than the local error.

Why does the global error drop one order? Consider integrating from x = 0 to x = T with step size h. There are N = T/h steps, each contributing a local error of O(h²). If these errors simply added, the total would be N × O(h²) = (T/h) × O(h²) = O(h). Errors also propagate — an error introduced at step k perturbs the trajectory for all subsequent steps — but careful stability analysis shows that this propagation does not cause exponential blowup for ODEs satisfying a Lipschitz condition. The net effect is still O(h) global error. This means halving the step size halves the final error: the method is **first-order accurate globally**.

The practical consequence is significant. To achieve global error ε, you need h ~ ε, requiring N ~ T/ε steps. For high accuracy (ε = 10⁻⁶), you need a million steps. This cost motivates higher-order methods: the classical Runge-Kutta method of order 4 achieves O(h⁴) global error, requiring only N ~ T/ε^(1/4) steps for the same accuracy — a factor of ε^(3/4) fewer steps. Error analysis is not just bookkeeping; it tells you precisely when Euler's method is adequate and when the step-size cost makes it impractical.
