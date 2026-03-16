---
id: legendre-equations
title: Legendre Equations and Legendre Polynomials
domain: mathematics
course: differential-equations
prerequisites:
- id: frobenius-method
  type: hard
builds-toward:
- fourier-series-definition
tags:
- legendre-polynomials
- special-functions
- orthogonal
stage: advanced
status: draft
---

# Legendre Equations and Legendre Polynomials

## Core Idea
Legendre's equation (1-x²)y'' - 2xy' + n(n+1)y = 0 has polynomial solutions P_n(x) for non-negative integers n. These arise in spherically symmetric problems and are orthogonal on [-1,1] with respect to the standard inner product. Legendre polynomials have generating functions, recurrence relations, and explicit formulas, forming the basis for Legendre expansions.

## Explainer

The Legendre equation arises naturally when you solve Laplace's equation ∇²φ = 0 in spherical coordinates and separate variables. The angular part of the solution leads to (1−x²)y'' − 2xy' + n(n+1)y = 0, where x = cos(θ) is the polar angle variable. This is a second-order linear ODE with non-constant coefficients and ordinary points everywhere on (−1, 1), so the **Frobenius method** you learned tells you to seek a power series solution y = Σ aₖxᵏ around x = 0.

Substituting into the equation and collecting powers of x gives a **recurrence relation**: aₖ₊₂ = −[n(n+1) − k(k+1)] / [(k+2)(k+1)] · aₖ. The series is determined by the choice of a₀ and a₁ (giving two independent solutions). Here is the key observation: if n is a non-negative integer, the recurrence terminates — the coefficient aₙ₊₂ = 0, and all subsequent coefficients vanish. The series becomes a **polynomial** of degree n. These terminating solutions are the **Legendre polynomials** P_n(x), normalized so P_n(1) = 1. The first few are: P₀(x) = 1, P₁(x) = x, P₂(x) = (3x²−1)/2, P₃(x) = (5x³−3x)/2.

The **orthogonality** of Legendre polynomials is what makes them useful: ∫₋₁¹ Pₘ(x)Pₙ(x) dx = 0 whenever m ≠ n. This mirrors how sine and cosine functions are orthogonal on [−π, π] — the key property that makes Fourier series work. Because Legendre polynomials are orthogonal, any reasonable function f on [−1, 1] can be expanded as f(x) = Σ cₙ Pₙ(x), where the coefficients are extracted by the inner product: cₙ = [(2n+1)/2] ∫₋₁¹ f(x) Pₙ(x) dx. This is a **Legendre expansion** — the spherical analogue of a Fourier series.

A practical tool is the **recurrence relation** between consecutive polynomials: (n+1)Pₙ₊₁(x) = (2n+1)x Pₙ(x) − n Pₙ₋₁(x). This lets you compute any Pₙ efficiently without re-deriving the series. Legendre polynomials appear throughout mathematical physics — gravitational and electrostatic potentials in spherical geometry, quantum mechanics of the hydrogen atom, and heat conduction on spheres — wherever physical symmetry makes spherical coordinates natural.
