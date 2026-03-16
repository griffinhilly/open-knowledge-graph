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

## Explainer

You know that infinite cardinals form a strict hierarchy — Cantor's theorem guarantees that the power set P(A) always has strictly larger cardinality than A, so there is no largest infinite cardinal. You also know the axiom of power set guarantees P(A) exists for any set. The **beth numbers** make this tower of iterated power-set operations precise: each ℶ_α names the cardinality you reach after α applications of the power set to ℵ₀.

Define the sequence: **ℶ₀ = ℵ₀** (the cardinality of ℕ). **ℶ₁ = 2^{ℵ₀}** (the cardinality of P(ℕ)), which equals |ℝ| — the cardinality of the continuum. **ℶ₂ = 2^{ℶ₁} = 2^{2^{ℵ₀}}** (the cardinality of P(ℝ) = the cardinality of all functions ℝ → {0,1}). In general, ℶ_{α+1} = 2^{ℶ_α}. At limit ordinals λ, ℶ_λ = sup{ℶ_β : β < λ}. Each step applies one power set; Cantor's theorem guarantees ℶ_{α+1} > ℶ_α strictly at every successor step.

How do beth numbers relate to the aleph numbers? The aleph sequence ℵ₀, ℵ₁, ℵ₂, ... enumerates all infinite cardinals *by ordinal rank* — ℵ₁ is the first uncountable cardinal, ℵ₂ is the next, and so on. The beth sequence enumerates cardinals by *power-set iteration*. We always have ℶ_α ≥ ℵ_α — beth numbers grow at least as fast as alephs — but the two sequences can diverge. The statement **ℶ₁ = ℵ₁** is precisely the **continuum hypothesis (CH)**: the power set of ℕ has the smallest possible uncountable cardinality. The statement **ℶ_α = ℵ_α for all ordinals α** is the **generalized continuum hypothesis (GCH)**, which says the aleph and beth sequences are identical — every power set operation produces exactly the next aleph. Both CH and GCH are independent of ZFC: they can be neither proved nor disproved from the axioms.

The practical value of beth numbers is as a natural measuring system for cardinalities that arise from power sets. When you encounter |ℝ| = ℶ₁, |P(ℝ)| = ℶ₂, or the cardinality of all functions from ℝ to ℝ (also ℶ₂, since |ℝ^ℝ| = (ℶ₁)^{ℶ₁} = 2^{ℶ₁} = ℶ₂), you are reading beth numbers directly. The beth hierarchy is the natural yardstick for the geometry of infinity produced by power sets, independent of the open question of how those sizes compare to the official aleph ranking.
