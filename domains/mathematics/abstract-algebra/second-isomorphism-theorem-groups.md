---
id: second-isomorphism-theorem-groups
title: Second Isomorphism Theorem for Groups
domain: mathematics
course: abstract-algebra
prerequisites:
- id: first-isomorphism-theorem-groups
  type: hard
builds-toward:
- direct-products-groups
tags:
- isomorphism-theorem
- subgroups
- correspondence
stage: advanced
status: draft
---

# Second Isomorphism Theorem for Groups

## Core Idea
Let H be a subgroup and N a normal subgroup of G. Then HN is a subgroup, N is normal in HN, and (HN)/N ≅ H/(H ∩ N).

## Explainer

The Second Isomorphism Theorem describes what happens when a subgroup H and a normal subgroup N interact inside a larger group G. You already know from the First Isomorphism Theorem that quotients and homomorphisms are deeply linked — this theorem extends that insight to a finer structural picture involving how two subgroups overlap and combine.

The setup: H is any subgroup of G and N is a normal subgroup. The theorem says three things at once. First, **HN = {hn : h ∈ H, n ∈ N}** is itself a subgroup of G (this wouldn't hold in general without N being normal). Second, N is normal inside HN (it was normal in all of G, so it's certainly normal in the smaller group HN). Third, and most importantly, there's an isomorphism **(HN)/N ≅ H/(H ∩ N)**. The key to proving this is the map φ: H → (HN)/N defined by φ(h) = hN. This map is a surjective homomorphism, and its kernel is {h ∈ H : hN = N} = H ∩ N. The First Isomorphism Theorem then delivers the result.

A concrete example: take G = Z₁₂, H = ⟨4⟩ = {0, 4, 8}, N = ⟨3⟩ = {0, 3, 6, 9}. Then HN contains both 4 and 3, and since gcd(3, 4) = 1 in Z₁₂ these generate all of Z₁₂, so HN = Z₁₂. Meanwhile H ∩ N = {0} (the two cyclic subgroups share only the identity). The theorem says Z₁₂/{0, 3, 6, 9} ≅ {0, 4, 8}/{0}, i.e., Z₃ ≅ Z₃ — the sizes match (4 elements on the left, 3 elements on the right... wait, Z₁₂/N has 3 cosets). The theorem keeps the "sizes" consistent: |HN|/|N| = |H|/|H ∩ N|.

The theorem is sometimes called the **diamond isomorphism theorem** because the four groups N, H, HN, and H ∩ N form a diamond shape in the subgroup lattice. The isomorphism (HN)/N ≅ H/(H ∩ N) says the "ratio" between HN and N equals the "ratio" between H and H ∩ N — a beautiful symmetry in the lattice structure of the group. This perspective becomes especially powerful when studying the correspondence theorem and the structure of quotient groups in more advanced algebra.
