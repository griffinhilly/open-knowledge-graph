---
id: introduction-p-adic-numbers
title: Introduction to p-adic Numbers
domain: mathematics
course: number-theory
prerequisites:
- id: p-adic-valuation
  type: hard
- id: metric-spaces-definition
  type: soft
builds-toward:
- hensels-lemma
tags:
- p-adic-numbers
- metric-spaces
- completion
stage: advanced
status: draft
---

# Introduction to p-adic Numbers

## Core Idea
The p-adic numbers ℚ_p are the completion of ℚ under the p-adic metric d_p(x, y) = p^(-v_p(x-y)). They provide a 'p-adic topology' where convergence is based on divisibility by powers of p, enabling tools like Hensel lifting.

## Explainer

You already know the **p-adic valuation** v_p(n): it counts how many times the prime p divides an integer n. If n = 12 and p = 2, then v₂(12) = 2 because 12 = 4 × 3. The p-adic absolute value is defined as |x|_p = p^(−v_p(x)), with |0|_p = 0. This inverts our usual sense of size: numbers highly divisible by p are *small* in the p-adic world. In the 5-adic world, 125 = 5³ has absolute value 5⁻³ = 1/125 — it's tiny, not large.

The **p-adic metric** d_p(x, y) = |x − y|_p measures how close two numbers are by how divisible their difference is by p. Two integers are close if their difference is divisible by a high power of p. This is a legitimate metric, and it satisfies the much stronger **ultrametric inequality**: d_p(x, z) ≤ max(d_p(x, y), d_p(y, z)). This "non-Archimedean" property means the hypotenuse of a triangle is never longer than its longest side — a world very different from the geometry you're used to.

From your study of metric spaces, you know that every metric space can be completed by adding limits of Cauchy sequences. The reals ℝ are the completion of ℚ under the usual absolute value. **ℚ_p is the completion of ℚ under the p-adic absolute value.** Concretely, every element of ℚ_p can be written as a formal power series in p: a₀ + a₁p + a₂p² + a₃p³ + ⋯, where each coefficient aᵢ is an integer between 0 and p−1. This looks like a base-p expansion, but it extends infinitely to the left (toward higher powers of p) rather than to the right.

This representation reveals surprising facts. In ℚ₃, the number −1 equals 2 + 2·3 + 2·3² + 2·3³ + ⋯ — an infinite string of 2's in base 3. This is valid because the partial sums converge 3-adically: after n terms, the error is 3ⁿ, and |3ⁿ|₃ = 3⁻ⁿ → 0. There are infinitely many p-adic number systems, one for each prime, and **Ostrowski's theorem** says these — together with the usual absolute value — are the only ways to complete the rationals. The reals and all the p-adic fields together capture every possible notion of size on ℚ.
