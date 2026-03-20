---
id: riemann-zeta-function-intro
title: Introduction to the Riemann Zeta Function
domain: mathematics
course: number-theory
prerequisites:
- id: distribution-of-primes
  type: soft
builds-toward:
- dirichlet-series-and-l-functions
tags:
- riemann-zeta
- analytic-number-theory
- special-functions
stage: advanced
status: draft
---

# Introduction to the Riemann Zeta Function

## Core Idea
The Riemann zeta function ζ(s) = Σₙ₌₁^∞ 1/nˢ converges for Re(s) > 1 and extends via analytic continuation to the entire complex plane (with a simple pole at s = 1). Its Euler product representation ζ(s) = ∏_p (1 − p⁻ˢ)⁻¹ reveals the deep connection between the zeta function and prime numbers. The distribution of primes is governed by the location of ζ's zeros: the prime number theorem follows from the fact that ζ has no zeros on the line Re(s) = 1. The Riemann Hypothesis—asserting that all non-trivial zeros lie on Re(s) = 1/2—remains one of the greatest unsolved problems in mathematics.

## How It's Best Learned
Start by computing partial sums of ζ(2) = π²/6 to see convergence, then study the Euler product for small primes to understand why prime factorization makes the product work. The connection to primes becomes concrete before the analytic continuation adds complexity.

## Common Misconceptions
The zeta function is not defined by the series Σ 1/nˢ for all s—that series diverges for Re(s) ≤ 1. Statements like "ζ(−1) = −1/12" refer to the analytic continuation, not to summing 1 + 2 + 3 + .... Students must distinguish the series from its continuation.

