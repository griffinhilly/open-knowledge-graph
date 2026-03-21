---
id: functor-composition
title: Composition of Functors and Functor Equations
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: functors
  type: hard
builds-toward:
- functor-categories
- natural-transformations
tags:
- functors
- categorical-structure
- composition
stage: advanced
status: draft
---

# Composition of Functors and Functor Equations

## Core Idea
Functors compose: given F: A → B and G: B → C, their composition GF: A → C is defined pointwise on objects and morphisms. Functor composition is associative with identity functors as units. This makes categories into a 2-category where objects are categories, 1-morphisms are functors, and 2-morphisms are natural transformations.

## Questions

```yaml
- question: "Given functors F: A → B, G: B → C, and H: C → D, which of the following correctly describes the relationship between (HG)F and H(GF)?"
  type: multiple-choice
  options:
    - "They are naturally isomorphic but not necessarily equal as functors"
    - "They are strictly equal as functors — associativity of functor composition holds on the nose"
    - "They are equal only when all categories involved are small"
    - "They are equal only when F, G, and H are all full and faithful"
  answer: 1
  explanation: "Functor composition is strictly associative — (HG)F = H(GF) as literal equalities, not merely up to natural isomorphism. This follows because functors are just functions on objects and morphisms satisfying extra laws, and composition of functions is strictly associative. No coherence isomorphism is needed. This strict equality (as opposed to 'up to isomorphism') is precisely what gives Cat the structure of a strict 2-category rather than a bicategory."

- question: "To verify that the composite GF: A → C preserves composition — that (GF)(g ∘ f) = (GF)(g) ∘ (GF)(f) — the key step is:"
  type: multiple-choice
  options:
    - "Showing that G and F have compatible object assignments on shared objects"
    - "Applying F's preservation of composition to get F(g ∘ f) = F(g) ∘ F(f), then applying G's preservation of composition to that result"
    - "Showing that GF is injective on morphisms"
    - "Applying the naturality condition for the identity natural transformation"
  answer: 1
  explanation: "The proof chains the two functor laws: first apply F's composition law to rewrite F(g ∘ f) = F(g) ∘ F(f), then apply G's composition law to rewrite G(F(g) ∘ F(f)) = G(F(g)) ∘ G(F(f)) = (GF)(g) ∘ (GF)(f). The proof is two applications of the functor axiom in sequence — no other properties of F or G are needed. This pattern of 'apply the inner functor law, then the outer' recurs throughout category theory."

- question: "Functor composition is associative only up to natural isomorphism — that is, (HG)F and H(GF) are naturally isomorphic but may not be literally equal."
  type: true-false
  answer: false
  explanation: "Functor composition is strictly associative: (HG)F = H(GF) as an equality of functors, not merely an isomorphism. This distinguishes Cat (the category of small categories with strict associativity) from a bicategory (where associativity holds only up to coherent isomorphism). The strict equality holds because functor composition is defined pointwise via function composition, which is itself strictly associative."

- question: "The identity functor id_A: A → A satisfies F ∘ id_A = F = id_B ∘ F for any functor F: A → B, making it a strict unit for composition."
  type: true-false
  answer: true
  explanation: "The identity functor sends every object and every morphism to itself. Pre-composing any functor F: A → B with id_A gives a functor that maps each object a to F(id_A(a)) = F(a), and each morphism f to F(id_A(f)) = F(f) — exactly F itself. Similarly for post-composing with id_B. These equalities hold strictly, not just up to isomorphism, for the same reason associativity holds strictly."

- question: "Explain why the strict (not merely 'up to isomorphism') associativity of functor composition is significant for the structure of Cat as a 2-category."
  type: short-answer
  answer: "In a strict 2-category, the composition of 1-morphisms (here: functors) must be strictly associative and have strict units — actual equalities, not just coherent isomorphisms. Cat satisfies this because functor composition is defined via pointwise function composition, which is strictly associative. If associativity held only up to natural isomorphism, Cat would be a bicategory (weak 2-category), requiring additional coherence data (associator and unitor isomorphisms satisfying pentagon and triangle identities). The strict equality simplifies the theory: proofs about functor composition can treat parenthesization as irrelevant rather than tracking coherence isomorphisms. This strictness is the algebraic foundation for treating Cat as a category of categories, with functors as its morphisms."
  explanation: "The distinction between strict and weak 2-categories becomes important when working with structures like monoidal categories or 2-functors, where weakening associativity introduces nontrivial coherence requirements. Understanding that Cat is strict clarifies when such coherence data is truly needed versus when it can be suppressed."
```

## Explainer

You already know what a functor is: a structure-preserving map between categories that sends objects to objects, morphisms to morphisms, and respects identity and composition. Functor composition asks the natural follow-up question: if F maps category A to B and G maps B to C, can we compose them to get a functor from A to C? The answer is yes, and the construction is exactly what you'd expect.

The **composite functor** GF: A → C is defined pointwise: on any object a ∈ A, (GF)(a) = G(F(a)); on any morphism f: a → a' in A, (GF)(f) = G(F(f)). That GF is actually a functor — not just a pair of assignments — requires checking that it preserves identities and composition. Preservation of identities: (GF)(id_a) = G(F(id_a)) = G(id_{Fa}) = id_{G(Fa)} = id_{(GF)(a)}, using the functor laws for F then G in sequence. Preservation of composition: (GF)(g ∘ f) = G(F(g ∘ f)) = G(F(g) ∘ F(f)) = G(F(g)) ∘ G(F(f)) = (GF)(g) ∘ (GF)(f). Both proofs are just applications of the functor laws twice over.

**Associativity** of functor composition follows immediately because composition of functions is associative, and functors are just functions on objects and morphisms that satisfy extra laws. For three composable functors F, G, H, the equality (HG)F = H(GF) holds strictly — no natural isomorphism is needed, the composites are literally equal. The **identity functor** id_A: A → A sends every object and morphism to itself. It acts as an identity for composition: F ∘ id_A = F = id_B ∘ F for any F: A → B.

This is where the **2-category** structure of **Cat** enters. In an ordinary category, you have objects and morphisms between objects. In a 2-category, you additionally have **2-morphisms** between morphisms — maps between maps. For **Cat** (the category of small categories), objects are categories, 1-morphisms are functors, and 2-morphisms are **natural transformations** between functors. Natural transformations can be composed both horizontally (composing with another natural transformation between adjacent functor pairs) and vertically (composing two natural transformations between the same pair of functors). Functor composition is precisely horizontal composition at the level of 1-morphisms, and the coherence conditions for 2-categories ensure that horizontal and vertical compositions interact consistently. Understanding this structure is the foundation for the upcoming topics on natural transformations and functor categories, where the interplay between these two composition operations becomes central.
