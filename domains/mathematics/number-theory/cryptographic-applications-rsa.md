---
id: cryptographic-applications-rsa
title: Cryptographic Applications (RSA)
domain: mathematics
course: number-theory
prerequisites:
- id: eulers-theorem
  type: hard
- id: eulers-totient-function
  type: hard
- id: modular-arithmetic
  type: hard
tags:
- rsa
- cryptography
- public-key
stage: advanced
status: draft
---

# Cryptographic Applications (RSA)

## Core Idea
RSA uses Euler's theorem and the difficulty of factoring large numbers. Given n = pq (p, q distinct primes), pick e coprime to φ(n) = (p-1)(q-1), compute d ≡ e^(-1) (mod φ(n)), encrypt m as c ≡ m^e (mod n), and decrypt as m ≡ c^d (mod n). Security rests on n's factorization being hard.

## Explainer

RSA is built entirely from the number theory you already know, assembled into an elegant trap. Recall **Euler's theorem**: if gcd(m, n) = 1, then m^φ(n) ≡ 1 (mod n). And recall that **Euler's totient function** φ(pq) = (p−1)(q−1) when p and q are distinct primes. RSA turns these facts into a one-way trapdoor: certain operations are easy to perform but computationally infeasible to reverse without secret information.

Here is how the system is constructed. Choose two large primes p and q, and form n = pq. Compute φ(n) = (p−1)(q−1). Now pick any e with 1 < e < φ(n) and gcd(e, φ(n)) = 1 — the **public exponent**. Since e is coprime to φ(n), Bézout's identity guarantees a **private exponent** d satisfying ed ≡ 1 (mod φ(n)). The public key is the pair (n, e); the private key is d (and ideally p, q are discarded). To encrypt a message m < n, compute c ≡ m^e (mod n). To decrypt, compute c^d ≡ (m^e)^d = m^(ed) (mod n). Since ed ≡ 1 (mod φ(n)), we have ed = 1 + kφ(n) for some integer k, so m^(ed) = m · (m^φ(n))^k ≡ m · 1^k = m (mod n) by Euler's theorem. Decryption recovers exactly the original message.

The security argument rests on the **integer factorization problem**. Anyone who knows e and n can encrypt, but to compute d they would need φ(n) = (p−1)(q−1), which requires knowing p and q. Factoring n into p and q is believed to be computationally hard for large n (thousands of bits). An adversary who intercepts c = m^e (mod n) and knows (n, e) is stuck: computing e-th roots modulo a composite n without knowing the factorization is believed to be as hard as factoring n itself. This asymmetry — easy to lock, hard to unlock without the key — is the essence of **public-key cryptography**.

A concrete small example: take p = 61, q = 53, so n = 3233 and φ(n) = 60 × 52 = 3120. Choose e = 17 (since gcd(17, 3120) = 1). Then d = 2753 (since 17 × 2753 = 46801 = 1 + 15 × 3120). To encrypt m = 65: c = 65^17 mod 3233 = 2790. To decrypt: 2790^2753 mod 3233 = 65. In practice p and q each have hundreds of digits, making factoring n infeasible with all known algorithms. RSA is the foundational example of how pure number theory — congruences, totient functions, and Euler's theorem — becomes the backbone of modern secure communications.
