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

## Questions

```yaml
- question: "Which pair (m, n) satisfies ALL the conditions required to generate a primitive Pythagorean triple via a = m² − n², b = 2mn, c = m² + n²?"
  type: multiple-choice
  options:
    - "m = 6, n = 2 — m > n, but gcd(6, 2) = 2 and both are even"
    - "m = 3, n = 1 — m > n and gcd = 1, but both are odd (same parity)"
    - "m = 5, n = 3 — m > n and gcd = 1, but both are odd (same parity)"
    - "m = 5, n = 2 — m > n, gcd(5, 2) = 1, and opposite parity"
  answer: 3
  explanation: "The conditions are: m > n > 0, gcd(m, n) = 1, and m and n have opposite parity (one odd, one even). Options A fails coprimality (gcd = 2). Options B and C fail the parity condition — both m and n are odd. Option D: m = 5 (odd), n = 2 (even), gcd(5, 2) = 1, m > n. This satisfies all conditions. The resulting triple is a = 25 − 4 = 21, b = 20, c = 29. Verify: 21² + 20² = 441 + 400 = 841 = 29². ✓"

- question: "A student uses the parametrization with m = 3, n = 1, computing a = 8, b = 6, c = 10, and verifies 8² + 6² = 10². But she notes that gcd(8, 6, 10) = 2, so the triple is not primitive. What went wrong?"
  type: multiple-choice
  options:
    - "She chose n = 1, which is not allowed in the parametrization for primitive triples"
    - "She used m and n of the same parity (both odd), which always produces an even-valued non-primitive triple"
    - "She computed b = 2mn incorrectly; the formula for primitive triples uses b = mn"
    - "The parametrization only works for m and n that are prime; m = 3 is prime but n = 1 is not"
  answer: 1
  explanation: "When m = 3 and n = 1 are both odd: a = m²−n² = 9−1 = 8 (even), b = 2mn = 6 (even), c = m²+n² = 9+1 = 10 (even). All three are even, so gcd ≥ 2 — not primitive. The parity condition (m and n of opposite parity) is precisely what prevents this: if m is even and n is odd (or vice versa), then m²−n² is odd, 2mn is divisible by 2 but not 4 in the primitive case, and m²+n² is odd, giving gcd(a, b, c) = 1. The condition gcd(m, n) = 1 alone is not enough to guarantee primitivity — opposite parity is independently required."

- question: "The pair m = 3, n = 2 generates the primitive Pythagorean triple (5, 12, 13)."
  type: true-false
  answer: true
  explanation: "Verify: a = m²−n² = 9−4 = 5, b = 2mn = 2(3)(2) = 12, c = m²+n² = 9+4 = 13. Check: 5² + 12² = 25 + 144 = 169 = 13². ✓ Conditions: m = 3 (odd), n = 2 (even) — opposite parity; gcd(3, 2) = 1; m > n. All conditions satisfied, confirming a primitive triple."

- question: "The parametrization a = m²−n², b = 2mn, c = m²+n² misses many primitive Pythagorean triples — for instance, triples where both legs a and b are odd."
  type: true-false
  answer: false
  explanation: "The parametrization is COMPLETE: it produces every primitive Pythagorean triple exactly once (up to swapping a and b). In fact, in any primitive triple one leg is always even (b = 2mn is always even) and one is always odd — a primitive triple can never have two odd legs, because if a and b are both odd, then a² + b² ≡ 2 (mod 4), and no perfect square is ≡ 2 (mod 4). So there are no missing triples of this kind. Every primitive triple is accounted for by exactly one valid (m, n) pair."

- question: "What does it mean for the parametrization of primitive Pythagorean triples to be 'complete,' and why is completeness a remarkable property for a Diophantine equation?"
  type: short-answer
  answer: "Completeness means the parametrization produces every primitive Pythagorean triple and misses none — each triple appears exactly once for some valid (m, n) pair. This is remarkable because most Diophantine equations (integer polynomial equations) either have no solutions, finitely many solutions, or infinitely many solutions with no known closed-form description. A complete explicit parametrization — a finite formula that generates all solutions with no gaps and no duplicates — is rare. The Pythagorean equation is unusual in admitting such a parametrization, made possible by its multiplicative structure and the factorization in the Gaussian integers."
  explanation: "For comparison, the Fermat equation xⁿ + yⁿ = zⁿ has no nontrivial integer solutions for n > 2 (Fermat's Last Theorem), and the general cubic Diophantine equation has no complete parametrization. The Pythagorean case is special: the equation a² + b² = c² factors nicely over ℤ[i], allowing a complete description."
```

## Explainer

You can verify easily that 3² + 4² = 5², and that 5² + 12² = 13². A natural question is: are there infinitely many such triples, and can we describe all of them systematically? The parametrization answers yes to both. Every **primitive Pythagorean triple** — one where gcd(a, b, c) = 1 — arises from a pair of parameters (m, n) via the formulas a = m² − n², b = 2mn, c = m² + n², where m > n > 0, gcd(m, n) = 1, and m and n have opposite parity (one even, one odd).

To see why this works algebraically, rewrite a² + b² = c² as b² = c² − a² = (c − a)(c + a). In a primitive triple, exactly one of a, b is even — say b is even. Then (c − a) and (c + a) are both even, coprime to each other, and their product is a perfect square b². When two coprime numbers multiply to a perfect square, each must itself be a perfect square. Setting c − a = 2n² and c + a = 2m² and solving gives c = m² + n², a = m² − n², b = 2mn. The coprimality and parity conditions on m, n ensure the triple is primitive and that you don't double-count.

The deeper explanation uses **Gaussian integers** — complex numbers of the form a + bi with a, b ∈ ℤ. The equation a² + b² = c² becomes (a + bi)(a − bi) = c². In the Gaussian integers, c factors into Gaussian primes, and the factorization of c² as a product of two conjugate factors pins down what a and b must be. The parity and coprimality conditions on m, n correspond exactly to the Gaussian factorization being primitive. This approach generalizes: the sum-of-two-squares theorem you studied as a prerequisite follows the same logic — a prime p is a sum of two squares if and only if p ≡ 1 (mod 4), which corresponds to p splitting as a product of conjugate Gaussian primes.

The parametrization has a beautiful completeness property: it misses nothing. Every primitive triple appears exactly once (up to swapping a and b). Non-primitive triples are just multiples: for any k, (ka, kb, kc) is a triple whenever (a, b, c) is. So the full list of all Pythagorean triples is exactly {k(m² − n², 2mn, m² + n²) : m > n > 0, gcd(m,n) = 1, m and n opposite parity, k ≥ 1}. This is a rare example in number theory of a complete, explicit description of all integer solutions to a Diophantine equation.
