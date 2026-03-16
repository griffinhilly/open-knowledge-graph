---
id: wilsons-theorem
title: Wilson's Theorem
domain: mathematics
course: number-theory
prerequisites:
- id: congruence-properties
  type: hard
tags:
- wilsons-theorem
- factorial
- prime-characterization
stage: advanced
status: draft
---

# Wilson's Theorem

## Core Idea
p is prime if and only if (p-1)! ≡ -1 (mod p). While elegant, this is computationally impractical for primality testing but illustrates the special structure of multiplicative groups mod p and provides a theoretical prime characterization.

## Explainer

From your study of congruence properties, you know that when p is prime, every integer from 1 to p−1 has a **multiplicative inverse mod p** — a unique number in {1, ..., p−1} that multiplies with it to give 1. This is because gcd(a, p) = 1 for all such a. Wilson's theorem asks: what happens when you multiply all these numbers together? The answer, (p−1)! ≡ −1 (mod p), seems surprising at first, but the proof emerges naturally once you pair each number with its inverse.

The key observation is that most elements in {1, 2, ..., p−1} pair up with a distinct inverse. For example, mod 7: 2 pairs with 4 (since 2·4 = 8 ≡ 1), 3 pairs with 5 (since 3·5 = 15 ≡ 1). Each such pair contributes a factor of 1 to the product. The only elements that are **self-inverse** — satisfying a² ≡ 1 (mod p), i.e., a ≡ ±1 (mod p) — are 1 and p−1 (which is −1 mod p). So when you form the product (p−1)!, all the middle terms cancel in pairs to 1, leaving just 1·(p−1) = p−1 ≡ −1 (mod p). That is the entire proof.

The biconditional is what makes Wilson's theorem a **characterization** of primes, not just a property of them. If n is composite, say n = ab with 1 < a ≤ b < n, then a divides (n−1)! (since a appears as one of the factors in the product), which means a also divides any multiple of (n−1)!. But if (n−1)! ≡ −1 (mod n) were true, then n would divide (n−1)! + 1, and since a divides n it would also divide (n−1)! + 1 — yet a already divides (n−1)!, so a would divide 1, a contradiction. This is why the congruence fails for composite n.

The practical limitation is obvious: computing (p−1)! for large p is astronomically expensive, making this useless as a primality test in practice. But its theoretical value is real. It gives an exact algebraic fingerprint of primality — a number is prime if and only if its "factorial residue" hits −1. It also previews deeper structure: the fact that the only self-inverse elements mod p are ±1 is a consequence of the multiplicative group (ℤ/pℤ)* being a **cyclic group** of order p−1, a result that underpins Fermat's little theorem and Euler's theorem, which you will study next.
