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

## Explainer

You already know that ordinals are well-ordered sets measuring "how long" a sequence is. Ordinal arithmetic asks: what happens when you combine these sequences? The key insight is that ordinal operations are defined by concatenation and replacement of well-orderings — and because well-orderings have a direction, the order of operands matters enormously.

**Ordinal addition** α + β means "put a copy of α first, then append a copy of β." So 1 + ω means: start with the single element {0}, then append the infinite sequence {0, 1, 2, …}. The result is just an infinite sequence with one extra element at the beginning — which is indistinguishable from ω itself. Hence 1 + ω = ω. But ω + 1 means: take the infinite sequence {0, 1, 2, …} and append one more element after it. That element has no immediate predecessor in the well-ordering and sits strictly beyond all of ω — so ω + 1 > ω, a strictly larger ordinal. The finite element is "swallowed" when it comes first, but survives when it comes last.

**Ordinal multiplication** α · β means "replace each element of β with a fresh copy of α." Think of ω · 2 as taking two copies of ω and laying them end to end: {0,1,2,…} followed by {0′,1′,2′,…}, which is a well-ordering of type ω + ω = ω · 2. But 2 · ω means: for each of ω's elements, put a 2-element copy. The result has type ω (the supremum of 2, 4, 6, …), because you never exhaust the two-element blocks to reach anything beyond ω. So 2 · ω = ω < ω · 2. **Ordinal exponentiation** follows similarly by transfinite recursion: α^β is ω when α = 2 and β = ω, since 2^n → ω but never reaches beyond it, while ω^2 = ω · ω is a genuinely larger ordinal.

**Cantor normal form** brings order to this landscape. Every ordinal can be written uniquely as a finite decreasing sum ω^{a₁} · c₁ + ω^{a₂} · c₂ + … + ω^{aₙ} · cₙ where a₁ > a₂ > … > aₙ are ordinals and the cᵢ are positive natural numbers — exactly like expressing a number in a positional base system, but with base ω. For example, ω² + ω · 3 + 5 is already in Cantor normal form. Arithmetic on ordinals in normal form follows rules analogous to polynomial arithmetic, except you must respect non-commutativity. The ordinals below ε₀ (the first fixed point of ω^α = α) are precisely those whose Cantor normal form uses only exponents smaller than themselves, forming a rich and concrete hierarchy for calculation.
