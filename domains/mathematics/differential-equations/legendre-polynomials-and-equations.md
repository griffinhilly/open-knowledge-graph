---
id: legendre-polynomials-and-equations
title: Legendre Polynomials and Legendre's Equation
domain: mathematics
course: differential-equations
prerequisites:
- id: frobenius-method
  type: hard
builds-toward:
- separation-of-variables-for-pdes
tags:
- special-functions
- legendre
- orthogonal
stage: advanced
status: draft
---

# Legendre Polynomials and Legendre's Equation

## Core Idea
Legendre's equation (1 - x²)y'' - 2xy' + n(n+1)y = 0 admits polynomial solutions P_n(x) when n is a non-negative integer. These Legendre polynomials form an orthogonal basis on [-1, 1] and arise in problems with spherical symmetry, particularly in solving Laplace's equation.

## How It's Best Learned
Compute the first few Legendre polynomials (P₀ = 1, P₁ = x, P₂ = (3x² - 1)/2) using the Frobenius method or Rodrigues' formula. Verify orthogonality: ∫₋₁¹ P_m(x)P_n(x) dx = 0 for m ≠ n.

## Explainer

You know the Frobenius method for ODEs near regular singular points. Legendre's equation (1−x²)y'' − 2xy' + n(n+1)y = 0 has a different structure: it is singular at x = ±1 but regular on the open interval (−1, 1) including at x = 0. Applying Frobenius at x = 0 produces a power series solution with a recurrence relation linking each coefficient to the one two steps back. The critical observation is that when n is a non-negative integer, the recurrence forces the coefficient of x^(n+2) to vanish — the series *terminates* after finitely many terms and becomes a polynomial. These terminating solutions, normalized so P_n(1) = 1, are the **Legendre polynomials**.

The first few are P₀ = 1, P₁ = x, P₂ = (3x²−1)/2, P₃ = (5x³−3x)/2. Notice the alternating parity: even-index P_n are even functions, odd-index are odd, directly reflecting the structure of the recurrence. When n is *not* a non-negative integer, neither Frobenius series terminates, and both solutions diverge at x = ±1 — making them unacceptable for physical problems on a closed interval. The requirement that solutions be finite at the endpoints *forces* n to be a non-negative integer, which is why the eigenvalues n(n+1) = 0, 2, 6, 12, 20, … form a discrete sequence.

The Legendre polynomials are **orthogonal on [−1, 1]**: ∫₋₁¹ P_m(x)P_n(x) dx = 0 for m ≠ n, and ∫₋₁¹ [P_n(x)]² dx = 2/(2n+1). This orthogonality is guaranteed by the **Sturm-Liouville structure** of Legendre's equation — it can be written as (d/dx)[(1−x²)y'] + n(n+1)y = 0, a self-adjoint eigenvalue problem. A general theorem says eigenfunctions of a self-adjoint operator with distinct eigenvalues are always orthogonal, so the P_n must be orthogonal without any computation. The result is that any "well-behaved" function f on [−1, 1] can be expanded as f(x) = Σ cₙ P_n(x), with cₙ = (2n+1)/2 ∫₋₁¹ f(x) P_n(x) dx.

The application that drives all of this is **Laplace's equation in spherical coordinates**. When you separate variables in ∇²u = 0, the angular part in the polar direction (colatitude θ) becomes Legendre's equation in x = cos θ. The demand that u be finite at the poles (cos θ = ±1, i.e., x = ±1) restricts solutions to the Legendre polynomials, and the general solution for problems with azimuthal symmetry is u(r, θ) = Σ (Aₙrⁿ + Bₙr^(−n−1)) P_n(cos θ). Legendre polynomials play the same role in spherical geometry that Fourier modes play in rectangular geometry: they are the natural "basis functions" for decomposing any spherically symmetric field.
