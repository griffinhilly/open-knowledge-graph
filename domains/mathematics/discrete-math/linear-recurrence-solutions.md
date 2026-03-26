---
id: linear-recurrence-solutions
title: Solving Linear Recurrence Relations via Characteristic Equations
domain: mathematics
course: discrete-math
prerequisites:
- id: recurrence-relations
  type: hard
builds-toward:
- nonhomogeneous-recurrence-solutions
tags:
- recurrence-relations
- characteristic-equations
stage: formal-systems
status: validated
---

# Solving Linear Recurrence Relations via Characteristic Equations

## Core Idea
For homogeneous linear recurrences a(n) = c₁a(n-1) + ⋯ + cₖa(n-k), the characteristic equation is xᵏ - c₁xᵏ⁻¹ - ⋯ - cₖ = 0. The general solution is a linear combination of terms r^n where r are roots of the characteristic equation. Repeated roots yield polynomial factors in the solution.

## Questions

```yaml
- question: "The recurrence a(n) = 5a(n−1) − 6a(n−2) has which characteristic equation?"
  type: multiple-choice
  options:
    - "x² = 5x − 6"
    - "x² − 5x + 6 = 0"
    - "x² + 5x − 6 = 0"
    - "5x² − x − 6 = 0"
  answer: 1
  explanation: "Substitute a(n) = r^n into the recurrence: r^n = 5r^(n−1) − 6r^(n−2). Divide by r^(n−2) to get r² = 5r − 6, then rearrange: r² − 5r + 6 = 0. The characteristic polynomial is built by moving all terms to one side, with the coefficient of a(n) term (1) on the leading power and the coefficients of a(n−k) terms contributing with alternating sign. Option A is the equation before rearranging — it's equivalent but not in standard polynomial form. Options C and D have sign errors."

- question: "The characteristic equation of a recurrence has r = 3 as a root of multiplicity 2. What is the general solution contributed by this root?"
  type: multiple-choice
  options:
    - "A · 3^n"
    - "A · 3^n + B · 3^n"
    - "A · 3^n + B · n · 3^n"
    - "A · n · 3^n + B · n² · 3^n"
  answer: 2
  explanation: "A root r of multiplicity m contributes m linearly independent solution terms: r^n, n·r^n, n²·r^n, …, n^(m−1)·r^n. For r = 3 with multiplicity 2, the two independent solutions are 3^n and n·3^n, so the general contribution is A·3^n + B·n·3^n. Option A only has one term — not enough free constants for multiplicity 2. Option B looks like two terms but A·3^n + B·3^n = (A+B)·3^n, which is really just one free constant. Option D skips the plain 3^n term entirely."

- question: "The general solution to a second-order homogeneous linear recurrence always requires exactly two free constants determined by initial conditions."
  type: true-false
  answer: true
  explanation: "The set of all solutions to a k-th order homogeneous linear recurrence forms a k-dimensional vector space. For k = 2, this means any solution is a linear combination of exactly 2 linearly independent basis solutions, giving 2 free constants. The initial conditions a(0) and a(1) provide 2 equations that uniquely determine those constants — no more, no less. This parallels second-order linear ODEs, which also have 2-dimensional solution spaces."

- question: "If r = 2 is a repeated root of multiplicity 3, the general solution contribution from this root is A·2^n + B·n·2^n."
  type: true-false
  answer: false
  explanation: "A root of multiplicity 3 requires three independent terms: 2^n, n·2^n, and n²·2^n. The general contribution is A·2^n + B·n·2^n + C·n²·2^n, with three free constants. Only including two terms would give a 2-dimensional subspace when the root contributes a 3-dimensional one — the solution would miss an entire family of valid sequences, and the constants determined by initial conditions would generally be wrong."

- question: "Why does guessing a(n) = r^n lead to a useful solution method for homogeneous linear recurrences?"
  type: short-answer
  answer: "Because substituting r^n into a linear recurrence with constant coefficients converts it from a functional equation over sequences to a polynomial equation in r. Dividing out a common factor of r^(n−k) leaves a polynomial whose roots are exactly the values of r that make a(n) = r^n a valid solution. Since the recurrence is linear, any linear combination of valid solutions is also valid, so the roots of the characteristic polynomial generate a full basis for the solution space."
  explanation: "The key leverage is that r^n is an 'eigenfunction' of the shift operator — multiplying n by a constant shifts the sequence by a fixed ratio. This makes the coefficient structure of the recurrence become multiplicative in r rather than recursive in n, collapsing an infinite-dimensional recurrence to a finite-degree polynomial. This is the same reason exponentials are eigenfunctions of linear ODEs with constant coefficients."
```

## Explainer

You already know what a recurrence relation is — a rule that defines each term of a sequence in terms of earlier terms. The Fibonacci sequence is the classic example: F(n) = F(n−1) + F(n−2). The challenge is going from this recursive rule to an explicit **closed-form formula** — an expression that gives F(n) directly, without computing all previous terms. The **characteristic equation** method provides this.

The key insight is to guess that the solution has the form a(n) = r^n for some constant r, then determine which values of r work. Substituting into F(n) = F(n−1) + F(n−2) gives r^n = r^(n−1) + r^(n−2). Dividing through by r^(n−2) yields r² = r + 1, or equivalently r² − r − 1 = 0. This is the **characteristic equation** of the recurrence. Solving gives r = (1 ± √5)/2 — the golden ratio φ and its conjugate ψ. Because the recurrence is linear, any linear combination of valid solutions is also a solution, so the general solution is F(n) = Aφ^n + Bψ^n, where the constants A and B are determined by the initial conditions F(0) = 0 and F(1) = 1.

For a k-th order linear recurrence a(n) = c₁a(n−1) + ⋯ + cₖa(n−k), the **characteristic polynomial** is x^k − c₁x^(k−1) − ⋯ − cₖ = 0. If it has k distinct roots r₁, r₂, …, rₖ, the general solution is a(n) = A₁r₁^n + A₂r₂^n + ⋯ + Aₖrₖ^n. The k initial conditions a(0), a(1), …, a(k−1) give you k equations to solve for A₁, …, Aₖ — a linear system you can solve by substitution or matrix methods.

**Repeated roots** require a modification. If r is a root of multiplicity m, then r^n, n·r^n, n²·r^n, …, n^(m−1)·r^n are all linearly independent solutions that must be included in the general solution. This parallels the treatment of repeated roots in differential equations, and for the same reason: both involve solving linear equations over a space of exponential-type basis functions. The underlying reason this all works is that the set of all solutions to a homogeneous k-th order linear recurrence forms a k-dimensional vector space, and the characteristic root terms (with polynomial factors for repeated roots) form a basis for that space.
