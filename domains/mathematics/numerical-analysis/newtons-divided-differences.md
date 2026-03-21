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

## Questions

```yaml
- question: "After building a divided difference table for 5 data points, you discover a 6th point must be included. Comparing Newton's divided difference form to Lagrange form, which statement is correct?"
  type: multiple-choice
  options:
    - "Lagrange is more efficient because its basis polynomials are orthogonal"
    - "Newton requires only extending the table with one new diagonal; all previous entries are unchanged"
    - "Both require the same work — the interpolating polynomial must be fully reconstructed from scratch in either case"
    - "Newton requires recomputing all divided differences because each entry depends on every node"
  answer: 1
  explanation: "The central advantage of Newton's form is incremental updating. The divided difference table entries f[x₀], f[x₀,x₁], f[x₀,x₁,x₂], … depend only on the nodes in their argument, so they are unchanged when a new node is appended. Only the new diagonal entries involving x₅ must be computed. In Lagrange form, every basis polynomial Lᵢ(x) involves a product over all nodes, so adding one point forces complete reconstruction of all n+1 basis polynomials."

- question: "A divided difference f[x₀, x₁, x₂] is best described as:"
  type: multiple-choice
  options:
    - "The average rate of change of f over the interval [x₀, x₂]"
    - "A coefficient defined only when x₀ < x₁ < x₂ are equally spaced"
    - "A recursive generalized slope computed from lower-order divided differences"
    - "The second derivative of f evaluated at the midpoint of [x₀, x₂]"
  answer: 2
  explanation: "Divided differences are defined recursively: f[xᵢ,xᵢ₊₁] = (f(xᵢ₊₁)−f(xᵢ))/(xᵢ₊₁−xᵢ), and f[x₀,…,xₖ] = (f[x₁,…,xₖ]−f[x₀,…,xₖ₋₁])/(xₖ−x₀). They generalize the notion of slope to higher orders and unequal spacing. Option A confuses divided differences with a simple average slope. Option D is approximately true for equally-spaced nodes (f[x₀,x₁,x₂] ≈ f''(ξ)/2!), but this is a consequence, not the definition."

- question: "Reordering the data points before computing Newton's divided differences produces a different interpolating polynomial."
  type: true-false
  answer: false
  explanation: "Divided differences are symmetric in their arguments — f[x₀,x₁,x₂] = f[x₂,x₀,x₁] = f[x₁,x₂,x₀], etc. The coefficients a₀, a₁, a₂, … will differ depending on the chosen ordering (since the first coefficient is always f[x₀], which changes), but the resulting polynomial evaluates to the same values at all nodes and is therefore the same polynomial. Uniqueness of the interpolating polynomial guarantees this."

- question: "Newton's divided difference form is superior to Lagrange interpolation because it produces a more accurate polynomial approximation of the underlying function."
  type: true-false
  answer: false
  explanation: "Both forms produce the exact same interpolating polynomial — there is a unique polynomial of degree ≤ n passing through n+1 distinct points. Newton's form is not more accurate; its advantage is purely computational: (1) adding new data points requires only extending the divided difference table, not a full recomputation, and (2) the nested (Horner's) form evaluates the polynomial in O(n) multiplications rather than O(n²)."

- question: "Why does adding a new data point require much less computational work in Newton's divided difference form than in Lagrange form?"
  type: short-answer
  answer: "In Newton's form, coefficients are computed recursively from existing table entries, and a new point only requires computing one new diagonal in the table — all prior entries are unchanged. In Lagrange form, every basis polynomial Lᵢ(x) is defined as a product involving all nodes, so adding one node requires rebuilding all basis polynomials from scratch."
  explanation: "This incremental property is the core practical motivation for Newton's form in numerical software. Divided differences depend only on the nodes in their argument, making the table modular. The Lagrange basis polynomials, by contrast, are global — each one changes whenever any node changes. For applications that progressively add data (adaptive sampling, real-time interpolation), this difference in update cost is decisive."
```

## Explainer

From Lagrange interpolation you know that through any n+1 distinct points there is a unique polynomial of degree at most n. The Lagrange form constructs it as a sum of basis polynomials Lᵢ(x), each equal to 1 at xᵢ and 0 at all other nodes. That form is elegant but computationally awkward: if you add a new data point, you must recompute every basis polynomial from scratch. Newton's divided difference form solves this by building the polynomial incrementally.

The idea is to write the interpolating polynomial in **Newton's nested (forward difference) form**: p(x) = f[x₀] + f[x₀,x₁](x-x₀) + f[x₀,x₁,x₂](x-x₀)(x-x₁) + ... where f[x₀, x₁, …, xₖ] is a **divided difference** — a generalized slope. The zeroth-order divided difference is just the function value: f[xᵢ] = f(xᵢ). The first-order divided difference is the ordinary slope: f[xᵢ, xᵢ₊₁] = (f(xᵢ₊₁) - f(xᵢ))/(xᵢ₊₁ - xᵢ). Higher-order divided differences are defined recursively: f[x₀,…,xₖ] = (f[x₁,…,xₖ] - f[x₀,…,xₖ₋₁]) / (xₖ - x₀). The pattern fills a triangular table, and the top diagonal gives the coefficients a₀, a₁, a₂, … directly.

The computational payoff is **incremental updating**. Once you have the divided difference table for n+1 points, adding a new point (x_{n+1}, f(x_{n+1})) only requires extending the table with one new diagonal — previous entries are unchanged. Compare this to Lagrange form, where every basis polynomial must be rebuilt. Newton's form also evaluates efficiently via **Horner's method**: p(x) = a₀ + (x-x₀)(a₁ + (x-x₁)(a₂ + …)), reducing the number of multiplications from O(n²) to O(n).

A subtle but important fact: divided differences are **symmetric** in their arguments, meaning f[x₀, x₁, x₂] = f[x₂, x₀, x₁] = ... regardless of the order. This symmetry reveals that the divided difference f[x₀,…,xₙ] equals f⁽ⁿ⁾(ξ)/n! for some ξ in the interval spanned by the nodes — a direct connection to Taylor coefficients when the nodes collapse to a single point. This link between divided differences and derivatives is what makes Newton's form the natural foundation for the interpolation error analysis you will study next.
