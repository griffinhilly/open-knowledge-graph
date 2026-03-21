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
stage: advanced
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

## Questions

```yaml
- question: "You have built a degree-5 Newton interpolating polynomial through 6 data points. A 7th data point now arrives. What is the correct procedure?"
  type: multiple-choice
  options:
    - "Recompute the entire Lagrange basis from scratch with all 7 points"
    - "Rebuild the full divided difference table using all 7 points"
    - "Compute one new column in the divided difference table and append one new term to the polynomial"
    - "Solve a new 7×7 linear system to find updated polynomial coefficients"
  answer: 2
  explanation: "This is Newton's divided differences' key advantage over Lagrange: adding a new point requires only computing the new diagonal entry in the divided difference table (one new column of differences), then appending a single new term f[x₀,…,x₆](x−x₀)(x−x₁)…(x−x₅) to the polynomial. All previous terms — and all previous divided differences — remain unchanged. Lagrange interpolation (option A) requires completely rebuilding all basis polynomials Lᵢ(x). The Vandermonde approach (option D) requires solving a new linear system. Newton's form makes incremental data addition O(n) rather than O(n²)."

- question: "As two interpolation nodes x₀ and x₁ approach the same value (x₁ → x₀), what does the first-order divided difference f[x₀, x₁] = (f(x₁)−f(x₀))/(x₁−x₀) approach?"
  type: multiple-choice
  options:
    - "Zero, since the numerator and denominator both approach zero"
    - "Infinity, since dividing by a vanishing quantity is undefined"
    - "The derivative f′(x₀)"
    - "The second-order divided difference f[x₀, x₀, x₁]"
  answer: 2
  explanation: "The first-order divided difference is exactly the difference quotient from calculus: (f(x₁)−f(x₀))/(x₁−x₀). As x₁ → x₀, this is precisely the definition of the derivative f′(x₀). More generally, the kth-order divided difference f[x₀,…,xₖ] approaches f^(k)(x₀)/k! as all nodes collapse to x₀. This connection explains why divided differences are well-defined even for coincident nodes (via derivatives) and why Newton's form is more numerically stable than Lagrange near-coincident nodes — it is computing genuine approximations to derivatives."

- question: "Newton's divided difference formula and Lagrange interpolation produce different polynomials when applied to the same set of data points."
  type: true-false
  answer: false
  explanation: "Both methods produce exactly the same polynomial — the unique polynomial of degree ≤ n passing through n+1 given points. The uniqueness theorem for polynomial interpolation guarantees there is only one such polynomial. Newton's divided difference form and Lagrange's basis-polynomial form are two different representations of the same mathematical object, analogous to how the same number can be written as a fraction or a decimal. The difference is computational: Newton's form is easier to update incrementally and numerically more stable for near-coincident nodes."

- question: "When a new data point is added to a Newton interpolating polynomial, the coefficients of all previously computed terms remain unchanged."
  type: true-false
  answer: true
  explanation: "This is the defining feature of Newton's form. The polynomial P(x) = f[x₀] + f[x₀,x₁](x−x₀) + f[x₀,x₁,x₂](x−x₀)(x−x₁) + ⋯ is built incrementally: each term uses divided differences computed from x₀ through xₖ, and those differences do not change when a new point xₙ₊₁ is added. Only a new divided difference (one new column in the table) and one new term are computed. This stands in contrast to Lagrange, where every basis polynomial Lᵢ(x) depends on all nodes and must be recomputed when any node changes."

- question: "Why is Newton's divided difference form computationally superior to Lagrange interpolation when data arrives incrementally?"
  type: short-answer
  answer: "In Lagrange interpolation, each basis polynomial Lᵢ(x) is defined as a product over all n+1 nodes, so adding a new data point forces complete recomputation of all n+1 basis polynomials. Newton's form builds the polynomial incrementally: each coefficient is a divided difference computed from a triangular subtable, and existing coefficients are unchanged when a new point is added. Adding the (n+1)th point requires only computing one new column in the divided difference table and appending one new term to the polynomial — O(n) work instead of O(n²)."
  explanation: "This incremental property makes Newton's form the natural choice for applications where data arrives one point at a time: adaptive ODE solvers that add mesh points, interpolation in iterative algorithms, or real-time systems receiving sensor readings. It also explains why divided difference tables are organized diagonally — the diagonal is precisely the sequence of coefficients, built up one at a time."
```

## Explainer

From Lagrange interpolation, you know that given n+1 data points (x₀, f₀), …, (xₙ, fₙ), there is a unique polynomial of degree ≤ n passing through all of them. Lagrange writes it as a sum of basis polynomials Lᵢ(x), each of which is 1 at xᵢ and 0 at all other nodes. This representation is mathematically elegant but computationally awkward: if you receive one new data point and must add it to your interpolant, you have to recompute every Lagrange basis polynomial from scratch. Newton's **divided difference** form solves this by building the same polynomial in a nested, additive structure that makes adding points trivial.

The **zeroth-order divided difference** is just the function value: f[xᵢ] = f(xᵢ). The **first-order divided difference** is the slope of the secant line: f[xᵢ, xⱼ] = (f[xⱼ] − f[xᵢ])/(xⱼ − xᵢ). Higher-order divided differences are defined recursively: f[x₀, x₁, …, xₙ] = (f[x₁, …, xₙ] − f[x₀, …, xₙ₋₁])/(xₙ − x₀). You build a triangular table: the first column is function values, the second column is first-order differences of adjacent pairs, the third column is second-order differences, and so on. The diagonal entries — f[x₀], f[x₀, x₁], f[x₀, x₁, x₂], … — become the coefficients of the Newton interpolating polynomial.

The Newton form then reads: P(x) = f[x₀] + f[x₀, x₁](x − x₀) + f[x₀, x₁, x₂](x − x₀)(x − x₁) + ···. Each new term tacks on one more factor (x − xₖ) and one new divided difference coefficient, leaving all previous terms unchanged. This is the crucial advantage over Lagrange: to add a new data point xₙ₊₁, simply compute one new column in the divided difference table and append one new term to the polynomial. No recomputation needed. Think of it as building the polynomial incrementally, the way you might fit a line first, then bend it to pass through a third point, then a fourth, each time adjusting the curve only as much as needed.

The connection to calculus is real: if all nodes collapse to a single point x₀, the kth-order divided difference approaches f^(k)(x₀)/k! — the Taylor coefficient. Divided differences are the finite-difference analogue of derivatives, well-defined even when the nodes are distinct. This analogy also explains why Newton's form is more numerically stable for near-coincident nodes: you are computing genuine approximations to derivatives rather than inverting a Vandermonde matrix, which becomes ill-conditioned when nodes are close together. In practice, Newton's divided differences are the foundation of adaptive interpolation algorithms, ODE solvers that add new mesh points on the fly, and any setting where data arrives incrementally.
