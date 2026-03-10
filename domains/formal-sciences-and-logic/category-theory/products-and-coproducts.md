---
id: products-and-coproducts
title: Products and Coproducts
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: universal-properties
  type: hard
- id: opposite-categories-and-duality
  type: hard
- id: initial-and-terminal-objects
  type: soft
- id: cartesian-product
  type: soft
builds-toward:
- limits-and-colimits
- equalizers-and-coequalizers
- adjoint-functors
tags:
- product
- coproduct
- projection
- injection
- universal property
stage: advanced
status: draft
---

# Products and Coproducts

## Core Idea
The categorical product A × B of two objects is characterized by a universal property: it comes with projections π_1: A×B → A and π_2: A×B → B such that for any object C with morphisms f: C → A and g: C → B, there is a unique morphism ⟨f,g⟩: C → A×B with π_1∘⟨f,g⟩ = f and π_2∘⟨f,g⟩ = g. The coproduct A+B is the dual: characterized by injections and unique morphisms out of it. In Set these are Cartesian product and disjoint union; in Grp they are direct product and free product; in Ab they coincide as the direct sum.

## How It's Best Learned
Prove that the Cartesian product of sets satisfies the universal property of the categorical product in Set. Then derive the coproduct by duality and verify it is the disjoint union. Compute products and coproducts in a poset category to see they correspond to meets (infima) and joins (suprema).

## Common Misconceptions
- Products and coproducts need not coincide (they do in Ab but not in Grp or Set).
- The product object A×B is only defined up to unique isomorphism; any specific construction (e.g., ordered pairs) is just one realization.
- The universal morphism ⟨f,g⟩ must be unique—uniqueness is what makes the product a limit, not just an object with projections.
