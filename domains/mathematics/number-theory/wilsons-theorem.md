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

## Questions

```yaml
- question: "You compute 10! mod 11 and get 10. Does Wilson's theorem confirm that 11 is prime?"
  type: multiple-choice
  options:
    - "Yes — since 10 ≡ −1 (mod 11), this satisfies Wilson's condition and confirms 11 is prime"
    - "No — Wilson's theorem only applies when (p−1)! ≡ 0 (mod p)"
    - "Yes — but only because 10! happened to be divisible by a factor of 11−1"
    - "Cannot determine — Wilson's theorem requires computing the result in a different form"
  answer: 0
  explanation: "10 ≡ −1 (mod 11) because 10 = 11 − 1. So 10! ≡ −1 (mod 11), which is exactly the condition Wilson's theorem requires. Since the congruence holds, Wilson's theorem confirms 11 is prime. Option B confuses the condition — Wilson's theorem requires (p−1)! ≡ −1 (mod p), not ≡ 0."

- question: "For a prime p, what happens to the elements {2, 3, ..., p−2} when computing (p−1)! mod p?"
  type: multiple-choice
  options:
    - "They are each divisible by p, so they contribute 0 to the product"
    - "They alternate in sign, canceling each other out"
    - "Each pairs with its distinct multiplicative inverse in the same set, contributing a factor of 1 to the product"
    - "They collectively produce a factor of (p−1)/2, which then cancels with the remaining terms"
  answer: 2
  explanation: "Every element a in {2, ..., p−2} has a multiplicative inverse mod p that is also in {2, ..., p−2} and distinct from a — the only self-inverse elements are 1 and p−1 (since a² ≡ 1 mod p implies a ≡ ±1 mod p). Each pair a · a⁻¹ ≡ 1 (mod p), so all these terms cancel to 1. What remains in the product is just 1 · (p−1) = p−1 ≡ −1 (mod p)."

- question: "Wilson's theorem provides an efficient algorithm for determining whether a large number is prime, since it gives an exact characterization of primality."
  type: true-false
  answer: false
  explanation: "Wilson's theorem provides a theoretically exact characterization — p is prime if and only if (p−1)! ≡ −1 (mod p) — but computing (p−1)! for large p is astronomically expensive. A number with 100 digits would require computing a factorial of roughly 10^100 terms. This makes it completely impractical as a primality test. Its value is theoretical, not computational."

- question: "In the proof of Wilson's theorem, the reason the product (p−1)! simplifies cleanly is that 1 and p−1 are the only elements in {1, ..., p−1} that are their own multiplicative inverses mod p."
  type: true-false
  answer: true
  explanation: "An element a is self-inverse if a² ≡ 1 (mod p), i.e., p divides (a−1)(a+1). Since p is prime, p must divide a−1 or a+1, giving a ≡ 1 or a ≡ −1 ≡ p−1 (mod p). These are the only two self-inverse elements. All other elements pair with a distinct inverse, contributing 1 to the product, leaving just 1 · (p−1) ≡ −1 (mod p)."

- question: "Why does Wilson's theorem fail for composite numbers? Explain why (n−1)! ≢ −1 (mod n) when n is composite."
  type: short-answer
  answer: "When n is composite, n has a factor a with 1 < a < n. Since a ≤ n−1, a appears as one of the factors in (n−1)!, so a divides (n−1)!. If (n−1)! ≡ −1 (mod n) were true, then n would divide (n−1)! + 1, and since a divides n, a would also divide (n−1)! + 1 — yet a already divides (n−1)!, so a would divide their difference 1. This is a contradiction since a > 1."
  explanation: "The core issue is that composite numbers have factors smaller than themselves that appear in the factorial. The congruence (n−1)! ≡ −1 (mod n) would require n to divide (n−1)! + 1, but any nontrivial factor of n also divides (n−1)!, making it divide 1 — impossible. This is why the congruence holds only for primes."
```

## Explainer

From your study of congruence properties, you know that when p is prime, every integer from 1 to p−1 has a **multiplicative inverse mod p** — a unique number in {1, ..., p−1} that multiplies with it to give 1. This is because gcd(a, p) = 1 for all such a. Wilson's theorem asks: what happens when you multiply all these numbers together? The answer, (p−1)! ≡ −1 (mod p), seems surprising at first, but the proof emerges naturally once you pair each number with its inverse.

The key observation is that most elements in {1, 2, ..., p−1} pair up with a distinct inverse. For example, mod 7: 2 pairs with 4 (since 2·4 = 8 ≡ 1), 3 pairs with 5 (since 3·5 = 15 ≡ 1). Each such pair contributes a factor of 1 to the product. The only elements that are **self-inverse** — satisfying a² ≡ 1 (mod p), i.e., a ≡ ±1 (mod p) — are 1 and p−1 (which is −1 mod p). So when you form the product (p−1)!, all the middle terms cancel in pairs to 1, leaving just 1·(p−1) = p−1 ≡ −1 (mod p). That is the entire proof.

The biconditional is what makes Wilson's theorem a **characterization** of primes, not just a property of them. If n is composite, say n = ab with 1 < a ≤ b < n, then a divides (n−1)! (since a appears as one of the factors in the product), which means a also divides any multiple of (n−1)!. But if (n−1)! ≡ −1 (mod n) were true, then n would divide (n−1)! + 1, and since a divides n it would also divide (n−1)! + 1 — yet a already divides (n−1)!, so a would divide 1, a contradiction. This is why the congruence fails for composite n.

The practical limitation is obvious: computing (p−1)! for large p is astronomically expensive, making this useless as a primality test in practice. But its theoretical value is real. It gives an exact algebraic fingerprint of primality — a number is prime if and only if its "factorial residue" hits −1. It also previews deeper structure: the fact that the only self-inverse elements mod p are ±1 is a consequence of the multiplicative group (ℤ/pℤ)* being a **cyclic group** of order p−1, a result that underpins Fermat's little theorem and Euler's theorem, which you will study next.
