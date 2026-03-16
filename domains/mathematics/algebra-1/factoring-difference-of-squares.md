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

## Explainer

The **difference of squares** pattern is a direct reversal of the FOIL process you already know. When you multiply (a + b)(a − b) using FOIL, the outer term is −ab and the inner term is +ab — and those two middle terms cancel completely, leaving a² − b². Factoring a² − b² just runs this in reverse: you recognize that some expression is a perfect square minus another perfect square, and you split it into the two binomials whose middle terms will cancel.

The first skill is recognizing perfect squares. A **perfect square** is any expression you can write as something squared: 25 is 5², x² is x², 4x² is (2x)², 9y⁶ is (3y³)². When you see a two-term expression connected by subtraction, ask yourself: "Is each term a perfect square?" If yes, name the square roots — call them a and b — and write (a + b)(a − b). For x² − 16, we have a = x and b = 4, giving (x + 4)(x − 4). For 9x² − 25, we have a = 3x and b = 5, giving (3x + 5)(3x − 5). You can always verify by re-FOILing.

A crucial boundary: **a sum of squares does not factor** over the real numbers. The expression x² + 25 cannot be written as a product of two real binomials — try (x + 5)(x + 5) = x² + 10x + 25 (wrong), or (x + 5)(x − 5) = x² − 25 (also wrong). The cancellation of middle terms in FOIL requires one factor to have a plus and the other to have a minus, which produces a difference, not a sum. This is why the pattern is specifically called the "difference" of squares.

Finally, watch for **nested applications**: some expressions can be factored using the pattern more than once. Consider x⁴ − 1. This is (x²)² − 1² = (x² + 1)(x² − 1). The first factor is a sum of squares and cannot be factored further; the second factor, x² − 1, is itself a difference of squares: (x + 1)(x − 1). So the complete factorization is (x² + 1)(x + 1)(x − 1). Always check whether any factor you produce can be factored again — complete factoring means no factor can be broken down further.
