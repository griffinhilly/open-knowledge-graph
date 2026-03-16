---
id: contraction-mapping-theorem
title: Contraction Mapping Theorem (Banach Fixed Point)
domain: mathematics
course: topology
prerequisites:
- id: completeness-metric-spaces
  type: hard
builds-toward:
- differential-equations-existence
- numerical-analysis
tags:
- fixed-points
- contraction-mappings
- banach-theorem
stage: advanced
status: draft
---

# Contraction Mapping Theorem (Banach Fixed Point)

## Core Idea
If f: X → X is a contraction on a complete metric space (with Lipschitz constant < 1), then f has a unique fixed point and iterating f from any starting point converges to it. This theorem provides a constructive method for proving existence and uniqueness of solutions to differential equations and other problems.

## Explainer

A **fixed point** of a function f is a point x where f(x) = x — the function maps x to itself. Fixed points are ubiquitous in mathematics: the equilibrium of a dynamical system is a fixed point of its update rule, the solution of an equation x = g(x) is a fixed point of g, and many existence proofs reduce to finding a fixed point of a cleverly constructed map. The Contraction Mapping Theorem gives a clean, constructive answer to when a unique fixed point exists and how to find it.

A map f: X → X on a metric space is a **contraction** if it shrinks distances: d(f(x), f(y)) ≤ k · d(x, y) for all x, y, where 0 ≤ k < 1. The constant k is the **Lipschitz constant**, and the requirement k < 1 is critical — equal to 1 is not enough. Think of squeezing a rubber band: every pair of points gets strictly closer after each application of f. The theorem says that on a **complete** metric space (one where Cauchy sequences converge — your prerequisite), any contraction has a unique fixed point, and you can find it by iterating: start anywhere, apply f repeatedly, and the sequence x, f(x), f(f(x)), ... converges to the fixed point. Uniqueness follows because if there were two fixed points p and q, then d(p, q) = d(f(p), f(q)) ≤ k · d(p, q), which forces d(p, q) = 0, so p = q.

The completeness requirement is not optional. Without it, the successive iterates could form a Cauchy sequence that never converges within the space. Imagine applying a contraction on the open interval (0, 1) whose fixed point would be at 0 — the iterates approach 0, but 0 is not in the space. Completeness guarantees the limit exists *in* X, so the fixed point is actually achieved.

The theorem's real power is in applications. The **Picard-Lindelöf theorem** for existence and uniqueness of ODE solutions is a direct application: it constructs an integral operator on a space of functions and shows it is a contraction in the uniform metric on a sufficiently small interval. The unique fixed function of this operator is the unique solution to the ODE. Similarly, Newton's method and many root-finding algorithms can be analyzed as iterating a contraction, and the theorem gives explicit error bounds — after n iterations, the distance to the fixed point is at most kⁿ/(1−k) times the initial step size. This quantitative bound is a distinctive feature: not only does the theorem guarantee existence, it gives you a rate of convergence.
