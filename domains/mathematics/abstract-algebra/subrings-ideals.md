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

## Questions

```yaml
- question: "Ring R = ℤ and subset I = 2ℤ (all even integers). A student claims 2ℤ is a subring but not an ideal because it doesn't contain the multiplicative identity 1. What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "The claim is correct — 2ℤ is a subring but not an ideal because ideals must contain 1"
    - "2ℤ is an ideal (it absorbs multiplication from outside ℤ) but not a subring, because it lacks the identity"
    - "2ℤ is an ideal — ideals do not need to contain the multiplicative identity, only to absorb ring multiplication"
    - "2ℤ is neither a subring nor an ideal because it is not closed under multiplication"
  answer: 2
  explanation: "Ideals do not require the multiplicative identity. The definition of an ideal I requires: (1) I is an additive subgroup, and (2) for all r ∈ R and a ∈ I, both ra and ar are in I. For I = 2ℤ and any integer r, the product r·(2k) = 2(rk) is even — so 2ℤ absorbs multiplication from all of ℤ. 2ℤ is also an additive subgroup. Therefore 2ℤ is an ideal. It is NOT a subring under the convention requiring the multiplicative identity (since 1 ∉ 2ℤ), but it is perfectly valid as an ideal."

- question: "Why can't you form a quotient ring R/S using a subring S the way you can form a quotient group using a normal subgroup?"
  type: multiple-choice
  options:
    - "You can — any subring produces a valid quotient ring"
    - "Coset multiplication (r + S)(s + S) = rs + S is not well-defined unless S absorbs multiplication from all of R"
    - "Subring cosets don't partition R properly, so the quotient set isn't well-defined"
    - "Quotient rings require the subring to be commutative, but not all subrings are"
  answer: 1
  explanation: "For coset multiplication to be well-defined, we need: if r ≡ r' (mod S) and s ≡ s' (mod S), then rs ≡ r's' (mod S). This requires that for any a ∈ S and r ∈ R, the product ra ∈ S — the absorption property of ideals. A subring S is closed under multiplication of its own elements, but rs (for r ∉ S, a ∈ S) need not land in S. Without the absorption property, different representatives of the same coset give different coset products, and the ring structure on R/S collapses. Ideals are exactly the substructure that makes quotient ring multiplication well-defined."

- question: "The kernel of any ring homomorphism is always a two-sided ideal."
  type: true-false
  answer: true
  explanation: "If φ: R → S is a ring homomorphism and a ∈ ker(φ), then for any r ∈ R: φ(ra) = φ(r)φ(a) = φ(r)·0 = 0, so ra ∈ ker(φ). Similarly ar ∈ ker(φ). The kernel is also an additive subgroup (homomorphisms preserve subtraction). So ker(φ) satisfies all the conditions of a two-sided ideal. Conversely, for every ideal I ⊆ R, the quotient map R → R/I is a ring homomorphism with kernel I. This bijection between ideals and kernels is the central fact of ring theory."

- question: "Every ideal in a ring is also a subring of that ring."
  type: true-false
  answer: false
  explanation: "This depends on the definition of subring. If subrings are required to contain the multiplicative identity 1 (the most common modern convention), then an ideal I ≠ R typically does not contain 1 — since if 1 ∈ I, then r·1 = r ∈ I for all r ∈ R, forcing I = R. So a proper ideal fails the subring test under this convention. Even under the weaker convention that subrings need not contain 1, an ideal is also a subring, but the more important point is that ideals and subrings serve different structural roles: ideals are the kernels of homomorphisms and the right notion for quotient constructions; subrings are rings in their own right but cannot generally support quotient structures."

- question: "Why is the absorption property of an ideal — that ra ∈ I and ar ∈ I for all r ∈ R — exactly the right condition to make the quotient R/I a well-defined ring, and why does the weaker closure condition of a subring fall short?"
  type: short-answer
  answer: "The absorption property guarantees that coset multiplication is independent of which representative you choose. If a ∈ I and r ∈ R, then (r + a)s = rs + as, and as ∈ I (by absorption), so rs + as lands in the same coset as rs. Without absorption, choosing a different representative of a coset (by adding an element of I) could shift the product to a different coset, making multiplication ill-defined. A subring S is only closed under multiplication of two elements already in S; it says nothing about r·a when r ∉ S. This means the coset product (r + S)(s + S) = rs + S can be ambiguous, because adding an element of S to r before multiplying by s produces rs + (element of S)·s, and that element of S times s need not stay in S."
  explanation: "The algebraic moral: quotient constructions always require the substructure to 'absorb' the action of the ambient structure. In groups, normal subgroups absorb conjugation (gNg⁻¹ ⊆ N), enabling well-defined quotient group multiplication. In rings, ideals absorb multiplication from outside (rI ⊆ I), enabling well-defined quotient ring multiplication. The ring analogy of 'normal subgroup' is precisely 'ideal' — not 'subring.'"
```

## Explainer

When you studied ring homomorphisms, you learned that a ring homomorphism φ: R → S preserves both addition and multiplication. The kernel of φ — the set of elements mapping to 0 in S — is not just a subgroup under addition; it absorbs multiplication from outside: if a ∈ ker(φ) and r ∈ R, then φ(ra) = φ(r)φ(a) = φ(r) · 0 = 0, so ra ∈ ker(φ). This absorbing property is exactly the definition of an **ideal**, and understanding it as the kernel of a homomorphism is the most illuminating way to grasp why ideals are the "right" notion of substructure for rings.

A **subring** is the weaker notion: a subset closed under addition, subtraction, and multiplication, and containing the multiplicative identity. Every subring is a ring in its own right. But subrings are not the natural building block for constructing quotient structures, because a coset decomposition R/S by a subring S doesn't generally support a well-defined ring multiplication. An **ideal** I ⊆ R strengthens the subring condition by requiring ra ∈ I and ar ∈ I for every r ∈ R and a ∈ I — this absorption property is precisely what makes the quotient R/I a well-defined ring, with coset multiplication (r + I)(s + I) = rs + I.

The distinction between **left ideals** (ra ∈ I), **right ideals** (ar ∈ I), and **two-sided ideals** (both) matters only in non-commutative rings. In commutative rings — the integers, polynomial rings, most familiar examples — all three coincide. The integers provide the prototype: every ideal in ℤ is of the form nℤ = {0, ±n, ±2n, ...} for some non-negative integer n. These are the kernels of the homomorphisms ℤ → ℤ/nℤ. So an ideal in ℤ is just a set of multiples of a fixed number.

The theorem that ideals are precisely the kernels of ring homomorphisms is the heart of the matter. For every ideal I in R, there is a canonical surjective homomorphism R → R/I whose kernel is exactly I. Conversely, the kernel of any ring homomorphism is always an ideal. This correspondence makes ideals the ring-theoretic analogue of normal subgroups in group theory — they are precisely the structure that quotient constructions require. When you go on to study maximal ideals and prime ideals, their defining properties (the quotient is a field; the quotient is an integral domain) are stated entirely in terms of this quotient ring construction.
