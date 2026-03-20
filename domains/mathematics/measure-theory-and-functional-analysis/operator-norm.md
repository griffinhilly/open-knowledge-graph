---
id: operator-norm
title: The Operator Norm
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: bounded-linear-operators
  type: hard
builds-toward:
- linear-functionals-dual-spaces
tags:
- functional-analysis
- operators
stage: advanced
status: draft
---

# The Operator Norm

## Core Idea
For a bounded linear operator T: X → Y, the operator norm is ‖T‖ = sup{‖T(x)‖_Y : ‖x‖_X ≤ 1}. The space ℒ(X,Y) of bounded operators is itself a normed space (Banach if Y is Banach).

## Explainer

From bounded linear operators, you know that T: X → Y is bounded if there exists a constant C such that ‖T(x)‖_Y ≤ C‖x‖_X for every x ∈ X. Many constants C work — the **operator norm** ‖T‖ is the smallest one that does. Formally, ‖T‖ = sup{‖T(x)‖_Y : ‖x‖_X ≤ 1}, which is the supremum of ‖T(x)‖ over the unit ball. Equivalently, ‖T‖ = sup{‖T(x)‖ / ‖x‖ : x ≠ 0}, the worst-case stretching factor. The operator norm answers: "by at most how much can T amplify a vector?"

In finite dimensions — when X = Rⁿ and Y = Rᵐ with their standard norms — every linear map is a matrix multiplication and every matrix is bounded. The operator norm of a matrix A (with respect to Euclidean norms) equals its largest singular value, which you might have seen as the square root of the largest eigenvalue of AᵀA. The unit ball in Rⁿ is a round sphere; T maps it to an ellipsoid in Rᵐ; the operator norm is the length of the longest axis of that ellipsoid. This geometric picture carries over to infinite dimensions, though "ellipsoid" becomes an abstract image.

The deeper significance of the operator norm is that it makes ℒ(X, Y) — the set of all bounded linear operators from X to Y — into a **normed space**. The norm axioms all check out: ‖T‖ = 0 if and only if T is the zero operator, ‖αT‖ = |α|‖T‖, and the triangle inequality ‖S + T‖ ≤ ‖S‖ + ‖T‖ holds. This means you can add operators, scale them, and take limits within ℒ(X, Y) using the operator norm as the notion of convergence. When Y is a Banach space (complete with respect to its norm), ℒ(X, Y) is also Banach — Cauchy sequences of operators converge to operators.

The operator norm also satisfies the submultiplicativity property ‖ST‖ ≤ ‖S‖‖T‖ whenever the composition makes sense. This is the operator analog of the scalar inequality |ab| = |a||b|, but it is an *inequality* rather than equality because composing two operators may not stretch as much as each would alone. Submultiplicativity is what makes the operator norm a **Banach algebra norm** on ℒ(X, X), the square case. This structure underpins the theory of functional calculus and the spectral theory of operators you will encounter next — the norm controls how analytic functions of operators (like eᵀ or (T − λI)⁻¹) behave.
