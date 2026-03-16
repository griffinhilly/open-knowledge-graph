---
id: limit-ordinals-and-omega
title: Limit Ordinals and Omega
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: finite-ordinals-as-natural-numbers
  type: hard
- id: von-neumann-ordinals
  type: soft
builds-toward:
- transfinite-induction
- ordinal-arithmetic-and-exponentiation
tags:
- ordinals
- limit-ordinals
- omega
- successor
stage: formal-systems
status: draft
---

# Limit Ordinals and Omega

## Core Idea
Limit ordinals are ordinals α with no immediate predecessor: α is not a successor ordinal (α ≠ β+1 for any β). The smallest limit ordinal is ω = {0, 1, 2, ...}, the order type of ℕ. Every ordinal is either 0, a successor, or a limit. Limits capture the idea of 'continuing indefinitely without end.'

## How It's Best Learned
Distinguish successor ordinals (n+1) from limits (ω, ω+ω, etc.). Show that ω is the union of all finite ordinals and verify it is indeed an ordinal. Explore ω+1, ω+2, ..., 2ω as further limits and successors.

## Common Misconceptions
- Confusing limit ordinals with suprema; limits are actual sets/ordinals, not limits in a topological sense.
- Forgetting that even very large ordinals have successors; the class of ordinals has no maximum.

## Explainer

The finite ordinals (0, 1, 2, 3, ...) are sets built from ∅ using the successor operation: each new ordinal is the set of all previous ordinals. Zero is ∅, one is {∅}, two is {∅, {∅}}, and so on. This process can continue indefinitely — but can the entire infinite sequence be gathered into a single set? The von Neumann ordinal construction you have already studied says yes: **ω** (omega) = {0, 1, 2, 3, ...}, the set containing all finite ordinals. It is itself an ordinal, since its elements are exactly the ordinals smaller than it. But notice something important: ω is not the successor of any finite ordinal. You cannot point to a "last" finite ordinal n and say ω = n+1, because for every n there is n+1 which is still finite and strictly less than ω.

This is the defining feature of a **limit ordinal**: an ordinal α that has no immediate predecessor — there is no β such that α = β+1. The key classification theorem states that every ordinal falls into exactly one of three categories: zero (∅), a successor ordinal (of the form β+1), or a limit ordinal. All nonzero finite ordinals are successors. ω is the first limit ordinal — it can only be "reached" by taking the union of everything before it. In fact, limit ordinals are precisely those α equal to the union of all smaller ordinals: ω = ∪{0, 1, 2, ...} = the set of all finite ordinals, which is ω itself.

Past ω the alternation of successors and limits continues indefinitely. ω+1, ω+2, ... are successors of previous ordinals. Then **ω+ω** (written 2ω) is the next limit ordinal — the union of all ω+n. Then 3ω, 4ω, and eventually ω² is a limit ordinal, then ω³, ωω (written ω^ω), and far beyond. The structure repeats at every scale: a stretch of successor ordinals, then a limit collecting all of them, then more successors, then a higher limit. Limit ordinals mark the moments where you cannot "count up" to an ordinal one step at a time — you can only approach from below by taking a supremum.

Understanding limit ordinals is a prerequisite for **transfinite induction**, where the inductive step must handle three cases instead of two: base case (0), successor case (α → α+1), and the limit case (showing the property holds at λ given it holds at all β < λ). The limit case is what allows proofs and definitions to "cross" the gap that no finite number of successor steps can bridge. Every time an ordinal construction reaches ω, 2ω, ω², or any other limit, the limit case handles the transition — and the pattern repeats throughout the transfinite ordinals.
