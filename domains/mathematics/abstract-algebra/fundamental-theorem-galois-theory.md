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
status: draft
---

# Fundamental Theorem of Galois Theory

## Core Idea
For a finite Galois extension K/F, there is a bijection between subgroups of Gal(K/F) and intermediate fields F ⊆ E ⊆ K. This bijection is order-reversing: larger subgroups correspond to smaller fields.

## Explainer

The Fundamental Theorem of Galois Theory is the crowning result of the Galois correspondence — it reveals a complete dictionary between algebra (subgroups of the Galois group) and the geometry of field extensions (intermediate fields). Since you have studied Galois groups, you know that Gal(K/F) is the group of field automorphisms of K that fix F pointwise. The theorem says this group encodes everything about the "landscape" of intermediate fields sitting between F and K.

The key word is **bijection**: every subgroup H of Gal(K/F) corresponds to exactly one intermediate field E = K^H (the **fixed field** of H), and every intermediate field corresponds to exactly one subgroup. Nothing is missed; nothing is duplicated. The fixed field K^H consists of all elements of K that every automorphism in H leaves unchanged. You can think of H as a "symmetry group" of K — the elements that H's symmetries cannot disturb form precisely the fixed field.

The **order-reversing** character is the most surprising feature. Bigger subgroup → smaller fixed field. Why? A larger subgroup has more automorphisms, and with more automorphisms imposing rigidity, fewer elements survive — so the fixed field shrinks. Conversely, a smaller subgroup has fewer constraints, allowing more elements to be fixed. Formally, |Gal(K/E)| = [K:E] and [E:F] = [Gal(K/F) : Gal(K/E)]. The field degrees and subgroup indices match exactly, quantifying the correspondence.

There is also a structural theorem for **normal subgroups**: H is normal in Gal(K/F) if and only if the fixed field E = K^H is itself a Galois extension of F. In that case, Gal(E/F) ≅ Gal(K/F)/H. Normal subgroups correspond to "nice" intermediate extensions — ones whose own Galois groups appear as quotients of the big Galois group. This is the algebraic link to the insolvability of the quintic: a polynomial is solvable by radicals if and only if its Galois group is solvable (has a chain of normal subgroups with abelian quotients), and the general quintic's Galois group S₅ is not solvable.
