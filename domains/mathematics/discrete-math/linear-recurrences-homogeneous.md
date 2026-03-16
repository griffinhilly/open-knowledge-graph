---
id: linear-recurrences-homogeneous
title: Solving Linear Recurrence Relations
domain: mathematics
course: discrete-math
prerequisites:
- id: recurrence-relations-discrete
  type: hard
- id: characteristic-polynomial
  type: soft
builds-toward:
- generating-functions-basics
tags:
- linear-recurrences
- characteristic-equation
- closed-form
stage: formal-systems
status: draft
---

# Solving Linear Recurrence Relations

## Core Idea
Linear homogeneous recurrences like aₙ = c₁aₙ₋₁ + c₂aₙ₋₂ + ... + cₖaₙ₋ₖ have closed-form solutions via the characteristic equation rᵏ − c₁rᵏ⁻¹ − ... − cₖ = 0. The roots determine the general form; initial conditions pin down constants.

## How It's Best Learned
Solve Fibonacci step-by-step: characteristic equation r² = r + 1 gives roots (1±√5)/2; express aₙ as a linear combination scaled by these roots. Verify by computing initial terms.

## Common Misconceptions
The characteristic equation is rᵏ = c₁rᵏ⁻¹ + ... + cₖ, not rᵏ⁻¹ etc. Repeated roots require adjusted forms (terms multiplied by n).

## Explainer

You already know from recurrence relations that a sequence can be defined by a rule connecting each term to earlier ones. The challenge is converting that recursive rule into a direct formula — one that gives you the 100th term without computing the first 99. For **linear homogeneous recurrences**, there is a systematic method that works every time, and it reduces the problem to polynomial algebra you already know.

The key insight is to guess that solutions look like powers: try aₙ = rⁿ for some constant r. Substitute into the recurrence aₙ = c₁aₙ₋₁ + c₂aₙ₋₂ to get rⁿ = c₁rⁿ⁻¹ + c₂rⁿ⁻². Dividing through by rⁿ⁻² gives r² = c₁r + c₂, the **characteristic equation**. This is the polynomial whose roots tell you what exponentials appear in the solution. If the roots r₁ and r₂ are distinct, the general solution is aₙ = Ar₁ⁿ + Br₂ⁿ for constants A and B determined by initial conditions.

The Fibonacci sequence, defined by Fₙ = Fₙ₋₁ + Fₙ₋₂ with F₀ = 0, F₁ = 1, is the standard worked example. The characteristic equation r² = r + 1 has roots φ = (1 + √5)/2 ≈ 1.618 (the golden ratio) and ψ = (1 − √5)/2 ≈ −0.618. So Fₙ = Aφⁿ + Bψⁿ. Plugging in F₀ = 0 and F₁ = 1 gives A = 1/√5 and B = −1/√5, yielding the closed-form **Binet's formula**: Fₙ = (φⁿ − ψⁿ)/√5. Despite containing irrational numbers, this formula always produces integers — a remarkable consequence of the algebra.

The method extends gracefully to higher-order recurrences (more previous terms) and to **repeated roots**. If the characteristic equation has a root r of multiplicity m, then the solution includes terms rⁿ, n·rⁿ, n²·rⁿ, …, nᵐ⁻¹·rⁿ — each power of n attached to the same exponential base. The initial conditions still uniquely determine all constants. The connection to your prerequisite on characteristic polynomials is direct: the characteristic polynomial of a recurrence plays exactly the same structural role as the characteristic polynomial of a matrix, and both encode the same idea — find the exponential rates at which the system grows or decays.
