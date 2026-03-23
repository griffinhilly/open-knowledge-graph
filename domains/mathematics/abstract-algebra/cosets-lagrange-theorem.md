---
id: cosets-lagrange-theorem
title: Cosets and Lagrange's Theorem
domain: mathematics
course: abstract-algebra
prerequisites:
- id: group-isomorphisms
  type: hard
- id: subgroups-subgroup-test
  type: hard
builds-toward:
- normal-subgroups
- quotient-groups
tags:
- cosets
- index
- lagrange
- order-divides
stage: advanced
status: validated
---

# Cosets and Lagrange's Theorem

## Core Idea
A left coset of subgroup H in group G is a set of the form aH = {ah : h ∈ H}. Cosets partition G into equal-sized disjoint subsets. Lagrange's theorem states that the order of H divides the order of G, and [G : H] = |G| / |H| is the index of H in G.

## Questions

```yaml
- question: "A student claims that Z₁₅ (integers mod 15 under addition) might contain a subgroup of order 4. What is wrong with this?"
  type: multiple-choice
  options:
    - "Z₁₅ is not a valid group because 15 is not prime"
    - "By Lagrange's theorem, the order of any subgroup must divide the order of the group; 4 does not divide 15, so no such subgroup can exist"
    - "Z₁₅ is cyclic, so it can only contain subgroups of prime order"
    - "Subgroups of abelian groups must have the same parity as the group order"
  answer: 1
  explanation: "Lagrange's theorem states that |H| divides |G| for any subgroup H of finite group G. Since |Z₁₅| = 15 and 4 does not divide 15, no subgroup of order 4 can exist. You don't need to search for one — the divisibility constraint alone rules it out. The valid candidate orders are the divisors of 15: 1, 3, 5, and 15."

- question: "In a group G of order 35, an element g satisfies g⁷ = e. What are the possible orders of g?"
  type: multiple-choice
  options:
    - "Any divisor of 35: so 1, 5, 7, or 35"
    - "Exactly 7, since g⁷ = e and 7 is the smallest such exponent"
    - "1 or 7 — the order must divide both |G| = 35 and 7 (since g⁷ = e), and the only common divisors are 1 and 7"
    - "35, since every element of a group of order 35 must generate the whole group"
  answer: 2
  explanation: "Two constraints apply simultaneously. First, by Lagrange's theorem, the order of g divides |G| = 35, so the order is among {1, 5, 7, 35}. Second, g⁷ = e means the order of g divides 7 (the order is the smallest positive integer n with gⁿ = e, and it must divide any n where gⁿ = e). Divisors of 7 are 1 and 7. The order must satisfy both constraints, so it lies in {1, 5, 7, 35} ∩ {1, 7} = {1, 7}."

- question: "A left coset aH is itself a subgroup of G whenever a is not in H."
  type: true-false
  answer: false
  explanation: "A coset aH is a subgroup only when aH = H, which happens exactly when a ∈ H. If a ∉ H, then the identity element e ∉ aH: if e were in aH, we'd have e = ah for some h ∈ H, giving a = h⁻¹ ∈ H — a contradiction. Without the identity, aH cannot be a subgroup. Cosets are translates of H (same shape, different location in G), not copies of H's group structure."

- question: "In any finite group, the order of every element must divide the order of the group."
  type: true-false
  answer: true
  explanation: "This is a direct corollary of Lagrange's theorem. Any element g generates a cyclic subgroup ⟨g⟩ = {e, g, g², ..., g^(ord(g)−1)}, which has order equal to the order of g. By Lagrange's theorem, this subgroup's order divides |G|. Therefore the order of g divides |G|. This is one of the most useful immediate consequences of the coset partition argument."

- question: "Why do the cosets of H partition G into equal-sized, non-overlapping subsets? What is the key argument that two cosets are either identical or completely disjoint?"
  type: short-answer
  answer: "Every element a ∈ G belongs to at least one coset (its own: a = ae ∈ aH since e ∈ H). The key disjointness argument: if x belongs to both aH and bH, then x = ah₁ = bh₂ for some h₁, h₂ ∈ H. This gives a = bh₂h₁⁻¹ ∈ bH (since H is closed under multiplication and inverses), so a ∈ bH, which means aH ⊆ bH. By symmetry bH ⊆ aH, so aH = bH. Any two cosets with a single element in common are identical; otherwise they are disjoint. Since every coset is a translate of H by one element, all cosets have exactly |H| elements, and they tile G perfectly: |G| = [G:H] · |H|."
  explanation: "This partition argument is the entire proof of Lagrange's theorem. The equal-size fact is immediate (right-multiplying H by a fixed element a is a bijection H → aH). The disjointness argument requires only the group axioms. Together they give a combinatorial proof of a deep divisibility result from pure structure."
```

## Explainer

Think of a **coset** as a "shifted copy" of the subgroup H. You already know from your study of subgroups that H is a subset of G closed under the group operation, and from group isomorphisms that structure can be preserved under mappings. A coset aH takes every element h of H and applies a fixed group element a to it on the left: aH = {ah : h ∈ H}. The result is not usually a subgroup itself — it is a translate of H, the same shape but sitting in a different part of G.

The crucial fact about cosets is that they **partition** the group: every element of G belongs to exactly one left coset of H. This follows from two observations. First, every a belongs to its own coset aH (since the identity e is in H, so ae = a ∈ aH). Second, any two cosets are either identical or completely disjoint — there is no partial overlap. You can verify this yourself: if x belongs to both aH and bH, then you can write x = ah₁ = bh₂, which means a and b are in the same coset. The cosets tile G perfectly, like congruence classes mod n tile the integers.

**Lagrange's Theorem** is the immediate payoff: since all cosets have the same size as H, and since they partition G without overlap, the number of cosets times |H| must equal |G|. In symbols, |G| = [G : H] · |H|, which means |H| divides |G|. This is a powerful divisibility constraint on subgroup orders. For example, a group of order 15 cannot have a subgroup of order 4 or 6 — only orders 1, 3, 5, and 15 are even candidates. This filters the possibilities before you do any detailed analysis.

The **index** [G : H] counts how many distinct cosets H has in G. For finite groups it equals |G|/|H|. For infinite groups (like the integers Z under the subgroup nZ), the index still makes sense — it counts the equivalence classes, which recover the familiar congruence classes mod n. Lagrange's theorem is the reason why the order of any group element divides the order of the group: the cyclic subgroup generated by an element has order equal to the element's order, and that subgroup's order must divide |G|. This connects cosets to the structure theory you will use throughout the rest of abstract algebra.
