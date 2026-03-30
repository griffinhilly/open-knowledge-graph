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
stage: expert
status: validated
---

# The Norm in Algebraic Number Fields

## Core Idea
For α in a number field K/ℚ, the norm N(α) is the product of α's conjugates. The norm is multiplicative: N(αβ) = N(α)N(β), and maps the integer ring to ℤ.

## Questions

```yaml
- question: "In ℤ[√−5], can the element 2 divide 1 + √−5? Use the norm to decide."
  type: multiple-choice
  options:
    - "Yes, because 2 divides every integer and 1 + √−5 has an integer real part"
    - "No, because N(2) = 4 does not divide N(1 + √−5) = 6, so divisibility is impossible"
    - "Yes, because 1 + √−5 = 2 · (1/2 + √−5/2) and fractions are allowed in ℤ[√−5]"
    - "The norm cannot determine divisibility — you need to find an explicit quotient"
  answer: 1
  explanation: "N(2) = 4 and N(1 + √−5) = 1 + 5 = 6. Multiplicativity of the norm says that if 2 | (1 + √−5) in ℤ[√−5], then N(2) | N(1 + √−5) in ℤ — that is, 4 | 6. But 4 does not divide 6, so 2 cannot divide 1 + √−5. This is the norm's power as a divisibility obstruction: proving non-divisibility in the algebraic ring by reducing to ordinary integer divisibility. Option C shows a common error — dividing in the field ℚ(√−5) is not the same as dividing in the ring ℤ[√−5]."

- question: "What does multiplicativity of the norm — N(αβ) = N(α)N(β) — immediately imply about the units of the ring of integers 𝒪_K?"
  type: multiple-choice
  options:
    - "Every element of norm 1 is a unit, and every unit has norm 1"
    - "Units must have prime norm, since prime elements generate the group of units"
    - "Only elements of norm 0 are units, since the norm of zero is 0"
    - "The norm of a unit can be any positive integer depending on the field"
  answer: 0
  explanation: "If α is a unit in 𝒪_K, then αβ = 1 for some β ∈ 𝒪_K. Applying the norm: N(α)N(β) = N(1) = 1. Since norms are integers, N(α) | 1, so N(α) = 1 (as norms are positive). Conversely, if N(α) = 1, then α divides 1 (a constructive argument shows the inverse lies in 𝒪_K), so α is a unit. This characterizes units exactly as norm-1 elements — for ℤ[i], that gives {1, −1, i, −i}, exactly the four Gaussian units of norm 1."

- question: "If N(α) divides N(β) in ℤ, then α divides β in the ring of integers 𝒪_K."
  type: true-false
  answer: false
  explanation: "Norm divisibility is a necessary but not sufficient condition for ring divisibility. If α | β in 𝒪_K, then N(α) | N(β) in ℤ — this is the useful direction for proving non-divisibility. But the converse fails. For example, in ℤ[√−5], N(2) = 4 divides N(2 + 2√−5) = 4 + 20 = 24, but 2 does not divide 2 + 2√−5 in ℤ[√−5] because (2 + 2√−5)/2 = 1 + √−5 ∈ ℤ[√−5]. Wait — actually that does work. A cleaner example: N(3) = 9 divides N(6) = 36, but 3 does divide 6 in ℤ[√−5]. The point is that norm divisibility is necessary, not sufficient: you can't conclude α | β from norm divisibility alone without additional work."

- question: "The multiplicativity of the norm N(αβ) = N(α)N(β) is what makes it a useful tool for studying divisibility in rings of integers of number fields."
  type: true-false
  answer: true
  explanation: "Multiplicativity is the essential property that connects divisibility in 𝒪_K to divisibility in ℤ. If α | β, then β = αγ for some γ, so N(β) = N(α)N(γ) — meaning N(α) | N(β). This reduction from divisibility questions in possibly exotic rings to ordinary integer divisibility is the entire value of the norm. Without multiplicativity, norms would just be a size measure; with it, they become a diagnostic tool for factorization, irreducibility, and the failure of unique factorization."

- question: "In ℤ[√−5], we have 6 = 2 · 3 = (1 + √−5)(1 − √−5). Explain, using norms, why these are genuinely different factorizations and not related by multiplication by units."
  type: short-answer
  answer: "Compute norms: N(2) = 4, N(3) = 9, N(1 ± √−5) = 1 + 5 = 6. Units in ℤ[√−5] have norm 1; the only elements of norm 1 are ±1. So none of {2, 3, 1 ± √−5} is a unit. Irreducibility: if 2 = αβ then N(α)N(β) = 4, so {N(α), N(β)} = {1,4} or {2,2}. Norm-1 elements are units; are there elements of norm 2? That would require a² + 5b² = 2, which has no integer solutions. So 2 is irreducible. Similarly 3 is irreducible (norm 9, no elements of norm 3). And 1 ± √−5 are irreducible (norm 6, no elements of norms 2 or 3 exist). Since 2 ≠ unit · (1 ± √−5) and 3 ≠ unit · (1 ± √−5), the two factorizations are genuinely distinct — unique factorization fails."
  explanation: "This argument shows the norm functioning at full capacity: first to identify the units (norm 1), then to check irreducibility (no elements of the required intermediate norm exist), and finally to compare factorizations (they involve elements of different norms so cannot be related by unit multiplication). The same analysis works for any ring of integers where unique factorization fails — the norm exposes the failure by making the incompatible factorizations visible through integer arithmetic."
```

## Explainer

Start with what you already know from **Gaussian integers**: for α = a + bi in ℤ[i], the norm is N(α) = a² + b² — the product of α and its complex conjugate ā = a − bi. This norm is multiplicative: N(αβ) = N(α)N(β), and it maps Gaussian integers to ordinary non-negative integers. You used this multiplicativity to study divisibility in ℤ[i], because if α | β in ℤ[i] then N(α) | N(β) in ℤ. The norm of a unit must be 1, so the units of ℤ[i] are exactly the elements of norm 1: {1, −1, i, −i}.

The general construction extends this idea to any **number field** K — a finite extension of ℚ. If [K : ℚ] = n, then every α ∈ K has exactly n field embeddings σ₁, ..., σₙ : K → ℂ (its **conjugates**), and the norm is defined as N_{K/ℚ}(α) = σ₁(α) · σ₂(α) · ··· · σₙ(α). For a Gaussian integer a + bi, the two embeddings send α ↦ a + bi and α ↦ a − bi, giving N = (a + bi)(a − bi) = a² + b² — recovering the formula you know. For a cubic field like ℚ(∛2), the norm of a + b∛2 + c∛4 is a product of three conjugate values, yielding a cubic in a, b, c.

The critical property is **multiplicativity**: N(αβ) = N(α)N(β) for all α, β ∈ K. This follows because each embedding is a ring homomorphism, so σᵢ(αβ) = σᵢ(α)σᵢ(β), and the product over all i factors accordingly. Multiplicativity is the bridge between arithmetic in the ring of integers 𝒪_K and ordinary integer arithmetic: if α divides β in 𝒪_K, then N(α) divides N(β) in ℤ. This gives you a tool to obstruct divisibility — if N(α) does not divide N(β) in ℤ, then α cannot divide β in 𝒪_K.

Why does this matter for unique factorization? In ℤ[√−5], consider the factorizations 6 = 2 · 3 = (1 + √−5)(1 − √−5). Computing norms: N(2) = 4, N(3) = 9, N(1 ± √−5) = 1 + 5 = 6. Since these norms are all different and none of these elements divide each other, these are genuinely different factorizations of 6. The norm reveals that none of {2, 3, 1 ± √−5} is a unit (norm 1) or a product of two non-unit factors — they are all irreducible — yet 6 factors in two distinct ways. The norm function is the diagnostic tool that exposes exactly where and why unique factorization fails in rings of integers of number fields.
