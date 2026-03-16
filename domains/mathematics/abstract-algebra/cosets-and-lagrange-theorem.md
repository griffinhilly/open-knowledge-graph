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

## Explainer

You already know that a subgroup H of G is a subset closed under the group operation and containing inverses and the identity. Now ask a different question: how does H relate to the rest of G? The answer is through **cosets**. The left coset of H by an element g is the set gH = {gh : h ∈ H} — you take every element of H and multiply it on the left by g. When g is itself in H, gH = H. When g is not in H, gH is a translated copy of H sitting somewhere else in G.

Here is the key structural fact: two cosets are either identical or completely disjoint. They never overlap partially. To see why, suppose gH and g'H share an element x = gh₁ = g'h₂. Then g = g'h₂h₁⁻¹, which means g is in g'H, and you can show this forces gH = g'H entirely. Since every element of G belongs to exactly one coset (g itself is in gH because g = g·e), the cosets partition G into equal-sized, non-overlapping blocks. Each block has exactly |H| elements, because the map h ↦ gh is a bijection from H to gH.

**Lagrange's Theorem** now follows by counting. G is partitioned into some number of cosets, say k of them. Each coset has |H| elements. Since they're disjoint and cover all of G, we have |G| = k · |H|, so k = |G|/|H|. In particular, |H| must divide |G|. This is the theorem: *the order of every subgroup divides the order of the group*. The number k of distinct cosets is called the **index** of H in G, written [G : H].

The consequences are powerful. From your prerequisite on element orders, you know the **order of an element** g — the smallest positive n with gⁿ = e — generates a cyclic subgroup ⟨g⟩ of order n inside G. By Lagrange's theorem, |⟨g⟩| = ord(g) divides |G|. This means: in any finite group of order n, every element satisfies gⁿ = e. It also means that a group whose order is prime p can have no proper non-trivial subgroups, since the only divisors of p are 1 and p itself — such a group must be cyclic. Lagrange's theorem turns divisibility arithmetic into a structural constraint on what subgroups and elements can exist.
