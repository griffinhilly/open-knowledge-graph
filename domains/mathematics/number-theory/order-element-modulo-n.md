---
id: order-element-modulo-n
title: Order of an Element Modulo n
domain: mathematics
course: number-theory
prerequisites:
- id: fermats-little-theorem
  type: hard
- id: congruence-properties
  type: hard
builds-toward:
- primitive-roots-cyclic-groups-mod-p
- discrete-logarithms
tags:
- order
- multiplicative-group
- exponents
stage: advanced
status: draft
---

# Order of an Element Modulo n

## Core Idea
The order of a mod n (with gcd(a,n) = 1) is the smallest positive k such that a^k ≡ 1 (mod n). The order divides φ(n) by Lagrange's theorem, and equals φ(n) precisely when a is a primitive root.

## Explainer

From your work with Fermat's Little Theorem, you know that if p is prime and gcd(a, p) = 1, then a^(p−1) ≡ 1 (mod p). But the exponent p−1 might not be the *smallest* such exponent — the powers of a might reset to 1 even earlier. The **order** of a modulo n pins down exactly when this first reset happens.

Take a = 2 and n = 7. Compute: 2¹ ≡ 2, 2² ≡ 4, 2³ ≡ 1 (mod 7). The order of 2 mod 7 is 3. Now try a = 3 mod 7: 3¹ ≡ 3, 3² ≡ 2, 3³ ≡ 6, 3⁴ ≡ 4, 3⁵ ≡ 5, 3⁶ ≡ 1 (mod 7). The order of 3 is 6, which equals φ(7) = 6. That makes 3 a **primitive root** mod 7 — its powers cycle through all 6 nonzero residues before returning to 1.

The key structural fact is that the order of a always **divides** φ(n). This is an application of Lagrange's theorem from group theory: the powers of a form a cyclic subgroup of the units modulo n, and subgroup sizes always divide the group size. Practically, this means you only need to check divisors of φ(n) when hunting for the order — you never need to check all exponents up to φ(n). For example, if φ(n) = 12, the possible orders are 1, 2, 3, 4, 6, or 12.

The **order** concept connects congruence arithmetic to the deeper structure of multiplicative groups. An element with order equal to φ(n) is a primitive root, and its existence (or non-existence) determines the structure of the entire group of units modulo n. This distinction — between elements that generate the whole group and those that don't — is foundational for discrete logarithms and the cryptographic hardness assumptions underlying protocols like Diffie-Hellman key exchange.
