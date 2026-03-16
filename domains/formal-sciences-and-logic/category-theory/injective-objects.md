---
id: injective-objects
title: Injective Objects and Injective Envelopes
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: additive-categories
  type: hard
builds-toward:
- derived-functors
- homological-dimension-intro
- ext-derived-hom
tags:
- homological-algebra
- universal-properties
- extensions
stage: advanced
status: draft
---

# Injective Objects and Injective Envelopes

## Core Idea
An object I is injective if Hom(−, I) preserves monomorphisms, equivalently, if every morphism A → I extends to a morphism B → I for any monomorphism A → B. Injectives are dual to projectives and generalize divisible groups. Every object embeds into an injective envelope, enabling injective resolutions essential to homology and cohomology theory.

## Explainer

From your study of additive categories and abelian groups, you know what it means for a morphism to be a monomorphism (injective on elements, or more generally left-cancellable). An object I is **injective** if, whenever you have a monomorphism i: A ↪ B and a morphism f: A → I, you can always find an extension f̃: B → I making the triangle commute: f̃ ∘ i = f. Informally: any map from a subobject A into I can be extended to the whole ambient object B. Injective objects are "extensible targets" — they never block extensions.

The canonical example over ℤ is the group ℚ of rational numbers. Given any subgroup A of an abelian group B and a homomorphism f: A → ℚ, you can always extend f to all of B. The key property enabling this is **divisibility**: for any x ∈ ℚ and non-zero integer n, there exists y ∈ ℚ with ny = x. When you try to extend f to a new element b ∈ B \ A, you need a consistent value for f̃(b). If nb ∈ A for some n (which happens in quotient situations), divisibility ensures you can divide f(nb) by n inside ℚ to define f̃(b) without contradiction. Injective modules over a ring generalize this: over a principal ideal domain, injective modules are exactly the divisible ones.

**Injective envelopes** capture the idea of the smallest injective object containing a given object. Every object M in a suitable abelian category embeds into an **injective envelope** I(M): an injective object in which M sits essentially — meaning every nonzero subobject of I(M) meets M non-trivially. The injective envelope is characterized by being both injective and essential over M, and it is unique up to isomorphism. For abelian groups, the injective envelope of ℤ/nℤ is ℤ[1/p₁, ..., 1/pₖ]/ℤ where the pᵢ divide n — the minimal divisible extension.

The payoff is **injective resolutions**: for any object M, choose an embedding M ↪ I₀ into its injective envelope, then embed the cokernel into another injective I₁, and continue: 0 → M → I₀ → I₁ → I₂ → ⋯. This is an injective resolution — an exact sequence of injective objects. Injective resolutions are the raw material for **derived functors**: apply Hom(N, −) to the deleted resolution (drop M from the front), take cohomology, and you get the Ext groups Ext^n(N, M). The failure of Hom to be exact on the right — it only preserves exactness at injective objects — is precisely what Ext measures. Without injective objects and their resolutions, cohomological invariants of modules and sheaves would have no computational foundation.
