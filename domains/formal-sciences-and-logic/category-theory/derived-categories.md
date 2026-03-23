---
id: derived-categories
title: Derived Categories and Derived Equivalences
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: chain-complexes-exact-sequences
  type: hard
- id: derived-functors
  type: hard
- id: triangulated-categories
  type: soft
builds-toward:
- spectral-sequences-introduction
tags:
- derived-category
- homotopy-category
- localization
- derived-equivalence
stage: expert
status: draft
---

# Derived Categories and Derived Equivalences

## Core Idea
The derived category of an abelian category is obtained by localizing the category of chain complexes at quasi-isomorphisms, so that objects related by homotopy-equivalent chain maps become isomorphic. Derived categories package homological invariants into a single triangulated category and are fundamental to homological algebra. Derived equivalences between algebras capture deep relationships between their module categories.

## How It's Best Learned
Begin with the derived category of an abelian category (e.g., modules over a ring or sheaves of abelian groups). Understand quasi-isomorphisms and homotopy equivalences. Compute the derived category in concrete examples. Study derived functors and how they arise naturally in this setting.

## Common Misconceptions
The derived category is not the homotopy category; localization at quasi-isomorphisms adds new isomorphisms beyond homotopy equivalences. Also, derived categories are triangulated but not necessarily abelian.

## Questions

```yaml
- question: "The homotopy category K(𝒜) identifies chain maps up to homotopy equivalence. The derived category D(𝒜) makes an additional identification. What is it?"
  type: multiple-choice
  options:
    - "D(𝒜) further identifies all complexes with their total cohomology, collapsing each complex to a graded group"
    - "D(𝒜) formally inverts quasi-isomorphisms, so complexes with the same homology groups become isomorphic even if they are not homotopy equivalent"
    - "D(𝒜) identifies complexes up to exact functor equivalence, splitting all short exact sequences"
    - "D(𝒜) collapses all bounded complexes to their degree-0 cohomology, making it equivalent to 𝒜 itself"
  answer: 1
  explanation: "K(𝒜) only identifies chain maps modulo homotopy; two complexes can be quasi-isomorphic in K(𝒜) yet remain non-isomorphic objects. D(𝒜) is obtained by localizing K(𝒜) at the class of quasi-isomorphisms — formally inverting them — so any quasi-isomorphism becomes an isomorphism in D(𝒜). This means complexes that encode the same homological data (same homology groups) are genuinely isomorphic objects in D(𝒜). This is strictly finer than homotopy equivalence: quasi-isomorphic complexes need not be homotopy equivalent."

- question: "In the derived category D(𝒜), how does the classical Ext^n(A, B) appear?"
  type: multiple-choice
  options:
    - "As the n-th cohomology of the internal Hom complex Hom(A, B)"
    - "As the set of homotopy classes of chain maps from A to B of degree n in K(𝒜)"
    - "As Hom_{D(𝒜)}(A, B[n]), the set of morphisms in D(𝒜) from A to the n-fold shift of B"
    - "As a derived functor that must still be computed externally via a projective resolution of A"
  answer: 2
  explanation: "One of the central payoffs of the derived category is the isomorphism Ext^n(A, B) ≅ Hom_{D(𝒜)}(A, B[n]), where B[n] is the complex B shifted n degrees. Derived functors, which classically required external resolution computations, become representable as morphisms within D(𝒜) itself. This is why derived categories are described as the 'natural home' of homological algebra: Ext is no longer a separate gadget but a Hom set in the correct category. Option D describes the classical construction that the derived category supersedes."

- question: "The derived category D(𝒜) equals the homotopy category K(𝒜) whenever the abelian category 𝒜 has enough injectives, because in that case every quasi-isomorphism is also a homotopy equivalence."
  type: true-false
  answer: false
  explanation: "Having enough injectives does not make quasi-isomorphisms into homotopy equivalences. Even in categories with enough injectives (such as modules over a ring), there exist quasi-isomorphic complexes that are not homotopy equivalent. The derived category adds new isomorphisms beyond those in K(𝒜) regardless of whether injectives exist. What enough injectives enables is the use of injective resolutions to compute derived functors — but this is about computational technique, not about collapsing D(𝒜) into K(𝒜)."

- question: "In D(𝒜), an object A (viewed as a complex concentrated in degree 0) is isomorphic to any of its injective resolutions."
  type: true-false
  answer: true
  explanation: "An injective resolution of A is a complex I• that is quasi-isomorphic to A (the augmentation map A → I• induces isomorphisms on all homology groups). Since D(𝒜) is obtained by inverting quasi-isomorphisms, A and I• become isomorphic in D(𝒜). This is the fundamental reason derived functors are natural in the derived category: RF(A) = F(I•) is not an external gadget but the image of A's isomorphic copy I• under F, making resolutions internal to the categorical structure."

- question: "Explain the difference between a quasi-isomorphism and a homotopy equivalence of chain complexes, and why D(𝒜) inverts quasi-isomorphisms rather than just homotopy equivalences."
  type: short-answer
  answer: "A homotopy equivalence is a chain map f: A→B with a chain homotopy inverse g: B→A such that gf and fg are chain homotopic to identity. A quasi-isomorphism is any chain map inducing isomorphisms on all homology groups, but it may not have any chain map as an inverse — it is a strictly weaker notion. Every homotopy equivalence is a quasi-isomorphism, but not conversely. D(𝒜) inverts quasi-isomorphisms because the correct notion of 'same object' in homological algebra is 'same homology,' not 'homotopy equivalent complex.' By inverting quasi-isomorphisms, D(𝒜) identifies A with all its resolutions, making derived functors representable as morphisms. Stopping at homotopy equivalences would leave distinct the objects and their resolutions — preventing Ext from being a Hom set in the category."
  explanation: "A concrete example: the complex 0 → ℤ →×2→ ℤ → 0 is quasi-isomorphic to ℤ/2 concentrated in degree 0 (they have the same cohomology), but they are not homotopy equivalent as chain complexes. In D(Ab), they become isomorphic, which is the correct identification for homological purposes."
```

## Explainer

You've studied chain complexes and exact sequences, which encode how algebraic objects fit together, and derived functors like Ext and Tor, which measure the failure of exactness. The derived category is the natural home where both of these ideas live simultaneously — it's the construction that makes derived functors *representable* as morphisms rather than as separate gadgets computed outside the category.

The starting point is the **homotopy category** K(𝒜) of an abelian category 𝒜: objects are chain complexes, and morphisms are chain maps modulo chain homotopy equivalence. Two chain maps are identified if their difference is null-homotopic. This already improves on the naive category of complexes, but it still distinguishes complexes that carry the same homological information. A **quasi-isomorphism** is a chain map that induces isomorphisms on all homology groups — it is the correct notion of "same homological information," even if the complexes themselves are not homotopy equivalent. The **derived category** D(𝒜) is obtained by **localizing** K(𝒜) at the class of quasi-isomorphisms: formally inverting them, so that any quasi-isomorphism becomes an isomorphism in D(𝒜). After this localization, two complexes are isomorphic in D(𝒜) if and only if they are quasi-isomorphic, capturing exactly the notion of "same homological content."

The critical distinction from the homotopy category is that **quasi-isomorphic complexes need not be homotopy equivalent** — localization at quasi-isomorphisms is strictly finer than homotopy equivalence. Concretely, every injective (or projective) resolution of an object A is quasi-isomorphic to A (viewed as a complex concentrated in degree 0), so in D(𝒜), the object A and any of its resolutions become *isomorphic*. This is what makes derived functors natural: the right-derived functor RF is simply F applied to an injective resolution, and the derived category absorbs the resolution into the object itself. The various Extⁿ(A, B) groups then appear as Hom groups in D(𝒜): Extⁿ(A, B) ≅ Hom_{D(𝒜)}(A, B[n]), where B[n] is the complex B shifted n degrees. Derived functors are no longer external computations — they are morphisms in the right category.

A **derived equivalence** between two algebras A and B is an equivalence of triangulated categories D(Mod-A) ≅ D(Mod-B). This is weaker than Morita equivalence (which requires equivalence of abelian module categories), but captures deep structural similarities. Tilting theory provides the main source of derived equivalences: if T is a tilting module over A, then End(T) is derived equivalent to A, even though Mod-A and Mod-End(T) may look very different as abelian categories. Derived equivalences preserve all homological invariants (K-theory, Hochschild cohomology, global dimension behavior) and are the fundamental tool in modern representation theory, algebraic geometry (Fourier-Mukai transforms between derived categories of coherent sheaves), and mathematical physics (mirror symmetry). The triangulated structure — distinguished triangles generalizing short exact sequences — is preserved under derived equivalence and is the structural skeleton that makes the comparison possible.
