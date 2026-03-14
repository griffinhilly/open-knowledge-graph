---
id: cardinal-arithmetic
title: Cardinal Arithmetic
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: infinite-cardinal-numbers
  type: hard
- id: axiom-of-choice
  type: soft
- id: cardinality-and-countability
  type: soft
- id: zorns-lemma
  type: soft
builds-toward:
- continuum-hypothesis
tags:
- cardinal arithmetic
- addition
- multiplication
- exponentiation
- beth numbers
stage: formal-systems
status: validated
---
# Cardinal Arithmetic

## Core Idea
Cardinal arithmetic defines operations on cardinals: addition κ + λ = |K ⊔ L| (disjoint union), multiplication κ · λ = |K × L| (Cartesian product), and exponentiation κ^λ = |K^L| (all functions from L to K). For infinite cardinals under AC, both addition and multiplication simplify dramatically: κ + λ = κ · λ = max(κ, λ) for any infinite cardinals κ, λ. Cardinal exponentiation, however, is far less trivial — the value of 2^ℵ₀ cannot be determined from ZFC alone and is the subject of the continuum hypothesis. These operations behave very differently from their ordinal arithmetic counterparts.

## How It's Best Learned
Prove κ + κ = κ and κ · κ = κ for infinite cardinals (using well-ordering to exhibit explicit bijections). Compute 2^ℵ₀ = |ℝ| = |P(ℕ)| via binary representations of reals. Then contrast with ordinal arithmetic: ω + ω > ω in ordinals, but ℵ₀ + ℵ₀ = ℵ₀ in cardinals — the same symbol behaves differently in the two systems.

## Common Misconceptions
- Cardinal and ordinal arithmetic are completely different: ω + ω > ω as ordinals, but ℵ₀ + ℵ₀ = ℵ₀ as cardinals.
- The equation 2^ℵ₀ = ℵ₁ is the continuum hypothesis, an independent statement, not a theorem provable in ZFC.
