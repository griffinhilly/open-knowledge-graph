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

## Explainer

You already know what a functor is: a structure-preserving map between categories that sends objects to objects, morphisms to morphisms, and respects identity and composition. Functor composition asks the natural follow-up question: if F maps category A to B and G maps B to C, can we compose them to get a functor from A to C? The answer is yes, and the construction is exactly what you'd expect.

The **composite functor** GF: A → C is defined pointwise: on any object a ∈ A, (GF)(a) = G(F(a)); on any morphism f: a → a' in A, (GF)(f) = G(F(f)). That GF is actually a functor — not just a pair of assignments — requires checking that it preserves identities and composition. Preservation of identities: (GF)(id_a) = G(F(id_a)) = G(id_{Fa}) = id_{G(Fa)} = id_{(GF)(a)}, using the functor laws for F then G in sequence. Preservation of composition: (GF)(g ∘ f) = G(F(g ∘ f)) = G(F(g) ∘ F(f)) = G(F(g)) ∘ G(F(f)) = (GF)(g) ∘ (GF)(f). Both proofs are just applications of the functor laws twice over.

**Associativity** of functor composition follows immediately because composition of functions is associative, and functors are just functions on objects and morphisms that satisfy extra laws. For three composable functors F, G, H, the equality (HG)F = H(GF) holds strictly — no natural isomorphism is needed, the composites are literally equal. The **identity functor** id_A: A → A sends every object and morphism to itself. It acts as an identity for composition: F ∘ id_A = F = id_B ∘ F for any F: A → B.

This is where the **2-category** structure of **Cat** enters. In an ordinary category, you have objects and morphisms between objects. In a 2-category, you additionally have **2-morphisms** between morphisms — maps between maps. For **Cat** (the category of small categories), objects are categories, 1-morphisms are functors, and 2-morphisms are **natural transformations** between functors. Natural transformations can be composed both horizontally (composing with another natural transformation between adjacent functor pairs) and vertically (composing two natural transformations between the same pair of functors). Functor composition is precisely horizontal composition at the level of 1-morphisms, and the coherence conditions for 2-categories ensure that horizontal and vertical compositions interact consistently. Understanding this structure is the foundation for the upcoming topics on natural transformations and functor categories, where the interplay between these two composition operations becomes central.
