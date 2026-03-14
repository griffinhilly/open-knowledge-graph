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
