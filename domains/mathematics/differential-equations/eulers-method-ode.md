---
id: eulers-method-ode
title: Euler's Method for Numerical Solution of ODEs
domain: mathematics
course: differential-equations
prerequisites:
- id: derivative-as-slope-of-tangent
  type: hard
- id: first-order-linear-odes
  type: soft
tags:
- numerical-methods
- approximation
- computation
stage: formal-systems
status: draft
---

# Euler's Method for Numerical Solution of ODEs

## Core Idea
Euler's method is a first-order numerical technique for solving dy/dx = f(x,y) with initial condition y(x₀) = y₀. At each step, advance by h using y_{n+1} = y_n + h·f(x_n, y_n). While simple and intuitive, Euler's method has limited accuracy but serves as the foundation for understanding numerical ODE solving and error propagation.

## Questions

```yaml
- question: "You apply Euler's method to dy/dx = y with y(0) = 1 using step size h = 0.1. After one step you get y₁ = 1.1, but the true value is e^0.1 ≈ 1.10517. Why does this error arise?"
  type: multiple-choice
  options:
    - "The formula y_{n+1} = y_n + h·f(x_n, y_n) is applied incorrectly"
    - "The method follows the tangent line at (0,1) instead of the actual exponential curve, which immediately curves away from that tangent"
    - "The step size h = 0.1 is too small for this method to work accurately"
    - "Euler's method only works correctly for linear differential equations"
  answer: 1
  explanation: "Euler's method is a tangent-line approximation: it advances by following the slope at the current point, which equals the slope of the tangent line, not the actual curve. Since the exponential solution curves upward away from any tangent, each step lands slightly below the true value. The method is not applied incorrectly — this error is inherent to the first-order approximation."

- question: "A researcher halves the step size in Euler's method from h = 0.01 to h = 0.005 over the same fixed interval. What happens to the total global error?"
  type: multiple-choice
  options:
    - "It roughly halves, because Euler's method has first-order global accuracy"
    - "It roughly quarters, because halving h reduces error quadratically"
    - "It stays the same — global error is independent of step size"
    - "It decreases exponentially with each halving"
  answer: 0
  explanation: "Euler's method is a 'first-order' method: the global (accumulated) error over a fixed interval is proportional to h. Halving h halves the global error. This is in contrast to the local truncation error (error in a single step), which is proportional to h². Second-order methods like Runge-Kutta 2 have global error proportional to h², so halving h quarters the error — a much better deal."

- question: "The local truncation error in a single Euler step is proportional to h², but the global error accumulated over a fixed interval is proportional to h."
  type: true-false
  answer: true
  explanation: "This is the defining property of a first-order method. Each step introduces an error of O(h²). But to traverse a fixed interval of length L, you need N = L/h steps, so the accumulated global error is roughly N · O(h²) = (L/h) · O(h²) = O(h). The extra factor of 1/h from doubling the number of steps cancels one power of h from the local error."

- question: "Euler's method is called 'first-order' because it can only be used to solve first-order differential equations (dy/dx = f(x, y)), not second-order or higher equations."
  type: true-false
  answer: false
  explanation: "'First-order' refers to the convergence rate: the global error is O(h), meaning the method converges linearly as step size shrinks. It has nothing to do with the order of the ODE being solved. Higher-order ODEs can be converted to systems of first-order equations and then solved with Euler's method, though still with the same first-order accuracy."

- question: "Explain in your own words why Euler's method introduces error at each step and how that error accumulates over many steps."
  type: short-answer
  answer: "At each step, Euler's method follows the tangent line to the solution curve rather than the curve itself. Since the actual solution curves away from the tangent, you arrive at a slightly wrong position after each step. Each subsequent step starts from that wrong position and computes slope there — not along the true solution — so errors compound over N steps. Over a fixed interval of length L = Nh, the total global error grows as O(h): proportional to step size."
  explanation: "This compounding behavior is what makes error analysis non-trivial. Even if each individual step introduces a tiny error O(h²), taking O(1/h) steps means those errors accumulate to O(h) total. Higher-order methods (Runge-Kutta) use multiple slope evaluations per step to better estimate the average slope over the interval, reducing the leading error term and achieving faster convergence."
```

## Explainer

Euler's method translates the geometric meaning of a derivative into a computational recipe. You know that dy/dx = f(x, y) at a point (x, y) gives the slope of the solution curve passing through that point. If you start at a known point (x₀, y₀) and know the slope there, you can step a small distance h forward in x and estimate where the curve goes: y₁ ≈ y₀ + h · f(x₀, y₀). This is just the **linear approximation** — instead of following the actual curve, you follow the tangent line. Repeat from (x₁, y₁) using the new slope, and you trace out an approximate solution one step at a time.

The formula y_{n+1} = y_n + h · f(x_n, y_n) is the **Euler step**. At each iteration, the current position determines the slope, and you advance by that slope times the step size. The approximation accumulates error because the actual solution curves away from the tangent line — after one step you are slightly off, and each subsequent step starts from a slightly wrong position. The **local truncation error** (error in a single step) is proportional to h², while the **global error** (accumulated over an entire interval of length L) is proportional to h. This is why Euler's method is called a "first-order" method: halving h halves the total error.

A concrete example makes the accuracy visible. Consider dy/dx = y with y(0) = 1, whose exact solution is eˣ. Using h = 0.1: y₁ = 1 + 0.1(1) = 1.1, y₂ = 1.1 + 0.1(1.1) = 1.21, and in general y_n = (1.1)ⁿ. After 10 steps (at x = 1), Euler gives (1.1)¹⁰ ≈ 2.594, while e¹ ≈ 2.718 — about a 4.5% error. Halving to h = 0.05 and taking 20 steps gives roughly half the error, confirming the first-order behavior. Notice that (1.1)ⁿ is the compound interest formula — Euler's method on exponential growth is discrete compounding.

Euler's method matters not because it is the most accurate numerical approach — for practical work it is usually too slow to converge — but because it makes the structure of numerical ODE solving fully transparent. Higher-order methods like **Runge-Kutta** use multiple slope evaluations per step to estimate the average slope over the interval more accurately, reducing the leading error term. Understanding Euler's method gives you the conceptual framework for understanding why those improvements work and how to reason about error in any numerical scheme.
