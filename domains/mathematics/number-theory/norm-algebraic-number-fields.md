---
id: norm-algebraic-number-fields
title: The Norm in Algebraic Number Fields
domain: mathematics
course: number-theory
prerequisites:
- id: gaussian-integers
  type: hard
- id: field-extensions
  type: hard
builds-toward:
- failure-unique-factorization
tags:
- norm
- field-extension
- multiplicative
stage: advanced
status: draft
---

# The Norm in Algebraic Number Fields

## Core Idea
For α in a number field K/ℚ, the norm N(α) is the product of α's conjugates. The norm is multiplicative: N(αβ) = N(α)N(β), and maps the integer ring to ℤ.

## Explainer

Start with what you already know from **Gaussian integers**: for α = a + bi in ℤ[i], the norm is N(α) = a² + b² — the product of α and its complex conjugate ā = a − bi. This norm is multiplicative: N(αβ) = N(α)N(β), and it maps Gaussian integers to ordinary non-negative integers. You used this multiplicativity to study divisibility in ℤ[i], because if α | β in ℤ[i] then N(α) | N(β) in ℤ. The norm of a unit must be 1, so the units of ℤ[i] are exactly the elements of norm 1: {1, −1, i, −i}.

The general construction extends this idea to any **number field** K — a finite extension of ℚ. If [K : ℚ] = n, then every α ∈ K has exactly n field embeddings σ₁, ..., σₙ : K → ℂ (its **conjugates**), and the norm is defined as N_{K/ℚ}(α) = σ₁(α) · σ₂(α) · ··· · σₙ(α). For a Gaussian integer a + bi, the two embeddings send α ↦ a + bi and α ↦ a − bi, giving N = (a + bi)(a − bi) = a² + b² — recovering the formula you know. For a cubic field like ℚ(∛2), the norm of a + b∛2 + c∛4 is a product of three conjugate values, yielding a cubic in a, b, c.

The critical property is **multiplicativity**: N(αβ) = N(α)N(β) for all α, β ∈ K. This follows because each embedding is a ring homomorphism, so σᵢ(αβ) = σᵢ(α)σᵢ(β), and the product over all i factors accordingly. Multiplicativity is the bridge between arithmetic in the ring of integers 𝒪_K and ordinary integer arithmetic: if α divides β in 𝒪_K, then N(α) divides N(β) in ℤ. This gives you a tool to obstruct divisibility — if N(α) does not divide N(β) in ℤ, then α cannot divide β in 𝒪_K.

Why does this matter for unique factorization? In ℤ[√−5], consider the factorizations 6 = 2 · 3 = (1 + √−5)(1 − √−5). Computing norms: N(2) = 4, N(3) = 9, N(1 ± √−5) = 1 + 5 = 6. Since these norms are all different and none of these elements divide each other, these are genuinely different factorizations of 6. The norm reveals that none of {2, 3, 1 ± √−5} is a unit (norm 1) or a product of two non-unit factors — they are all irreducible — yet 6 factors in two distinct ways. The norm function is the diagnostic tool that exposes exactly where and why unique factorization fails in rings of integers of number fields.
