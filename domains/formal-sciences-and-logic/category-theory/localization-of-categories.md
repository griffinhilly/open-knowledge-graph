---
id: localization-of-categories
title: Localization of Categories
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: functors
  type: hard
- id: equivalence-of-categories
  type: hard
builds-toward:
- derived-categories
- quotient-categories
tags:
- localization
- inverting-morphisms
- quotient-categories
stage: abstract-reasoning
status: draft
---

# Localization of Categories

## Core Idea
Localization is the process of formally inverting a class of morphisms in a category to create a new category where those morphisms become isomorphisms. This is analogous to localization in ring theory and allows systematic modification of categorical structure. The resulting localized category admits a universal property characterizing functors that preserve the inverted morphisms.

## How It's Best Learned
Study localization in the category of modules, where localizing at a multiplicative set yields the category of localized modules. Understand the universal property and verify that the localization functor is universal. Explore applications to homological algebra and algebraic geometry.

## Common Misconceptions
Localization does not always result in a category equivalent to a known category; checking whether a localization is 'nice' requires careful analysis. Also, different classes of morphisms can yield very different localizations.

## Explainer

The motivation for localization comes from a familiar algebraic operation. In ring theory, you localize a ring R at a multiplicative set S ⊂ R by formally adding inverses to every element of S, creating the localized ring S⁻¹R where s/1 is invertible for each s ∈ S. The integers localized at powers of 2 give dyadic rationals; the integers localized at all nonzero elements give the rationals. The categorical version does the same thing one dimension up: given a category C and a collection W of morphisms you want to become invertible, the **localization** C[W⁻¹] is a new category where every morphism in W is an isomorphism, and it is the smallest such category fitting a **universal property**: any functor F: C → D that sends all morphisms in W to isomorphisms factors uniquely through the localization functor γ: C → C[W⁻¹].

You already understand functors as structure-preserving maps between categories, and equivalences of categories as the "right" notion of sameness (an equivalence need not be a bijection on objects, but pairs of functors F and G with FG ≅ Id and GF ≅ Id). Localization is a way of constructing new categories by declaring some morphisms to be equivalences even when they weren't before. This is different from forming a quotient category (which identifies morphisms) — localization adds formal inverses rather than equating morphisms.

The construction of C[W⁻¹] in full generality is technically demanding. Morphisms in C[W⁻¹] are represented by **zig-zags** — alternating sequences of forward morphisms from C and backward morphisms that formally invert elements of W. Composition of zig-zags requires concatenation and simplification, and without additional conditions on W, the resulting hom-sets may be proper classes rather than sets, making the localization ill-defined as a category. The classical solution is to require that W be a **calculus of fractions**: a system of conditions (closure under composition, common-denominator conditions) that ensures zig-zags reduce to left or right fractions of the form s⁻¹f or fs⁻¹, giving well-controlled hom-sets.

The most important application of categorical localization is in homological algebra and algebraic geometry. The **derived category** of an abelian category is constructed exactly by localizing the category of chain complexes at the class of **quasi-isomorphisms** — morphisms that induce isomorphisms on all cohomology groups. Two complexes that are quasi-isomorphic may look very different as complexes, but they become isomorphic in the derived category. This identifies the "real" invariants (cohomology) and disregards structural differences that don't affect those invariants. The derived category framework lets you work with resolutions interchangeably with the objects they resolve, which is the algebraic foundation of sheaf theory, algebraic K-theory, and modern homotopy theory.

Understanding localization also illuminates why equivalences of categories are more natural than isomorphisms. An equivalence says there is a functor F: C → D and a functor G: D → C with GF ≅ Id_C and FG ≅ Id_D — but the two categories need not have the same objects or morphisms, just the same "shape" up to invertible natural transformation. Localizations can produce categories equivalent to known ones: for example, localizing the category of topological spaces at the homotopy equivalences gives the **homotopy category**, which captures topological structure up to continuous deformation. Different choices of W can carve out very different aspects of the same underlying category, making localization a flexible tool for focusing on the invariants that matter for a particular application.

