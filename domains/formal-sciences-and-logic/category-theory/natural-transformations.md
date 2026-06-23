---
id: natural-transformations
title: Natural Transformations
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: functors
  type: hard
- id: functions-domain-codomain-range
  type: soft
- id: composition-of-functions
  type: soft
- id: functions-and-function-properties
  type: hard
- id: function-composition-and-inverses
  type: soft
- id: function-composition-and-inverses
  type: soft
- id: commutative-diagrams-and-composition
  type: hard
- id: commutative-diagrams-in-categories
  type: hard
- id: functor-composition
  type: soft
builds-toward:
- functor-categories
- yoneda-lemma
- adjoint-functors
- monads-in-category-theory
tags:
- natural transformation
- naturality square
- morphisms of functors
stage: advanced
status: validated
---

# Natural Transformations

## Core Idea
A natural transformation η: F ⇒ G between functors F, G: C → D assigns to each object A in C a morphism η_A: F(A) → G(A) in D such that for every morphism f: A → B in C, the naturality square commutes: η_B ∘ F(f) = G(f) ∘ η_A. Natural transformations are the morphisms between functors, making them the 2-morphisms of the 2-category Cat. The concept of 'naturality' formalizes the intuition that a construction is canonical or independent of arbitrary choices—the determinant, double dual embedding, and many algebraic maps are natural transformations.

## How It's Best Learned
Verify that the double dual embedding V → V** for vector spaces (sending v to the evaluation map ev_v) is natural by drawing and checking the naturality square for an arbitrary linear map T: V → W. Contrast with the non-natural isomorphism V ≅ V* (which requires choosing a basis).

## Common Misconceptions
- Naturality is not automatic from having the right type signature; many component-wise maps fail the naturality square.
- A natural transformation is not a single morphism but a whole family of morphisms, one per object, satisfying coherence conditions.
- Natural isomorphisms (where every η_A is an isomorphism) are stronger than just having isomorphic functors pointwise.

## Questions

```yaml
- question: "The naturality square for η: F ⇒ G at a morphism f: A → B requires which condition to hold?"
  type: multiple-choice
  options: ["η_A ∘ F(f) = G(f) ∘ η_B", "η_B ∘ F(f) = G(f) ∘ η_A", "F(f) ∘ η_A = η_A ∘ G(f)", "G(f) = F(f) for all f"]
  answer: 1
  explanation: "The naturality condition is η_B ∘ F(f) = G(f) ∘ η_A. Reading left to right: going from F(A) to F(B) via F(f) and then applying η_B must equal applying η_A first (from F(A) to G(A)) and then going from G(A) to G(B) via G(f). The square commutes when both paths — 'apply η after F' and 'apply G before η' — give the same composite morphism."

- question: "Any family of morphisms {φ_A: F(A) → G(A)} indexed by objects of C is automatically a natural transformation as long as each φ_A has the correct type."
  type: true-false
  answer: false
  explanation: "Having the correct type signature is necessary but not sufficient. The naturality condition — that η_B ∘ F(f) = G(f) ∘ η_A for every morphism f: A → B — must also be verified. Many 'obvious' component-wise maps fail this coherence check. For example, the isomorphism V ≅ V* (dual vector space) that requires choosing a basis is not natural: applying it to a linear map T and then dualizing does not commute with dualizing first and then applying T."

- question: "The double dual embedding V → V** is considered 'natural' while the isomorphism V ≅ V* is not, even though both are isomorphisms of vector spaces of the same dimension. What makes the difference?"
  type: short-answer
  answer: "The map V → V** (sending v to the evaluation functional ev_v: φ ↦ φ(v)) is defined without choosing a basis and commutes with every linear map T: the naturality square holds for all T. In contrast, V ≅ V* requires picking an inner product or a basis to define the isomorphism, and the resulting map changes when the basis changes — it does not commute uniformly with all linear maps."
  explanation: "Naturality formalizes 'canonical' or 'basis-free': a natural transformation is the same construction applied uniformly across all objects, independent of arbitrary choices. The V → V** map needs nothing extra because evaluation is intrinsically defined. The V ≅ V* isomorphism is not intrinsic — it depends on external data (a bilinear form or basis), so it cannot satisfy the naturality square for all morphisms in a uniform way."
```

## Explainer

You have already seen that a functor F: C → D is a structure-preserving map between categories — it sends objects to objects and morphisms to morphisms while respecting composition and identities. A natural transformation takes the next step: it is a map between two functors that themselves go between the same pair of categories. If F and G are both functors from C to D, a natural transformation η: F ⇒ G gives, for each object A in C, a morphism η_A: F(A) → G(A) in D. These components must fit together coherently across all morphisms of C.

The coherence condition is the naturality square. For any morphism f: A → B in C, the square formed by F(f), G(f), η_A, and η_B must commute: η_B ∘ F(f) = G(f) ∘ η_A. Think of it this way: you can either first apply F to f (getting a morphism in D between the F-images) and then translate from the F-image to the G-image via η_B, or you can first translate at A via η_A and then apply G to f. The naturality condition says these two paths yield the same morphism. This is a genuine constraint — many component-wise maps of the right type fail it.

The canonical example is the double dual embedding. For a finite-dimensional vector space V, define η_V: V → V** by η_V(v) = ev_v, where ev_v(φ) = φ(v). This map is defined purely in terms of evaluation — no basis, no inner product, no arbitrary choices. For any linear map T: V → W, the naturality square commutes: T** ∘ η_V = η_W ∘ T. Contrast this with the isomorphism V ≅ V* (dual space). Such an isomorphism exists and V and V* have the same dimension, but constructing a specific one requires choosing a basis or an inner product. The resulting map fails the naturality square for arbitrary T because the choice of basis on V and W may not be compatible. The difference is exactly what "natural" means: the double dual map is canonical; the V ≅ V* map is not.

Natural transformations are important partly because they are the morphisms of functor categories: the collection of all functors from C to D forms a category, denoted [C, D] or D^C, where objects are functors and morphisms are natural transformations. This is the beginning of higher-dimensional category theory. Natural transformations also compose: given η: F ⇒ G and ε: G ⇒ H, the composite ε ∘ η: F ⇒ H is defined component-wise by (ε ∘ η)_A = ε_A ∘ η_A, and the naturality squares paste together correctly.

The concept of a natural isomorphism — a natural transformation where every component η_A is an isomorphism — formalizes the idea that two functors are "the same up to canonical isomorphism." This is subtly stronger than just knowing F(A) ≅ G(A) for each A separately; a natural isomorphism guarantees those isomorphisms are compatible with all morphisms. Many fundamental equivalences in algebra and topology are natural isomorphisms, and recognizing them as such is often the key to transferring results from one context to another.

