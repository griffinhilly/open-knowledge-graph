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

## Questions

```yaml
- question: "Using the summation identity F₁ + F₂ + ... + Fₙ = Fₙ₊₂ − 1, what is F₁ + F₂ + F₃ + F₄ + F₅? (Recall: F₁=1, F₂=1, F₃=2, F₄=3, F₅=5, F₆=8, F₇=13)"
  type: multiple-choice
  options:
    - "11"
    - "12"
    - "13"
    - "14"
  answer: 1
  explanation: "By the identity, F₁+...+F₅ = F₇ − 1 = 13 − 1 = 12. You can verify directly: 1+1+2+3+5 = 12. The identity converts a five-term sum into a single lookup, which is precisely why these identities are useful — they compress calculation."

- question: "Cassini's identity Fₙ₋₁Fₙ₊₁ − Fₙ² = (−1)ⁿ is most elegantly derived from which perspective?"
  type: multiple-choice
  options:
    - "Direct computation for several values of n followed by strong induction"
    - "Applying the Binet closed-form formula twice and simplifying"
    - "Recognizing that det(Mⁿ) = (det M)ⁿ = (−1)ⁿ, where Mⁿ encodes Fibonacci numbers as entries"
    - "Counting tiling arrangements of a strip of length n−1"
  answer: 2
  explanation: "The matrix M = [[1,1],[1,0]] has the property that Mⁿ = [[Fₙ₊₁, Fₙ],[Fₙ, Fₙ₋₁]]. The determinant of Mⁿ is (det M)ⁿ = (−1)ⁿ. Reading the determinant of the right-hand matrix directly gives Fₙ₊₁Fₙ₋₁ − Fₙ², so Cassini's identity follows immediately. This approach is most elegant because it reveals the identity as a consequence of matrix structure rather than a numerical curiosity."

- question: "The general addition formula Fₘ₊ₙ = FₘFₙ₊₁ + Fₘ₋₁Fₙ reduces to the basic Fibonacci recurrence when m = 1."
  type: true-false
  answer: true
  explanation: "Setting m = 1: F₁₊ₙ = F₁Fₙ₊₁ + F₀Fₙ. Since F₁ = 1 and F₀ = 0 (by convention), this gives Fₙ₊₁ = Fₙ₊₁, which is trivially the recurrence. More usefully, setting m = 2 gives F₂₊ₙ = F₂Fₙ₊₁ + F₁Fₙ = Fₙ₊₁ + Fₙ = Fₙ₊₂, which is exactly the definition. The general formula truly generalizes the recurrence."

- question: "Cassini's identity shows that for any n, the product Fₙ₋₁Fₙ₊₁ equals Fₙ² exactly — consecutive Fibonacci numbers are perfectly correlated."
  type: true-false
  answer: false
  explanation: "Cassini's identity states Fₙ₋₁Fₙ₊₁ − Fₙ² = (−1)ⁿ, which means the difference alternates between +1 and −1 — never zero. The flanking product is always exactly 1 away from the square, not equal to it. This near-miss is what makes the identity surprising and beautiful."

- question: "Why is the matrix M = [[1,1],[1,0]] particularly powerful for deriving Fibonacci identities, rather than just using induction directly?"
  type: short-answer
  answer: "Because Mⁿ encodes Fibonacci numbers as entries in a structured way, so identities about Fibonacci numbers become statements about matrix operations. Multiplying Mᵐ × Mⁿ = Mᵐ⁺ⁿ instantly yields the addition formula by reading off entries; taking the determinant of Mⁿ instantly yields Cassini's identity. The matrix framework generates many identities simultaneously from a single algebraic fact, rather than requiring a separate inductive proof for each."
  explanation: "Induction proves identities one at a time and requires guessing the right form in advance. The matrix approach provides a unified generating structure: since Mⁿ has a known form with Fibonacci entries, any algebraic property of matrices (determinant, trace, multiplication) automatically produces a Fibonacci identity. This is the deeper structural insight — the sequence is not just a list of numbers but the shadow of matrix exponentiation."
```

## Explainer

You already know the Fibonacci sequence: F₁ = 1, F₂ = 1, and Fₙ = Fₙ₋₁ + Fₙ₋₂ for every subsequent term. What Fibonacci identities reveal is that this simple recurrence generates a surprisingly rich web of algebraic relationships — the sequence is not just a list of numbers, but a structured object with deep internal symmetry.

The most accessible identity is the summation formula: F₁ + F₂ + ⋯ + Fₙ = Fₙ₊₂ − 1. This is a perfect case for **mathematical induction**, your prerequisite tool. The base case n = 1 gives F₁ = 1 = F₃ − 1 = 2 − 1 ✓. For the inductive step, add Fₙ₊₁ to both sides of the assumed identity: F₁ + ⋯ + Fₙ₊₁ = Fₙ₊₂ − 1 + Fₙ₊₁ = Fₙ₊₃ − 1 (using the recurrence). Induction is the right tool here because the Fibonacci recurrence itself is inductive — the identity is essentially a cumulative consequence of applying the definition repeatedly.

More surprising is **Cassini's identity**: Fₙ₋₁Fₙ₊₁ − Fₙ² = (−1)ⁿ. The product of two Fibonacci numbers flanking Fₙ differs from Fₙ² by exactly 1, alternating sign. This can be proven by induction, but it also emerges naturally from a **matrix representation**. Define the matrix M = [[1,1],[1,0]]. A remarkable fact is that Mⁿ = [[Fₙ₊₁, Fₙ],[Fₙ, Fₙ₋₁]]. Since det(Mⁿ) = (det M)ⁿ = (−1)ⁿ, and the determinant of the matrix on the right is Fₙ₊₁Fₙ₋₁ − Fₙ², Cassini's identity follows immediately. The matrix viewpoint unifies many identities at once.

The general addition formula Fₘ₊ₙ = FₘFₙ₊₁ + Fₘ₋₁Fₙ also follows from the matrix approach: multiply Mᵐ and Mⁿ and read off the top-left entry. This identity generalizes the recurrence (which is the case m = 1) and has a beautiful combinatorial interpretation: it counts the number of ways to tile a (m+n−1)-length board with squares and dominoes, split at position m. Fibonacci identities thus form a landscape where algebra, induction, linear algebra, and combinatorics all converge — each method illuminates a different facet of the same underlying structure.
