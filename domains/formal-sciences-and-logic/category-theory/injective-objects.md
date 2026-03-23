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
stage: expert
status: draft
---

# Injective Objects and Injective Envelopes

## Core Idea
An object I is injective if Hom(−, I) preserves monomorphisms, equivalently, if every morphism A → I extends to a morphism B → I for any monomorphism A → B. Injectives are dual to projectives and generalize divisible groups. Every object embeds into an injective envelope, enabling injective resolutions essential to homology and cohomology theory.

## Questions

```yaml
- question: "An object I is injective in an abelian category. Given a monomorphism i: A ↪ B and a morphism f: A → I, what does injectivity guarantee?"
  type: multiple-choice
  options:
    - "That f is an isomorphism from A onto I"
    - "That there exists a morphism f̃: B → I such that f̃ ∘ i = f — the map from the subobject A extends to all of B"
    - "That every morphism from B factors through A via the monomorphism i"
    - "That I has no proper subobjects other than the zero object"
  answer: 1
  explanation: "Injectivity is precisely the extension property: any morphism into I from a subobject A can always be extended to the ambient object B. The injective object I is an 'extensible target' — it never blocks extending morphisms from subobjects. This is the categorical generalization of divisibility: just as every homomorphism from a subgroup into ℚ can be extended to the whole group, injectivity guarantees extensions in any abelian category."

- question: "Why is ℚ injective as a ℤ-module, while ℤ itself is not?"
  type: multiple-choice
  options:
    - "ℚ contains ℤ as a subgroup, and containing a non-injective subobject forces injectivity on the ambient object"
    - "ℚ is a field, and all fields are automatically injective over their prime subfields"
    - "ℚ is divisible — for any x ∈ ℚ and nonzero n ∈ ℤ, there exists y ∈ ℚ with ny = x — which enables extending any ℤ-homomorphism; ℤ fails this because, for example, 1 ∈ ℤ cannot be divided by 2 within ℤ"
    - "ℤ is a ring, not a ℤ-module, so the comparison is invalid"
  answer: 2
  explanation: "Over a PID like ℤ, injective modules are exactly the divisible ones. Divisibility is what enables the extension: when you try to extend a homomorphism to a new element b with nb ∈ A for some n, divisibility lets you define f̃(b) = f(nb)/n consistently inside ℚ. ℤ fails injectivity because there is no integer y with 2y = 1 — the extension is blocked in cases requiring division by 2."

- question: "Every object in a suitable abelian category embeds essentially into a unique (up to isomorphism) injective envelope."
  type: true-false
  answer: true
  explanation: "The injective envelope I(M) is characterized by two properties: (1) it is injective, and (2) M embeds essentially — every nonzero subobject of I(M) meets M nontrivially. This combination makes it the minimal injective extension of M. Injective envelopes exist in categories like R-Mod and Ab, and their uniqueness up to isomorphism is what makes injective resolutions well-defined for every object."

- question: "Injective objects and projective objects are the same objects in every abelian category, since injectivity and projectivity are categorically dual and defined by reversing all arrows."
  type: true-false
  answer: false
  explanation: "While injectives and projectives are categorically dual — defined by reversing all arrows in the extension/lifting diagrams — they are generally different objects in the same category. In Ab, projective objects are free abelian groups (ℤ, ℤⁿ, etc.), while injective objects are divisible groups (ℚ, ℤ[1/p], ℚ/ℤ, etc.). Duality tells you that theorems about injectives translate to theorems about projectives by reversing arrows, but it does not make them the same objects."

- question: "Why are injective resolutions essential for defining derived functors like Ext, rather than simply applying Hom(N, −) directly?"
  type: short-answer
  answer: "The Hom functor Hom(N, −) is only left-exact — it preserves exact sequences on the left but fails exactness on the right. To define Ext^n(N, M), you resolve M by an injective resolution 0 → M → I₀ → I₁ → I₂ → ⋯, apply Hom(N, −) to the deleted resolution, and take cohomology. The injective objects in the resolution are chosen precisely because Hom is exact on injectives, making the cohomology groups well-defined. The Ext groups measure the failure of Hom to be right-exact — a failure that only becomes computable by resolving through injectives."
  explanation: "This is the fundamental idea of homological algebra: derived functors measure the failure of ordinary functors to preserve exactness. To compute these derived functors, you need resolutions by objects on which the functor is exact — injective resolutions for right-derived functors (Ext), projective resolutions for left-derived functors (Tor). Without injective objects and the guarantee that every object embeds into one, this entire framework collapses."
```

## Explainer

From your study of additive categories and abelian groups, you know what it means for a morphism to be a monomorphism (injective on elements, or more generally left-cancellable). An object I is **injective** if, whenever you have a monomorphism i: A ↪ B and a morphism f: A → I, you can always find an extension f̃: B → I making the triangle commute: f̃ ∘ i = f. Informally: any map from a subobject A into I can be extended to the whole ambient object B. Injective objects are "extensible targets" — they never block extensions.

The canonical example over ℤ is the group ℚ of rational numbers. Given any subgroup A of an abelian group B and a homomorphism f: A → ℚ, you can always extend f to all of B. The key property enabling this is **divisibility**: for any x ∈ ℚ and non-zero integer n, there exists y ∈ ℚ with ny = x. When you try to extend f to a new element b ∈ B \ A, you need a consistent value for f̃(b). If nb ∈ A for some n (which happens in quotient situations), divisibility ensures you can divide f(nb) by n inside ℚ to define f̃(b) without contradiction. Injective modules over a ring generalize this: over a principal ideal domain, injective modules are exactly the divisible ones.

**Injective envelopes** capture the idea of the smallest injective object containing a given object. Every object M in a suitable abelian category embeds into an **injective envelope** I(M): an injective object in which M sits essentially — meaning every nonzero subobject of I(M) meets M non-trivially. The injective envelope is characterized by being both injective and essential over M, and it is unique up to isomorphism. For abelian groups, the injective envelope of ℤ/nℤ is ℤ[1/p₁, ..., 1/pₖ]/ℤ where the pᵢ divide n — the minimal divisible extension.

The payoff is **injective resolutions**: for any object M, choose an embedding M ↪ I₀ into its injective envelope, then embed the cokernel into another injective I₁, and continue: 0 → M → I₀ → I₁ → I₂ → ⋯. This is an injective resolution — an exact sequence of injective objects. Injective resolutions are the raw material for **derived functors**: apply Hom(N, −) to the deleted resolution (drop M from the front), take cohomology, and you get the Ext groups Ext^n(N, M). The failure of Hom to be exact on the right — it only preserves exactness at injective objects — is precisely what Ext measures. Without injective objects and their resolutions, cohomological invariants of modules and sheaves would have no computational foundation.
