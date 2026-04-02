---
id: carmichael-function-and-numbers
title: Carmichael Function and Carmichael Numbers
domain: mathematics
course: discrete-math
prerequisites:
- id: euler-totient-function
  type: hard
- id: fermat-little-theorem
  type: soft
tags:
- number-theory
- carmichael
- prime-testing
stage: advanced
status: validated
---

# Carmichael Function and Carmichael Numbers

## Core Idea
The Carmichael function λ(n) is the exponent of the multiplicative group modulo n. Carmichael numbers are composite numbers n where aⁿ⁻¹ ≡ 1 (mod n) for all a coprime to n, making them pseudoprimes to all bases. Understanding them is essential for probabilistic primality testing.

## Questions

```yaml
- question: "A primality testing program uses Fermat's test with base a = 2 and declares 561 to be prime because 2^560 ≡ 1 (mod 561). Why is this conclusion wrong, and what does this reveal about Fermat's test?"
  type: multiple-choice
  options:
    - "The program computed the modular exponentiation incorrectly; 2^560 ≢ 1 (mod 561)"
    - "561 = 3 × 7 × 11 is composite, and as a Carmichael number it satisfies Fermat's condition for every coprime base — not just base 2 — making single-base Fermat testing fundamentally unreliable"
    - "Fermat's test only applies to numbers that are products of exactly two primes; 561 has three prime factors so a different test is needed"
    - "The computation is correct and 561 is prime; Carmichael numbers are a theoretical curiosity with no real examples below 10,000"
  answer: 1
  explanation: "561 = 3 × 7 × 11 is indeed composite, and 2^560 ≡ 1 (mod 561) is correct — it really does pass. The problem is that 561 passes for every base coprime to it, not just base 2. λ(561) = lcm(λ(3), λ(7), λ(11)) = lcm(2, 6, 10) = 30, and 30 | 560 = n−1, so a^560 = (a^30)^(56/3)... more precisely: since λ(561)|560, a^560 ≡ 1 for all a coprime to 561. Increasing the number of bases tested does not help — all pass. This is exactly the attack on Fermat's test that Miller-Rabin was designed to address."

- question: "Why is the Carmichael function λ(n) sometimes strictly less than Euler's totient φ(n)?"
  type: multiple-choice
  options:
    - "λ(n) counts only the prime elements of the multiplicative group, while φ(n) counts all elements coprime to n"
    - "φ(n) gives the size of the multiplicative group (ℤ/nℤ)×; λ(n) gives its exponent — the smallest power that sends every element to 1 — which can be smaller when the group's structure is not cyclic"
    - "λ(n) = φ(n) for all positive integers; apparent differences arise from computation errors or misapplication of the formulas"
    - "φ(n) includes non-coprime elements that λ(n) correctly excludes, inflating φ(n) above λ(n)"
  answer: 1
  explanation: "φ(n) counts the elements of (ℤ/nℤ)×. Every element a satisfies a^φ(n) ≡ 1, because the order of any element divides the group size. But the group may not be cyclic — it may decompose into components whose orders don't share a common factor close to φ(n). λ(n) = lcm of orders of all elements = the exponent of the group, which is ≤ φ(n) and can be a proper divisor. For λ(12) = 2 while φ(12) = 4: every element of (ℤ/12ℤ)× satisfies a² ≡ 1, even though the group has 4 elements."

- question: "The Korselt criterion states that a squarefree composite n is Carmichael if and only if (p−1) | (n−1) for every prime p dividing n. This condition directly ensures λ(n) | (n−1), making n pass Fermat's test for all coprime bases."
  type: true-false
  answer: true
  explanation: "For a squarefree n = p₁ · p₂ · ... · pₖ, the Carmichael function is λ(n) = lcm(p₁−1, p₂−1, ..., pₖ−1). Korselt's condition (p−1)|(n−1) for every prime p|n means each (pᵢ−1) divides n−1. Since λ(n) = lcm of these factors and each factor divides n−1, their lcm also divides n−1 — so λ(n)|(n−1). Then for any a coprime to n, a^λ(n) ≡ 1 (mod n), so a^(n−1) = (a^λ(n))^((n−1)/λ(n)) ≡ 1^k = 1. Every valid base passes Fermat's test."

- question: "Because Carmichael numbers are extremely rare among large integers, Fermat's primality test is considered a reliable probabilistic test for cryptographic purposes — Miller-Rabin offers no meaningful improvement in practice."
  type: true-false
  answer: false
  explanation: "Infinitely many Carmichael numbers exist (proved by Alford, Granville, and Pomerance in 1994), and they are dense enough that probabilistic Fermat testing is not considered cryptographically reliable. More importantly, Fermat's test can be fooled by a single Carmichael number regardless of how many bases are tested — all coprime bases pass. Miller-Rabin closes this gap by checking additional conditions (whether n is a strong probable prime) that Carmichael numbers cannot satisfy for all bases. No Carmichael number can fool Miller-Rabin with all possible bases, making it the standard for probabilistic primality testing."

- question: "Explain why Carmichael numbers break Fermat's primality test, using the relationship between λ(n), φ(n), and the Fermat condition."
  type: short-answer
  answer: "Fermat's little theorem guarantees a^(p−1) ≡ 1 (mod p) when p is prime. The test checks the contrapositive: if a^(n−1) ≢ 1, n is composite. A Carmichael number n is composite but satisfies a^(n−1) ≡ 1 (mod n) for every a coprime to n. The reason: λ(n) | (n−1), where λ(n) is the exponent of the multiplicative group — the smallest m such that a^m ≡ 1 for all coprime a. Since every element order divides λ(n) and λ(n) divides n−1, a^(n−1) = 1 for all coprime a. The number masquerades as having the multiplicative structure of a prime. Fermat's test cannot distinguish this case because it only checks one congruence; Miller-Rabin adds witnesses that composite numbers — even Carmichael numbers — cannot satisfy for all choices."
  explanation: "The key insight is that Fermat's test is a necessary but not sufficient condition for primality: a prime must pass, but not everything that passes is prime. Carmichael numbers are exactly the composite exceptions. Understanding why they exist — λ(n) | (n−1) despite n being composite — requires understanding the relationship between group exponent (λ) and group size (φ), and why a composite group can have a small exponent relative to its size."
```

## Explainer

You already know Euler's totient function φ(n), which counts how many integers from 1 to n are coprime to n. You also know that for any such integer a, the multiplicative order of a modulo n divides φ(n) — meaning a^φ(n) ≡ 1 (mod n). But φ(n) is often larger than necessary: it counts elements, but what you really want is the smallest exponent that works for *all* of them simultaneously. That smaller value is the **Carmichael function** λ(n), defined as the **exponent** of the multiplicative group (ℤ/nℤ)×.

Concretely, λ(n) is the least positive integer m such that a^m ≡ 1 (mod n) for every a coprime to n. For prime p, λ(p) = p−1 = φ(p), so nothing changes. For prime powers and composites, λ(n) can be a proper divisor of φ(n). For example, λ(12) = 2 even though φ(12) = 4, because every integer coprime to 12 satisfies a² ≡ 1 (mod 12). The formula for λ on prime powers is: λ(2) = 1, λ(4) = 2, λ(2^k) = 2^(k−2) for k ≥ 3, and λ(p^k) = p^(k−1)(p−1) for odd primes p. For composite n, λ(n) = lcm of λ over the prime-power factors.

Carmichael numbers arise from a subtle flaw in Fermat's primality test. Fermat's little theorem says a^(p−1) ≡ 1 (mod p) for all a coprime to p — so if this congruence *fails*, p is definitely composite. The test checks this as a primality certificate. A **Carmichael number** is a composite n that passes this test for *every* base a coprime to n: a^(n−1) ≡ 1 (mod n) for all gcd(a,n) = 1. The smallest example is 561 = 3 × 7 × 11. Because λ(561) = lcm(2, 6, 10) = 30 divides 560 = n−1, every valid base satisfies the Fermat condition — despite 561 being composite.

The **Korselt criterion** characterizes Carmichael numbers elegantly: a squarefree composite n is Carmichael if and only if (p−1) | (n−1) for every prime p dividing n. This directly connects the structure of Carmichael numbers to the Carmichael function: the condition guarantees λ(n) | (n−1). Infinitely many Carmichael numbers exist (proved by Alford, Granville, and Pomerance in 1994), which means Fermat's test alone is not a reliable primality test. Modern primality tests like Miller-Rabin specifically address this weakness by choosing bases adversarially and checking additional conditions that Carmichael numbers cannot satisfy for all bases.
