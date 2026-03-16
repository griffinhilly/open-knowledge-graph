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
status: draft
---

# p-adic Valuation

## Core Idea
The p-adic valuation v_p(n) is the exponent of p in n's factorization: v_p(p^e · m) = e when gcd(p,m) = 1. Extending multiplicatively to rationals via v_p(a/b) = v_p(a) - v_p(b), it assigns 'distance to zero' based on powers of p.

## Explainer

Start from the Fundamental Theorem of Arithmetic, which you know: every integer factors uniquely into primes. For any prime p and any positive integer n, there is a specific non-negative integer recording "how many times p divides n." The **p-adic valuation** v_p(n) is exactly that exponent. For p = 2: v_2(12) = 2 because 12 = 2² · 3. For p = 3: v_3(12) = 1. For p = 5: v_5(12) = 0, since 5 does not divide 12. The valuation simply reads off a specific prime-exponent from the factorization.

The definition extends naturally to positive rationals via v_p(a/b) = v_p(a) − v_p(b). So v_2(3/4) = v_2(3) − v_2(4) = 0 − 2 = −2. A negative valuation means the prime appears in the denominator. This extension is consistent because unique factorization tells us every rational has a well-defined prime decomposition with possibly negative exponents, and the valuation reads off the p-component. Crucially, v_p is **completely additive**: v_p(ab) = v_p(a) + v_p(b) for all nonzero rationals a and b. Multiplication in the rationals becomes addition in the valuations — exactly like a logarithm, but tracking divisibility rather than magnitude.

The key conceptual shift is using the valuation to define a **p-adic absolute value**: |x|_p = p^{−v_p(x)}, with |0|_p = 0. Under this notion of size, numbers are "small" when they are highly divisible by p. For instance, |1000|_2 = 2^{−3} = 1/8, because 1000 = 2³ · 125 is divisible by 2³. The integer 1000 is p-adically small for p = 2 and p = 5 — the opposite of what usual magnitude would say. This reframes arithmetic: "closeness to zero" is measured by how much of p goes into a number, not by how small the number is on the number line.

This p-adic absolute value satisfies an even stronger property than the usual triangle inequality, called the **ultrametric inequality**: |x + y|_p ≤ max(|x|_p, |y|_p). Two p-adically small numbers sum to something p-adically small or smaller. This unusual geometry — where every triangle is isoceles and every point in an open ball is a center — is the seed from which the p-adic numbers ℚ_p grow. The p-adic numbers are the completion of ℚ under the p-adic absolute value, exactly as the real numbers are the completion of ℚ under the usual absolute value. The p-adic valuation is the precise tool that makes this alternative arithmetic universe accessible.
