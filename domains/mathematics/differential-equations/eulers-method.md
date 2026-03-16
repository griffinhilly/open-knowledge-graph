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
status: draft
---

# Euler's Method for Numerical Solutions

## Core Idea
Euler's method approximates solutions to initial value problems y' = f(x,y), y(x₀) = y₀ by stepping forward: y_{n+1} ≈ y_n + h·f(x_n, y_n). Though simple and first-order accurate, it provides intuition for numerical ODE solving and forms the basis for more sophisticated methods.

## How It's Best Learned
Implement Euler's method by hand for a few steps on a simple problem (like y' = y), then compare with the exact solution to see accumulated error. Explore how step size h affects accuracy.

## Common Misconceptions
- Thinking Euler's method is exact; it's an approximation with error proportional to h. - Using a step size that's too large, leading to significant local truncation errors. - Confusing Euler's method with exact separation of variables or other analytical methods.

## Explainer

From **linear approximation**, you know that near any point (x₀, y₀) on a differentiable curve, the tangent line is a good local approximation: y ≈ y₀ + y'(x₀) · (x − x₀). **Euler's method** is simply this idea applied repeatedly to trace out an approximate solution to a differential equation. You have an initial value problem: y' = f(x, y) with y(x₀) = y₀. You don't know the solution curve, but you know its *slope at every point* (that's what the ODE gives you: the slope at (x, y) is f(x, y)). So you take a small step along the tangent line, arrive at an approximate new point, recompute the slope there, take another small step, and continue.

The update rule is **y_{n+1} = y_n + h · f(x_n, y_n)**, where h is the **step size**. At each step, you're walking along the current tangent line for a horizontal distance h. The new x-coordinate is x_{n+1} = x_n + h, and the new y-coordinate uses the current slope f(x_n, y_n) multiplied by the step size. This is exactly the linear approximation formula with h playing the role of Δx. To apply it: start at (x₀, y₀), compute the slope f(x₀, y₀), step to (x₁, y₁) = (x₀ + h, y₀ + h · f(x₀, y₀)), then repeat.

The approximation accumulates **error** for two reasons. First, **local truncation error**: each step drifts from the true curve because the slope changes between x_n and x_{n+1}, but you use only the slope at x_n. This error is proportional to h² per step. Second, **global error**: you take 1/h steps to reach a fixed endpoint, so errors accumulate, giving a total global error proportional to h. Halving the step size roughly halves the total error — hence "first-order accurate." More sophisticated methods like Runge-Kutta use multiple slope estimates per step to achieve much better accuracy for the same computational cost.

The intuition for when Euler's method works well versus poorly is essential. It works well when the solution is nearly linear locally (the derivative of y' is small) and the step size is small relative to how quickly the slope changes. It fails badly when the solution curves sharply or when the ODE is **stiff** (has components that vary on very different time scales). The most instructive example is y' = y with y(0) = 1: the exact solution is eˣ. Euler's method gives y_{n+1} = y_n + h · y_n = y_n(1 + h), so after n steps, yₙ = (1 + h)^n. With x = nh fixed and h → 0, this approaches e^x — exactly recovering the exponential, which is a reassuring confirmation that the method is consistent with the exact solution in the limit.
