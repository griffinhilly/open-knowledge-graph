---
id: infinite-cardinal-numbers
title: Infinite Cardinal Numbers
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: cardinality-and-countability
  type: hard
- id: von-neumann-ordinals
  type: hard
- id: well-ordering-theorem
  type: soft
- id: axiom-of-power-set
  type: soft
- id: transfinite-induction
  type: soft
- id: transfinite-recursion
  type: soft
builds-toward:
- cantor-theorem
- cardinal-arithmetic
- continuum-hypothesis
- cofinality-and-regular-cardinals
tags:
- cardinals
- aleph
- infinite sets
- equinumerosity
- initial ordinals
stage: formal-systems
status: validated
---
# Infinite Cardinal Numbers

## Core Idea
A cardinal number measures the size of a set via bijection: two sets have the same cardinality if and only if there is a bijection between them. In ZFC, each infinite cardinal is represented as an initial ordinal — an ordinal not in bijection with any smaller ordinal. The infinite cardinals are indexed by ordinals via the aleph sequence: ℵ₀ (cardinality of ℕ), ℵ₁ (the next uncountable cardinal), ℵ₂, ..., ℵ_ω, .... The axiom of choice ensures every set has a cardinality comparable with all others; without choice, some sets cannot be well-ordered and thus have no aleph. The aleph hierarchy, defined by transfinite recursion on ordinals, provides a complete listing of all infinite cardinals.

## How It's Best Learned
Begin with countability and the distinction between ℵ₀ and uncountable sets. Then define initial ordinals formally: verify ω is the initial ordinal for ℵ₀, and construct ω₁ (the first uncountable ordinal) via the Hartogs number construction. Build the first few alephs and locate familiar sets (ℕ, ℚ, ℝ) within the hierarchy.

## Common Misconceptions
- ℵ₁ is the second infinite cardinal (the first uncountable one); it is NOT necessarily |ℝ| — whether |ℝ| = ℵ₁ is exactly the continuum hypothesis.
- The existence of ℵ₁ does not require exhibiting an uncountable set by construction; it follows by applying axiom of replacement to ω.
