---
id: kan-extensions
title: Kan Extensions
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: yoneda-lemma
  type: hard
- id: limits-and-colimits
  type: hard
- id: adjoint-functors
  type: soft
- id: functor-categories
  type: soft
- id: functions-and-function-properties
  type: soft
tags:
- Kan extension
- left Kan extension
- right Kan extension
- pointwise Kan extension
- colimit formula
- universal construction
stage: advanced
status: draft
---
# Kan Extensions

## Core Idea
Given functors K: C → D and F: C → E, the left Kan extension Lan_K F: D → E is the universal functor extending F along K, satisfying a universal property: Nat(Lan_K F, G) ≅ Nat(F, G ∘ K) for all G: D → E. Dually, the right Kan extension Ran_K F satisfies Nat(G, Ran_K F) ≅ Nat(G ∘ K, F). When E is cocomplete, left Kan extensions can be computed pointwise as colimits: (Lan_K F)(d) = colim_{(c, K(c)→d)} F(c) over the comma category (K ↓ d). Saunders Mac Lane famously wrote that "all concepts are Kan extensions," since limits, colimits, adjunctions, and even the Yoneda embedding can be expressed as Kan extensions.

## How It's Best Learned
Start with the simplest case: K is the inclusion of a subcategory and F assigns values on that subcategory. Compute the left Kan extension as a colimit over the relevant comma category for a concrete example (e.g., extending a functor defined on a discrete category to a larger one). Then verify that adjoint functors are a special case: the left adjoint of G is the left Kan extension of the identity along G.

## Common Misconceptions
- Kan extensions need not exist in general; existence requires sufficient (co)completeness conditions or specific properties of the functors involved.
- Pointwise Kan extensions (computed as (co)limits) are stronger than abstract Kan extensions defined solely by the universal property; the pointwise version implies the abstract one but not conversely.
- The phrase "all concepts are Kan extensions" is a conceptual statement about the universality of the construction, not a claim that every theorem in category theory literally reduces to a Kan extension computation.
