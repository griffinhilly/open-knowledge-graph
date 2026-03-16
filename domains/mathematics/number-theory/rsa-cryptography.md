---
id: rsa-cryptography
title: 'Cryptographic Applications: RSA'
domain: mathematics
course: number-theory
prerequisites:
- id: euler-theorem
  type: hard
- id: euler-totient-function
  type: soft
tags:
- rsa
- cryptography
- applications
- public-key
stage: advanced
status: draft
---

# Cryptographic Applications: RSA

## Core Idea
RSA encryption relies on the difficulty of factoring large numbers and the ease of computing modular exponentiation. Using Euler's theorem, encryption and decryption are inverse operations: (m^e)^d ≡ m (mod n) when ed ≡ 1 (mod φ(n)). Security depends on the computational hardness of factorization.

## Explainer

You've already proved **Euler's theorem**: if gcd(a, n) = 1, then a^φ(n) ≡ 1 (mod n), where φ is the Euler totient function. RSA is Euler's theorem transformed into a cryptographic protocol. The core asymmetry is that exponentiation mod n is fast to compute (using repeated squaring), but recovering the base from the result — without knowing the factorization of n — is believed to be computationally infeasible.

**Key generation** proceeds as follows. Choose two large distinct primes p and q, and let n = pq. Compute φ(n) = (p−1)(q−1). Choose a public exponent e with 1 < e < φ(n) and gcd(e, φ(n)) = 1. Use the extended Euclidean algorithm to find d with ed ≡ 1 (mod φ(n)). The **public key** is (n, e); the **private key** is d. To encrypt a message m encoded as an integer with 0 ≤ m < n, compute ciphertext c = mᵉ mod n. To decrypt, compute cᵈ mod n.

Why does decryption recover m? Because ed ≡ 1 (mod φ(n)), we have ed = 1 + k·φ(n) for some integer k. Then cᵈ = (mᵉ)ᵈ = m^(ed) = m^(1 + k·φ(n)) = m · (m^φ(n))^k ≡ m · 1ᵏ = m (mod n), by Euler's theorem — provided gcd(m, n) = 1. Encryption by e and decryption by d are inverse operations mod n precisely because their exponents multiply to 1 mod φ(n).

The **security** of RSA rests on the apparent hardness of factoring n. An adversary with the public key (n, e) who could factor n = pq would immediately compute φ(n) = (p−1)(q−1) and recover d = e⁻¹ mod φ(n). With 2048-bit primes, no known classical algorithm can factor n in feasible time. In practice, RSA encrypts a symmetric session key rather than raw data, and **padding schemes** like OAEP are mandatory — textbook RSA without padding leaks structure, since (m₁m₂)ᵉ = m₁ᵉ · m₂ᵉ mod n allows an attacker to combine ciphertexts multiplicatively.
