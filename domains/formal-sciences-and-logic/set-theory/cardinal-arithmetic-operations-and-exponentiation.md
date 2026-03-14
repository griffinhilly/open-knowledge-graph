---
id: cardinal-arithmetic-operations-and-exponentiation
title: Cardinal Arithmetic, Exponentiation, and Hierarchy
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: aleph-hierarchy-and-cardinal-numbers
  type: hard
- id: cardinal-arithmetic
  type: soft
builds-toward:
- continuum-hypothesis-and-independence
tags:
- cardinal-arithmetic
- cardinal-exponentiation
- power-set
stage: formal-systems
status: draft
---

# Cardinal Arithmetic, Exponentiation, and Hierarchy

## Core Idea
Cardinal addition and multiplication of infinite cardinals collapse: for any infinite cardinal κ, κ + κ = κ and κ · κ = κ. Cardinal exponentiation 2^κ is the cardinality of P(κ), always strictly larger than κ by Cantor's theorem. This creates an infinite hierarchy: κ < 2^κ < 2^(2^κ) < ...

## How It's Best Learned
Verify collapse laws: |ℕ| + |ℕ| = |ℕ|, |ℕ| · |ℕ| = |ℕ|. Prove 2^ℵ₀ > ℵ₀ by Cantor's diagonal argument. Build the beth hierarchy to see increasingly larger infinities via exponentiation.

## Common Misconceptions
- Assuming κ + κ ≠ κ for infinite κ based on finite intuition. - Thinking 2^κ is just 'slightly larger' than κ. - Confusing cardinal and ordinal arithmetic operations and properties.
