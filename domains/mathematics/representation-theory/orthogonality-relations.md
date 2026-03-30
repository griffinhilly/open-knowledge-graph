---
id: orthogonality-relations
title: Orthogonality Relations
domain: mathematics
course: representation-theory
prerequisites:
- id: character-theory
  type: hard
- id: inner-product-spaces
  type: soft
builds-toward:
- character-tables
tags:
- orthogonality
- inner-product
- class-function
- row-orthogonality
- column-orthogonality
stage: expert
status: validated
---

# Orthogonality Relations

## Core Idea
The irreducible characters of a finite group G are orthonormal with respect to the inner product ⟨χ, ψ⟩ = (1/|G|) Σ_{g∈G} χ(g) conjugate(ψ(g)). This means ⟨χᵢ, χⱼ⟩ = δᵢⱼ — different irreducible characters are orthogonal, and each has norm 1. These relations, derived from Schur's lemma, are the primary computational tool for decomposing representations and constructing character tables.

## Questions

```yaml
- question: "Using the orthogonality relations, how do you compute the multiplicity of an irreducible representation Vᵢ in a representation V?"
  type: short-answer
  answer: "The multiplicity is nᵢ = ⟨χ_V, χᵢ⟩ = (1/|G|) Σ_{g∈G} χ_V(g) conjugate(χᵢ(g)). Since χ_V = Σⱼ nⱼχⱼ and the χⱼ are orthonormal, the inner product extracts the coefficient nᵢ."
  explanation: "This is the Fourier-analytic viewpoint: just as a function's Fourier coefficient is computed by an inner product with a basis function, the multiplicity of an irreducible in a representation is computed by inner product with the corresponding character. This reduces decomposition from an algebraic problem to a numerical one."

- question: "The column orthogonality relations state that Σᵢ χᵢ(g) conjugate(χᵢ(h)) = |C_G(g)| if g and h are conjugate, and 0 otherwise. What is C_G(g)?"
  type: multiple-choice
  options:
    - "The center of G"
    - "The centralizer of g — the set of elements commuting with g"
    - "The conjugacy class of g"
    - "The commutator subgroup of G"
  answer: 1
  explanation: "C_G(g) = {h ∈ G : hg = gh} is the centralizer of g. Its order relates to the conjugacy class size by |C_G(g)| = |G|/|Cl(g)|. The column orthogonality relations are dual to the row relations and express orthogonality across different conjugacy classes rather than across different representations. Both sets of relations follow from Schur's lemma applied to specific intertwining operators."

- question: "If a character χ satisfies ⟨χ, χ⟩ = 1, then the corresponding representation is irreducible."
  type: true-false
  answer: true
  explanation: "Write χ = Σ nᵢχᵢ where the χᵢ are irreducible characters. Then ⟨χ, χ⟩ = Σ nᵢ² by orthonormality. The equation Σ nᵢ² = 1 with non-negative integers nᵢ forces exactly one nᵢ = 1 and all others zero. So χ = χₖ for some k, meaning the representation is irreducible. This gives a quick test for irreducibility."

- question: "The inner product ⟨χ, ψ⟩ = (1/|G|) Σ_{g∈G} χ(g)ψ(g) (without conjugation) works for characters over ℂ."
  type: true-false
  answer: false
  explanation: "Complex conjugation is essential. The correct formula is ⟨χ, ψ⟩ = (1/|G|) Σ χ(g) conjugate(ψ(g)). For representations of finite groups over ℂ, characters satisfy χ(g⁻¹) = conjugate(χ(g)) (since eigenvalues of ρ(g) are roots of unity), so the inner product can also be written (1/|G|) Σ χ(g)ψ(g⁻¹). Without conjugation, the inner product would not be positive definite and the orthonormality statement would fail."
```

## Explainer

The orthogonality relations are the quantitative backbone of character theory. Define an inner product on the space of class functions (functions G → ℂ that are constant on conjugacy classes) by ⟨f₁, f₂⟩ = (1/|G|) Σ_{g∈G} f₁(g) conjugate(f₂(g)). The **first orthogonality relations** (row orthogonality) state that the irreducible characters χ₁, …, χₖ form an orthonormal set: ⟨χᵢ, χⱼ⟩ = δᵢⱼ.

The proof distills from Schur's lemma. Given irreducible representations ρ and σ, consider the "averaged" operator T̃ = (1/|G|) Σ_{g∈G} σ(g)⁻¹ T ρ(g) for an arbitrary linear map T. Schur's lemma forces T̃ to be zero when ρ ≇ σ, and a scalar when ρ ≅ σ. Taking traces with judicious choices of T yields the orthogonality relations. The proof is constructive — it builds the intertwining operators whose properties Schur's lemma constrains.

The practical payoff is enormous. To decompose a representation V into irreducibles, write χ_V = n₁χ₁ + ··· + nₖχₖ. Taking inner products: nᵢ = ⟨χ_V, χᵢ⟩. Each inner product is a finite sum over the group (or equivalently, a weighted sum over conjugacy classes). To test irreducibility: compute ⟨χ, χ⟩ = Σ nᵢ²; the result is 1 if and only if the representation is irreducible. These are concrete, computable checks.

There are also **column orthogonality relations**, obtained by summing over irreducible representations rather than group elements: Σᵢ χᵢ(C_r) conjugate(χᵢ(C_s)) = |G|/|C_r| · δᵣₛ, where C_r, C_s are conjugacy classes. Together, the row and column relations impose so many constraints on a character table that it can often be determined with minimal additional input. The number of irreducible characters equals the number of conjugacy classes, so the character table is always square — a fact that underscores the deep duality between group elements and representations.
