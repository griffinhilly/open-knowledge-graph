---
id: primes-arithmetic-progressions
title: Primes in Arithmetic Progressions (Dirichlet's Theorem)
domain: mathematics
course: number-theory
prerequisites:
- id: dirichlet-series-and-l-functions
  type: hard
tags:
- dirichlet-theorem
- arithmetic-progressions
- primes
stage: advanced
status: draft
---

# Primes in Arithmetic Progressions (Dirichlet's Theorem)

## Core Idea
Dirichlet's theorem states that if gcd(a, q) = 1, the arithmetic progression a, a+q, a+2q, ... contains infinitely many primes with asymptotic density 1/φ(q). The proof uses non-vanishing of L(1, χ) and represents a major application of analytic number theory to elementary problems.

## Explainer

The question sounds elementary: among the infinitely many integers in an arithmetic progression like 1, 5, 9, 13, 17, ..., do infinitely many happen to be prime? The answer — yes, whenever the common difference and first term share no factor — was proved by Dirichlet in 1837, but the proof required tools far beyond elementary number theory. Understanding it connects your knowledge of Dirichlet series and L-functions to a concrete structural claim about primes.

The strategy mirrors Euler's proof that there are infinitely many primes overall. Euler observed that the divergence of Σ1/p (summing over primes) can be derived from the product formula for the Riemann zeta function ζ(s) = Πₚ(1 − p^−s)^−1. To isolate primes in a specific residue class mod q, Dirichlet introduced **Dirichlet characters** χ mod q — completely multiplicative functions that are periodic mod q and orthogonal to one another. These characters act like indicator functions: using the orthogonality relation Σ_{χ} χ(a)^{-1} χ(n) = φ(q) when n ≡ a (mod q) and 0 otherwise, you can isolate the contribution of primes in any given residue class.

This produces a sum involving **Dirichlet L-functions** L(s, χ) = Σ_{n=1}^∞ χ(n)/n^s. Like ζ(s), each L-function has an Euler product over primes, and the behavior near s = 1 controls whether the corresponding sum of 1/p over primes in the residue class diverges. For the principal character χ₀, L(s, χ₀) essentially equals ζ(s) up to a finite factor and therefore diverges as s → 1. For non-principal characters, the crucial step is showing L(1, χ) ≠ 0. If any L(1, χ) were zero, the contribution from the target residue class would be finite — meaning only finitely many primes in that class — contradicting the full divergence when all characters are combined. The non-vanishing proof is the technical heart of the theorem and the point where complex analysis becomes unavoidable.

The **asymptotic density** result is equally important: primes are equidistributed among all φ(q) valid residue classes mod q, each class containing 1/φ(q) of all primes (in the sense of natural density). For example, among all primes, exactly half are ≡ 1 (mod 4) and half ≡ 3 (mod 4) — primes ending in digit 1 and digit 3 in base 4 occur with equal frequency. This equidistribution is a deep regularity hidden behind the apparent irregularity of primes, and it is the prototype for more general equidistribution results in analytic number theory including the Chebotarev density theorem.
