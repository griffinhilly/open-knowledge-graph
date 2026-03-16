---
id: yoneda-lemma
title: The Yoneda Lemma
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: representable-functors
  type: hard
- id: natural-transformations
  type: hard
- id: functor-categories
  type: soft
- id: full-and-faithful-functors
  type: soft
- id: limits-and-colimits
  type: soft
- id: functions-and-function-properties
  type: soft
- id: composition-of-functions
  type: soft
- id: function-composition
  type: soft
- id: set-operations
  type: soft
- id: functions-and-mappings-formal
  type: soft
- id: equivalence-relations
  type: soft
- id: function-composition-and-inverses
  type: soft
builds-toward:
- adjoint-functors
- equivalence-of-categories
tags:
- Yoneda lemma
- Yoneda embedding
- natural transformations
- presheaf
- representability
stage: advanced
status: validated
---
# The Yoneda Lemma

## Core Idea
The Yoneda lemma states that for any functor F: C → Set and any object A in C, there is a bijection Nat(Hom(A,-), F) ≅ F(A) that is natural in both A and F. This means natural transformations from a representable functor to any functor F are completely determined by a single element of F(A). The Yoneda embedding A ↦ Hom(A,-) is a fully faithful functor from C to [C^op, Set], showing every category embeds into a presheaf category and that an object is completely determined by how morphisms map into it from all other objects.

## How It's Best Learned
Work through the proof step by step: given a natural transformation η: Hom(A,-) ⇒ F, evaluate at A and apply to id_A to get an element of F(A). Verify this map is an inverse to the map F(A) → Nat(Hom(A,-), F) given by the Yoneda construction. Appreciate the slogan 'an object is determined by its relationships with all other objects'.

## Common Misconceptions
- The Yoneda lemma is not merely a technical result; it is a fundamental philosophical principle of category theory—objects are determined by their morphisms.
- The bijection Nat(Hom(A,-), F) ≅ F(A) is not a set isomorphism requiring special conditions; it holds for all locally small categories.
- The Yoneda embedding is contravariant when using Hom(-,A); be careful about which version (covariant vs. contravariant) is being used.

## Questions

```yaml
- question: "If F: C → Set is any functor and A is an object in C, the Yoneda lemma gives a bijection between Nat(Hom(A,-), F) and which set?"
  type: multiple-choice
  options: ["The set of all functors from C to Set", "The set F(A)", "The set of morphisms from A to itself", "The set of all objects in C"]
  answer: 1
  explanation: "The Yoneda lemma states Nat(Hom(A,-), F) ≅ F(A). Any natural transformation η: Hom(A,-) ⇒ F is uniquely determined by the image of id_A under the component η_A: Hom(A,A) → F(A). This single element of F(A) encodes the entire natural transformation — the rest is forced by naturality."

- question: "The Yoneda lemma's bijection Nat(Hom(A,-), F) ≅ F(A) only holds when F is itself a representable functor."
  type: true-false
  answer: false
  explanation: "The bijection holds for *any* functor F: C → Set — representability of F is not required. If F happens to be representable (F ≅ Hom(B,-) for some object B), that gives additional structure, but the Yoneda lemma applies universally to all functors into Set. This generality is precisely what makes it so powerful."

- question: "What does it mean for the Yoneda embedding to be fully faithful, and why is this philosophically significant for category theory?"
  type: short-answer
  answer: "A functor is fully faithful when it is bijective on hom-sets. The Yoneda embedding being fully faithful means morphisms A → B in C correspond exactly to natural transformations Hom(A,-) ⇒ Hom(B,-). Philosophically, this encodes the principle that an object is completely determined by its relationships to all other objects — you lose no information about C by studying it through its representable functors."
  explanation: "Full faithfulness is the precise statement that C embeds into the presheaf category without loss of information. Two objects that look the same from the outside (same representable functor) must be isomorphic inside C. This 'objects are determined by their morphisms' principle is one of the deepest ideas in category theory and motivates much of topos theory and sheaf theory."
```

## Explainer

To understand the Yoneda lemma, start with what a natural transformation from Hom(A,-) to F actually is. Hom(A,-) is a functor that sends each object X to the set of morphisms A → X. A natural transformation η: Hom(A,-) ⇒ F assigns to each object X a function η_X: Hom(A,X) → F(X), subject to naturality squares commuting for every morphism in C. The question is: how much freedom do you have in choosing such an η?

The Yoneda lemma gives a surprising answer: none at all, once you fix one thing. The naturality conditions are so rigid that the entire natural transformation η is completely determined by a single element of F(A) — specifically, by η_A(id_A), the image of the identity morphism on A. Every component η_X is then forced by the functoriality of F and the naturality condition. This means the (potentially enormous) collection of all natural transformations Nat(Hom(A,-), F) is in bijection with the set F(A), which may be much smaller and more concrete.

The bijection goes both ways. Given any element s ∈ F(A), you construct a natural transformation η^s by defining η^s_X(f) = F(f)(s) for any morphism f: A → X. Naturality is automatic from the functoriality of F. The proof that these two constructions are inverse to each other is a short diagram chase that repays close reading — following id_A through both directions reveals why the whole argument works.

The Yoneda embedding takes this further. The assignment A ↦ Hom(A,-) defines a functor from C^op into the functor category [C, Set]. The Yoneda lemma implies this functor is fully faithful: morphisms between objects in C correspond exactly to natural transformations between their representable functors. This means C embeds into [C^op, Set] without losing any structural information — every object is completely determined by how morphisms map out of it into every other object. The slogan is: **an object is its relationships**.

This principle has far-reaching consequences. Representability becomes a way to define objects by universal properties rather than by internal construction. Limits, colimits, and adjunctions can all be characterized Yoneda-style. In more advanced contexts, the Yoneda lemma underlies the theory of sheaves, stacks, and the entire approach of algebraic geometry via functor-of-points. It is not an isolated lemma — it is the lens through which category theory sees everything.
