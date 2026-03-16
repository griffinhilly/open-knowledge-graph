---
id: tor-derived-tensor
title: Tor Functors as Derived Tensor Product
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: exact-sequences
  type: hard
- id: projective-objects
  type: hard
- id: tensor-products-universal
  type: soft
builds-toward:
- derived-functors
- homology-and-cohomology
tags:
- derived-functors
- homological-algebra
- tensor-products
stage: advanced
status: draft
---

# Tor Functors as Derived Tensor Product

## Core Idea
The Tor functor Tor_n(A, B) is the n-th left derived functor of − ⊗ B, computed via a projective resolution of A. Tor_1(A, B) measures the failure of A ⊗ − to be exact, capturing torsion phenomena. Higher Tor groups measure higher-order non-exactness. Tor is dual to Ext and crucial in computing tensor products of complexes and understanding flatness.

## Explainer

From exact sequences, you know what it means for a functor to be exact: it preserves the exactness of short exact sequences 0 → A' → A → A'' → 0. The tensor product − ⊗ B is **right-exact**: a short exact sequence 0 → A' → A → A'' → 0 yields A' ⊗ B → A ⊗ B → A'' ⊗ B → 0, with the zero on the right preserved. But the map A' ⊗ B → A ⊗ B may fail to be injective — left-exactness can break. The **Tor functors** are the derived functors that measure precisely how and how much it breaks.

The construction uses projective resolutions. For a module A, take a **projective resolution**: a long exact sequence ... → P₂ → P₁ → P₀ → A → 0 where each Pᵢ is projective (you know projective modules: they are the modules for which Hom(P, −) is exact, equivalently the direct summands of free modules). Remove A from the sequence. Tensor the remaining complex with B to get ... → P₂⊗B → P₁⊗B → P₀⊗B → 0. This tensored complex is generally no longer exact. Take its homology: Tor_n(A, B) = Hₙ(P_• ⊗ B). A key theorem establishes that this is independent of the choice of projective resolution, so Tor_n is well-defined.

The lowest cases give the most intuition. **Tor_0(A, B) = A ⊗ B**: the zeroth homology just recovers the original tensor product. **Tor_1(A, B)** is the most geometrically meaningful and gives Tor its name. For cyclic groups: Tor_1(ℤ/mℤ, ℤ/nℤ) ≅ ℤ/gcd(m,n)ℤ. This captures **torsion interaction**: two cyclic groups have non-trivial Tor₁ exactly when their orders share a common factor. The torsion in A interacts with the torsion in B in a way that is invisible to the tensor product itself (ℤ/mℤ ⊗ ℤ/nℤ ≅ ℤ/gcd(m,n)ℤ as well, but the information about the failure of exactness in the resolution is what Tor records at higher levels).

The flatness connection ties Tor back to module theory: A is **flat** if and only if Tor_n(A, B) = 0 for all n ≥ 1 and all B. Flat modules are precisely those for which tensoring preserves exact sequences — they are the "good" modules for tensor products, analogous to projective modules for Hom. Free modules are flat, projective modules are flat, but flatness is a strictly weaker condition (every projective is flat, but not conversely). In algebraic geometry, the fibers of a flat morphism vary "continuously" — Tor vanishing is the algebraic condition ensuring this geometric regularity. Higher Tor groups also appear in the Künneth formula for computing homology of product spaces, where Tor_1 terms correct for the non-exactness that can arise when the chain groups have torsion. Tor is, alongside Ext, one of the two fundamental invariants of homological algebra.
