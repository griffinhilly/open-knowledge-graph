---
id: first-isomorphism-theorem-for-groups
title: First Isomorphism Theorem for Groups
domain: mathematics
course: abstract-algebra
prerequisites:
- id: quotient-groups
  type: hard
- id: group-isomorphisms
  type: hard
builds-toward:
- second-and-third-isomorphism-theorems
tags:
- isomorphism-theorems
- fundamental
- structure
stage: advanced
status: draft
---

# First Isomorphism Theorem for Groups

## Core Idea
If φ: G → H is a homomorphism, then G/ker(φ) ≅ im(φ). Every homomorphism factors through a quotient by its kernel. This fundamental theorem connects quotient groups to isomorphisms and reveals homomorphism structure.

## Explainer

You already know two things: how to build quotient groups G/N by collapsing a normal subgroup N into a single identity element, and what it means for two groups to be isomorphic — a structure-preserving bijection between them. The First Isomorphism Theorem is the statement that these two ideas are secretly the same thing. Every homomorphism is, at its core, a quotient map followed by a relabeling.

Here is the key insight. When φ: G → H is a homomorphism, it sends every element of ker(φ) to the identity in H. So φ cannot distinguish between g and gk if k ∈ ker(φ) — they map to the same place. This means φ is really "seeing" the **cosets** of ker(φ), not the individual elements of G. The quotient group G/ker(φ) is precisely the structure you get when you declare "g and gk are the same thing." The theorem says that once you pass to that quotient, the induced map φ̄: G/ker(φ) → im(φ), defined by φ̄(gK) = φ(g), is an isomorphism — it is now bijective and still a homomorphism.

The factoring picture makes this vivid. The original map φ: G → H factors as G → G/ker(φ) → im(φ) → H, where the first arrow is the quotient map (collapsing), the middle arrow is the isomorphism φ̄, and the last arrow is the inclusion of im(φ) into H. The hard part of the proof is checking that φ̄ is well-defined (the coset representative doesn't matter), injective (different cosets map to different images), surjective onto im(φ) (clear from definition), and a homomorphism (inherited from φ). Each step follows directly from the definition of kernel and coset multiplication.

The theorem has an important corollary you will use constantly: if φ is surjective, then im(φ) = H, so G/ker(φ) ≅ H. This is the standard way to prove two groups are isomorphic — find a surjective homomorphism from one to the other, then compute the kernel. For example, the map ℝ → ℝ/ℤ (real numbers mod 1) shows ℝ/ℤ is isomorphic to the circle group. The map ℤ → ℤ/nℤ shows integers mod n are a quotient of the integers. In each case, the First Isomorphism Theorem tells you exactly which quotient gives the target group.
