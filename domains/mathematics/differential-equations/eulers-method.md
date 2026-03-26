---
id: eulers-method
title: Euler's Method for Numerical Solutions
domain: mathematics
course: differential-equations
prerequisites:
- id: differential-equations-intro
  type: hard
- id: linear-approximation
  type: hard
builds-toward:
- runge-kutta-methods
tags:
- numerical
- approximation
- computational
stage: formal-systems
status: validated
---
# Euler's Method for Numerical Solutions

## Core Idea
Euler's method approximates solutions to initial value problems y' = f(x,y), y(x₀) = y₀ by stepping forward: y_{n+1} ≈ y_n + h·f(x_n, y_n). Though simple and first-order accurate, it provides intuition for numerical ODE solving and forms the basis for more sophisticated methods.

## How It's Best Learned
Implement Euler's method by hand for a few steps on a simple problem (like y' = y), then compare with the exact solution to see accumulated error. Explore how step size h affects accuracy.

## Common Misconceptions
- Thinking Euler's method is exact; it's an approximation with error proportional to h. - Using a step size that's too large, leading to significant local truncation errors. - Confusing Euler's method with exact separation of variables or other analytical methods.

## Questions

```yaml
- question: "For the IVP y' = 2x, y(0) = 1, using Euler's method with step size h = 0.5, what is the approximate value of y(0.5)?"
  type: multiple-choice
  options:
    - "1.0 — Euler's approximation using the slope at x = 0"
    - "1.25 — the exact value of y(0.5) = x² + 1"
    - "1.5 — one full step of slope 1 from y₀ = 1"
    - "2.0 — the slope at x = 0.5 times the step size"
  answer: 0
  explanation: "Euler's method: y₁ = y₀ + h·f(x₀, y₀) = 1 + 0.5·f(0, 1) = 1 + 0.5·(2·0) = 1 + 0 = 1.0. The slope at x = 0 is f(0, 1) = 2(0) = 0, so the method predicts no change. The exact solution is y = x² + 1, giving y(0.5) = 1.25. The error is 0.25 — Euler's method misses the curvature entirely in this step because the slope is changing (it's 0 at x=0 but grows), yet we only use the slope at the left endpoint."

- question: "If you reduce the step size h by half in Euler's method while approximating over the same total interval, what happens to the total (global) error?"
  type: multiple-choice
  options:
    - "Error is reduced by a factor of 4 — halving h gives quadratic improvement"
    - "Error is roughly halved — Euler's method is first-order accurate"
    - "Error is unchanged — more steps accumulate more error, canceling the per-step improvement"
    - "Error is reduced by a factor of √2 — each step's error decreases as √h"
  answer: 1
  explanation: "Euler's method is first-order accurate: global error is proportional to h. Halving h doubles the number of steps (from N to 2N) but each step's local error is proportional to h², so local error is quartered. Combined: 2N steps × (h/2)² local error per step ≈ 2N × h²/4 ∝ h. Net effect: halving h halves the global error. Option A would describe a second-order method like the improved Euler (Heun's method) or RK2."

- question: "Halving the step size in Euler's method reduces the total accumulated error quadratically — that is, by a factor of 4."
  type: true-false
  answer: false
  explanation: "Euler's method is first-order accurate, meaning global error is proportional to h (not h²). Halving h only halves the global error, not quarters it. A factor-of-4 improvement per halving would describe a second-order method. This distinction matters practically: to gain one extra decimal digit of accuracy with Euler's method, you must use ten times as many steps — much more expensive than higher-order methods like Runge-Kutta 4, which achieves the same digit with only about 1.8× more steps."

- question: "Euler's method uses only the slope at the left endpoint of each step interval to predict the next value, without incorporating any slope information from within the interval."
  type: true-false
  answer: true
  explanation: "The update rule y_{n+1} = y_n + h·f(x_n, y_n) uses f(x_n, y_n) — the slope at the start of the interval — and then walks a straight line to the next point. It ignores the fact that the slope changes across the interval. This is the source of local truncation error: the true curve curves, but Euler follows a tangent line. Higher-order methods like RK4 evaluate the slope at multiple points within each interval (the midpoint, endpoint, etc.) to get a more representative average slope, achieving much smaller error for the same step size."

- question: "Why does Euler's method accumulate error over many steps, even though the linear approximation formula underlying each step is mathematically correct?"
  type: short-answer
  answer: "Each step of Euler's method is a linear approximation: it assumes the slope is constant across the interval [x_n, x_{n+1}], equal to f(x_n, y_n). But the true solution curves — the slope changes — so each step drifts slightly from the true curve. This per-step drift (local truncation error, proportional to h²) is small for small h. However, to cover a fixed interval [x₀, X], you need 1/h steps, so errors accumulate over many steps. The total global error is (1/h) × h² = h — small but nonzero. Crucially, each step starts from the wrong point (because previous steps already introduced error), so errors compound rather than cancel."
  explanation: "The intuition is geometric: Euler walks along tangent lines. Each tangent line is slightly off from the curve, and you start the next step from the end of the wrong tangent line. The cumulative effect is that you wander progressively further from the true solution. Making h smaller keeps each tangent line closer to the curve and reduces compounding — but no matter how small h is, there is always some positive error unless the true solution is itself linear."
```

## Explainer

From **linear approximation**, you know that near any point (x₀, y₀) on a differentiable curve, the tangent line is a good local approximation: y ≈ y₀ + y'(x₀) · (x − x₀). **Euler's method** is simply this idea applied repeatedly to trace out an approximate solution to a differential equation. You have an initial value problem: y' = f(x, y) with y(x₀) = y₀. You don't know the solution curve, but you know its *slope at every point* (that's what the ODE gives you: the slope at (x, y) is f(x, y)). So you take a small step along the tangent line, arrive at an approximate new point, recompute the slope there, take another small step, and continue.

The update rule is **y_{n+1} = y_n + h · f(x_n, y_n)**, where h is the **step size**. At each step, you're walking along the current tangent line for a horizontal distance h. The new x-coordinate is x_{n+1} = x_n + h, and the new y-coordinate uses the current slope f(x_n, y_n) multiplied by the step size. This is exactly the linear approximation formula with h playing the role of Δx. To apply it: start at (x₀, y₀), compute the slope f(x₀, y₀), step to (x₁, y₁) = (x₀ + h, y₀ + h · f(x₀, y₀)), then repeat.

The approximation accumulates **error** for two reasons. First, **local truncation error**: each step drifts from the true curve because the slope changes between x_n and x_{n+1}, but you use only the slope at x_n. This error is proportional to h² per step. Second, **global error**: you take 1/h steps to reach a fixed endpoint, so errors accumulate, giving a total global error proportional to h. Halving the step size roughly halves the total error — hence "first-order accurate." More sophisticated methods like Runge-Kutta use multiple slope estimates per step to achieve much better accuracy for the same computational cost.

The intuition for when Euler's method works well versus poorly is essential. It works well when the solution is nearly linear locally (the derivative of y' is small) and the step size is small relative to how quickly the slope changes. It fails badly when the solution curves sharply or when the ODE is **stiff** (has components that vary on very different time scales). The most instructive example is y' = y with y(0) = 1: the exact solution is eˣ. Euler's method gives y_{n+1} = y_n + h · y_n = y_n(1 + h), so after n steps, yₙ = (1 + h)^n. With x = nh fixed and h → 0, this approaches e^x — exactly recovering the exponential, which is a reassuring confirmation that the method is consistent with the exact solution in the limit.
