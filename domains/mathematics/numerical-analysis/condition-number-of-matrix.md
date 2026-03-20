---
id: condition-number-of-matrix
title: Condition Number of a Matrix
domain: mathematics
course: numerical-analysis
prerequisites:
- id: condition-number
  type: hard
- id: matrix-operations
  type: hard
builds-toward:
- jacobi-iterative-method
tags:
- condition-number
- matrix
- ill-conditioning
stage: formal-systems
status: draft
---

# Condition Number of a Matrix

## Core Idea
The condition number of a matrix A is κ(A) = ‖A‖ ‖A⁻¹‖, measuring how much small perturbations in A or b affect the solution x to Ax = b. If κ(A) is large, the system is ill-conditioned: small changes in inputs produce large changes in outputs. The condition number depends on the chosen norm; large κ(A) indicates potential numerical difficulties regardless of algorithm.

## Explainer

You know from your prerequisite work that the general condition number of a problem measures relative output sensitivity to relative input perturbation. The condition number of a matrix specializes this idea to linear systems Ax = b, where the "problem" is "given b, find x = A⁻¹b." You also know matrix operations well enough to manipulate A and its inverse. Now the question becomes: how does a small change in the right-hand side b affect the solution x?

If b is perturbed to b + δb, the solution changes to x + δx = A⁻¹(b + δb), giving δx = A⁻¹δb. Taking norms: ‖δx‖ ≤ ‖A⁻¹‖ ‖δb‖. To convert this to a relative error bound, divide both sides and use ‖b‖ ≤ ‖A‖ ‖x‖ to get ‖δx‖/‖x‖ ≤ ‖A‖ ‖A⁻¹‖ · ‖δb‖/‖b‖. The factor ‖A‖ ‖A⁻¹‖ = κ(A) is the **condition number** — it amplifies relative input error into relative output error.

For the 2-norm (Euclidean), κ₂(A) = σ_max/σ_min, the ratio of the largest to smallest singular value. Geometrically, A transforms the unit sphere into an ellipsoid; σ_max and σ_min are the longest and shortest semi-axes. A large condition number means the ellipsoid is very elongated — A stretches some directions enormously while nearly collapsing others. The inverse A⁻¹ must reverse this, enormously amplifying the nearly-collapsed directions. When b has any component in those directions (and floating-point b always will, due to rounding), that component blows up in the solution.

A nearly singular matrix illustrates this concretely. Consider A = [[1, 1], [1, 1+ε]] for small ε. The determinant is ε, so A⁻¹ has entries of order 1/ε, giving κ(A) ≈ 4/ε². For ε = 0.001, κ ≈ 4×10⁶. A useful rule of thumb: if κ(A) ≈ 10^k, solving Ax = b costs you roughly k decimal digits of accuracy. Starting with double-precision arithmetic (about 15–16 digits), a condition number of 10¹⁰ leaves only 5–6 reliable digits in the solution — even if your algorithm is perfect. The condition number characterizes what is achievable, not how well you solved it.
