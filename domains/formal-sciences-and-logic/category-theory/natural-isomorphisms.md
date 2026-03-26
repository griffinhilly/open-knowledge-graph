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
- id: functor-composition
  type: soft
- id: two-categories-and-weak-functors
  type: soft
builds-toward:
- equivalence-of-categories
- adjoint-functors
tags:
- functors
- equivalence
- natural-transformations
stage: expert
status: validated
---
# Natural Isomorphisms Between Functors

## Core Idea
A natural isomorphism between functors F, G: C → D is a natural transformation α: F ⇒ G where each component α_c: F(c) → G(c) is an isomorphism. Natural isomorphisms express that two functors are 'the same up to isomorphism' in a way respecting naturality. They form the 2-morphisms in the 2-category Cat.

## Questions

```yaml
- question: "Every finite-dimensional vector space V is isomorphic to both its dual V* and its double dual V**. Which isomorphism is natural, and why?"
  type: multiple-choice
  options:
    - "Both are natural — all isomorphisms between spaces of the same dimension are natural"
    - "Neither is natural — categorical naturality requires a group structure, not just vector space structure"
    - "V ≅ V** is natural via the evaluation map; V ≅ V* is not natural because it requires a basis choice"
    - "V ≅ V* is natural because duals are a canonical construction; V ≅ V** requires choosing an evaluation point"
  answer: 2
  explanation: "The isomorphism V → V** given by ev_V(v)(φ) = φ(v) requires no choices — it works the same way for every vector space and every linear map, and the naturality square commutes for any f: V → W. By contrast, the isomorphism V → V* sends each basis vector to its dual basis functional, which requires first choosing a basis. Different basis choices give different isomorphisms. This is precisely what 'natural' means in category theory: canonical, requiring no arbitrary choices. The V ≅ V* isomorphism exists but varies with convention."

- question: "To verify that a natural transformation α: F ⇒ G is a natural isomorphism, what must you do?"
  type: multiple-choice
  options:
    - "Find a single morphism α^{-1}: G ⇒ F at the level of entire functors, not just components"
    - "Find an inverse isomorphism α_c^{-1}: G(c) → F(c) for each object c; naturality of the inverses is then automatic"
    - "Verify that F and G are isomorphic as objects in the functor category, which requires a separate computation"
    - "Find an inverse for each α_c and independently verify that the collection {α_c^{-1}} satisfies the naturality squares"
  answer: 1
  explanation: "The key convenience of natural isomorphisms is that you work componentwise. For each object c, find an inverse isomorphism α_c^{-1}: G(c) → F(c). Once you have these and know α is a natural transformation with each α_c an isomorphism, the collection {α_c^{-1}} automatically forms a natural transformation G ⇒ F — you do not need to separately verify naturality of the inverses. This follows from the fact that naturality squares for α can be 'inverted' using the invertibility of each component."

- question: "If α: F ⇒ G is a natural isomorphism, then the collection of inverses {α_c^{-1}} automatically assembles into a natural transformation G ⇒ F."
  type: true-false
  answer: true
  explanation: "This is a key feature of natural isomorphisms. If α is natural and each α_c is an isomorphism, then the inverses α_c^{-1} satisfy the naturality condition for the transformation G ⇒ F automatically. Naturality of α says α_d ∘ F(f) = G(f) ∘ α_c for any morphism f: c → d. Since each component is invertible, we can apply α_c^{-1} on the right and α_d^{-1} on the left to obtain the naturality square for the inverse transformation. You get naturality of α^{-1} for free."

- question: "Assigning an isomorphism between F(c) and G(c) for nearly every object c in C is sufficient to make α a natural isomorphism between functors F and G."
  type: true-false
  answer: false
  explanation: "Having an isomorphism at each component is necessary but not sufficient. The collection {α_c} must also be natural — meaning for every morphism f: c → d in C, the square α_d ∘ F(f) = G(f) ∘ α_c must commute. Without naturality, you merely have a collection of unrelated isomorphisms, not a coherent relationship between functors. The naturality condition is what ensures the identification 'respects the structure of C and D' and makes F and G categorically interchangeable."

- question: "What does it mean for two functors to be naturally isomorphic, and how does this differ from having isomorphisms between their values at each object?"
  type: short-answer
  answer: "Two functors F, G: C → D are naturally isomorphic if there is a natural transformation α: F ⇒ G where each component α_c: F(c) → G(c) is an isomorphism, and these components commute with all morphisms in C. Having isomorphisms at each object (without naturality) only says the values are individually related; naturality ensures the isomorphisms are coherent — they transform consistently with the structure of C. Naturally isomorphic functors are categorically interchangeable: any categorical statement about F applies equally to G."
  explanation: "The distinction captures what 'canonical' means in mathematics. A choice of isomorphisms at each object might depend on arbitrary conventions (like a choice of basis), giving a different isomorphism in each context. Naturality rules this out: the isomorphisms must fit together consistently with every morphism, making them independent of choices. This is why 'naturally isomorphic' is the correct notion of sameness for functors, just as 'isomorphic' is the correct notion for objects."
```

## Explainer

You know that a **natural transformation** α: F ⇒ G assigns to each object c in C a morphism α_c: F(c) → G(c), and that this assignment is natural — meaning it commutes with every morphism in C. A **natural isomorphism** is simply a natural transformation where every component α_c happens to be an isomorphism. This sounds like a small extra condition, but its consequences are substantial: it means F and G are not just vaguely "similar" but interchangeable in any categorical context that respects the structure of C and D.

The standard example to build intuition: in linear algebra, the double dual V** of a finite-dimensional vector space is isomorphic to V. But there are actually two different things going on. There is a natural isomorphism η: Id ⇒ (−)** where η_V: V → V** is the evaluation map ev_V(v)(φ) = φ(v). This isomorphism is **natural** because for any linear map f: V → W, the square η_W ∘ f = f** ∘ η_V commutes. Contrast this with the isomorphism between V and its dual V*: this exists for finite-dimensional spaces (they have the same dimension), but the isomorphism depends on a choice of basis — it is not natural in the categorical sense. Natural isomorphisms capture the precise meaning of "canonical" in mathematics: an identification that requires no arbitrary choices.

Checking that a natural transformation is a natural isomorphism can be done componentwise: you do not need to find a single inverse map between entire functors at once. Instead, find an inverse isomorphism α_c^{-1}: G(c) → F(c) for each object c, then verify that the collection {α_c^{-1}} is itself a natural transformation G ⇒ F. This splits the verification into manageable pieces. Importantly, naturality of α together with the fact that each α_c is an isomorphism guarantees that the inverses also assemble naturally — you get naturality of α^{-1} for free.

Natural isomorphisms appear throughout mathematics as the correct notion of "sameness" for functors, just as isomorphisms are the correct notion of sameness for objects. Two functors F and G that are naturally isomorphic carry exactly the same categorical information: any construction or theorem stated in purely categorical language about F applies equally to G. This is the key to understanding **equivalence of categories** (your next topic): two categories are equivalent if there exist functors between them that are inverse up to natural isomorphism. The condition is strictly weaker than having an isomorphism of categories (a functor with a strict inverse), but it is the right condition for capturing when two categories have the same structure — it correctly identifies, for instance, that finite sets and finite-dimensional vector spaces over a field have "the same categorical skeleton" in appropriate senses, even though they are very different as concrete mathematical objects.


