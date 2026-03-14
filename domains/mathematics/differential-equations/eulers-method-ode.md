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
stage: advanced
status: draft
---

# Euler's Method for Numerical Solution of ODEs

## Core Idea
Euler's method is a first-order numerical technique for solving dy/dx = f(x,y) with initial condition y(x₀) = y₀. At each step, advance by h using y_{n+1} = y_n + h·f(x_n, y_n). While simple and intuitive, Euler's method has limited accuracy but serves as the foundation for understanding numerical ODE solving and error propagation.
