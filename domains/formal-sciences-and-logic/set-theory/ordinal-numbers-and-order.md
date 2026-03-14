---
id: ordinal-numbers-and-order
title: Ordinal Numbers and Order
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: von-neumann-ordinals
  type: hard
- id: transfinite-induction
  type: hard
builds-toward:
- ordinal-arithmetic
- aleph-numbers
tags:
- ordinals
- well-ordering
- order types
- limit ordinals
- successor ordinals
stage: formal-systems
status: draft
---

# Ordinal Numbers and Order

## Core Idea
Ordinal numbers serve as canonical representatives of well-order types: two well-ordered sets have the same ordinal if and only if they are order-isomorphic. Every ordinal is either 0 (the empty well-ordering), a successor ordinal α+1 (with an immediate predecessor), or a limit ordinal (a nonzero ordinal with no immediate predecessor, such as ω, ω·2, or ε₀). The ordinals themselves are well-ordered by membership, forming a proper class that extends far beyond the natural numbers. Ordinal comparison is trichotomous — for any ordinals α and β, exactly one of α < β, α = β, or α > β holds — and this total ordering is a cornerstone of transfinite arguments.

## How It's Best Learned
Classify the first several ordinals into successor vs. limit: 0, 1, 2, ..., ω (limit), ω+1 (successor), ..., ω+ω (limit). Prove that the ordinals under ∈ are well-ordered by showing every nonempty class of ordinals has a least element. Then work through examples of order-isomorphism: show that {0, 1, 2, ...} under < is isomorphic to ω, while {0, 1, 2, ..., ω} under < is isomorphic to ω+1.

## Common Misconceptions
- Limit ordinals are not simply 'large' ordinals — ω is the smallest limit ordinal and is countable. Every infinite cardinal is a limit ordinal, but most limit ordinals are not cardinals.
- Ordinal equality is order-type equality, not set-size equality: ω and ω+ω have the same cardinality (both countable) but are distinct ordinals with different order structures.
