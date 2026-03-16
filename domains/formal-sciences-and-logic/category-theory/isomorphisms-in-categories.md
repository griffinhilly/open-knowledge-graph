---
id: isomorphisms-in-categories
title: Isomorphisms in Categories
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: categories-and-morphisms
  type: hard
- id: injective-surjective-bijective
  type: soft
- id: functions-and-function-properties
  type: soft
builds-toward:
- equivalence-of-categories
- universal-properties
- initial-and-terminal-objects
tags:
- isomorphism
- inverse
- equivalence
- structure
stage: advanced
status: validated
---

# Isomorphisms in Categories

## Core Idea
A morphism f: A → B in a category is an isomorphism if there exists a morphism g: B → A such that g∘f = id_A and f∘g = id_B. This categorical definition unifies bijections in Set, group isomorphisms in Grp, homeomorphisms in Top, and linear isomorphisms in Vect under a single concept. Two objects are isomorphic if an isomorphism exists between them; isomorphic objects are categorically indistinguishable.

## How It's Best Learned
Verify that bijective functions are exactly the isomorphisms in Set, and that group isomorphisms match the definition. Then check that in a poset category (where morphisms are ≤ relations), the only isomorphisms are identity morphisms—since a ≤ b and b ≤ a implies a = b.

## Common Misconceptions
- An isomorphism is not simply a bijective morphism in every category; in Top the isomorphisms are homeomorphisms, not just bijective continuous maps.
- The inverse g is unique when it exists, but its existence must be verified explicitly.

## Explainer

You already know what a bijection is: a function that is both injective (no two inputs give the same output) and surjective (every output is reached). In Set, bijections are exactly the morphisms that can be "undone" — given any output, you can trace back to exactly one input. The categorical definition of an **isomorphism** generalizes this idea: a morphism f: A → B is an isomorphism if there exists a morphism g: B → A such that g∘f = id_A and f∘g = id_B. The morphism g is the **inverse** of f. This definition captures "undoability" purely in terms of composition and identities, without mentioning elements, injectivity, or surjectivity.

The power of this definition is that it unifies "sameness" across every mathematical structure. In **Set**, an isomorphism is a bijection — the two sets have the same cardinality and their elements can be matched one-to-one. In **Grp** (groups), an isomorphism is a bijective group homomorphism — both the structure (multiplication table) and the underlying set are the same up to relabeling. In **Top** (topological spaces), an isomorphism is a **homeomorphism**: a continuous bijection whose inverse is also continuous. Note that a continuous bijection need not be a homeomorphism — the inverse must *also* be continuous. This is why "bijective morphism" and "isomorphism" diverge in categories where morphisms carry structure beyond set-maps.

In a **poset category** (where there is at most one morphism a → b, representing a ≤ b), the only isomorphisms are the identity morphisms. If a ≤ b and b ≤ a, then a = b, so the only way to have both f: a → b and g: b → a is when a and b are the same object. This example makes an important point: isomorphisms are a property of the *entire categorical structure*, not just of the underlying sets. Two objects can be set-theoretically distinct but categorically isomorphic, or set-theoretically bijectable but not categorically isomorphic.

A key theorem: the inverse g of an isomorphism f is unique. If h also satisfies h∘f = id and f∘h = id, then h = h∘id = h∘(f∘g) = (h∘f)∘g = id∘g = g. This uniqueness means that "f⁻¹" is well-defined notation. In practice, to show f is an isomorphism, you exhibit an explicit inverse and verify the two composition equations — there is no shortcut from bijectivity alone except in particularly well-behaved categories (like Set). Isomorphisms are the categorical standard for "the same structure" and underlie equivalences of categories, universal properties, and the entire language of categorical equivalence that pervades modern mathematics.
