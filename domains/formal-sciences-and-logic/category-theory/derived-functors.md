---
id: derived-functors
title: Derived Functors
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: homology-and-cohomology
  type: hard
- id: adjoint-functors
  type: soft
- id: abelian-categories
  type: soft
- id: vector-spaces
  type: soft
tags:
- derived functor
- Ext
- Tor
- projective resolution
- injective resolution
- left derived
- right derived
stage: advanced
status: draft
---
# Derived Functors

## Core Idea
Derived functors measure how a functor between abelian categories fails to be exact. Given a left exact functor F (such as Hom(M, −)), its right derived functors R^nF are computed by taking an injective resolution of the input, applying F, and taking cohomology: R^nF(A) = H^n(F(I^*)). Dually, left derived functors L_nF of a right exact functor (such as − ⊗ M) use projective resolutions. The key examples are Ext^n(M, N) = R^n Hom(M, −)(N), which classifies n-fold extensions, and Tor_n(M, N) = L_n(− ⊗ N)(M), which detects torsion phenomena. Derived functors convert exactness failures into computable invariants and are the foundation of homological algebra.

## How It's Best Learned
Compute Ext^1_Z(Z/2, Z) by hand: take a projective resolution of Z/2 (namely 0 → Z →(×2) Z → Z/2 → 0), apply Hom(−, Z), and compute the cohomology. Then compute Tor_1^Z(Z/2, Z/3) using a projective resolution of Z/2 and tensoring with Z/3. Connect these computations to the abstract definition and verify independence of the choice of resolution.

## Common Misconceptions
- Derived functors are independent of the choice of resolution (projective or injective); this is a theorem, not obvious, and relies on comparison lemmas and homotopy invariance.
- Ext^0 and Tor_0 recover the original functors (Hom and ⊗ respectively); the higher derived functors measure the non-exactness.
- Not every abelian category has enough projectives or injectives; derived functors require such existence conditions, which must be verified for each category.
