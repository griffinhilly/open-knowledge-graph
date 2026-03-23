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
status: validated
---

# Second Isomorphism Theorem for Groups

## Core Idea
Let H be a subgroup and N a normal subgroup of G. Then HN is a subgroup, N is normal in HN, and (HN)/N ≅ H/(H ∩ N).

## Questions

```yaml
- question: "In the proof of the Second Isomorphism Theorem, the map φ: H → (HN)/N is defined by φ(h) = hN. What is the kernel of this map?"
  type: multiple-choice
  options:
    - "All of N, since N is normal in G"
    - "H ∩ N, since ker(φ) = {h ∈ H : hN = N} = {h ∈ H : h ∈ N}"
    - "HN, since every element of HN maps to the identity coset"
    - "The trivial subgroup {e}, since φ is always injective"
  answer: 1
  explanation: "The kernel consists of h ∈ H such that hN = N (the identity coset of (HN)/N). This holds if and only if h ∈ N. Since we only consider h ∈ H, the kernel is {h ∈ H : h ∈ N} = H ∩ N. The first isomorphism theorem then gives H/ker(φ) = H/(H ∩ N) ≅ im(φ) = (HN)/N. N itself is not the kernel because φ is defined on H, not on all of G — elements of N that lie outside H are not in the domain of φ at all."

- question: "Suppose H and N are both subgroups of G but N is NOT normal in G. Which conclusion of the Second Isomorphism Theorem fails first?"
  type: multiple-choice
  options:
    - "N fails to be a subgroup of HN"
    - "HN may fail to be a subgroup of G at all"
    - "H ∩ N may fail to be a subgroup"
    - "The map φ(h) = hN fails to be well-defined"
  answer: 1
  explanation: "For HN to be a subgroup, it must be closed under multiplication. A product (h₁n₁)(h₂n₂) must be expressible as an element of HN. We can write this as h₁(n₁h₂)n₂ = h₁h₂(h₂⁻¹n₁h₂)n₂. For this to land in HN, we need h₂⁻¹n₁h₂ ∈ N — exactly the normality condition on N. Without normality, products of elements of HN can escape HN, so HN is not guaranteed to be a subgroup. The other conclusions also fail downstream, but closure of HN fails first."

- question: "For finite groups, the Second Isomorphism Theorem implies that if H ∩ N = {e}, then |HN| = |H| · |N|."
  type: true-false
  answer: true
  explanation: "From (HN)/N ≅ H/(H ∩ N), we get |HN|/|N| = |H|/|H ∩ N|, so |HN| = |H| · |N| / |H ∩ N|. When H ∩ N = {e}, this gives |HN| = |H| · |N| / 1 = |H| · |N|. This counting formula is one of the most useful consequences of the theorem for finite groups."

- question: "If H ∩ N = {e} and N is normal in G, the Second Isomorphism Theorem guarantees that HN ≅ H × N (the direct product)."
  type: true-false
  answer: false
  explanation: "The theorem gives (HN)/N ≅ H/(H ∩ N) ≅ H, which tells you HN/N ≅ H — a statement about the quotient. For HN to be isomorphic to the direct product H × N, you would additionally need H to be normal in HN (or in G). N is normal in HN by hypothesis, but H need not be. The theorem is silent on whether H is normal in HN; that requires further information about the group structure."

- question: "The Second Isomorphism Theorem is sometimes called the 'diamond isomorphism theorem.' Describe the diamond structure and explain what the isomorphism (HN)/N ≅ H/(H ∩ N) says about it."
  type: short-answer
  answer: "The four groups H ∩ N, H, N, and HN form a diamond in the subgroup lattice: H ∩ N sits at the bottom, H and N on the two sides, and HN at the top. The isomorphism says that the 'ratio' between HN and N (measuring how much bigger HN is than N) equals the 'ratio' between H and H ∩ N (measuring how much of H lies outside N). In other words, the two sides of the diamond are symmetric: quotienting out N from the top is equivalent to quotienting out the overlap H ∩ N from H."
  explanation: "This lattice perspective is the geometric heart of the theorem. The isomorphism doesn't just give an abstract group isomorphism — it reveals a symmetry in how the subgroups fit together. The 'ratio' interpretation (|HN|/|N| = |H|/|H ∩ N| for finite groups) is a direct consequence of this diamond symmetry and generalizes to infinite groups via the isomorphism itself."
```

## Explainer

The Second Isomorphism Theorem describes what happens when a subgroup H and a normal subgroup N interact inside a larger group G. You already know from the First Isomorphism Theorem that quotients and homomorphisms are deeply linked — this theorem extends that insight to a finer structural picture involving how two subgroups overlap and combine.

The setup: H is any subgroup of G and N is a normal subgroup. The theorem says three things at once. First, **HN = {hn : h ∈ H, n ∈ N}** is itself a subgroup of G (this wouldn't hold in general without N being normal). Second, N is normal inside HN (it was normal in all of G, so it's certainly normal in the smaller group HN). Third, and most importantly, there's an isomorphism **(HN)/N ≅ H/(H ∩ N)**. The key to proving this is the map φ: H → (HN)/N defined by φ(h) = hN. This map is a surjective homomorphism, and its kernel is {h ∈ H : hN = N} = H ∩ N. The First Isomorphism Theorem then delivers the result.

A concrete example: take G = Z₁₂, H = ⟨4⟩ = {0, 4, 8}, N = ⟨3⟩ = {0, 3, 6, 9}. Then HN contains both 4 and 3, and since gcd(3, 4) = 1 in Z₁₂ these generate all of Z₁₂, so HN = Z₁₂. Meanwhile H ∩ N = {0} (the two cyclic subgroups share only the identity). The theorem says Z₁₂/{0, 3, 6, 9} ≅ {0, 4, 8}/{0}, i.e., Z₃ ≅ Z₃ — the sizes match (4 elements on the left, 3 elements on the right... wait, Z₁₂/N has 3 cosets). The theorem keeps the "sizes" consistent: |HN|/|N| = |H|/|H ∩ N|.

The theorem is sometimes called the **diamond isomorphism theorem** because the four groups N, H, HN, and H ∩ N form a diamond shape in the subgroup lattice. The isomorphism (HN)/N ≅ H/(H ∩ N) says the "ratio" between HN and N equals the "ratio" between H and H ∩ N — a beautiful symmetry in the lattice structure of the group. This perspective becomes especially powerful when studying the correspondence theorem and the structure of quotient groups in more advanced algebra.
