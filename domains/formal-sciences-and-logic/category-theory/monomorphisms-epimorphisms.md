---
id: monomorphisms-epimorphisms
title: Monomorphisms and Epimorphisms
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: categories-and-morphisms
  type: hard
builds-toward:
- additive-categories
- abelian-structure-properties
tags:
- morphisms
- universal-properties
- categorical-structure
stage: advanced
status: draft
---

# Monomorphisms and Epimorphisms

## Core Idea
Monomorphisms generalize injective functions to arbitrary categories: a morphism f: A → B is monic if whenever gf = hf, then g = h. Epimorphisms are the dual concept, generalizing surjections. In categories without a notion of elements, these abstract properties capture injectivity and surjectivity without requiring explicit set-theoretic membership.

## How It's Best Learned
Start in Set and Ring where monomorphisms are exactly injections and epimorphisms are exactly surjections. Then explore categories where these concepts diverge—for example, in rings the natural homomorphism R → R[x] is epic but not surjective.

## Common Misconceptions
Assuming monomorphisms are always injective (false in general). Thinking epimorphisms must be surjective (counterexample: R → R[x] in Ring). Assuming every morphism is either monic or epic.

## Explainer

From your study of categories and morphisms, you know that category theory abstracts mathematical structures away from their internal elements, describing objects only through their relationships — the morphisms between them. Most concepts that feel element-dependent in familiar settings (like injectivity: "no two inputs give the same output") must be reformulated in terms of morphisms to make sense in an arbitrary category. **Monomorphisms** and **epimorphisms** are the categorical versions of injective and surjective maps, and the reformulation reveals what those concepts truly mean structurally.

A morphism f: A → B is a **monomorphism** (or *monic*) if it is **left-cancellable**: for any two morphisms g, h: C → A, if f ∘ g = f ∘ h then g = h. In Set, this coincides exactly with injectivity. Here's the intuition: if f is injective, then knowing f(g(x)) = f(h(x)) for all x forces g(x) = h(x), since different inputs can't produce the same output under an injective map. The categorical definition extracts this "information-preserving" property without ever mentioning elements. A monomorphism is a morphism through which you can distinguish the domain — you cannot "compress" information passing through it. Dually, f: A → B is an **epimorphism** (or *epic*) if it is **right-cancellable**: for any g, h: B → C, if g ∘ f = h ∘ f then g = h. In Set, surjectivity ensures this: if f hits every element of B, then any two functions that agree on all outputs of f must agree everywhere on B.

The surprise is that these concepts **diverge from injectivity/surjectivity** outside of Set. In the category **Ring** (with ring homomorphisms), the inclusion ι: ℤ → ℚ is an epimorphism even though it is far from surjective. The reason: any ring homomorphism f: ℚ → R is entirely determined by f(1) (since f(p/q) = f(p)/f(q) by homomorphism axioms, and f(p) is determined by f(1)). So if g ∘ ι = h ∘ ι — meaning g and h agree on all integers — they must agree on all rationals. Right-cancellability holds, so ι is epic. Yet ℚ has elements (non-integer rationals) that ι never reaches. This shows that epimorphism is *not* about surjectivity; it's about whether morphisms out of the codomain are uniquely determined by composition with f.

Understanding where mono/epic do and don't coincide with injective/surjective is important for each category you work in. In **Ab** (abelian groups) and more generally in any abelian category, the coincidence is restored: monomorphisms are exactly injections (kernel = 0) and epimorphisms are exactly surjections (cokernel = 0), with the natural notion of image and coimage defined via universal properties. This is part of why abelian categories are so well-behaved for homological algebra. In topological spaces, monomorphisms are again injections, but epimorphisms are *dense* continuous maps (not necessarily surjective). The categorical definitions thus serve as diagnostic tools: when mono ≠ injective or epic ≠ surjective in a given category, it reveals something structural about that category's morphisms — and understanding this divergence is the first step toward the richer theory of abelian and additive categories you'll study next.
