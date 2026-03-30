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
status: validated
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

## Questions

```yaml
- question: "What is the coproduct of two sets A and B in the category Set?"
  type: multiple-choice
  options:
    - "The Cartesian product A × B"
    - "The disjoint union A ⊔ B"
    - "The intersection A ∩ B"
    - "The set of all functions from A to B"
  answer: 1
  explanation: "The coproduct in Set is the disjoint union A ⊔ B. It is equipped with injections i₁: A → A ⊔ B and i₂: B → A ⊔ B, and for any set C with functions f: A → C and g: B → C there is a unique function [f,g]: A ⊔ B → C satisfying [f,g]∘i₁ = f and [f,g]∘i₂ = g. The Cartesian product A × B is the categorical product, not the coproduct — a common confusion."

- question: "In most category, the product A × B and the coproduct A + B of two objects are isomorphic to each other."
  type: true-false
  answer: false
  explanation: "This is only true in special categories. In Ab (abelian groups), finite products and coproducts coincide as the direct sum A ⊕ B — this is a special property of abelian categories called a 'biproduct.' But in Set, A × B (Cartesian product) and A ⊔ B (disjoint union) have different cardinalities and are generally non-isomorphic. In Grp, the product is the direct product while the coproduct is the free product — very different structures."

- question: "The universal property of the categorical product requires that the pairing morphism ⟨f,g⟩ be unique. Why is uniqueness essential — what would fail if two distinct morphisms both commuted with the projections?"
  type: short-answer
  answer: "If two distinct morphisms h, k: C → A×B both satisfied π₁∘h = f, π₂∘h = g and π₁∘k = f, π₂∘k = g, then A×B would not be a limit — it would merely be an object with projections. Uniqueness forces the product to be the 'most economical' or 'universal' object satisfying the factoring condition, ensuring that any two constructions satisfying the universal property are uniquely isomorphic. Without uniqueness, the universal property cannot determine the product up to unique isomorphism."
  explanation: "Uniqueness is the defining feature that distinguishes universal properties from weaker existence conditions. It guarantees that different constructions of the product (e.g., ordered pairs vs. tagged unions) are not just isomorphic but canonically so, which is why category theory can work 'up to isomorphism' without losing information."
```

## Explainer

You already know the Cartesian product of sets: A × B = {(a, b) : a ∈ A, b ∈ B}. Category theory asks a surprising question: can we describe this construction **purely in terms of morphisms**, without ever mentioning elements? The answer is the universal property of the product.

The categorical product A × B is defined by two projection morphisms π₁: A×B → A and π₂: A×B → B, satisfying the following condition: for **any** object C and **any** pair of morphisms f: C → A and g: C → B, there exists a **unique** morphism ⟨f,g⟩: C → A×B such that π₁∘⟨f,g⟩ = f and π₂∘⟨f,g⟩ = g. The key word is *unique* — there is exactly one way to factor a pair of morphisms through the product. You can verify this in Set: the unique morphism ⟨f,g⟩ is just c ↦ (f(c), g(c)), the function that pairs the outputs. Any other function into A × B that agrees with π₁ and π₂ must produce the same pairs, so uniqueness holds.

The coproduct is the **dual** construction — obtained by reversing all the arrows. The coproduct A + B comes with **injection** morphisms i₁: A → A+B and i₂: B → A+B, and for any C with morphisms f: A → C and g: B → C, there is a unique morphism [f,g]: A+B → C satisfying [f,g]∘i₁ = f and [f,g]∘i₂ = g. In Set, this is the disjoint union: [f,g] applies f to elements tagged as coming from A and g to elements tagged as coming from B. Notice how the arrows to the product (morphisms *into* A×B) become arrows from the coproduct (morphisms *out of* A+B) — perfect duality.

The behavior of products and coproducts varies dramatically across categories. In a poset (ordered set viewed as a category), the product of two elements is their **meet** (greatest lower bound) and the coproduct is their **join** (least upper bound) — notions you may recognize from lattice theory. In Ab, finite products and coproducts coincide as the direct sum A ⊕ B, a special property of abelian categories. In Grp, the product is the familiar direct product but the coproduct is the **free product** A * B, a much larger and more complicated construction where elements interleave freely from both groups.

The deep lesson is that the same abstract universal property pattern — existence and uniqueness of a factoring morphism — determines the "right" notion of pairing or co-pairing in each category. The product is defined by what maps *into* it; the coproduct by what maps *out of* it. Mastering this duality is the first step toward understanding limits and colimits in full generality.
