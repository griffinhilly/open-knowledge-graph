---
id: beth-numbers
title: Beth Numbers
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: infinite-cardinal-numbers
  type: hard
- id: axiom-of-power-set
  type: hard
builds-toward:
- continuum-hypothesis
tags:
- beth
- beth numbers
- power set
- GCH
- cardinal exponentiation
stage: formal-systems
status: draft
---

# Beth Numbers

## Core Idea
The beth numbers ℶ₀, ℶ₁, ℶ₂, ... measure cardinality by iterated power set operations rather than by ordinal indexing. ℶ₀ = ℵ₀ (the cardinality of ℕ), and ℶ_{α+1} = 2^{ℶ_α} (the cardinality of the power set of a set of size ℶ_α). At limit ordinals, ℶ_λ = sup{ℶ_β : β < λ}. By Cantor's theorem, ℶ_{α+1} > ℶ_α, so the beth sequence is strictly increasing. The generalized continuum hypothesis (GCH) is equivalent to the statement that ℶ_α = ℵ_α for all ordinals α — that is, each power set operation produces exactly the next aleph. Without GCH, the beth and aleph sequences can diverge: we always have ℶ_α ≥ ℵ_α, but the gap can be arbitrarily large.

## How It's Best Learned
Compute the first few beth numbers: ℶ₀ = ℵ₀, ℶ₁ = 2^{ℵ₀} = |ℝ| (the continuum), ℶ₂ = 2^{2^{ℵ₀}} = |P(ℝ)|. Compare with the aleph sequence: ℵ₀ = ℶ₀ always, but ℵ₁ = ℶ₁ is exactly the continuum hypothesis. State GCH as 'the aleph and beth sequences are identical' and verify that this is equivalent to saying 2^{ℵ_α} = ℵ_{α+1} for all α.

## Common Misconceptions
- Beth numbers are not an alternative to aleph numbers — they measure a different thing. Alephs enumerate cardinals by ordinal rank; beths enumerate cardinals by power-set iteration.
- ℶ₁ is always equal to 2^{ℵ₀} (by definition), but whether ℶ₁ = ℵ₁ is independent of ZFC.
