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

## Explainer

Euler's method translates the geometric meaning of a derivative into a computational recipe. You know that dy/dx = f(x, y) at a point (x, y) gives the slope of the solution curve passing through that point. If you start at a known point (x₀, y₀) and know the slope there, you can step a small distance h forward in x and estimate where the curve goes: y₁ ≈ y₀ + h · f(x₀, y₀). This is just the **linear approximation** — instead of following the actual curve, you follow the tangent line. Repeat from (x₁, y₁) using the new slope, and you trace out an approximate solution one step at a time.

The formula y_{n+1} = y_n + h · f(x_n, y_n) is the **Euler step**. At each iteration, the current position determines the slope, and you advance by that slope times the step size. The approximation accumulates error because the actual solution curves away from the tangent line — after one step you are slightly off, and each subsequent step starts from a slightly wrong position. The **local truncation error** (error in a single step) is proportional to h², while the **global error** (accumulated over an entire interval of length L) is proportional to h. This is why Euler's method is called a "first-order" method: halving h halves the total error.

A concrete example makes the accuracy visible. Consider dy/dx = y with y(0) = 1, whose exact solution is eˣ. Using h = 0.1: y₁ = 1 + 0.1(1) = 1.1, y₂ = 1.1 + 0.1(1.1) = 1.21, and in general y_n = (1.1)ⁿ. After 10 steps (at x = 1), Euler gives (1.1)¹⁰ ≈ 2.594, while e¹ ≈ 2.718 — about a 4.5% error. Halving to h = 0.05 and taking 20 steps gives roughly half the error, confirming the first-order behavior. Notice that (1.1)ⁿ is the compound interest formula — Euler's method on exponential growth is discrete compounding.

Euler's method matters not because it is the most accurate numerical approach — for practical work it is usually too slow to converge — but because it makes the structure of numerical ODE solving fully transparent. Higher-order methods like **Runge-Kutta** use multiple slope evaluations per step to estimate the average slope over the interval more accurately, reducing the leading error term. Understanding Euler's method gives you the conceptual framework for understanding why those improvements work and how to reason about error in any numerical scheme.
