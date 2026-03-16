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

## Explainer

From your work with von Neumann ordinals, you already know that ordinals are built from the empty set outward: 0 = ∅, 1 = {0}, 2 = {0, 1}, and in general each natural number n = {0, 1, ..., n−1}. The key property that makes this construction powerful is that membership (∈) among von Neumann ordinals coincides exactly with the ordering relation (<). When we say α < β for ordinals, we mean α ∈ β, and also α ⊂ β — the smaller ordinal is literally a member and a subset of the larger. This tight connection between set-membership and ordering is what lets ordinals serve as canonical yardsticks for well-ordered sets.

The central idea of this topic is that every **well-ordered set** has a unique ordinal that describes its order structure. Two well-ordered sets are **order-isomorphic** if there is a bijection between them that preserves the ordering in both directions — every "before/after" relationship is maintained. The ordinal of a well-ordered set is the unique von Neumann ordinal it is isomorphic to. So the ordinal ω is not just the set {0, 1, 2, ...}; it is the canonical representative of "any countably infinite well-ordering that has no greatest element and where every element has only finitely many predecessors." Any well-ordering with that structure is isomorphic to ω, regardless of what its elements actually are.

Every ordinal falls into exactly one of three categories. **Zero** (0 = ∅) is the empty well-ordering. A **successor ordinal** has the form α + 1 = α ∪ {α} — it has an immediate predecessor. A **limit ordinal** is any nonzero ordinal that is not a successor; it has no immediate predecessor and equals the supremum of all smaller ordinals. The first limit ordinal is ω, the ordinal of the natural numbers. After ω come ω+1, ω+2, ..., then ω+ω (written ω·2), which is the next limit ordinal. This trichotomy mirrors the structure of transfinite induction, which you already know: you handle the base case (0), the successor step (α → α+1), and the limit step (taking the union up to a limit ordinal) separately, covering all ordinals.

Ordinal comparison is **trichotomous**: for any ordinals α and β, exactly one of α < β, α = β, or α > β holds. This follows because the ordinals are themselves well-ordered by membership — every nonempty class of ordinals has a least element. This total ordering is much stronger than the situation with arbitrary sets, where two sets may be incomparable. The fact that ordinals are totally ordered makes them powerful tools for transfinite arguments: you can always compare two well-ordered sets by comparing their ordinals, and knowing which is smaller tells you that one embeds as an initial segment of the other. This is the foundation on which ordinal arithmetic and the theory of infinite cardinals (via aleph numbers) will be built.
