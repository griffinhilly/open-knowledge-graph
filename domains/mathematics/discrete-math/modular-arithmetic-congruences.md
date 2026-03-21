---
id: modular-arithmetic-congruences
title: Modular Arithmetic and Congruences
domain: mathematics
course: discrete-math
prerequisites: []
builds-toward:
- euclidean-algorithm-gcd
- chinese-remainder-theorem
tags:
- modular-arithmetic
- number-theory
stage: formal-systems
status: draft
---

# Modular Arithmetic and Congruences

## Core Idea
a ≡ b (mod n) if and only if n divides a - b. Modular arithmetic obeys addition, subtraction, and multiplication rules like standard arithmetic. Congruences partition the integers into residue classes, and arithmetic can be performed within these classes.

## Questions

```yaml
- question: "To compute 7¹⁰⁰ (mod 5), a student notes that 7 ≡ 2 (mod 5) and instead computes 2¹⁰⁰ (mod 5). What property of modular arithmetic justifies replacing 7 with 2?"
  type: multiple-choice
  options:
    - "Since 7 and 2 are in the same residue class mod 5, all arithmetic operations on them produce the same result mod 5"
    - "This substitution only works for exponents, not for addition or multiplication"
    - "This only works because 5 is prime"
    - "7 and 2 are both single-digit numbers, so the substitution happens to work in this case"
  answer: 0
  explanation: "The fundamental property of modular arithmetic is that congruent numbers behave identically in arithmetic operations. If a ≡ b (mod n), then aᵏ ≡ bᵏ (mod n) for any positive integer k — and the same holds for addition and multiplication. This holds for any modulus, not just primes, and for large numbers just as much as small ones. The entire power of modular arithmetic comes from this substitution principle: replacing large numbers with small residues before computing."

- question: "In Z/6Z (integers mod 6), which element has a multiplicative inverse, and why?"
  type: multiple-choice
  options:
    - "4, because 4 is even and even numbers pair nicely in mod 6"
    - "2, because 2 is small and divides 6"
    - "5, because gcd(5, 6) = 1, meaning 5 and 6 share no common factors"
    - "3, because 3 is half of 6"
  answer: 2
  explanation: "The modular inverse of a (mod n) exists if and only if gcd(a, n) = 1. In Z/6Z: gcd(2, 6) = 2, gcd(3, 6) = 3, gcd(4, 6) = 2 — none equal 1, so 2, 3, and 4 have no inverses. But gcd(5, 6) = 1, so 5 has an inverse: 5 × 5 = 25 ≡ 1 (mod 6), confirming 5⁻¹ ≡ 5 (mod 6). This is why prime moduli are preferred in cryptography — every nonzero element has an inverse."

- question: "13 ≡ 1 (mod 4)"
  type: true-false
  answer: true
  explanation: "13 − 1 = 12, and 12 is divisible by 4 (12 = 3 × 4). So 13 and 1 leave the same remainder when divided by 4 (both leave remainder 1), confirming 13 ≡ 1 (mod 4). Alternatively: 13 = 3 × 4 + 1, so the remainder is 1."

- question: "In modular arithmetic, if a × b ≡ 0 (mod n), then either a ≡ 0 (mod n) or b ≡ 0 (mod n)."
  type: true-false
  answer: false
  explanation: "This cancellation law holds for ordinary integers but fails for composite moduli. Counterexample: 2 × 3 = 6 ≡ 0 (mod 6), but 2 ≢ 0 (mod 6) and 3 ≢ 0 (mod 6). The elements 2 and 3 are called 'zero divisors' of Z/6Z. This is why prime moduli are important: when n is prime, Z/nZ has no zero divisors, and the cancellation property holds as expected."

- question: "Why does the modular inverse of a (mod n) only exist when gcd(a, n) = 1? Give an example illustrating what goes wrong when gcd(a, n) > 1."
  type: short-answer
  answer: "The modular inverse of a is a number x such that ax ≡ 1 (mod n), meaning ax − 1 is divisible by n, i.e., ax − ny = 1 for some integer y. By Bézout's identity, this equation has integer solutions if and only if gcd(a, n) divides 1, which requires gcd(a, n) = 1. When gcd(a, n) = d > 1, every value of ax − ny is divisible by d, so it can never equal 1. Example: try to find x with 4x ≡ 1 (mod 6). Every multiple of 4 is even, and 1 + 6k is odd for all k, so 4x can never equal 1 + 6k. No inverse exists because gcd(4, 6) = 2."
  explanation: "This is why cryptographic systems like RSA use prime moduli or carefully chosen composite moduli — the need for every nonzero element to have an inverse is essential for encryption and decryption to work. When the modulus is prime, gcd(a, p) = 1 for all nonzero a, so every element is invertible."
```

## Explainer

Think of a clock. After 12 hours, the clock resets — 13 o'clock is the same position as 1 o'clock. This is modular arithmetic in action: 13 ≡ 1 (mod 12) because 12 divides 13 − 1 = 12. The notation a ≡ b (mod n) simply means that a and b leave the same remainder when divided by n, or equivalently that n divides a − b. Every integer belongs to exactly one **residue class** modulo n, represented by its remainder: 0, 1, 2, ..., n − 1. Instead of working with all integers, you work with these n classes.

The power of modular arithmetic comes from its **closure under operations**. If a ≡ b (mod n) and c ≡ d (mod n), then a + c ≡ b + d (mod n) and a × c ≡ b × d (mod n). This means you can reduce numbers before performing operations and still get the right answer modulo n. For example, to compute 99 × 101 (mod 10), note that 99 ≡ 9 and 101 ≡ 1 (mod 10), so the product is ≡ 9 × 1 = 9 (mod 10). The actual product 9,999 also ends in 9 — confirming the calculation. This reduction trick makes modular arithmetic essential in cryptography and computer science, where numbers can be astronomically large.

Division works differently in modular arithmetic. You cannot always divide — you need a **modular inverse**. The inverse of a modulo n exists if and only if gcd(a, n) = 1; when it exists, a⁻¹ is the unique x with ax ≡ 1 (mod n). For example, 3 × 5 = 15 ≡ 1 (mod 7), so 3⁻¹ ≡ 5 (mod 7). When n is prime, every nonzero element has an inverse, making the residue classes modulo a prime into a complete arithmetic system (a field). This is why prime moduli appear everywhere in cryptographic protocols.

A powerful shortcut for large powers is **modular exponentiation**. To compute 2¹⁰⁰ (mod 13), you don't multiply 100 times. Instead, repeatedly square and reduce: 2² = 4, 2⁴ ≡ 3, 2⁸ ≡ 9, 2¹⁶ ≡ 3 (mod 13), and so on, then combine. This connects to Fermat's Little Theorem: if p is prime and p does not divide a, then aᵖ⁻¹ ≡ 1 (mod p). So 2¹² ≡ 1 (mod 13), meaning powers of 2 cycle with period dividing 12 modulo 13. Modular arithmetic transforms intractable arithmetic on huge numbers into manageable computation on small residues.
