---
id: p-adic-valuation
title: p-adic Valuation
domain: mathematics
course: number-theory
prerequisites:
- id: fundamental-theorem-arithmetic-rigorous
  type: hard
builds-toward:
- introduction-p-adic-numbers
tags:
- p-adic-valuation
- valuations
- primes
stage: advanced
status: validated
---

# p-adic Valuation

## Core Idea
The p-adic valuation v_p(n) is the exponent of p in n's factorization: v_p(p^e · m) = e when gcd(p,m) = 1. Extending multiplicatively to rationals via v_p(a/b) = v_p(a) - v_p(b), it assigns 'distance to zero' based on powers of p.

## Questions

```yaml
- question: "A student calculates v₂(12) = 2 (since 12 = 2²·3) and v₂(1000) = 3 (since 1000 = 2³·125), then concludes that 12 is 2-adically closer to zero than 1000 because 12 is smaller in magnitude. Is this correct?"
  type: multiple-choice
  options:
    - "Yes — the p-adic valuation preserves the ordinary ordering of integers"
    - "No — higher valuation means larger p-adic absolute value, so both conclusions are wrong"
    - "No — higher valuation means smaller p-adic absolute value, so 1000 is 2-adically closer to zero than 12"
    - "It depends on which prime p is chosen"
  answer: 2
  explanation: "The p-adic absolute value is |x|_p = p^{−v_p(x)}. Since v₂(1000) = 3 > v₂(12) = 2, we get |1000|₂ = 2⁻³ = 1/8 < |12|₂ = 2⁻² = 1/4. So 1000 is 2-adically closer to zero than 12, despite being larger in ordinary magnitude. The p-adic world inverts intuition: 'large' numbers (that are highly divisible by p) are p-adically 'small.'"

- question: "The p-adic valuation v_p satisfies v_p(ab) = v_p(a) + v_p(b) for all nonzero rationals. This property makes the valuation analogous to which familiar function?"
  type: multiple-choice
  options:
    - "A polynomial — it counts the degree of divisibility by p"
    - "A logarithm — multiplication in the domain becomes addition in the range"
    - "An exponential — the values grow rapidly with the number of prime factors"
    - "A modular arithmetic function — values cycle through a fixed period"
  answer: 1
  explanation: "Just as log(ab) = log(a) + log(b), we have v_p(ab) = v_p(a) + v_p(b). Both functions convert multiplication to addition. The analogy goes further: v_p is 'log base p of the p-part of a number.' This additive structure is what makes the valuation so algebraically tractable and is what allows the p-adic absolute value to satisfy the ultrametric inequality."

- question: "In the 5-adic absolute value, the integer 5,000,000 is 'closer to zero' than the integer 7."
  type: true-false
  answer: true
  explanation: "5,000,000 = 5⁶ · 2⁶, so v₅(5,000,000) = 6 and |5,000,000|₅ = 5⁻⁶ ≈ 0.000064. For 7, v₅(7) = 0 and |7|₅ = 1. So |5,000,000|₅ << |7|₅, meaning 5,000,000 is far closer to zero in the 5-adic metric. This is the central conceptual reversal: p-adic 'smallness' measures divisibility by p, not magnitude on the number line."

- question: "The p-adic absolute value satisfies primarily the ordinary triangle inequality |x + y|_p ≤ |x|_p + |y|_p, just like the usual absolute value."
  type: true-false
  answer: false
  explanation: "The p-adic absolute value satisfies the strictly stronger ultrametric inequality: |x + y|_p ≤ max(|x|_p, |y|_p). Since max(a, b) ≤ a + b, the ultrametric inequality implies the ordinary triangle inequality, but not vice versa. The ultrametric inequality has unusual geometric consequences: every triangle in the p-adic metric is isoceles, and every point in an open ball is a center. This is what makes p-adic geometry so different from real analysis."

- question: "Why does the p-adic valuation define a notion of 'size' in which large integers can be p-adically small?"
  type: short-answer
  answer: "Because p-adic size measures how divisible a number is by p, not its magnitude. A number like 2^100 is 2-adically tiny (|2^100|₂ = 2^{-100}) even though it is astronomically large ordinarily. The valuation extracts one specific prime-exponent from the factorization and treats it as the sole measure of closeness to zero — an assignment orthogonal to ordinary magnitude."
  explanation: "The Fundamental Theorem of Arithmetic guarantees a unique factorization, and the p-adic valuation simply reads off one coordinate of that factorization. Different primes give different 'lenses' on the integers, each measuring a different kind of divisibility. None of them corresponds to ordinary magnitude, which is why p-adic geometry is genuinely different geometry, not just a rescaling of the familiar number line."
```

## Explainer

Start from the Fundamental Theorem of Arithmetic, which you know: every integer factors uniquely into primes. For any prime p and any positive integer n, there is a specific non-negative integer recording "how many times p divides n." The **p-adic valuation** v_p(n) is exactly that exponent. For p = 2: v_2(12) = 2 because 12 = 2² · 3. For p = 3: v_3(12) = 1. For p = 5: v_5(12) = 0, since 5 does not divide 12. The valuation simply reads off a specific prime-exponent from the factorization.

The definition extends naturally to positive rationals via v_p(a/b) = v_p(a) − v_p(b). So v_2(3/4) = v_2(3) − v_2(4) = 0 − 2 = −2. A negative valuation means the prime appears in the denominator. This extension is consistent because unique factorization tells us every rational has a well-defined prime decomposition with possibly negative exponents, and the valuation reads off the p-component. Crucially, v_p is **completely additive**: v_p(ab) = v_p(a) + v_p(b) for all nonzero rationals a and b. Multiplication in the rationals becomes addition in the valuations — exactly like a logarithm, but tracking divisibility rather than magnitude.

The key conceptual shift is using the valuation to define a **p-adic absolute value**: |x|_p = p^{−v_p(x)}, with |0|_p = 0. Under this notion of size, numbers are "small" when they are highly divisible by p. For instance, |1000|_2 = 2^{−3} = 1/8, because 1000 = 2³ · 125 is divisible by 2³. The integer 1000 is p-adically small for p = 2 and p = 5 — the opposite of what usual magnitude would say. This reframes arithmetic: "closeness to zero" is measured by how much of p goes into a number, not by how small the number is on the number line.

This p-adic absolute value satisfies an even stronger property than the usual triangle inequality, called the **ultrametric inequality**: |x + y|_p ≤ max(|x|_p, |y|_p). Two p-adically small numbers sum to something p-adically small or smaller. This unusual geometry — where every triangle is isoceles and every point in an open ball is a center — is the seed from which the p-adic numbers ℚ_p grow. The p-adic numbers are the completion of ℚ under the p-adic absolute value, exactly as the real numbers are the completion of ℚ under the usual absolute value. The p-adic valuation is the precise tool that makes this alternative arithmetic universe accessible.
