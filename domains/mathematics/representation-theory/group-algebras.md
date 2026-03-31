---
id: group-algebras
title: Group Algebras
domain: mathematics
course: representation-theory
prerequisites:
- id: group-representations
  type: hard
- id: rings-and-ideals
  type: soft
builds-toward:
- semisimplicity-and-wedderburn
- regular-representation
tags:
- group-algebra
- modules
- convolution
- kG
stage: expert
status: validated
---

# Group Algebras

## Core Idea
The group algebra k[G] of a finite group G over a field k is the vector space with basis {eᵍ : g ∈ G} equipped with multiplication extending the group operation linearly: (Σ aᵍeᵍ)(Σ bₕeₕ) = Σ aᵍbₕe_{gh}. This construction translates group representation theory into module theory: a representation of G over k is precisely the same thing as a left k[G]-module. This equivalence is not merely a convenience — it unlocks the full machinery of ring theory (ideals, radicals, semisimplicity) for studying representations.

## Questions

```yaml
- question: "What is the dimension of the group algebra ℂ[S₃] as a vector space over ℂ?"
  type: multiple-choice
  options:
    - "3"
    - "6"
    - "9"
    - "36"
  answer: 1
  explanation: "dim(k[G]) = |G| as a k-vector space, since G itself is the basis. |S₃| = 6, so dim(ℂ[S₃]) = 6. As an algebra, ℂ[S₃] is 6-dimensional but non-commutative (since S₃ is non-abelian). By the Artin-Wedderburn theorem, ℂ[S₃] ≅ ℂ ⊕ ℂ ⊕ M₂(ℂ) as algebras, reflecting the three irreducible representations of dimensions 1, 1, and 2."

- question: "A representation ρ: G → GL(V) is the same data as a left k[G]-module structure on V."
  type: true-false
  answer: true
  explanation: "Given ρ, define the module action by (Σ aᵍeᵍ)·v = Σ aᵍρ(g)v. Conversely, given a k[G]-module V, define ρ(g)v = eᵍ·v. These constructions are inverse to each other and preserve all the relevant structure: subrepresentations correspond to submodules, G-equivariant maps correspond to module homomorphisms, and irreducibility corresponds to simplicity. This equivalence is the reason group algebras exist."

- question: "The center Z(k[G]) of the group algebra consists of elements that commute with all of k[G]. What is the dimension of Z(ℂ[G]) for a finite group G?"
  type: short-answer
  answer: "The dimension of Z(ℂ[G]) equals the number of conjugacy classes of G."
  explanation: "A basis for Z(ℂ[G]) is given by the class sums zC = Σ_{g∈C} eᵍ, one for each conjugacy class C. An element Σ aᵍeᵍ lies in the center if and only if it is constant on conjugacy classes (aᵍ = a_{hgh⁻¹} for all h), which means it is a linear combination of the class sums. Since the number of conjugacy classes also equals the number of irreducible representations, this connects the center of the group algebra to character theory."

- question: "For an abelian group G, the group algebra k[G] is commutative. Over ℂ, what is ℂ[ℤ/nℤ] isomorphic to as an algebra?"
  type: multiple-choice
  options:
    - "The polynomial ring ℂ[x]"
    - "The matrix algebra Mₙ(ℂ)"
    - "ℂ ⊕ ℂ ⊕ ··· ⊕ ℂ (n copies)"
    - "The ring ℤ/nℤ tensored with ℂ"
  answer: 2
  explanation: "ℂ[ℤ/nℤ] ≅ ℂ[x]/(xⁿ − 1). Over ℂ, xⁿ − 1 factors into n distinct linear factors (the nth roots of unity), so by the Chinese Remainder Theorem, ℂ[x]/(xⁿ−1) ≅ ℂ ⊕ ℂ ⊕ ··· ⊕ ℂ. Each copy of ℂ corresponds to one irreducible representation (all 1-dimensional, since the group is abelian). This is the Artin-Wedderburn decomposition for cyclic groups."
```

## Explainer

The **group algebra** k[G] is the algebraic structure that bridges group theory and ring theory. As a vector space, k[G] has dimension |G| with the group elements as a basis. Multiplication is defined by extending the group operation linearly: if a = Σ aᵍeᵍ and b = Σ bₕeₕ, then ab = Σ_{g,h} aᵍbₕe_{gh}. This makes k[G] an associative algebra with identity e_e (the identity element of G). For non-abelian G, the algebra is non-commutative. The group algebra can also be thought of as the algebra of k-valued functions on G with convolution as multiplication, connecting it to harmonic analysis.

The fundamental theorem of this subject is that **representations of G over k are equivalent to left k[G]-modules**. Given a representation ρ: G → GL(V), define the module action by (Σ aᵍeᵍ)·v = Σ aᵍρ(g)v — this extends the G-action on V linearly to all of k[G]. Conversely, any left k[G]-module V gives a representation by restricting the action to the basis elements eᵍ. Under this correspondence, subrepresentations are submodules, intertwining operators are module homomorphisms, direct sums are direct sums, and irreducible representations are simple modules. Every theorem about representations has a module-theoretic counterpart.

This perspective reveals why Maschke's theorem is really a statement about semisimplicity. When char(k) does not divide |G|, the group algebra k[G] is a **semisimple ring** — every module is a direct sum of simple modules. The Artin-Wedderburn theorem then gives the structure: k[G] ≅ M_{d₁}(D₁) ⊕ ··· ⊕ M_{dₖ}(Dₖ), a direct sum of matrix algebras over division rings. Over ℂ, each Dᵢ = ℂ (by Schur's lemma), so ℂ[G] ≅ M_{d₁}(ℂ) ⊕ ··· ⊕ M_{dₖ}(ℂ), where d₁, …, dₖ are the dimensions of the irreducible representations. This isomorphism is the deepest structural result in finite group representation theory.

The **center** Z(k[G]) plays a special role. Its basis consists of the class sums — the formal sums of all elements in each conjugacy class. Since dim(Z(ℂ[G])) equals the number of conjugacy classes, which equals the number of irreducible representations, the center encodes the character theory. The primitive central idempotents eᵢ = (dᵢ/|G|) Σ_{g∈G} χᵢ(g⁻¹)eᵍ project k[G] onto its simple components, providing an algebraic realization of the decomposition into irreducible representations.
