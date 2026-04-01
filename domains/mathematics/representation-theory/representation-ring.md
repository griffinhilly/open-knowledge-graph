---
id: representation-ring
title: Representation Ring
domain: mathematics
course: representation-theory
prerequisites:
- id: tensor-product-of-representations
  type: hard
- id: character-theory
  type: hard
- id: subrings-and-ideals
  type: soft
builds-toward: []
tags:
- representation-ring
- grothendieck-group
- virtual-representation
- adams-operations
- K-theory
stage: expert
status: validated
---

# Representation Ring

## Core Idea
The representation ring R(G) (also called the Green ring or character ring) is the Grothendieck group of finite-dimensional representations of G, with addition from direct sum and multiplication from tensor product. Its elements are formal differences of isomorphism classes of representations — "virtual representations" — and it is a commutative ring where the irreducible representations form a ℤ-basis. The character map χ: R(G) → Class(G, ℂ) embeds R(G) as a subring of class functions, making R(G) a bridge between representation theory, K-theory, and algebraic number theory.

## Questions

```yaml
- question: "In the representation ring R(G), what is the additive identity and what is the multiplicative identity?"
  type: short-answer
  answer: "The additive identity is 0 (the zero virtual representation, corresponding to the zero-dimensional representation). The multiplicative identity is the class of the trivial representation [1_G], since V ⊗ 1_G ≅ V for any representation V."
  explanation: "R(G) is a commutative ring with the class [V ⊕ W] = [V] + [W] defining addition and [V ⊗ W] = [V]·[W] defining multiplication. The trivial representation acts as a tensor-product identity because V ⊗ ℂ ≅ V (where ℂ is the trivial representation). Virtual representations like [V] − [W] make sense formally even though negative-dimensional representations do not exist."

- question: "For G = ℤ/nℤ with irreducible representations ρ₀, ρ₁, ..., ρₙ₋₁ (where ρₖ sends the generator to e^{2πik/n}), what is ρ_a · ρ_b in R(G)?"
  type: multiple-choice
  options:
    - "ρ_{a+b} (with index mod n)"
    - "ρ_a ⊕ ρ_b"
    - "ρ_{ab} (with index mod n)"
    - "The regular representation"
  answer: 0
  explanation: "Since ρ_a and ρ_b are both 1-dimensional, ρ_a ⊗ ρ_b is also 1-dimensional, with the generator acting by e^{2πia/n} · e^{2πib/n} = e^{2πi(a+b)/n}. This is ρ_{a+b mod n}. So R(ℤ/nℤ) ≅ ℤ[x]/(xⁿ − 1) as a ring, where x = [ρ₁]. The ring structure of R(G) captures all tensor product decomposition rules."

- question: "A 'virtual representation' [V] − [W] in R(G) always corresponds to an actual representation of G."
  type: true-false
  answer: false
  explanation: "Virtual representations are formal differences and do not correspond to actual representations when the subtracted part is nonzero. However, the character of a virtual representation (χ_V − χ_W) is a well-defined class function that can take negative values. Virtual representations are necessary to make R(G) a ring (not just a semiring) — without additive inverses, we could not do algebra. In topological K-theory, virtual bundles play an analogous role."

- question: "The Adams operation ψᵏ on R(G) sends a representation V to a virtual representation whose character satisfies χ_{ψᵏ(V)}(g) = χ_V(gᵏ). What is ψ² of a 1-dimensional representation ρ?"
  type: short-answer
  answer: "ψ²(ρ) = ρ², where ρ²(g) = ρ(g)². This is the representation obtained by squaring the character values."
  explanation: "For 1-dimensional ρ, χ_{ψ²(ρ)}(g) = χ_ρ(g²) = ρ(g²) = ρ(g)². So ψ²(ρ) = ρ ⊗ ρ = ρ². For higher-dimensional representations, ψᵏ is more subtle — it involves the power sum symmetric functions applied to the eigenvalues of ρ(g). Adams operations are ring homomorphisms (ψᵏ(V⊗W) = ψᵏ(V)⊗ψᵏ(W)) and play a central role in K-theory and the theory of λ-rings."
```

## Explainer

The **representation ring** R(G) organizes all representations of G into an algebraic structure. Start with the free abelian group on isomorphism classes of finite-dimensional representations, then impose the relation [V ⊕ W] = [V] + [W]. This is the **Grothendieck group** construction, which formally adds additive inverses to get "virtual representations." The tensor product of representations defines a multiplication [V]·[W] = [V ⊗ W], making R(G) a commutative ring. The isomorphism classes of irreducible representations form a ℤ-basis, so every element is a unique integer linear combination of irreducibles.

The **character map** χ: R(G) → Class(G, ℂ) sends each representation to its character. Since characters are additive (χ_{V⊕W} = χ_V + χ_W) and multiplicative (χ_{V⊗W} = χ_V · χ_W), this is a ring homomorphism. Over ℂ, it is injective (characters determine representations up to isomorphism), so R(G) embeds as a subring of the ring of class functions. The image consists of the **virtual characters** — ℤ-linear combinations of irreducible characters. The full ring of class functions is R(G) ⊗_ℤ ℂ.

The **Adams operations** ψᵏ: R(G) → R(G) are ring endomorphisms defined by ψᵏ(V) being the virtual representation whose character at g is χ_V(gᵏ). These operations satisfy ψᵏ ∘ ψˡ = ψᵏˡ and encode the interplay between the ring structure and the group structure. For 1-dimensional representations, ψᵏ(ρ) = ρᵏ (the kth tensor power). For general representations, ψᵏ is related to exterior and symmetric powers by Newton's identities. Adams operations make R(G) a **λ-ring**, connecting it to algebraic K-theory.

The representation ring has deep connections to number theory. For a cyclic group ℤ/nℤ, R(G) ≅ ℤ[ζₙ], the ring of integers in the cyclotomic field (after tensoring appropriately). For general finite groups, R(G) captures the "representation-theoretic arithmetic" of G. The rank of R(G) as a ℤ-module equals the number of irreducible representations (= number of conjugacy classes). The **representation ring functor** G ↦ R(G) is contravariant in G via restriction and covariant via induction, and these operations satisfy Frobenius reciprocity at the level of rings, providing the algebraic backbone for the Mackey machine and equivariant K-theory.
