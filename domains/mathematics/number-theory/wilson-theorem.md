---
id: wilson-theorem
title: Wilson's Theorem
domain: mathematics
course: number-theory
prerequisites:
- id: modular-arithmetic
  type: hard
tags:
- modular-arithmetic
- primes
- factorials
- wilson
stage: advanced
status: draft
---

# Wilson's Theorem

## Core Idea
For a prime p, we have (p−1)! ≡ −1 (mod p). While elegant and providing a primality test, Wilson's theorem is computationally impractical for large primes compared to probabilistic tests. It exemplifies the beauty of elementary number theory and connects factorials to modular arithmetic.

## How It's Best Learned
Prove using the pairing of elements with their modular inverses in (ℤ/pℤ)*. Understand why non-primes violate this: for composite n > 4, n/2 pairs with itself.

## Common Misconceptions
Wilson's theorem only characterizes primes; (n−1)! ≡ −1 (mod n) fails for all composite n > 4. It is inefficient for primality testing compared to Fermat or Miller-Rabin tests.

## Questions

```yaml
- question: "A student wants to test whether a 500-digit number is prime using Wilson's theorem: compute (n−1)! mod n and check if it equals −1. A classmate says this is a valid but impractical primality test. Which response best explains the computational problem?"
  type: multiple-choice
  options:
    - "The test is invalid — Wilson's theorem only works for primes less than 100"
    - "The test is valid but requires computing a factorial with ~10^500 multiplications, making it exponentially slower than methods like Miller-Rabin"
    - "The test is valid and efficient because modular reduction keeps the numbers small throughout"
    - "The test is invalid for even numbers, but fast for odd candidates"
  answer: 1
  explanation: "Wilson's theorem gives an exact characterization of primes — (n−1)! ≡ −1 (mod n) if and only if n is prime — so the test is logically valid. The problem is computational: (n−1)! requires (n−2) multiplications, and n itself is exponentially large in its bit length. A 500-digit prime has roughly 10^500 multiplications to perform, making it laughably impractical. Fermat's little test and Miller-Rabin use modular exponentiation, which is polynomial in the bit length. Option C is the key misconception: while mod reduction does keep individual numbers small, it cannot reduce the number of operations needed."

- question: "In the proof of Wilson's theorem, why does the element p−1 not cancel with a distinct partner, and what role does this play in the final result?"
  type: multiple-choice
  options:
    - "p−1 is even, so it has no modular inverse"
    - "p−1 ≡ −1 (mod p), so (p−1)² ≡ 1 (mod p) — it is self-inverse and contributes the factor of −1 to (p−1)!"
    - "p−1 cancels with 1, leaving the middle terms to contribute −1"
    - "p−1 is the largest element, so it has no smaller element to pair with"
  answer: 1
  explanation: "The pairing argument pairs each element a in {1, ..., p−1} with its distinct multiplicative inverse a⁻¹. Most elements pair with a different element, contributing 1 to the product. The exceptions are the self-inverse elements where a ≡ a⁻¹, i.e., a² ≡ 1 (mod p). For a prime p, this equation has exactly two solutions: a ≡ 1 and a ≡ −1 ≡ p−1. So 1 and p−1 are left unpaired. Their product is 1 · (p−1) ≡ −1 (mod p), giving (p−1)! ≡ −1 (mod p)."

- question: "Wilson's theorem states that n is prime if and only if (n−1)! ≡ −1 (mod n). For composite n > 4, (n−1)! ≡ 0 (mod n) rather than −1."
  type: true-false
  answer: true
  explanation: "For composite n > 4, n has a proper factor d with 1 < d < n. Since d appears in {1, 2, ..., n−1} and n's factors appear multiple times in that product, n divides (n−1)!. So (n−1)! ≡ 0 (mod n), not −1. This is why the theorem provides a perfect if-and-only-if characterization of primes."

- question: "Because Wilson's theorem provides an exact test for primality, it is more reliable than probabilistic tests like Miller-Rabin, which only give probable primality."
  type: true-false
  answer: false
  explanation: "While Wilson's theorem is exact (no false positives or negatives), reliability in practice is not the same as mathematical exactness. Miller-Rabin is deterministic for all practical inputs (with multiple witnesses it has no false positives in the numbers we care about) and runs in polynomial time. Wilson's test requires computing a factorial with exponentially many steps, making it computationally useless for any large prime regardless of its theoretical exactness. Practical reliability favors the probabilistic tests overwhelmingly."

- question: "Why does the pairing argument in the proof of Wilson's theorem fail for composite numbers? What property of primes makes it work?"
  type: short-answer
  answer: "For prime p, every nonzero element in ℤ/pℤ has a unique multiplicative inverse because ℤ/pℤ is a field. This means the elements of {1, ..., p−1} can be paired with their distinct inverses, each pair contributing 1 to the product, leaving only the self-inverse elements 1 and p−1 = −1. For composite n, the integers mod n do not form a field — zero divisors exist, and some elements lack inverses. The factor d of n appears in {1, ..., n−1}, and n divides the product, so (n−1)! ≡ 0 (mod n). The clean cancellation that powers the proof depends entirely on the field structure, which only exists when the modulus is prime."
  explanation: "The key is that primality guarantees a field structure (every nonzero element has a unique inverse), which makes the pairing argument work perfectly. Compositeness introduces zero divisors and elements without inverses, breaking the pairing and forcing the product to 0 rather than −1."
```

## Explainer

From your work with modular arithmetic, you know that the integers mod p form a field when p is prime, which means every nonzero element has a unique multiplicative inverse mod p. Wilson's theorem exploits this structure to evaluate (p−1)! mod p in one elegant step. The key observation is that most elements in {1, 2, ..., p−1} can be paired with their distinct modular inverse. If a ≢ a⁻¹ (mod p), then a and a⁻¹ are two different elements that contribute a product of 1 to the factorial. So most of the product cancels in pairs, leaving only the **self-inverse** elements: those where a² ≡ 1 (mod p), i.e., a ≡ ±1 (mod p).

Since p is prime, the equation a² ≡ 1 (mod p) has exactly two solutions: a ≡ 1 and a ≡ −1 (mod p), which are 1 and p−1 respectively. Every other element in {2, 3, ..., p−2} pairs with a distinct inverse, and those pairs multiply to 1. So (p−1)! ≡ 1 · (paired terms all giving 1) · (p−1) ≡ p−1 ≡ −1 (mod p). The theorem is proved. For small primes, verify directly: 4! = 24 ≡ −1 (mod 5) ✓, and 6! = 720 ≡ −1 (mod 7) ✓.

Why does this fail for composite n? If n is composite, n has a factor d with 1 < d < n, so d appears in the list {1, 2, ..., n−1}. Since d | n and d | d, we get d | gcd(d, n) = d, but more importantly, n divides (n−1)! because the prime factors of n appear among {1, ..., n−1} (except when n = p² for a prime p, which is a minor special case). This means (n−1)! ≡ 0 (mod n) for most composite n, not −1. The theorem thus provides an exact characterization of primes: n is prime if and only if (n−1)! ≡ −1 (mod n).

The practical limitation is computational. Computing (p−1)! requires multiplying together (p−1) numbers, each of size up to p — an exponential number of operations in the bit length of p. A 1000-digit prime has roughly 10^{1000} in its factorial, making Wilson's test laughably slow compared to **Fermat's little test** (which needs only a modular exponentiation, polynomial in the bit length) or the Miller-Rabin test. Wilson's theorem is best appreciated as a theoretical gem: a perfect characterization of primeness that is simultaneously useless for practical computation. It illustrates a broader theme in number theory — elegant exact characterizations and efficient algorithms are often different things.
