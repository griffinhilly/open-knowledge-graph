---
id: fundamental-theorem-galois-theory
title: Fundamental Theorem of Galois Theory
domain: mathematics
course: abstract-algebra
prerequisites:
- id: galois-groups
  type: hard
builds-toward:
- insolvability-quintic
tags:
- galois-correspondence
- subgroups
- fixed-fields
stage: advanced
status: validated
---

# Fundamental Theorem of Galois Theory

## Core Idea
For a finite Galois extension K/F, there is a bijection between subgroups of Gal(K/F) and intermediate fields F ⊆ E ⊆ K. This bijection is order-reversing: larger subgroups correspond to smaller fields.

## Questions

```yaml
- question: "In the Galois extension ℚ(√2, √3)/ℚ, the Galois group has order 4. If H is a subgroup of order 2, what is the degree [E:ℚ] of the corresponding fixed field E?"
  type: multiple-choice
  options:
    - "2 — larger subgroup, larger fixed field"
    - "4 — subgroup index equals field degree"
    - "2 — the index [Gal:H] = 4/2 = 2 equals [E:ℚ]"
    - "1 — the entire field is fixed"
  answer: 2
  explanation: "The Fundamental Theorem states that [E:F] = [Gal(K/F) : H], the index of H in the full Galois group. With |Gal| = 4 and |H| = 2, the index is 2, so [E:ℚ] = 2. Option A names the right number but gives the wrong reason — it inverts the logic. The bijection is order-reversing: a subgroup of order 2 (large relative to index 2) corresponds to a small field of degree 2 over F, not a large one."

- question: "Suppose H is a normal subgroup of Gal(K/F) with fixed field E = K^H. Which of the following is guaranteed by the Fundamental Theorem?"
  type: multiple-choice
  options:
    - "E/F is an algebraic extension with no proper intermediate fields"
    - "E/F is itself a Galois extension, and Gal(E/F) ≅ Gal(K/F)/H"
    - "H must be abelian for E to be a Galois extension of F"
    - "Gal(K/E) is isomorphic to Gal(K/F)"
  answer: 1
  explanation: "The normal subgroup correspondence is the structural heart of the theorem: H is normal in Gal(K/F) if and only if the fixed field E = K^H is a Galois extension of F (not merely an arbitrary extension). In that case, the Galois group of E over F is the quotient Gal(K/F)/H. This is the link to solvability by radicals — a polynomial is solvable if and only if its Galois group has a chain of normal subgroups with abelian quotients. H need not itself be abelian (option C); it is the quotient that must be."

- question: "In the Galois correspondence, a larger subgroup of Gal(K/F) corresponds to a larger fixed field."
  type: true-false
  answer: false
  explanation: "The bijection is order-reversing — this is its most surprising feature. A larger subgroup H imposes more automorphisms on K, and with more symmetries acting, fewer elements of K survive unchanged. The fixed field K^H therefore shrinks: more constraints, smaller fixed set. Conversely, a small subgroup (few automorphisms) fixes many elements, producing a large intermediate field. The correct statement is: larger subgroup ↔ smaller fixed field, smaller subgroup ↔ larger fixed field."

- question: "If E is a Galois extension of F and F ⊆ E ⊆ K is an intermediate field in a Galois extension K/F, then the subgroup Gal(K/E) is normal in Gal(K/F)."
  type: true-false
  answer: true
  explanation: "This is exactly the normal subgroup correspondence: H is normal in Gal(K/F) if and only if the fixed field K^H is a Galois extension of F. Equivalently, an intermediate field E gives rise to a normal subgroup Gal(K/E) precisely when E/F is itself Galois. The direction stated here is correct — a Galois intermediate extension E/F corresponds to a normal subgroup. The converse also holds."

- question: "Why is the order-reversing character of the Galois correspondence not a coincidence but a reflection of the relationship between automorphisms and fixed elements?"
  type: short-answer
  answer: "A subgroup H consists of automorphisms of K — symmetries that permute elements while fixing F. The fixed field K^H is exactly the set of elements that all of H's automorphisms leave unchanged. The more automorphisms H contains, the more rigidly it acts on K, and the smaller the set of elements that survive every one of H's symmetries. So a larger H means fewer elements escape all automorphisms, giving a smaller K^H. Conversely, a tiny subgroup with only the identity automorphism fixes everything — the full field K. The correspondence reverses order because bigger symmetry group means smaller invariant set."
  explanation: "This is not a formal trick but a direct consequence of what fixed fields measure. The identity subgroup {e} fixes all of K, giving fixed field K itself (maximum). The full Galois group Gal(K/F) fixes precisely F (minimum). Every intermediate subgroup gives an intermediate field, and the containment relationship inverts. Seeing this logic removes the need to memorize the direction — it follows from what 'being fixed by automorphisms' means."
```

## Explainer

The Fundamental Theorem of Galois Theory is the crowning result of the Galois correspondence — it reveals a complete dictionary between algebra (subgroups of the Galois group) and the geometry of field extensions (intermediate fields). Since you have studied Galois groups, you know that Gal(K/F) is the group of field automorphisms of K that fix F pointwise. The theorem says this group encodes everything about the "landscape" of intermediate fields sitting between F and K.

The key word is **bijection**: every subgroup H of Gal(K/F) corresponds to exactly one intermediate field E = K^H (the **fixed field** of H), and every intermediate field corresponds to exactly one subgroup. Nothing is missed; nothing is duplicated. The fixed field K^H consists of all elements of K that every automorphism in H leaves unchanged. You can think of H as a "symmetry group" of K — the elements that H's symmetries cannot disturb form precisely the fixed field.

The **order-reversing** character is the most surprising feature. Bigger subgroup → smaller fixed field. Why? A larger subgroup has more automorphisms, and with more automorphisms imposing rigidity, fewer elements survive — so the fixed field shrinks. Conversely, a smaller subgroup has fewer constraints, allowing more elements to be fixed. Formally, |Gal(K/E)| = [K:E] and [E:F] = [Gal(K/F) : Gal(K/E)]. The field degrees and subgroup indices match exactly, quantifying the correspondence.

There is also a structural theorem for **normal subgroups**: H is normal in Gal(K/F) if and only if the fixed field E = K^H is itself a Galois extension of F. In that case, Gal(E/F) ≅ Gal(K/F)/H. Normal subgroups correspond to "nice" intermediate extensions — ones whose own Galois groups appear as quotients of the big Galois group. This is the algebraic link to the insolvability of the quintic: a polynomial is solvable by radicals if and only if its Galois group is solvable (has a chain of normal subgroups with abelian quotients), and the general quintic's Galois group S₅ is not solvable.
