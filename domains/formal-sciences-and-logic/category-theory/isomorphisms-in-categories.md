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
stage: expert
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

## Questions

```yaml
- question: "Let f: X → Y be a continuous bijection between topological spaces. Is f necessarily an isomorphism in the category Top?"
  type: multiple-choice
  options:
    - "Yes — a bijective morphism is always an isomorphism in any category"
    - "Yes — continuity plus bijectivity is sufficient for a homeomorphism"
    - "No — f is an isomorphism only if its inverse f⁻¹ is also continuous"
    - "No — only surjective maps are isomorphisms in Top"
  answer: 2
  explanation: "This is the canonical example showing that 'bijective morphism' ≠ 'isomorphism' outside Set. A homeomorphism requires f to be a continuous bijection *whose inverse is also continuous*. A standard counterexample: let f: [0,1) → S¹ be the map f(t) = e^{2πit}. This is a continuous bijection, but f⁻¹ is not continuous (the preimage of an open arc near f(0) is not open in [0,1)). So f is bijective and continuous but not a homeomorphism — not an isomorphism in Top."

- question: "In a poset category where objects are elements of a partially ordered set and there is a unique morphism a → b whenever a ≤ b, which morphisms are isomorphisms?"
  type: multiple-choice
  options:
    - "All morphisms — since there is at most one morphism between any two objects, each morphism is trivially invertible"
    - "Only identity morphisms — because if a ≤ b and b ≤ a then a = b, so both morphisms exist only when they are the same object"
    - "No morphisms — posets have no invertible structure"
    - "Any morphism a → b where a and b are comparable elements"
  answer: 1
  explanation: "For f: a → b to be an isomorphism, we need g: b → a such that g∘f = idₐ and f∘g = id_b. In the poset category, a morphism b → a exists only if b ≤ a. Combined with a ≤ b, antisymmetry gives a = b. So the only isomorphisms are identity morphisms (a = b), where the morphism is the identity. This shows that isomorphisms capture the categorical notion of 'the same,' and in a poset, two distinct elements are never 'the same' even if they are comparable."

- question: "The inverse of an isomorphism f: A → B, when it exists, is unique."
  type: true-false
  answer: true
  explanation: "Suppose g and h are both inverses of f, meaning g∘f = idₐ, f∘g = id_B, h∘f = idₐ, f∘h = id_B. Then: h = h∘id_B = h∘(f∘g) = (h∘f)∘g = idₐ∘g = g. The proof uses only associativity of composition and the identity laws — the axioms of any category. This uniqueness is what makes the notation f⁻¹ well-defined."

- question: "In any category, a morphism that is bijective on the underlying sets of objects is an isomorphism."
  type: true-false
  answer: false
  explanation: "This is only true in Set. In other categories, morphisms carry additional structure, and the inverse must preserve that structure. In Top, a bijective continuous map need not have a continuous inverse (see homeomorphism counterexample). In a poset category, bijectivity between underlying sets is not even the relevant concept — morphisms represent order relations, not set-maps. The categorical definition of isomorphism — existence of a two-sided inverse in the category — is the correct standard, and it requires the inverse to be a morphism in the same category."

- question: "Why isn't bijectivity of the underlying set-function sufficient to guarantee an isomorphism in all categories? Give an example where they come apart."
  type: short-answer
  answer: "Morphisms in a category can carry structure beyond being set-maps. An isomorphism requires a two-sided inverse *that is itself a valid morphism in the category* — it must preserve whatever structure the morphisms represent. In Top, morphisms are continuous maps, so the inverse must also be continuous. A continuous bijection whose inverse is discontinuous is not an isomorphism even though the underlying set-map has an inverse. Example: f: [0,1) → S¹, f(t) = e^{2πit} is a continuous bijection but not a homeomorphism."
  explanation: "The key insight is that 'isomorphism' is a *categorical* notion, defined by composition equations g∘f = id and f∘g = id in the given category. The inverse g must itself be a morphism — it must satisfy the category's requirements on morphisms. Bijectivity only guarantees a set-theoretic inverse exists; it says nothing about whether that inverse is a valid morphism. This is why the categorical definition, which only mentions composition and identities, is more fundamental than any element-based notion."
```

## Explainer

You already know what a bijection is: a function that is both injective (no two inputs give the same output) and surjective (every output is reached). In Set, bijections are exactly the morphisms that can be "undone" — given any output, you can trace back to exactly one input. The categorical definition of an **isomorphism** generalizes this idea: a morphism f: A → B is an isomorphism if there exists a morphism g: B → A such that g∘f = id_A and f∘g = id_B. The morphism g is the **inverse** of f. This definition captures "undoability" purely in terms of composition and identities, without mentioning elements, injectivity, or surjectivity.

The power of this definition is that it unifies "sameness" across every mathematical structure. In **Set**, an isomorphism is a bijection — the two sets have the same cardinality and their elements can be matched one-to-one. In **Grp** (groups), an isomorphism is a bijective group homomorphism — both the structure (multiplication table) and the underlying set are the same up to relabeling. In **Top** (topological spaces), an isomorphism is a **homeomorphism**: a continuous bijection whose inverse is also continuous. Note that a continuous bijection need not be a homeomorphism — the inverse must *also* be continuous. This is why "bijective morphism" and "isomorphism" diverge in categories where morphisms carry structure beyond set-maps.

In a **poset category** (where there is at most one morphism a → b, representing a ≤ b), the only isomorphisms are the identity morphisms. If a ≤ b and b ≤ a, then a = b, so the only way to have both f: a → b and g: b → a is when a and b are the same object. This example makes an important point: isomorphisms are a property of the *entire categorical structure*, not just of the underlying sets. Two objects can be set-theoretically distinct but categorically isomorphic, or set-theoretically bijectable but not categorically isomorphic.

A key theorem: the inverse g of an isomorphism f is unique. If h also satisfies h∘f = id and f∘h = id, then h = h∘id = h∘(f∘g) = (h∘f)∘g = id∘g = g. This uniqueness means that "f⁻¹" is well-defined notation. In practice, to show f is an isomorphism, you exhibit an explicit inverse and verify the two composition equations — there is no shortcut from bijectivity alone except in particularly well-behaved categories (like Set). Isomorphisms are the categorical standard for "the same structure" and underlie equivalences of categories, universal properties, and the entire language of categorical equivalence that pervades modern mathematics.
