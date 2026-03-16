---
id: pythagorean-triples-parametrization
title: Pythagorean Triples (Parametrization)
domain: mathematics
course: number-theory
prerequisites:
- id: linear-diophantine-equations
  type: soft
- id: sum-two-squares-theorem
  type: soft
tags:
- pythagorean-triples
- diophantine
- parametrization
stage: advanced
status: draft
---

# Pythagorean Triples (Parametrization)

## Core Idea
Primitive Pythagorean triples (a, b, c) with a^2 + b^2 = c^2 and gcd(a,b,c) = 1 are parameterized by: a = m^2 - n^2, b = 2mn, c = m^2 + n^2 for coprime m > n > 0 of opposite parity. This complete description follows from factoring in Gaussian integers.

## Explainer

You can verify easily that 3² + 4² = 5², and that 5² + 12² = 13². A natural question is: are there infinitely many such triples, and can we describe all of them systematically? The parametrization answers yes to both. Every **primitive Pythagorean triple** — one where gcd(a, b, c) = 1 — arises from a pair of parameters (m, n) via the formulas a = m² − n², b = 2mn, c = m² + n², where m > n > 0, gcd(m, n) = 1, and m and n have opposite parity (one even, one odd).

To see why this works algebraically, rewrite a² + b² = c² as b² = c² − a² = (c − a)(c + a). In a primitive triple, exactly one of a, b is even — say b is even. Then (c − a) and (c + a) are both even, coprime to each other, and their product is a perfect square b². When two coprime numbers multiply to a perfect square, each must itself be a perfect square. Setting c − a = 2n² and c + a = 2m² and solving gives c = m² + n², a = m² − n², b = 2mn. The coprimality and parity conditions on m, n ensure the triple is primitive and that you don't double-count.

The deeper explanation uses **Gaussian integers** — complex numbers of the form a + bi with a, b ∈ ℤ. The equation a² + b² = c² becomes (a + bi)(a − bi) = c². In the Gaussian integers, c factors into Gaussian primes, and the factorization of c² as a product of two conjugate factors pins down what a and b must be. The parity and coprimality conditions on m, n correspond exactly to the Gaussian factorization being primitive. This approach generalizes: the sum-of-two-squares theorem you studied as a prerequisite follows the same logic — a prime p is a sum of two squares if and only if p ≡ 1 (mod 4), which corresponds to p splitting as a product of conjugate Gaussian primes.

The parametrization has a beautiful completeness property: it misses nothing. Every primitive triple appears exactly once (up to swapping a and b). Non-primitive triples are just multiples: for any k, (ka, kb, kc) is a triple whenever (a, b, c) is. So the full list of all Pythagorean triples is exactly {k(m² − n², 2mn, m² + n²) : m > n > 0, gcd(m,n) = 1, m and n opposite parity, k ≥ 1}. This is a rare example in number theory of a complete, explicit description of all integer solutions to a Diophantine equation.
