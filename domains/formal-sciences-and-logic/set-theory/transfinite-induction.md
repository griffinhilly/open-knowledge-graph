---
id: transfinite-induction
title: Transfinite Induction
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: von-neumann-ordinals
  type: hard
- id: mathematical-induction
  type: soft
- id: well-ordering-principle
  type: soft
- id: well-founded-relations
  type: soft
builds-toward:
- transfinite-recursion
- well-ordering-theorem
- infinite-cardinal-numbers
tags:
- induction
- ordinals
- transfinite
- proof technique
- limit ordinals
stage: formal-systems
status: validated
---

# Transfinite Induction

## Core Idea
Transfinite induction extends mathematical induction to all ordinals. To prove a property P holds for every ordinal α, it suffices to verify three cases: (1) the base case P(0); (2) the successor step: P(α) implies P(α+1) for all α; and (3) the limit step: if P(β) holds for all β < λ, then P(λ) holds for every limit ordinal λ. The limit step is the essential addition beyond ordinary induction and captures behavior at stages like ω, ω², and ε₀. The principle is justified by the fact that the ordinals are well-ordered by ∈, so every non-empty class of ordinals has a least element.

## How It's Best Learned
Prove simple properties of ordinals by transfinite induction: every ordinal is 0, a successor, or a limit; every ordinal is transitive. Then prove results in ordinal arithmetic. Internalize that the limit case typically takes a union or supremum of all previous values rather than appealing to an immediate predecessor.

## Common Misconceptions
- Omitting the limit case yields a principle that only reaches finite ordinals — it does not extend to ω or beyond.
- The limit step assumes P holds for ALL β < λ (the strong induction pattern), not just for the element immediately before λ, which does not exist.
