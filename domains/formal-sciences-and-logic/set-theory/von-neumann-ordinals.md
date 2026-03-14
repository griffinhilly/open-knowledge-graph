---
id: von-neumann-ordinals
title: Von Neumann Ordinals
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: axiom-of-infinity
  type: hard
- id: axiom-of-regularity
  type: soft
- id: equivalence-relations
  type: soft
- id: axiom-of-replacement
  type: soft
- id: axiom-of-separation
  type: soft
builds-toward:
- transfinite-induction
- transfinite-recursion
- infinite-cardinal-numbers
- well-ordering-theorem
tags:
- ordinals
- von neumann
- transfinite
- well-order
- successor
- limit
stage: formal-systems
status: validated
---
# Von Neumann Ordinals

## Core Idea
In the von Neumann representation, each ordinal is defined as the set of all smaller ordinals: 0 = ∅, 1 = {0}, 2 = {0,1}, ω = {0,1,2,...}, ω+1 = {0,1,2,...,ω}, and so on. A set α is a (von Neumann) ordinal if it is transitive (every element of α is also a subset of α) and is well-ordered by membership ∈. Every well-ordered set is order-isomorphic to a unique ordinal, making ordinals canonical representatives of well-order types. The ordinals are partitioned into three kinds: 0 (the empty set), successor ordinals (of the form α ∪ {α}), and limit ordinals (non-zero ordinals with no immediate predecessor, like ω, ω·2, ε₀).

## How It's Best Learned
Build the first several ordinals explicitly: 0, 1, 2, 3, ω, ω+1, ω+2, ω+ω. For each, verify transitivity and that ∈ well-orders the set. Work through the proof that any well-ordered set is isomorphic to a unique ordinal — this makes the definition feel canonical rather than arbitrary.

## Common Misconceptions
- ω is not just 'infinity' — it is a specific set (the set of all finite ordinals) and is the smallest infinite ordinal.
- Ordinal arithmetic is not commutative: 1+ω = ω (since ω is the supremum), but ω+1 > ω — order matters.
