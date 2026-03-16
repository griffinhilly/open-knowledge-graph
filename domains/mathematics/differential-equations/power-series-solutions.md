---
id: power-series-solutions
title: Power Series Solutions to Differential Equations
domain: mathematics
course: differential-equations
prerequisites:
- id: power-series
  type: hard
- id: taylor-series
  type: hard
- id: higher-order-linear-odes
  type: hard
builds-toward:
- frobenius-method
tags:
- power-series
- analytic-solutions
- series-method
stage: formal-systems
status: draft
---

# Power Series Solutions to Differential Equations

## Core Idea
When an ODE cannot be solved by standard methods, assume a power series solution y = Σ aₙx^n, substitute into the equation, and match coefficients to find aₙ. This approach works when the equation has an analytic solution around a point. Recurrence relations for the coefficients determine the solution, usually yielding two linearly independent series from different initial conditions.

## Explainer

You have already solved second-order linear ODEs when the coefficients are constants: you guess y = eʳˣ, plug in, find the characteristic equation, and recover the solution. But many important ODEs — Bessel's equation, Legendre's equation, the simple harmonic oscillator with non-constant forcing — have **variable coefficients** that invalidate the exponential guess. The **power series method** replaces the exponential ansatz with a more flexible one: assume y = a₀ + a₁x + a₂x² + ⋯ = Σₙ₌₀^∞ aₙxⁿ, then determine what the coefficients aₙ must be for y to satisfy the ODE.

The mechanics of the method rely on your knowledge of Taylor series. If y is a power series, its derivative is also a power series: y' = Σ n·aₙxⁿ⁻¹, y'' = Σ n(n−1)aₙxⁿ⁻², and so on. Substitute y, y', y'' into the ODE, multiply out any variable-coefficient terms, and collect all powers of x together. For the result to equal zero (since the ODE is set to zero), the coefficient of each power xᵏ must independently equal zero. This gives you infinitely many equations — one for each power — but they are linked by a **recurrence relation**: aₙ₊₂ in terms of aₙ, or aₙ₊₁ in terms of aₙ, depending on the ODE. Once you find the recurrence, you can compute as many coefficients as you need from two free parameters (typically a₀ and a₁).

The two free parameters correspond to the two linearly independent solutions you expect from a second-order ODE. Choosing a₀ = 1, a₁ = 0 generates one solution; choosing a₀ = 0, a₁ = 1 generates a second, independent solution. Both are power series, and their span gives the general solution. If you recognize the series as a Taylor series you know — say, cos x or eˣ — you can write it in closed form. If not, the series itself is the answer, and you truncate it to as many terms as precision requires. This is exactly how many of the "special functions" of mathematical physics were first discovered and named.

The method works reliably when the ODE has an **ordinary point** at x = 0 — meaning the coefficient functions are analytic there (equal their Taylor series in a neighborhood). At an ordinary point, both independent solutions are guaranteed to be analytic, and the power series method produces them directly. When x = 0 is instead a **singular point**, the solutions may involve logarithms or non-integer powers, and the method requires modification (the Frobenius method). Understanding which case you are in — ordinary or singular — is the first diagnostic step whenever you reach for the series approach. The power series method is ultimately the bridge between the finite, closed-form solutions of constant-coefficient ODEs and the infinite-dimensional function spaces that naturally arise in physics and engineering.
