---
id: linear-congruences-discrete
title: Linear Congruences and Solutions
domain: mathematics
course: discrete-math
prerequisites:
- id: modular-arithmetic
  type: hard
- id: divisibility-and-gcd
  type: hard
- id: multiplicative-inverse-modular
  type: soft
builds-toward:
- simultaneous-congruences-crt
- multiplicative-inverse-modular
tags:
- number-theory
- modular-arithmetic
- congruences
stage: formal-systems
status: validated
---
# Linear Congruences and Solutions

## Core Idea
A linear congruence ax ≡ b (mod n) has solutions if and only if gcd(a,n) divides b. When solutions exist, there are exactly gcd(a,n) distinct solutions modulo n. These can be found using the extended Euclidean algorithm.

## Questions

```yaml
- question: "How many solutions does 6x ≡ 4 (mod 9) have?"
  type: multiple-choice
  options:
    - "No solutions"
    - "Exactly one solution modulo 9"
    - "Exactly 2 solutions modulo 9"
    - "Exactly 3 solutions modulo 9"
  answer: 0
  explanation: "The solvability condition is that gcd(a, n) must divide b. Here gcd(6, 9) = 3, and 3 does not divide 4 (since 4 = 3 × 1 + 1). Therefore, no solutions exist. A common mistake is checking only whether a and n are coprime — that is the condition for a unique solution, not for existence. When gcd(6, 9) = 3, solutions exist only if b is a multiple of 3, which 4 is not."

- question: "For ax ≡ b (mod n) where gcd(a, n) = 1, which statement best describes the solution set?"
  type: multiple-choice
  options:
    - "No solution exists, because a and n share no common factors"
    - "Exactly one solution modulo n"
    - "Infinitely many solutions"
    - "Exactly gcd(a, n) = 1 solutions, meaning no solution"
  answer: 1
  explanation: "When gcd(a, n) = 1, the solvability condition gcd(a, n) | b is automatically satisfied for any b, and there is exactly one solution modulo n. This is the coprime case — the cleanest scenario. Options A and D reflect a misreading: gcd = 1 is favorable, not problematic. Exactly one solution means a has a unique modular inverse modulo n, the foundation of modular division."

- question: "The congruence 4x ≡ 2 (mod 6) has exactly 2 distinct solutions modulo 6."
  type: true-false
  answer: true
  explanation: "gcd(4, 6) = 2, and 2 divides 2, so solutions exist. By the theorem, the number of distinct solutions modulo n equals gcd(a, n) = 2. The two solutions are x ≡ 2 (mod 6) and x ≡ 5 (mod 6). Check: 4 × 2 = 8 ≡ 2 (mod 6) ✓; 4 × 5 = 20 ≡ 2 (mod 6) ✓."

- question: "If ax ≡ b (mod n) has at least one solution, then gcd(a, n) must equal 1."
  type: true-false
  answer: false
  explanation: "The existence of a solution requires only that gcd(a, n) divides b — not that gcd(a, n) = 1. For example, 4x ≡ 2 (mod 6) has solutions (x = 2 and x = 5) even though gcd(4, 6) = 2 ≠ 1. The condition gcd = 1 guarantees a unique solution; it is sufficient but not necessary for existence."

- question: "Explain why the condition gcd(a, n) | b is both necessary and sufficient for ax ≡ b (mod n) to have integer solutions. What does this mean in terms of the values you can 'reach' with ax − nk?"
  type: short-answer
  answer: "The congruence ax ≡ b (mod n) is equivalent to the Diophantine equation ax − nk = b. By Bezout's theorem, the set of all integers expressible as ax − nk (as x and k range over integers) is exactly the set of multiples of gcd(a, n). Therefore b must be a multiple of gcd(a, n) for a solution to exist — and this is also sufficient, since if gcd(a, n) divides b, scaling a particular Bezout solution finds x."
  explanation: "The key insight is that linear combinations ax − nk can only produce multiples of gcd(a, n). No matter how you choose x and k, you can never reach a b that isn't in this set. Once b is in this set, dividing through by gcd(a, n) reduces the problem to a coprime case with a unique solution modulo n/gcd(a, n)."
```

## Explainer

A **linear congruence** ax ≡ b (mod n) is the modular-arithmetic analog of the linear equation ax = b. From your prerequisite on modular arithmetic, you know that x ≡ y (mod n) means n divides (x - y). Substituting this definition, ax ≡ b (mod n) is exactly the same as asking: for what integer x does n divide (ax - b)? In other words, you are looking for integers x and k such that ax - b = kn, or equivalently ax - kn = b. This is a linear Diophantine equation in two unknowns, and from your study of divisibility and GCD, you know when such equations have solutions.

The **solvability condition** follows directly from Bezout's theorem, which you encountered with GCD. The equation ax - kn = b has integer solutions if and only if gcd(a, n) divides b. Intuitively: the set of all values that ax - kn can take (as x and k range over integers) is exactly the multiples of gcd(a, n). So b must be one of those multiples for a solution to exist. If gcd(a, n) = 1 — that is, if a and n are coprime — then the condition is automatically satisfied for any b, and there is a unique solution modulo n. This is the clean, familiar case: 3x ≡ 5 (mod 7) has exactly one solution mod 7 because gcd(3,7) = 1.

When a solution exists, finding it uses the **extended Euclidean algorithm** — an algorithm you have already studied for computing GCDs. The algorithm finds integers s and t such that as + nt = gcd(a, n). If gcd(a, n) divides b, say b = gcd(a, n) · m, then a(sm) + n(tm) = b, which means x = sm is a solution to ax ≡ b (mod n). From this one solution, all others are obtained by adding multiples of n / gcd(a, n): the full solution set is x ≡ x₀ (mod n/gcd(a,n)), generating exactly gcd(a, n) distinct residues modulo n.

Understanding linear congruences is the key to unlocking the **Chinese Remainder Theorem** (CRT), which solves systems of simultaneous congruences with different moduli. CRT is fundamental in computer science (fast arithmetic, cryptography) and number theory. It also leads directly to **modular inverses**: when gcd(a, n) = 1, the unique solution to ax ≡ 1 (mod n) is called the modular inverse of a, written a⁻¹ mod n — the modular analog of dividing by a. Every step from here relies on the solvability test and solution technique you are learning now.
