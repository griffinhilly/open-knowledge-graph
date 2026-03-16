---
id: dirichlet-series-and-l-functions
title: Dirichlet Series and L-Functions
domain: mathematics
course: number-theory
prerequisites:
- id: riemann-zeta-function-intro
  type: soft
builds-toward:
- primes-arithmetic-progressions
tags:
- dirichlet-series
- l-functions
- analytic-number-theory
stage: advanced
status: draft
---

# Dirichlet Series and L-Functions

## Core Idea
Dirichlet L-functions L(s, χ) = Σ χ(n)/n^s generalize the Riemann zeta function for Dirichlet characters χ. They satisfy functional equations and have Euler products, enabling study of primes in arithmetic progressions and other structured subsets of integers.

## Explainer

From the Riemann zeta function you already know that ζ(s) = Σ 1/n^s encodes deep arithmetic information, particularly about primes, via its Euler product ζ(s) = Π (1 − p^−s)^−1. A **Dirichlet series** is any series of the form Σ a(n)/n^s, and the zeta function is simply the case where a(n) = 1 for all n. The key insight of analytic number theory is to replace the constant sequence 1 with a richer arithmetic function — one that "sees" structure in the integers that 1 cannot detect.

A **Dirichlet character** χ mod q is a completely multiplicative, periodic function on the integers that is zero on integers sharing a common factor with q, and otherwise takes values that are roots of unity. The **principal character** χ₀ just assigns 1 to integers coprime to q and 0 otherwise, making L(s, χ₀) essentially ζ(s) with finitely many factors removed. Non-principal characters are the interesting ones: they "color" residues mod q differently, and the L-function L(s, χ) = Σ χ(n)/n^s becomes a weighted zeta function that selectively picks up integers according to their residue class. Because χ is completely multiplicative, L(s, χ) also factors into an Euler product L(s, χ) = Π_p (1 − χ(p)p^−s)^−1, one factor per prime.

The reason Dirichlet introduced these objects was to prove that every arithmetic progression a, a+q, a+2q, … with gcd(a, q) = 1 contains infinitely many primes — a statement you cannot prove by the same direct argument used for primes overall. The key is to show L(1, χ) ≠ 0 for all non-principal characters, which requires complex analysis. Think of it as follows: if you take a formal "average" of L(s, χ) over all characters mod q, the multiplicativity and orthogonality of characters cause most prime contributions to cancel — except for primes in the specific residue class a mod q. Showing these L-functions are nonzero at s = 1 is the heart of Dirichlet's theorem.

Like the Riemann zeta function, L-functions satisfy **functional equations** that relate L(s, χ) to L(1 − s, χ̄) (where χ̄ is the conjugate character), allowing analytic continuation to the whole complex plane. The analogue of the Riemann Hypothesis — that the non-trivial zeros of L(s, χ) all lie on the line Re(s) = 1/2 — is known as the **Generalized Riemann Hypothesis** (GRH), and most of analytic number theory would become considerably sharper if it were proved. Every result you will encounter about primes in arithmetic progressions and residue structure ultimately traces back to the non-vanishing and zero distribution of these L-functions.
