---
id: derived-equivalences-categories
title: Derived Equivalences of Categories
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: triangulated-categories
  type: hard
- id: equivalence-of-categories
  type: hard
builds-toward:
- topos-theory-intro
tags:
- derived-equivalence
- derived-category
- Morita
- homological
stage: advanced
status: draft
---

# Derived Equivalences of Categories

## Core Idea
Two categories are derived equivalent if their derived categories are equivalent as triangulated categories. Derived equivalence is coarser than ordinary equivalence but preserves homological invariants. Morita equivalence (between module categories) is an instance of derived equivalence. Derived equivalent categories need not be equivalent as ordinary categories but share the same derived categorical structure, making derived equivalence a fundamental invariant in representation theory.

## How It's Best Learned
Study Morita equivalence for rings and modules as the canonical example. Verify that derived equivalent categories have isomorphic Hochschild homology and K-theory. Explore how tilting complexes induce derived equivalences between module categories.

## Common Misconceptions
Derived equivalence is weaker than ordinary equivalence; two derived equivalent categories may have very different ordinary categorical properties. The notion depends on the choice of derived category (unbounded, bounded, etc.). Not every equivalence of derived categories lifts to an equivalence of underlying categories.

## Explainer

From your study of triangulated categories and equivalence of categories, you have the conceptual building blocks for derived equivalence. Recall that the derived category D(A) of an abelian category A is constructed by formally inverting quasi-isomorphisms — maps of chain complexes that induce isomorphisms on all cohomology groups. This process loses some fine-grained information about A but retains its homological behavior. Two categories are **derived equivalent** when their derived categories are equivalent as triangulated categories — meaning there is a triangulated functor between them that is an equivalence.

The key calibration is where derived equivalence sits in a hierarchy of notions of sameness. Ordinary categorical equivalence is strongest: two categories that are equivalent in the usual sense certainly have equivalent derived categories. Derived equivalence is strictly weaker: two categories can be derived equivalent while being very different as ordinary categories. The classic example is **Morita equivalence** for rings: rings R and S are Morita equivalent when their module categories Mod-R and Mod-S are equivalent (as ordinary categories). Morita equivalence is an instance of derived equivalence, since an ordinary equivalence induces a derived equivalence. But derived equivalence allows more: a derived equivalence between module categories need not come from any ordinary equivalence between the categories themselves.

The mechanism for constructing derived equivalences is the **tilting complex**. A tilting complex T in the derived category D^b(Mod-R) is a complex satisfying certain orthogonality conditions (no self-Ext groups in nonzero degrees) and generating the derived category. The endomorphism ring S = End(T) is the derived equivalent partner: there is a derived equivalence D^b(Mod-R) ≅ D^b(Mod-S). This is the Rickard-Morita theorem, the derived analogue of classical Morita theory. Tilting theory is the primary tool for constructing and classifying derived equivalences in representation theory of algebras.

Derived equivalence preserves a substantial collection of invariants: **Hochschild homology** and **Hochschild cohomology**, **K-theory**, the **center** of the derived category, and many other homological and homotopical data. This makes derived equivalence a powerful coarsening that is still discriminating enough to be useful. Two algebras that are derived equivalent are "homologically indistinguishable" in a precise sense — all homological machinery applied to one gives the same answer as applied to the other. The study of which invariants are preserved and which are not is an active area, and derived equivalence is the standard notion of "same homological type" in modern representation theory and algebraic geometry.
