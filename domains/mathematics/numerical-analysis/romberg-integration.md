---
id: romberg-integration
title: Romberg Integration
domain: mathematics
course: numerical-analysis
prerequisites:
- id: richardson-extrapolation
  type: hard
- id: composite-quadrature
  type: hard
tags:
- romberg
- integration
- extrapolation
stage: advanced
status: draft
---

# Romberg Integration

## Core Idea
Romberg integration systematically applies composite trapezoidal rules with successive halvings of step size, then uses Richardson extrapolation to accelerate convergence. The method builds a triangular array where each new entry combines results from halved step size with previous entries to cancel error terms. Romberg achieves high accuracy efficiently and provides adaptive error estimation.

## Explainer

From your study of composite quadrature, you know the composite trapezoidal rule approximates ∫f(x)dx with error proportional to h² — halving the step size h reduces the error by a factor of four, requiring twice as many function evaluations. That convergence rate is fine but not spectacular. From Richardson extrapolation, you know a more powerful idea: if you have two estimates of a quantity with a known error structure, you can algebraically combine them to cancel the leading error term and get a much more accurate estimate without extra function evaluations. Romberg integration is what happens when you apply Richardson extrapolation repeatedly and systematically to the trapezoidal rule.

Start with the trapezoidal approximation T(h) at step size h. The **Euler–Maclaurin formula** tells us the error has the exact form: T(h) = I + c₁h² + c₂h⁴ + c₃h⁶ + ..., where I is the true integral and the cₖ are constants (depending on the function but not on h). This is the key structural fact: the error consists of even powers of h only. Halve h to get T(h/2) = I + c₁(h/2)² + c₂(h/2)⁴ + ... = I + c₁h²/4 + c₂h⁴/16 + ... Multiply the first equation by 1 and the second by 4, then subtract: the c₁h² term cancels, leaving a new estimate with error O(h⁴). This is Richardson extrapolation eliminating the leading error term.

The **Romberg table** applies this process repeatedly. Column 0 holds trapezoidal approximations T(h), T(h/2), T(h/4), ... (each row halves the step, doubling the function evaluations but cleverly reusing old ones since every other point of the finer grid already exists). Column 1 holds the Richardson combinations that cancel O(h²) error — these are Simpson's rule values. Column 2 cancels O(h⁴) error — these are Boole's rule values. Each successive column eliminates another error term, so the diagonal of the triangular table converges much faster than the first column alone. For smooth functions, the method achieves very high accuracy with relatively few function evaluations.

The table also provides a natural **error estimate**: compare the bottom-right entries in adjacent columns. If they agree to many decimal places, you have likely converged. If not, add another row (halve h again) and extend the table. This adaptive character makes Romberg practical: you keep refining until the error estimate is satisfactory, spending function evaluations only where needed. For smooth integrands, Romberg is often the method of choice — it combines the simplicity of the trapezoidal rule (easy to implement, robust, reuses evaluations) with the accuracy of high-order methods, all without requiring any special structure from the integrand beyond smoothness.
