---
id: tensor-product-of-representations
title: Tensor Product of Representations
domain: mathematics
course: representation-theory
prerequisites:
- id: reducibility-and-irreducibility
  type: hard
- id: tensor-products-universal
  type: hard
builds-toward:
- representation-ring
tags:
- tensor-product
- clebsch-gordan
- kronecker-product
stage: expert
status: validated
---

# Tensor Product of Representations

## Core Idea
Given representations ρ: G → GL(V) and σ: G → GL(W), their tensor product ρ ⊗ σ: G → GL(V ⊗ W) is defined by (ρ ⊗ σ)(g)(v ⊗ w) = ρ(g)v ⊗ σ(g)w. The character of the tensor product is the pointwise product of characters: χ_{ρ⊗σ}(g) = χ_ρ(g)·χ_σ(g). Decomposing tensor products of irreducibles into irreducible summands (the Clebsch-Gordan problem) is fundamental in both mathematics and physics.

## Questions

```yaml
- question: "If ρ has dimension m and σ has dimension n, what is the dimension of ρ ⊗ σ?"
  type: multiple-choice
  options:
    - "m + n"
    - "m · n"
    - "max(m, n)"
    - "m² + n²"
  answer: 1
  explanation: "dim(V ⊗ W) = dim(V) · dim(W) = mn. In terms of matrices, if ρ(g) is m×m and σ(g) is n×n, then (ρ ⊗ σ)(g) is the mn×mn Kronecker product ρ(g) ⊗ σ(g). This multiplicativity of dimension under tensor products contrasts with the additivity under direct sums: dim(V ⊕ W) = m + n."

- question: "The character of ρ ⊗ σ equals the product χ_ρ · χ_σ. Why?"
  type: short-answer
  answer: "If the eigenvalues of ρ(g) are α₁, ..., αₘ and of σ(g) are β₁, ..., βₙ, then the eigenvalues of ρ(g) ⊗ σ(g) are all products αᵢβⱼ. The trace is Σᵢ,ⱼ αᵢβⱼ = (Σ αᵢ)(Σ βⱼ) = tr(ρ(g)) · tr(σ(g)) = χ_ρ(g) · χ_σ(g)."
  explanation: "This multiplicativity of characters under tensor products makes decomposition computationally tractable. To find the irreducible decomposition of ρ ⊗ σ, compute the pointwise product χ_ρ · χ_σ, then take inner products with each irreducible character. This avoids ever constructing the tensor product space explicitly."

- question: "The tensor product of two irreducible representations is always irreducible."
  type: true-false
  answer: false
  explanation: "Tensor products of irreducibles are generally reducible. For example, for S₃: the standard 2-dimensional representation ρ has χ_ρ = (2, 0, −1) on the three conjugacy classes. Then χ_{ρ⊗ρ}(g) = χ_ρ(g)² = (4, 0, 1). Decomposing: ⟨χ_{ρ⊗ρ}, χ_triv⟩ = (4+0+2)/6 = 1, ⟨χ_{ρ⊗ρ}, χ_sign⟩ = (4+0+2)/6 = 1, ⟨χ_{ρ⊗ρ}, χ_ρ⟩ = (8+0−2)/6 = 1. So ρ ⊗ ρ ≅ triv ⊕ sign ⊕ ρ — three irreducible summands."

- question: "In physics, the decomposition of tensor products of representations of SU(2) is governed by Clebsch-Gordan coefficients. The result for spin-j₁ ⊗ spin-j₂ is:"
  type: multiple-choice
  options:
    - "A single irreducible of spin j₁ + j₂"
    - "Direct sum of irreducibles with spins from |j₁−j₂| to j₁+j₂ in integer steps"
    - "A direct sum of j₁·j₂ copies of the trivial representation"
    - "An irreducible of spin j₁·j₂"
  answer: 1
  explanation: "The Clebsch-Gordan decomposition for SU(2) is V_{j₁} ⊗ V_{j₂} ≅ V_{|j₁−j₂|} ⊕ V_{|j₁−j₂|+1} ⊕ ··· ⊕ V_{j₁+j₂}. For example, spin-1 ⊗ spin-1 = spin-0 ⊕ spin-1 ⊕ spin-2, with dimensions 3·3 = 1+3+5 = 9. This is the mathematical basis for angular momentum addition in quantum mechanics."
```

## Explainer

The **tensor product** gives a way to combine two representations into a new, larger one. If G acts on V via ρ and on W via σ, the tensor product representation acts on V ⊗ W by the **diagonal action**: g sends v ⊗ w to ρ(g)v ⊗ σ(g)w, extended linearly to all of V ⊗ W. This is not the same as acting on V and W independently (which would be the direct sum ρ ⊕ σ) — in the tensor product, the same group element g acts simultaneously on both factors.

The dimension of V ⊗ W is dim(V) · dim(W), and in a chosen basis the representing matrix is the Kronecker product of the two individual matrices. The character has a beautiful form: χ_{ρ⊗σ}(g) = χ_ρ(g) · χ_σ(g), a pointwise product. This follows from the fact that the eigenvalues of A ⊗ B are all pairwise products of eigenvalues of A and B, so tr(A ⊗ B) = tr(A) · tr(B). This multiplicativity converts the tensor product decomposition problem into arithmetic with characters.

The **Clebsch-Gordan problem** asks: given irreducible representations V_i and V_j, decompose V_i ⊗ V_j into irreducibles. The answer is V_i ⊗ V_j ≅ ⊕_k N_{ij}^k V_k, where the multiplicities N_{ij}^k (called Clebsch-Gordan coefficients or Kronecker coefficients for symmetric groups) are computed by N_{ij}^k = ⟨χ_i · χ_j, χ_k⟩. For finite groups over ℂ, this is always a finite computation. For SU(2) in physics, the Clebsch-Gordan decomposition governs angular momentum addition: coupling spin-j₁ and spin-j₂ gives all spins from |j₁−j₂| to j₁+j₂.

Tensor products interact with direct sums distributively: (V₁ ⊕ V₂) ⊗ W ≅ (V₁ ⊗ W) ⊕ (V₂ ⊗ W). This, combined with the tensor product of irreducibles, means the entire tensor product structure is determined by the Clebsch-Gordan coefficients for irreducible pairs. These coefficients encode deep information about the group and are the subject of ongoing research, particularly for symmetric groups (where computing Kronecker coefficients is a major open problem in algebraic combinatorics).
