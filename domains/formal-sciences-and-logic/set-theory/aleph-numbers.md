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
