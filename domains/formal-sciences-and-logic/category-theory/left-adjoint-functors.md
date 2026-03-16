---
id: left-adjoint-functors
title: Left Adjoint Functors
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: functors
  type: hard
- id: natural-transformations
  type: hard
builds-toward:
- adjoint-functors
- adjunction-as-hom-bijection
- monads-in-category-theory
tags:
- adjunction
- functor-pairs
- universal-properties
stage: advanced
status: draft
---

# Left Adjoint Functors

## Core Idea
A functor L: C → D is a left adjoint if there exists R: D → C such that morphisms Lc → d in D correspond bijectively to morphisms c → Rd in C, naturally in both variables. Left adjoints preserve colimits and satisfy a universal property characterizing them as the 'best approximation' in a precise sense.

## Explainer

From functors, you know how to map one category to another in a structure-preserving way. From natural transformations, you know how to compare two functors systematically. An **adjunction** is the next step: a relationship between a pair of functors that captures a profound and ubiquitous symmetry in mathematics. It is one of the most important organizing concepts in category theory.

The formal definition: L: C → D is a **left adjoint** to R: D → C, written L ⊣ R, if there is a bijection Hom_D(Lc, d) ≅ Hom_C(c, Rd), natural in both c ∈ C and d ∈ D. Read this slowly. A morphism from Lc to d in the category D corresponds bijectively to a morphism from c to Rd in the category C. The word "naturally" means this bijection commutes with pre- and post-composition by morphisms in C and D — it is not just a set-theoretic correspondence but one that respects all categorical structure. The bijection is often written φ_{c,d}: Hom_D(Lc, d) → Hom_C(c, Rd).

The canonical example is the free group construction. Let F: Set → Grp be the free group functor (F(S) is the free group on the set S of generators) and U: Grp → Set the forgetful functor (U(G) is the underlying set of a group G). Then F ⊣ U. A group homomorphism F(S) → G corresponds exactly to a function S → U(G): to define a homomorphism out of the free group, you only need to specify where each generator goes, and the group structure takes care of the rest. The adjunction makes this "generators vs. homomorphisms" trade-off precise. Many constructions in mathematics follow this pattern: free objects, tensor products, abelianizations, completions, and sheafifications are all left adjoints to forgetful-style right adjoints.

Left adjoints have a powerful structural property: they **preserve all colimits**. Colimits generalize unions, pushouts, coproducts (disjoint unions), and coequalizers. If L is a left adjoint, then L(colim F) ≅ colim(L∘F) for any small diagram F. This means: to compute L on a complex colimit, compute L on each piece and take the colimit of the results. The dual statement holds for right adjoints, which preserve limits (products, pullbacks, equalizers). These theorems make adjunctions central throughout homological algebra, algebraic geometry, and topos theory — wherever you need to know how a functor interacts with universal constructions, the adjoint structure tells you immediately.
