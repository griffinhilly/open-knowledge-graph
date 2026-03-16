---
id: fibonacci-identities
title: Fibonacci Identities and Relations
domain: mathematics
course: discrete-math
prerequisites:
- id: fibonacci-sequence-properties
  type: hard
- id: mathematical-induction-intro
  type: soft
tags:
- sequences
- identities
- fibonacci
stage: formal-systems
status: draft
---

# Fibonacci Identities and Relations

## Core Idea
Fibonacci numbers satisfy numerous identities: Fₘ₊ₙ = FₘFₙ₊₁ + Fₘ₋₁Fₙ, F₁+F₂+...+Fₙ = Fₙ₊₂-1, and others. These identities reveal the deep structure of the sequence and are proven using induction, the Binet formula, or combinatorial arguments.

## Explainer

You already know the Fibonacci sequence: F₁ = 1, F₂ = 1, and Fₙ = Fₙ₋₁ + Fₙ₋₂ for every subsequent term. What Fibonacci identities reveal is that this simple recurrence generates a surprisingly rich web of algebraic relationships — the sequence is not just a list of numbers, but a structured object with deep internal symmetry.

The most accessible identity is the summation formula: F₁ + F₂ + ⋯ + Fₙ = Fₙ₊₂ − 1. This is a perfect case for **mathematical induction**, your prerequisite tool. The base case n = 1 gives F₁ = 1 = F₃ − 1 = 2 − 1 ✓. For the inductive step, add Fₙ₊₁ to both sides of the assumed identity: F₁ + ⋯ + Fₙ₊₁ = Fₙ₊₂ − 1 + Fₙ₊₁ = Fₙ₊₃ − 1 (using the recurrence). Induction is the right tool here because the Fibonacci recurrence itself is inductive — the identity is essentially a cumulative consequence of applying the definition repeatedly.

More surprising is **Cassini's identity**: Fₙ₋₁Fₙ₊₁ − Fₙ² = (−1)ⁿ. The product of two Fibonacci numbers flanking Fₙ differs from Fₙ² by exactly 1, alternating sign. This can be proven by induction, but it also emerges naturally from a **matrix representation**. Define the matrix M = [[1,1],[1,0]]. A remarkable fact is that Mⁿ = [[Fₙ₊₁, Fₙ],[Fₙ, Fₙ₋₁]]. Since det(Mⁿ) = (det M)ⁿ = (−1)ⁿ, and the determinant of the matrix on the right is Fₙ₊₁Fₙ₋₁ − Fₙ², Cassini's identity follows immediately. The matrix viewpoint unifies many identities at once.

The general addition formula Fₘ₊ₙ = FₘFₙ₊₁ + Fₘ₋₁Fₙ also follows from the matrix approach: multiply Mᵐ and Mⁿ and read off the top-left entry. This identity generalizes the recurrence (which is the case m = 1) and has a beautiful combinatorial interpretation: it counts the number of ways to tile a (m+n−1)-length board with squares and dominoes, split at position m. Fibonacci identities thus form a landscape where algebra, induction, linear algebra, and combinatorics all converge — each method illuminates a different facet of the same underlying structure.
