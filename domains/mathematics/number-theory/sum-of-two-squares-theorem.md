---
id: sum-of-two-squares-theorem
title: Sum of Two Squares Theorem
domain: mathematics
course: number-theory
prerequisites:
- id: quadratic-residues-and-legendre-symbol
  type: soft
- id: fundamental-theorem-of-arithmetic-rigorous
  type: soft
- id: lagrange-four-square-theorem
  type: soft
builds-toward:
- pythagorean-triples-parametrization
tags:
- representations
- quadratic-forms
- diophantine
stage: advanced
status: validated
---
# Sum of Two Squares Theorem

## Core Idea
A positive integer n can be expressed as a sum of two squares if and only if in the prime factorization of n, every prime of the form 4k+3 appears to an even power. This classical result elegantly connects arithmetic structure to geometric representations and is proved using Gaussian integers.

## Questions

```yaml
- question: "The number 45 = 3² × 5. Can 45 be expressed as a sum of two squares?"
  type: multiple-choice
  options:
    - "No — because 3 is a prime of the form 4k+3, it blocks all representations"
    - "Yes — because 3 appears to an even power (2), it does not block representation"
    - "No — because 5 ≡ 1 (mod 4) primes can never be sums of two squares"
    - "Yes — but only because 45 is composite, not prime"
  answer: 1
  explanation: "The theorem states that 4k+3 primes must appear to *even* powers. In 45 = 3² × 5, the only 4k+3 prime is 3, and it appears to the power 2 (even). So 45 is representable: 45 = 3² + 6² = 9 + 36. The common misconception (option A) is treating any appearance of a 4k+3 prime as a total block — but only *odd-power* appearances block representation."

- question: "Which of the following integers CANNOT be expressed as a sum of two squares?"
  type: multiple-choice
  options:
    - "25 = 5²"
    - "50 = 2 × 5²"
    - "63 = 3² × 7"
    - "65 = 5 × 13"
  answer: 2
  explanation: "63 = 3² × 7. The prime 7 ≡ 3 (mod 4) appears to the first power (odd), so 63 cannot be expressed as a sum of two squares. Check the others: 25 = 5² (5 ≡ 1 mod 4, works: 3² + 4²), 50 = 2 × 5² (both 2 and 5 are not 4k+3 primes, works: 5² + 5²), 65 = 5 × 13 (both ≡ 1 mod 4, works: 4² + 7²). Only 63 has a 4k+3 prime appearing to an odd power."

- question: "The prime 7 cannot be expressed as a sum of two squares because 7 ≡ 3 (mod 4)."
  type: true-false
  answer: true
  explanation: "True. The theorem states that a prime p is expressible as a² + b² if and only if p = 2 or p ≡ 1 (mod 4). Since 7 ≡ 3 (mod 4), it belongs to the 4k+3 class, which is never a sum of two squares. You can verify directly: the only pairs of non-negative integers with a² + b² ≤ 7 are (0,1), (0,2), (1,1), (1,2) — giving squares 1, 4, 2, 5. None sum to 7."

- question: "The integer 9 = 3² can rarely be expressed as a sum of two squares because 3 is a prime of the form 4k+3."
  type: true-false
  answer: false
  explanation: "False. 9 = 3² + 0². While 3 ≡ 3 (mod 4), it appears to the *second* power (even) in 9 = 3². The theorem requires that 4k+3 primes appear to even powers — and a prime to an even power 2k equals p^(2k) = (p^k)² + 0². So 9 is representable: 9 = 3² + 0². Only an *odd* power of a 4k+3 prime blocks representation."

- question: "Why does a prime p ≡ 3 (mod 4) appearing to an odd power in the factorization of n block n from being a sum of two squares?"
  type: short-answer
  answer: "In the Gaussian integers ℤ[i], a prime p ≡ 3 (mod 4) remains prime (stays inert) — it does not factor as a product of conjugates π·π̄. This means p cannot be written as |π|² = a² + b². When p appears to an odd power, the Gaussian integer factorization of n contains an irreducible factor that cannot be paired with its conjugate. Brahmagupta's identity shows that products of sums of two squares remain sums of two squares, but an unpaired 4k+3 prime breaks this: it contributes a factor that cannot be absorbed into any (a² + b²) representation."
  explanation: "The proof via Gaussian integers is the cleanest way to see this. Primes ≡ 1 (mod 4) factor as p = π·π̄ in ℤ[i], so p = |π|² = a² + b². Primes ≡ 3 (mod 4) remain inert (prime in ℤ[i]) and cannot be decomposed this way. An even power p² = (p + 0i)(p − 0i) = p² + 0² can still be represented (trivially). An odd power introduces an irreducible factor without a conjugate match, making representation impossible."
```

## Explainer

The question "which integers are sums of two squares?" sounds simple but has a surprisingly structured answer. Start by testing small cases: 1 = 1² + 0², 2 = 1² + 1², 4 = 2² + 0², 5 = 2² + 1², 9 = 3² + 0², 10 = 3² + 1². But 3, 6, 7, and 11 cannot be written this way no matter how you try. The pattern is not obvious from the examples alone, but it becomes crisp once you classify the primes.

Primes split into three types for this problem: 2 = 1² + 1² (works), primes p ≡ 1 (mod 4) like 5, 13, 17, 29 (always expressible as sums of two squares), and primes p ≡ 3 (mod 4) like 3, 7, 11, 19 (never expressible). The modular condition connects to your background in **quadratic residues**: −1 is a quadratic residue mod p exactly when p ≡ 1 (mod 4), and this is precisely the condition that makes p expressible as a² + b². The connection between "−1 has a square root mod p" and "p is a sum of two squares" is the heart of the theorem.

The cleanest proof uses **Gaussian integers**, the ring ℤ[i] = {a + bi : a, b ∈ ℤ}. In this ring, a² + b² = (a + bi)(a − bi) = |a + bi|². So asking whether p = a² + b² is the same as asking whether p factors nontrivially in ℤ[i]. Using the **fundamental theorem of arithmetic** for ℤ[i] (which is a Euclidean domain and hence a UFD), one can show: a prime p ≡ 1 (mod 4) factors as p = π · π̄ where π = a + bi is a Gaussian prime; a prime p ≡ 3 (mod 4) remains prime (inert) in ℤ[i] and cannot be written as a product of conjugates. This is why primes of the form 4k+3 are the obstruction.

For composite n, the full theorem follows from **Brahmagupta's identity**: (a² + b²)(c² + d²) = (ac − bd)² + (ad + bc)² = (ac + bd)² + (ad − bc)². This identity says the product of two sums of squares is again a sum of squares. So to check whether n is representable, you only need to check its prime factors: each prime p ≡ 1 (mod 4) contributes, 2 contributes, and a prime p ≡ 3 (mod 4) to an even power can be absorbed (since p² = p² + 0²), but a prime p ≡ 3 (mod 4) to an odd power blocks representation entirely. The theorem gives a complete, efficient criterion: factor n, check the exponents of the 4k+3 primes, and you immediately know whether n lands on the integer lattice as the squared distance from the origin.
