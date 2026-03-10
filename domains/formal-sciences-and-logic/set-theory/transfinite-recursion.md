---
id: transfinite-recursion
title: Transfinite Recursion
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: transfinite-induction
  type: hard
- id: axiom-of-replacement
  type: hard
- id: mathematical-induction
  type: soft
- id: well-ordering-principle
  type: soft
builds-toward:
- infinite-cardinal-numbers
- cofinality-and-regular-cardinals
tags:
- recursion
- ordinals
- transfinite
- cumulative hierarchy
- ordinal arithmetic
stage: formal-systems
status: draft
---

# Transfinite Recursion

## Core Idea
Transfinite recursion allows the definition of functions on all ordinals by specifying: F(0) = base value, F(α+1) = g(F(α)) at successors, and F(λ) = h({F(β) : β < λ}) at limit ordinals. The axiom of replacement is needed to ensure that the partial functions at each stage form a set. The theorem on transfinite recursion guarantees a unique such F exists given any valid specifications. Key applications include defining ordinal arithmetic (+, ·, exponentiation), constructing the cumulative hierarchy V_α, and building the aleph sequence ℵ₀, ℵ₁, ℵ₂, ....

## How It's Best Learned
Define ordinal addition α+β by recursion on β: (α+0) = α, (α+(β+1)) = (α+β)+1, (α+λ) = sup{α+β : β < λ}. Then define ordinal multiplication and exponentiation similarly. In each case explicitly state all three cases. Separately define the cumulative hierarchy V_α by recursion on α and compute V₀, V₁, V₂, V_ω.

## Common Misconceptions
- Transfinite recursion requires the axiom of replacement — without it, the recursion may not produce a set at every transfinite stage.
- At limit stages, one typically takes a union or supremum over all previous values, not the 'previous value' (which doesn't exist at limits).
