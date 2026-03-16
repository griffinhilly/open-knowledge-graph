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

## Explainer

You know from infinite cardinal numbers that cardinals measure the "size" of sets, and Cantor's theorem guarantees infinitely many distinct infinite cardinals: ℵ₀ < ℵ₁ < ℵ₂ < ... You also know that two sets have the same cardinality exactly when a bijection between them exists. Cardinal arithmetic extends this framework by defining operations on cardinalities. The definitions are natural — but the behavior of infinite cardinals is shockingly different from finite arithmetic.

**Cardinal addition** is defined via disjoint union: κ + λ = |K ⊔ L|, where K and L are disjoint sets of cardinalities κ and λ. **Cardinal multiplication** is the cardinality of the Cartesian product: κ · λ = |K × L|. For finite cardinals, these agree with ordinary arithmetic. For infinite cardinals, both operations **collapse**: if κ and λ are infinite and κ ≥ λ, then κ + λ = κ · λ = κ. Intuitively: ℕ ∪ ℕ and ℕ × ℕ are both countable, so ℵ₀ + ℵ₀ = ℵ₀ · ℵ₀ = ℵ₀. The general proof uses the axiom of choice to well-order κ and exhibit an explicit bijection κ × κ → κ by a transfinite diagonal enumeration. The conceptual consequence is that infinity **absorbs**: adding or multiplying an infinite cardinal by anything no larger leaves the cardinal unchanged. There is nothing analogous in finite arithmetic.

**Cardinal exponentiation** κ^λ is the cardinality of the set of all functions from L to K — equivalently, K^L. This operation does not collapse. The most important case is 2^ℵ₀: the cardinality of all functions ℕ → {0, 1}, equivalently the cardinality of all subsets of ℕ (by binary representation), equivalently the cardinality of ℝ (by the decimal expansion bijection). Cantor's theorem guarantees 2^ℵ₀ > ℵ₀. But the precise value of 2^ℵ₀ in the ℵ-hierarchy cannot be determined from ZFC alone — the assertion 2^ℵ₀ = ℵ₁ is the **continuum hypothesis**, which Gödel showed cannot be disproved from ZFC and Cohen showed cannot be proved. It is genuinely independent, meaning there are models of ZFC where 2^ℵ₀ = ℵ₁ and models where 2^ℵ₀ = ℵ₂₃₇.

Comparing cardinal and ordinal arithmetic reveals how different they are. In ordinal arithmetic, ω + ω > ω: the first copy of ω finishes before the second one begins, producing a strictly larger well-order. In cardinal arithmetic, ℵ₀ + ℵ₀ = ℵ₀: cardinality ignores order and cares only about bijective matching — the two copies of ℕ can be interleaved into one. The symbols ω and ℵ₀ name the same underlying set (the natural numbers), but they represent different mathematical structures: ω is that set viewed as a well-ordered type, ℵ₀ is that set viewed as a cardinality class. Operating on them under different arithmetic rules is not a contradiction — it is a consequence of measuring different things.
