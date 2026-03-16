---
id: sylow-theorems
title: Sylow Theorems
domain: mathematics
course: abstract-algebra
prerequisites:
- id: class-equation
  type: hard
builds-toward:
- applications-sylow-theorems
tags:
- sylow-p-subgroup
- sylow-theorems
- p-groups
stage: advanced
status: draft
---

# Sylow Theorems

## Core Idea
For a finite group G of order pᵏm with gcd(p, m) = 1, Sylow's theorems assert the existence of p-Sylow subgroups of order pᵏ, that all such subgroups are conjugate, and that the number of p-Sylow subgroups divides m and is ≡ 1 (mod p).

## Explainer

You came to the Sylow theorems through the **class equation**, which used conjugacy classes to count elements and extract information about a group's structure. The Sylow theorems push this counting machinery much further — they are the main tool for classifying finite groups and proving that groups of certain orders cannot be simple.

Write |G| = pᵏm where p is prime and p does not divide m. A **Sylow p-subgroup** is a subgroup of G of order exactly pᵏ — the largest power of p that divides |G|. The **First Sylow Theorem** guarantees these always exist: for every prime p dividing |G|, at least one Sylow p-subgroup exists. This extends Cauchy's theorem (which gave elements of prime order) to subgroups of prime-power order.

The **Second Sylow Theorem** says all Sylow p-subgroups are conjugate to each other: if P and Q are both Sylow p-subgroups, then Q = gPg⁻¹ for some g ∈ G. This is remarkable — all Sylow p-subgroups are isomorphic (as they're conjugate) even if there are many of them. The **Third Sylow Theorem** pins down how many there are: if nₚ denotes the number of Sylow p-subgroups, then nₚ divides m and nₚ ≡ 1 (mod p). These two constraints together are often enough to pin down nₚ exactly.

The power of the Sylow theorems is in the applications. For a concrete example, suppose |G| = 12 = 2² · 3. The number of Sylow 3-subgroups satisfies n₃ | 4 and n₃ ≡ 1 mod 3, so n₃ ∈ {1, 4}. The number of Sylow 2-subgroups satisfies n₂ | 3 and n₂ ≡ 1 mod 2, so n₂ ∈ {1, 3}. If n₃ = 4, then there are 4 × 2 = 8 elements of order 3, leaving only 4 elements for two Sylow 2-subgroups of order 4 — but two distinct subgroups of order 4 would require at least 5 elements (they must share the identity). This forces n₂ = 1 when n₃ = 4. A **unique** Sylow subgroup (nₚ = 1) is automatically **normal** — it equals its own conjugates. This is how the Sylow theorems reveal normal subgroups and, ultimately, whether a group must be a direct product of smaller groups.
