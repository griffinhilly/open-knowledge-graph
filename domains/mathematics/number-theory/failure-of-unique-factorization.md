---
id: failure-of-unique-factorization
title: Failure of Unique Factorization in Algebraic Number Fields
domain: mathematics
course: number-theory
prerequisites:
- id: gaussian-integers
  type: soft
- id: fundamental-theorem-of-arithmetic-rigorous
  type: soft
builds-toward:
- introduction-to-ideal-class-group
tags:
- unique-factorization
- algebraic-number-fields
- ideals
stage: advanced
status: draft
---

# Failure of Unique Factorization in Algebraic Number Fields

## Core Idea
Unlike ℤ and Gaussian integers, many algebraic number rings fail unique factorization: in ℤ[√−5], we have 6 = 2·3 = (1+√−5)(1−√−5) with non-associate factors. Ideal theory was developed to restore unique factorization by factoring into ideals instead of elements.

## Explainer

The Fundamental Theorem of Arithmetic tells you that every integer factors into primes uniquely — 12 = 2² × 3, and there is no other way to write it. The same is true for the Gaussian integers ℤ[i], which you showed is a Euclidean domain. But these happy cases disguise how special unique factorization actually is. Most algebraic number rings do not have it.

The classic example is ℤ[√−5], the ring of numbers a + b√−5 with a, b ∈ ℤ. In this ring, 6 factors in two genuinely different ways: 6 = 2 × 3, and also 6 = (1 + √−5)(1 − √−5). You can verify the second: (1 + √−5)(1 − √−5) = 1 − (−5) = 6. To confirm these are genuinely distinct factorizations and not just associate variants, you use the **norm** N(a + b√−5) = a² + 5b² to show that 2, 3, (1 + √−5), and (1 − √−5) are all **irreducible** in ℤ[√−5] but not **primes**. In ℤ, irreducible and prime coincide — but in rings without unique factorization, they come apart. An element p is prime if p | ab implies p | a or p | b; an element is irreducible if it cannot be written as a product of two non-units. In ℤ[√−5], the element 2 is irreducible (no element has norm 2) but not prime: 2 | (1 + √−5)(1 − √−5) = 6, yet 2 divides neither factor.

The resolution, due to Kummer and Dedekind, was to shift from factoring *elements* to factoring *ideals*. Even though the element 2 cannot be factored further in ℤ[√−5], the ideal (2) factors into a product of prime ideals: (2) = 𝔭² where 𝔭 = (2, 1 + √−5). When you re-express 6 = 2 × 3 = (1 + √−5)(1 − √−5) in terms of ideal factorizations, both sides yield the same product of prime ideals — uniqueness is restored at the level of ideals. The **ideal class group** measures how badly unique factorization fails for elements: if the class group is trivial, every ideal is principal and the ring is a UFD. The class group of ℤ[√−5] has order 2, encoding exactly the two-fold ambiguity. Algebraic number theory thus does not abandon unique factorization — it relocates it from elements to ideals.
