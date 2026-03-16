---
id: projective-objects
title: Projective Objects and Projective Covers
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: additive-categories
  type: hard
- id: free-objects
  type: soft
builds-toward:
- derived-functors
- homological-dimension-intro
tags:
- homological-algebra
- universal-properties
- lifts
stage: advanced
status: draft
---

# Projective Objects and Projective Covers

## Core Idea
An object P is projective if Hom(P, −) preserves epimorphisms, equivalently, if every morphism P → C/B lifts to a morphism P → C. Projectives are dual to injectives and generalize free modules. In Module categories, projectives are direct summands of free modules. Every object has a projective cover, a surjection from a projective object with 'minimal kernel'.

## Explainer

From your study of free objects, you know that free modules have a remarkable property: given any surjection M → N and any map F → N from a free module F, there exists a map F → M that makes the diagram commute — the map can always be "lifted." **Projective objects** are defined by exactly this lifting property, generalized to arbitrary additive or abelian categories without requiring the object to be free in any literal sense.

The definition is this: an object P is **projective** if for every epimorphism e: C ↠ B and every morphism f: P → B, there exists a morphism f̃: P → C such that e ∘ f̃ = f. The map f̃ is the lift — it reaches through the surjection and lands in the "larger" object C rather than the quotient B. Equivalently, the functor **Hom(P, −)** preserves epimorphisms: whenever C → B is surjective, the induced map Hom(P, C) → Hom(P, B) is also surjective. This is the categorical dual of the definition of **injective objects**, where it is Hom(−, I) that preserves monomorphisms. Projective and injective objects are mirror images — the duality of "surjections lift in" versus "injections extend out."

In the category of R-modules, projective modules are precisely the **direct summands of free modules**: M is projective if and only if there exists a module N such that M ⊕ N is free. Over a field, every module is free and hence projective. Over ℤ (a principal ideal domain), every projective module is in fact free — the two notions coincide for PIDs. Over more general rings, projective-but-not-free modules exist and are geometrically meaningful. The finitely generated projective modules over the ring of continuous functions on a compact space are exactly the **vector bundles** over that space (Serre-Swan theorem). A vector bundle that becomes trivial when you add a trivial bundle is algebraically a projective module that becomes free when summed with a free module — the projective condition captures stable triviality.

The **projective cover** of an object M is a surjection P ↠ M from a projective object P such that the kernel is **superfluous** — removing it cannot produce a smaller projective surjecting onto M. Projective covers are the minimal projective objects that map onto M, and they provide canonical **minimal projective resolutions**: exact sequences 0 ← M ← P₀ ← P₁ ← P₂ ← ··· where each Pᵢ is projective and as small as possible. These resolutions are the raw material for **derived functors** such as Tor and Ext — which measure how far a functor deviates from exactness and encode deep information about the module structure of a ring. Not every abelian category has projective covers (sheaves often lack them), but in the module categories where they exist, minimal projective resolutions are the canonical tool for homological computation.
