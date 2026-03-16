---
id: ext-derived-hom
title: Ext Functors as Derived Hom
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: exact-sequences
  type: hard
- id: injective-objects
  type: hard
builds-toward:
- derived-functors
- homology-and-cohomology
tags:
- derived-functors
- homological-algebra
- extensions
stage: advanced
status: draft
---

# Ext Functors as Derived Hom

## Core Idea
The Ext functor Ext^n(A, B) is the n-th right derived functor of Hom(A, −), computed via an injective resolution of B. Ext^1(A, B) classifies extensions of A by B, while higher Ext groups measure obstructions to splitting. Ext is fundamental to extension theory and provides invariants for classifying objects in abelian categories.

## Explainer

From your study of exact sequences, you know that a short exact sequence 0 → B → E → A → 0 encodes the idea that E is built from B and A — but not necessarily as a direct sum B ⊕ A. The question of whether such a sequence splits (whether E ≅ A ⊕ B) is a central one, and you've seen that it depends on properties of the morphisms involved. From injective objects, you know that having enough injectives in an abelian category allows you to resolve any object in a canonical way. The Ext functor is where these ideas converge: it measures, systematically, the obstruction to splitting.

The construction begins by choosing an **injective resolution** of B: an exact sequence 0 → B → I^0 → I^1 → I^2 → ⋯ where each I^k is injective. Such resolutions exist in any abelian category with enough injectives (like modules over a ring). Now apply the functor Hom(A, −) to the resolution (dropping B): you get a cochain complex 0 → Hom(A, I^0) → Hom(A, I^1) → Hom(A, I^2) → ⋯. This complex is generally not exact — Hom(A, −) is left exact but not right exact, so exactness can fail at each step. The **n-th cohomology** of this complex is defined to be **Ext^n(A, B)**. Ext^0(A, B) recovers Hom(A, B) itself (the original left-exact piece that did survive). The higher Ext groups measure the failure of the resolution to remain exact after applying Hom.

The deepest result is the **classification theorem for Ext^1**: elements of Ext^1(A, B) are in natural bijection with equivalence classes of short exact sequences 0 → B → E → A → 0, where two extensions are equivalent if there is an isomorphism between them that fixes both B and A. The zero element of Ext^1(A, B) corresponds to the split extension B ⊕ A; a nonzero element corresponds to a genuinely non-split extension. This makes Ext^1 a computable algebraic invariant that encodes whether and how A and B can be "glued together" non-trivially. For example, Ext^1_ℤ(ℤ/2, ℤ) ≅ ℤ/2, which corresponds to the fact that there are exactly two extensions of ℤ/2 by ℤ: the split one (ℤ ⊕ ℤ/2) and the non-split one (ℤ itself, via the sequence 0 → ℤ →×2 ℤ → ℤ/2 → 0).

Higher Ext groups Ext^n(A, B) for n ≥ 2 have a similar interpretation in terms of longer exact sequences and appear naturally in cohomology theories. In group cohomology, Ext^n over the group ring ℤ[G] computes H^n(G, M); in sheaf theory, Ext^n encodes derived global sections. The power of the derived functor framework is that it is universal: regardless of which injective resolution of B you choose, the Ext groups are well-defined up to canonical isomorphism, so they are genuine invariants of the pair (A, B), not artifacts of the resolution.
