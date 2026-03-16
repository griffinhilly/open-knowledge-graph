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

## Explainer

You already know that **cardinals** measure the size of sets, and that infinite cardinals exist — ℵ₀ (the cardinality of the natural numbers) is the smallest. You know that cardinals form a hierarchy and that Cantor's theorem guarantees 2^κ > κ for every cardinal κ. Now we make this arithmetic precise and discover something surprising: for infinite cardinals, the ordinary rules of arithmetic collapse in addition and multiplication but become genuinely complex in exponentiation.

**Cardinal addition** for infinite sets is trivial in a strong sense. If κ is infinite and λ ≤ κ, then κ + λ = κ. In particular, ℵ₀ + ℵ₀ = ℵ₀. The proof is concrete: you can biject ℕ ∪ ℕ (two disjoint copies of the naturals) with ℕ itself by interleaving even and odd indices. More generally, the union of any two sets of the same infinite cardinality has that same cardinality. **Cardinal multiplication** collapses similarly: κ · κ = κ for any infinite cardinal κ. The bijection between ℕ × ℕ and ℕ (enumerate pairs by diagonals) is the key example. This means the product of two infinite sets is no larger than either factor — the "grid" of pairs has the same size as a single row.

**Cardinal exponentiation** is where the story becomes interesting. 2^κ counts the number of functions from κ to {0,1}, equivalently the number of subsets of κ (the **power set**). Cantor's theorem guarantees 2^κ > κ strictly, so exponentiation always escapes to a higher level of infinity. For ℵ₀, we get 2^ℵ₀ = **𝔠** (the cardinality of the continuum — the cardinality of the real numbers). Cantor proved 𝔠 > ℵ₀ via his diagonal argument; it cannot be enumerated. But exactly *which* aleph is 𝔠? That question — the **Continuum Hypothesis** (CH) — asks whether 𝔠 = ℵ₁, the very next cardinal after ℵ₀. CH is independent of ZFC, meaning neither it nor its negation can be proved.

For larger infinite cardinals, cardinal exponentiation exhibits further unpredictable behavior. Whether 2^ℵ₁ equals ℵ₂ or something larger is not decided by ZFC alone; different models of set theory give different answers. The **Generalized Continuum Hypothesis** (GCH) postulates 2^ℵₙ = ℵₙ₊₁ for all n, which would make exponentiation neat and predictable — but GCH is also unprovable and unrefutable from ZFC. Without additional axioms, cardinal exponentiation is the wild and unresolved part of cardinal arithmetic.

The contrast between addition/multiplication (trivial and determined) and exponentiation (complex and undetermined) is the central lesson. For finite cardinals, all three operations behave predictably. For infinite cardinals, only exponentiation retains genuine complexity. This asymmetry explains why the exponentiation tower — ℵ₀, 2^ℵ₀, 2^(2^ℵ₀), … — is the ladder of infinities that matters for questions about the real number system, Borel sets, and the foundations of analysis.
