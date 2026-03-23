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
status: validated
---

# Order of an Element Modulo n

## Core Idea
The order of a mod n (with gcd(a,n) = 1) is the smallest positive k such that a^k ≡ 1 (mod n). The order divides φ(n) by Lagrange's theorem, and equals φ(n) precisely when a is a primitive root.

## Questions

```yaml
- question: "You compute powers of 4 modulo 15 and find 4¹ ≡ 4, 4² ≡ 1 (mod 15), so the order of 4 mod 15 is 2. Note that φ(15) = 8. Which statement about 2 must be true by the theory?"
  type: multiple-choice
  options:
    - "2 must divide 15"
    - "2 must divide φ(15) = 8"
    - "2 must equal φ(15) = 8, since every element has order equal to φ(n)"
    - "2 must be the smallest prime factor of 15"
  answer: 1
  explanation: "The order of any element a modulo n always divides φ(n), by Lagrange's theorem: the powers of a form a cyclic subgroup of the multiplicative group (Z/nZ)*, and every subgroup's size divides the group's order. Here ord(4) = 2 and φ(15) = 8, and indeed 2 divides 8. Option C states the common misconception — that every element has order exactly φ(n). This is only true for primitive roots, which are special. Elements can have smaller orders that divide φ(n). Fermat's Little Theorem guarantees a^φ(n) ≡ 1, but φ(n) is an upper bound on the order's possible values, not the order itself."

- question: "Which of the following is TRUE about primitive roots modulo n?"
  type: multiple-choice
  options:
    - "Every positive integer n has at least one primitive root"
    - "An element a is a primitive root mod n if and only if its order equals φ(n) — meaning its successive powers cycle through every unit modulo n before returning to 1"
    - "A primitive root modulo n must itself be a prime number"
    - "Primitive roots exist only when n is prime"
  answer: 1
  explanation: "A primitive root is precisely an element whose order equals φ(n), the size of the full multiplicative group. Such an element generates the entire group — its powers {a, a², ..., a^φ(n) ≡ 1} produce every unit modulo n. For example, 3 mod 7 is a primitive root because its six powers give all nonzero residues mod 7. Option A is false: not every n has primitive roots — they exist for n = 1, 2, 4, p^k, and 2p^k (for odd prime p), but not, for example, mod 8 or mod 15. Option C is false: 3 is prime but 2 mod 7 is not a primitive root (order 3), so primeness is irrelevant."

- question: "If a^k ≡ 1 (mod n) for some positive integer k, then the order of a modulo n must divide k."
  type: true-false
  answer: true
  explanation: "This is a key divisibility property of the order. If d = ord_n(a), then a^k ≡ 1 (mod n) if and only if d divides k. The 'only if' direction: write k = qd + r with 0 ≤ r < d. Then a^k = (a^d)^q · a^r ≡ 1^q · a^r = a^r ≡ 1 (mod n), so a^r ≡ 1. Since r < d and d is the smallest positive exponent with a^d ≡ 1, we must have r = 0, meaning d | k. This fact has immediate practical use: knowing some exponent k that gives 1 immediately tells you the order divides k, restricting your search to divisors of k."

- question: "By Fermat's Little Theorem, the order of any element a modulo a prime p is exactly p − 1."
  type: true-false
  answer: false
  explanation: "Fermat's Little Theorem says a^(p−1) ≡ 1 (mod p) for gcd(a, p) = 1. This means the order of a *divides* p − 1, not that it *equals* p − 1. For example, mod 7: the order of 2 is 3 (since 2³ = 8 ≡ 1 mod 7), and the order of 6 is 2 (since 6² = 36 ≡ 1 mod 7), while p − 1 = 6. Only elements with order exactly p − 1 are primitive roots, and not every element is a primitive root. Confusing 'divides p−1' with 'equals p−1' is the most common error when first encountering order theory."

- question: "When searching for the order of a modulo n, why is it sufficient to check only the divisors of φ(n) rather than all integers from 1 to φ(n)?"
  type: short-answer
  answer: "The order of a modulo n always divides φ(n), by Lagrange's theorem: the powers of a form a cyclic subgroup of (Z/nZ)*, and subgroup sizes divide the group order φ(n). Since the order must be a divisor of φ(n), there is no need to check integers that don't divide φ(n) — they cannot be the order. For example, if φ(n) = 12, the possible orders are 1, 2, 3, 4, 6, or 12, so we check only these six values rather than all twelve. The strategy is to test the divisors of φ(n) in increasing order; the smallest k with a^k ≡ 1 (mod n) is the order."
```

## Explainer

From your work with Fermat's Little Theorem, you know that if p is prime and gcd(a, p) = 1, then a^(p−1) ≡ 1 (mod p). But the exponent p−1 might not be the *smallest* such exponent — the powers of a might reset to 1 even earlier. The **order** of a modulo n pins down exactly when this first reset happens.

Take a = 2 and n = 7. Compute: 2¹ ≡ 2, 2² ≡ 4, 2³ ≡ 1 (mod 7). The order of 2 mod 7 is 3. Now try a = 3 mod 7: 3¹ ≡ 3, 3² ≡ 2, 3³ ≡ 6, 3⁴ ≡ 4, 3⁵ ≡ 5, 3⁶ ≡ 1 (mod 7). The order of 3 is 6, which equals φ(7) = 6. That makes 3 a **primitive root** mod 7 — its powers cycle through all 6 nonzero residues before returning to 1.

The key structural fact is that the order of a always **divides** φ(n). This is an application of Lagrange's theorem from group theory: the powers of a form a cyclic subgroup of the units modulo n, and subgroup sizes always divide the group size. Practically, this means you only need to check divisors of φ(n) when hunting for the order — you never need to check all exponents up to φ(n). For example, if φ(n) = 12, the possible orders are 1, 2, 3, 4, 6, or 12.

The **order** concept connects congruence arithmetic to the deeper structure of multiplicative groups. An element with order equal to φ(n) is a primitive root, and its existence (or non-existence) determines the structure of the entire group of units modulo n. This distinction — between elements that generate the whole group and those that don't — is foundational for discrete logarithms and the cryptographic hardness assumptions underlying protocols like Diffie-Hellman key exchange.
