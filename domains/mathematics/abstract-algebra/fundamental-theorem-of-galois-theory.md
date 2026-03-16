---
id: fundamental-theorem-of-galois-theory
title: Fundamental Theorem of Galois Theory
domain: mathematics
course: abstract-algebra
prerequisites:
- id: galois-groups
  type: hard
- id: normal-subgroups
  type: soft
builds-toward:
- insolvability-of-the-quintic
tags:
- galois-theory
- correspondence
- fundamental
stage: advanced
status: draft
---

# Fundamental Theorem of Galois Theory

## Core Idea
For Galois extension F/K, there is a bijection between intermediate fields E (K ⊆ E ⊆ F) and subgroups H of Gal(F/K), given by H ↔ F^H (the fixed field). Subgroups are normal iff corresponding fields are Galois extensions. The correspondence reverses inclusion.

## Explainer

The Fundamental Theorem of Galois Theory is a dictionary that translates field-theoretic questions into group-theoretic ones and back. You already know that a Galois group Gal(F/K) is the group of all field automorphisms of F that fix K pointwise — every element permutes the roots of the minimal polynomial while leaving the base field unchanged. The Fundamental Theorem reveals that this group encodes the complete structure of every intermediate field between K and F.

The correspondence works like this: for each subgroup H of Gal(F/K), define its **fixed field** F^H as the set of all elements of F that every automorphism in H leaves unchanged. This fixed field is an intermediate field sitting between K and F. Conversely, for each intermediate field E, you get the subgroup of Gal(F/K) consisting of all automorphisms that fix E. The theorem says these two operations — taking fixed fields and taking fixing subgroups — are inverses of each other, establishing a perfect bijection.

The most striking feature of this bijection is that it **reverses inclusion**: a larger subgroup corresponds to a smaller intermediate field, and vice versa. Think about why: if H is big (many automorphisms must all fix an element), then very few elements of F are fixed, so F^H is small. If H is small (fewer constraints), more elements can satisfy them, making F^H large. This reversal is not accidental — it mirrors the way index and degree are related: [Gal(F/K) : H] = [F^H : K].

The theorem also captures the qualitative difference between "nice" and "arbitrary" intermediate fields via normal subgroups. Recall from your study of normal subgroups that H is normal in G when it is closed under conjugation — gHg⁻¹ = H for all g in G. In the Galois correspondence, H is a normal subgroup of Gal(F/K) if and only if F^H is itself a Galois extension of K. In this case, the quotient group Gal(F/K)/H is isomorphic to Gal(F^H/K). This is the engine behind the theory of solvable equations: the question of whether a polynomial's roots can be expressed in radicals reduces to whether the Galois group has a particular chain of normal subgroups — a **composition series** through solvable groups. The field/subgroup dictionary converts a geometric question about fields into a purely algebraic question about group structure.
