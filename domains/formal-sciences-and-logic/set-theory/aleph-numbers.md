---
id: aleph-numbers
title: Aleph Numbers
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: infinite-cardinal-numbers
  type: hard
- id: ordinal-numbers-and-order
  type: soft
builds-toward:
- beth-numbers
- continuum-hypothesis
tags:
- aleph
- cardinal numbers
- aleph-null
- aleph-one
- cardinal successor
stage: formal-systems
status: draft
---

# Aleph Numbers

## Core Idea
The aleph numbers ℵ₀, ℵ₁, ℵ₂, ... enumerate the infinite cardinal numbers in increasing order, indexed by ordinals. ℵ₀ is the cardinality of ℕ — the smallest infinite cardinal. ℵ₁ is the smallest cardinal greater than ℵ₀, ℵ₂ the smallest greater than ℵ₁, and in general ℵ_{α+1} is the cardinal successor of ℵ_α. At limit ordinals λ, ℵ_λ = sup{ℵ_β : β < λ}. Every infinite cardinal is an aleph (assuming the axiom of choice, which guarantees that every set can be well-ordered). The aleph sequence thus provides a complete, well-ordered enumeration of all infinite cardinalities.

## How It's Best Learned
Begin with ℵ₀ and its closure properties (ℵ₀ + ℵ₀ = ℵ₀, ℵ₀ · ℵ₀ = ℵ₀). Then define ℵ₁ as the cardinality of the set of all countable ordinals (ω₁), and verify that ω₁ is uncountable. Understand that the continuum hypothesis is precisely the claim ℵ₁ = 2^{ℵ₀}. Work through the distinction between 'the next cardinal' (ℵ_{α+1}) and 'the power set cardinal' (2^{ℵ_α}) — these are conceptually different operations that may or may not coincide.

## Common Misconceptions
- ℵ₁ is not defined as the cardinality of the reals — it is the smallest uncountable cardinal. Whether |ℝ| = ℵ₁ is the content of the continuum hypothesis, which is independent of ZFC.
- The aleph sequence requires the axiom of choice; without it, there can be infinite cardinals that are incomparable and do not appear in the aleph hierarchy.

## Explainer

You already know about infinite cardinal numbers: the idea that two sets have the same cardinality when a bijection exists between them, and that not all infinities are the same size. The aleph numbers give infinite cardinals a systematic name and a complete well-ordered listing. The starting point, **ℵ₀** (aleph-null), is the cardinality of the natural numbers ℕ — the smallest infinite cardinal, as you verified when showing that ℤ, ℚ, and ℕ×ℕ are all countable. Any set that can be put in bijection with ℕ has cardinality ℵ₀.

The next step requires ordinal numbers. The set ω₁ of all countable ordinals (all ordinals in bijection with a subset of ℕ) is itself *not* countable — if it were, it would be a countable ordinal and would appear in itself, a contradiction. So ω₁ is an uncountable well-ordered set, and its cardinality is defined to be **ℵ₁**, the smallest uncountable cardinal. Continuing the pattern: ω₂ is the set of all ordinals of cardinality ≤ ℵ₁, and its cardinality is **ℵ₂**. In general, ℵ_{α+1} is the cardinality of the set of all ordinals of cardinality ≤ ℵ_α — the "next" infinite cardinal after ℵ_α. At limit ordinals λ (ordinals with no immediate predecessor), ℵ_λ is the supremum of all earlier alephs.

The critical conceptual distinction is between **ℵ_{α+1}** (the cardinal successor of ℵ_α, defined as the next larger cardinal) and **2^{ℵ_α}** (the power set cardinal, the cardinality of the set of all subsets of a set of size ℵ_α). These are conceptually different operations. Cardinal arithmetic tells us 2^{ℵ₀} is the cardinality of ℝ (and of the power set of ℕ), but where this cardinal sits in the aleph hierarchy is exactly the **continuum hypothesis**: the claim that 2^{ℵ₀} = ℵ₁. Gödel and Cohen together proved this is independent of ZFC — neither provable nor disprovable — so the relationship between power sets and the aleph hierarchy is genuinely undecidable from the standard axioms.

Finally, the axiom of choice is what makes the aleph numbers a *complete* account of infinite cardinality. Under the axiom of choice, every set can be well-ordered, and every infinite cardinal is therefore equal to ℵ_α for some ordinal α. Without choice, there can be infinite sets with cardinality incomparable to any aleph — "wild" cardinals that do not fit into the aleph hierarchy at all. With choice, the hierarchy is total: the alephs are *all* the infinite cardinals, and the question of how a set's cardinality relates to the alephs is always well-posed. This completeness of the aleph hierarchy under AC is one of the strongest arguments for adopting the axiom of choice as a set-theoretic foundation.
