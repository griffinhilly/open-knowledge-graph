---
id: lagrange-polynomial-interpolation
title: Lagrange Polynomial Interpolation
domain: mathematics
course: numerical-analysis
prerequisites:
- id: polynomial-rings
  type: soft
builds-toward:
- newton-divided-differences
- interpolation-error-analysis
tags:
- interpolation
- polynomials
- lagrange
stage: formal-systems
status: validated
---

# Lagrange Polynomial Interpolation

## Core Idea
Given n+1 distinct points (x_i, y_i), Lagrange interpolation constructs the unique polynomial of degree ≤n passing through all points using L_i(x) = ∏_{j≠i} (x - x_j)/(x_i - x_j). The Lagrange form P(x) = Σ y_i L_i(x) is elegant and explicit but becomes numerically unstable when adding new points since all basis functions must be recomputed.

## Explainer

The interpolation problem is fundamental: given n+1 data points (x₀, y₀), (x₁, y₁), ..., (xₙ, yₙ) with distinct x-values, find a polynomial P(x) of degree at most n that passes through all of them. A uniqueness theorem guarantees that exactly one such polynomial exists — if two polynomials of degree ≤ n agree at n+1 points, their difference has n+1 roots but degree at most n, which forces it to be identically zero. The Lagrange construction gives an explicit formula for this unique polynomial.

The idea is to build **basis polynomials** L₀(x), L₁(x), ..., Lₙ(x), each of degree n, with a remarkable property: L_i(x_j) = 1 when j = i and L_i(x_j) = 0 when j ≠ i. Each basis polynomial "selects" exactly one data point and ignores the others. The formula is L_i(x) = ∏_{j≠i} (x − x_j) / (x_i − x_j). The numerator product ensures L_i vanishes at every node except x_i (each factor x − x_j is zero when x = x_j). The denominator normalizes the result so that L_i(x_i) = 1. Once you have these basis polynomials, the interpolant is simply P(x) = Σᵢ yᵢ L_i(x) — at any node x_k, every term vanishes except y_k · L_k(x_k) = y_k, confirming the polynomial passes through every data point.

The Lagrange form is mathematically elegant and invaluable for theoretical analysis — for instance, it makes the interpolation error formula transparent. However, it has a practical limitation: if you add a new data point (xₙ₊₁, yₙ₊₁), every basis polynomial must be recomputed from scratch because each L_i depends on all the nodes. The new factor (x − xₙ₊₁) must be inserted into every numerator, and every denominator must be updated. This makes incremental updates expensive, costing O(n²) work.

Newton's divided-difference form addresses this limitation by writing the same unique polynomial in a different basis — one where adding a new point requires computing just one new coefficient and appending one new term. The two forms represent the same polynomial (since it is unique) but are suited to different tasks: Lagrange for theory and closed-form expressions, Newton for computation and incremental updates. Understanding both forms, and why they must agree, deepens your grasp of polynomial interpolation as a whole and prepares you for the error analysis that governs when interpolation can be trusted and when it breaks down (as in Runge's phenomenon).

## Questions

```yaml
- question: "You have 5 distinct data points. What is the maximum degree of the Lagrange interpolating polynomial that passes through all of them?"
  type: multiple-choice
  options:
    - "5"
    - "4"
    - "3"
    - "It depends on whether the y-values are linearly independent"
  answer: 1
  explanation: "Given n+1 distinct points, the unique interpolating polynomial has degree *at most* n. With 5 points, n+1 = 5 so n = 4, and the polynomial has degree at most 4. It may be lower if the points happen to lie on a lower-degree polynomial. A common error is confusing the number of points (5) with the degree (at most 4)."

- question: "What is the defining property of the Lagrange basis polynomial L_i(x)?"
  type: multiple-choice
  options:
    - "L_i(x_i) = 0 for every interpolation node x_i"
    - "L_i(x_j) = 1 for all nodes x_j in the data set"
    - "L_i(x_j) = 0 for j ≠ i and L_i(x_i) = 1"
    - "L_i(x) is the derivative of the interpolating polynomial at x_i"
  answer: 2
  explanation: "L_i(x) is constructed to equal 1 at node x_i and 0 at all other nodes x_j (j ≠ i). This property is what makes P(x) = Σ y_i L_i(x) work: at any node x_k, every term vanishes except y_k · L_k(x_k) = y_k · 1 = y_k, confirming the polynomial passes through all data points. The numerator product ∏_{j≠i}(x − x_j) gives zeros at all other nodes; dividing by ∏_{j≠i}(x_i − x_j) normalizes it to 1 at x_i."

- question: "Given n+1 distinct data points, there exists exactly one polynomial of degree ≤ n that passes through all of them."
  type: true-false
  answer: true
  explanation: "This is the uniqueness theorem for polynomial interpolation. Existence is provided by the Lagrange (or Newton) construction. Uniqueness follows because if two polynomials of degree ≤ n agree at n+1 points, their difference is a polynomial of degree ≤ n with n+1 roots, which forces it to be identically zero."

- question: "The Lagrange basis polynomial L_i(x) equals 1 at every interpolation node x_j in the data set."
  type: true-false
  answer: false
  explanation: "L_i(x) equals 1 *only* at x_i and equals 0 at all other nodes x_j (j ≠ i). This selective property — being 1 at exactly one node and 0 at all others — is precisely what allows the Lagrange sum P(x) = Σ y_i L_i(x) to reproduce the correct y-value at every data point."

- question: "Why does the Lagrange form become computationally inconvenient when a new data point is added to an existing interpolation set?"
  type: short-answer
  answer: "Each Lagrange basis polynomial L_i(x) = ∏_{j≠i} (x − x_j)/(x_i − x_j) depends on all n+1 interpolation nodes. When a new node x_{n+1} is added, every existing basis polynomial must be updated because its numerator product must now include the new factor (x − x_{n+1}), and its denominator must include (x_i − x_{n+1}). All n+1 existing basis functions must be completely recomputed, making updates cost O(n²) rather than incremental."
  explanation: "This contrasts with Newton's divided-difference form, where adding a new point requires only one new divided difference and appending one new term. The Lagrange form is mathematically elegant and useful for theoretical analysis, but Newton's form is preferred when incremental updates are needed."
```
