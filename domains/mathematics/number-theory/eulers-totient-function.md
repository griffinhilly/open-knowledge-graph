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
- rsa-cryptography
tags:
- totient
- euler-phi
- coprime
stage: advanced
status: validated
---

# Euler's Totient Function

## Core Idea
Euler's totient function φ(n) counts the positive integers up to n that are coprime to n. For a prime power p^k, φ(p^k) = p^(k-1)(p-1). Since φ is multiplicative, φ(n) = n∏(1 - 1/p) over primes dividing n.

## How It's Best Learned
Compute φ(n) for small values and verify the formula. Recognize the multiplicative structure and its connection to cyclic groups.

## Common Misconceptions
Thinking φ(n) requires checking all n integers (use the formula instead). Confusing φ with other arithmetic functions like σ or τ.

## Questions

```yaml
- question: "What is φ(30)? (30 = 2 × 3 × 5)"
  type: multiple-choice
  options:
    - "φ(30) = 14, because you remove multiples of 2, 3, and 5 from 1–30"
    - "φ(30) = 8, using the formula 30 × (1 − 1/2) × (1 − 1/3) × (1 − 1/5) = 8"
    - "φ(30) = 12, because 30 has 3 prime factors and each contributes 4 coprime integers"
    - "φ(30) = 15, because exactly half of the integers up to 30 share no factor of 2"
  answer: 1
  explanation: "φ(30) = 30 × (1 − 1/2) × (1 − 1/3) × (1 − 1/5) = 30 × (1/2) × (2/3) × (4/5) = 8. The integers coprime to 30 in {1,...,30} are {1, 7, 11, 13, 17, 19, 23, 29} — exactly 8. The formula works by inclusion-exclusion: start with 30, remove the 15 multiples of 2, the 10 multiples of 3, the 6 multiples of 5, then add back the double-counted multiples of 6, 10, 15, subtract multiples of 30. The product formula compresses this entire inclusion-exclusion into a single expression."

- question: "For any prime number p, φ(p) = p − 1. Why?"
  type: multiple-choice
  options:
    - "Because all even numbers less than p are not coprime to p, leaving p − 1 odd numbers"
    - "Because the only positive factor of a prime p is 1 and p itself, so all integers from 1 to p−1 are coprime to p"
    - "Because the multiplicative group mod p has exactly p − 1 generators"
    - "Because p − 1 is always even, ensuring the group has exactly two generators"
  answer: 1
  explanation: "A prime p has exactly two positive divisors: 1 and p. Therefore, gcd(k, p) = 1 for every k in {1, 2, ..., p−1} — none of these share any common factor with p. All p−1 integers below p are coprime to p, so φ(p) = p − 1. From the formula: φ(p) = p × (1 − 1/p) = p − 1. This is also why Fermat's little theorem states a^(p−1) ≡ 1 (mod p) for gcd(a,p) = 1 — the multiplicative group mod p has order p − 1."

- question: "φ(n) equals the number of elements in the multiplicative group of integers modulo n — that is, the count of residues in {1, ..., n−1} that have multiplicative inverses mod n."
  type: true-false
  answer: true
  explanation: "An integer k has a multiplicative inverse mod n if and only if gcd(k, n) = 1. This is exactly the condition that φ(n) counts. So φ(n) is both 'the count of integers up to n coprime to n' and 'the order of the multiplicative group (ℤ/nℤ)×'. This dual interpretation — counting coprime integers vs. measuring group size — is why φ appears in Euler's theorem: raising any element of the group to the power equal to the group's order returns the identity element 1."

- question: "φ(mn) = φ(m)φ(n) for most positive integers m and n."
  type: true-false
  answer: false
  explanation: "This is the multiplicativity property, but it only holds when gcd(m, n) = 1. For example, φ(4) = 2, φ(2) = 1, but 4 = 2 × 2 and gcd(2, 2) = 2 ≠ 1, so φ(4) = 2 ≠ φ(2)φ(2) = 1. The correct statement is: φ is a *multiplicative* arithmetic function, meaning φ(mn) = φ(m)φ(n) whenever gcd(m, n) = 1. This condition is essential — it is what allows you to decompose n into prime powers and compute φ separately for each."

- question: "Explain why knowing φ(n) for n = pq (a product of two large primes) is computationally easy if you know p and q, but essentially impossible if you only know n — and why RSA's security depends on this."
  type: short-answer
  answer: "If you know p and q, then φ(pq) = (p−1)(q−1), computable in a single multiplication. But if you only know n, recovering φ(n) requires knowing p and q — which requires factoring n. Factoring the product of two large primes (each ~1000+ bits) is believed to be computationally intractable with current algorithms. RSA exploits this: n = pq is public, but φ(n) = (p−1)(q−1) is kept secret. Encryption and decryption exponents are chosen as inverses mod φ(n), and Euler's theorem guarantees that decryption undoes encryption. An attacker who cannot factor n cannot compute φ(n) and cannot find the decryption key."
  explanation: "The security of RSA reduces to the integer factorization problem: no efficient classical algorithm is known for factoring large semi-primes. The connection to φ is direct — knowing any one of {p, q, φ(n), d (the decryption exponent)} allows you to recover all the others efficiently. So factoring n, computing φ(n), and breaking RSA are computationally equivalent problems. This is why φ, a pure number-theoretic counting function, sits at the heart of the most widely deployed asymmetric encryption scheme."
```

## Explainer

The totient function asks: among the integers 1, 2, ..., n, how many share no common factor with n? If n = 12, the integers coprime to 12 are {1, 5, 7, 11} — just those sharing no factor of 2 or 3 — so φ(12) = 4. You already know modular arithmetic, so you know that working "mod n" means working within a set of residues; φ(n) precisely counts the size of the **multiplicative group** mod n, the residues that have multiplicative inverses. This connection is why the totient function appears everywhere in number theory and cryptography.

The formula φ(n) = n∏(1 − 1/p) over primes p dividing n comes from inclusion-exclusion. Start with n integers; remove the multiples of p₁ (there are n/p₁ of them), then the multiples of p₂, then add back the double-counted multiples of p₁p₂, and so on. Each prime factor p "knocks out" a fraction 1/p of the survivors, leaving a fraction (1 − 1/p). For n = 12 = 2² × 3: φ(12) = 12 × (1 − 1/2) × (1 − 1/3) = 12 × 1/2 × 2/3 = 4. The **multiplicativity** you studied — that φ(mn) = φ(m)φ(n) whenever gcd(m, n) = 1 — lets you decompose any n into its prime power factors first: φ(p^k) = p^{k−1}(p−1), because the only numbers not coprime to p^k are its p^{k−1} multiples.

The power of φ becomes visible in **Euler's theorem**: if gcd(a, n) = 1, then a^{φ(n)} ≡ 1 (mod n). This is a direct consequence of the multiplicative group having order φ(n) — every element raised to the group's order returns to the identity. Fermat's little theorem is the special case n = p prime, where φ(p) = p − 1. This interplay between counting (φ), modular arithmetic, and group structure is a microcosm of how number theory works: a simple counting question opens into deep algebraic structure.

The RSA cryptosystem rests entirely on φ. Given n = pq (a product of two large primes), φ(n) = (p−1)(q−1) is easy to compute if you know p and q, but essentially impossible if you only know n (factoring large integers is computationally hard). The encryption and decryption exponents are chosen to be inverses mod φ(n), and the security guarantee — that decryption undoes encryption — follows directly from Euler's theorem. The totient function thus bridges elementary arithmetic counting and the algorithms securing modern internet communication.
