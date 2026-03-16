---
id: radical-expressions-simplifying
title: Simplifying Radical Expressions
domain: mathematics
course: algebra-1
prerequisites:
- id: square-roots-intro
  type: hard
- id: exponent-rules-product-power-quotient
  type: soft
builds-toward:
- operations-with-radicals
- quadratic-formula
- segment-and-distance
tags:
- radicals
- simplifying
- square-roots
- perfect-squares
stage: abstract-reasoning
status: validated
---
# Simplifying Radical Expressions

## Core Idea
Simplifying a radical expression means rewriting it so that no perfect square factors remain under the radical sign. For example, sqrt(72) = sqrt(36 × 2) = 6sqrt(2). The key property is the product rule for radicals: sqrt(ab) = sqrt(a) × sqrt(b). To simplify, find the largest perfect square factor of the radicand, take its square root out of the radical, and leave the rest inside. This skill is necessary for simplifying answers to the quadratic formula, working with the distance formula, and performing operations with radicals.

## How It's Best Learned
Build a list of perfect squares (1, 4, 9, 16, 25, ..., 144, 169, ...) and practice identifying the largest perfect square factor. Use factor trees as an alternative: prime factorize the radicand, then pair up prime factors (each pair comes out as one factor). Practice with both numerical radicals and variable expressions (sqrt(x⁶) = x³). Include rationalizing the denominator as an extension.

## Common Misconceptions
- Not finding the largest perfect square factor (writing sqrt(72) = sqrt(4 × 18) = 2sqrt(18) and stopping, when sqrt(72) = 6sqrt(2)).
- Thinking sqrt(a + b) = sqrt(a) + sqrt(b) (this is false — the product rule works, the sum rule does not).
- Leaving perfect square factors under the radical.

## Explainer

From your work with square roots, you know that √36 = 6 because 6² = 36. The key insight behind simplifying radicals is that square roots and multiplication interact in a very clean way: **√(ab) = √a · √b**, provided a and b are nonnegative. This product rule is the only tool you need.

The strategy is to look at the number under the radical — the **radicand** — and find a perfect square hiding inside it. For example, 72 = 36 × 2, and 36 is a perfect square. So √72 = √(36 × 2) = √36 · √2 = 6√2. The trick is finding the *largest* perfect square factor, not just any perfect square factor. If you factor out 4 first, you get √72 = √(4 × 18) = 2√18, but √18 still has a perfect square hiding inside it (9 × 2), so you'd need another step. Working with the largest perfect square factor saves steps. This is why building fluency with perfect squares — 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144 — pays off immediately.

An alternative approach using your exponent rules: **prime factorize** the radicand and look for pairs of identical factors. For √72, prime factorize: 72 = 2 · 2 · 2 · 3 · 3. Each pair of identical factors comes out of the radical as one copy: the two 2s pair up to give one 2, the two 3s pair up to give one 3. The lone remaining 2 stays inside. Result: 2 · 3 · √2 = 6√2. This method connects directly to the exponent rule you know: √(x²) = x, because the square root "undoes" the square. More generally, √(x^(2k)) = x^k.

One warning that trips up many students: the product rule works for multiplication, but **not for addition**. √(a + b) ≠ √a + √b. You can check this with numbers: √(9 + 16) = √25 = 5, but √9 + √16 = 3 + 4 = 7. The two are different. This is one of the most common algebra errors, and it persists all the way into calculus — so getting clear on it now matters. The product rule is a genuine law of arithmetic; the "sum rule for radicals" is a fiction.
