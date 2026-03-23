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
status: validated
---

# The Norm in Algebraic Number Fields

## Core Idea
The norm N: K → ℚ of a number field K is a multiplicative function sending each element to the product of its conjugates. The norm is essential for factorization properties, ideal theory, and solving Diophantine equations in algebraic number fields.

## Questions

```yaml
- question: "An element α ∈ ℤ[i] has norm N(α) = 13, where 13 is a prime integer. What can you conclude about α?"
  type: multiple-choice
  options:
    - "α must be a unit in ℤ[i]"
    - "α is irreducible in ℤ[i]"
    - "α = 2 + 3i specifically"
    - "α must be a real integer"
  answer: 1
  explanation: "If α = βγ for non-units β, γ ∈ ℤ[i], then multiplicativity gives N(β)·N(γ) = N(α) = 13. Since N takes positive integer values for Gaussian integers, this forces one factor to be 1, meaning one of β or γ is a unit. So α cannot factor into two non-units — it is irreducible. This is the direct payoff of multiplicativity: prime norm implies irreducibility."

- question: "A number theorist wants to find all integer solutions to x² + y² = 5. How does the norm in ℤ[i] turn this into a factorization problem?"
  type: multiple-choice
  options:
    - "By finding the prime factorization of 5 in ℤ and lifting it"
    - "By expressing the equation as N(x + yi) = 5 and finding Gaussian integers with that norm"
    - "By counting lattice points on the circle of radius √5"
    - "By computing 5 mod 4 to determine representability"
  answer: 1
  explanation: "The equation x² + y² = 5 is exactly N(x + yi) = 5 in ℤ[i], since N(a+bi) = a²+b². Solutions correspond to Gaussian integers with norm 5. Since N(2+i) = 4+1 = 5 and 5 is prime, 2+i is a Gaussian prime, and the integer solutions follow from its factorizations (up to units). The norm translates a Diophantine equation into an algebraic factorization question."

- question: "The multiplicativity of the norm, N(αβ) = N(α)N(β), follows from the fact that each field embedding σᵢ: K → ℂ is a ring homomorphism."
  type: true-false
  answer: true
  explanation: "Since σᵢ is a ring homomorphism, σᵢ(αβ) = σᵢ(α)·σᵢ(β). Taking the product over all embeddings: N(αβ) = ∏ σᵢ(αβ) = ∏ σᵢ(α)·σᵢ(β) = (∏ σᵢ(α))·(∏ σᵢ(β)) = N(α)·N(β). The multiplicativity is a direct algebraic consequence of how embeddings interact with multiplication."

- question: "If α, β ∈ ℤ[i] each have norm 5, then N(αβ) = 10."
  type: true-false
  answer: false
  explanation: "By multiplicativity, N(αβ) = N(α)·N(β) = 5·5 = 25, not 10. The norm multiplies — it does not add. A common error is to treat norm like a linear function. For instance, N(2+i) = 5 and N(1+2i) = 5, so N((2+i)(1+2i)) = N(2+i)·N(1+2i) = 25."

- question: "Why does an element with prime norm have to be irreducible in the ring of integers O_K?"
  type: short-answer
  answer: "If α = βγ with β, γ non-units, then N(α) = N(β)·N(γ) by multiplicativity. Both N(β) and N(γ) are positive integers greater than 1 (since units have norm 1). But then N(α) = N(β)·N(γ) is a product of two integers each ≥ 2, so N(α) is composite — contradicting the assumption that N(α) is prime. Therefore no such factorization into non-units exists, and α is irreducible."
  explanation: "This argument works directly because norm is multiplicative and norms of units equal 1. The key logical move is: prime norm → can't be written as a product of two integers both > 1 → can't factor into two non-units. This makes prime-norm-checking a practical tool for identifying irreducibles without constructing all possible factorizations."
```

## Explainer

Start with the simplest nontrivial case: the Gaussian integers ℤ[i], where elements are a+bi with a,b ∈ ℤ. The norm of a+bi is N(a+bi) = a²+b², which you may recognize as the squared distance from the origin. Equivalently, N(a+bi) = (a+bi)(a−bi) — the element times its complex conjugate. This gives a positive integer, and crucially, N is multiplicative: N((a+bi)(c+di)) = N(a+bi)·N(c+di). You can verify this directly, or notice it follows from |zw| = |z||w| for complex numbers.

In a general number field K = ℚ(α) of degree n, an algebraic integer α satisfies a degree-n polynomial over ℚ with n conjugates α = α₁, α₂, ..., αₙ (the roots). The **norm** of an element θ ∈ K is N(θ) = σ₁(θ)·σ₂(θ)···σₙ(θ), the product over all field embeddings σᵢ: K → ℂ. For K = ℚ(i), there are two embeddings: the identity and complex conjugation, giving N(a+bi) = (a+bi)(a−bi) = a²+b² — exactly what we computed above.

Multiplicativity N(αβ) = N(α)N(β) follows from the fact that each embedding is a ring homomorphism: σᵢ(αβ) = σᵢ(α)σᵢ(β), so the product over all embeddings factorizes. This multiplicativity is the norm's most useful property. It means if N(α) is a rational prime p, then α cannot factor as α = βγ with both β,γ non-units in O_K — otherwise N(β)·N(γ) = p with both factors integers greater than 1, a contradiction. So **elements with prime norm are irreducible**.

This gives a direct tool for Diophantine equations. To solve x²+y²=5 in integers, rewrite it as N(x+yi) = 5 in ℤ[i]. Since N(2+i) = 4+1 = 5, we find 2+i is a Gaussian prime, and the solutions to the Diophantine equation correspond to the Gaussian integer factorizations of 5. More generally, any question about which primes p are representable as x²+ny² translates into a question about factorization in ℤ[√(−n)], with the norm measuring whether factorization is possible.
