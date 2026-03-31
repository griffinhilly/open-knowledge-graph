---
id: representations-of-abelian-groups
title: Representations of Abelian Groups
domain: mathematics
course: representation-theory
prerequisites:
- id: representations-of-cyclic-groups
  type: hard
- id: schurs-lemma
  type: hard
- id: character-theory
  type: soft
builds-toward:
- representation-ring
tags:
- abelian-group
- dual-group
- pontryagin-duality
- one-dimensional
stage: expert
status: validated
---

# Representations of Abelian Groups

## Core Idea
Every irreducible complex representation of a finite abelian group is one-dimensional, a consequence of Schur's lemma (every group element commutes with the entire representation, hence acts as a scalar). Since every finite abelian group is a product of cyclic groups ℤ/n₁ℤ × ··· × ℤ/nₖℤ, its irreducible representations are products of irreducible representations of the cyclic factors — each specified by a tuple of roots of unity. The set of all irreducible representations forms the **dual group** Ĝ, which is (non-canonically) isomorphic to G itself.

## Questions

```yaml
- question: "How many irreducible complex representations does ℤ/2ℤ × ℤ/2ℤ have, and what are their dimensions?"
  type: multiple-choice
  options:
    - "2 representations, each of dimension 2"
    - "4 representations, each of dimension 1"
    - "1 representation of dimension 4"
    - "3 representations of dimensions 1, 1, 2"
  answer: 1
  explanation: "The group has order 4 and is abelian, so all irreducible representations are 1-dimensional. There must be exactly 4 of them (one per element, since each element is its own conjugacy class). They are: (1,1)→1, (1,−1), (−1,1), (−1,−1), where each entry gives the scalar by which the corresponding generator acts. Check: 1² × 4 = 4 = |G|."

- question: "The dual group Ĝ = Hom(G, ℂ*) of a finite abelian group G is isomorphic to G."
  type: true-false
  answer: true
  explanation: "For G = ℤ/nℤ, Ĝ ≅ ℤ/nℤ (there are n homomorphisms to ℂ*, indexed by roots of unity). For G = ℤ/n₁ℤ × ··· × ℤ/nₖℤ, Ĝ ≅ ℤ/n₁ℤ × ··· × ℤ/nₖℤ ≅ G. The isomorphism is non-canonical — it depends on choosing generators — but the abstract group structure is the same. This is a special case of Pontryagin duality for finite abelian groups."

- question: "Let G = ℤ/2ℤ × ℤ/3ℤ. The representation sending (a,b) to (−1)ᵃ · ω^b (where ω = e^{2πi/3}) is irreducible because:"
  type: short-answer
  answer: "It is 1-dimensional (a homomorphism G → ℂ*), and all 1-dimensional representations are automatically irreducible since they have no proper nonzero subspaces."
  explanation: "This representation maps (1,0) ↦ −1 and (0,1) ↦ ω. Since (−1)² = 1 and ω³ = 1, it is a well-defined group homomorphism to ℂ*. It is one of the 6 = 2·3 irreducible representations of ℤ/2ℤ × ℤ/3ℤ, obtained by choosing one representation from each cyclic factor independently."

- question: "For a finite abelian group G, the character table is a |G| × |G| matrix. What special property does this matrix have?"
  type: multiple-choice
  options:
    - "It is the identity matrix"
    - "All entries are ±1"
    - "Its rows are orthogonal with respect to the standard inner product (after conjugation), and it defines a generalized DFT on G"
    - "It is upper triangular"
  answer: 2
  explanation: "The character table of a finite abelian group has rows indexed by Ĝ and columns by G. The orthogonality relations say the rows are orthogonal: Σ_{g∈G} χ(g)·conjugate(χ'(g)) = |G|·δ_{χ,χ'}. The matrix (1/√|G|)(χ(g))_{χ,g} is unitary and defines the Fourier transform on G. For cyclic groups this recovers the DFT; for general abelian groups it is the higher-dimensional DFT on the product structure."
```

## Explainer

The representation theory of finite abelian groups is completely determined by a single fact: **Schur's lemma forces all irreducible representations to be 1-dimensional**. Here is why. If G is abelian, then for any representation ρ: G → GL(V), every ρ(g) commutes with every ρ(h). So every ρ(g) is a G-equivariant endomorphism of V. By Schur's lemma (over ℂ), if V is irreducible, each ρ(g) must be a scalar λ_g · I. But then every subspace of V is invariant, so irreducibility forces dim(V) = 1.

Since every irreducible representation is a homomorphism χ: G → ℂ*, the set of irreducible representations forms a group under pointwise multiplication: (χ₁ · χ₂)(g) = χ₁(g) · χ₂(g). This group is the **dual group** (or **character group**) Ĝ = Hom(G, ℂ*). For G = ℤ/n₁ℤ × ··· × ℤ/nₖℤ, the fundamental theorem of finite abelian groups gives Ĝ ≅ ℤ/n₁ℤ × ··· × ℤ/nₖℤ ≅ G. The isomorphism Ĝ ≅ G is non-canonical (it depends on choices of generators), but the **double dual** Ĝ̂ ≅ G has a canonical isomorphism g ↦ (χ ↦ χ(g)). This is the finite-group version of **Pontryagin duality**.

The **Fourier analysis** on a finite abelian group decomposes functions f: G → ℂ into irreducible components. Every function can be written as f = Σ_{χ∈Ĝ} f̂(χ)·χ, where f̂(χ) = (1/|G|) Σ_{g∈G} f(g)·conjugate(χ(g)) are the Fourier coefficients. The Plancherel formula Σ_{g∈G} |f(g)|² = |G| Σ_{χ∈Ĝ} |f̂(χ)|² is a consequence of the orthogonality relations. For G = ℤ/nℤ, this is the classical discrete Fourier transform. For general abelian groups, the Fourier transform factors according to the product decomposition of G, recovering the multidimensional FFT.

The representation ring R(G) of a finite abelian group is particularly simple: it is isomorphic to the group ring ℤ[Ĝ] ≅ ℤ[x₁, …, xₖ]/(x₁^{n₁} − 1, …, xₖ^{nₖ} − 1). The tensor product of representations corresponds to multiplication of characters in Ĝ, and direct sum corresponds to addition. This ring structure encodes all the decomposition rules for representations of G and connects naturally to algebraic number theory through the cyclotomic fields generated by the roots of unity involved.
