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
status: validated
---

# Cryptographic Applications (RSA)

## Core Idea
RSA uses Euler's theorem and the difficulty of factoring large numbers. Given n = pq (p, q distinct primes), pick e coprime to φ(n) = (p-1)(q-1), compute d ≡ e^(-1) (mod φ(n)), encrypt m as c ≡ m^e (mod n), and decrypt as m ≡ c^d (mod n). Security rests on n's factorization being hard.

## Questions

```yaml
- question: "An attacker intercepts ciphertext c and knows the public key (n, e). What does the attacker need in order to compute the private key d?"
  type: multiple-choice
  options:
    - "More ciphertext samples to analyze the pattern of encryption"
    - "The factorization of n into its prime factors p and q"
    - "The value of e raised to a high power modulo n"
    - "A collision in the encryption function m^e mod n"
  answer: 1
  explanation: "The private key d satisfies ed ≡ 1 (mod φ(n)), so computing d requires knowing φ(n) = (p−1)(q−1). But φ(n) can only be calculated if you know p and q — which requires factoring n. An adversary who knows only (n, e) cannot compute φ(n) without factoring n, and factoring large n is computationally infeasible with current algorithms. This asymmetry — anyone can encrypt, but only the key-holder (who knows p and q) can decrypt — is the core security guarantee of RSA."

- question: "In RSA, decryption works because m^(ed) ≡ m (mod n). Which number-theoretic theorem guarantees this?"
  type: multiple-choice
  options:
    - "The Chinese Remainder Theorem, which decomposes computation mod pq into computations mod p and mod q"
    - "Euler's theorem: if gcd(m, n) = 1, then m^φ(n) ≡ 1 (mod n)"
    - "Fermat's Last Theorem, which rules out unwanted modular coincidences"
    - "The fundamental theorem of arithmetic, which guarantees unique prime factorization of n"
  answer: 1
  explanation: "Since ed ≡ 1 (mod φ(n)), we have ed = 1 + kφ(n) for some integer k. Therefore m^(ed) = m^(1+kφ(n)) = m · (m^φ(n))^k ≡ m · 1^k = m (mod n) by Euler's theorem. The Chinese Remainder Theorem is useful for speeding up RSA computations but is not what guarantees correctness. Fermat's Last Theorem and unique factorization are both irrelevant to the decryption argument."

- question: "RSA is secure even against an adversary who knows the encryption algorithm and all public information, as long as factoring large integers remains computationally hard."
  type: true-false
  answer: true
  explanation: "RSA is an example of security-through-computational-hardness rather than security-through-obscurity. The encryption algorithm, the public key (n, e), and the ciphertext can all be fully public. Security rests entirely on the fact that computing d from (n, e) requires factoring n, which is believed to require superpolynomial time for large n with all known classical algorithms."

- question: "RSA's security relies on the difficulty of the discrete logarithm problem — computing x from g^x mod p."
  type: true-false
  answer: false
  explanation: "RSA's security relies on the difficulty of integer factorization — computing p and q from n = pq. The discrete logarithm problem underlies different cryptosystems such as Diffie-Hellman key exchange and elliptic curve cryptography. While both are believed to be computationally hard, they are distinct problems. A quantum computer running Shor's algorithm can efficiently solve both, which is why both RSA and Diffie-Hellman are vulnerable to quantum attacks."

- question: "Why can't someone who knows the public key (n, e) simply compute the private key d directly from the relation ed ≡ 1 (mod φ(n))?"
  type: short-answer
  answer: "Computing d requires knowing φ(n) = (p−1)(q−1), which in turn requires knowing the prime factors p and q of n. The public key only reveals n and e, not p and q. Although n = pq is known, factoring n to recover p and q is computationally infeasible for large n with all known algorithms. Without φ(n), the modular inverse equation ed ≡ 1 (mod φ(n)) cannot be solved."
  explanation: "This is the essential asymmetry that makes RSA work: computing d is easy if you know p and q (just compute φ(n) and apply the extended Euclidean algorithm), but hard if you know only n. The mathematical relationship ed ≡ 1 (mod φ(n)) is well-understood — the hardness is entirely in obtaining φ(n) without the factorization."
```

## Explainer

RSA is built entirely from the number theory you already know, assembled into an elegant trap. Recall **Euler's theorem**: if gcd(m, n) = 1, then m^φ(n) ≡ 1 (mod n). And recall that **Euler's totient function** φ(pq) = (p−1)(q−1) when p and q are distinct primes. RSA turns these facts into a one-way trapdoor: certain operations are easy to perform but computationally infeasible to reverse without secret information.

Here is how the system is constructed. Choose two large primes p and q, and form n = pq. Compute φ(n) = (p−1)(q−1). Now pick any e with 1 < e < φ(n) and gcd(e, φ(n)) = 1 — the **public exponent**. Since e is coprime to φ(n), Bézout's identity guarantees a **private exponent** d satisfying ed ≡ 1 (mod φ(n)). The public key is the pair (n, e); the private key is d (and ideally p, q are discarded). To encrypt a message m < n, compute c ≡ m^e (mod n). To decrypt, compute c^d ≡ (m^e)^d = m^(ed) (mod n). Since ed ≡ 1 (mod φ(n)), we have ed = 1 + kφ(n) for some integer k, so m^(ed) = m · (m^φ(n))^k ≡ m · 1^k = m (mod n) by Euler's theorem. Decryption recovers exactly the original message.

The security argument rests on the **integer factorization problem**. Anyone who knows e and n can encrypt, but to compute d they would need φ(n) = (p−1)(q−1), which requires knowing p and q. Factoring n into p and q is believed to be computationally hard for large n (thousands of bits). An adversary who intercepts c = m^e (mod n) and knows (n, e) is stuck: computing e-th roots modulo a composite n without knowing the factorization is believed to be as hard as factoring n itself. This asymmetry — easy to lock, hard to unlock without the key — is the essence of **public-key cryptography**.

A concrete small example: take p = 61, q = 53, so n = 3233 and φ(n) = 60 × 52 = 3120. Choose e = 17 (since gcd(17, 3120) = 1). Then d = 2753 (since 17 × 2753 = 46801 = 1 + 15 × 3120). To encrypt m = 65: c = 65^17 mod 3233 = 2790. To decrypt: 2790^2753 mod 3233 = 65. In practice p and q each have hundreds of digits, making factoring n infeasible with all known algorithms. RSA is the foundational example of how pure number theory — congruences, totient functions, and Euler's theorem — becomes the backbone of modern secure communications.
