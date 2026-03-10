---
id: cofinality-and-regular-cardinals
title: Cofinality and Regular Cardinals
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: infinite-cardinal-numbers
  type: hard
- id: transfinite-induction
  type: soft
- id: transfinite-recursion
  type: soft
builds-toward:
- independence-results-set-theory
tags:
- cofinality
- regular cardinals
- singular cardinals
- König's theorem
stage: formal-systems
status: draft
---

# Cofinality and Regular Cardinals

## Core Idea
The cofinality of an ordinal α, written cf(α), is the smallest ordinal β such that α is the supremum of a β-indexed sequence of ordinals less than α. A cardinal κ is regular if cf(κ) = κ (it cannot be written as a union of fewer than κ sets each of size less than κ); otherwise it is singular. Every successor cardinal ℵ_{α+1} is regular; limit cardinals like ℵ_ω may be singular (cf(ℵ_ω) = ω). Königʼs theorem states that cf(2^κ) > κ for all cardinals κ, placing a fundamental constraint on the continuum function: for example, 2^ℵ₀ cannot equal ℵ_ω.

## How It's Best Learned
Compute cofinalities directly: cf(ω) = ω (regular), cf(ω₁) = ω₁ (regular), cf(ℵ_ω) = ω (singular). Prove that every successor cardinal is regular. Apply König's theorem to rule out specific values for 2^ℵ₀: for instance, 2^ℵ₀ ≠ ℵ_ω because cf(ℵ_ω) = ω ≤ ℵ₀.

## Common Misconceptions
- 'Singular' cardinal is a precise technical term, not a judgment about pathological behavior — singular cardinals are perfectly well-defined and important.
- ℵ_ω is the ω-th aleph (the supremum of ℵ₀, ℵ₁, ℵ₂, ...), not ω steps beyond ℵ₀ in some other sense.
