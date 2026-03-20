---
id: contraction-mapping
title: Contraction Mapping Theorem
domain: mathematics
course: numerical-analysis
prerequisites:
- id: metric-spaces-definition
  type: hard
builds-toward:
- fixed-point-iteration
tags:
- contraction-mapping
- banach
- fixed-point
stage: formal-systems
status: draft
---

# Contraction Mapping Theorem

## Core Idea
The contraction mapping theorem (Banach fixed-point theorem) guarantees that if g is a contraction with Lipschitz constant L < 1 on a complete metric space, then g has a unique fixed point and iteration x_{n+1} = g(x_n) converges to it with exponential rate. This theorem justifies fixed-point and iterative methods throughout numerical analysis.

## Explainer

You already know what a metric space is: a set with a distance function that satisfies the usual geometric axioms. A **contraction** is a function g on a metric space that brings any two points strictly closer together: d(g(x), g(y)) ≤ L · d(x, y) for some fixed **Lipschitz constant** L strictly less than 1. The function "squeezes" the space. No matter how far apart x and y start, after applying g they are at most L times as far apart. After applying g twice, at most L² times. Repeating indefinitely, the images of any two starting points converge to the same limit.

The **Banach fixed-point theorem** (contraction mapping theorem) makes this rigorous. If g is a contraction on a **complete** metric space — one where every Cauchy sequence converges to a point in the space — then three things are simultaneously guaranteed: (1) there is exactly one **fixed point** x* satisfying g(x*) = x*, (2) it is unique, and (3) the iteration x_{n+1} = g(x_n) converges to x* from any starting point. Completeness is essential: it rules out the limit "escaping" to a missing boundary point. The error at step n is bounded by d(x_n, x*) ≤ L^n / (1 − L) · d(x_1, x_0), a formula derived from the geometric series.

The convergence is **exponential** in n. Each step multiplies the error by at most L. If L = 0.5, the error halves every step — 20 iterations give a factor of 2²⁰ ≈ 10⁶ improvement in accuracy. The proof of the theorem is itself a model of clarity: form the sequence x_0, g(x_0), g(g(x_0)), … and show it is Cauchy by bounding consecutive distances with a geometric series. The limit exists by completeness; then verify g maps it to itself by continuity. Uniqueness follows because two fixed points would have distance L times themselves — forcing zero distance between them.

In numerical analysis, the contraction mapping theorem justifies iterative root-finding and equation-solving. Solving f(x) = 0 is equivalent to finding a fixed point of g(x) = x − αf(x) for suitable α. The theorem converts the question "will this iteration converge?" into "is g a contraction on some neighborhood of the solution?" If yes, you immediately have existence, uniqueness, and a concrete error bound. Newton's method, Picard iteration for differential equations, and the power iteration for eigenvalues all fit this framework. The theorem is not just an existence result — it is a computational guarantee that tells you precisely how many steps you need.
