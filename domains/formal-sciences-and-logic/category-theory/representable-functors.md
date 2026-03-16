---
id: representable-functors
title: Representable Functors
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: functors
  type: hard
- id: natural-transformations
  type: soft
- id: opposite-categories-and-duality
  type: soft
- id: full-and-faithful-functors
  type: soft
- id: functor-categories
  type: soft
builds-toward:
- yoneda-lemma
- adjoint-functors
tags:
- representable functor
- hom-functor
- Yoneda
- presheaf
stage: advanced
status: validated
---
# Representable Functors

## Core Idea
For each object A in a locally small category C, the hom-functor Hom(A, -): C → Set sends each object B to the set of morphisms Hom(A, B) and each morphism f: B → C to post-composition with f. A functor F: C → Set is representable if it is naturally isomorphic to Hom(A, -) for some object A, called the representing object. Representability is a powerful concept: many construction functors (tensor product, free algebras, cohomology groups) are representable, and their representing objects carry universal properties.

## How It's Best Learned
Show that the forgetful functor from Grp to Set is representable by the free group on one generator ℤ: a group homomorphism ℤ → G is uniquely determined by where 1 goes, so Grp(ℤ, G) ≅ G as sets, naturally in G. Identify the representing objects for other familiar functors.

## Common Misconceptions
- Not every functor C → Set is representable; representability is a non-trivial condition checked via the Yoneda lemma.
- The representing object is unique up to unique isomorphism, not unique as a set-theoretic construction.
- The contravariant hom-functor Hom(-, A) is representable in C^op, not in C.

## Explainer

You know that a functor F: C → Set assigns a set to each object and a function to each morphism. Most functors you encounter in practice have an interesting feature: the sets F(B) can be identified with sets of morphisms in C. When this identification is natural — meaning compatible with all morphisms in C in the precise sense you learned from natural transformations — the functor is called **representable**. Representability is a way of saying "this functor is really just about morphisms out of a fixed object."

The **hom-functor** Hom(A, −): C → Set is the prototype. Fix any object A. For each object B, define Hom(A, B) to be the set of all morphisms from A to B in C. For each morphism f: B → C, define Hom(A, f) to be post-composition: send each g: A → B to f ∘ g: A → C. This construction is functorial — it respects identity morphisms and composition — and it is the canonical example of a representable functor, with representing object A. A functor F: C → Set is **representable** if there exists an object A and a natural isomorphism α: F ≅ Hom(A, −). The object A is called the **representing object** of F.

A concrete example clarifies what representability means. Consider the forgetful functor U: Grp → Set. Does there exist a group A such that group homomorphisms from A to any group G are in natural bijection with elements of G? Yes: take A = ℤ. A homomorphism φ: ℤ → G is completely determined by φ(1) ∈ G (since φ(n) = φ(1)^n by the homomorphism property), and any element g ∈ G determines a valid homomorphism by φ(1) = g. So Hom_Grp(ℤ, G) ≅ U(G) naturally in G — the forgetful functor is represented by ℤ. The "naturally in G" condition means this bijection commutes with all group homomorphisms G → G', which is exactly the naturality square you learned with natural transformations.

The power of representability is that it converts abstract functor questions into questions about morphisms in C, which are often more tractable. The **representing object** plays the role of a "universal element" — the bijection Hom(A, B) ≅ F(B) maps the identity morphism id_A ∈ Hom(A, A) to a distinguished element u ∈ F(A) with the property that every element of every F(B) is the image of u under some morphism. This universal element characterizes the representing object up to unique isomorphism, and recognizing it is the standard way to prove representability. The Yoneda lemma, which you will study next, sharpens this: natural transformations Hom(A, −) → F are in bijection with elements of F(A), giving a complete and powerful description of all representable functors.
