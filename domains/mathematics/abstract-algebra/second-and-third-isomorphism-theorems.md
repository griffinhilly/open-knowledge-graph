---
id: second-and-third-isomorphism-theorems
title: Second and Third Isomorphism Theorems
domain: mathematics
course: abstract-algebra
prerequisites:
- id: first-isomorphism-theorem-for-groups
  type: hard
tags:
- isomorphism-theorems
- subgroups
- structure
stage: advanced
status: draft
---

# Second and Third Isomorphism Theorems

## Core Idea
The second theorem: (S ∨ N)/N ≅ S/(S ∩ N) for S ≤ G and N ◁ G. The third: (G/M)/(N/M) ≅ G/N for M ⊆ N both normal. These theorems relate subgroup and quotient structures through isomorphisms.

## Explainer

The Second and Third Isomorphism Theorems extend the First Isomorphism Theorem to more complex situations involving subgroups and nested quotients. Rather than being standalone results, both are consequences of the first theorem applied in a structured way. Understanding them means recognizing the First Isomorphism Theorem operating in disguise — the key is identifying the right homomorphism and computing its kernel.

The **Second Isomorphism Theorem** concerns a subgroup S ≤ G and a normal subgroup N ◁ G. The product SN = {sn : s ∈ S, n ∈ N} is a subgroup of G (guaranteed because N is normal), and the theorem states (SN)/N ≅ S/(S ∩ N). The proof uses the First Isomorphism Theorem: define φ: S → (SN)/N by φ(s) = sN. This is a homomorphism, and its kernel is exactly S ∩ N (the elements of S that land in N, hence map to the identity coset). The image is all of (SN)/N, so the First Isomorphism Theorem gives S/(S ∩ N) ≅ (SN)/N. The intuition: N "absorbs" the part of S that overlaps with it, and what remains of S in the quotient is S modulo that overlap. To see it numerically: in ℤ₁₂, take S = {0, 4, 8} and N = {0, 6}. Then S ∩ N = {0}, SN = {0, 4, 6, 8, 2, 10}, and the isomorphism says (SN)/N ≅ S/{0} ≅ S, both groups of order 3.

The **Third Isomorphism Theorem** handles nested normal subgroups: if M ◁ G and N ◁ G with M ⊆ N, then N/M is normal in G/M, and (G/M)/(N/M) ≅ G/N. The intuition is "cancellation of quotients" — quotienting by M and then by N/M is equivalent to quotienting by N in one step. Think of it as fraction cancellation: (G/M)/(N/M) behaves like G/N. A number-theoretic example: G = ℤ, M = 6ℤ, N = 2ℤ. Then G/M = ℤ₆, N/M = {0̄, 2̄, 4̄} ≅ ℤ₃ inside ℤ₆, and (ℤ₆)/(ℤ₃) ≅ ℤ₂ = G/N. The proof again invokes the First Isomorphism Theorem, this time for the natural projection G/M → G/N.

Both theorems are tools for translating between different descriptions of the same group-theoretic structure. When confronted with a complicated quotient or an intersection of subgroups, they provide canonical rewritings that simplify further analysis. They appear constantly in deeper group theory — the Jordan-Hölder theorem and Sylow theory both require comparing quotients at different levels of a group's subgroup lattice — and in the isomorphism theorems for rings and modules, where the same patterns recur.
