---
id: ordinal-addition-multiplication
title: Ordinal Addition and Multiplication
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: ordinal-numbers-and-order
  type: hard
- id: limit-ordinals-and-omega
  type: hard
builds-toward:
- ordinal-arithmetic
- transfinite-induction
tags:
- ordinals
- arithmetic
- order
- non-commutativity
stage: formal-systems
status: draft
---

# Ordinal Addition and Multiplication

## Core Idea
Ordinal addition and multiplication are defined recursively on ordinal order. Unlike cardinal arithmetic, ordinal operations are not commutative: 1 + ω = ω but ω + 1 ≠ ω. Multiplication is defined via repeated addition, and both operations respect order: if α < β, then γ + α < γ + β.

## How It's Best Learned
Compute concrete examples: 1 + ω (append one element at the end of ω), ω + 1 (place ω first, then one element), ω · 2 (two copies of ω in sequence), 2 · ω (infinite copies of the ordinal 2). Visualize as order types of specific sets.

## Common Misconceptions
- Assuming commutativity of ordinal addition (ω + 1 ≠ 1 + ω).
- Confusing ordinal operations with cardinal operations; they differ fundamentally.

## Explainer

Recall that ordinals represent **order types** — not just sizes, but the specific shape of how elements are arranged. The ordinal ω is the order type of the natural numbers: an endless sequence with a beginning but no end. ω + 1 is the order type of the natural numbers followed by one more element — still countably infinite in size, but with a different structure: now there is a last element. This is the key insight for ordinal arithmetic. Every operation must be interpreted in terms of how it rearranges the ordering, not merely how it changes the count.

**Ordinal addition** α + β means: take an ordered copy of α, then immediately after it, place an ordered copy of β. So 1 + ω places one element before the natural numbers. Since there is no last element in ω, that initial element gets absorbed — the resulting order type looks just like ω. But ω + 1 places the natural numbers first, then appends one element at the end. Now there is a greatest element. These two are genuinely different order types, which is why **ordinal addition is not commutative**: 1 + ω = ω, but ω + 1 ≠ ω.

**Ordinal multiplication** α · β means: take β many ordered copies of α, laid end to end. So ω · 2 is two copies of ω in sequence — still countable, but with a more complex structure: two "episodes" of endless counting. But 2 · ω is ω many copies of the ordinal 2 (the set {0, 1} ordered by size). That produces an endless sequence of pairs: (0,0), (1,0), (0,1), (1,1), (0,2), (1,2), … which is order-isomorphic to ω itself. So 2 · ω = ω, but ω · 2 ≠ ω — multiplication is also non-commutative, and the argument you already know from addition explains why.

The contrast with **cardinal arithmetic** is sharp. Cardinals care only about size: ℵ₀ + 1 = ℵ₀ and ℵ₀ · 2 = ℵ₀ in both orders. Ordinals care about structure. This makes ordinal arithmetic richer and more subtle — and it is exactly this structure-sensitivity that makes ordinals the right tool for transfinite induction and recursive definitions over well-ordered sets, which you will use next.
