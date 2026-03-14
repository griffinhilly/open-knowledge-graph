---
id: cardinal-arithmetic-infinite-sets
title: Cardinal Arithmetic for Infinite Sets
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: cardinal-arithmetic
  type: hard
- id: infinite-cardinal-numbers
  type: hard
- id: aleph-numbers
  type: soft
builds-toward:
- continuum-hypothesis
- cardinal-exponentiation-and-continuums
tags:
- cardinals
- arithmetic
- infinity
- exponentiation
stage: formal-systems
status: draft
---

# Cardinal Arithmetic for Infinite Sets

## Core Idea
For infinite cardinals, addition and multiplication become trivial: ℵ₀ + ℵ₀ = ℵ₀ and ℵ₀ · ℵ₀ = ℵ₀. Exponentiation, however, is nontrivial: 2^ℵ₀ = 𝔠 (the cardinality of the continuum). The hierarchy of infinities is determined by exponentiation, and cardinal exponentiation is less understood than ordinal arithmetic.

## How It's Best Learned
Prove that ℵ₀ + ℵ₀ = ℵ₀ by enumerating the union of two countable sets. Show 2^ℵ₀ > ℵ₀ via Cantor's theorem. Introduce the notation ℵ₁ = 2^ℵ₀ (assuming CH), and explore whether ℵ₁ + ℵ₁ = ℵ₁.

## Common Misconceptions
- Thinking cardinal exponentiation has simple rules (it does not: 2^κ depends on κ in complex ways).
- Confusing cardinal addition with ordinal addition, or cardinal multiplication with set intersection.
