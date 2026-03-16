---
id: primes-arithmetic-progressions-dirichlet
title: Primes in Arithmetic Progressions (Dirichlet's Theorem)
domain: mathematics
course: number-theory
prerequisites:
- id: dirichlet-series-l-functions
  type: hard
- id: congruence-properties
  type: hard
tags:
- dirichlet-theorem
- primes
- arithmetic-progressions
- analytic-number-theory
stage: advanced
status: draft
---

# Primes in Arithmetic Progressions (Dirichlet's Theorem)

## Core Idea
If gcd(a,d) = 1, there are infinitely many primes p ≡ a (mod d). The proof uses Dirichlet characters and L-functions, showing primes equidistribute among allowed residue classes.

## Explainer

Start with a basic observation from your study of congruences: the integers modulo d split into residue classes 0, 1, 2, ..., d−1. Some of these classes cannot contain primes other than d itself — for example, class 0 mod d contains only multiples of d, and class 0 mod 6 contains multiples of 6, which are composite. But what about the classes that *could* contain primes? Is it possible that primes, becoming sparser as you go higher, all eventually pile into one residue class and avoid the others?

Dirichlet's Theorem answers this decisively: if gcd(a, d) = 1 — that is, if a and d share no common factor — then the arithmetic progression a, a+d, a+2d, a+3d, ... contains infinitely many primes. The condition gcd(a, d) = 1 is exactly the right condition: if gcd(a, d) = k > 1, then every element of the progression is divisible by k, so only finitely many (if any) can be prime. Beyond this, though, Dirichlet guarantees primes spread out across all the "eligible" residue classes — not just some of them.

The proof strategy draws on the Dirichlet series and L-functions you've studied. The key tool is **Dirichlet characters** — completely multiplicative functions χ: ℤ → ℂ that are periodic mod d and encode information about residue classes. From these characters, Dirichlet constructed **L-functions** L(s, χ) = ∑ χ(n)/n^s, analytic relatives of the Riemann zeta function. The central step of the proof shows that log(number of primes ≤ x in the progression a mod d) grows like (1/φ(d)) · log log x, where φ(d) is Euler's totient — the count of residue classes coprime to d. Since this diverges, there must be infinitely many such primes.

A stronger result, the **Prime Number Theorem for Arithmetic Progressions**, refines this: among primes up to x, approximately x/(φ(d) · ln x) lie in each eligible class mod d. Primes don't just appear infinitely often in each valid class — they appear *equally often* in the long run, a phenomenon called **equidistribution**. This is remarkable: the primes, despite their irregular individual behavior, are perfectly democratic among residue classes when viewed in aggregate.

The key technical ingredient is proving that L(1, χ) ≠ 0 for all non-principal characters χ. This is where Dirichlet's original proof was subtle — he had to show the L-function doesn't vanish at s = 1, which would collapse the divergence argument. The non-vanishing at s = 1 is what separates Dirichlet's theorem from a near-theorem, and it requires using the full multiplicative structure of Dirichlet characters rather than any single character in isolation. This interplay between number-theoretic structure (congruences) and analytic tools (L-functions) is the hallmark of analytic number theory.
