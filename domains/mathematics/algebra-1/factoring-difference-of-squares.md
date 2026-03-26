---
id: factoring-difference-of-squares
title: Factoring Difference of Squares
domain: mathematics
course: algebra-1
prerequisites:
  - id: multiplying-binomials-foil
    type: hard
  - id: square-roots-intro
    type: soft
builds-toward:
  - factoring-completely
  - solving-quadratics-by-factoring
tags: [factoring, difference-of-squares, special-products, polynomials]
stage: abstract-reasoning
status: validated
---

# Factoring Difference of Squares

## Core Idea
The difference of two perfect squares factors as a² − b² = (a + b)(a − b). This pattern comes from FOIL: (a + b)(a − b) = a² − ab + ab − b² = a² − b², where the middle terms cancel. For example, x² − 25 = (x + 5)(x − 5), and 4x² − 9 = (2x + 3)(2x − 3). This is one of the most recognizable and useful factoring patterns. It appears in simplifying rational expressions, solving equations, and even in mental math (e.g., 52 × 48 = (50 + 2)(50 − 2) = 2500 − 4 = 2496).

## How It's Best Learned
Start by having students FOIL (a + b)(a − b) to discover the pattern themselves. Then practice recognizing when an expression fits the pattern — both terms must be perfect squares separated by subtraction. Include expressions where a and b involve coefficients or higher powers (e.g., 16x⁴ − 1). Emphasize that a sum of squares (a² + b²) does not factor over the real numbers.

## Common Misconceptions
- Trying to factor a sum of squares (x² + 25 does not factor as (x + 5)(x + 5) — that gives x² + 10x + 25).
- Not recognizing perfect squares with coefficients (4x² is (2x)², 9y⁴ is (3y²)²).
- Stopping too early when the result can be factored further (x⁴ − 1 = (x² + 1)(x² − 1) = (x² + 1)(x + 1)(x − 1)).

## Questions

```yaml
- question: "A student claims that 4x² − 9 cannot be factored because 4 and 9 aren't 'simple' perfect squares. What is the correct factorization?"
  type: multiple-choice
  options:
    - "(2x − 3)(2x − 3)"
    - "(4x + 3)(4x − 3)"
    - "(2x + 3)(2x − 3)"
    - "4x² − 9 cannot be factored"
  answer: 2
  explanation: "4x² = (2x)² and 9 = 3², so a = 2x and b = 3, giving (2x + 3)(2x − 3). The key is recognizing that coefficients can be parts of perfect squares. Option A is (2x − 3)² = 4x² − 12x + 9 — a trinomial, not a difference of squares. Option B incorrectly uses 4x instead of 2x as the square root of 4x²."

- question: "Which represents the complete factorization of x⁴ − 1?"
  type: multiple-choice
  options:
    - "(x² + 1)(x² − 1)"
    - "(x + 1)²(x − 1)²"
    - "(x² + 1)(x + 1)(x − 1)"
    - "(x² − 1)(x² − 1)"
  answer: 2
  explanation: "x⁴ − 1 = (x²)² − 1² = (x² + 1)(x² − 1). The first factor is a sum of squares — it cannot be factored further over the reals. The second factor, x² − 1, is itself a difference of squares: (x + 1)(x − 1). Complete factorization means checking every factor for further factorability. Option A stops too early. Option B incorrectly treats (x² + 1) as (x + 1)²."

- question: "The expression x² + 49 can be factored as (x + 7)(x + 7)."
  type: true-false
  answer: false
  explanation: "(x + 7)(x + 7) = x² + 14x + 49, not x² + 49. A sum of squares cannot be factored over the real numbers at all — there is no pair of real binomials whose product eliminates all middle terms while producing a plus sign between the squared terms. The difference of squares pattern requires subtraction: x² − 49 = (x + 7)(x − 7)."

- question: "In the pattern a² − b² = (a + b)(a − b), the variable a should represent a single variable like x, not a compound expression like 3x or 2y³."
  type: true-false
  answer: false
  explanation: "a and b can represent any algebraic expression. In 9x² − 25, a = 3x and b = 5, giving (3x + 5)(3x − 5). In 4y⁶ − 1, a = 2y³ and b = 1. The pattern is fully general — 'a' and 'b' are placeholders for whatever expressions, when squared, produce the two terms of the difference."

- question: "Why does a² − b² factor into two binomials, but a² + b² cannot be factored over the real numbers?"
  type: short-answer
  answer: "The factorization a² − b² = (a + b)(a − b) works because FOIL produces outer term −ab and inner term +ab, which cancel completely, leaving a² − b². For a sum a² + b², any attempt to write it as (a + c)(a − c) changes the sign of the last term, and any attempt with same-sign factors produces a nonzero middle term that can't be eliminated. The cancellation of middle terms that makes the difference factorable requires one factor to have +b and the other −b — which forces the last terms to produce a difference, not a sum."
  explanation: "The mechanical reason is the cancellation of FOIL's outer and inner terms. Conceptually: factoring over the reals means finding two real expressions that multiply to give the original. For the middle terms to cancel, the two factors must have opposite signs for the b-term, which forces the squared terms to subtract. There is no escape from this constraint when you need a plus sign."
```

## Explainer

The **difference of squares** pattern is a direct reversal of the FOIL process you already know. When you multiply (a + b)(a − b) using FOIL, the outer term is −ab and the inner term is +ab — and those two middle terms cancel completely, leaving a² − b². Factoring a² − b² just runs this in reverse: you recognize that some expression is a perfect square minus another perfect square, and you split it into the two binomials whose middle terms will cancel.

The first skill is recognizing perfect squares. A **perfect square** is any expression you can write as something squared: 25 is 5², x² is x², 4x² is (2x)², 9y⁶ is (3y³)². When you see a two-term expression connected by subtraction, ask yourself: "Is each term a perfect square?" If yes, name the square roots — call them a and b — and write (a + b)(a − b). For x² − 16, we have a = x and b = 4, giving (x + 4)(x − 4). For 9x² − 25, we have a = 3x and b = 5, giving (3x + 5)(3x − 5). You can always verify by re-FOILing.

A crucial boundary: **a sum of squares does not factor** over the real numbers. The expression x² + 25 cannot be written as a product of two real binomials — try (x + 5)(x + 5) = x² + 10x + 25 (wrong), or (x + 5)(x − 5) = x² − 25 (also wrong). The cancellation of middle terms in FOIL requires one factor to have a plus and the other to have a minus, which produces a difference, not a sum. This is why the pattern is specifically called the "difference" of squares.

Finally, watch for **nested applications**: some expressions can be factored using the pattern more than once. Consider x⁴ − 1. This is (x²)² − 1² = (x² + 1)(x² − 1). The first factor is a sum of squares and cannot be factored further; the second factor, x² − 1, is itself a difference of squares: (x + 1)(x − 1). So the complete factorization is (x² + 1)(x + 1)(x − 1). Always check whether any factor you produce can be factored again — complete factoring means no factor can be broken down further.
