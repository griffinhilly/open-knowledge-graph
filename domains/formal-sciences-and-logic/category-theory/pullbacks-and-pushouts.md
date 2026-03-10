---
id: pullbacks-and-pushouts
title: Pullbacks and Pushouts
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: limits-and-colimits
  type: hard
- id: products-and-coproducts
  type: soft
builds-toward:
- adjoint-functors
tags:
- pullback
- pushout
- fiber product
- amalgamation
- span
- cospan
stage: advanced
status: draft
---

# Pullbacks and Pushouts

## Core Idea
A pullback of morphisms f: A → C and g: B → C is a limit of the cospan diagram A → C ← B: an object P with morphisms to A and B making a commutative square, universal with this property. The pushout is the colimit of the span A ← C → B. In Set, the pullback is {(a,b) ∈ A×B | f(a) = g(b)} (fiber product), and the pushout is the coproduct A+B quotiented by the relation f(c) ~ g(c). Pullbacks model intersection, preimage, and change of base; pushouts model amalgamation, gluing, and quotients.

## How It's Best Learned
Compute pullbacks explicitly in Set for a concrete choice of f and g: take f: {1,2,3} → {a,b} and g: {x,y} → {a,b} and construct the pullback set. Then dualize to understand pushouts by gluing topological spaces along a common subspace.

## Common Misconceptions
- A pullback square is not just any commutative square; the universal property is essential.
- Pullbacks and intersections coincide in Set only when A and B are subsets of C with f and g being inclusions.
- Pushouts in Top are colimits in the category of topological spaces, which involves a specific topology on the pushout set.
