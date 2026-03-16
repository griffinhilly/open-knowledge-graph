---
id: frobenius-method
title: Frobenius Method and Equations with Singular Points
domain: mathematics
course: differential-equations
prerequisites:
- id: power-series-solutions
  type: hard
- id: continuity-definition
  type: soft
builds-toward:
- bessel-functions
- legendre-equations
tags:
- frobenius-method
- singular-points
- series-solution
stage: advanced
status: draft
---

# Frobenius Method and Equations with Singular Points

## Core Idea
For regular singular points where (x-x₀)p and (x-x₀)²q are analytic in y'' + p(x)y' + q(x)y = 0, the Frobenius method seeks y = (x-x₀)^r Σ aₙ(x-x₀)^n. Substituting yields an indicial equation for r and a recurrence relation for coefficients. Two independent solutions typically arise from different indicial roots. This method extends power series to a broader class of important equations.

## Explainer

You've already learned to solve ODEs near ordinary points using power series: substitute y = Σ aₙ(x - x₀)^n, plug into the equation, and match coefficients to find a recurrence. But many of the most important equations in physics — Bessel's equation, Legendre's equation, the hypergeometric equation — have **singular points** where p(x) or q(x) blow up and the plain power series method fails. The Frobenius method extends the idea to handle a special, well-behaved class of singularities called **regular singular points**.

A singular point x₀ is **regular** if the coefficients satisfy a specific growth condition: (x - x₀)p(x) and (x - x₀)²q(x) must both be analytic (expandable as convergent power series) near x₀. Intuitively, the singularity can't be too bad — p(x) can blow up like 1/(x - x₀) and q(x) like 1/(x - x₀)², but not faster. When this condition holds, you're guaranteed at least one solution of the **Frobenius form**: y = (x - x₀)^r Σₙ₌₀^∞ aₙ(x - x₀)^n. The exponent r is now a free parameter — not necessarily an integer — that the equation itself will determine. Plain power series correspond to r = 0; the Frobenius method lets r be any real (or even complex) number.

The procedure starts by substituting the Frobenius series into the ODE. Collecting the lowest-power term gives you the **indicial equation**: a quadratic in r whose roots r₁ ≥ r₂ are the two candidate exponents. The larger root r₁ always yields a valid Frobenius series. Whether the smaller root r₂ gives a second independent Frobenius series or requires a logarithmic term depends on r₁ - r₂: if it is not a non-negative integer, both roots give distinct Frobenius series; if r₁ = r₂ or r₁ - r₂ is a positive integer, the second solution involves ln(x - x₀) multiplied by a Frobenius series. Once r is fixed, the coefficients aₙ satisfy a recurrence relation obtained by equating each power's coefficient to zero.

The Frobenius method reveals why Bessel's equation x²y'' + xy' + (x² - ν²)y = 0 has solutions of the form x^ν times a power series: x = 0 is a regular singular point with indicial roots r = ±ν. The **Bessel functions** Jₙ(x) you'll encounter next are precisely these Frobenius solutions, built coefficient-by-coefficient from the recurrence. The method acts as a bridge — it explains the unusual non-integer power behavior of important special functions and provides a systematic algorithm for computing them to any desired order, making it indispensable across mathematical physics and engineering.
