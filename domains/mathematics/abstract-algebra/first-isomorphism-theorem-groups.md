---
id: first-isomorphism-theorem-groups
title: First Isomorphism Theorem for Groups
domain: mathematics
course: abstract-algebra
prerequisites:
- id: quotient-groups
  type: hard
builds-toward:
- second-isomorphism-theorem-groups
- third-isomorphism-theorem-groups
tags:
- isomorphism-theorem
- fundamental-theorem
- kernel
- image
stage: advanced
status: draft
---

# First Isomorphism Theorem for Groups

## Core Idea
If φ: G → H is a group homomorphism, then G/ker(φ) ≅ im(φ). This theorem connects quotient groups and images of homomorphisms.

## Explainer

The First Isomorphism Theorem is one of the central structural results in group theory. It tells you that when a homomorphism φ: G → H cannot be injective — because multiple elements of G map to the same element of H — the "reason" for that collision is always the kernel. The **kernel** ker(φ) = {g ∈ G : φ(g) = e_H} is a normal subgroup of G, and it captures exactly the elements that get "crushed to the identity" by φ. Any two elements g₁ and g₂ with the same image — φ(g₁) = φ(g₂) — differ by a kernel element: g₂ = g₁k for some k ∈ ker(φ). So the kernel completely describes the collisions.

Your prerequisite knowledge of quotient groups is the key ingredient. The quotient group G/ker(φ) takes G and glues together everything that φ sends to the same place — creating one coset gK (where K = ker(φ)) for each "equivalence class" of elements sharing an image. The theorem says this collapsing operation produces a group genuinely isomorphic to the image im(φ) ≤ H. The isomorphism is the map φ̄: G/ker(φ) → im(φ) defined by φ̄(gK) = φ(g). This is well-defined precisely because any two representatives of gK have the same image under φ.

A concrete example makes this vivid. Let φ: ℤ → ℤ/3ℤ be the reduction-mod-3 map: φ(n) = n mod 3. The kernel is 3ℤ = {…, −6, −3, 0, 3, 6, …}, the multiples of 3. The quotient group ℤ/3ℤ on the left side of the isomorphism has three cosets: {3ℤ, 1+3ℤ, 2+3ℤ}. The image of φ is all of ℤ/3ℤ on the right. The theorem confirms these are isomorphic, and the isomorphism is immediate: coset k+3ℤ maps to k mod 3.

The deeper insight is a **dimension-like counting principle**. For finite groups, the theorem implies |G| = |ker(φ)| × |im(φ)|, since |G/ker(φ)| = |G|/|ker(φ)|. This is the group-theoretic analog of the rank-nullity theorem from linear algebra: the kernel (what collapses) and the image (what survives) together account for all of G. Every homomorphism factors as G surjecting onto G/ker(φ), followed by G/ker(φ) injecting isomorphically into H. The theorem makes this two-step factorization precise and universal — it applies to every group homomorphism, regardless of the specific groups involved.
