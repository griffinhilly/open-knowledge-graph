---
id: newtons-divided-differences
title: Newton's Divided Differences
domain: mathematics
course: numerical-analysis
prerequisites:
- id: lagrange-polynomial-interpolation
  type: hard
builds-toward:
- interpolation-error-analysis
tags:
- divided-differences
- newton-polynomial
- efficiency
stage: advanced
status: draft
---

# Newton's Divided Differences

## Core Idea
Newton's divided differences provide an efficient recursive method to construct the interpolating polynomial in the form p(x) = a_0 + a_1(x-x_0) + a_2(x-x_0)(x-x_1) + .... The coefficients are computed via a systematic table, and new points can be added without recomputing all previous coefficients, making this form superior to Lagrange for practical computation.

## Explainer

From Lagrange interpolation you know that through any n+1 distinct points there is a unique polynomial of degree at most n. The Lagrange form constructs it as a sum of basis polynomials Lᵢ(x), each equal to 1 at xᵢ and 0 at all other nodes. That form is elegant but computationally awkward: if you add a new data point, you must recompute every basis polynomial from scratch. Newton's divided difference form solves this by building the polynomial incrementally.

The idea is to write the interpolating polynomial in **Newton's nested (forward difference) form**: p(x) = f[x₀] + f[x₀,x₁](x-x₀) + f[x₀,x₁,x₂](x-x₀)(x-x₁) + ... where f[x₀, x₁, …, xₖ] is a **divided difference** — a generalized slope. The zeroth-order divided difference is just the function value: f[xᵢ] = f(xᵢ). The first-order divided difference is the ordinary slope: f[xᵢ, xᵢ₊₁] = (f(xᵢ₊₁) - f(xᵢ))/(xᵢ₊₁ - xᵢ). Higher-order divided differences are defined recursively: f[x₀,…,xₖ] = (f[x₁,…,xₖ] - f[x₀,…,xₖ₋₁]) / (xₖ - x₀). The pattern fills a triangular table, and the top diagonal gives the coefficients a₀, a₁, a₂, … directly.

The computational payoff is **incremental updating**. Once you have the divided difference table for n+1 points, adding a new point (x_{n+1}, f(x_{n+1})) only requires extending the table with one new diagonal — previous entries are unchanged. Compare this to Lagrange form, where every basis polynomial must be rebuilt. Newton's form also evaluates efficiently via **Horner's method**: p(x) = a₀ + (x-x₀)(a₁ + (x-x₁)(a₂ + …)), reducing the number of multiplications from O(n²) to O(n).

A subtle but important fact: divided differences are **symmetric** in their arguments, meaning f[x₀, x₁, x₂] = f[x₂, x₀, x₁] = ... regardless of the order. This symmetry reveals that the divided difference f[x₀,…,xₙ] equals f⁽ⁿ⁾(ξ)/n! for some ξ in the interval spanned by the nodes — a direct connection to Taylor coefficients when the nodes collapse to a single point. This link between divided differences and derivatives is what makes Newton's form the natural foundation for the interpolation error analysis you will study next.
