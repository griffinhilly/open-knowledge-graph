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
builds-toward:
- simultaneous-congruences-crt
- multiplicative-inverse-modular
tags:
- number-theory
- modular-arithmetic
- congruences
stage: formal-systems
status: draft
---

# Linear Congruences and Solutions

## Core Idea
A linear congruence ax ≡ b (mod n) has solutions if and only if gcd(a,n) divides b. When solutions exist, there are exactly gcd(a,n) distinct solutions modulo n. These can be found using the extended Euclidean algorithm.

## Explainer

A **linear congruence** ax ≡ b (mod n) is the modular-arithmetic analog of the linear equation ax = b. From your prerequisite on modular arithmetic, you know that x ≡ y (mod n) means n divides (x - y). Substituting this definition, ax ≡ b (mod n) is exactly the same as asking: for what integer x does n divide (ax - b)? In other words, you are looking for integers x and k such that ax - b = kn, or equivalently ax - kn = b. This is a linear Diophantine equation in two unknowns, and from your study of divisibility and GCD, you know when such equations have solutions.

The **solvability condition** follows directly from Bezout's theorem, which you encountered with GCD. The equation ax - kn = b has integer solutions if and only if gcd(a, n) divides b. Intuitively: the set of all values that ax - kn can take (as x and k range over integers) is exactly the multiples of gcd(a, n). So b must be one of those multiples for a solution to exist. If gcd(a, n) = 1 — that is, if a and n are coprime — then the condition is automatically satisfied for any b, and there is a unique solution modulo n. This is the clean, familiar case: 3x ≡ 5 (mod 7) has exactly one solution mod 7 because gcd(3,7) = 1.

When a solution exists, finding it uses the **extended Euclidean algorithm** — an algorithm you have already studied for computing GCDs. The algorithm finds integers s and t such that as + nt = gcd(a, n). If gcd(a, n) divides b, say b = gcd(a, n) · m, then a(sm) + n(tm) = b, which means x = sm is a solution to ax ≡ b (mod n). From this one solution, all others are obtained by adding multiples of n / gcd(a, n): the full solution set is x ≡ x₀ (mod n/gcd(a,n)), generating exactly gcd(a, n) distinct residues modulo n.

Understanding linear congruences is the key to unlocking the **Chinese Remainder Theorem** (CRT), which solves systems of simultaneous congruences with different moduli. CRT is fundamental in computer science (fast arithmetic, cryptography) and number theory. It also leads directly to **modular inverses**: when gcd(a, n) = 1, the unique solution to ax ≡ 1 (mod n) is called the modular inverse of a, written a⁻¹ mod n — the modular analog of dividing by a. Every step from here relies on the solvability test and solution technique you are learning now.
