---
id: rsa-cryptosystem
title: The RSA Cryptosystem
domain: computer-science
course: cryptography
prerequisites:
- id: modular-arithmetic
  type: hard
- id: eulers-theorem
  type: hard
- id: fundamental-theorem-of-arithmetic
  type: hard
- id: hash-functions-and-collision-resistance
  type: soft
tags:
- rsa
- public-key-cryptography
- factoring
- trapdoor-function
stage: advanced
status: validated
---

# The RSA Cryptosystem

## Core Idea
RSA is a public-key cryptosystem whose security rests on the difficulty of factoring large integers. The public key (n, e) consists of a product n = pq of two large primes and an encryption exponent e. The private key d satisfies ed ≡ 1 (mod phi(n)). Encryption computes c = m^e mod n; decryption computes m = c^d mod n. Correctness follows from Euler's theorem. The trapdoor is factorization: computing d from (n, e) is easy if p and q are known but believed hard otherwise. RSA is used for key exchange and digital signatures, though direct RSA encryption requires padding schemes (OAEP) to be secure against chosen-ciphertext attacks.

## Questions

```yaml
- question: "Why does 'textbook RSA' — computing c = m^e mod n directly without padding — fail to achieve semantic security?"
  type: short-answer
  answer: "Textbook RSA is deterministic: the same plaintext always produces the same ciphertext. An adversary who wants to distinguish encryptions of m0 vs m1 simply computes m0^e mod n and compares with the ciphertext. Additionally, textbook RSA is multiplicatively homomorphic (E(m1) * E(m2) = E(m1*m2)), enabling chosen-ciphertext attacks. RSA-OAEP adds randomized padding before encryption, making it probabilistic and provably CCA-secure under the RSA assumption."
  explanation: "Semantic security (IND-CPA) requires that encryptions of different messages be indistinguishable. Any deterministic encryption fails this — the attacker can always check their guess by encrypting it. Padding schemes like OAEP introduce randomness and structure that eliminate these weaknesses. No one should ever use textbook RSA in practice."

- question: "RSA key generation requires finding two large primes p and q. Primality testing algorithms like Miller-Rabin are probabilistic. A student worries: what if the algorithm falsely certifies a composite as prime?"
  type: multiple-choice
  options:
    - "This cannot happen — Miller-Rabin is deterministic for numbers used in RSA"
    - "If n = pq where p or q is composite, RSA decryption may fail on some messages and the key is functionally broken. However, the probability of Miller-Rabin giving a false positive after k rounds is at most 4^(-k), so with k = 64 rounds the risk is negligible (less than 2^(-128))"
    - "Composite factors actually make RSA more secure because factoring becomes harder"
    - "The Chinese Remainder Theorem corrects for any composite factors during decryption"
  answer: 1
  explanation: "RSA's correctness depends on Euler's theorem, which requires p and q to be prime. If either is composite, phi(n) is computed incorrectly, and decryption fails for some messages. Miller-Rabin's false-positive rate of 4^(-k) means that 64 iterations give a false-positive probability below 2^(-128) — astronomically unlikely. In practice, this probabilistic guarantee is more than sufficient; the risk is far smaller than hardware errors."

- question: "An attacker knows the RSA public key (n, e) and wants to compute the private key d. Finding d is computationally equivalent to factoring n."
  type: true-false
  answer: true
  explanation: "This equivalence goes both ways. Given the factorization n = pq, computing d = e^(-1) mod phi(n) is straightforward. Conversely, if an attacker knows d (and e), they can efficiently factor n using a probabilistic algorithm that exploits the relationship ed - 1 = k*phi(n). So computing d without factoring n is exactly as hard as factoring n. This is why RSA's security reduces to the factoring assumption."

- question: "RSA with a 2048-bit modulus n is considered secure today. Why is doubling the key length to 4096 bits more than doubling the security?"
  type: multiple-choice
  options:
    - "Longer keys use more rounds of encryption, adding security multiplicatively"
    - "The best known factoring algorithm (General Number Field Sieve) has sub-exponential but super-polynomial runtime in the bit length of n. Doubling the bit length more than doubles the exponent in the runtime expression, providing a super-linear security increase"
    - "4096-bit keys are exactly twice as secure as 2048-bit keys"
    - "Longer keys enable more padding, which adds independent security"
  answer: 1
  explanation: "GNFS runs in time exp(O(n^{1/3} * (log n)^{2/3})) where n is the bit length. This is sub-exponential — faster than brute force but slower than polynomial. Because the exponent grows as n^{1/3}, doubling n multiplies the exponent by 2^{1/3} ≈ 1.26, which roughly squares the runtime (or more). The security increase is super-linear in key length, which is why RSA key sizes are measured in thousands of bits while symmetric key sizes are measured in hundreds."

- question: "For RSA signatures, the signer computes s = H(m)^d mod n and the verifier checks that s^e mod n equals H(m). Why is hashing the message before signing essential?"
  type: short-answer
  answer: "Without hashing, an attacker can forge signatures using RSA's multiplicative homomorphism: given signatures s1 = m1^d and s2 = m2^d on messages m1 and m2, the attacker computes s1 * s2 = (m1 * m2)^d mod n, which is a valid signature on m1 * m2. Hashing prevents this because H(m1 * m2) != H(m1) * H(m2) — the hash function is not homomorphic, so the algebraic attack fails. Additionally, hashing allows signing messages of any length with a fixed-size RSA operation."
  explanation: "The hash function acts as a barrier against algebraic manipulation. It converts the multiplicative structure of RSA — which an attacker could exploit — into an unstructured computation that the attacker cannot predict or control. Formal signature schemes (RSA-PSS) add randomized padding to the hash for additional security guarantees."
```

## Explainer

RSA, introduced by Rivest, Shamir, and Adleman in 1977, was the first practical public-key cryptosystem and remains widely deployed. Its core idea is a **trapdoor permutation**: a function that is easy to compute but hard to invert without a secret trapdoor. Key generation picks two large primes p and q, computes n = pq and phi(n) = (p-1)(q-1), chooses a public exponent e (commonly 65537) coprime to phi(n), and computes the private exponent d = e^{-1} mod phi(n). The public key is (n, e); the private key is d. Anyone can encrypt by computing c = m^e mod n, but only the holder of d can decrypt: m = c^d mod n. Correctness follows from Euler's theorem: since ed ≡ 1 mod phi(n), we have m^{ed} = m^{1 + k*phi(n)} = m * (m^{phi(n)})^k ≡ m mod n.

The security assumption is that **factoring n** is computationally hard when p and q are large random primes (each at least 1024 bits, giving a 2048-bit modulus). If an attacker could factor n, they could compute phi(n) and derive d directly. The best known classical factoring algorithm, the General Number Field Sieve, runs in sub-exponential time — faster than trying all possible factors but dramatically slower than polynomial. For 2048-bit moduli, GNFS is estimated to require roughly 2^112 operations, well beyond current capabilities. However, Shor's quantum algorithm factors in polynomial time, which is why RSA is considered vulnerable to future quantum computers and why post-quantum alternatives are being standardized.

A critical practical point is that **textbook RSA is insecure**. Encrypting as c = m^e mod n is deterministic (same message always gives same ciphertext), which violates semantic security. It is also multiplicatively homomorphic: E(m1) * E(m2) = E(m1 * m2) mod n, enabling algebraic attacks. Real RSA encryption uses **OAEP (Optimal Asymmetric Encryption Padding)**, which adds randomness and structure to the message before exponentiation, achieving provable CCA-security under the RSA assumption. Similarly, RSA signatures require hashing the message first (and adding randomized padding via PSS) to prevent forgery through multiplicative manipulation.

In practice, RSA is rarely used to encrypt bulk data directly because modular exponentiation is orders of magnitude slower than AES. Instead, RSA typically encrypts a random **session key** (a few hundred bits), and the session key is used with a fast symmetric cipher for the actual data. This hybrid approach — asymmetric cryptography for key exchange, symmetric cryptography for data — combines the convenience of public keys with the speed of symmetric encryption. RSA also serves as the basis for digital signature schemes, where the signer applies the private key to a hash of the message and any verifier can check using the public key.
