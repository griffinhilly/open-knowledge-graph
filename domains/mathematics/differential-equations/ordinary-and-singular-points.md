---
id: ordinary-and-singular-points
title: Ordinary and Singular Points of ODEs
domain: mathematics
course: differential-equations
prerequisites:
- id: power-series-solutions-to-odes
  type: hard
- id: analytic-functions
  type: soft
builds-toward:
- frobenius-method
tags:
- series
- classification
- analytic
stage: advanced
status: draft
---

# Ordinary and Singular Points of ODEs

## Core Idea
For y'' + p(x)y' + q(x)y = 0, a point x₀ is ordinary if p and q are analytic at x₀ (power series solutions exist), and singular if either is not. Regular singular points admit Frobenius series solutions; irregular singular points do not.

## Explainer

From your work with power series solutions, you know that you can assume y = ∑ aₙ(x − x₀)ⁿ, substitute into a differential equation, and solve for the coefficients by matching powers of (x − x₀). This method works beautifully when the equation behaves well near x₀. But not all equations behave well everywhere: some have coefficients that blow up at certain points, and near those points the standard power series method breaks down. The classification into ordinary and singular points is exactly the question of where the method works versus where it needs modification.

Write the equation in **standard form**: y'' + p(x)y' + q(x)y = 0. A point x₀ is called an **ordinary point** if both p(x) and q(x) are analytic at x₀ — meaning each can be represented by a convergent power series in a neighborhood of x₀. Near an ordinary point, the existence theorem guarantees two linearly independent power series solutions, and the radius of convergence extends at least as far as the nearest singular point. The familiar examples (like Hermite's equation or simple harmonic oscillator) have no singular points or have them far from the origin, which is why power series solutions in those cases are straightforward.

A **singular point** is any x₀ where p(x) or q(x) fails to be analytic. Not all singular points are equally bad. A point x₀ is a **regular singular point** if (x − x₀)p(x) and (x − x₀)²q(x) are both analytic at x₀ — that is, p(x) has at most a simple pole and q(x) has at most a double pole at x₀. The multiplication by (x − x₀) and (x − x₀)² "removes" the bad behavior just enough. The Euler equation x²y'' + αxy' + βy = 0 is the prototype: at x₀ = 0, p(x) = α/x (simple pole) and q(x) = β/x² (double pole), so x · p(x) = α and x² · q(x) = β are both constant — definitely analytic. Euler equations are exactly the regular singular case in its purest form.

An **irregular singular point** is one where the singularity is worse: (x − x₀)p(x) or (x − x₀)²q(x) is still singular. Near irregular singular points, power series and Frobenius series both fail, and solutions typically involve essential singularities, exponential factors, or formal divergent series. The theory is much harder and outside most first courses.

The classification matters because it tells you which tool to reach for. Near an ordinary point, use standard power series. Near a regular singular point, use the **Frobenius method** (which you'll study next): assume y = (x − x₀)^r ∑ aₙ(x − x₀)ⁿ, where the exponent r is determined by the **indicial equation** formed from the coefficients of p and q. The indicial equation typically gives two roots r₁, r₂, and depending on whether r₁ − r₂ is a non-integer, zero, or a positive integer, you get two independent Frobenius series, one series and one series times ln(x − x₀), or other special forms. Identifying the type of point before computing is not a formality — it determines whether you proceed with a standard series, a Frobenius series, or need more advanced methods entirely.
