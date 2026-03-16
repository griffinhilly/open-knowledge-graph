---
id: discrete-logarithms
title: Discrete Logarithms
domain: mathematics
course: number-theory
prerequisites:
- id: primitive-roots-cyclic-groups-mod-p
  type: hard
- id: order-element-modulo-n
  type: hard
tags:
- discrete-log
- cryptography
- cyclic-groups
stage: advanced
status: draft
---

# Discrete Logarithms

## Core Idea
Given a primitive root g mod p and nonzero residue a, the discrete logarithm is the unique k (mod p-1) such that g^k ≡ a (mod p). Computing discrete logs is believed hard; this one-way function underpins Diffie-Hellman and elliptic-curve cryptography.

## Explainer

You already know that a **primitive root** g modulo p generates every nonzero residue as successive powers: g¹, g², g³, … cycle through all p-1 nonzero residues mod p before repeating. This means for any nonzero a mod p, there is exactly one exponent k in {0, 1, …, p-2} with g^k ≡ a (mod p). That exponent k is called the **discrete logarithm** of a to the base g, written log_g(a) mod (p-1). It is the modular analogue of the ordinary logarithm: just as log_b(x) asks "to what power must I raise b to get x?", the discrete log asks the same question inside Z/pZ.

The crucial asymmetry is computational. Given g, k, and p, computing g^k mod p is fast — repeated squaring does it in O(log k) multiplications. But given g, a, and p, finding k requires examining (in the naive case) each power of g until you hit a. For a prime p with hundreds of digits, this is astronomically slow. This **one-way function** property — easy in one direction, hard to reverse — is precisely what cryptographic protocols exploit. Diffie-Hellman key exchange works because two parties can combine public values derived from g^k mod p without an eavesdropper being able to recover k.

The discrete log obeys algebraic laws that mirror ordinary logarithms. From your knowledge of the order of elements, you know g^k has order (p-1)/gcd(k, p-1), so log_g(ab) ≡ log_g(a) + log_g(b) (mod p-1). This is the discrete analogue of log(xy) = log(x) + log(y). The exponents add in Z/(p-1)Z in the same way that ordinary logs add in the reals, because the group (Z/pZ)* is cyclic of order p-1, and g is a generator.

There are algorithms faster than brute force — **baby-step giant-step** runs in O(√p) time and space, and the **index calculus** method is subexponential for integers. This is why modern cryptographic systems use primes with thousands of bits, or move to elliptic curves where no index calculus analogue is known. The hardness assumption for discrete logs in carefully chosen groups remains one of the cornerstones of public-key cryptography.
