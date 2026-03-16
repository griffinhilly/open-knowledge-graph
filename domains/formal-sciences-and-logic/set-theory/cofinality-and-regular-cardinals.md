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
- id: cardinality-and-countability
  type: soft
- id: cantor-theorem
  type: soft
builds-toward:
- independence-results-set-theory
tags:
- cofinality
- regular cardinals
- singular cardinals
- König's theorem
stage: formal-systems
status: validated
---
# Cofinality and Regular Cardinals

## Core Idea
The cofinality of an ordinal α, written cf(α), is the smallest ordinal β such that α is the supremum of a β-indexed sequence of ordinals less than α. A cardinal κ is regular if cf(κ) = κ (it cannot be written as a union of fewer than κ sets each of size less than κ); otherwise it is singular. Every successor cardinal ℵ_{α+1} is regular; limit cardinals like ℵ_ω may be singular (cf(ℵ_ω) = ω). Königʼs theorem states that cf(2^κ) > κ for all cardinals κ, placing a fundamental constraint on the continuum function: for example, 2^ℵ₀ cannot equal ℵ_ω.

## How It's Best Learned
Compute cofinalities directly: cf(ω) = ω (regular), cf(ω₁) = ω₁ (regular), cf(ℵ_ω) = ω (singular). Prove that every successor cardinal is regular. Apply König's theorem to rule out specific values for 2^ℵ₀: for instance, 2^ℵ₀ ≠ ℵ_ω because cf(ℵ_ω) = ω ≤ ℵ₀.

## Common Misconceptions
- 'Singular' cardinal is a precise technical term, not a judgment about pathological behavior — singular cardinals are perfectly well-defined and important.
- ℵ_ω is the ω-th aleph (the supremum of ℵ₀, ℵ₁, ℵ₂, ...), not ω steps beyond ℵ₀ in some other sense.

## Explainer

From your study of infinite cardinals, you know that the aleph sequence ℵ₀, ℵ₁, ℵ₂, ... extends through all ordinals: ℵ_α for every ordinal α. Successor cardinals like ℵ₁ = ℵ_{0+1} are defined as the next cardinal above the previous one. Limit cardinals like ℵ_ω are defined as suprema — ℵ_ω = sup{ℵ₀, ℵ₁, ℵ₂, ...}. **Cofinality** asks a finer question about such limit cardinals: how "approachable" is a cardinal from below?

The **cofinality** cf(κ) of a limit ordinal κ is the smallest cardinality of a cofinal subset — a set whose supremum is κ. Equivalently, it is the length of the shortest sequence that converges to κ. For ℵ_ω, the sequence ℵ₀, ℵ₁, ℵ₂, ... is cofinal and has length ω, and no shorter sequence suffices (ℵ_ω is not the supremum of any finite set). So cf(ℵ_ω) = ω. By contrast, cf(ℵ₁) = ℵ₁ itself — you cannot approach ℵ₁ from below via a countable sequence, because the supremum of countably many countable ordinals is countable, never ℵ₁.

A cardinal κ is **regular** if cf(κ) = κ — it cannot be written as the supremum of fewer than κ sets each smaller than κ. A cardinal is **singular** if cf(κ) < κ. Every successor cardinal is regular: ℵ_{α+1} cannot be the supremum of an ℵ_α-indexed sequence of cardinals each less than ℵ_{α+1}, because such a sequence would contain at most ℵ_α many cardinals each of size ≤ ℵ_α, and their union would have size ≤ ℵ_α · ℵ_α = ℵ_α < ℵ_{α+1}. Limit cardinals like ℵ_ω, ℵ_{ω₁}, etc., can be singular — ℵ_ω is the supremum of ω many smaller cardinals, so cf(ℵ_ω) = ω < ℵ_ω.

**König's theorem** states that cf(2^κ) > κ for every infinite cardinal κ. This is proved by a diagonal argument: a union of κ many sets each of size < 2^κ has size < 2^κ (by the cardinal arithmetic of cofinalities), so 2^κ cannot be the supremum of a κ-indexed sequence of smaller cardinals, meaning cf(2^κ) > κ. The striking application: 2^ℵ₀ cannot equal ℵ_ω, because cf(ℵ_ω) = ω = ℵ₀, which would require cf(2^ℵ₀) = ω ≤ ℵ₀ — contradicting König's theorem which requires cf(2^ℵ₀) > ℵ₀. Similarly, the continuum 2^ℵ₀ cannot be any ℵ_α with cf(ℵ_α) ≤ ℵ₀. This is one of the few unconditional constraints on the continuum function that holds regardless of additional set-theoretic axioms — no consistency proof or forcing argument can circumvent it.
