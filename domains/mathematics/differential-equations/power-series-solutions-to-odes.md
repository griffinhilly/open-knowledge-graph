---
id: power-series-solutions-to-odes
title: Power Series Solutions to Differential Equations
domain: mathematics
course: differential-equations
prerequisites:
- id: power-series
  type: hard
- id: second-order-linear-homogeneous-odes
  type: hard
builds-toward:
- ordinary-and-singular-points
- frobenius-method
tags:
- series
- method
- special-functions
stage: formal-systems
status: draft
---

# Power Series Solutions to Differential Equations

## Core Idea
For ODEs that don't have elementary closed-form solutions, assume a power series solution y = Σ(a_n·x^n) and substitute into the ODE to find a recurrence relation for coefficients a_n. This yields convergent power series solutions valid near x = 0.

## How It's Best Learned
Work through Airy's equation or Bessel's equation. Substitute y = Σ(a_n·x^n) and y' = Σ(n·a_n·x^{n-1}), then collect powers of x and equate coefficients to zero.

## Common Misconceptions
- Confusing power series solutions with Taylor series approximations; they are exact within their radius of convergence. - Not recognizing the radius of convergence limitations. - Making algebra errors when equating coefficients of like powers.

## Explainer

You know how to solve second-order linear ODEs with constant coefficients using the characteristic equation — assuming exponential solutions works because eˣ is its own derivative. But many important ODEs have **variable coefficients**, where the multipliers on y'', y', and y depend on x. An example is Airy's equation y'' − xy = 0, which governs quantum tunneling and optics. The characteristic equation trick doesn't apply. The **power series method** is the systematic approach: assume the solution is an infinite polynomial and determine the coefficients by substituting into the ODE.

The assumption is y = a₀ + a₁x + a₂x² + a₃x³ + ... = Σₙ₌₀^∞ aₙxⁿ. Within its radius of convergence, a power series can be differentiated term by term: y' = Σₙ₌₁^∞ naₙxⁿ⁻¹ and y'' = Σₙ₌₂^∞ n(n−1)aₙxⁿ⁻². You substitute these series into the ODE, collect all terms containing the same power of x, and require each coefficient to be zero (since a power series is identically zero only if all its coefficients vanish). This produces a **recurrence relation**: a formula expressing each aₙ in terms of earlier coefficients, letting you compute the solution one coefficient at a time.

As a worked example, consider y'' + y = 0. Substituting gives Σₙ₌₂^∞ n(n−1)aₙxⁿ⁻² + Σₙ₌₀^∞ aₙxⁿ = 0. Re-index the first sum with m = n−2 so both sums run over xᵐ: Σₘ₌₀^∞ [(m+2)(m+1)aₘ₊₂ + aₘ] xᵐ = 0. Setting each bracket to zero gives the recurrence aₘ₊₂ = −aₘ / [(m+2)(m+1)]. Starting from free parameters a₀ and a₁, this generates two independent series: one involving only even powers (the Taylor series for cos x) and one involving only odd powers (the Taylor series for sin x). The power series method has re-derived a result you already know — but it works equally well on equations like Airy's where no closed form in elementary functions exists.

The series solution is exact, not an approximation: within its **radius of convergence**, the power series satisfies the ODE at every point. The radius of convergence is determined by the nearest singularity of the coefficient functions — if the variable coefficients are analytic everywhere (like a polynomial), the series may converge for all x. The method fails at **singular points** of the ODE — values of x where the leading coefficient vanishes or the equation becomes irregular. Handling those cases requires the Frobenius method, where you generalize the power series assumption to allow non-integer powers of x. For now, the ordinary point case (coefficients analytic near x = 0) is the foundation you need.
