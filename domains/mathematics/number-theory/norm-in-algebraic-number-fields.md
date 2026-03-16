---
id: norm-in-algebraic-number-fields
title: The Norm in Algebraic Number Fields
domain: mathematics
course: number-theory
prerequisites:
- id: algebraic-integers
  type: hard
tags:
- norm
- algebraic-number-fields
- number-theory
stage: advanced
status: draft
---

# The Norm in Algebraic Number Fields

## Core Idea
The norm N: K → ℚ of a number field K is a multiplicative function sending each element to the product of its conjugates. The norm is essential for factorization properties, ideal theory, and solving Diophantine equations in algebraic number fields.

## Explainer

Start with the simplest nontrivial case: the Gaussian integers ℤ[i], where elements are a+bi with a,b ∈ ℤ. The norm of a+bi is N(a+bi) = a²+b², which you may recognize as the squared distance from the origin. Equivalently, N(a+bi) = (a+bi)(a−bi) — the element times its complex conjugate. This gives a positive integer, and crucially, N is multiplicative: N((a+bi)(c+di)) = N(a+bi)·N(c+di). You can verify this directly, or notice it follows from |zw| = |z||w| for complex numbers.

In a general number field K = ℚ(α) of degree n, an algebraic integer α satisfies a degree-n polynomial over ℚ with n conjugates α = α₁, α₂, ..., αₙ (the roots). The **norm** of an element θ ∈ K is N(θ) = σ₁(θ)·σ₂(θ)···σₙ(θ), the product over all field embeddings σᵢ: K → ℂ. For K = ℚ(i), there are two embeddings: the identity and complex conjugation, giving N(a+bi) = (a+bi)(a−bi) = a²+b² — exactly what we computed above.

Multiplicativity N(αβ) = N(α)N(β) follows from the fact that each embedding is a ring homomorphism: σᵢ(αβ) = σᵢ(α)σᵢ(β), so the product over all embeddings factorizes. This multiplicativity is the norm's most useful property. It means if N(α) is a rational prime p, then α cannot factor as α = βγ with both β,γ non-units in O_K — otherwise N(β)·N(γ) = p with both factors integers greater than 1, a contradiction. So **elements with prime norm are irreducible**.

This gives a direct tool for Diophantine equations. To solve x²+y²=5 in integers, rewrite it as N(x+yi) = 5 in ℤ[i]. Since N(2+i) = 4+1 = 5, we find 2+i is a Gaussian prime, and the solutions to the Diophantine equation correspond to the Gaussian integer factorizations of 5. More generally, any question about which primes p are representable as x²+ny² translates into a question about factorization in ℤ[√(−n)], with the norm measuring whether factorization is possible.
