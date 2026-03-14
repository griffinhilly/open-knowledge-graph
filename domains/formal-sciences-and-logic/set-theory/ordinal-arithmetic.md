---
id: ordinal-arithmetic
title: Ordinal Arithmetic
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: ordinal-numbers-and-order
  type: hard
builds-toward:
- aleph-numbers
tags:
- ordinal arithmetic
- ordinal addition
- ordinal multiplication
- ordinal exponentiation
- non-commutativity
- Cantor normal form
stage: formal-systems
status: draft
---

# Ordinal Arithmetic

## Core Idea
Ordinal addition, multiplication, and exponentiation extend the corresponding finite operations into the transfinite, but with a critical difference: they are not commutative. Addition α + β is defined by concatenating the well-orderings of α and β (placing β after α); multiplication α · β by replacing each element of β with a copy of α; exponentiation α^β by transfinite recursion. The failure of commutativity is dramatic: 1 + ω = ω (the single element is absorbed into the limit), but ω + 1 > ω. Every ordinal has a unique Cantor normal form as a finite decreasing sum of powers of ω, analogous to base-ω representation.

## How It's Best Learned
Compute explicit examples: 2 + ω = ω, ω + 2 = ω + 2, 2 · ω = ω, ω · 2 = ω + ω. For each, draw the concatenated well-ordering to see why commutativity fails. Then prove the Cantor normal form theorem for ordinals below ε₀ by expressing ordinals like ω² + ω · 3 + 5 and verifying uniqueness. This gives concrete intuition before tackling the formal recursive definitions.

## Common Misconceptions
- Ordinal arithmetic is not cardinal arithmetic — ω + ω = ω · 2 as ordinals, but ℵ₀ + ℵ₀ = ℵ₀ as cardinals.
- Non-commutativity applies to all three operations, not just addition: 2^ω = ω (the supremum of 2^n), but ω^2 = ω · ω, which is much larger than ω.
