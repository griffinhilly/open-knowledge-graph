---
id: third-isomorphism-theorem-groups
title: Third Isomorphism Theorem for Groups
domain: mathematics
course: abstract-algebra
prerequisites:
- id: first-isomorphism-theorem-groups
  type: hard
tags:
- isomorphism-theorem
- normal-subgroups
stage: advanced
status: draft
---

# Third Isomorphism Theorem for Groups

## Core Idea
If N and M are normal subgroups of G with N ⊆ M, then M/N is a normal subgroup of G/N, and (G/N)/(M/N) ≅ G/M.

## Explainer

The Third Isomorphism Theorem is easiest to understand through a familiar arithmetic analogy. Consider the integers ℤ, with the subgroups 2ℤ ⊆ 6ℤ. Here N = 6ℤ and M = 2ℤ. The quotient ℤ/6ℤ ≅ ℤ₆ is the integers mod 6. Inside ℤ₆, the subgroup 2ℤ/6ℤ = {0, 2, 4} ≅ ℤ₃ is the even residues mod 6. The theorem says (ℤ/6ℤ)/(2ℤ/6ℤ) ≅ ℤ/2ℤ — that is, ℤ₆ modulo its subgroup {0, 2, 4} gives ℤ₂. Check: ℤ₆/{0,2,4} has cosets {0,2,4} and {1,3,5}, giving a two-element group. And ℤ/2ℤ ≅ ℤ₂. The theorem is confirmed.

The intuition is cancellation, like fractions: (G/N)/(M/N) behaves like "G over M", with the N's cancelling. The N that was introduced into the denominator of both quotient groups washes out, leaving G/M. This is why the Third Isomorphism Theorem is sometimes stated as a "cancellation law" for quotient groups.

To prove it, the **First Isomorphism Theorem** is the main tool. You already know that if φ: G → H is a surjective homomorphism with kernel K, then G/K ≅ H. Here, define a map φ: G/N → G/M by φ(gN) = gM — that is, "re-coset" each coset of N into a coset of M. Because N ⊆ M, every coset of M is a union of cosets of N, so this map is well-defined. It is clearly surjective (every coset gM is hit). Its kernel consists of all cosets gN such that gM = eM, i.e., g ∈ M, i.e., gN ∈ M/N. So ker(φ) = M/N. By the First Isomorphism Theorem, (G/N)/ker(φ) ≅ G/M, which is exactly (G/N)/(M/N) ≅ G/M.

The practical significance is that the Third Isomorphism Theorem lets you "factor" quotient groups: instead of computing (G/N)/(M/N) directly, you can compute the simpler G/M. It also reinforces a general lesson in abstract algebra: the isomorphism theorems are not independent facts to memorize but a coherent family of tools built on the First Isomorphism Theorem and the kernel-image correspondence.
