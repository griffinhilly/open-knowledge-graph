---
id: cardinality-and-countability
title: Cardinality and Countability
domain: mathematics
course: methods-of-proof
prerequisites:
- id: injective-surjective-bijective
  type: hard
- id: set-operations
  type: soft
builds-toward:
- cantor-diagonalization
tags:
- cardinality
- countable
- uncountable
- bijection
- infinite-sets
- Cantor
stage: formal-systems
status: draft
---

# Cardinality and Countability

## Core Idea
Two sets have the same cardinality if there exists a bijection between them. A set is countably infinite if it has the same cardinality as ℕ — that is, its elements can be listed as a sequence a₁, a₂, a₃, …. Surprisingly, ℤ and ℚ are countably infinite, even though they seem 'larger' than ℕ. A set is uncountable if no bijection with ℕ exists. The real numbers ℝ are uncountable, which means there are fundamentally different 'sizes' of infinity.

## How It's Best Learned
Construct explicit bijections: show ℕ bijects with ℤ by interleaving positive and negative integers; show ℕ bijects with ℕ × ℕ via Cantor pairing; use this to show ℚ is countable. The argument for ℝ being uncountable requires Cantor's diagonalization and is done separately.

## Common Misconceptions
- Believing infinite sets cannot be compared in size — Cantor's theory gives a rigorous way to do so.
- Assuming that because ℤ contains ℕ, |ℤ| > |ℕ| — proper subsets of infinite sets can have the same cardinality.
- Confusing 'countable' (including finite sets) with 'countably infinite'.
