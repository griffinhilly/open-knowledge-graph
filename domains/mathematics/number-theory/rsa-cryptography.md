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
- id: eulers-theorem
  type: hard
- id: eulers-totient-function
  type: hard
- id: fermats-little-theorem
  type: soft
- id: multiplicative-inverse-modular
  type: hard
- id: fermat-little-theorem
  type: soft
tags:
- rsa
- cryptography
- applications
- public-key
stage: advanced
status: validated
---

# Cryptographic Applications: RSA

## Core Idea
RSA encryption relies on the difficulty of factoring large numbers and the ease of computing modular exponentiation. Using Euler's theorem, encryption and decryption are inverse operations: (m^e)^d ≡ m (mod n) when ed ≡ 1 (mod φ(n)). Security depends on the computational hardness of factorization.

## How It's Best Learned
Run a full key cycle with numbers you can check by hand: p = 3, q = 11, n = 33, φ(n) = 20, e = 3, and d = 7 since 21 ≡ 1 (mod 20). Encrypt m = 4 to c = 64 mod 33 = 31. Decrypt using 31 ≡ −2: (−2)⁷ = −128 ≡ 4 (mod 33). Then try to find d from (33, 3) alone and notice that you need φ(33).

## Common Misconceptions
- The private exponent d is the inverse of e modulo n. (It is the inverse modulo φ(n). In the toy key, 3 has no inverse mod 33 at all, while 3 · 7 ≡ 1 (mod 20).)
- Computing φ(n) is easier than factoring n. (From n and φ(n) you get p + q = n − φ(n) + 1, and then p and q are the roots of a quadratic. So finding φ(n) is as hard as factoring.)
- RSA is secure because modular exponentiation is hard to compute. (Exponentiation is fast. The hard step is taking e-th roots mod n without knowing the factors.)
- Encrypting the same message twice gives different ciphertexts. (Textbook RSA is deterministic, which is one reason randomized padding such as OAEP is used.)

## Questions

```yaml
- question: "An adversary has RSA's public key (n, e) and wants to find the private key d. What information do they need that they cannot easily obtain?"
  type: multiple-choice
  options:
    - "The value of the ciphertext c = mᵉ mod n"
    - "The factorization of n into its prime factors p and q"
    - "The value of the modular inverse of e in ℤ"
    - "The bit-length of the modulus n"
  answer: 1
  explanation: "To find d, the attacker must compute d ≡ e⁻¹ (mod φ(n)). But computing φ(n) = (p−1)(q−1) requires knowing p and q — which requires factoring n. With a 2048-bit modulus, no known classical algorithm can factor n in feasible time. Options A and D give no useful information; option C is impossible to compute without φ(n)."

- question: "Textbook RSA without padding allows an attacker who intercepts ciphertexts c₁ = m₁ᵉ mod n and c₂ = m₂ᵉ mod n to compute the ciphertext of m₁·m₂ without knowing the messages. This attack works because:"
  type: multiple-choice
  options:
    - "The encryption exponent e is publicly known, so anyone can re-encrypt"
    - "RSA encryption is multiplicatively homomorphic: (m₁m₂)ᵉ ≡ m₁ᵉ · m₂ᵉ (mod n)"
    - "Modular exponentiation can be reversed with two ciphertext samples"
    - "The product m₁·m₂ is always smaller than n"
  answer: 1
  explanation: "Textbook RSA preserves multiplicative structure: (m₁m₂)ᵉ mod n equals (m₁ᵉ mod n)·(m₂ᵉ mod n) mod n. So c₁·c₂ mod n is a valid ciphertext for m₁m₂. This algebraic leakage is why padding schemes like OAEP are mandatory in practice — they destroy the clean algebraic structure that makes such manipulation possible."

- question: "RSA's security rests on the difficulty of computing discrete logarithms — recovering the exponent from a modular power."
  type: true-false
  answer: false
  explanation: "RSA's security rests on the hardness of *integer factorization*, not discrete logarithm. An attacker who can factor n = pq immediately recovers φ(n) = (p−1)(q−1) and then d = e⁻¹ mod φ(n). Discrete logarithm hardness underlies different cryptographic schemes such as Diffie-Hellman and elliptic curve cryptography."

- question: "If you know the two primes p and q used to generate an RSA key with public exponent e, you can compute the private key d."
  type: true-false
  answer: true
  explanation: "Yes. Knowing p and q lets you compute φ(n) = (p−1)(q−1), and then d = e⁻¹ mod φ(n) via the extended Euclidean algorithm. This is exactly why keeping p and q secret is the foundation of RSA security — the public key (n, e) reveals n but not its factors."

- question: "Why does RSA decryption correctly recover the original message m? Explain the mathematical reason, citing the key theorem involved."
  type: short-answer
  answer: "Decryption works because ed ≡ 1 (mod φ(n)), so ed = 1 + k·φ(n) for some integer k. Then (mᵉ)ᵈ = m^(ed) = m^(1+k·φ(n)) = m · (m^φ(n))^k ≡ m · 1 = m (mod n) by Euler's theorem, which states m^φ(n) ≡ 1 (mod n) when gcd(m, n) = 1. The choice of e and d as modular inverses mod φ(n) is precisely what makes encryption and decryption inverse operations."
  explanation: "The key is Euler's theorem. The exponents e (encrypt) and d (decrypt) are chosen to be multiplicative inverses mod φ(n), so raising m to the ed power mod n cycles back to m. Without knowing φ(n) — which requires factoring n — an attacker cannot find the right d, even though they know e and n."
```

## Explainer

You've already proved **Euler's theorem**: if gcd(a, n) = 1, then a^φ(n) ≡ 1 (mod n), where φ is the Euler totient function. RSA is Euler's theorem transformed into a cryptographic protocol. The core asymmetry is that exponentiation mod n is fast to compute (using repeated squaring), but recovering the base from the result — without knowing the factorization of n — is believed to be computationally infeasible.

**Key generation** proceeds as follows. Choose two large distinct primes p and q, and let n = pq. Compute φ(n) = (p−1)(q−1). Choose a public exponent e with 1 < e < φ(n) and gcd(e, φ(n)) = 1. Use the extended Euclidean algorithm to find d with ed ≡ 1 (mod φ(n)). The **public key** is (n, e); the **private key** is d. To encrypt a message m encoded as an integer with 0 ≤ m < n, compute ciphertext c = mᵉ mod n. To decrypt, compute cᵈ mod n.

Why does decryption recover m? Because ed ≡ 1 (mod φ(n)), we have ed = 1 + k·φ(n) for some integer k. Then cᵈ = (mᵉ)ᵈ = m^(ed) = m^(1 + k·φ(n)) = m · (m^φ(n))^k ≡ m · 1ᵏ = m (mod n), by Euler's theorem — provided gcd(m, n) = 1. Encryption by e and decryption by d are inverse operations mod n precisely because their exponents multiply to 1 mod φ(n).

The **security** of RSA rests on the apparent hardness of factoring n. An adversary with the public key (n, e) who could factor n = pq would immediately compute φ(n) = (p−1)(q−1) and recover d = e⁻¹ mod φ(n). With a 2048-bit modulus, no known classical algorithm can factor n in feasible time. In practice, RSA encrypts a symmetric session key rather than raw data, and **padding schemes** like OAEP are mandatory — textbook RSA without padding leaks structure, since (m₁m₂)ᵉ = m₁ᵉ · m₂ᵉ mod n allows an attacker to combine ciphertexts multiplicatively.
