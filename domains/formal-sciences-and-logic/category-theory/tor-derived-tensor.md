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
stage: expert
status: draft
---

# Tor Functors as Derived Tensor Product

## Core Idea
The Tor functor Tor_n(A, B) is the n-th left derived functor of − ⊗ B, computed via a projective resolution of A. Tor_1(A, B) measures the failure of A ⊗ − to be exact, capturing torsion phenomena. Higher Tor groups measure higher-order non-exactness. Tor is dual to Ext and crucial in computing tensor products of complexes and understanding flatness.

## Questions

```yaml
- question: "The tensor product functor − ⊗ B is right-exact but not generally left-exact. What does Tor₁(A, B) measure?"
  type: multiple-choice
  options:
    - "The failure of A ⊗ B to commute with direct sums"
    - "The kernel of the map A' ⊗ B → A ⊗ B when 0 → A' → A → A'' → 0 is exact"
    - "The failure of Hom(A, −) to be right-exact"
    - "The number of non-zero summands in a projective resolution of A"
  answer: 1
  explanation: "When 0 → A' → A → A'' → 0 is exact, tensoring with B gives A' ⊗ B → A ⊗ B → A'' ⊗ B → 0 (right-exactness preserved), but the left map A' ⊗ B → A ⊗ B may fail to be injective. Tor₁(A, B) is exactly the kernel of this map — it measures how much the injection fails. If Tor₁(A, B) = 0 for all B, then − ⊗ A is left-exact (and hence exact), meaning A is flat. Note: Tor measures failure of left-exactness of the tensor product, not Hom — Ext handles the failure of Hom to be right-exact."

- question: "What is Tor₁(ℤ/6ℤ, ℤ/4ℤ)?"
  type: multiple-choice
  options:
    - "ℤ/24ℤ"
    - "ℤ/2ℤ"
    - "0"
    - "ℤ/6ℤ ⊕ ℤ/4ℤ"
  answer: 1
  explanation: "For cyclic groups, Tor₁(ℤ/mℤ, ℤ/nℤ) ≅ ℤ/gcd(m,n)ℤ. Here gcd(6,4) = 2, so Tor₁(ℤ/6ℤ, ℤ/4ℤ) ≅ ℤ/2ℤ. This captures 'torsion interaction': the two groups have a common factor of 2, so their Tor₁ is non-trivial. Note that ℤ/6ℤ ⊗ ℤ/4ℤ ≅ ℤ/2ℤ as well — but Tor₁ encodes information about the *failure of exactness* in the resolution, which happens to coincide here. For coprime orders (e.g., ℤ/2ℤ and ℤ/3ℤ), Tor₁ = 0."

- question: "A module A is flat if and only if Tor_n(A, B) = 0 for all n ≥ 1 and all modules B."
  type: true-false
  answer: true
  explanation: "This is the defining characterization of flatness in terms of Tor. Flatness means tensoring with A preserves exact sequences (− ⊗ A is an exact functor). Tor_n(A, B) measures the failure of exactness at the nth level of a projective resolution tensored with B. If all these failure groups vanish, the tensor product is exact at every level, which is precisely flatness. Free modules and projective modules are flat; flatness is strictly weaker than projectivity (there exist flat modules that are not projective)."

- question: "Tor₀(A, B) is zero whenever A and B have no common torsion elements."
  type: true-false
  answer: false
  explanation: "Tor₀(A, B) = A ⊗ B, always — it recovers the ordinary tensor product and is never 'zero because of no common torsion.' The subscript-zero Tor is just the tensor product itself, regardless of torsion. It is Tor₁ and higher groups that detect torsion interaction. For example, ℤ ⊗ ℤ/nℤ ≅ ℤ/nℤ ≠ 0 even though ℤ is torsion-free."

- question: "Why is Tor computed using projective resolutions rather than injective resolutions, and what does it mean for a module to be flat in terms of Tor?"
  type: short-answer
  answer: "Tor is the left derived functor of the tensor product. Derived functors of a right-exact functor F are computed by replacing the argument with a projective resolution, applying F, and taking homology — this 'fills in' the left-exactness that F lacks. Injective resolutions are used for right derived functors of left-exact functors (like Hom, which gives Ext). Since − ⊗ B is right-exact (not left-exact), its derived functors go to the left, requiring projective resolutions. A module A is flat precisely when Tor_n(A, B) = 0 for all n ≥ 1 and all B, meaning tensoring with A is already exact and no derived correction is needed."
  explanation: "The left/right distinction is fundamental: left derived functors correct for failure of left-exactness (Tor from tensor), right derived functors correct for failure of right-exactness (Ext from Hom). Using an injective resolution for Tor would produce incorrect (and in fact trivially zero) answers in many cases because projective modules are exactly the ones for which tensoring is exact — they are the 'acyclic objects' for the tensor product functor."
```

## Explainer

From exact sequences, you know what it means for a functor to be exact: it preserves the exactness of short exact sequences 0 → A' → A → A'' → 0. The tensor product − ⊗ B is **right-exact**: a short exact sequence 0 → A' → A → A'' → 0 yields A' ⊗ B → A ⊗ B → A'' ⊗ B → 0, with the zero on the right preserved. But the map A' ⊗ B → A ⊗ B may fail to be injective — left-exactness can break. The **Tor functors** are the derived functors that measure precisely how and how much it breaks.

The construction uses projective resolutions. For a module A, take a **projective resolution**: a long exact sequence ... → P₂ → P₁ → P₀ → A → 0 where each Pᵢ is projective (you know projective modules: they are the modules for which Hom(P, −) is exact, equivalently the direct summands of free modules). Remove A from the sequence. Tensor the remaining complex with B to get ... → P₂⊗B → P₁⊗B → P₀⊗B → 0. This tensored complex is generally no longer exact. Take its homology: Tor_n(A, B) = Hₙ(P_• ⊗ B). A key theorem establishes that this is independent of the choice of projective resolution, so Tor_n is well-defined.

The lowest cases give the most intuition. **Tor_0(A, B) = A ⊗ B**: the zeroth homology just recovers the original tensor product. **Tor_1(A, B)** is the most geometrically meaningful and gives Tor its name. For cyclic groups: Tor_1(ℤ/mℤ, ℤ/nℤ) ≅ ℤ/gcd(m,n)ℤ. This captures **torsion interaction**: two cyclic groups have non-trivial Tor₁ exactly when their orders share a common factor. The torsion in A interacts with the torsion in B in a way that is invisible to the tensor product itself (ℤ/mℤ ⊗ ℤ/nℤ ≅ ℤ/gcd(m,n)ℤ as well, but the information about the failure of exactness in the resolution is what Tor records at higher levels).

The flatness connection ties Tor back to module theory: A is **flat** if and only if Tor_n(A, B) = 0 for all n ≥ 1 and all B. Flat modules are precisely those for which tensoring preserves exact sequences — they are the "good" modules for tensor products, analogous to projective modules for Hom. Free modules are flat, projective modules are flat, but flatness is a strictly weaker condition (every projective is flat, but not conversely). In algebraic geometry, the fibers of a flat morphism vary "continuously" — Tor vanishing is the algebraic condition ensuring this geometric regularity. Higher Tor groups also appear in the Künneth formula for computing homology of product spaces, where Tor_1 terms correct for the non-exactness that can arise when the chain groups have torsion. Tor is, alongside Ext, one of the two fundamental invariants of homological algebra.
