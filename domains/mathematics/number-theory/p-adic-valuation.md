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
