---
id: cosets-and-lagrange-theorem
title: Cosets and Lagrange's Theorem
domain: mathematics
course: abstract-algebra
prerequisites:
- id: subgroups-and-subgroup-test
  type: hard
- id: order-of-group-element
  type: hard
builds-toward:
- normal-subgroups
- the-class-equation
tags:
- cosets
- lagrange
- order-divisibility
stage: advanced
status: draft
---

# Cosets and Lagrange's Theorem

## Core Idea
A left coset gH = {gh : h ∈ H} partitions G with all cosets having size |H|. Lagrange's theorem: |H| divides |G| and the number of cosets is |G|/|H|. This fundamental result constrains possible subgroup orders.

## Questions

```yaml
- question: "A student claims that the symmetric group S₄ (which has order 24) might contain a subgroup of order 7. How should you respond?"
  type: multiple-choice
  options:
    - "It is possible if those 7 elements happen to be closed under composition"
    - "It is impossible: by Lagrange's theorem, the order of any subgroup must divide the order of the group, and 7 does not divide 24"
    - "It is impossible only for abelian groups; S₄ is non-abelian so it might have unusual subgroups"
    - "You would need to list all elements of S₄ and check whether any 7 form a subgroup"
  answer: 1
  explanation: "Lagrange's theorem states that if H is a subgroup of a finite group G, then |H| divides |G|. The divisors of 24 are 1, 2, 3, 4, 6, 8, 12, and 24. Since 7 does not divide 24, no subgroup of order 7 can exist in S₄. This is a powerful constraint: instead of having to search through all possible subsets, Lagrange gives a necessary condition that eliminates most candidates instantly. Note that Lagrange's theorem is a one-way result — it says which orders are *impossible*, not which possible orders are actually achieved."

- question: "In a group G whose order is a prime number p, what must be true of every non-identity element?"
  type: multiple-choice
  options:
    - "Every non-identity element has order 2, making G isomorphic to ℤ/2ℤ"
    - "Every non-identity element generates a proper non-trivial subgroup of order strictly between 1 and p"
    - "Every non-identity element has order p, so it generates all of G — making G cyclic"
    - "The elements may have various orders, but their orders must all divide p"
  answer: 2
  explanation: "By Lagrange's theorem, the order of any element g (i.e., the order of the cyclic subgroup ⟨g⟩) must divide |G| = p. Since p is prime, the only divisors of p are 1 and p. A non-identity element has order greater than 1, so its order must be exactly p. This means every non-identity element generates all of G — the group has no proper non-trivial subgroups and is necessarily cyclic (isomorphic to ℤ/pℤ). This is one of the most striking consequences of Lagrange's theorem: it completely classifies groups of prime order."

- question: "Two distinct left cosets of a subgroup H in G can share some elements without being identical — partial overlap is possible."
  type: true-false
  answer: false
  explanation: "Cosets are either identical or completely disjoint — they never partially overlap. The proof: suppose cosets gH and g'H share an element x = gh₁ = g'h₂. Then g = g'h₂h₁⁻¹ ∈ g'H, which forces gH = g'H (every element of gH is also in g'H and vice versa). This all-or-nothing property is what makes cosets a *partition* of G: every element of G belongs to exactly one coset, and the cosets tile G into non-overlapping, equal-sized blocks. The counting argument of Lagrange's theorem depends entirely on this partition structure."

- question: "If G is a group of order 12, then subgroups of G can only have orders 1, 2, 3, 4, 6, or 12."
  type: true-false
  answer: true
  explanation: "Lagrange's theorem: |H| divides |G| = 12. The positive divisors of 12 are 1, 2, 3, 4, 6, and 12. Any subgroup of G must have order from this list. Note: Lagrange's theorem gives a necessary condition, not a sufficient one — not every divisor of 12 is necessarily the order of some subgroup (that is the content of converse theorems like Cauchy's and Sylow's). But Lagrange rules out all other orders: there is provably no subgroup of order 5, 7, 8, 9, 10, or 11 in any group of order 12."

- question: "Explain the counting argument that proves Lagrange's theorem: why must the order of every subgroup H divide the order of G?"
  type: short-answer
  answer: "The key is that left cosets partition G. Two cosets are either identical or disjoint, and every element of G belongs to exactly one coset (since g ∈ gH for all g, as g = g·e). Each coset gH has exactly |H| elements, because the map h ↦ gh is a bijection from H to gH. So G is tiled into k disjoint cosets, each of size |H|. Counting all elements: |G| = k·|H|, where k = [G:H] is the number of distinct cosets. Therefore |H| divides |G|, and k = |G|/|H|."
  explanation: "The elegance of the proof is that it uses only two facts: cosets partition G (disjoint, exhaustive), and all cosets have the same size as H (via the bijection h ↦ gh). No algebraic machinery beyond the definition of a coset is needed — it is a pure counting argument."
```

## Explainer

You already know that a subgroup H of G is a subset closed under the group operation and containing inverses and the identity. Now ask a different question: how does H relate to the rest of G? The answer is through **cosets**. The left coset of H by an element g is the set gH = {gh : h ∈ H} — you take every element of H and multiply it on the left by g. When g is itself in H, gH = H. When g is not in H, gH is a translated copy of H sitting somewhere else in G.

Here is the key structural fact: two cosets are either identical or completely disjoint. They never overlap partially. To see why, suppose gH and g'H share an element x = gh₁ = g'h₂. Then g = g'h₂h₁⁻¹, which means g is in g'H, and you can show this forces gH = g'H entirely. Since every element of G belongs to exactly one coset (g itself is in gH because g = g·e), the cosets partition G into equal-sized, non-overlapping blocks. Each block has exactly |H| elements, because the map h ↦ gh is a bijection from H to gH.

**Lagrange's Theorem** now follows by counting. G is partitioned into some number of cosets, say k of them. Each coset has |H| elements. Since they're disjoint and cover all of G, we have |G| = k · |H|, so k = |G|/|H|. In particular, |H| must divide |G|. This is the theorem: *the order of every subgroup divides the order of the group*. The number k of distinct cosets is called the **index** of H in G, written [G : H].

The consequences are powerful. From your prerequisite on element orders, you know the **order of an element** g — the smallest positive n with gⁿ = e — generates a cyclic subgroup ⟨g⟩ of order n inside G. By Lagrange's theorem, |⟨g⟩| = ord(g) divides |G|. This means: in any finite group of order n, every element satisfies gⁿ = e. It also means that a group whose order is prime p can have no proper non-trivial subgroups, since the only divisors of p are 1 and p itself — such a group must be cyclic. Lagrange's theorem turns divisibility arithmetic into a structural constraint on what subgroups and elements can exist.
