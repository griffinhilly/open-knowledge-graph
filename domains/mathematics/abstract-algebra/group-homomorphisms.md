---
id: group-homomorphisms
title: Group Homomorphisms
domain: mathematics
course: abstract-algebra
prerequisites:
- id: group-basic-properties
  type: hard
builds-toward:
- group-isomorphisms
- cosets-lagrange-theorem
- normal-subgroups
tags:
- homomorphisms
- structure-preserving
- kernel
- image
stage: advanced
status: draft
---

# Group Homomorphisms

## Core Idea
A group homomorphism φ: G → H preserves the group operation: φ(ab) = φ(a)φ(b). The kernel ker(φ) = {a ∈ G : φ(a) = e} is a normal subgroup, and the image im(φ) is a subgroup of H. Homomorphisms reveal the underlying structure of groups.

## Explainer

A group homomorphism is a map that respects the group operation — if you combine two elements first and then map the result, you get the same answer as mapping each element individually and then combining. This structural respect is what makes homomorphisms powerful: they let you transport information from one group to another while preserving the algebraic relationships you care about. The defining equation φ(ab) = φ(a)φ(b) says that the map commutes with the operation.

From your study of group basic properties, you know a group has an identity element and every element has an inverse. The homomorphism property automatically preserves both: φ(e_G) = e_H (the identity maps to the identity), and φ(a⁻¹) = φ(a)⁻¹ (inverses map to inverses). These aren't additional requirements — they follow for free from the single defining equation. This is a recurring theme in algebra: a small structural requirement implies a cascade of consequences.

The two most important objects associated to a homomorphism are its **kernel** and its **image**. The kernel ker(φ) = {a ∈ G : φ(a) = e_H} is the set of elements that get "collapsed" to the identity in H. The image im(φ) is the subset of H that φ actually reaches. Both are subgroups — the kernel is a subgroup of G, and the image is a subgroup of H. The kernel has an extra property that the image lacks: it is a **normal subgroup**, meaning gker(φ)g⁻¹ = ker(φ) for every g ∈ G. This normality is not an accident; it is precisely what allows you to build a quotient group G/ker(φ) and identify it with the image.

To make this concrete: consider the map φ: ℤ → ℤ/nℤ that sends each integer to its remainder mod n. This is a homomorphism because φ(a + b) = (a + b) mod n = ((a mod n) + (b mod n)) mod n = φ(a) + φ(b). Its kernel is the set of multiples of n (those integers that map to 0), and its image is all of ℤ/nℤ. The homomorphism exactly encodes what modular arithmetic does to the integers. Recognizing the abstract homomorphism structure in this familiar operation is the moment the definition shifts from symbol-shuffling into genuine understanding — and prepares you for the First Isomorphism Theorem, which makes the G/ker(φ) ≅ im(φ) relationship precise.
