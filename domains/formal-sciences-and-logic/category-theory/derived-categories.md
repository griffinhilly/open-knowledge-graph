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
stage: abstract-reasoning
status: draft
---

# Derived Categories and Derived Equivalences

## Core Idea
The derived category of an abelian category is obtained by localizing the category of chain complexes at quasi-isomorphisms, so that objects related by homotopy-equivalent chain maps become isomorphic. Derived categories package homological invariants into a single triangulated category and are fundamental to homological algebra. Derived equivalences between algebras capture deep relationships between their module categories.

## How It's Best Learned
Begin with the derived category of an abelian category (e.g., modules over a ring or sheaves of abelian groups). Understand quasi-isomorphisms and homotopy equivalences. Compute the derived category in concrete examples. Study derived functors and how they arise naturally in this setting.

## Common Misconceptions
The derived category is not the homotopy category; localization at quasi-isomorphisms adds new isomorphisms beyond homotopy equivalences. Also, derived categories are triangulated but not necessarily abelian.

## Explainer

You've studied chain complexes and exact sequences, which encode how algebraic objects fit together, and derived functors like Ext and Tor, which measure the failure of exactness. The derived category is the natural home where both of these ideas live simultaneously — it's the construction that makes derived functors *representable* as morphisms rather than as separate gadgets computed outside the category.

The starting point is the **homotopy category** K(𝒜) of an abelian category 𝒜: objects are chain complexes, and morphisms are chain maps modulo chain homotopy equivalence. Two chain maps are identified if their difference is null-homotopic. This already improves on the naive category of complexes, but it still distinguishes complexes that carry the same homological information. A **quasi-isomorphism** is a chain map that induces isomorphisms on all homology groups — it is the correct notion of "same homological information," even if the complexes themselves are not homotopy equivalent. The **derived category** D(𝒜) is obtained by **localizing** K(𝒜) at the class of quasi-isomorphisms: formally inverting them, so that any quasi-isomorphism becomes an isomorphism in D(𝒜). After this localization, two complexes are isomorphic in D(𝒜) if and only if they are quasi-isomorphic, capturing exactly the notion of "same homological content."

The critical distinction from the homotopy category is that **quasi-isomorphic complexes need not be homotopy equivalent** — localization at quasi-isomorphisms is strictly finer than homotopy equivalence. Concretely, every injective (or projective) resolution of an object A is quasi-isomorphic to A (viewed as a complex concentrated in degree 0), so in D(𝒜), the object A and any of its resolutions become *isomorphic*. This is what makes derived functors natural: the right-derived functor RF is simply F applied to an injective resolution, and the derived category absorbs the resolution into the object itself. The various Extⁿ(A, B) groups then appear as Hom groups in D(𝒜): Extⁿ(A, B) ≅ Hom_{D(𝒜)}(A, B[n]), where B[n] is the complex B shifted n degrees. Derived functors are no longer external computations — they are morphisms in the right category.

A **derived equivalence** between two algebras A and B is an equivalence of triangulated categories D(Mod-A) ≅ D(Mod-B). This is weaker than Morita equivalence (which requires equivalence of abelian module categories), but captures deep structural similarities. Tilting theory provides the main source of derived equivalences: if T is a tilting module over A, then End(T) is derived equivalent to A, even though Mod-A and Mod-End(T) may look very different as abelian categories. Derived equivalences preserve all homological invariants (K-theory, Hochschild cohomology, global dimension behavior) and are the fundamental tool in modern representation theory, algebraic geometry (Fourier-Mukai transforms between derived categories of coherent sheaves), and mathematical physics (mirror symmetry). The triangulated structure — distinguished triangles generalizing short exact sequences — is preserved under derived equivalence and is the structural skeleton that makes the comparison possible.
