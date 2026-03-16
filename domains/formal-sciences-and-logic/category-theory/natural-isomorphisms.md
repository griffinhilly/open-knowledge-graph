---
id: natural-isomorphisms
title: Natural Isomorphisms Between Functors
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: natural-transformations
  type: hard
- id: functors
  type: hard
builds-toward:
- equivalence-of-categories
- adjoint-functors
tags:
- functors
- equivalence
- natural-transformations
stage: advanced
status: draft
---

# Natural Isomorphisms Between Functors

## Core Idea
A natural isomorphism between functors F, G: C → D is a natural transformation α: F ⇒ G where each component α_c: F(c) → G(c) is an isomorphism. Natural isomorphisms express that two functors are 'the same up to isomorphism' in a way respecting naturality. They form the 2-morphisms in the 2-category Cat.

## Explainer

You know that a **natural transformation** α: F ⇒ G assigns to each object c in C a morphism α_c: F(c) → G(c), and that this assignment is natural — meaning it commutes with every morphism in C. A **natural isomorphism** is simply a natural transformation where every component α_c happens to be an isomorphism. This sounds like a small extra condition, but its consequences are substantial: it means F and G are not just vaguely "similar" but interchangeable in any categorical context that respects the structure of C and D.

The standard example to build intuition: in linear algebra, the double dual V** of a finite-dimensional vector space is isomorphic to V. But there are actually two different things going on. There is a natural isomorphism η: Id ⇒ (−)** where η_V: V → V** is the evaluation map ev_V(v)(φ) = φ(v). This isomorphism is **natural** because for any linear map f: V → W, the square η_W ∘ f = f** ∘ η_V commutes. Contrast this with the isomorphism between V and its dual V*: this exists for finite-dimensional spaces (they have the same dimension), but the isomorphism depends on a choice of basis — it is not natural in the categorical sense. Natural isomorphisms capture the precise meaning of "canonical" in mathematics: an identification that requires no arbitrary choices.

Checking that a natural transformation is a natural isomorphism can be done componentwise: you do not need to find a single inverse map between entire functors at once. Instead, find an inverse isomorphism α_c^{-1}: G(c) → F(c) for each object c, then verify that the collection {α_c^{-1}} is itself a natural transformation G ⇒ F. This splits the verification into manageable pieces. Importantly, naturality of α together with the fact that each α_c is an isomorphism guarantees that the inverses also assemble naturally — you get naturality of α^{-1} for free.

Natural isomorphisms appear throughout mathematics as the correct notion of "sameness" for functors, just as isomorphisms are the correct notion of sameness for objects. Two functors F and G that are naturally isomorphic carry exactly the same categorical information: any construction or theorem stated in purely categorical language about F applies equally to G. This is the key to understanding **equivalence of categories** (your next topic): two categories are equivalent if there exist functors between them that are inverse up to natural isomorphism. The condition is strictly weaker than having an isomorphism of categories (a functor with a strict inverse), but it is the right condition for capturing when two categories have the same structure — it correctly identifies, for instance, that finite sets and finite-dimensional vector spaces over a field have "the same categorical skeleton" in appropriate senses, even though they are very different as concrete mathematical objects.


