---
id: elliptic-curve-cryptography-basics
title: Elliptic Curve Cryptography Basics
domain: computer-science
course: cryptography
prerequisites:
- id: diffie-hellman-key-exchange
  type: hard
- id: modular-arithmetic
  type: hard
tags:
- elliptic-curve
- ecdh
- ecdsa
- point-multiplication
- curve25519
stage: advanced
status: validated
---

# Elliptic Curve Cryptography Basics

## Core Idea
Elliptic curve cryptography (ECC) performs the same operations as classical public-key cryptography (DH, DSA, encryption) but over the group of points on an elliptic curve rather than the multiplicative group of integers modulo a prime. The key advantage is efficiency: the best known attacks on elliptic curve discrete logarithms (Pollard's rho) run in O(sqrt(n)) time, compared to sub-exponential algorithms for integer factorization and modular discrete logarithms. A 256-bit elliptic curve provides ~128 bits of security, matching a 3072-bit RSA/DH key. This makes ECC the default choice for modern protocols (TLS 1.3, Signal, SSH).

## Questions

```yaml
- question: "Why does a 256-bit elliptic curve key provide equivalent security to a 3072-bit RSA key? What fundamental difference in attack complexity explains this?"
  type: short-answer
  answer: "The best known attack on the elliptic curve discrete logarithm problem (ECDLP) in well-chosen curves is Pollard's rho algorithm, which runs in O(sqrt(n)) = O(2^{128}) time for a 256-bit curve. No sub-exponential algorithm analogous to the Number Field Sieve exists for ECDLP. For RSA, the GNFS runs in sub-exponential time L(1/3), so a 3072-bit modulus is needed to reach the same 2^{128} operation threshold. The absence of sub-exponential attacks on curves means shorter keys achieve the same security."
  explanation: "This efficiency gap exists because elliptic curve groups lack the special algebraic structure (smooth element orders, index calculus) that enables sub-exponential factoring and discrete logarithm algorithms in integer groups. The curves commonly used in cryptography are chosen specifically to resist all known structural attacks, leaving generic algorithms as the best approach."

- question: "Points on an elliptic curve form a group under 'point addition.' What is the geometric intuition for this operation?"
  type: multiple-choice
  options:
    - "Two points are added by averaging their coordinates"
    - "To add points P and Q, draw the line through them. It intersects the curve at a third point R. The sum P + Q is the reflection of R across the x-axis"
    - "Points are added by concatenating their coordinate representations"
    - "Point addition is matrix multiplication of the coordinate vectors"
  answer: 1
  explanation: "This geometric construction defines an abelian group: the operation is commutative, associative, has an identity element (the 'point at infinity'), and every point has an inverse (its reflection across the x-axis). Cryptography uses this in the 'scalar multiplication' operation: computing nP = P + P + ... + P (n times). Given P and nP, finding n is the elliptic curve discrete logarithm problem. Over finite fields, the visual geometry no longer applies but the algebraic formulas derived from it are identical."

- question: "NIST P-256 and Curve25519 are both widely used elliptic curves. Curve25519 was designed to be 'safe by default.' What design choices make it safer to implement?"
  type: multiple-choice
  options:
    - "Curve25519 uses a larger field size, providing more security bits"
    - "Curve25519 is a Montgomery curve designed for constant-time scalar multiplication, has no special points requiring edge-case handling, and uses a prime (2^255 - 19) that enables simple, fast modular arithmetic. NIST P-256 requires careful implementation to avoid timing side channels and has more complex formulas with edge cases"
    - "Curve25519 uses post-quantum algorithms while NIST P-256 does not"
    - "Curve25519 encrypts data directly while P-256 is only for key exchange"
  answer: 1
  explanation: "Curve25519 was designed by Daniel Bernstein with implementation safety as a primary goal. The Montgomery ladder for scalar multiplication naturally runs in constant time (no branches on secret data). The prime 2^255 - 19 is close to a power of 2, simplifying field arithmetic. The curve has cofactor 8, which is handled cleanly in the X25519 protocol. By contrast, NIST P-256's random-looking parameters have fueled suspicion of backdoors, and its Weierstrass form requires careful handling of the point at infinity and exceptional cases in addition formulas. Both curves are believed secure, but Curve25519 is much harder to implement incorrectly."

- question: "Elliptic curve cryptography is vulnerable to Shor's quantum algorithm, just like RSA and classical DH."
  type: true-false
  answer: true
  explanation: "Shor's algorithm solves the discrete logarithm problem in any finite abelian group, including elliptic curve groups, in polynomial time on a quantum computer. ECC's shorter key lengths actually make it slightly easier to attack with quantum computers than RSA (a 256-bit curve requires fewer logical qubits than a 3072-bit RSA modulus). This is why post-quantum cryptography research focuses on mathematical problems that resist quantum attacks: lattices, codes, multivariate polynomials, and isogenies. Current recommendations call for hybrid schemes using both ECC and post-quantum algorithms during the transition."

- question: "The 'scalar multiplication' operation kP (adding a curve point P to itself k times) can be computed in O(log k) group operations using the double-and-add algorithm, even though it involves k additions."
  type: true-false
  answer: true
  explanation: "Double-and-add is the elliptic curve analog of fast modular exponentiation (square-and-multiply). To compute kP, write k in binary. Scan bits from most significant to least: for each bit, double the current accumulator; if the bit is 1, also add P. A 256-bit scalar requires at most 256 doublings and 256 additions — O(log k) group operations. Without this, computing kP would require k - 1 additions, which for a 256-bit k is astronomically infeasible. This logarithmic cost is what makes ECC practical."
```

## Explainer

Classical public-key cryptography (RSA, DH) works in the multiplicative group of integers modulo a large prime or composite number. These groups are well-understood mathematically, which is both their strength (clear security analysis) and their weakness (sub-exponential algorithms like the Number Field Sieve exploit their structure). **Elliptic Curve Cryptography (ECC)** performs the same cryptographic operations — key exchange, signatures, encryption — but in a different mathematical group: the set of points on an elliptic curve over a finite field, where the "addition" operation has a geometric definition that translates cleanly into algebraic formulas.

An elliptic curve over a prime field F_p is defined by an equation like y^2 = x^3 + ax + b mod p. The set of solutions (x, y), together with a special "point at infinity" serving as the identity element, forms an abelian group under **point addition**. Given two points P and Q on the curve, their sum is defined geometrically (draw the line through P and Q, find its third intersection with the curve, reflect across the x-axis) and computed algebraically using field operations. **Scalar multiplication** — computing kP = P + P + ... + P (k times) — is the elliptic curve analog of modular exponentiation. The **elliptic curve discrete logarithm problem (ECDLP)** asks: given P and Q = kP, find k. This is the hard problem underpinning all of ECC.

The critical advantage of ECC is that no sub-exponential algorithm is known for ECDLP on well-chosen curves. The best generic attack is **Pollard's rho**, which runs in O(sqrt(n)) time where n is the group order. For a 256-bit curve (group order around 2^256), this gives roughly 2^128 operations — matching the security of 3072-bit RSA, which requires a much larger key because the Number Field Sieve attacks it in sub-exponential time. This roughly 12x key size advantage translates directly into faster computation, lower bandwidth, and smaller certificates, which is why **ECDH** (Elliptic Curve Diffie-Hellman) and **ECDSA** (Elliptic Curve Digital Signature Algorithm) have largely replaced their classical counterparts. TLS 1.3, the current web security standard, uses ECDH exclusively for key exchange.

Curve selection matters enormously. The NIST curves (P-256, P-384, P-521) are defined over random-looking primes with parameters that some researchers find suspicious (were they chosen to enable a backdoor?). **Curve25519**, designed by Daniel Bernstein, uses the prime 2^255 - 19 (chosen for fast arithmetic), a Montgomery curve form that enables constant-time scalar multiplication (preventing timing side channels), and fully specified parameters with clear design rationale. Its signature variant **Ed25519** has become the default for SSH keys, Signal messages, and many other applications. Both NIST curves and Curve25519 are believed secure against classical attacks, but ECC as a whole falls to **Shor's quantum algorithm**, motivating the parallel development of post-quantum cryptography based on lattices and other quantum-resistant problems.
