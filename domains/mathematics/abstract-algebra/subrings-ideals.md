---
id: subrings-ideals
title: Subrings and Ideals
domain: mathematics
course: abstract-algebra
prerequisites:
- id: ring-homomorphisms
  type: hard
builds-toward:
- quotient-rings
- maximal-prime-ideals
tags:
- subring
- ideal
- left-ideal
- right-ideal
stage: advanced
status: draft
---

# Subrings and Ideals

## Core Idea
A subring is a subset of a ring that is closed under addition and multiplication. An ideal is an additive subgroup I such that ra, ar ∈ I for all r ∈ R and a ∈ I. Ideals are precisely the kernels of ring homomorphisms.

## Explainer

When you studied ring homomorphisms, you learned that a ring homomorphism φ: R → S preserves both addition and multiplication. The kernel of φ — the set of elements mapping to 0 in S — is not just a subgroup under addition; it absorbs multiplication from outside: if a ∈ ker(φ) and r ∈ R, then φ(ra) = φ(r)φ(a) = φ(r) · 0 = 0, so ra ∈ ker(φ). This absorbing property is exactly the definition of an **ideal**, and understanding it as the kernel of a homomorphism is the most illuminating way to grasp why ideals are the "right" notion of substructure for rings.

A **subring** is the weaker notion: a subset closed under addition, subtraction, and multiplication, and containing the multiplicative identity. Every subring is a ring in its own right. But subrings are not the natural building block for constructing quotient structures, because a coset decomposition R/S by a subring S doesn't generally support a well-defined ring multiplication. An **ideal** I ⊆ R strengthens the subring condition by requiring ra ∈ I and ar ∈ I for every r ∈ R and a ∈ I — this absorption property is precisely what makes the quotient R/I a well-defined ring, with coset multiplication (r + I)(s + I) = rs + I.

The distinction between **left ideals** (ra ∈ I), **right ideals** (ar ∈ I), and **two-sided ideals** (both) matters only in non-commutative rings. In commutative rings — the integers, polynomial rings, most familiar examples — all three coincide. The integers provide the prototype: every ideal in ℤ is of the form nℤ = {0, ±n, ±2n, ...} for some non-negative integer n. These are the kernels of the homomorphisms ℤ → ℤ/nℤ. So an ideal in ℤ is just a set of multiples of a fixed number.

The theorem that ideals are precisely the kernels of ring homomorphisms is the heart of the matter. For every ideal I in R, there is a canonical surjective homomorphism R → R/I whose kernel is exactly I. Conversely, the kernel of any ring homomorphism is always an ideal. This correspondence makes ideals the ring-theoretic analogue of normal subgroups in group theory — they are precisely the structure that quotient constructions require. When you go on to study maximal ideals and prime ideals, their defining properties (the quotient is a field; the quotient is an integral domain) are stated entirely in terms of this quotient ring construction.
