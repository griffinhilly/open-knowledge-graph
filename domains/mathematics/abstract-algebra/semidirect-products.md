---
id: semidirect-products
title: Semidirect Products
domain: mathematics
course: abstract-algebra
prerequisites:
  - id: normal-subgroups
    type: hard
  - id: direct-products-groups
    type: hard
  - id: group-homomorphisms
    type: hard
  - id: group-isomorphisms
    type: hard
  - id: dihedral-groups
    type: soft
builds-toward:
  - applications-of-sylow-theorems
tags: [abstract-algebra, group-theory, semidirect-product, automorphisms, group-construction]
stage: advanced
status: validated
---

# Semidirect Products

## Core Idea
A semidirect product builds a group from two groups N and H when H acts on N by automorphisms. Given a homomorphism φ: H → Aut(N), the semidirect product N ⋊_φ H is the set of pairs (n, h) with multiplication (n₁, h₁)(n₂, h₂) = (n₁·φ_{h₁}(n₂), h₁h₂). When φ is trivial this is the direct product; otherwise the result is a new, usually nonabelian, group. Internally, a group G is a semidirect product of N and H when N is normal, H is a subgroup, N ∩ H = {e} and NH = G.

## How It's Best Learned
Start with the dihedral group D_n, where rotations form a normal cyclic subgroup and a reflection conjugates each rotation to its inverse. Rewrite D_n as ℤ_n ⋊ ℤ_2 and check that the multiplication rule reproduces its familiar relations. Then construct new groups by listing the homomorphisms ℤ_p → Aut(ℤ_q) ≅ ℤ_q^×, for example the nonabelian group of order 21. Compare with direct products to see what the twisting changes.

## Common Misconceptions
- If G has a normal subgroup N and a subgroup H with N ∩ H = {e} and NH = G, then G ≅ N × H. (That needs H to be normal as well; with only N normal, G is a semidirect product, as S_3 ≅ ℤ_3 ⋊ ℤ_2 shows.)
- The semidirect product of N and H depends only on N and H. (It depends on the action φ; different actions can give non-isomorphic groups, and the trivial action gives the direct product.)
- Any normal subgroup N of G has a complement H making G a semidirect product. (ℤ_4 has normal subgroup {0, 2} but no subgroup of order 2 meeting it trivially, so ℤ_4 is not a semidirect product of ℤ_2 by ℤ_2.)

## Questions

```yaml
- question: "In D_n = ℤ_n ⋊ ℤ_2, how does the generator of ℤ_2 act on ℤ_n?"
  type: multiple-choice
  options:
    - "Trivially: k ↦ k"
    - "By inversion: k ↦ -k"
    - "By doubling: k ↦ 2k"
    - "By adding 1: k ↦ k + 1"
  answer: 1
  explanation: "A reflection s satisfies s r s⁻¹ = r⁻¹ for each rotation r, so conjugation by s inverts rotations. In additive notation on ℤ_n this is k ↦ -k, which is an automorphism. Adding 1 is not a homomorphism, and the trivial action would give the abelian group ℤ_n × ℤ_2."

- question: "If N is normal in G, H is a subgroup, N ∩ H = {e} and NH = G, then G is isomorphic to the direct product N × H."
  type: true-false
  answer: false
  explanation: "These conditions make G an internal semidirect product. G is the direct product only if H is also normal, which is equivalent to the conjugation action of H on N being trivial. S_3 has normal subgroup A_3 ≅ ℤ_3 and complement ⟨(1 2)⟩ ≅ ℤ_2, but S_3 is nonabelian, so it is not ℤ_3 × ℤ_2."

- question: "Explain why there is a nonabelian group of order 21 but no nonabelian group of the form ℤ_5 ⋊ ℤ_3."
  type: short-answer
  answer: "Aut(ℤ_7) ≅ ℤ_6 contains elements of order 3, so a nontrivial homomorphism ℤ_3 → Aut(ℤ_7) exists. Aut(ℤ_5) ≅ ℤ_4 has no element of order 3, so every homomorphism ℤ_3 → Aut(ℤ_5) is trivial and the product is ℤ_15."
  explanation: "A nontrivial action requires the order of a generator's image to divide both 3 and |Aut(N)|. Since 3 divides 6 but not 4, only ℤ_7 admits a twisted product with ℤ_3. This matches the general fact that a nonabelian group of order pq with p < q exists exactly when p divides q - 1."

- question: "Using the rule (n₁, h₁)(n₂, h₂) = (n₁·φ_{h₁}(n₂), h₁h₂), what is the inverse of (n, h)?"
  type: short-answer
  answer: "(φ_{h⁻¹}(n⁻¹), h⁻¹)"
  explanation: "Check: (n, h)(φ_{h⁻¹}(n⁻¹), h⁻¹) = (n·φ_h(φ_{h⁻¹}(n⁻¹)), e) = (n·n⁻¹, e) = (e, e), using φ_h ∘ φ_{h⁻¹} = φ_e = identity."
```

## Explainer

The direct product N × H combines two groups so that they do not interact: (n₁, h₁)(n₂, h₂) = (n₁n₂, h₁h₂). Many groups are built from smaller pieces that do interact. The semidirect product describes the most common kind of interaction, in which one factor acts on the other by automorphisms.

Look at the dihedral group D_n of symmetries of a regular n-gon. The rotations form a cyclic subgroup R ≅ ℤ_n, and R is normal. A single reflection s generates a subgroup S ≅ ℤ_2 with R ∩ S = {e} and RS = D_n. If D_n were R × S, rotations and reflections would commute. They do not: s r s⁻¹ = r⁻¹. Conjugation by s acts on R as an automorphism (inversion), and that action is what the direct product leaves out.

Here is the general construction. Let N and H be groups and φ: H → Aut(N) a homomorphism; write φ_h for the automorphism attached to h. Define N ⋊_φ H to be the set N × H with product

(n₁, h₁)(n₂, h₂) = (n₁·φ_{h₁}(n₂), h₁h₂).

When the H-part h₁ passes the N-part n₂, it changes n₂ by the automorphism φ_{h₁}. One can check that this operation is associative, that (e, e) is the identity, and that the inverse of (n, h) is (φ_{h⁻¹}(n⁻¹), h⁻¹). The copy N × {e} is normal, the copy {e} × H is a subgroup, and conjugating (n, e) by (e, h) gives (φ_h(n), e). So inside the new group, the abstract action becomes conjugation.

The internal version runs the other way. If G has a normal subgroup N and a subgroup H with N ∩ H = {e} and NH = G, then G ≅ N ⋊_φ H where φ_h(n) = hnh⁻¹. If the action is trivial, meaning H commutes with N, this reduces to the direct product.

Semidirect products are a main tool for building and classifying groups. Since Aut(ℤ_n) ≅ ℤ_n^×, actions of a cyclic group on a cyclic group are easy to list. For example, Aut(ℤ_7) ≅ ℤ_6 has elements of order 3, so ℤ_3 has a nontrivial action on ℤ_7, and ℤ_7 ⋊ ℤ_3 is a nonabelian group of order 21. Combined with the Sylow theorems, this shows that for primes p < q there is a nonabelian group of order pq exactly when p divides q - 1.
