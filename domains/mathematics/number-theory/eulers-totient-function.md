---
id: eulers-totient-function
title: Euler's Totient Function
domain: mathematics
course: number-theory
prerequisites:
- id: arithmetic-functions-multiplicativity
  type: hard
- id: modular-arithmetic
  type: hard
builds-toward:
- eulers-theorem
- primitive-roots-cyclic-groups-mod-p
- cryptographic-applications-rsa
tags:
- totient
- euler-phi
- coprime
stage: advanced
status: draft
---

# Euler's Totient Function

## Core Idea
Euler's totient function φ(n) counts the positive integers up to n that are coprime to n. For a prime power p^k, φ(p^k) = p^(k-1)(p-1). Since φ is multiplicative, φ(n) = n∏(1 - 1/p) over primes dividing n.

## How It's Best Learned
Compute φ(n) for small values and verify the formula. Recognize the multiplicative structure and its connection to cyclic groups.

## Common Misconceptions
Thinking φ(n) requires checking all n integers (use the formula instead). Confusing φ with other arithmetic functions like σ or τ.

## Explainer

The totient function asks: among the integers 1, 2, ..., n, how many share no common factor with n? If n = 12, the integers coprime to 12 are {1, 5, 7, 11} — just those sharing no factor of 2 or 3 — so φ(12) = 4. You already know modular arithmetic, so you know that working "mod n" means working within a set of residues; φ(n) precisely counts the size of the **multiplicative group** mod n, the residues that have multiplicative inverses. This connection is why the totient function appears everywhere in number theory and cryptography.

The formula φ(n) = n∏(1 − 1/p) over primes p dividing n comes from inclusion-exclusion. Start with n integers; remove the multiples of p₁ (there are n/p₁ of them), then the multiples of p₂, then add back the double-counted multiples of p₁p₂, and so on. Each prime factor p "knocks out" a fraction 1/p of the survivors, leaving a fraction (1 − 1/p). For n = 12 = 2² × 3: φ(12) = 12 × (1 − 1/2) × (1 − 1/3) = 12 × 1/2 × 2/3 = 4. The **multiplicativity** you studied — that φ(mn) = φ(m)φ(n) whenever gcd(m, n) = 1 — lets you decompose any n into its prime power factors first: φ(p^k) = p^{k−1}(p−1), because the only numbers not coprime to p^k are its p^{k−1} multiples.

The power of φ becomes visible in **Euler's theorem**: if gcd(a, n) = 1, then a^{φ(n)} ≡ 1 (mod n). This is a direct consequence of the multiplicative group having order φ(n) — every element raised to the group's order returns to the identity. Fermat's little theorem is the special case n = p prime, where φ(p) = p − 1. This interplay between counting (φ), modular arithmetic, and group structure is a microcosm of how number theory works: a simple counting question opens into deep algebraic structure.

The RSA cryptosystem rests entirely on φ. Given n = pq (a product of two large primes), φ(n) = (p−1)(q−1) is easy to compute if you know p and q, but essentially impossible if you only know n (factoring large integers is computationally hard). The encryption and decryption exponents are chosen to be inverses mod φ(n), and the security guarantee — that decryption undoes encryption — follows directly from Euler's theorem. The totient function thus bridges elementary arithmetic counting and the algorithms securing modern internet communication.
