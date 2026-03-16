---
id: newton-divided-differences
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
- interpolation
- newton
stage: abstract-reasoning
status: draft
---

# Newton's Divided Differences

## Core Idea
Newton's divided difference formula represents the interpolating polynomial as P(x) = f[x_0] + f[x_0,x_1](x-x_0) + f[x_0,x_1,x_2](x-x_0)(x-x_1) + ..., where divided differences are defined recursively. This form is numerically stable and allows efficient addition of new points by appending terms without recomputing previous coefficients.

## How It's Best Learned
Construct divided difference tables by hand for small datasets, then implement the recurrence relation to see how coefficients build up naturally.

## Common Misconceptions
- Thinking divided differences are the same as derivatives; they are discrete approximations that approach derivatives as points converge.
- Assuming the divided difference formula is just a rearrangement of Lagrange; it expresses the same polynomial more stably and flexibly.

## Explainer

From Lagrange interpolation, you know that given n+1 data points (x₀, f₀), …, (xₙ, fₙ), there is a unique polynomial of degree ≤ n passing through all of them. Lagrange writes it as a sum of basis polynomials Lᵢ(x), each of which is 1 at xᵢ and 0 at all other nodes. This representation is mathematically elegant but computationally awkward: if you receive one new data point and must add it to your interpolant, you have to recompute every Lagrange basis polynomial from scratch. Newton's **divided difference** form solves this by building the same polynomial in a nested, additive structure that makes adding points trivial.

The **zeroth-order divided difference** is just the function value: f[xᵢ] = f(xᵢ). The **first-order divided difference** is the slope of the secant line: f[xᵢ, xⱼ] = (f[xⱼ] − f[xᵢ])/(xⱼ − xᵢ). Higher-order divided differences are defined recursively: f[x₀, x₁, …, xₙ] = (f[x₁, …, xₙ] − f[x₀, …, xₙ₋₁])/(xₙ − x₀). You build a triangular table: the first column is function values, the second column is first-order differences of adjacent pairs, the third column is second-order differences, and so on. The diagonal entries — f[x₀], f[x₀, x₁], f[x₀, x₁, x₂], … — become the coefficients of the Newton interpolating polynomial.

The Newton form then reads: P(x) = f[x₀] + f[x₀, x₁](x − x₀) + f[x₀, x₁, x₂](x − x₀)(x − x₁) + ···. Each new term tacks on one more factor (x − xₖ) and one new divided difference coefficient, leaving all previous terms unchanged. This is the crucial advantage over Lagrange: to add a new data point xₙ₊₁, simply compute one new column in the divided difference table and append one new term to the polynomial. No recomputation needed. Think of it as building the polynomial incrementally, the way you might fit a line first, then bend it to pass through a third point, then a fourth, each time adjusting the curve only as much as needed.

The connection to calculus is real: if all nodes collapse to a single point x₀, the kth-order divided difference approaches f^(k)(x₀)/k! — the Taylor coefficient. Divided differences are the finite-difference analogue of derivatives, well-defined even when the nodes are distinct. This analogy also explains why Newton's form is more numerically stable for near-coincident nodes: you are computing genuine approximations to derivatives rather than inverting a Vandermonde matrix, which becomes ill-conditioned when nodes are close together. In practice, Newton's divided differences are the foundation of adaptive interpolation algorithms, ODE solvers that add new mesh points on the fly, and any setting where data arrives incrementally.
